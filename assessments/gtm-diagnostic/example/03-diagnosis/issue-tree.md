# Issue Tree: Sentinel Cloud Defense

**Week 3 deliverable** | MECE issue tree rooted at the stated growth question. Monetary figures in USD.

---

## Root question

**"How does Sentinel reach 58M ARR by close of FY26?"**

Decomposed MECE (mutually exclusive, collectively exhaustive):

---

## Level 1: How to grow ARR

```
Reach 58M ARR
├── (A) Acquire more new ARR
│   ├── Increase MQL supply
│   ├── Improve MQL→Won conversion (CR2 x CR3 x CR4)
│   └── Increase ACV per Won deal
├── (B) Retain more existing ARR
│   ├── Reduce churn (improve CR6)
│   └── Reduce contraction
└── (C) Expand more from existing customers
    ├── Improve adoption/Impact (CR5)
    ├── Build dedicated expansion motion (CR7)
    └── Increase expansion ACV per account
```

---

## Level 2: Branch (A.2) "Improve conversion": which CR?

```
Improve conversion CR2 x CR3 x CR4
├── CR2 (MQL→SQL): currently 4% (benchmark 25%)   <- 6x gap
│   ├── Routing (Layer 1)
│   ├── Effort (Layer 2)
│   ├── Cadence (Layer 3)
│   └── Enforcement (Layer 4)
├── CR3 (SQL→SAL): currently 88% (benchmark 87%)  <- in-band
│   └── No action, preserve
└── CR4 (SAL→Won): currently 27% (benchmark 27%)  <- in-band
    └── No action, preserve
```

**CR2 is the only conversion factor with a material gap.** The tree prunes here.

---

## Level 3: Branch (CR2.Layer 3) "Cadence"

```
Cadence (Layer 3): 71% of MQLs on Email-Only
├── Sequence library
│   ├── No phone-inclusive default sequence exists  <- root cause
│   └── Manager-approved sequences are 5 years old
├── Default selection logic
│   ├── New MQLs auto-assigned to "Standard Email" template
│   └── No tier-based routing (SMB / MM / MM+)
└── Manager visibility
    ├── No dashboard showing sequence-assignment %
    └── No weekly review of cadence mix
```

**The root cause of Layer 3 is the absence of a phone-inclusive default sequence in the library.** A single fix unlocks the layer.

---

## Pruned branches (and why)

The diagnostic deliberately prunes branches that are out of scope OR not the dominant cause:

| Branch | Status | Why pruned |
|---|---|---|
| (A.1) Increase MQL supply | Pruned | Refuted by data; the CR2 fix produces 6x more wins on the same supply |
| (A.3) Increase ACV per Won deal | Phase 3 | Real opportunity (CR4 sits at the 50th %ile) but slower payoff than the CR2 fix |
| (B.1) Reduce churn | Out of scope | NRR work; separate engagement |
| (B.2) Reduce contraction | Out of scope | Sample too small to diagnose |
| (C.1) Improve adoption / CR5 | **Phase 2** | Real issue (CR5 at 15th %ile); recommended for the 60-90 day window |
| (C.2) Build expansion motion / CR7 | **Phase 3** | Real opportunity but requires Phase 1+2 first |
| (C.3) Increase expansion ACV | Out of scope | Sub-branch of (C.2); addressed when (C.2) launches |

---

## Sequencing logic from the tree

The pruned tree directly produces the phased plan:

| Phase | Tree branch | Window | Owner |
|---|---|---|---|
| **Phase 1** | CR2 x {Cadence + Routing + Enforcement} | 30 days | VP Sales + RevOps |
| **Phase 2** | CR5 x {CSM proactive coverage + adoption milestones} | 60 days | VP CS + Product |
| **Phase 3** | CR7 x {Dedicated expansion motion} | 90 days | CRO |

---

## Why the issue-tree exercise matters

Without the tree:
- The recommendations look like an unprioritized wishlist ("fix CR2, fix CR5, fix CR7, hire more SDRs, redo cadences, train CSMs...")
- Stakeholders argue about which to do first based on volume, not value
- Branches that AREN'T the bottleneck still consume planning attention

With the tree:
- The plan is sequenced by structural logic
- Out-of-scope items are explicitly named (so they don't return)
- The CRO can defend the prioritization to her board with a single page

This is the **Pyramid Principle** in action: answer first, support after.
