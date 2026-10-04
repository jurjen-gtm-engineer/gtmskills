---
name: crm-enrichment-cost-estimate
description: Triggers when a user wants to estimate yearly Clay data credits and actions for enriching records they already have in a CRM, with phrasings like "how many Clay credits will CRM enrichment use", "scope credits and actions", "what does enriching 20,000 contacts cost per year", or "size the Clay plan for this use case". Owns the audience size, credits and actions per enrichment field, signals and exports, and the yearly totals per record. Follows the model of Clay's public Data Credit and Actions Scoping Template. Not for pricing a new market sourced from scratch (tam-data-cost-estimate) and not for auditing what a live workspace already spends.
metadata:
  version: "1.0"
---

# CRM Enrichment Cost Estimate

## Trigger

Apply this skill when someone plans to enrich existing CRM records with Clay and needs the yearly usage before they pick a plan or sign a scope.

## Scope

This skill estimates two meters for one use case: **data credits** (data bought in Clay's marketplace) and **actions** (platform usage: enrichment runs and exports). It does not pick the plan, and it does not cover provider subscriptions you bring on your own API key.

## Inputs

- Per object (accounts, contacts): CRM volume, the share that is relevant for the use case, and new records you expect to source.
- Per enrichment field: credits each, expected coverage, runs per year, whether it is a waterfall, and whether it runs on your own API key.
- Per signal: credits each, checks per year, and whether it watches accounts or contacts.
- Per export: how many times per year each record is synced, turned into content, or sent to a rep or a prospect.
- Optional: your price per credit and per action, to turn usage into money.

Take credits each from the enrichment's own page in Clay. Do not guess them.

## Roles

The user owns the scope and the credit prices. The agent runs the script and never invents a credit cost. An input that was assumed is labelled as assumed in the output.

## Procedure

1. Fill a scope file in the shape of `examples/scope.json`.
2. Run `python3 scripts/estimate.py --scope scope.json --out estimate.md`.
3. Read the line items from the top. The few lines that carry most of the credits are almost always an AI research field or a field with a high refresh rate. Challenge those first: fewer runs per year, a cheaper gate in front, or a smaller audience.
4. Run again and hand over the totals with the scope.

The model:

```
Audience        = CRM volume x share relevant + new records sourced
Field credits   = credits each x coverage x audience x runs per year   (0 on your own API key)
Field actions   = audience x runs per year x 3 if waterfall, else x 1
Signal credits  = credits each x checks per year x audience
Signal actions  = checks per year x audience
Export actions  = exports per year x audience
```

## Outputs

`estimate.md` with the audience, every line item, and yearly totals for credits and actions per block (account enrichment, contact enrichment, signals, exports), plus credits per record.

## Exceptions

What this model assumes, so say it when you quote the number:

- **Credits count per hit, actions per attempt.** Coverage lowers credits but not actions. Your own API key zeroes the credits but the actions still count. This reading comes from the template's formulas. Confirm it against your Clay plan before you commit to a number.
- **A waterfall counts as 3 actions and one provider's credits.** A real waterfall that falls through to a second or third paid provider costs more credits than shown.
- **Refresh rate is the multiplier that hurts.** A field that runs six times a year costs six times as much.
- **Your own keys move cost, they do not remove it.** The provider's subscription is a separate line.
- **Signals are counted once.** Some copies of Clay's sheet add signal actions to the account and contact rows and again to a signals row. This script keeps them in the signals block only, so its action total can be lower than the sheet's summary.

## QC

- The example scope reproduces Clay's own default example: 321,000 credits and 648,000 actions per year.
- Every credits each value has a source.
- The output names which inputs were assumed.

## References

`scripts/estimate.py` (no dependencies), `examples/scope.json` (the default CRM Enrichment example from Clay's template). Related: `tam-data-cost-estimate`, `claygent-prompt-generator`, `prompt-engineering-rules`.

## Credits

The model follows Clay's public Data Credit and Actions Scoping Template. Clay is a trademark of Clay Labs. This skill is an independent calculator and is not made or endorsed by Clay. For plans and current prices, go to [clay.com/pricing](https://www.clay.com/pricing).
