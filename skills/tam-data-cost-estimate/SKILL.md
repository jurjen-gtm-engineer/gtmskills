---
name: tam-data-cost-estimate
description: Triggers when a user wants to know what it will cost in data to map or source a market before building it, with phrasings like "what will this TAM cost", "price the list build", "data cost for 3,000 accounts", "estimate enrichment spend for this market", or "put a data budget in the proposal". Owns the row math (accounts, qualifying titles per account, priced fields, refresh) and the three numbers for a proposal, one-off build data, monthly run data and tool subscriptions, each as a range. Not for enriching records you already own in a CRM (crm-enrichment-cost-estimate), not for sizing the market itself, and not for sending volume or mailbox cost.
metadata:
  version: "1.0"
---

# TAM Data Cost Estimate

## Trigger

Apply this skill when a market is about to be sourced from scratch and someone needs the data cost first. Before you map a market, price it.

## Scope

This skill prices data. It covers company rows, contact rows, the fields on each that carry a unit cost, and the monthly run. It does not price people's time, the sending tools' usage, or records the client already owns.

## Inputs

Ask for these, and write down the ones you had to assume:

- Accounts in scope, split by tier when tiers exist.
- Qualifying titles per account, per tier. Count the titles that qualify. Do not use a flat "5 per account".
- The field list per object (company or contact), with a low and a high unit cost from the provider's own price list, and expected coverage.
- Refreshes per year per field, and new accounts per month.
- Tool subscriptions the client holds, per month.

## Roles

The user owns the scope and the provider prices. The agent does the row math with the script and never invents a unit cost. A price that was not checked against a live price list is marked as an assumption.

## Procedure

1. Fill a scope file in the shape of `examples/scope.json`.
2. Run `python3 scripts/estimate.py --scope scope.json --out estimate.md`.
3. Read the flags. A field priced above its band, or a field over the gate (250 by default) with no cheaper alternative named, needs an answer before the estimate goes out.
4. Run the five checks below against the scope and change the scope when one applies. Then run the script again.
5. Hand over the three numbers with the scope they assume.

The row math the script uses:

```
Company rows   = accounts in scope
Contact rows   = accounts x qualifying titles per account
Field cost     = rows x coverage x unit cost
Monthly rows   = new accounts per month + rows x refreshes per year / 12
```

Contact rows are where estimates blow up. Twelve qualifying titles instead of five more than doubles contact sourcing and verification. Weight by tier before you price: the full buying group on Tier 1, the decision maker only on Tier 3.

**Price bands (sanity check only, your provider's price list wins):**

| Band | Per row | Examples |
|---|---|---|
| `free` | 0 | Your own CRM and history, public registries, a plain website fetch |
| `cheap_deterministic` | 0.005 to 0.03 | Standard company enrichment, lookalike sourcing, domain resolution |
| `llm_research` | 0.003 to 0.05 | A small model reading a scraped page |
| `contact_email` | 0.03 to 0.15 | Waterfall email finding, verification |
| `premium` | 0.15 to 0.60 | Mobile numbers, multi-provider waterfalls, deep research agents |

**Five checks that move the number:**

- **Registry before aggregator.** Check whether a public registry covers the market before you price a paid source.
- **Broad at the source, sharp after.** Source wide, qualify with cheap filters, and spend on expensive fields only for what survives.
- **Enrich before you score.** Scoring on partial data produces a tier you have to redo, and you pay twice.
- **Verify only what gets contacted.** Verification across the whole list is the classic silent overspend.
- **Two or three providers, then qualify.** Good checks on average data beat one expensive provider with none.

## Outputs

`estimate.md` with the scope, every priced field, and three numbers:

| Line | What it covers |
|---|---|
| **One-off build data** | The full mapping and enrichment run, once |
| **Monthly run data** | New accounts plus the refreshing fields, per month |
| **Tool subscriptions** | Contracted by the client directly |

Quote a range at scoping and one number once the field list is locked.

## Exceptions

No unit cost from a real price list: stop and ask, or mark the field as an assumption in the output. Usage priced in credits instead of money: convert with the plan's price per credit first, or use `crm-enrichment-cost-estimate` for Clay credits and actions.

## QC

- Every priced field has a low and a high unit cost with a named source.
- Contact rows come from titles per account per tier, not from a flat multiplier.
- Every flag in the output has an answer.
- The scope is printed under the numbers, so a change in scope visibly changes the number.

## References

`scripts/estimate.py` (no dependencies), `examples/scope.json` (a fictional scope that runs as is). Related: `crm-enrichment-cost-estimate`, `free-first-domain-resolver`, `win-loss-rewind`.
