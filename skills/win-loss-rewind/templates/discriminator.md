# Discriminator: {{client}} / archetype: {{archetype_name}}

**Phase 7 deliverable of win-loss-rewind.** One file per surviving archetype.

Built: {{date}}
Training accounts: {{n_train}} | Holdout: {{n_holdout}}
Outcome definition: positive = won + healthy + expanded; negative = lost + churned

## The archetype, in operational language

> {{one sentence a skeptical buyer would recognise, e.g. "two-state legal-ops shop that just hired its first compliance owner"}}

Not: a headcount band, not a vertical, not a revenue range.

## Scoring rubric

| Signal | Source | Threshold | Weight | Train lift | Holdout lift |
|--------|--------|-----------|--------|-----------|--------------|
| {{signal 1}} | {{provider}} | {{>= 2}} | {{0.55}} | {{4.1x}} | {{3.6x}} |
| {{signal 2}} | {{provider}} | {{present}} | {{0.45}} | {{3.5x}} | {{3.2x}} |

**Combined fit_score:** `{{0.55*I(sig1) + 0.45*I(sig2)}}`

**Looks-like-archetype threshold:** `fit_score >= {{0.60}}`

## What was killed and why

| Candidate | Train lift | Holdout lift | Why killed |
|-----------|-----------|--------------|------------|
| {{vowel-name style coincidence}} | {{2.4x}} | {{~1.0}} | holdout collapse |
| {{gate violation}} | n/a | n/a | used headcount / leaked outcome / no public source |

(If nothing was killed, say so and explain why you still trust the holdout.)

## Stripped leakage columns

{{list: arr, acv, deal_size, close_date, stage, nps, csm_assigned, ...}}

## How to score a new prospect

`python scripts/score_prospect.py --discriminator discriminator.json --domain example.com`

Returns fit_score per archetype and a looks-like boolean.
