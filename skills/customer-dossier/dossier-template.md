# Dossier: {Account Name}

Built: {date} · Mode: {customer | prospect} · Join key: {canonical key} · Systems: {n} of 5

## Identity

| Field | Value | State | Source |
|---|---|---|---|
| Account name | | verified/inferred/fuzzy/missing | |
| Domain | | | |
| CRM ID | | | |
| Billing ID | | | |
| Segment | | | |
| Owner | | | |

## Revenue

| Field | Value | State | Source | Conflict |
|---|---|---|---|---|
| MRR | | | | e.g. "billing $4,200 vs CRM $3,800, unexplained" |
| Plan tier | | | | |
| Tenure | | | | prefer opportunity close date over created_at |
| Payment status | | | | |

## Timeline

Sorted, every event with provenance. Rejected-link events are absent by construction.

| Date | Event | System | Verdict |
|---|---|---|---|
| | | | |

## Voice of customer

Verbatim quotes only, with speaker and source recording/ticket. No paraphrases presented as quotes.

> "{quote}" ({speaker}, {source}, {date})

## Conflicts and open questions

Every disagreement between systems that the trust hierarchy resolved, plus everything unresolved.

- {conflict}: kept {value} per trust hierarchy rank {n}; alternative was {value} from {system}

## Unavailable

Fields where confidence was too low to state a value. A gap is better than a lie.

- {field}: {why}
