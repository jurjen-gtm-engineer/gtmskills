# Outcome leakage: the strip list

A feature leaks if it exists *because* the customer bought. Train on it and your
discriminator predicts the past instead of the future. Strip every one of these
in Phase 1, before clustering or hypothesis generation sees the data.

| Column / pattern | Why it leaks |
|------------------|--------------|
| ARR / ACV / MRR | only exists after a contract |
| deal_size / contract_value | post-sale artifact |
| close_date (as a feature) | encodes that they closed; fine only as a window marker to look back from |
| pipeline stage | a record of the sale progressing |
| NPS / CSAT | only collected from customers |
| CSM assigned / owner | only assigned after close |
| seat count / plan tier | provisioned after purchase |
| renewal date / expansion flag | post-sale |
| any "customer since" tenure | definitionally post-sale |

## Two subtler traps

1. **Firmographics are not leakage, but they are forbidden anyway.** Headcount, industry, revenue, country, funding. They do not leak the outcome, but they are inputs, not signals: cluster or score on them and you just rebuild the Apollo filter. Strip from clustering and from the final rubric.

2. **Enrichment captured "now" instead of "then".** If you pull a signal as it looks today, for a customer that bought 2 years ago, you may be capturing a state that the *purchase itself* caused (e.g. they now run your category of tool). Prefer point-in-time, pre-outcome signals. When you cannot get point-in-time, prefer signals unlikely to be caused by the purchase.

## Gate-5 check (hypothesis phase)

Before a candidate signal ships, ask: "could this value only be true because they already became a customer?" If yes, reject it as leakage even if its lift looks great.
