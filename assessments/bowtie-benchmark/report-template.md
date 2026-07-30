# Bowtie Benchmark Scorecard

<!--
Output structure for the bowtie-benchmark skill.
Replace every {placeholder}. Delete sections only where the template says so.
Status legend: AHEAD / NEAR / BEHIND (unmeasured metrics go to their own section, not the table).
Never use em dashes or en dashes anywhere in the output.
-->

**Company context**: {ARR if given} | Avg deal ${acv} ({band label} band) | {period if given}
**Scored**: {n} of 12 metrics | **Tally**: {ahead} ahead, {near} near, {behind} behind
**Verdict**: {compounding | mixed | leaking}, {one-sentence summary of where the engine stands against companies at this deal size}

---

## The bowtie at a glance

Stage layout, acquisition on the left, retention and expansion on the right, the win at the knot:

```
 ACQUISITION                            |   RETENTION . EXPANSION
                                        |
 Awareness   Education    Selection   (WIN)   Onboard   Achieve Impact   Growth   Expand
 CR1         CR2 / LTO    CR3   CR4  Commit   CR6       CR7              CR8      NRR
 {status}    {status}     {st}  {st}          {status}  {status}         {status} {status}
```

<!-- Mark each stage with its scored status word (ahead/near/behind) or "not measured". Sales cycle and discount (CR5) sit at the knot: report them on their own line below the diagram. -->

Sales cycle: {value} vs benchmark ~{midpoint}d ({status}) | Discount (CR5): {value}% vs {benchmark}% ({status})

---

## Scorecard

| # | Metric | You | Benchmark ({band label}) | Delta | Status |
|---|--------|-----|--------------------------|-------|--------|
| CR1 | Prospect to MQL | {v}% | {b}% | {+/-x}pp | {status} |
| CR2 | MQL to SQL | {v}% | {b}% | {+/-x}pp | {status} |
| LTO | Lead to Opportunity | {v}% | {median}% (median) | {+/-x}pp | {status} |
| CR3 | Qualification / handoff | {v}% | {b}% | {+/-x}pp | {status} |
| CR4 | Win rate | {v}% | {b}% | {+/-x}pp | {status} |
| OTC | Opportunity to Close | {v}% | {median}% (median) | {+/-x}pp | {status} |
| CYCLE | Sales cycle | {v}d | ~{midpoint}d | {+/-x}d | {status} |
| CR5 | Median discount | {v}% | {b}% | {+/-x}pp | {status} |
| CR6 | Onboarding retained | {v}% | {b}% | {+/-x}pp | {status} |
| CR7 | Gross retention | {v}% | {b}% | {+/-x}pp | {status} |
| CR8 | Expansion rate | {v}% | {b}% | {+/-x}pp | {status} |
| NRR | Net revenue retention | {v}% | {median}% (median) | {+/-x}pp | {status} |

<!-- Include only rows the user provided. Rows without a value move to "Not measured" below. If a band value is null (CR1/CR2 at the $150k+ band), write "no benchmark at this band" and score neutral. -->

---

## Leak diagnosis

<!-- Top 4 metrics scored behind or near, worst first (behind before near, then by relative gap). One block per leak. Adapt the leak narrative from SKILL.md to the user's actual numbers; name the likely mechanism and the first thing to inspect. If no leaks: replace this section with one paragraph saying every benchmarked stage is at or ahead of the market, and point to the unmeasured list as the remaining risk. -->

### 1. {CRx} {Metric name}: {value} vs {benchmark}
{Adapted leak narrative: what this gap means mechanically, what it costs downstream, what to inspect first.}

### 2. ...

---

## Not measured (data-model gaps)

<!-- Every metric the user could not provide. This is a finding, not a footnote: an unmeasured stage is invisible to the operating model. For each, state what instrumenting it requires (a CRM stage, a cohort definition, a timestamp). If everything was measured, replace with: "All 12 metrics are instrumented. The data model covers the full bowtie." -->

- **{CRx} {Metric name}**: not tracked. {What is needed to measure it.}

---

## Derived metrics

<!-- Only rows whose inputs exist. Omit the section entirely if none can be computed. -->

| Derived | Formula | Value |
|---------|---------|-------|
| Implied NRR | CR7 x (1 + CR8) | {v}% |
| Installed base in 10 years | NRR^10, before new logos | {v}x |
| Lead to Won yield | {CR1 x CR2 x CR3 x CR4, given terms only} | {v}% |
| Expected new logos | {leads} leads x yield | {v} |
| Implied new ARR | logos x avg deal | ${v} |

---

## Reading this report

- Benchmarks are keyed to your ACV band ({band label}) and recreated from the Bowtie Standard (Winning by Design). LTO, OTC and NRR compare against live-cohort medians instead.
- Ahead means at or better than benchmark. Near means within 20% of it (25% for the lower-is-better metrics: cycle and discount). Behind means outside that.
- Benchmarks tell you where the engine leaks, not how much each leak costs. Quantifying the cost per leak and ranking fixes by gap closed requires modeling on your own funnel data.
- Run the interactive version of this assessment at https://bowtie-benchmarks.vercel.app.
