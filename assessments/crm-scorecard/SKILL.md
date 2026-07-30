---
name: crm-scorecard
description: Turn raw CRM CSV exports (HubSpot, Salesforce, Attio, Pipedrive, or any CRM) into a bowtie conversion scorecard, computing CR1-CR8 where the data allows, benchmarking against ACV-band tables, and naming the top two revenue leaks.
---

# CRM Scorecard

Take a CRM export as CSV, map the customer's pipeline onto the bowtie model, compute the conversion rates the data actually supports, compare them against ACV-band benchmarks, and write a scorecard that names where the revenue engine leaks.

This skill is **CRM-agnostic and CSV-first**. It works on exports from HubSpot, Salesforce, Attio, Pipedrive, or any other CRM that can export deals to CSV. It makes **no live API calls** and requires no credentials. Everything runs locally on files the user provides.

## Inputs

Required:

- **Deals / opportunities CSV**: one row per deal. Minimum useful columns: deal id, deal name, current stage, create date, close date, amount. Strongly preferred additions: stage history (one column per stage-entry date, or a separate stage-change log CSV), pipeline name, deal type (new business / renewal / expansion), closed lost reason, company or account id.

Optional (unlocks more CRs):

- **Contacts / leads CSV**: contact id, create date, lifecycle stage or lead status, MQL date, SQL date, associated company or deal.
- **Companies / accounts CSV**: account id, name, domain, customer status, first won date.
- **Revenue by account over time** (from CRM, billing, or finance): account id, period, recurring revenue. This is what makes CR7 and CR8 honest.

Ask the user for whatever subset they have. Never refuse to run because a file is missing: the skill's contract is to compute what the data allows and to flag the rest explicitly.

## The bowtie model

Eight measurements across the full customer journey. The CR numbering below matches `benchmarks.json` exactly; use it consistently in every output.

| CR | Measures | Typical numerator / denominator |
|----|----------|-------------------------------|
| CR1 | Prospect to MQL | MQLs created / prospects or visitors reached |
| CR2 | MQL to SQL | SQLs / MQLs |
| CR3 | Qualification, handoff (SQL to accepted opportunity) | Deals accepted past the qualification boundary / deals or SQLs created |
| CR4 | Win rate | Closed Won / deals that passed the qualification boundary |
| CR5 | Median discount (pricing discipline, lower is better) | (list price minus closed amount) / list price, median over won deals |
| CR6 | Onboarding retained (Won to live / first impact) | Customers live or at first impact / Closed Won |
| CR7 | Gross revenue retention | Retained recurring revenue / renewable recurring revenue |
| CR8 | Expansion rate | Accounts (or revenue) that expanded / retained accounts (or base revenue) |

Supporting metrics: sales cycle (median days, opportunity creation to Closed Won), Lead to Opportunity, Opportunity to Close, NRR. Benchmarks for all of these are in `benchmarks.json`.

Two structural notes that shape interpretation:

- CR1 through CR4 are the acquisition side; CR6 through CR8 are the retention and expansion side. CR8 is the only place in the whole model where growth compounds.
- CR6 x CR7 approximates GRR when onboarding is untracked, and CR7 x CR8 dynamics drive NRR. Net numbers can hide gross problems: always read CR7 before celebrating CR8 or NRR.

## Workflow

Run the phases in order. **Phase 1 and Phase 2 each end in a hard stop for user confirmation.** Do not compute any conversion rate before both confirmations are in.

### Phase 0: Intake

1. Collect the CSV file paths from the user.
2. Identify the CRM flavor from the column headers (HubSpot exports say `Deal Stage`, Salesforce says `StageName` or `Stage`, Pipedrive says `Status` plus `Stage`, Attio uses custom attribute names). Say which flavor you detected; if unclear, ask.
3. Confirm three framing choices with the user:
   - **Analysis period** (default: trailing 12 months by deal create date).
   - **Currency and billing cadence** (if amounts are monthly, annualize by 12 before any ACV math).
   - **Whether the export mixes new business with renewals or expansions**, and if so, which column distinguishes them. Left-side CRs (CR1 to CR4) must be computed on new business only.

### Phase 1: Data-quality preflight (before any conversion math)

Run this with a script (Python with the csv module or pandas), not by eyeballing. Produce a preflight report containing, per file:

- **Row counts**: total rows, rows inside the analysis period, duplicate ids (report the count and three example ids).
- **Date coverage**: earliest and latest create date, % of rows with a parseable create date, % of closed rows missing a close date, and a per-month row count so obvious import spikes or dead months are visible.
- **Stage distribution**: every distinct stage value with count and % of total, sorted by count. Include the pipeline column cross-tab if multiple pipelines exist.
- **% missing per critical column**: stage, create date, close date, amount, account link. Flag any column above 20% missing as a computation risk.
- **Amount sanity**: median and p90 amount, count of zero or negative amounts, mixed currency symbols, % of won deals missing an amount.

Then STOP. Present the preflight report and ask the user to confirm:

1. that the row counts match their expectation of the export,
2. which pipelines are in scope (exclude renewal-only or partner pipelines from the left side),
3. that the analysis period stands, and
4. whether any anomaly the preflight surfaced (an import spike, a dead quarter, a 40%-missing amount column) has a known explanation.

Do not proceed until confirmed. If the data is too broken to score (for example, no dates at all, or one stage holds 95% of rows), say so and stop: a scorecard on garbage data is worse than no scorecard.

### Phase 2: Stage mapping (interactive, the hardest step)

CRM stage names never map 1:1 onto the bowtie. This step is a conversation, not an inference.

1. Read `stage-mapping-guide.md` in this skill folder for common stage vocabularies per CRM and the rules for ambiguous cases.
2. Build a proposed mapping: every distinct stage value from the preflight mapped to exactly one of: `pre-qualification`, `qualified` (at or past the qualification boundary), `won`, `lost`, `excluded` (nurture, on hold, renewal pipeline, junk).
3. Present the mapping as a table: stage name, row count, proposed bowtie bucket, one-line reasoning for every non-obvious call. Explicitly mark the **qualification boundary** (the first stage that counts as sales-accepted), because CR3 and CR4 both hinge on it.
4. Ask the user to confirm or correct. Apply corrections and show the final table once more before computing.

Never assume the stage order implied by the export is the true funnel order; confirm it. Deals can also skip stages and can be lost from any stage: mapping is by stage meaning, not by position alone.

### Phase 3: Compute conversions

**Method choice: cohort first, milestone as fallback.**

- **Cohort (preferred, requires stage timestamps or a stage-change log):** denominator = records that entered stage X inside the analysis window; numerator = how many of those ever reached stage Y by the cutoff. Apply a **maturity cutoff**: the cohort window must end at least one median sales cycle before today, otherwise deals that have not had time to convert drag the rate down. State the cutoff you used.
- **Milestone (fallback, when only current stage plus create/close dates exist):** count records at-or-past Y in the period divided by records at-or-past X in the period. Always attach this caveat verbatim to any milestone-based CR: *"Milestone method: numerator and denominator are not the same cohort. The rate is distorted when volume is growing or shrinking and can even exceed 100%. Treat as directional."*

Never mix methods within one CR, and label every CR in the scorecard with the method used.

**Per-CR computation and computability rules:**

| CR | Needs | If missing |
|----|-------|-----------|
| CR1 | Contacts CSV with MQL flag or lifecycle stage, plus a prospect denominator (visitor count or target account list) | Flag N/A: "no prospect denominator in a CRM export". For outbound motions CR1 alone is not meaningful; report combined Prospect to SQL instead |
| CR2 | Contacts CSV with MQL and SQL dates or lifecycle transitions | Flag N/A: "no lifecycle timestamps". Watch for contacts created at deal creation: if contact create date equals deal create date on most rows, CR2 is an artifact, not a measurement |
| CR3 | Deals with the confirmed qualification boundary | Computable from deals alone. If no acceptance stage exists, combine CR3 and CR4 into one number and multiply the two benchmarks for comparison |
| CR4 | Deals: Closed Won / passed qualification boundary | Computable from deals alone. Denominator is qualified deals, never all deals: using all deals hides qualification problems |
| CR5 | List price or discount column next to closed amount | Almost always N/A from standard exports. Flag: "no list price data, discount not measurable" |
| CR6 | An onboarding-complete or live/first-impact marker | Usually N/A from CRM alone. If every won customer appears active, report "not gated in CRM, assumed near 100%" and fold its benchmark into CR7 (multiply benchmarks) |
| CR7 | Renewal deals, or revenue by account across two periods | With neither, estimate from logo survival (accounts won more than 12 months ago that still show activity) and label it a logo proxy |
| CR8 | Deal type column or account revenue over time to identify expansion | Flag N/A if deal types are untracked; recommend the field |

**Sample size discipline:** report n for every CR. Below n=20 add "small sample, directional only". Below n=5, do not report a percentage at all: write "insufficient sample (n=X)".

**Supporting metrics** (compute where possible): median sales cycle on won deals (create to close), Lead to Opportunity (contacts with a deal / contacts created), Opportunity to Close (won / all deals created), NRR (current period revenue from last period's customer base / last period's revenue), median won deal size, closed-lost-cycle vs closed-won-cycle comparison.

### Phase 4: Benchmark comparison

1. Compute **ACV** = median annualized Closed Won amount in the period.
2. Load `benchmarks.json` from this skill folder. Select the ACV band whose range contains the ACV. If ACV is unknown, use the `$15k-$50k` band and disclose that.
3. Score every computed metric with the scoring rule from `benchmarks.json`:
   - Higher-is-better metrics: **ahead** when at or above benchmark, **near** when at or above 80% of benchmark, **behind** below that.
   - Lower-is-better metrics (CR5 discount, sales cycle): **ahead** at or below benchmark, **near** up to 125% of benchmark, **behind** above that.
   - Null benchmark or non-computable metric: **neutral**, never ahead or behind.
4. Before comparing, normalize definitions: cohort vs milestone, logo vs revenue, monthly vs annualized, recurring vs services revenue. A benchmark comparison on mismatched definitions is noise; state any normalization you could not perform.

### Phase 5: Write the scorecard

Output a single markdown scorecard with this structure:

```
# CRM Conversion Scorecard

Period: ... | Deals analyzed: n=... | ACV band: ... | Method: cohort / milestone per CR

## Scorecard
| CR | Metric | Value | n | Benchmark (band) | Status | Method |
(one row per CR plus sales cycle, LTO, OTC, NRR; N/A rows kept, with reason)

## The top 2 leaks
(ranked; see selection rule below)

## Per-CR read
(one short paragraph per computed CR using the interpretation rubric)

## Data confidence and gaps
(which CRs were computable, preflight risks that survived, CRM hygiene fixes that would unlock the N/A rows next quarter)
```

**Top 2 leaks selection rule:** among metrics scored `behind`, rank by relative gap: (benchmark minus value) / benchmark for higher-is-better, (value minus benchmark) / benchmark for lower-is-better. Exclude any metric with n below 20 from leak ranking. If fewer than two metrics are `behind`, fill from `near`, and say the engine is close to benchmark rather than inventing a crisis. For each leak: the number, the gap, the most likely mechanism (from the rubric below), and the single next question to investigate.

## Per-CR interpretation rubric

Restate these in the scorecard in plain language. Every read should end in a question to investigate, not a verdict: a CSV shows where the funnel leaks, not why.

- **CR1 low:** awareness or scoring problem. Check whether MQL criteria are too strict (only hand-raisers), whether an ICP is defined at all, and whether duplicates inflate the denominator. **CR1 high:** either healthy or the MQL definition is too generous; check whether volume actually supports pipeline goals. Gotcha: MQL definitions drift over time, so trend lines can reflect definition changes, not performance.
- **CR2 low:** speed-to-lead and follow-through. Check the first-touch SLA, prospector activity, and whether a loose CR1 is dumping unfiltered volume downstream. **CR2 high:** verify volume is sufficient before celebrating. Never interpret CR1, CR2, CR3 in isolation: they trade off against each other.
- **CR3 low:** the marketing-to-sales or SDR-to-AE handoff is soft. Check whether SDRs are goaled on meetings booked rather than down-funnel conversion, and whether qualification is buyer-centric. **CR3 high:** could mean upstream over-filtering. Only relevant in two-stage motions; skip for PLG and founder-led sales. Often untracked: meetings-held is the standard proxy.
- **CR4 low:** the most consequential and most analyzed number, since sales carries the highest cost concentration in the journey. Check the stage-of-death distribution (where do deals die), closed-lost reasons, inbound vs outbound split (outbound normally converts lower), and per-source rates. Also compare closed-lost cycle to closed-won cycle: lost deals taking longer than won deals signals late-stage indecision. **CR4 high:** check that opportunities are created consistently and that CR3 is not doing the flattering by over-filtering. Cohort win rate is not the same as Won / (Won + Lost); the ratio version is distorted by stalled deals.
- **CR5 (discount) high:** deals are being bought with price instead of value; margin and price anchoring erode. Check discount authority and whether discounts cluster around period-end.
- **CR6 low:** revenue churns before it is ever realized, the silent leak that caps everything downstream. Should sit near 100%; the shortfall is bad-fit selling, buyer's remorse, or onboarding failure. Also track median time from Won to live: a slow start hurts CR7 even when CR6 looks fine.
- **CR7 low:** the installed base leaks faster than peers. Check whether renewal conversations start 6+ months before renewal date, whether accounts are multi-threaded, and whether churn concentrates in a segment that should not have been sold. **CR7 high:** verify it is real. Multi-year and auto-renew contracts inflate it; normalize monthly to annual; read revenue retention and logo retention separately; subtract downsells from the numerator.
- **CR8 low:** no expansion engine, so NRR is structurally capped near 100% even with fine retention. Distinguish the four expansion types (re-sell to a new unit, upsell, cross-sell, renewal with price increase) because they need different plays. **CR8 high with CR7 low:** net is hiding gross; fix retention first.
- **Sales cycle behind:** capacity tied up and cash slowed, even when conversion looks fine. Wide spread between min and max cycle indicates no repeatable process.

**Cross-CR governance rules** (apply to every scorecard):

1. Left-side CRs on new business deals only; strip renewals and expansions from CR1 to CR4.
2. Normalize definitions before benchmarking; state what could not be normalized.
3. CR1, CR2, CR3 are interdependent; interpret them as one system.
4. Gross before net: CR7 before CR8 and NRR.
5. Time metrics flag operational problems that conversion rates hide.

## Hard rules

1. **Never fake a CR from insufficient data.** "Insufficient sample (n=3)" is a valid and required answer.
2. **Never skip the preflight or its confirmation stop.** Conversion math on unvalidated data produces confident nonsense.
3. **Never map stages without showing the mapping.** The user confirms the qualification boundary; you do not.
4. **CR4's denominator is qualified deals**, never all deals created.
5. **Label the method (cohort or milestone) on every CR**, and attach the milestone caveat wherever it applies.
6. **N/A rows stay in the scorecard** with the reason and the CRM fix that would make them computable. Gaps are findings.
7. **No live API calls, no credentials.** If the user offers API access, ask for a CSV export instead.
