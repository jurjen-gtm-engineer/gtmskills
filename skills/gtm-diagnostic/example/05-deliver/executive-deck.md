# Executive Deck: Sentinel Cloud Defense

**Week 5 deliverable** | 8-page deck using Pyramid structure + storyboarding. Each slide = one idea, answer-first, supported by evidence-rated data. Markdown is the source of truth; the rendered version goes to slides or PDF. Monetary figures in USD.

---

## Slide 1: Title

**SENTINEL CLOUD DEFENSE**

**FY26 GTM Diagnostic: Findings and 90-Day Plan**

Prepared by the diagnostic team · Sprint window: May 13 to June 17, 2026 · Tier: Pro

---

## Slide 2: The headline (answer first)

> **Sentinel can reach 58M ARR by FY26 close, with the team it has, on the leads it gets today, by fixing one conversion step.**

The growth slowdown is not a strategic problem.
It's an operational one.
And it's fixable in 30 days.

*[Footer: Source-tier 73% L1/L2 evidence · Map-limits register attached · Four-framework methodology]*

---

## Slide 3: The diagnostic in one diagram

```
Bowtie Conversion Performance (Q1 2024 cohort, n=843 MQLs)

CR1   ok        6.8%      (Benchmark 5-8%)        Marketing supply is fine
CR2   CRITICAL  4.0%      (Benchmark 20-25%)      THE BOTTLENECK
CR3   ok        88%       (Benchmark 85-90%)      Handoff works
CR4   ok        27%       (Benchmark 25-30%)      AEs close on benchmark
CR5   below     62%       (Benchmark 75-85%)      Adoption gap (Phase 2)
CR6   below     80%       (Benchmark 85-90%)      Slight renewal weakness
CR7   ok        25%       (Benchmark 25-30%)      Expansion at lower bound
CR8   below     102%      (Benchmark 110-115%)    NRR recoverable
```

**One step (MQL to SQL) loses 96% of our marketing-qualified leads.**
The benchmark loses 75%.
The 21-percentage-point gap is what makes every other problem secondary.

*[Footer: Full cohort data in 02-calculation/cr-matrix.md]*

---

## Slide 4: Why it's happening (root cause)

The CR2 collapse is **not** a single failure. It's four aligned layers:

| Layer | What's broken | Evidence |
|---|---|---|
| **Routing** | MQLs sit in the "Working" queue | 32% untouched after 30 days |
| **Effort** | Too few touches per MQL | 1.4 avg vs benchmark 6+ |
| **Cadence** | Default sequence is Email-Only | 71% of MQLs receive no call |
| **Enforcement** | "Dial First" policy not enforced | 22% receive a call despite the rule |

**No single fix solves it.** All four layers must close.

But three of the four are near-zero-cost.

*[Footer: Full causal model in 03-diagnosis/causal-model.md]*

---

## Slide 5: What we deliberately are NOT doing

Common operator responses that the data REFUTES:

| Tempting | Status | Why |
|---|---|---|
| Hire more SDRs | Phase 2 only | New hires inherit a broken system |
| Increase MQL supply | Out of scope | CR1 is healthy; more volume = more waste |
| Replace the SDR manager | Out of scope | The manager operates within the broken system |
| Build new product features | Out of scope | CR4 is at benchmark; the product converts when prospects engage |
| Major brand campaign | Phase 4+ | Pays off over 24mo, too slow for this forecast |
| Launch outbound motion | Phase 4+ | Fix inbound before adding a parallel motion |

**The plan is what the data supports, not what's loudest.**

*[Footer: Full lift/cost matrix in 04-design/probability-lift-matrix.md]*

---

## Slide 6: The 90-day plan

```
Phase 1 (Days 0-30)        Phase 2 (Days 31-60)       Phase 3 (Days 61-90)
─────────────────────      ─────────────────────       ─────────────────────
Fix CR2 system layers      Cement CR2 + fix CR5        Build expansion motion

• Phone-first sequence     • Tier-by-segment           • Dedicated role
• Re-route stuck MQLs        sequences                 • Expansion playbook
• Enforce Dial-First       • SDR discovery training    • Quarterly campaign
• Touch-coverage dash      • CSM 7-day SLA             • Tier-1 base targeted
• Comp tweak               • Detection-tuning service

CR2: 4% to 12%             CR2: 12% to 18%             CR5: 70% to 80%
                           CR5: 62% to 70%             CR7: 25% to 30%

Cost: 5K + 0.5 FTE-wk      Cost: 1 FTE realloc         Cost: 1 FTE hire (180K)
```

Each phase has a **measurable exit criterion.** Miss one: re-diagnose, don't double down.

*[Footer: Full plan in 04-design/action-plan-30-60-90.md]*

---

## Slide 7: Probability of hitting the 58M target

```
                Status Quo    Phase 1     Phase 1+2    Phase 1+2+3
                ───────────   ─────────   ──────────   ───────────
P10 (low)       39M           45M         48M          52M
P50 (median)    44M           51M         54M          58M  <-
P90 (high)      50M           57M         60M          66M

P(hit 58M)      3%            8%          31%          54%
                                                       └── 18x lift
```

**The plan moves Sentinel from a 3% probability of hitting target to a 54% probability over 90 days.**

Same MQL supply. Same product. Same team (until Phase 3).

*[Footer: Full forecast in 03-diagnosis/monte-carlo.md]*

---

## Slide 8: Decision needed today

| Decision | Approver | Cost | Outcome |
|---|---|---|---|
| Approve Phase 1 (start Day 1 of next sprint) | Maya (CRO) | 5K + 0.5 FTE-wk | CR2 to 12% by D30 |
| Approve Phase 2 (conditional on the D30 review) | Maya + Michelle (CFO) | 1 FTE realloc | CR2 to 18%, CR5 to 70% by D60 |
| Approve the Phase 3 expansion-role hire | Maya + Michelle | 180K (annualized) | CR7 to 30% by D90 |

**Recommended:** approve Phase 1 + 2 today. Phase 3 contingent on the Day 60 review.

**Pre-committed re-review:** Day 90 full diagnostic re-measurement. Phase 4 (annual operating plan) launched only if the Day 90 milestone holds.

---

## Appendix slides (deck back-matter)

| Appendix | What it contains |
|---|---|
| A. Methodology | Four-framework stack overview |
| B. Source-tier ledger | 213 ledger entries, evidence grades |
| C. Map-limits register | 13 known limitations |
| D. CR decomposition | Algebraic factor analysis for CR2 + CR5 |
| E. Sensitivity table | 5 most-sensitive variables |
| F. Risk register | Phase-by-phase risks + mitigations |
| G. Comparable benchmark peer set | 18 cybersecurity SaaS companies, anonymized |
| H. Operator runbook | Day-by-day execution playbook |

Each appendix has its own deep-dive markdown file in the engagement folder.

---

## Speaker notes: what to say at each slide

**Slide 2 (Headline):** *"Maya, you came to this engagement with one hypothesis: we need more MQLs. The data says something different, and better, because it means you can hit your target without spending more on marketing."*

**Slide 3 (Bowtie):** *"Walk through each CR. Land on CR2. Say: 'This is where 96% of your marketing-qualified leads die. Not where the diagnosis ends: where it begins.'"*

**Slide 4 (Root cause):** *"Don't accept 'one cause.' The diagnostic explicitly tested five single-cause hypotheses; all five were refuted by the data. The Swiss-Cheese model is what the data actually supports."*

**Slide 5 (Not doing):** *"This is the slide you'll come back to most often when the board asks 'why aren't we doing X?' Every item here is a question the data answered."*

**Slide 6 (Plan):** *"Don't read every bullet. Read the exit criteria. Each phase has a measurable check at the end. We don't proceed unless the previous phase delivered."*

**Slide 7 (Probability):** *"This is the slide your CFO will use to defend the plan to your board. 3% to 54% on a 185K investment is a 76x return if you weight by probability."*

**Slide 8 (Decision):** *"Three approvals. Today. Phase 1 and 2 are no-regret moves. Phase 3 is contingent: we hold the option open."*
