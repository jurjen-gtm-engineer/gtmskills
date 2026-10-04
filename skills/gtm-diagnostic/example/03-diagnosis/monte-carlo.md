# Probabilistic Forecast: Sentinel Cloud Defense

**Week 3 deliverable** | Method: 10,000-run bootstrap simulation, cohort progression sampled from historical variance. A spreadsheet or a short script both work; the discipline is the distribution, not the tooling. Monetary figures in USD.

---

## The question being forecast

**What is the probability distribution of Sentinel's ARR at FY26 close (Q4 2026), under each scenario?**

Stated target: **58M ARR.**

---

## Model inputs

| Parameter | Value | Source |
|---|---|---|
| Starting ARR (Q1 2026 close) | 40.2M | L1 finance system |
| Monthly net-new ARR run rate | 750K (Q4 2025 avg) | L1 finance system |
| MQL inflow run rate | 280/month | L1 marketing automation |
| MQL→Won conversion (composite) | 0.95% | Computed |
| Historical variance sigma | 18% MoM | Bootstrap from 24 months |
| Churn rate | 4% annualized | L1 finance system |
| Expansion rate | 25% of renewable base | L2 finance system |
| Forecast horizon | 9 months (Q2 to Q4 2026) | Stated target |
| Simulation runs | 10,000 | Standard |

---

## Scenarios run

### Scenario 0: Current trajectory (do nothing)

```
P10  ████░░░░░░░░░░░░░░░░░░░░░░░░░░░░  39.1M  (below current)
P25  ██████░░░░░░░░░░░░░░░░░░░░░░░░░░  42.0M
P50  ████████░░░░░░░░░░░░░░░░░░░░░░░░  44.3M  <- median
P75  ██████████░░░░░░░░░░░░░░░░░░░░░░  46.7M
P90  ████████████░░░░░░░░░░░░░░░░░░░░  49.5M
                                       58.0M  <- TARGET (97th %ile, virtually impossible)
```

**Probability of hitting 58M: 3.2%**

The forecast captures the gap between operator confidence and probabilistic reality. DOING NOTHING doesn't get them there, and current operator-side confidence is overstating the probability.

### Scenario 1: Phase 1 only (CR2 fix in 30 days)

Assumes CR2 lifts from 4% to 12% by Day 30, holds. (Conservative; benchmark is 22%.)

```
P10  ████████░░░░░░░░░░░░░░░░░░░░░░░░  44.6M
P25  ███████████░░░░░░░░░░░░░░░░░░░░░  47.8M
P50  ██████████████░░░░░░░░░░░░░░░░░░  50.5M
P75  ████████████████░░░░░░░░░░░░░░░░  53.4M
P90  ███████████████████░░░░░░░░░░░░░  56.9M
                                       58.0M  <- TARGET (92nd %ile, possible)
```

**Probability of hitting 58M: 8.3%**

Phase 1 alone shifts the distribution dramatically but doesn't reliably reach the target.

### Scenario 2: Phase 1 + 2 (CR2 + CR5 fixes by Day 90)

CR2 to 18% by Day 60. CR5 to 75% by Day 90.

```
P10  ███████████░░░░░░░░░░░░░░░░░░░░░  48.2M
P25  ██████████████░░░░░░░░░░░░░░░░░░  51.3M
P50  █████████████████░░░░░░░░░░░░░░░  54.2M  <- median, close to target
P75  ████████████████████░░░░░░░░░░░░  57.0M
P90  ███████████████████████░░░░░░░░░  60.4M
                                       58.0M  <- TARGET (78th %ile)
```

**Probability of hitting 58M: 31%**

The median forecast is 54M: within reach of 58M. The probability of a hit moves from 3% to 31%.

### Scenario 3: Phase 1 + 2 + 3 (add the CR7 fix at Day 90)

CR2 to 22%. CR5 to 80%. CR7 to 30%.

```
P10  ██████████████░░░░░░░░░░░░░░░░░░  52.3M
P25  █████████████████░░░░░░░░░░░░░░░  55.6M
P50  ████████████████████░░░░░░░░░░░░  58.4M  <- target essentially the median
P75  ███████████████████████░░░░░░░░░  61.5M
P90  ██████████████████████████░░░░░░  65.8M
                                       58.0M  <- TARGET (52nd %ile)
```

**Probability of hitting 58M: 54%**

The full three-phase plan brings the target into the median forecast: a coin-flip at minimum, with significant upside.

---

## Comparative probabilities

| Scenario | P(hit 58M target) | P50 ARR | Upside (P90) |
|---|---|---|---|
| 0: Status quo | 3.2% | 44.3M | 49.5M |
| 1: Phase 1 (CR2) | 8.3% | 50.5M | 56.9M |
| 2: Phase 1+2 | 31% | 54.2M | 60.4M |
| 3: Phase 1+2+3 | 54% | 58.4M | 65.8M |

---

## Sensitivity analysis (most-leveraged variables)

Holding Scenario 2 fixed, varying single inputs plus/minus 1 sigma:

| Input | Effect on P50 ARR | Effect on P(hit) |
|---|---|---|
| CR2 actual lift (4 to 18% target) | 54.2M becomes 56.8M / 51.6M | 31% becomes 42% / 22% |
| MQL inflow rate (280/mo, 20% either way) | 54.2M becomes 56.1M / 52.2M | 31% becomes 39% / 24% |
| Time-to-lift on CR2 (60 days, 15 days either way) | 54.2M becomes 55.7M / 52.8M | 31% becomes 37% / 26% |
| Churn rate (4%, 1pp either way) | 54.2M becomes 54.9M / 53.5M | 31% becomes 34% / 28% |
| CR5 lift (62.5 to 75% target) | 54.2M becomes 55.4M / 53.0M | 31% becomes 35% / 27% |

**The most sensitive variable is the CR2 lift itself.** If CR2 only reaches 12% instead of 18% by Day 60, the entire scenario degrades by ~2.6M.

This is also where the highest-leverage operational work sits: every effort to push CR2 above the conservative target compounds throughout the forecast.

---

## Why probabilistic and not deterministic

Most operators run forecasts as a single number. The diagnostic deliberately delivers a probability distribution because:

1. **Growth is stochastic.** Even with perfect execution, cohort progression has natural variance.
2. **Decisions vary by risk tolerance.** A 31% chance of hitting target is a different conversation than a 90% chance, both at the same P50.
3. **Sensitivity matters more than the point estimate.** Knowing CR2 is the most sensitive variable tells the operator where to focus.
4. **It surfaces overconfidence.** The CRO's pre-diagnostic confidence was ~80% on 58M. The model says <5% on status quo. That gap is the diagnostic's value.

---

## Model limitations (linked to the map-limits register)

- **ML-9 applies:** the model uses bootstrapped cohort progression; major motion changes (e.g. moving to outbound-led) would invalidate it
- Sensitivity ranges assume normality of error distributions; heavy-tail risk not modeled
- Doesn't model competitive response (e.g. a competitor matching the recovery)
- Doesn't model macroeconomic regime change

For an L4 forecast, these limits are acceptable. For deeper rigor (board-level capital allocation), recommend stress-testing with adversarial scenarios in a follow-on engagement.
