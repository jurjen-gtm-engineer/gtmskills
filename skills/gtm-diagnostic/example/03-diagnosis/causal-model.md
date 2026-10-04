# Causal Model: Sentinel Cloud Defense

**Week 3 deliverable** | Method: Swiss Cheese layered causality. Multiple failure layers align to produce the observed CR2 of 4%.

---

## The Swiss Cheese diagram (text-rendered)

```
INPUT (MQLs at 843/quarter, decent quality)
            ↓
┌───────────────────────────────────────────┐
│  LAYER 1: ROUTING                         │
│  Hole: MQLs sit in "Working" queue        │
│  Effect: 32% MQLs untouched 30+ days      │
└───────────────────────────────────────────┘
            ↓ (68% pass)
┌───────────────────────────────────────────┐
│  LAYER 2: EFFORT/CAPACITY                 │
│  Hole: 1 SDR per 71 MQLs (benchmark 45)   │
│  Effect: Touches = 1.4 avg vs 6+ benchmark│
└───────────────────────────────────────────┘
            ↓ (~50% receive multi-touch)
┌───────────────────────────────────────────┐
│  LAYER 3: CADENCE DESIGN                  │
│  Hole: 71% on "Email Only" sequence       │
│  Effect: Mode of communication wrong      │
└───────────────────────────────────────────┘
            ↓ (~14% on phone-included)
┌───────────────────────────────────────────┐
│  LAYER 4: MANAGEMENT ENFORCEMENT          │
│  Hole: "Dial First" policy exists but     │
│        only 22% MQLs ever receive a call  │
│  Effect: Policy is theater                │
└───────────────────────────────────────────┘
            ↓
OUTPUT: CR2 = 4.0% (vs 25% benchmark)
```

**All four holes must close for the benchmark to be reached.** Closing any one in isolation produces partial lift.

---

## Single-cause diagnoses we ruled out (and why)

The diagnostic deliberately tests obvious single-cause hypotheses before settling on the layered explanation.

| Single-cause hypothesis | Argument for | Why rejected |
|---|---|---|
| "MQL quality is bad" | If MQLs are low-intent, low CR2 follows | CR1 is at benchmark; the MM+ segment converts at 12%. Quality is fine when reps actually engage |
| "We need more MQLs" (CRO hypothesis) | Adding more leads to a stable funnel produces more wins | But the funnel isn't stable. Adding more leads to the same broken machine multiplies waste, not output |
| "SDRs are bad / need replacing" | Variable performance suggests a skill gap | The Quality factor (60% vs 75%) accounts for ~15pp of gap: meaningful but not the dominant cause |
| "We don't have enough SDRs" | 1:71 ratio vs benchmark 1:45 | Real, but capacity alone explains only about half the Effort gap. Even with full headcount the cadence is still wrong |
| "The product is undifferentiated" | Could explain low conversion | But CR4 is healthy: AEs close at benchmark. The product converts when prospects actually engage |
| "Sales-Marketing misalignment" | Common diagnosis at this stage | CR3 (SQL acceptance) is 88%: alignment is fine. The breakage is upstream of the handoff |

**None of the single-cause hypotheses survive the data.** Only the layered Swiss-Cheese explanation does.

---

## Pareto rank of contributing factors

```
Pareto of CR2 gap (factors contributing to the -21pp deficit vs benchmark):
┌──────────────────────────────────────────────────────┬─────────┐
│ Cadence Fit (Email-Only default)                     │  35%   │
│ Effort (touch coverage <5 days)                      │  28%   │
│ Routing (MQLs parked in queue)                       │  18%   │
│ Quality (touch quality / discovery completion)       │  11%   │
│ Management enforcement of "Dial First"               │   5%   │
│ Other / unattributed                                 │   3%   │
└──────────────────────────────────────────────────────┴─────────┘
                                                        81%  <-  Pareto 80/20
```

The top 3 factors account for **81% of the gap.** Phase 1 must target all three.

---

## Why this isn't an SDR problem

**The diagnostic deliberately resists "blame the SDRs."** The 12 individual SDRs are operating within a system that:
- Doesn't route them leads in a timely way
- Defaults their sequences to Email-Only
- Doesn't enforce its own "Dial First" policy
- Has a 1:71 ratio that exceeds anyone's individual bandwidth

In a system this misaligned, the best SDR in the world would still produce a CR2 of ~8-10%, not 25%. Replacing people without fixing the system reproduces the same outcome with new names.

This framing matters for client buy-in. The CRO will want to fire someone. The diagnostic redirects to fixing the layers.

---

## What this means for the action plan

The recommendations in `04-design/` are sequenced by Swiss-Cheese layer:

1. **Layer 4 first** (Management enforcement): cheap, fast, signals seriousness. *Day 1*
2. **Layer 3 next** (Cadence design): build a new sequence library, change defaults. *Week 2 of Phase 1*
3. **Layer 1 third** (Routing): fix queue logic so MQLs don't park. *Week 3 of Phase 1*
4. **Layer 2 last** (Capacity): hire after the other layers prove the system works. *Phase 2*

**This ordering is counterintuitive.** Most operators reach for hiring (Layer 2) first because it's the most visible. The data says hire AFTER the system is working; otherwise new SDRs inherit the same broken machine and produce the same result.
