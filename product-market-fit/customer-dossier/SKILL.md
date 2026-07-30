---
name: customer-dossier
description: Build a ground-truth customer dossier per account from CRM exports, call transcripts, billing, product usage, and support data. One sorted timeline, provenance on every field, conflicts surfaced instead of hidden. The dossier describes, never reasons.
---

# Customer Dossier

Builds one dossier per account: a single sorted timeline fusing every system that knows something about the customer, with a source and a confidence state on every field. The dossier answers one question: what does every system say about this account, and where do they disagree?

The concept comes from Jordan Crawford (Blueprint): the dossier is the foundation artifact of AI GTM. Every downstream job (ICP analysis, churn analysis, expansion scoring, win-loss) runs on top of it. Build it wrong and every conclusion downstream is fiction anchored to plausible-looking data.

## The prime rule

**The dossier describes. It never reasons.**

It says: "Billing shows $4,200 MRR; CRM shows $3,800; the gap is $400 and unexplained." It does not say: "this customer is at risk." Scoring, prediction, and recommendation are downstream consumers of the dossier, not parts of it. Keeping description and reasoning separate means a change in your scoring logic never forces a rebuild of the dossiers.

## Inputs

Local file exports, any subset of:

1. **CRM export** (CSV): accounts, contacts, deals/opportunities with stages and dates
2. **Call transcripts** (txt/VTT/SRT/JSON): sales and CS calls
3. **Billing export** (CSV): subscriptions, MRR, invoices, payment events
4. **Product analytics export** (CSV): logins, feature events, usage
5. **Support export** (CSV): tickets with dates and status

Plus: the company's own email domain(s), needed for join hygiene (see rules below).

More systems means a better dossier, but the skill runs with as little as CRM + one other source. With only a CRM you do not have a dossier, you have a CRM report; the skill will say so and continue with a caveat.

## The trust hierarchy (governs every conflict)

When two systems disagree, prefer in this order:

1. **Customer actions**: product events, logins, payments. They voted with behavior.
2. **Customer voice**: call transcripts, tickets, emails. They said it themselves.
3. **CRM-derived state**: stages, account types, classifications. Entered by reps, one step removed from reality.

A rep marks a deal Customer when commission triggers; product data shows that customer never logged in; the product is right. Record the conflict, apply the hierarchy, keep both values in the audit trail.

## Process: the 6-wave build

Run the waves in order. Each wave produces an artifact. Stop and show the user the artifact after waves 1, 2, and 5.

### Wave 1: System discovery and preflight

Inventory every provided file: system, record count, primary key, date coverage, known issues. Pick ONE canonical join key (usually the CRM account ID; sometimes the billing ID; never "all of them"). Run a preflight data-quality check on the raw files BEFORE any joining: fake or test names (exclude names containing Fake, Test, Demo, Sandbox at this stage, not later), future dates, suspicious value distributions, bulk-import artifacts (many records sharing one created date), fill-rate gaps.

Output: source registry + preflight report. Show it and get confirmation.

### Wave 2: Identity linking (the load-bearing wave)

Link every record in every system to an account. Every link gets one of six verdicts:

- keep (authenticated source confirms)
- keep (email-domain verified)
- reject (authenticated source says no)
- reject (email conflict)
- email conflict, pending tiebreaker
- indeterminate

Three non-negotiable rules:

1. **Strip the company's own domain before any email-domain join.** Internal employees appearing as external participants create mass false matches.
2. **Never join on a single key.** Require at least 2 of: ID match, domain match, name fuzzy similarity of 0.92 or higher. Single-key joins produce collisions between unrelated companies.
3. **Show a random spot-check sample (up to 100 links) to the user.** Do not trust the aggregate. Tiebreaker decisions go into the dossier as audit trail.

Output: linking ledger with verdict counts. Show it and get confirmation.

### Wave 3: Revenue and key fields

Reconcile the fields that matter most, one at a time: MRR/ARR, plan tier, segment, churn reason, health indicators, owner. When two systems disagree on MRR by more than 10% on more than 5% of accounts, surface the conflict list; never average the values. Flag implausible outliers (an account paying far outside the normal band deserves a look before it enters the dossier).

Output: reconciled key-field set with a conflict log.

### Wave 4: Timeline assembly

Build the per-account sorted timeline. Drop every event whose linking verdict was reject or indeterminate. Every event carries provenance: source system, source field, linking verdict. For PROSPECT dossiers, split evidence into pre-engagement and post-engagement so that post-event facts can never leak into pre-event analysis downstream.

### Wave 5: Critique pass

Run three independent critiques over the assembled dossiers (as sub-agents if available, sequentially otherwise):

- **Statistician**: distributions, outliers, impossible values
- **Operations reviewer**: does the operational story cohere (stages vs dates vs revenue)
- **Outlier hunter**: individual paradoxes (a high-paying account with zero recorded calls in a year is either extraordinary or a linking failure)

Merge into one must-fix list. Show it; the user resolves or accepts each item.

### Wave 6: Render

Write one dossier file per account using `dossier-template.md`. Every field carries the 4-state uncertainty grammar:

- **verified**: confirmed by a rank-1 or rank-2 source
- **inferred**: derived, derivation shown
- **fuzzy**: conflicting or weak evidence, conflict shown
- **missing**: no evidence

When confidence in a field is low, render "unavailable" rather than a plausible guess. A gap is better than a lie.

## Two modes

- **Customer mode** (post-sale): tenure, MRR history, usage trajectory, support load, renewal events
- **Prospect mode** (pre-sale): deal shape, funnel position, fit evidence, with the pre/post-engagement split enforced

## Output

- `dossiers/<account-slug>.md` per account (see `dossier-template.md`)
- `dossier-build-log.md`: source registry, linking ledger summary, conflict log, critique resolutions

## Quality gates before shipping

- Zero events from rejected links present in any timeline
- Test/demo accounts excluded at the pull stage (grep the output to prove it)
- Every field in every dossier carries one of the four uncertainty states
- Spot-check sample was shown and confirmed
- Completeness check: every input file's record count reconciles to kept + rejected + indeterminate (a job that ran without errors is not the same as a job that processed everything)
