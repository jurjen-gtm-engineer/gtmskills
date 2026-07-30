---
name: compound-growth-check
description: Diagnose whether a company's growth actually compounds. Takes 6+ quarters of ARR, computes the first and second derivatives, classifies the trajectory (compounding, inflection, decompounding, decay), places the company on the 10-state growth ladder, and writes a one-page verdict.
---

# Compound Growth Check

A 90-second diagnostic that separates growth that compounds from growth that merely looks healthy. ARR going up and to the right tells you almost nothing. The question is whether growth itself is growing: whether output from one quarter reliably becomes input for the next.

**Concept attribution:** the derivative-based compound check, the compounding versus bought-growth framing, and the 10-state growth ladder are concepts from Winning by Design (Jacco van der Kooij's Growth Architecture framework). This skill implements the math and the diagnostic workflow at concept level; it reproduces no proprietary course material.

## What it computes

Given quarterly ARR snapshots X_1 ... X_n (oldest first):

| Measure | Formula | Reads as |
|---|---|---|
| First derivative | delta X_t = X_t - X_(t-1) | Absolute QoQ ARR growth |
| Second derivative | delta2 X_t = delta X_t - delta X_(t-1) | The change in growth itself |

Simple finite differences, deliberately. No smoothing, no gradients. This matches how the check is presented on public charts and keeps every number auditable by hand.

## Trajectory classification

| Verdict | Rule | Meaning |
|---|---|---|
| compounding | At least 60% of delta2 values positive AND at least 2 of the last 3 readings positive | Growth is accelerating; output feeds next-period input |
| inflection | Growth positive but the delta2 signal is mixed or recently flipped negative | The engine is sputtering; the next 2 to 3 quarters decide |
| decompounding | Under 50% of delta2 positive, or exactly 50% with average at or below zero | delta2 oscillates around zero; each dip resets the compound engine; the signature of bought, not earned, growth |
| decay | Both of the last two delta values negative | ARR itself is shrinking; there is no compound check to run |

Two refinements, both implemented in the script:

1. **Trailing window wins.** With 8 or more delta2 values, the trailing 8 quarters are classified separately. If the full series says inflection but the recent window says decompounding, the verdict escalates to decompounding: recent state beats history biased by an early acceleration period.
2. **Decay preempts everything.** If ARR fell in both of the last two quarters, the verdict is decay regardless of the delta2 statistics.

## The 10-state growth ladder

Ten states across three macro phases. The ladder places a company by combining revenue scale (which states are plausible at this ARR) with the trajectory verdict (which of those states the derivatives support).

| # | State | Phase | Powered by |
|---|---|---|---|
| 1 | Unstructured | Accelerated Growth | Effort and volume |
| 2 | Structured | Accelerated Growth | |
| 3 | Scalable | Accelerated Growth | |
| 4 | Accelerated | Accelerated Growth | |
| 5 | Sustainable | Compound Growth | Feedback and learning loops |
| 6 | Exponential | Compound Growth | |
| 7 | Compounding | Compound Growth | |
| | **The Wall** | | The shift from "sell a great product" to "help the customer succeed" |
| 8 | Durable | Autonomous Growth | Orchestration and self-correction |
| 9 | Orchestrated | Autonomous Growth | |
| 10 | Autonomous | Autonomous Growth | |

Where companies typically stall: perpetual-license software stalled at state 3, most SaaS companies sit at states 5 to 6 (buying growth instead of earning it through loops), AI-native companies tend to sit at state 7. The Wall between 7 and 8 is the hardest transition: the mental model has to change, not just the metrics.

The script's placement logic: revenue bands narrow the candidate states, then the trajectory picks within them (compounding favors the highest candidate, decompounding the middle, inflection and decay the lowest). Optional NRR and cost growth inputs refine the pick. Confidence starts at 0.50 and rises with more quarters and more inputs, capped at 0.95. Placement above the Wall is always flagged as unverifiable from ARR alone.

## Workflow

### Step 1: Collect the input

Accept either format:

- **Pasted in chat:** a series of quarterly ARR values, oldest first. Confirm the ordering and the unit (millions is the common case) before running.
- **CSV file:** two columns, `quarter` and `arr`, header row optional.

Rules:

- 6 or more quarters is the standard run. 3 to 5 quarters: run anyway, but the script attaches an explicit low-confidence caveat and reduces confidence; carry that caveat prominently into the verdict.
- Fewer than 3 quarters: refuse, a second derivative needs 3 points.
- Values must be ARR snapshots (annualized recurring revenue at quarter end), not quarterly revenue. If the user pastes quarterly revenue, either ask for ARR or multiply a clean quarterly figure by 4 and say so in the report.

### Step 2: Run the script

```bash
python scripts/compound_check.py "12.0,13.5,15.4,17.8,20.9,24.7,29.4,35.1"
python scripts/compound_check.py arr.csv --company "Acme" --nrr 1.12
python scripts/compound_check.py arr.csv --unit thousands --cost-growth 0.20
```

Flags: `--unit` (auto, dollars, thousands, millions; auto reads values of 100,000 and above as dollars, smaller values as millions), `--company`, `--nrr` (decimal, 1.15 means 115%), `--cost-growth` (decimal YoY cost growth). NRR and cost growth are optional but each adds 0.10 confidence and sharpens the state pick; ask for them if the user has them at hand.

The script prints one JSON object: the series, both derivatives, QoQ growth rates, the trajectory verdict with headline and explanation, the ladder placement with confidence and reasoning, and all caveats.

### Step 3: Write the one-page verdict

Use `report-template.md`. Verdict first, evidence second: the reader must get the whole diagnostic from the first three lines. Fill in:

1. **The verdict:** trajectory classification plus ladder state, with confidence.
2. **The math table:** quarter, ARR, delta, delta2, straight from the JSON.
3. **What the trajectory says:** the script's explanation, expanded with the specific quarters where delta2 flipped.
4. **What typically causes this pattern** (pick the matching block):
   - *Compounding:* one or more real feedback loops are live (customer-led acquisition, usage-led expansion, data or content loops). Confirm which loop, then protect it.
   - *Inflection:* a loop is forming or dying; a channel is saturating; a pricing or packaging change is working through the base; a strong cohort is aging out.
   - *Decompounding:* growth is bought quarter by quarter (paid acquisition, headcount-driven pipeline, promotional pricing) with no loop feeding output back to input. Momentum resets every time spend or effort dips. Also common: onboarding gaps quietly leaking the gains, so acquisition wins are cancelled by churn.
   - *Decay:* retention has collapsed, the market is contracting, or a dominant channel died. Diagnosis shifts from growth to the bleeding: what acquisition and retention floor stops the decline.
5. **What to check next** (pick the matching block):
   - *Compounding:* which loop drives it and its conversion economics; whether the loop survives a spend freeze; NRR by cohort; where the next state on the ladder requires a different operating model.
   - *Inflection:* the last 2 to 3 quarters of pipeline sources; cohort NRR trend; whether recent delta2 dips coincide with spend cuts (bought growth exposed) or with churn (retention problem).
   - *Decompounding:* cost to grow per dollar of net-new ARR and its trend; the ratio of loop-sourced to spend-sourced pipeline; onboarding-to-impact conversion; whether any output (customers, usage, data) is wired back into acquisition at all.
   - *Decay:* GRR and logo churn immediately; concentration of the losses (segment, cohort, channel); whether new sales still clear a floor that funds a turnaround.
6. **Caveats:** every caveat from the JSON, verbatim or tightened, always including the low-confidence caveat on short series and the Wall caveat on state 8+ placements.

Keep the whole report on one page. State placement is a hypothesis with a confidence score, not a certificate: say so.

## Honest limits

This check claims only what the math supports: whether the growth system compounds, oscillates, or decays, and a scale-plus-trajectory hypothesis for the ladder state. It does not claim probability of hitting a target, lever sensitivity, or segment decomposition; those require more data than an ARR series. Never present the state placement as verified above state 7, and never run the check on fewer than 3 points.
