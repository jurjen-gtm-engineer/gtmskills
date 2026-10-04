---
name: gtm-diagnostic
description: 5-week GTM diagnostic sprint that stacks four frameworks (Revenue Architecture, Bowtie Analytics, Growth Architecture, Insight Engineering) to measure the full revenue engine, name the dominant cause, forward-project the probability of hitting the target, and produce a defensible 30-60-90 day action plan ordered by probability lift, not gap size.
---

# GTM Diagnostic

A 5-week diagnostic sprint for a B2B revenue engine. Measures the full bowtie (Acquisition, Onboarding, Retention, Expansion), names the dominant cause via layered causal modeling, forward-projects the probability of hitting the stated growth target, and sequences the fixes by probability lift.

**Concept attribution:** the bowtie model, the CR1-CR8 conversion-rate framework, cohort-first measurement, the probabilistic growth forecast, and the consulting-craft toolkit (Pyramid Principle, issue trees, MECE, Swiss Cheese causality) are concepts from Winning by Design (Jacco van der Kooij's Revenue Architecture and its companion Bowtie Analytics, Growth Architecture, and Insight Engineering frameworks). This skill is an original operationalization of those concepts as a working diagnostic; it reproduces no proprietary course material.

**Use when:**
- A company needs a defensible diagnostic of its revenue engine
- "Our growth is flat, why?" or "How do we hit our number?" is the question
- A board, investor, or acquirer wants a third-party-grade audit
- The company has 12+ months of CRM data, a defined-ish ICP, and a stated growth target

**Do NOT use for:**
- Single-channel audits (just cold email, just paid ads): use a channel-specific skill
- Pre-PMF startups with a thin dataset: cohort analysis needs real deal history; start with the assessments in `../gtm-readiness-scan` and `../bowtie-benchmark` instead
- Pure offer-design work: out of scope for this diagnostic
- Sales-skills enablement: out of scope; the diagnostic tells you WHERE enablement is needed, not how to train
- Lead-list-quality audits: use your enrichment and list-building tooling

CRM is one data source, not the diagnostic. The bowtie spans CRM + finance + product analytics + call intelligence.

---

## The Four-Framework Stack

Each framework patches the others' failure modes:

| Framework | Owns | Without it you get |
|---|---|---|
| **Revenue Architecture** | The structural lens: the bowtie as a recurring-revenue factory, with revenue, data, math, operating, growth, and GTM models underneath | Measurement without strategy: "you have a CR2 problem," so what? |
| **Bowtie Analytics** | The calculation playbook: cohort vs milestone measurement, CR1-CR8 computation and interpretation | Frameworks without measurement: interesting but unactionable |
| **Growth Architecture** | The forward look: probabilistic (Monte Carlo style) forecasting, growth-loop math, growth-state classification | Scoreboard without forecast: what is the probability of hitting the number? |
| **Insight Engineering** | The consulting craft: Pyramid Principle, issue trees, storyboarding, Pareto, MECE, Swiss Cheese causality | Beautiful slides over hollow analysis |

**Stack composition is the point.** Any single framework alone has a known failure mode.

---

## The 5-Week Sprint Structure

All deliverables are markdown files under `gtm-diagnostic/` in your working directory, one folder per week.

### Week 1: Intake and Normalization
**Goal:** single source of truth on the company's bowtie.

Actions:
1. Connect data sources: your CRM export, finance system export, product analytics export, your call recording exports
2. Normalize to the bowtie schema: Awareness, Education, Selection, Commit, Onboarding, Retention, Expansion
3. Build the **Source-Tier Ledger**: every number tagged L1-L6 (audited system-of-record down to industry benchmark)
4. Build the **Map-Limit Register**: every place the model will be inexact for THIS business, surfaced BEFORE the analysis

Deliverables:
- `gtm-diagnostic/01-intake/normalized-bowtie.md`
- `gtm-diagnostic/01-intake/source-tier-ledger.md`
- `gtm-diagnostic/01-intake/map-limits.md`

### Week 2: Calculation and Benchmarks
**Goal:** every conversion rate (CR1-CR8) computed cohort-first, benchmarked against peers.

Actions:
1. Apply cohort-first methodology: follow one cohort of records through every stage, rather than dividing this quarter's stage counts by each other. Milestone calculation only when cohort measurement is impossible, and flagged as such
2. Compute CR1 through CR8 with confidence intervals
3. Benchmark each CR against peer companies of comparable ACV, motion, and vertical (the sibling skill `../bowtie-benchmark` carries a benchmark table by ACV band)
4. Algebraic decomposition of any CR that is significantly off-benchmark: express the CR as a product of measurable factors, then measure each factor

Deliverables:
- `gtm-diagnostic/02-calculation/cr-matrix.md`
- `gtm-diagnostic/02-calculation/benchmarks.md`
- `gtm-diagnostic/02-calculation/decomposition-notes.md`

### Week 3: Diagnosis (Swiss-Cheese Causality)
**Goal:** name the dominant cause using layered causal modeling, not single-metric blame.

Actions:
1. Apply the Swiss Cheese model: real failures happen when multiple layers fail together; map the layers whose holes align to produce the observed outcome
2. Hypothesis-driven analysis: propose 3-5 causal hypotheses (including the operator's own stated hypothesis), test each against data, and show the rejections
3. Pareto-rank the contributing factors (which 20% of factors explain 80% of the gap)
4. Build an issue tree from the dominant cause down to root drivers, MECE at every level, pruning branches explicitly
5. Forecast: project P10/P50/P90 of hitting the stated target on the current trajectory, using a bootstrap simulation over historical cohort variance (a spreadsheet or a short script both work; for the trajectory-shape math see `../compound-growth-check`)

Deliverables:
- `gtm-diagnostic/03-diagnosis/causal-model.md`
- `gtm-diagnostic/03-diagnosis/issue-tree.md`
- `gtm-diagnostic/03-diagnosis/monte-carlo.md`

### Week 4: Action-Plan Design (Probability-Lift Ordering)
**Goal:** a 30-60-90 plan ordered by probability lift, not gap size and not stakeholder volume.

Actions:
1. For each candidate intervention, model the lift in P50 (and in probability of hitting the target)
2. Sort interventions by lift / cost ratio
3. Sequence: 30-day phase (highest lift, lowest cost), 60-day phase (medium), 90-day phase (longest payoff)
4. For each action: define owner, dependencies, leading indicator, and exit criterion
5. Pre-build the operator, CFO, CEO, and board reads of the same plan: same facts, different lenses

Deliverables:
- `gtm-diagnostic/04-design/action-plan-30-60-90.md`
- `gtm-diagnostic/04-design/probability-lift-matrix.md`
- `gtm-diagnostic/04-design/stakeholder-reads.md`

### Week 5: Deliver
**Goal:** stakeholder-tier deliverables, each pre-validated against the quality gates.

Actions:
1. Build the executive deck: Pyramid structure (answer first, support after), dot-dash storyboarding, one idea per slide
2. Build the operator runbook: what each owner does on day 1, day 30, day 60, day 90
3. Build the CFO/board appendix: forecasts, sensitivity analysis, source-tier ledger, risk register
4. Run all quality gates (below)
5. Present and hand over

Deliverables:
- `gtm-diagnostic/05-deliver/executive-deck.md`
- `gtm-diagnostic/05-deliver/operator-runbook.md`
- `gtm-diagnostic/05-deliver/board-appendix.md`

---

## Depth options

| Depth | Turnaround | Scope |
|---|---|---|
| **Quick pass** | 1 week | CR matrix + 30-day plan only; thin diagnosis |
| **Compressed** (default) | 3 weeks | Compressed sprint, all 4 frameworks lite |
| **Full** | 5 weeks | Full sprint as described above |
| **Full with follow-through** | 5 weeks + 90 days | Full + weekly check-ins and mid-quarter recalibration |

Default to Compressed unless specified.

---

## Quality Gates (every diagnostic ships these)

Before any deliverable goes out the door:

- [ ] Every number has a source-tier tag (L1-L6)
- [ ] Every Map-Limit was surfaced in Week 1, not discovered late
- [ ] CR calculation is cohort-first (milestone calc flagged where used)
- [ ] At least 3 causal hypotheses tested, not just the obvious one
- [ ] The forecast includes the CURRENT-trajectory baseline, not just intervention scenarios
- [ ] The 30-60-90 plan is sequenced by **probability lift**, not gap size
- [ ] Every recommendation has an owner, a leading indicator, and an exit criterion
- [ ] Pyramid structure on the deck: answer first, support after
- [ ] Operator + CFO + board reads are pre-built, not improvised in the meeting

If any item is unchecked: don't ship. Fix first.

---

## Anti-Patterns (things that kill a diagnostic)

| Anti-pattern | Why it fails |
|---|---|
| Treating CRM data as the only source | The CRM doesn't have churn, ARR per cohort, or product usage; you need finance + product + call intelligence |
| Single-cause diagnosis | Real growth systems are Swiss Cheese: multiple layers fail together |
| Recommending the loudest gap | "Hire more SDRs" is rarely the highest-probability lift |
| Forecasting deterministically | Growth is probabilistic; a single-number forecast hides the risk |
| Skipping the Map-Limit register | Surprise inaccuracies destroy trust at delivery |
| One-deck deliverable | Operator, CFO, CEO, and board each need their own read of the same plan |
| A plan without named owners per line | Plans without owners don't execute |

---

## Composition with sibling skills

| Skill | How it connects |
|---|---|
| `../gtm-readiness-scan` | Run first if the company's stage is unclear; the diagnostic assumes a working motion exists to measure |
| `../bowtie-benchmark` | The CR1-CR8 benchmark table by ACV band, used in Week 2 |
| `../crm-scorecard` | Computes CR1-CR8 from a raw CRM export with a data-quality preflight; a Week 1-2 accelerator |
| `../conversational-intelligence` | Structures call-transcript intelligence for the Week 1 intake |
| `../blueprint-swarm` | Parallel sub-agent analysis of large call/record volumes feeding the customer-voice layer |
| `../compound-growth-check` | The ARR-trajectory classification math behind the Week 3 forward look |

---

## Inputs needed to start

1. **A working directory** for the engagement
2. **Data access**: CRM export, finance export, product analytics export, call recording exports
3. **Stated growth target** + timeframe (the number the forecast will be run against)
4. **Defined ICP or segment**, even a rough one; Week 1 will refine it
5. **Stakeholder list**: who reads the operator runbook, the CFO appendix, the board summary
6. **Tier selection**: Quick pass / Compressed / Full / Full with follow-through

If any are missing, intake them before the Week 1 kickoff.

---

## Output conventions

- All deliverables in markdown at `gtm-diagnostic/{week}-{phase}/` in the working directory
- Every number cites its source row in the source-tier ledger
- The final deck is rendered separately (slides, PDF, or a doc) on top of the markdown source of truth
- After delivery, log what worked, what surprised, and what to retest; patterns that repeat across engagements should be promoted into this skill

---

## Worked example

`example/` contains a complete, fully fictional engagement for "Sentinel Cloud Defense," a cybersecurity SaaS at 40M ARR whose CRO believes "we need more MQLs" while the data shows a collapsed MQL-to-SQL conversion step. It shows what the output of every week looks like: the case brief, all three intake artifacts, the CR matrix and decompositions, the causal model, issue tree and probabilistic forecast, the probability-lift matrix and 30-60-90 plan, and all three final deliverables. Start with `example/README.md`.
