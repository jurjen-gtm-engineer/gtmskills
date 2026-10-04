# Win-Loss Rewind: outcome-data intake

Send this to whoever owns the CRM (or pull the export yourself) before running the skill. Without an outcome-labeled customer export, win-loss-rewind cannot run. A prospect list or a TAM export is not enough.

## What is needed (one row per account)

| Field | Required | Why |
|-------|----------|-----|
| Company name | yes | identity |
| Website domain | yes | the join key for every public-data enrichment |
| Outcome | yes | one of: won, lost, healthy, churned, expanded |
| Outcome date | strongly preferred | lets the analysis look back 6-18 months *before* the outcome, which is where the signal lives |
| First contact / deal-created date | preferred | defines the pre-purchase window |
| Closed-lost reason (if lost) | nice to have | sharpens the negative class |

## What must NOT be in the training file

These are outcome leakage. They exist *because* the customer bought, so a model that uses them just predicts the past:

- ARR / ACV / MRR / deal size / contract value
- Close date as a feature (date is fine as a window marker, not as a signal)
- Pipeline stage, NPS, CSM assigned, seat count, plan tier

The skill also does not cluster or score on headcount, industry, or revenue. Those are inputs, not signals. Include them only if convenient for sanity checks; they will be stripped before modelling.

## Optional but high value

- Call transcripts or call notes per account (feeds Phase 4 pain themes). Gong / Fireflies export, or even rep notes.
- Date of each call.

## Volume guidance

- Minimum useful: ~40 labelled accounts (so a 20% holdout leaves ~8, with ~4 per class). Below this the holdout is too thin to validate.
- Healthy: 100+ labelled accounts across won/lost/churned.
- If the export is mostly "healthy" with no real losses/churns, say so. A discriminator needs a negative class.

## Where it comes from

- Export from the CRM of the company whose ICP you are building (HubSpot, Salesforce, Pipedrive, Attio).
- If you are an agency: your own CRM holds your deals with the client, not the client's customers. The customer outcome export must come from the client's own CRM.
