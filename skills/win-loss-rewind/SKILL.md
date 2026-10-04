---
name: win-loss-rewind
description: Build an outcome-backward ICP. Works backward from real customer outcomes (won, lost, healthy, churned, expanded) to find the operational situations 6-18 months pre-purchase that actually predict who buys and stays, then ships a per-archetype scoring rubric validated on a 20% holdout. Use when you have an outcome-labeled customer list and need a situational ICP, not a firmographic filter. Based on Jordan Crawford's win-loss-rewind method (Blueprint GTM). Not for firmographic top-25%-by-revenue scoring (that is the anti-pattern this skill exists to stop), and not for a quick interview-based ICP (icp-agent).
---

# Win-Loss Rewind

Outcome-backward ICP discovery. Based on Jordan Crawford's `win-loss-rewind` method ([Blueprint GTM](https://blueprintgtm.com)), rewritten in our own words with a deterministic lift and holdout toolkit.

**The thesis:** A firmographic ICP ("HC 100-500, vertical X") is a database filter with a strategy label on it. It does not predict purchase. The companies that write the biggest checks and stay longest share a *situation*: a specific operational thing that happened to them 6-18 months before they bought, that almost nobody else on the filter is going through right now. This skill reconstructs that situation from the customers you already have.

**What it produces:** a `discriminator.md` per archetype (signal, source, threshold, weight, train lift, holdout lift, combined `fit_score` formula, looks-like-archetype threshold) plus a runnable `score_prospect.py` that scores a new domain against every archetype.

---

## Hard prerequisite: outcome-labeled customer data

This skill **cannot run** on a prospect list, a TAM export, or a "top 25% by company revenue" proxy. It needs the company's actual book of business with an outcome label per account. If you only have firmographic prospect data, stop and run the intake (`templates/intake-checklist.md`) to request the right export first. Using revenue-as-proxy is the exact anti-pattern this skill exists to kill.

**Minimum required input (one row per account):**

| Field | Required | Notes |
|-------|----------|-------|
| `company_name` | yes | identity |
| `domain` | yes | the join key for all enrichment |
| `outcome` | yes | one of: `won`, `lost`, `healthy`, `churned`, `expanded` |
| `outcome_date` | strongly preferred | so we can look back 6-18mo *before* it |
| call transcripts / notes | optional | feeds Phase 4 pain themes; if absent, Phase 4 degrades gracefully |

Outcome comes from the CRM export of the company whose ICP you are building. If you are an agency, note that your own CRM holds your deals with that client, not the client's customers, so the export must come from the client's CRM. See the intake checklist.

---

## Working rules (read before running)

1. **LLM steps run as sub-agents.** Cluster naming (Phase 3), theme extraction (Phase 4) and hypothesis generation (Phase 5) each spawn a sub-agent of your coding agent. Do not write Python that calls a model API from inside the math path.
2. **Deterministic-first enrichment.** Every paid API call must justify why a free deterministic step could not do it first. For page reads: a plain HTML-to-text fetch plus regex before a paid scraper. Run the paid scraper only on the residual.
3. **Bring your own providers.** `reference/enrichment-providers.md` maps each signal type to the kind of provider that carries it. Use whatever enrichment stack you already pay for.
4. **Lift, holdout, clustering, and significance are deterministic.** `pandas` + `scikit-learn` + `scipy.stats`. No LLM in the math path.

---

## The 8 phases

Run sequentially. Phase 0 and Phase 6 are the two non-negotiable phases: skip Phase 0 and you train on garbage, skip Phase 6 and you ship coincidences.

```
0  Data archaeology      → data_confidence.md (operator approves before anything else)
1  Pull and normalize    → unified per-account panel keyed by domain + 20% holdout split
2  Enrich panel          → operational feature matrix (NO firmographics)
3  Auto-segment          → named archetypes (min cluster size 5)
4  Pull pain themes       → theme corpus per archetype
5  Generate hypotheses    → candidate signals through 5 hard gates
6  Backcast and validate  → train + holdout lift; kill coincidences
7  Compose discriminator  → discriminator.md per archetype + score_prospect.py
```

Outputs live in `win-loss-rewind/` in your working directory.

---

### Phase 0: Data archaeology

**Purpose:** Distrust the data before trusting it. A CRM record that says "$50K healthy, expansion in flight" is sometimes a one-person shop with a dead website that auto-renewed once. You cannot build a discriminator on poisoned labels.

**Process:**
1. For every account, cross-reference the CRM label against external reality:
   - Does the domain resolve and serve a real page? (plain HTML-to-text fetch first, paid scraper on the residual)
   - Does the LinkedIn company page exist and look active? (any LinkedIn company data provider)
   - Does claimed headcount roughly match external headcount?
2. Quarantine any row where the label and reality conflict (dead site, ghost LinkedIn, headcount off by >5x, duplicate of another account).
3. Write `data_confidence.md` (use `templates/data_confidence.md`): total rows, quarantined rows with reason, confidence tier per outcome bucket.
4. **Stop and get operator approval.** Do not proceed until the operator signs off on the quarantine list.

**Triage rule:** If Phase 0 quarantines **more than 30%** of records, CRM hygiene is the problem, not the ICP. Report that and stop. Fixing the export comes before running the skill.

---

### Phase 1: Pull and normalize

**Purpose:** One clean panel, one join key, holdout carved out at the very start.

**Process:**
1. Build a unified per-account panel keyed by `domain` (normalize: lowercase, strip www, strip protocol). Dedupe by domain.
2. Define the **binary outcome** per analysis. The discriminator is "looks like a good-fit customer", so positive = `won` + `healthy` + `expanded`, negative = `lost` + `churned`. (You can also run per-archetype later.)
3. **Strip outcome-leakage columns now**, before anything downstream sees them: `arr`, `acv`, `deal_size`, `close_date`, `stage`, `nps`, `csm_assigned`, seat count, plan tier, and anything that exists *because* the customer bought. If the discriminator uses these, it predicts the past.
4. **Carve out a 20% holdout, stratified by outcome, with a fixed seed.** Persist the split as a column. Nothing in Phases 3-5 may look at holdout rows. This is the single most important line in the whole skill.

```python
from sklearn.model_selection import train_test_split
train, holdout = train_test_split(panel, test_size=0.20, stratify=panel["outcome"], random_state=42)
```

If any outcome bucket has fewer than ~20 accounts, note that the holdout will be thin (<4 per cluster) and lift on it will be noisy. Report it; do not silently proceed.

---

### Phase 2: Enrich the panel

**Purpose:** Add operational signals from public data. **Never enrich on firmographic fields.** Headcount, industry, and revenue are inputs, not signals: they are how data vendors organized the world, not how customers feel pain.

**Signal sources (deterministic-first):**
- **Careers / job postings** (a job-posting data provider, or a scrape of `/careers`): role X posted in prior N months, hiring velocity change.
- **Website self-description** (HTML-to-text first, paid scraper on the residual): new product line, new region, new compliance page, a tool migration announced.
- **LinkedIn org activity** (a LinkedIn data provider): leadership change, headcount inflection, post cadence change.
- **Tech-stack change over time** (a technographics provider): adopted or dropped a platform in the window.
- **Public registries / filings**: regulatory registrations, funding events, M&A.
- **GitHub public org activity** (for technical buyers): repos that went quiet, language shift, a compliance-tagged repo abandoned.

Every feature must be a **point-in-time, pre-outcome** signal where possible. The question is always "what was true about this company in the 6-18 months *before* the outcome", not "what is true now".

Output: a feature matrix, one row per domain, operational features only.

---

### Phase 3: Auto-segment into archetypes

**Purpose:** Let the data tell you the archetypes instead of assuming them.

**Process:**
1. Cluster on **behavioral / operational features only.** Industry, headcount, and revenue are leakage: if they are in the feature set the clusters will just rediscover firmographics. Strip and recluster if clusters look firmographic.
2. Minimum cluster size = 5. Smaller clusters overfit. Merge or drop.
3. Name each cluster with a **Cynical Buyer sub-agent**: spawn a sub-agent, give it the cluster's feature centroid and the member companies, ask it to name the cluster in operational language a skeptical buyer would recognize ("two-state legal-ops shop that just hired its first compliance owner"), not firmographic language ("mid-market financials").

```python
from sklearn.cluster import KMeans   # or HDBSCAN for variable-density clusters
# X = operational features only, scaled
labels = KMeans(n_clusters=k, random_state=42).fit_predict(X)
```

Output: named archetypes with member lists. Same company-stage and revenue band can land in totally different archetypes with totally different signal recipes. That is the point.

---

### Phase 4: Pull pain themes per archetype

**Purpose:** Ground each archetype in the language of the pain that preceded the buy.

**Process:** For each archetype, batch its call transcripts / notes and spawn a theme-extractor sub-agent. It returns the recurring operational pains for that cluster, with source-tagged quotes. This is the input to hypothesis generation.

If there are no transcripts, degrade gracefully: derive candidate themes from website and job-posting language instead, and flag in the output that themes are inferred from public text, not calls.

---

### Phase 5: Generate hypotheses

**Purpose:** For each archetype, generate "what operational event would have preceded a customer like this entering the market?" hypotheses.

Spawn a hypothesis-generation sub-agent per archetype. Every candidate must pass **5 hard gates** or it is rejected:

1. **Proves operational pain** (an event the company experienced), not a category it sits in.
2. **Uses a public-data source** you can actually pull.
3. **Has a measurable threshold** (>= 2 registrations, role present, repo quiet >= 9 months).
4. **Does not use headcount, vertical, or revenue.**
5. **Does not leak the outcome** (nothing that exists because they bought).

Gate-1 failure example to reject on sight: "operates in B2B" describes a category, not an event. Kill it.

Output: candidate signals per archetype, each with a proposed source and threshold.

---

### Phase 6: Backcast and validate (the safety net)

**Purpose:** Kill training-set coincidences before they ship. This is the phase that separates a discriminator you trust from one you fooled yourself into.

**Process:** For every surviving candidate signal, compute lift **independently** on the train set and the held-out 20% from Phase 1.

`lift = prevalence(signal | outcome-positive) / prevalence(signal | outcome-negative)`

Run `scripts/lift.py`. It computes train lift, holdout lift, and a Fisher-exact p-value on the train 2x2.

**Kill rule:** train lift high + holdout lift collapses toward ~1.0 = coincidence, kill it. A typical failure is a **nonsense signal** such as "won customers have a domain of eight characters or fewer": it can show a train lift above 2x by chance and a holdout lift of 1.0. Dead. Real signals (state registrations, compliance role) hold their lift across the split.

**Triage:**
- Great train lift, no holdout lift: coincidence, or holdout sample < 4 per cluster (then say so, do not pretend it survived).
- All signals collapse: features may be too noisy, or the archetype is not real.

Only signals that hold lift on the holdout proceed to Phase 7.

---

### Phase 7: Compose the discriminator

**Purpose:** Ship the rubric and the scorer.

For each surviving archetype, write `discriminator.md` (use `templates/discriminator.md`):

| field | example |
|-------|---------|
| signal | state professional registrations in prior 18mo |
| source | Secretary of State portal (or the provider that carries it) |
| threshold | >= 2 |
| weight | 0.55 |
| train lift | 4.1x |
| holdout lift | 3.6x |
| `fit_score` | `0.55*I(reg) + 0.45*I(role)` |
| looks-like-archetype | `fit_score >= 0.60` |

Also emit `discriminator.json` (machine-readable, one object per archetype) so `scripts/score_prospect.py` can score a new domain by pulling the same public signals and returning a per-archetype `fit_score`.

**What must NOT appear in the final rubric:** headcount band, vertical, revenue range. If they are there, you rebuilt the database filter.

---

## Quality checklist (final gate)

- [ ] Phase 0 ran and operator approved the quarantine list
- [ ] Outcome-leakage columns stripped before clustering (list them in the output)
- [ ] 20% holdout carved at Phase 1 with a fixed seed; never seen by Phases 3-5
- [ ] Clusters built on operational features only (no firmographics leaked in)
- [ ] Every shipped signal passes all 5 hard gates
- [ ] Every shipped signal holds lift on the holdout, not just train
- [ ] At least one candidate was killed at holdout (if none, be suspicious of the holdout)
- [ ] `discriminator.md` + `discriminator.json` + `score_prospect.py` produced
- [ ] No headcount / vertical / revenue in the final rubric

If any check fails, go back and fix it.

---

## Rules

1. No outcome data, no run. Request it via the intake checklist instead.
2. Phase 0 is not optional. Half your "healthy customers" may be auto-renewed dead accounts.
3. Hold out 20% from the very beginning, always.
4. Firmographics are inputs, not signals. Never cluster or score on them.
5. Every LLM step is a sub-agent, never a model API call inside the scripts.
6. Deterministic-first on every paid call.
7. A signal that does not hold lift on the holdout does not ship.
8. The unit is the situation, not the company-size band.

## References

- `reference/outcome-leakage.md`: full leakage strip list and why each leaks
- `reference/enrichment-providers.md`: which kind of provider for which signal
- `templates/intake-checklist.md`: outcome-data request spec
- Composes with `blueprint-swarm` (Phase 4 transcript analysis) and `icp-agent` (the interview-based ICP this one replaces once you have outcome data)

## Credits

The method (work backward from outcomes, operational situations over firmographics, hold out 20%, kill signals that do not survive the holdout) is Jordan Crawford's, from his win-loss-rewind work at [Blueprint GTM](https://blueprintgtm.com). This skill is our own write-up of it plus the scripts in `scripts/`. If you want the original, go to him.
