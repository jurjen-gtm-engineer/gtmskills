---
name: bowtie-benchmark
description: Interview the user for their bowtie revenue metrics, benchmark each against companies at their ACV band, score ahead/near/behind, and write a scorecard report with per-metric leak diagnosis.
---

# Bowtie Benchmark

Benchmark a B2B recurring-revenue funnel against the Bowtie Standard (recreated from Winning by Design). The skill runs a short interview, compares every metric the user can provide against the benchmark for their deal-size band, scores each one, and produces a written scorecard with a leak diagnosis per underperforming stage.

A hosted, interactive version of this assessment lives at https://bowtie-benchmarks.vercel.app. This skill produces the same scoring as a written report inside your session, no browser needed.

## Files

- `benchmarks.json`: the single source of truth. All benchmark values, band edges, medians, metric definitions, scoring thresholds, and derived-metric formulas. Read it before scoring anything. Never invent or adjust benchmark numbers.
- `report-template.md`: the output structure. Follow it section by section.

## How it works

The bowtie is the recurring-revenue funnel drawn as two triangles meeting at a knot (the WIN moment):

- Left side (acquisition): Awareness, Education, Selection
- Knot: Commit (the win)
- Right side (retention and expansion): Onboard, Achieve Impact, Growth, Expand

Eight conversion rates (CR1 through CR8) plus a sales cycle measure the flow through it. Benchmarks are keyed to average deal size because a $500 self-serve product and a $200k enterprise contract convert completely differently.

## Step 1: Establish the ACV band

Ask first, before any metric:

> What is your average new deal size in USD, after discounts? (Annual contract value for a typical new customer.)

Compute the band with the rule in `benchmarks.json` (`bands.rule`): splits at $1k, $5k, $15k, $50k, $150k, giving six bands labeled `<$1k` through `$150k+`. Every benchmark lookup uses this band index. Tell the user which band they landed in.

Optionally also ask for the lead cohort size (leads entering the funnel in the period) and ARR: not scored, but they unlock the derived metrics in Step 4.

## Step 2: Collect the 12 metrics

Ask in funnel order, grouped so the interview stays short. Every metric is optional: if the user does not measure something, record it as unmeasured and move on. Do not stall the interview on a missing number.

**Acquisition (left side)**

1. CR1, Prospect to MQL (%). A lead that shows interest through behavior and fits the target profile.
2. CR2, MQL to SQL (%). A lead that acknowledges a pain, fits, and wants to act. Meetings booked is a common proxy.
   - If the user tracks the front of the funnel as one number instead of CR1/CR2 separately, take LTO, Lead to Opportunity (%), instead.
3. CR3, Qualification / handoff (%). Share of SQLs that sellers accept as real pipeline, with an owner and a need-by date.
4. CR4, Win rate (%). Wins divided by the cohort of accepted opportunities from the same period. Won / (won + lost) is an acceptable proxy.
   - If the user tracks the back half as one number, take OTC, Opportunity to Close (%), instead.

**Deal mechanics**

5. Sales cycle (days or months). If given in months, convert: days = round(months * 30.4).
6. CR5, Median price discount (% off list).

**Retention and expansion (right side)**

7. CR6, Onboarding retained (%). Revenue that reaches first impact: the customer does something with the product they could not do before. Not sign-in, not a kickoff call.
8. CR7, Gross retention rate (% annual). This period's ARR from last period's customers divided by last period's ARR. Excludes expansion. Dollar-based beats logo-based.
9. CR8, Expansion rate (% of the post-churn base, annual). New ARR from existing customers: upsell, cross-sell, seats, price increases.
   - If the user tracks NRR instead of CR8, take NRR, Net revenue retention (%), directly.
   - If both CR7 and CR8 are given, derive implied NRR = CR7/100 * (1 + CR8/100) * 100 and show it.

The full metric model (keys, labels, direction, benchmark source) is in `benchmarks.json` under `metrics`.

## Step 3: Score every given metric

For each metric with a value, look up the benchmark:

- `source: band`: take the value at the band index from `benchmarks_by_band`. A `null` (CR1 and CR2 at the $150k+ band) means no ACV-keyed benchmark exists: fall back to the median if one exists for that metric, otherwise score it neutral.
- `source: median`: use `medians` (LTO 8%, OTC 16%, NRR 102%). These are live-cohort medians, not band-keyed.
- `source: cycle`: use `CYCLE_days_midpoint` for the band (the midpoints of the published ranges: 10, 15, 45, 75, 135, 180 days).

Then score, exactly as in `benchmarks.json` `scoring`:

- Higher is better (all CRs except CR5 and cycle): value >= benchmark is **ahead**; value >= benchmark * 0.8 is **near**; else **behind**.
- Lower is better (sales cycle, discount): value <= benchmark is **ahead**; value <= benchmark * 1.25 is **near**; else **behind**.
- No benchmark or no parseable value: **neutral**, excluded from the tally.

Report the delta: percentage points for % metrics (value minus benchmark), days for the cycle.

**Unmeasured metrics are a finding, not a footnote.** Any metric the user could not provide goes on its own list in the report. An unmeasured conversion rate means the data model cannot see that stage of the bowtie, which is itself a gap to fix (usually a CRM stage, cohort definition, or handoff timestamp that does not exist yet).

## Step 4: Compute derived metrics (when inputs allow)

Formulas in `benchmarks.json` `derived`:

- Implied NRR: CR7/100 * (1 + CR8/100) * 100 (when CR7 and CR8 are given and NRR was not entered directly).
- Installed base in 10 years: (NRR/100)^10, the compounding multiple before any new logos.
- Lead to Won yield: product of the given values among CR1, CR2, CR3, CR4 (needs 2 or more).
- Expected new logos: leads * yield (needs the lead cohort size).
- Implied new ARR: expected new logos * ACV.

Skip any derived metric whose inputs are missing. Never fabricate inputs to force a derived number.

## Step 5: Write the report

Use `report-template.md`. Fill every section. Rules:

- Overall verdict: count ahead/near/behind over scored (non-neutral) metrics. Any behind with behind >= ahead reads as "leaking"; behind present but ahead dominates, or only near, reads as "mixed"; all ahead reads as "compounding".
- Leak diagnosis: list metrics scored behind or near, worst first (behind before near, then by relative gap: (benchmark - value)/benchmark for higher-is-better, (value - benchmark)/benchmark for lower-is-better). Cap at the top 4. For each, adapt the matching narrative below to the user's actual numbers and context; do not paste it verbatim.
- If nothing scored behind or near: say every benchmarked stage is at or ahead of the market, and point at the unmeasured list as the remaining risk.

### Leak narratives (adapt per metric)

- **CR1**: Top-of-funnel targeting. The MQL definition or channel mix is leaking before sales ever sees it.
- **CR2**: MQL to SQL. Marketing-qualified leads are not surviving sales qualification: a definition misalignment between marketing and sales.
- **LTO**: Lead to Opportunity. The combined front of the funnel converts below the live median.
- **CR3**: Qualification discipline. Opportunities are entering the pipeline that should not. The handoff is soft.
- **CR4**: Win rate. The core selling motion converts below market for this deal size: a skill or fit gap.
- **OTC**: Opportunity to Close. The back half of the deal converts below the live median.
- **Sales cycle**: Deals take longer to close than peers, tying up capacity and slowing cash.
- **CR5**: Discounting. Deals are being bought with price instead of value. Margin and anchoring erode.
- **CR6**: Onboarding. Revenue churns before it is ever realized: the silent leak that caps everything downstream.
- **CR7**: Gross retention. The base leaks faster than peers. Impact is not landing in the first year.
- **CR8**: Expansion. The installed base is not growing, so the NRR upside is structurally capped.
- **NRR**: Net revenue retention. Expansion is not outrunning churn. The right side of the bowtie is flat.

## Constraints

- Benchmarks come from `benchmarks.json` only. If a value is null there, say "no benchmark at this band", never estimate one.
- Score only what was given. Never guess a metric the user did not provide.
- One clarifying question at most per metric (unit or definition), then accept the number as reported.
- Percentages arrive as numbers like 22 (meaning 22%), not 0.22. If an input looks like a fraction (below 1 for a conversion rate), confirm before scoring.
