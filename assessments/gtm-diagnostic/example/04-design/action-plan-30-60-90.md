# 30-60-90 Action Plan: Sentinel Cloud Defense

**Week 4 deliverable** | Interventions ordered by **probability lift** (not gap size, not stakeholder volume). Every line has an owner, a leading indicator, and an exit criterion. Monetary figures in USD.

---

## Phase 1, Days 0-30: Fix CR2 (Cadence + Routing + Enforcement)

**Target:** lift CR2 from 4% to at least 12% by Day 30.
**Probability lift:** +5 percentage points (target probability 3% to 8%).
**Estimated investment:** no cash + 1.5 FTE-weeks of RevOps and Sales-Ops time.

| # | Action | Owner | Day | Leading indicator | Exit criterion |
|---|---|---|---|---|---|
| 1.1 | Build phone-inclusive default sequence ("MQL Phone-First v1"): 5 touches over 7 days | RevOps + VP Sales | D1-D5 | Sequence published in the sales engagement platform | Sequence approved by CRO |
| 1.2 | Change MQL routing to assign new MQLs to v1 by default | RevOps | D5 | New MQLs >=80% on v1 | All new MQLs auto-routed |
| 1.3 | Re-route the 270 MQLs currently in "Working" 30+ days to v1 | VP Sales + SDR managers | D6 | Inactive queue cleared | Backlog <50 leads |
| 1.4 | Enforce "Dial First" via weekly manager review of call counts per SDR | VP Sales | D7 (then weekly) | Avg dials/SDR/day >=30 | Sustained for 2 weeks |
| 1.5 | Dashboard: real-time sequence-assignment + touch-coverage by SDR | RevOps | D10 | Dashboard live | All managers using it daily |
| 1.6 | Compensation tweak: 10% SDR bonus tied to touch-coverage SLA | CRO + Finance | D15 | Comp plan amended | Communicated to SDRs |
| 1.7 | Weekly Phase 1 standup with all SDRs to surface obstacles | VP Sales | D8 (weekly) | Attendance 100% | Sustained 4 weeks |
| 1.8 | Day 30 milestone review: measure CR2 on the Days 1-30 cohort | RevOps + diagnostic team | D30 | CR2 measurable | CR2 >=12% continue; <8% diagnose blockers |

### Phase 1 risk register
| Risk | Likelihood | Mitigation |
|---|---|---|
| SDRs resist the call-volume increase | High | Tie comp to it (1.6); manager-driven, not policy-driven |
| Sequence tooling config takes longer than expected | Medium | Backup template ready (manual sequence assignment as fallback) |
| Initial CR2 lift smaller than expected | Medium | Phase 2 work begins anyway; doesn't block sequencing |
| Backlog routing creates SDR overload | Medium | Cap re-routing at 50 leads/SDR/week |

---

## Phase 2, Days 31-60: Cement CR2 + start CR5 (Adoption)

**Target:** CR2 to 18% by Day 60; CR5 to 70%.
**Probability lift:** +23 pp (8% to 31%).
**Estimated investment:** 1 FTE CSM hire OR reallocation; no cash beyond that.

| # | Action | Owner | Day | Leading indicator | Exit criterion |
|---|---|---|---|---|---|
| 2.1 | Sequence library v2: tier-by-segment (SMB / MM / MM+), 3 variants | RevOps + VP Sales | D31-D40 | v2 sequences live | A/B-tested against v1 |
| 2.2 | SDR training on discovery technique (deepen the Quality factor) | VP Sales | D32-D45 | All 12 SDRs trained | 30-day post-training CR2 measured |
| 2.3 | Adoption milestones added to the AE-to-CSM handoff template | VP CS + VP Sales | D35 | Template in use | All new wins use it |
| 2.4 | CSM time-to-first-checkin SLA: 7 days (down from 45) | VP CS | D40 | SLA met for new wins | 90%+ compliance |
| 2.5 | Detection-tuning service: built into onboarding for the SMB tier | VP CS + Product | D45 | Service operational | First 3 customers complete |
| 2.6 | Day 60 milestone review: CR2 + CR5 measured on the Phase 2 cohort | RevOps + diagnostic team | D60 | Both CRs measurable | CR2 >=18% AND CR5 >=70% continue |

### Phase 2 risk register
| Risk | Likelihood | Mitigation |
|---|---|---|
| CSM reallocation creates churn risk on existing accounts | Medium | Phase 2 hires a CSM rather than reallocating from the existing book |
| Tier-segmented sequences add complexity SDRs don't want | Medium | Manager training; tooling guardrails |
| Phase 1 gains erode without continuous management | High | Sustained dashboard + weekly review in Phase 2 |

---

## Phase 3, Days 61-90: Expansion motion (CR7)

**Target:** CR7 to 30% by Day 90.
**Probability lift:** +23 pp (31% to 54%).
**Estimated investment:** either reallocate 1 senior AE or hire a dedicated expansion rep.

| # | Action | Owner | Day | Leading indicator | Exit criterion |
|---|---|---|---|---|---|
| 3.1 | Dedicated expansion role created (reallocation or hire) | CRO | D61 | Role defined | Role filled by D75 |
| 3.2 | Expansion playbook documented (expansion triggers, offers, cadence) | RevOps + diagnostic team | D65 | Playbook complete | Sales team trained |
| 3.3 | Compensation plan for the expansion role | CRO + CFO | D70 | Plan approved | Role-holder accepts |
| 3.4 | Existing-customer base segmented for expansion readiness | CSM team | D75 | All 85 renewables tiered | Tier 1 list (target accounts) prioritized |
| 3.5 | Quarterly expansion campaign launched to Tier 1 | New role + Marketing | D80 | Campaign live | First 3 expansion conversations |
| 3.6 | Day 90 milestone review: full diagnostic re-measurement | RevOps + diagnostic team | D90 | All CRs measurable | Forecast model re-run; decision on Phase 4 |

---

## Probability lift summary

| Phase | Cumulative target | Cumulative probability of hitting 58M |
|---|---|---|
| Status quo | 44M | 3% |
| Phase 1 (Day 30) | 51M | 8% |
| Phase 1+2 (Day 60-90) | 54M | 31% |
| Phase 1+2+3 (Day 90+) | 58M | 54% |

**The plan moves Sentinel from a 3% probability of hitting target to a 54% probability over 90 days.** An 18x improvement on the same MQL supply, same product, same team. No additional CAC.

---

## What this plan deliberately doesn't do

| Tempting addition | Why excluded |
|---|---|
| Hire more SDRs immediately | The system is broken; new hires inherit the breakage. Hire in Phase 2 once the system is working. |
| Increase MQL supply (the CRO's instinct) | More volume into a broken machine = more waste. The CR2 fix delivers 5.6x output on the same supply. |
| Replace the SDR manager | The system caused the outcome. Replacement without a system fix produces the same result with new names. |
| Build new product features | CR4 is at benchmark: the product converts when prospects engage. Product isn't the bottleneck. |
| Major brand investment | Phase 3 follow-on at the earliest. Brand isn't the constraint. |

Each excluded item is a recurring "but what about..." that the diagnostic preempts by being explicit.

---

## Handover (Day 90 deliverable)

At Day 90 we re-measure all CRs, re-run the forecast, and either:
- **Greenlight Phase 4** (full annual operating plan around the working motion), or
- **Re-diagnose** if any phase milestone failed its exit criterion

The 30-60-90 plan is a hypothesis. The data at Day 90 confirms or revises it.
