# Data Confidence Report: {{client}}

**Phase 0 of win-loss-rewind. Operator must approve before Phase 1 runs.**

Date: {{date}}
Source export: {{source_file}}
Rows in: {{n_total}}

## Summary

| Metric | Value |
|--------|-------|
| Rows in | {{n_total}} |
| Rows quarantined | {{n_quarantined}} ({{pct_quarantined}}%) |
| Rows cleared for training | {{n_clear}} |
| Quarantine rate verdict | {{ok if <30% else "STOP: CRM hygiene problem"}} |

> Triage rule: if more than 30% of rows are quarantined, the CRM hygiene is the problem, not the ICP. Fix the export, then rerun Phase 0.

## Outcome distribution (cleared rows only)

| Outcome | Count | Holdout (20%) |
|---------|-------|---------------|
| won | | |
| healthy | | |
| expanded | | |
| lost | | |
| churned | | |

Negative class present? {{yes/no}}  (a discriminator needs losses/churns)

## Quarantined rows

| Company | Domain | CRM label | Reality found | Reason quarantined |
|---------|--------|-----------|---------------|--------------------|
| | | | dead site / ghost LinkedIn / headcount off >5x / duplicate | |

## Cross-reference method

- Domain resolves + real page: HTML-to-text fetch first, paid scraper on the residual
- LinkedIn company page exists + active: any LinkedIn company data provider
- Headcount sanity: external vs CRM-claimed

## Operator decision

- [ ] Approve quarantine list as-is, proceed to Phase 1
- [ ] Override specific rows (list below)
- [ ] Stop, fix CRM export first

Notes:
