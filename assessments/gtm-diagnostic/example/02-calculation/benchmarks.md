# Benchmarks: Sentinel Cloud Defense

**Week 2 deliverable** | Source: illustrative peer-set benchmark, cybersecurity SaaS inbound-motion peers. All numbers fictional; monetary figures in USD.

---

## Benchmark cohort selection

Selected peer set: **18 cybersecurity SaaS companies, 25M-80M ARR, inbound-led motion, US headquartered.**

| Dimension | Peer set range | Sentinel | Position |
|---|---|---|---|
| ARR | 25M-80M | 40.2M | median |
| ACV | 32K-95K | 47K | 40th %ile |
| YoY growth | 18%-110% | 22% | 25th %ile |
| Headcount (S&M) | 22-87 | 48 | 55th %ile |
| Inbound motion % of revenue | 60%-95% | 78% | median |

Sentinel is dead-center in the peer set on size and structure. Direct comparison is valid.

---

## CR benchmarks vs Sentinel (full peer-set distribution)

| CR | Peer p25 | Peer p50 | Peer p75 | Sentinel | Sentinel %ile |
|---|---|---|---|---|---|
| CR1 | 4.2% | 6.5% | 8.1% | 6.8% | 55th |
| **CR2** | **18%** | **22%** | **28%** | **4.0%** | **<5th** |
| CR3 | 81% | 87% | 92% | 88.2% | 55th |
| CR4 | 23% | 27% | 31% | 26.7% | 50th |
| CR5 | 71% | 79% | 86% | 62.5% | 15th |
| CR6 | 82% | 87% | 91% | 80.0% | 20th |
| CR7 | 22% | 26% | 31% | 25.0% | 45th |
| CR8 (NRR) | 105% | 112% | 121% | 102% | 20th |

**Visualization (terminal art for the deck):**
```
CR1  ▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░ (55th)
CR2  ▓░░░░░░░░░░░░░░░░░░░░ (<5th)  CRITICAL
CR3  ▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░ (55th)
CR4  ▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░ (50th)
CR5  ▓▓▓░░░░░░░░░░░░░░░░░░ (15th)  below
CR6  ▓▓▓▓░░░░░░░░░░░░░░░░░ (20th)  below
CR7  ▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░ (45th)
CR8  ▓▓▓▓░░░░░░░░░░░░░░░░░ (20th)  below
```

---

## What the percentile rankings tell us

- **3 of 8 CRs are at or above median**: Sentinel is not broadly underperforming
- **1 CR is catastrophically below the 5th percentile**: CR2 is a uniquely large outlier
- **3 CRs sit at the 15th-20th percentile**: meaningful but recoverable (CR5, CR6, CR8)
- **No CR is above the 75th percentile**: there are no standout strengths to leverage

The pattern is **"one big leak, three small ones, nothing exceptional."** Fix the big leak first; the small leaks become smaller in relative terms once the big one is fixed.

---

## What "moving to benchmark" would mean financially

If Sentinel hit the **median peer** on every CR with identical MQL volume:

| Scenario | Annual ARR |
|---|---|
| Current state | 40.2M |
| All CRs to median | 76M (1.89x) |
| CR2 alone to median | 54M (1.34x) <- realistic Phase 1+2 target |
| CR2 + CR5 to median | 63M (1.57x) <- Phase 1+2+3 stretch |

**The CR2 fix alone clears the stated 58M target.** Right-side work is upside.

---

## Where the benchmarks come from (transparency)

In a real engagement, state exactly where your benchmark data comes from: which peer companies or datasets, what motion and ACV band they cover, and how fresh they are. In this fictional example the peer set is invented, but the disclosure discipline is the point:

- Peer set: **n=18, vintage 2023-2025**, refresh cadence quarterly
- For each CR, the benchmark uses **cohort calculation** at the peer level, not milestone, so comparisons are like-for-like with Sentinel's cohort-first measurement
- Benchmarks are tagged L6 in the source-tier ledger and never presented as if they were the client's own data
