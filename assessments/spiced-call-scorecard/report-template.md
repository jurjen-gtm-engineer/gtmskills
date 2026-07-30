# Report Templates

Two report structures: single call and multi-call. Follow them structurally. Every quote must be verbatim from the transcript with correct speaker attribution. Fields with no evidence read "not surfaced", never a guess.

---

## Single-Call Report

```markdown
# SPICED Call Scorecard: [call title or file name]

**Call date:** [date if known, else "not stated"]
**Participants:** [name (side: customer/seller), ...]
**Side inference:** [state how customer vs seller sides were determined, so the user can correct it]
**Transcript:** [file name, format, duration if known]

## Capture score: NN / 100

| Dimension | Score (0-3) | One-line status |
|---|---|---|
| Situation | n | [e.g. "stack and team size confirmed"] |
| Pain | n | ... |
| Impact | n | ... |
| Critical Event | n | ... |
| Decision | n | ... |

**Biggest gap:** [dimension]. [One sentence: why this gap is the most expensive one on this deal.]

## Evidence by dimension

### Situation: n/3
> "[verbatim quote]" (Speaker Name, customer, [timestamp if available])
> "[additional quote if load-bearing]" (Speaker Name, side, [timestamp])

Rationale: [1-3 sentences. Why this evidence lands at this level and what blocks the next level.]

### Pain: n/3
[same structure; if score is 0: "Not surfaced. No transcript evidence." and nothing else]

### Impact: n/3
[same structure]

### Critical Event: n/3
[same structure]

### Decision: n/3
[same structure]

## Contradictions and flags
- [Conflicting statements, both quoted with speakers; or "None found."]
- [Attribution uncertainties, unlabeled segments, inaudible markers that affected scoring]

## Follow-up questions for the next call
[3 to 5 questions, Impact and Critical Event gaps first.]

1. **[Dimension it closes]** [The question, phrased naturally.]
   Builds on: "[short verbatim hook from this call]" (Speaker)
   Target: moves [dimension] from n to n+1 by capturing [the specific missing element].
2. ...
```

Rules for this report:

- The evidence blocks contain only quotes and attribution. Interpretation lives in the rationale lines.
- If a dimension scored above 0, its section must contain at least one customer-side quote (levels 2 and 3) or a confirmed exchange (level 1).
- The follow-up section always leads with the Impact or Critical Event gap when either scored below 2.

---

## Multi-Call Report

```markdown
# SPICED Scorecard: [deal name or team name], [N] calls

**Mode:** [deal trend | team pattern]
**Calls analyzed:** [list: file name, date, rep, customer account]

## Score matrix

| Call | Date | Rep | S | P | I | CE | D | Capture |
|---|---|---|---|---|---|---|---|---|
| [name] | [date] | [rep] | n | n | n | n | n | NN |
| ... | | | | | | | | |
| **Average** | | | n.n | n.n | n.n | n.n | n.n | NN |

## Trend (deal mode: calls in time order)

[Per dimension, one line: climbing / flat / regressed, with the call where it moved.]

- Situation: [e.g. "2 on call 1, 3 by call 2. Done."]
- Pain: ...
- Impact: ...
- Critical Event: ...
- Decision: ...

**Stall flags:** [Any dimension at 0 or 1 for 3+ consecutive calls, named explicitly as a stalled-deal signal. Else "None."]

## Team pattern (team mode)

**Systemically weakest dimension:** [dimension], average n.n across [N] calls.

| Rep | Calls | Avg on weakest dimension | Avg capture |
|---|---|---|---|
| [rep] | n | n.n | NN |

**Systemic or individual:** [If most reps are weak on the same dimension: "Systemic. This is an operating-model gap, not a rep gap: fix the question set, the call structure, and the stage gates that let deals advance without this dimension captured." If one rep is the outlier: "Individual: coach [rep] on [dimension]; the rest of the team captures it at n.n average."]

## Best evidence found
[2-4 verbatim quotes from across the calls that show what good capture looked like when it happened, each with speaker, side, call, and the dimension it served. This gives the team a copyable internal example.]

## Biggest gap across all calls
[Dimension, why it is the expensive one, and the single change (question, call-structure step, or stage gate) most likely to close it.]

## Follow-up priorities
[Deal mode: 3 to 5 questions for the NEXT call on this deal, same format as the single-call report.]
[Team mode: the 2-3 questions every rep should add to their discovery structure, mapped to the weakest dimensions.]
```

Rules for this report:

- Each call is scored independently before the matrix is assembled. No cross-call evidence bleed.
- Averages are shown to one decimal; capture scores as whole numbers.
- Team mode must always answer the systemic-vs-individual question explicitly. That distinction decides whether the fix is coaching or operating-model change.
