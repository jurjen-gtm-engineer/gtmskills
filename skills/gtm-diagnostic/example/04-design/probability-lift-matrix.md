# Probability Lift Matrix: Sentinel Cloud Defense

**Week 4 deliverable** | Every candidate intervention modeled for its lift in P(hit the 58M target). Sorted by **lift / cost ratio**, not gap size or stakeholder enthusiasm. Monetary figures in USD.

---

## All interventions considered (full set, before sequencing)

| # | Intervention | P(hit) lift | Investment | Time to lift | Lift/cost score |
|---|---|---|---|---|---|
| **A** | Build phone-first default sequence | +6pp | No cash + 0.5 FTE-wk | 7 days | **Highest** |
| **B** | Enforce "Dial First" via dashboards + manager reviews | +4pp | No cash + 0.3 FTE-wk ongoing | 10 days | **Highest** |
| **C** | Re-route stuck MQLs to an active sequence | +3pp | No cash + 0.2 FTE-wk | 5 days | **Highest** |
| **D** | SDR comp adjustment to reward touch coverage | +2pp | No cash + finance time | 15 days | High |
| **E** | Tier-by-segment sequences (SMB/MM/MM+) | +5pp | No cash + 1 FTE-wk | 30 days | High |
| **F** | SDR discovery training | +3pp | 5K external + 1 FTE-wk | 45 days | High |
| **G** | CSM time-to-first-checkin SLA (45d to 7d) | +4pp | 1 FTE realloc | 30 days | High |
| **H** | Detection-tuning service for SMB onboarding | +3pp | Product+CSM time | 45 days | Medium |
| **I** | Dedicated expansion role | +12pp | 1 FTE hire (180K) | 60 days | Medium |
| **J** | Hire 4 additional SDRs | +6pp | 4 FTE hires (480K) | 90 days | Medium |
| **K** | Major brand campaign | +1pp | 200K+ | 120 days | Low |
| **L** | Replace the SDR manager | +0pp (sometimes negative) | Severance + transition | 60 days | Low / Negative |
| **M** | New product feature dev (specific request) | +1pp | 50K+ | 90 days | Low |
| **N** | Outbound motion launch | +4pp | 150K+ infrastructure | 120 days | Low (this phase) |

---

## Lift/cost ranking visualized

```
TIER 1 (do immediately, near-zero cost):
   A  ████████████████████████████  Phone-first sequence
   B  ███████████████████████░░░░░  Dial-First enforcement
   C  ██████████████████░░░░░░░░░░  Re-route stuck MQLs
   D  ████████████████░░░░░░░░░░░░  SDR comp adjustment

TIER 2 (Phase 2, modest cost):
   E  █████████████████████░░░░░░░  Tier sequences
   G  ████████████████████░░░░░░░░  CSM SLA fix
   F  ███████████████░░░░░░░░░░░░░  SDR training
   H  █████████████░░░░░░░░░░░░░░░  Detection-tuning service

TIER 3 (Phase 3, larger cost):
   I  ████████████████░░░░░░░░░░░░  Expansion role
   J  ███████░░░░░░░░░░░░░░░░░░░░░  Hire 4 SDRs

EXCLUDED (low lift / high cost / wrong sequence):
   K  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░  Brand campaign
   L  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░  Replace SDR manager
   M  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░  Product feature dev
   N  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░  Outbound motion
```

---

## Why the highest-lift items are the cheapest

This is counterintuitive but characteristic of broken systems:

> **When a system has multiple aligned Swiss-Cheese holes, closing the cheapest hole often produces the largest single lift, because every other layer downstream gets to do its job.**

In Sentinel's case:
- The phone-first sequence costs nothing and lifts CR2 by ~4 percentage points
- Hiring 4 SDRs costs 480K and lifts CR2 by ~3 percentage points

The order is operator-counterintuitive but mathematically clean. The diagnostic's job is to SHOW this math before stakeholder politics determines which items get done.

---

## Why some interventions were explicitly excluded

### K: Brand campaign
**Lift: +1pp. Cost: 200K+.** Brand work pays off over 24+ months. The diagnostic's 12-month forecast can't credit material returns. Recommend after Phase 3 is stable.

### L: Replace the SDR manager
**Lift: 0pp (often negative).** The manager is operating within the broken system. Replacement disrupts the team during the highest-leverage 30-day window. Re-evaluate at Day 90 with the system in working order.

### M: Product feature dev
**Lift: +1pp. Cost: 50K+ and a 90-day timeline.** CR4 is at benchmark: the product converts when prospects engage. Product isn't the constraint. Park for the product team's own roadmap.

### N: Outbound motion
**Lift: +4pp. Cost: 150K+ infrastructure.** Real lift, but adding another go-to-market motion while the existing one is broken multiplies operational load. Sequence: fix inbound (Phases 1-2), then consider outbound (Phase 4+).

---

## Sensitivity around the rankings

The ranking changes if assumptions change. Key sensitivities:

| Assumption | If different... | Ranking change |
|---|---|---|
| SDR comp adjustment works | If SDRs don't respond | D drops to Tier 2; rest unchanged |
| Tier sequences improve over a single default | If marginal improvement only | E drops to Tier 3 |
| CSM SLA is enforceable without a hire | If reallocation impossible | G needs +1 FTE budget |
| Expansion role can find revenue in the existing base | If the base is too small | I drops to Tier 3 |
| Hiring SDRs solves capacity vs system issue | If the system isn't fixed first | J becomes negative-lift |

The diagnostic flags each sensitivity in the executive deck so the CRO can defend the prioritization under questioning.

---

## What the matrix produces

This file is the input to the 30-60-90 plan (`action-plan-30-60-90.md`). Every action in the plan is taken from Tier 1 or Tier 2 here. Nothing in the plan is from "EXCLUDED."

The matrix is also the document the CFO uses to challenge the plan: every objection points to a row in this matrix, and we can show the modeled lift vs cost behind each decision.
