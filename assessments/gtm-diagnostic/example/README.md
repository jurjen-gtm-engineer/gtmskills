# GTM Diagnostic, Worked Example: Sentinel Cloud Defense

> **THIS IS A DEMO.** "Sentinel Cloud Defense" is a fictional company. Every person, number, and quote in this folder is invented; the figures are constructed to be realistic for the archetype (a mid-size cybersecurity SaaS with an inbound motion). The bowtie, CR1-CR8, and cohort-measurement concepts come from Winning by Design's frameworks; this worked example is an original illustration, not course material. Use it as a template for what a real engagement deliverable looks like, never as real customer data. All monetary figures are in USD.

---

## The case in one paragraph

Sentinel Cloud Defense ("Sentinel") is a cybersecurity SaaS at 40M ARR with a 47K average ACV. Growth has slowed from 80% YoY two years ago to 22% YoY. The CRO believes "we need more MQLs." The data says the opposite: **MQL volume is healthy at ~850/quarter, but only 4% of MQLs become SQLs vs a 25% benchmark.** The growth target is 58M ARR by Q4 (a 45% lift) and on the current trajectory the P50 forecast is 44M. This diagnostic identifies the dominant cause (SDR cadence + routing collapse, not lead supply), sequences three interventions by probability lift, and forecasts a P50 of 54M after Phase 1 + 2 (90 days).

---

## Directory structure

```
example/
├── README.md                              <- you are here
├── 00-CASE-BRIEF.md                       <- cover sheet for the engagement
├── 01-intake/
│   ├── normalized-bowtie.md
│   ├── source-tier-ledger.md
│   └── map-limits.md
├── 02-calculation/
│   ├── cr-matrix.md
│   ├── benchmarks.md
│   └── decomposition-notes.md
├── 03-diagnosis/
│   ├── causal-model.md
│   ├── issue-tree.md
│   └── monte-carlo.md
├── 04-design/
│   ├── action-plan-30-60-90.md
│   ├── probability-lift-matrix.md
│   └── stakeholder-reads.md
└── 05-deliver/
    ├── executive-deck.md
    ├── operator-runbook.md
    └── board-appendix.md
```

## How to read it

| If you are... | Start with |
|---|---|
| The operator (RevOps / VP Sales / CRO) | `05-deliver/operator-runbook.md`: what to do Day 1 / Day 30 / Day 60 / Day 90 |
| The CFO | `05-deliver/board-appendix.md`: forecast + sensitivity + source-tier evidence |
| The CEO / board | `05-deliver/executive-deck.md`: pyramid-structured 8-page deck |
| A consultant studying the method | `00-CASE-BRIEF.md` then `01-intake/` then `02-calculation/` then `03-diagnosis/` |
| A skeptic | `01-intake/source-tier-ledger.md` + `01-intake/map-limits.md`: every number's evidence |

## What's different from a real engagement

| Real engagement | This demo |
|---|---|
| Pulls live data from CRM/finance/product analytics | Numbers invented to fit the archetype |
| Includes 6-10 stakeholder interviews | Interview quotes are illustrative |
| The forecast runs a real bootstrap simulation on the client's actual cohorts | Numbers shown with realistic variance |
| Source-tier ledger has hundreds of rows | This ledger has the representative rows |
| Final deliverable is a 30-50 slide deck + appendices | This shows the markdown source the deck would render from |

Everything else (the framework stack, the calculation order, the Swiss-Cheese diagnostic, the probability-lift sequencing, the stakeholder-tier deliverables) is identical to a real engagement.
