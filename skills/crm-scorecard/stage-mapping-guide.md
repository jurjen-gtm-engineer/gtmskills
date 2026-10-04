# Stage Mapping Guide

How to map a customer's CRM pipeline stages onto the bowtie buckets used by the `crm-scorecard` skill. This is the step where scorecards go wrong, so treat every mapping as a proposal to be confirmed by the user, never as a settled fact.

## The five buckets

Every distinct stage value in the deals export maps to exactly one bucket:

| Bucket | Meaning | Feeds |
|--------|---------|-------|
| `pre-qualification` | Deal exists but sales has not accepted it as a real, qualified opportunity | CR3 denominator |
| `qualified` | At or past the qualification boundary: sales-accepted, actively worked | CR3 numerator, CR4 denominator |
| `won` | Contract signed, Closed Won | CR4 numerator, right-side inputs |
| `lost` | Closed Lost, dead, disqualified after entering the pipeline | Loss analysis |
| `excluded` | Not part of the new-business funnel: nurture, on hold, renewal pipelines, junk, test rows | Nothing (but report the excluded volume) |

The single most important call is the **qualification boundary**: the first stage that counts as `qualified`. CR3 and CR4 both hinge on it. Rule of thumb: the boundary is the first stage that implies a human on the sales side accepted the deal after a real conversation (discovery held, demo completed, qualification confirmed). A booked meeting is not acceptance; a held discovery usually is.

## Common stage vocabularies by CRM

These are the default or most frequently seen stage names. Custom pipelines override all of this: the names below are priors, not answers.

### HubSpot (default sales pipeline)

| Stage | Typical bucket |
|-------|---------------|
| Appointment Scheduled (`appointmentscheduled`) | pre-qualification |
| Qualified To Buy (`qualifiedtobuy`) | qualified (this is usually the boundary) |
| Presentation Scheduled | qualified |
| Decision Maker Bought-In | qualified |
| Contract Sent | qualified |
| Closed Won (`closedwon`) | won |
| Closed Lost (`closedlost`) | lost |

HubSpot lifecycle stages on contacts (Subscriber, Lead, MQL, SQL, Opportunity, Customer) are the CR1/CR2 source, separate from deal stages. Exports may contain multiple pipelines in one file: split on the `Pipeline` column before mapping.

### Salesforce (default opportunity stages)

| Stage | Typical bucket |
|-------|---------------|
| Prospecting | pre-qualification |
| Qualification | pre-qualification (the deal is being qualified, not yet qualified) |
| Needs Analysis | qualified (common boundary; confirm) |
| Value Proposition | qualified |
| Id. Decision Makers | qualified |
| Perception Analysis | qualified |
| Proposal/Price Quote | qualified |
| Negotiation/Review | qualified |
| Closed Won | won |
| Closed Lost | lost |

Salesforce Lead objects (with Lead Status and conversion dates) are the CR1/CR2 source. A converted Lead becomes Contact plus Opportunity; if the export only holds Opportunities, CR1 and CR2 are N/A. Watch for `IsClosed` and `IsWon` boolean columns, which are more reliable than stage strings.

### Pipedrive

| Stage | Typical bucket |
|-------|---------------|
| Qualified | ambiguous: often the FIRST stage, meaning "lead entered", not "sales accepted". Check volume: if nearly 100% of deals pass through it, it is pre-qualification |
| Contact Made | pre-qualification |
| Demo Scheduled | pre-qualification (scheduled is not held) |
| Demo Done / Meeting Held | qualified (common boundary) |
| Proposal Made | qualified |
| Negotiations Started | qualified |
| Won (`status = won`) | won |
| Lost (`status = lost`) | lost |

Pipedrive exports carry both a `Stage` and a `Status` (open/won/lost) column: use `Status` for won/lost, `Stage` for the boundary. Won and lost deals keep their last open stage in the `Stage` column, which is useful for stage-of-death analysis.

### Attio

Attio pipelines are fully custom (statuses on a list or deal object), so there are no reliable default names. Common patterns follow the bowtie or a generic ladder (Lead, Qualified, In Progress, Proposal, Won, Lost). Map by the rules in the next section and lean harder on user confirmation. Attio exports often include status-changed-at timestamps, which enable cohort-based computation: look for them.

### Generic / other CRMs

Frequently seen names and their usual buckets: New, Open, Untouched, Working, Contacted (pre-qualification); Discovery, Scoping, Evaluation, Solution Fit, POC, Pilot, Proposal, Quote, Verbal, Contract, Legal, Procurement (qualified); Signed, Live, Booked (won); Dead, Churned pre-sale, No Decision, Disqualified (lost).

## Rules for ambiguous cases

1. **"Qualified" as a first stage is a trap.** Many pipelines name their entry stage "Qualified" or "Qualified Lead" while it actually means "created". Check the stage's share of volume: an entry stage holds close to 100% of deals ever created. Real qualification boundaries pass noticeably less.
2. **Scheduled is not held.** "Demo Scheduled", "Meeting Booked", "Appointment Scheduled" are pre-qualification. The held version ("Demo Done", "Discovery Held") is where acceptance can start.
3. **Proposal and negotiation stages are always `qualified`.** No pipeline sends proposals to unqualified deals on purpose.
4. **Nurture, On Hold, Parked, Recycled are `excluded`,** not lost: they are outside the funnel clock. Report their volume separately; a large parked bucket is itself a hygiene finding.
5. **Renewal and expansion pipelines are `excluded` from the left side.** They feed CR7/CR8 inputs instead. If one pipeline mixes new business and renewals, use the deal type column; if there is none, flag that CR4 is inflated by renewals and recommend the field.
6. **Deals can be lost from any stage.** Do not require lost deals to have passed the boundary; instead use their last open stage for stage-of-death analysis (early death = qualification filter working, late death = pricing, competition, or indecision).
7. **Skipped stages are normal.** A deal can jump from entry to proposal. Bucket by the furthest stage reached (from stage history if present, otherwise current/last stage), never by assuming every deal walks every step.
8. **Stages holding under 2% of volume** are usually vestigial. Map them anyway, but call them out: the team's real process likely differs from the configured pipeline.
9. **Multiple pipelines never share one mapping by default.** Map each pipeline separately, then ask which are in scope. Partner, renewal, and test pipelines routinely hide in exports.
10. **When two stages could both be the boundary, pick the earlier one and say so.** An earlier boundary makes CR3 stricter and CR4 more generous; disclose the choice so the user can flip it. Whatever is chosen, apply it consistently to both CR3 and CR4.
11. **Ordering comes from meaning, not from the export.** CSV column order and alphabetical sorting say nothing about funnel order. Confirm the true sequence with the user, ideally against the CRM's configured stage order or the stage-history timestamps.
12. **Won without a close date, or open deals in a won/lost stage, are data defects,** not mapping problems. Send them back to the preflight report rather than bending the mapping around them.

## Output format for the mapping proposal

Present the proposal exactly like this before computing anything:

```
| Stage (as exported) | Rows | % | Proposed bucket | Reasoning |
|---------------------|------|---|-----------------|-----------|
| ...                 | ...  |...| ...             | ...       |

Qualification boundary: <stage name>
Pipelines in scope: <list>  |  Excluded: <list, with row counts>
```

Then ask: "Does this mapping match how your team actually uses these stages, and is the qualification boundary right?" Apply corrections and show the final table once more before Phase 3.
