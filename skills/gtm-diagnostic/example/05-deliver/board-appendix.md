# Board Appendix: Sentinel Cloud Defense

**Week 5 deliverable** | The risk + evidence layer of the executive deck. Designed for the CFO and the board. Monetary figures in USD.

---

## A. Methodology disclosure

This diagnostic stacks four frameworks, each a concept from Winning by Design, operationalized for this engagement:

| Framework | Concept origin | What it contributed |
|---|---|---|
| Revenue Architecture | Jacco van der Kooij (Winning by Design) | Structural model: the bowtie + 8 CRs + the underlying models |
| Bowtie Analytics | Winning by Design | Calculation methodology: cohort-first, algebraic decomposition |
| Growth Architecture | Winning by Design | Probabilistic forecast: bootstrap simulation, sensitivity |
| Insight Engineering | Winning by Design | Consulting craft: Swiss Cheese, Pyramid, issue tree |

The combination of all four is what produces a defensible diagnostic. Any single framework alone has a known failure mode.

---

## B. Source-tier evidence summary

213 numbered claims in this diagnostic, distributed by evidence tier:

| Tier | Count | % | Examples |
|---|---|---|---|
| L1 (audited / system-of-record) | 142 | 67% | ARR, MQL counts, deal counts, activity logs |
| L2 (system-extracted, interpretive) | 41 | 19% | Computed metrics, attribution-adjusted figures |
| L3 (stakeholder interview) | 18 | 8% | CRO/VP statements, SDR survey responses |
| L4 (modeled / inferred) | 5 | 2% | Forecast outputs |
| L5 (analyst judgment) | 1 | <1% | Single edge-case interpretation |
| L6 (industry benchmark) | 6 | 3% | Peer-set reference data |

**73% of the diagnostic is L1 or L2 evidence.** Every L3+ claim is flagged in the map-limits register.

Full ledger: `01-intake/source-tier-ledger.md`

---

## C. Map-limits register (13 known limitations)

| ID | Limitation | Mitigation |
|---|---|---|
| ML-1 | Product analytics data starts Q3 2024 | Cohort selection avoids pre-Q3 2024 |
| ML-2 | Multi-touch attribution is L2 | Sensitivity-tested |
| ML-3 | CRM stage definition changed Feb 2025 | Normalization table applied |
| ML-4 | MM+ segment n=27 closed-won | Small-n caveats on segment-specific recs |
| ML-5 | Renewals Manager hired Mar 2025 | CR6/7 forecasts conservative |
| ML-6 | MQL score recalibrated Oct 2024 | Cohort selection unaffected |
| ML-7 | Activity tagging ~14% incomplete | Median used, not mean |
| ML-8 | No conversation-intelligence data for SMB SDRs | AE survey proxy |
| ML-9 | Forecast uses cohort-progression bootstrap | Conservative ranges |
| ML-10 | "Routine Use" definition Sentinel-specific | Cross-walk applied |
| EL-1 | No finance-system access Days 1-4 | Cross-validated Week 2 |
| EL-2 | VP Sales on PTO Week 1 | Input via questionnaire |
| EL-3 | 2 SDRs unavailable for survey | n=5 of 7 SMB SDRs |

Full register: `01-intake/map-limits.md`

---

## D. CR decomposition (algebraic structure)

The diagnostic's recommendations derive from decomposing off-benchmark CRs. **CR2 = Effort x Quality x Cadence_Fit.**

| Factor | Sentinel | Benchmark | Lift target (Phase 1 end) |
|---|---|---|---|
| Effort (touch coverage <5 days) | 47% | 95% | 75% |
| Quality (discovery completeness) | 60% | 75% | 65% |
| Cadence Fit (% on phone-first) | 14% | 35% | 35% |
| **Composite CR2** | **4.0%** | **25%** | **12% by D30** |

CR5 decomposes similarly (`02-calculation/decomposition-notes.md`).

---

## E. Sensitivity analysis (top 5 variables)

Scenario 2 baseline P50 = 54.2M. Single-variable shifts of 1 sigma:

| Input | Range | P50 effect | P(hit) effect |
|---|---|---|---|
| CR2 actual lift (target 18%) | 3pp either way | 51.6M to 56.8M | 22% to 42% |
| MQL inflow rate (280/mo) | 20% either way | 52.2M to 56.1M | 24% to 39% |
| Time-to-CR2-lift (60 days) | 15 days either way | 52.8M to 55.7M | 26% to 37% |
| Churn rate (4% annualized) | 1pp either way | 53.5M to 54.9M | 28% to 34% |
| CR5 lift (target 75%) | 5pp either way | 53.0M to 55.4M | 27% to 35% |

**Most sensitive: CR2 lift achievement.** Phase 1 execution discipline is the single biggest determinant of forecast accuracy.

---

## F. Risk register (all phases)

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Phase 1: SDRs resist the dial-volume increase | High | Medium | Comp incentive (10% bonus on the touch SLA) |
| Phase 1: sequence tooling config slippage | Medium | Low | Backup manual sequence assignment |
| Phase 1: CR2 lift smaller than targeted | Medium | Medium | Phase 2 still proceeds; doesn't block sequencing |
| Phase 1: backlog re-routing overloads SDRs | Medium | Low | Cap at 50 leads/SDR/week |
| Phase 2: CSM reallocation creates existing-account churn | Medium | High | Hire a CSM rather than reallocate |
| Phase 2: tier sequences add SDR complexity | Medium | Low | Manager training + tooling guardrails |
| Phase 2: Phase 1 gains erode | High | Medium | Sustained dashboard + weekly reviews |
| Phase 3: expansion role takes >30 days to fill | Medium | Medium | Begin sourcing Day 40 |
| Phase 3: existing base too small to support the role | Low | High | Conditional on the Day 60 milestone holding |
| All phases: competitive response | Low | Medium | Not modeled; monitor; flag for follow-on |
| All phases: macro / regime change | Low | High | Not modeled; standard caveat |

---

## G. Comparable benchmark peer set (transparency)

The cybersecurity inbound peer set used for benchmark comparison (fictional in this demo; in a real engagement, disclose your actual benchmark source):

- **n = 18 companies**
- **ARR range:** 25M to 80M (median 46M)
- **ACV range:** 32K to 95K (median 44K)
- **Growth YoY:** 18% to 110% (median 38%)
- **Vintage:** 2023-2025 data
- **Refresh cadence:** quarterly

**Sentinel's position in the peer set:**
- ARR: median (50th %ile)
- ACV: 40th %ile
- Growth: 25th %ile (where the gap lives)
- S&M headcount: 55th %ile

**Sentinel is dead-center in the peer set on size and structure.** Direct comparison is valid.

Anonymized peer-set composition available on request (under NDA).

---

## H. Investment and ROI summary

**Total 90-day investment:**
- Phase 1: 5K + 0.5 FTE-week = ~10K all-in
- Phase 2: 1 FTE reallocation (no incremental cash)
- Phase 3: 1 FTE hire (180K annualized; 45K in Q4) = 45K Q4

**Total Q3+Q4 cash outlay:** ~55K
**Probability-weighted incremental ARR (vs status quo):** 14M
**ROI on cash investment:** ~250x
**ROI on cash + FTE-equivalent cost:** ~76x

This is the lowest-cost path the diagnostic identified to reach the stated target. Any higher-cost intervention (additional SDR hires, brand campaigns, new motions) was modeled and ranked lower on lift/cost.

---

## I. What the board should commit to

| Commitment | Approver | Trigger |
|---|---|---|
| Approve Phase 1 + 2 cash + 1 FTE realloc | CRO + CFO | Today |
| Approve the Phase 3 expansion-role hire (180K annualized) | CRO + CFO + CEO | Day 60 milestone holds |
| Monthly probability re-forecast against this model | CFO | Ongoing |
| Day 90 full-diagnostic re-measurement | Maya + diagnostic team | Day 90 |
| Optional Phase 4 annual operating plan engagement | TBD | Day 90 review |

---

## J. What this engagement DOESN'T commit Sentinel to

- Any specific Phase 4 follow-on engagement (decided at Day 90 based on results)
- Any compensation plan changes beyond the SDR touch-coverage bonus
- Any vendor selection beyond the tools already in use and any net-new CSM tool
- Any product roadmap shifts
- Any pricing changes
- Any structural reorg (Phase 3 adds a role; it doesn't restructure existing teams)

The diagnostic produces a plan, not a constraint. The plan is reversible at each milestone if assumptions don't hold.

---

## Quality gate (all items checked before this deck shipped)

- [x] Every number has a source-tier ledger row
- [x] Every Map-Limit surfaced in Week 1
- [x] CR calculation is cohort-first (milestone flagged where used)
- [x] At least 3 causal hypotheses tested
- [x] The forecast includes the current-trajectory baseline
- [x] The 30-60-90 plan is sequenced by probability lift, not gap size
- [x] Every recommendation has an owner + leading indicator + exit criterion
- [x] Pyramid structure on the deck: answer first, support after
- [x] Operator + CFO + board reads are pre-built

Deliverable is decision-ready.
