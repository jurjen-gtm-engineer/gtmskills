# Map-Limit Register: Sentinel Cloud Defense

> **Surface every place the model is likely to be inexact for this business, BEFORE the analysis runs.** This is the consulting equivalent of trust: naming our blind spots before the client finds them.

---

## Standing limitations (apply throughout)

| ID | Limit | Effect | Mitigation |
|---|---|---|---|
| **ML-1** | Product analytics data starts Q3 2024 | Pre-Q3 2024 cohorts have CR5 back-filled from product-team retrospective tagging (L3) | Use cohort Q1 2024 onward for CR5 analysis; flag earlier as L3 |
| **ML-2** | Marketing attribution via multi-touch model | Channel-source attribution is L2: first-touch is reliable, multi-touch reattribution is interpretive | Report results with attribution caveats; sensitivity-test channel mix |
| **ML-3** | CRM stage "Discovery" definition changed Feb 2025 | CR3 measurement slightly inflated pre-Feb 2025 | Normalize: pre-Feb 2025 records mapped through a translation table |
| **ML-4** | Mid-Market+ segment only 27 closed-won deals over 13 quarters | Segment-level CR4/CR5 has wide confidence intervals | Report MM+ with an explicit small-n caveat; don't make segment-specific recommendations off MM+ alone |
| **ML-5** | Renewals Manager hired Mar 2025 | Renewal motion not yet steady-state, so CR6/CR7 measurements reflect an early-stage motion | Forecast renewal lift conservatively; revisit at the 12-month mark |
| **ML-6** | MQL score recalibrated Oct 2024 | Pre-Oct 2024 MQLs may not be apples-to-apples with current MQLs | For trend lines, apply a recalibration adjustment; for static cohort selection (Q1 2024), no adjustment needed |
| **ML-7** | Activity tagging incomplete for ~14% of touches | "Time-to-first-touch" is sample-based; underlying touch counts may be undercounted | Use median (not mean) for time-to-touch; flag the undercount in detailed activity analysis |
| **ML-8** | No conversation-intelligence data for SMB SDRs (cost decision) | Cannot directly verify call quality / discovery technique for the SMB motion | Use AE survey as proxy; recommend extending call-recording coverage as part of Phase 1 |
| **ML-9** | Forecast model uses bootstrapped cohort progression | Forecast confidence intervals reflect within-cohort variation but not regime change | P10/P90 ranges are conservative; major motion changes would invalidate |
| **ML-10** | "Routine Use" definition (>=5 active users + >=3 detections) is Sentinel-specific | Not directly comparable to CR6 benchmarks without adjustment | Cross-walk applied when comparing to benchmarks; flagged on every benchmark slide |

---

## Engagement-specific limitations (this sprint only)

| ID | Limit | Effect | Mitigation |
|---|---|---|---|
| **EL-1** | No access to the finance system for the first 4 days (procurement) | Week 1 ARR-related deliverables draft from CRM-reported revenue | Cross-validate in Week 2 once the finance system is connected |
| **EL-2** | VP Sales (Carlos) on vacation Week 1 | His causal-model input deferred to the Week 2 standup | Pre-circulated questionnaire; written follow-up |
| **EL-3** | Two SDRs not available for survey (PTO + sick) | Sample size for the SDR survey is n=5 of 7 SMB SDRs | Reasonable representation but not exhaustive |

---

## What we are NOT measuring (out of scope, documented)

| Out of scope | Why | Where to do this if needed |
|---|---|---|
| Product-market-fit re-audit | The diagnostic assumes PMF holds | Separate engagement: a pre-PMF targeting audit |
| Pricing optimization | Out of scope of this engagement | Separate engagement: a pricing study |
| Competitive positioning | Strategy work, not diagnostic | Battlecard refresh project |
| Compensation plan redesign | Sensitive; recommend after the diagnostic | Phase 2 follow-on if Phase 1 succeeds |
| Recruiting / hiring | Capacity planning is out of scope | Org design study post-diagnostic |

---

## When to update this register

- Anytime a new ledger row is added with L3+ evidence
- Anytime the model is asked to extend beyond the documented cohort window
- Anytime a recommendation depends on a limit-flagged measurement

The register is a living document for the engagement, and a versioned artifact at handover.
