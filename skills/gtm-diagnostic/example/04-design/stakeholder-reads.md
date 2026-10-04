# Stakeholder Reads: Sentinel Cloud Defense

**Week 4 deliverable** | Same plan, four perspectives. Each stakeholder gets the slice that lets THEM decide. Monetary figures in USD.

---

## The operator read (CRO + VPs)

**Headline:** *"You can hit 58M ARR with the team you have, on the MQL supply you have. The bottleneck is CR2, fixable in 30 days at near-zero cost."*

### What changes day-to-day
- VP Sales runs a daily standup on touch coverage + dial counts
- RevOps owns the new Phase 1 dashboard
- SDR managers do weekly cadence-mix reviews
- VP CS shifts the CSM motion from reactive to 7-day proactive

### What the operator owns
- Phase 1 execution (Days 1-30)
- The leading indicators (touch coverage, dial counts, sequence mix)
- The exit criteria at each milestone
- Weekly check-ins with the diagnostic team throughout the 90 days

### What success looks like for the operator
- The Q3 board update can show CR2 at 18%+ with proof
- The Q4 board update can show 54M+ ARR (P50 forecast)
- Year-end can show 58M with reasonable confidence

---

## The CFO read

**Headline:** *"This plan moves the probability of hitting 58M from 3% to 54% on a 5K cash outlay + 1 FTE reallocation. Sensitivity-tested across 5 key variables."*

### What the CFO needs to see
- The forecast distribution per scenario (see `03-diagnosis/monte-carlo.md`)
- The sensitivity table (top 5 variables that move the forecast)
- Cash investment by phase (Phase 1: 5K; Phase 2: 1 FTE; Phase 3: 180K)
- ROI math: 14M of probability-weighted incremental ARR for 185K total investment = 76x return

### What the CFO should pressure-test
- "What if CR2 only lifts to 8% instead of 12%?" P50 falls to 48M (still better than the status quo 44M)
- "What if a competitor matches our recovery?" Not modeled; flag for a follow-on engagement
- "What's the worst-case 6-month cash burn?" No change to current burn until the Phase 3 expansion-role hire

### What the CFO commits to
- Approval of Phase 1 + 2 (5K + 1 FTE reallocation)
- Conditional approval of the Phase 3 expansion-role hire, contingent on the Day 60 milestone
- Monthly re-forecast against this model

---

## The CEO read

**Headline:** *"Growth is slowing not because the product or market is wrong, but because we're losing 96% of our marketing-qualified leads at one step. We can fix it in 30 days without hiring or spending more on ads."*

### What the CEO needs to see
- One slide: the bowtie, with CR2 highlighted in red
- One slide: the probability distribution (Status Quo vs Plan)
- One slide: the 30-60-90 phases with cumulative probability lift
- One slide: what we deliberately are NOT doing (and why)

### What the CEO should communicate to the board
- "We diagnosed the bottleneck. It's not lead supply. It's lead conversion at the SDR layer."
- "We have a 90-day plan with three sequential milestones."
- "Each milestone has an exit criterion. If we miss a milestone, we re-diagnose, we don't double down."
- "We expect to be at P50 = 54M by Day 90, with a 31% probability of hitting our 58M target. Phase 3 brings that to 54%."

### What the CEO should NOT say
- "We're going to hire 10 more SDRs." (The diagnostic explicitly excludes this.)
- "We need to spend more on marketing." (CR1 is healthy.)
- "We're pivoting to outbound." (Out of phase.)

---

## The board read

**Headline:** *"Sentinel's growth slowdown is not strategic, it's operational. The diagnostic identifies a single, fixable bottleneck. The plan is sequenced by probability lift, measurable at three 30-day checkpoints, and reversible if assumptions don't hold."*

### What the board needs to see (3 pages max)
- Page 1: Status. Current ARR, current trajectory P50, stated target, gap
- Page 2: Diagnosis. The Swiss-Cheese causal model in one diagram
- Page 3: Plan. 30-60-90 with cumulative probability lift; check-ins at each phase

### What the board pressure-tests
- *"What's the downside scenario?"* Status-quo P10 = 39M (vs 40M today). Even with no plan execution, we don't lose ground meaningfully.
- *"Is the team capable of executing?"* Phase 1 is dashboard + sequence work, achievable by the current team. Phase 2 requires 1 hire. Phase 3 requires 1 hire + role-design work.
- *"What's the diligence on the diagnostic?"* Four-framework methodology (Revenue Architecture + Bowtie Analytics + Growth Architecture + Insight Engineering, concepts from Winning by Design); a source-tier ledger with 73% L1/L2 evidence; a published map-limits register.

### What the board commits to
- Approval of the 90-day plan
- Re-review at Day 90 with a re-measured forecast
- Capital reservation for the Phase 3 expansion-role hire (180K)

---

## Why four reads, not one

Most consultancies deliver one slide deck and expect every stakeholder to find their slice. The result: the CRO reads the CFO's risk slides and gets defensive; the CFO reads the operator's task list and demands cost detail; the CEO reads everything and gets paralyzed by detail.

**The four-read approach applies the Pyramid Principle plus audience-first storyboarding.** Each stakeholder gets the slice that lets THEM decide. They can read more if they want, but they don't NEED to.

This is also what makes the deliverable feel like a premium engagement rather than a thin audit. The artifact respects the time of each consumer.

---

## File mapping to deliverables

| Stakeholder | Primary deliverable | Supporting |
|---|---|---|
| Operator (CRO + VPs) | `05-deliver/operator-runbook.md` | All Week 1-4 working files |
| CFO | `05-deliver/board-appendix.md` | `monte-carlo.md`, `source-tier-ledger.md` |
| CEO | `05-deliver/executive-deck.md` | Operator runbook for detail |
| Board | `05-deliver/executive-deck.md` (3-page extract) + `board-appendix.md` | none |
