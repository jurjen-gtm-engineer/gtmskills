# Normalized Bowtie: Sentinel Cloud Defense

**Week 1 deliverable** | Cohort: Q1 2024 to Q1 2025 closed cohort (selected for full 12-month visibility)

---

## The bowtie schema applied

```
                        ┌────────────────── EXPANSION ──────────────────┐
                        ↑                                                 ↓
PROSPECT → MQL → SQL → SAL → WON → ONBOARDED → IMPACT → RENEWED → EXPANDED
 (TAM)    CR1   CR2   CR3   CR4    CR5         CR6      CR7        CR8
```

Each stage normalized below to Sentinel's specific definitions and quirks.

---

## Stage definitions (Sentinel-specific)

| Bowtie stage | Sentinel definition | Source system | Owner |
|---|---|---|---|
| **Prospect** | Account in ICP firmographic (industry x headcount x tech stack) | Enriched account list | Marketing Ops |
| **MQL** | Lead with score >= 65 (marketing automation) OR demo request | Marketing automation + CRM | Marketing |
| **SQL** | MQL accepted by SDR after BANT-lite check | CRM lead status = "Qualified" | SDR Team |
| **SAL** | SQL with first meeting completed and AE confirms ICP fit | CRM opportunity stage = "Discovery" | AE / SDR handoff |
| **Won** | Closed-Won opportunity | CRM opportunity stage = "Closed-Won" | AE |
| **Onboarded** | Customer with implementation complete + first user login | Product analytics + CRM | CSM |
| **Impact** | Customer reaches "Routine Use", defined as >=5 active users + >=3 detections triaged | Product analytics | CSM |
| **Renewed** | Annual contract renewed | Finance system | Renewals Manager |
| **Expanded** | Net-new ARR added beyond original contract value | Finance system + CRM opp | AE (no dedicated expansion team) |

Map limit: the "Impact" definition is an approximation. Product analytics coverage starts Q3 2024, so Impact for 2023-vintage cohorts is back-filled from product-team retrospective tagging (L3 evidence).

---

## Cohort selection

Cohort-first methodology: follow one cohort of records through every stage, rather than dividing this quarter's stage counts by each other.

**Selected cohort:** Q1 2024 MQL cohort. Reasons:
1. Full 12-month visibility (so CR1 through CR7 are all observable)
2. Largest single cohort (n=843 MQLs)
3. Post-product-update, so the motion is comparable to current
4. Includes both segments (SMB + Mid-Market)

**Where milestone calc was used:** CR8 only (expansion measured at the 12-month mark, not by single-cohort progression). Flagged.

---

## Stage volumes (Q1 2024 cohort, n=843 MQLs)

| Stage | Volume | Notes |
|---|---|---|
| Prospect (TAM in ICP) | ~12,400 accounts | Estimated; account scoring not exhaustive |
| MQL | 843 | Starting cohort |
| SQL | 34 | Massive drop |
| SAL | 30 | Almost no further loss |
| Won | 8 | Steady CR4 |
| Onboarded | 8 | All Won customers reach Onboarded within 60 days |
| Impact (Routine Use) | 5 | 3 customers stalled in "Implemented but not in Routine Use" |
| Renewed (at month 13) | 4 | One churn |
| Expanded (within 12mo of Win) | 1 | Modest expansion motion |

**The shape of the funnel is the immediate diagnostic clue.** MQL to SQL is where 96% of the volume disappears. Everything else is roughly within industry norms.

---

## Where the data isn't clean (precursor to the map-limits register)

| Issue | Impact | Confidence | Notes |
|---|---|---|---|
| MQL score recalibrated Oct 2024 | Some 2024-vintage MQLs may not be apples-to-apples with 2025 | Medium | Recalibration adjustment applied where possible |
| CRM stage "Discovery" definition changed Feb 2025 | CR3 measurement slightly inflated pre-Feb 2025 | Low | Normalization tag applied |
| Sales engagement data starts Jan 2024 | No SDR activity history for pre-2024 cohorts | High | Doesn't affect chosen cohort |
| "First user login" timestamp partially missing | CR5 timing imprecise for ~12% of customers | Low | Used login proxy where missing |
| Renewals Manager hired Mar 2025 | Renewal motion not stable yet | Medium | CR6/CR7 reflect early-stage motion |

---

## Segment overlay

| Segment | MQL volume | Avg ACV | Notes |
|---|---|---|---|
| SMB (<500 emp) | 612 (73%) | 28K | Bulk of MQL volume |
| Mid-Market (500-2,500) | 198 (23%) | 54K | Most growth potential |
| Mid-Market+ (2,500+) | 33 (4%) | 112K | Tiny cohort, statistical caveat |

CR2 by segment (preview; full matrix in Week 2):
- SMB: 3.4%
- MM: 6.6%
- MM+: 12.1%

The CR2 problem is **most acute in SMB**, which is also where the bulk of volume sits. Targeting this is the highest-leverage move.

---

## What the bowtie tells us before any deep analysis

1. **MQL supply is fine.** 843/quarter is healthy for 40M ARR at 47K ACV.
2. **CR2 is the dominant problem.** 4% blended vs 25% benchmark is a 6x gap.
3. **Right-side metrics are stable but unimpressive.** CR5/CR6/CR7 all sit slightly below benchmark: modest issues, not crises.
4. **Expansion is undersized.** Only 1 of 4 renewing customers expanded, which suggests CR7 work has runway, but it's a Phase 3 issue, not Phase 1.

The data refutes the CRO's stated hypothesis ("we need more MQLs"). The bottleneck is conversion, not supply.
