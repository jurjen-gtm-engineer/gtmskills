# Decomposition Notes: Sentinel Cloud Defense

**Week 2 deliverable** | Algebraic decomposition of off-benchmark CRs.

---

## Why decompose

A single CR number is a symptom. The decomposition turns it into testable factors. Without decomposition, the recommendation is "improve CR2": useless. With decomposition, the recommendation is "lift Cadence Fit from 14% to 35% by switching the default sequence from Email-Only to Dial-First."

The diagnostic only decomposes CRs that are **more than 10 percentage points off benchmark** or in the bottom quartile.

---

## CR2 (MQL → SQL): full decomposition

### Algebraic structure
```
CR2 = Effort x Quality x Cadence_Fit
```

Where:
- **Effort** = % of MQLs with at least 1 meaningful touch within 5 business days
- **Quality** = % of touched MQLs that receive a contact-discovery-complete touch (not just a generic open-ended email)
- **Cadence Fit** = % of MQLs on a sequence that includes phone calls

### Factor measurements

| Factor | Sentinel | Benchmark | Gap | Root |
|---|---|---|---|---|
| Effort | 47% | 95% | -48pp | Capacity + routing |
| Quality | 60% | 75% | -15pp | Training + script standardization |
| Cadence Fit | 14% | 35% | -21pp | Sequence library + manager enforcement |

### Composite check
- 47% x 60% x 14% = 3.95%, approximately the observed 4.0% (checks out)
- 95% x 75% x 35% = 24.9%, approximately the benchmark 25% (checks out)

### Hypotheses generated (tested in Week 3)

| # | Hypothesis | Test |
|---|---|---|
| H1 | Effort gap is capacity-driven (too few SDRs) | Calculate SDR:MQL ratio. Sentinel has 1 SDR per 71 MQLs/qtr; benchmark is 1 per 45. Plausible but not the WHOLE story. |
| H2 | Effort gap is routing-driven (MQLs sit in queues) | 32% of MQLs in "Working" 30+ days = leads parked, not actively worked. Routing logic broken. |
| H3 | Quality gap is training-driven | 1.4 avg touches before disqualification = SDRs giving up after 1 attempt. Training/process issue. |
| H4 | Cadence Fit gap is policy-not-enforced | A "Dial First" rule exists; only 22% receive a call. Management enforcement failure. |
| H5 | Cadence Fit gap is template-driven | 71% of MQLs on the "MQL Email Only" sequence = the default option is wrong. |

H2, H4, H5 are the strongest candidates. H1 is real but secondary. H3 is a longer-cycle fix.

---

## CR5 (Won → First Impact): partial decomposition

### Algebraic structure
```
CR5 = Implementation_Completion x Activation_Achievement
```

Where:
- **Implementation Completion** = % of won customers whose deployment is finished within 60 days
- **Activation Achievement** = % of implementation-complete customers who reach "Routine Use" (>=5 active users + >=3 detections triaged)

### Factor measurements

| Factor | Sentinel | Benchmark | Gap |
|---|---|---|---|
| Implementation Completion | 92% | 95% | -3pp (close) |
| Activation Achievement | 68% | 84% | -16pp |

**Diagnostic:** the leak is not deployment, it's adoption after deployment. 3 of 8 closed-won customers have working software but aren't using it meaningfully.

### Hypotheses

| # | Hypothesis | Test |
|---|---|---|
| H6 | CSM coverage is reactive, not proactive | Average time from go-live to first CSM check-in: 45 days. Benchmark: 7 days. |
| H7 | "Routine Use" criteria not communicated at sale | The AE post-sale handoff template lacks adoption milestones. Confirmed via document review. |
| H8 | Product detection-tuning is left to the customer | Customers are expected to self-configure detections; 5 of 8 didn't complete tuning. Service gap. |

**Conclusion:** the CR5 lift requires a CSM motion change, not a product change. Phase 2 work.

---

## CR8 (NRR proxy): no decomposition, sample too small

NRR of 102% at 40M ARR comes from ~85 renewable accounts in Q1 2025. Within that, decomposition into expansion-rate x downsell-rate x churn-rate has confidence intervals too wide to be actionable yet.

**Recommendation:** re-decompose at the end of Phase 2 (90 days) when the sample grows. Flag for re-measurement.

---

## CR1, CR3, CR4, CR6, CR7: not decomposed (in-band)

These CRs are within benchmark range. Decomposing them is not actionable for this engagement. Notes for the future:
- CR4 is at the 50th percentile; moving to the 75th would require AE-skills work. Out of scope this sprint.
- CR7 is at the lower bound of benchmark: a Phase 3 candidate after CR5 is fixed.

---

## What the decomposition unlocks

The recommendations table in `04-design/action-plan-30-60-90.md` is built directly from this decomposition. Every recommendation cites a specific factor in the CR2 or CR5 decomposition that it lifts.

This is what separates a GTM diagnostic from a generic audit: **the recommendations are derived, not asserted.**
