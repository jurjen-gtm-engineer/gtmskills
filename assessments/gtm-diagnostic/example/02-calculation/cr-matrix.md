# CR Matrix: Sentinel Cloud Defense

**Week 2 deliverable** | Method: cohort-first. Cohort: Q1 2024 MQL cohort (n=843). Monetary figures in USD.

---

## The 8 Conversion Rates: Sentinel vs Benchmark

| CR | Stage | Sentinel | Benchmark (Cybersec SaaS Inbound) | Delta | Flag |
|---|---|---|---|---|---|
| **CR1** | Prospect → MQL | 6.8% | 5-8% | within | healthy |
| **CR2** | **MQL → SQL** | **4.0%** | **20-25%** | **-21pp** | **CRITICAL** |
| **CR3** | SQL → SAL | 88.2% | 85-90% | within | healthy |
| **CR4** | SAL → Won | 26.7% | 25-30% | within | healthy |
| **CR5** | Won → First Impact | 62.5% | 75-85% | -15pp | below |
| **CR6** | First Impact → Renewal | 80.0% | 85-90% | -7pp | slightly below |
| **CR7** | Renewal → Expansion | 25.0% | 25-30% | within | at lower bound |
| **CR8** | NRR proxy | 102% | 110-115% | -10pp | below |

---

## Composite throughput math

**Funnel arithmetic:**
- Sentinel actual: 843 MQLs x 4% x 88% x 27% = **8.0 closed-won**
- At benchmark: 843 x 22% x 87% x 28% = **45.2 closed-won** (5.6x)

**ARR translation (at 47K ACV blended):**
- Actual: **376K** new ARR / cohort
- At benchmark: **2.12M** / cohort
- **Gap: 1.75M per quarter** if CRs hit benchmark on identical MQL supply
- **Annualized leak: ~7M ARR/year** before any MQL-supply increase

---

## CR2 algebraic decomposition

Express the off-benchmark CR as a product of measurable factors, then measure each factor:

```
CR2 = Effort_Rate x Quality_Rate x Cadence_Fit_Rate
```

| Factor | Sentinel observed | Benchmark | Gap |
|---|---|---|---|
| Effort (touch coverage within 5 days) | 47% | 95% | -48pp |
| Quality (touch quality / contact-discovery completeness) | 60% | 75% | -15pp |
| Cadence Fit (% MQLs on phone-first sequence) | 14% | 35% | -21pp |
| **Composite** | **47% x 60% x 14% = 4.0%** | **95% x 75% x 35% = 25%** | matches observed |

**Largest single lever:** Cadence Fit (14% to 35%) = ~2.5x lift on its own. Effort (47% to 95%) = ~2x lift. Stacked, they account for a ~6x CR2 improvement: closing the entire benchmark gap.

---

## CR-by-CR notes

### CR1 (healthy): Marketing supply is fine. Stop saying "we need more MQLs."

### CR2 (critical): **THE PROBLEM.**
Decomposition findings:
- 47% MQLs touched within 5 days (benchmark 95%)
- 9% never touched after 30 days
- 32% stuck in "Working" 30+ days (pipeline rot)
- 22% received any phone call despite the "Dial First" rule (the rule is decorative)
- 71% on the "MQL Email Only" sequence (cadence design failure)
- Avg touches before disqualification: 1.4 (industry norm: 6+)

### CR3 (healthy): When SDRs do convert MQLs, the qualification is real. AEs accept at 88%.

### CR4 (healthy): AE close rate is on benchmark. Sales execution is not the problem.

### CR5 (below): 3 of 8 closed-won stall in "Implemented but not Routine Use." Phase 2 work.

### CR6 (slightly below): Mostly a downstream effect of CR5.

### CR7 (at lower bound): No dedicated expansion role. Phase 3.

### CR8 (below): NRR 102%, recoverable through CR7 work.

---

## Segment cut: where CR2 concentrates

| Segment | MQL volume | CR2 | Note |
|---|---|---|---|
| SMB (<500 emp) | 612 (73%) | 3.4% | Worst CR2, most volume |
| Mid-Market (500-2,500) | 198 | 6.6% | Better but still below |
| Mid-Market+ (2,500+) | 33 | 12.1% | Best: AE-touched directly |

The MM+ CR2 of 12% proves the **qualification model itself works** when applied. The problem is operational coverage of SMB high-volume.

---

## What this tells us before causal modeling

1. Marketing is doing its job (CR1 healthy)
2. AEs are doing their job (CR3 + CR4 healthy)
3. The collapse is at the SDR layer (CR2), specifically SMB volume
4. The right side has modest leaks (CR5, CR7): Phase 2/3, not primary
5. **The CRO's hypothesis ("more MQLs") would funnel more volume into the same broken machine.** The diagnostic refutes the operator instinct with hard math.
