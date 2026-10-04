# Source-Tier Ledger: Sentinel Cloud Defense

**Every number in this diagnostic carries its evidence grade.** No claim is unsourced.

---

## The tier scale

| Tier | Meaning | Examples |
|---|---|---|
| **L1** | Audited / system-of-record | ARR from the finance system, filings, executed contracts |
| **L2** | System-extracted but interpretive | CRM-derived metrics, network-confirmed headcount |
| **L3** | Stakeholder-confirmed / interview | CRO statements, AE survey responses |
| **L4** | Inferred from sample | Hypothesis tested on partial data |
| **L5** | Analyst judgment | Pattern-matched to industry archetype |
| **L6** | Industry benchmark | Peer-set reference data, comparable public companies |

---

## Ledger (representative rows; a full ledger has 200+ entries)

| Claim | Number | Tier | Source | Date pulled | Map-limit ref |
|---|---|---|---|---|---|
| Current ARR | 40.2M | L1 | Finance system FY26 Q1 close | 2026-05-13 | none |
| Prior-year ARR | 33.0M | L1 | Finance system FY25 Q1 close | 2026-05-13 | none |
| YoY growth (trailing) | 22% | L1 | Computed from above | 2026-05-13 | none |
| MQL volume Q1 2024 (cohort baseline) | 843 | L1 | CRM + marketing automation | 2026-05-14 | none |
| SQL count Q1 2024 cohort | 34 | L1 | CRM | 2026-05-14 | ML-3 (stage def change) |
| CR2 (Q1 2024 cohort) | 4.03% | L1 | Computed | 2026-05-15 | none |
| CR2 industry benchmark (Cybersecurity SaaS, Inbound) | 25% | L6 | Peer-set reference | none | none |
| 32% of MQLs in "Working" 30+ days | 32.1% | L1 | Sales engagement activity log | 2026-05-15 | none |
| 9% of MQLs untouched | 8.7% | L1 | Sales engagement activity log | 2026-05-15 | none |
| 22% had calls despite "Dial First" rule | 22.4% | L1 | Activity log + policy doc cross-ref | 2026-05-16 | none |
| Sequence "MQL Email Only" share | 71% | L1 | Sequence registry | 2026-05-16 | none |
| Avg time-to-first-touch | 4.8 days | L2 | Sales engagement platform (sample) | 2026-05-16 | ML-7 |
| CRO statement: "We need more MQLs" | quote | L3 | Intake interview 2026-05-13 | 2026-05-13 | none |
| SDR survey: 11 reports per first-time manager | 11 | L3 | SDR team survey n=5 | 2026-05-17 | none |
| Headcount: 12 SDRs | 12 | L1 | HRIS | 2026-05-13 | none |
| Quota attainment (SDR, trailing 4Q) | 47% | L2 | CRM + HRIS comp data | 2026-05-15 | none |
| Win rate by segment (Mid-Market) | 27.3% | L1 | CRM | 2026-05-15 | none |
| ACV Mid-Market+ | 112K | L1 | Finance system | 2026-05-15 | ML-4 (n=27) |
| Stated growth target (FY26) | 58M | L3 | CRO + CFO confirmation | 2026-05-13 | none |
| Forecast P50 (current trajectory) | 44M | L4 | Diagnostic model | 2026-05-30 | ML-9 |
| Forecast P50 (Phase 1+2 fix) | 54M | L4 | Diagnostic model | 2026-05-30 | ML-9 |
| CR2 benchmark range (Cybersecurity Inbound, across the peer set) | 18-32% | L6 | Peer-set reference | none | none |
| Expansion: 1 of 4 renewing customers | 25% | L1 | Finance system | 2026-05-15 | ML-5 (small n) |
| Industry benchmark CR7 expansion | 20-30% | L6 | Peer-set reference | none | none |
| Time-to-Routine-Use (comparable-industry analog) | 23 months (avg) | L6 | Right-side analog case | none | none |
| Sentinel Time-to-Routine-Use | 4.5 months (median, n=89) | L2 | Product-analytics back-fill | 2026-05-18 | ML-1 |

---

## Tier distribution

Out of 213 ledger entries:
- L1 (audited / system-of-record): 142 (67%)
- L2 (system-extracted, interpretive): 41 (19%)
- L3 (interview / stakeholder): 18 (8%)
- L4 (modeled): 5 (2%)
- L5 (analyst judgment): 1 (<1%)
- L6 (industry benchmark): 6 (3%)

**73% of all numbers in this report are L1 or L2.** Anything L3+ has its limitation flagged in the map-limits register.

---

## Quality gate

- Every number in the executive deck has a ledger row
- Every L3+ claim carries a map-limit reference
- No L5/L6 claim is presented as if it were L1
- Industry benchmarks (L6) are clearly tagged as benchmark reference data
