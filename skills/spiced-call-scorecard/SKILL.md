---
name: spiced-call-scorecard
description: Score sales call transcripts (plain text, VTT, or SRT) against the five SPICED dimensions with verbatim-evidence discipline, then generate the follow-up questions that close the gaps before the next call.
---

# SPICED Call Scorecard

Score one or more sales call transcripts on the five SPICED dimensions: Situation, Pain, Impact, Critical Event, Decision. SPICED is Winning by Design's diagnostic framework for recurring-revenue sales. This skill measures how well a call CAPTURED each dimension, not how well the rep "performed". A charming call that surfaces no Impact scores low. A clumsy call where the customer quantifies their pain scores high.

The output is a per-dimension score (0 to 3) backed by verbatim evidence, an overall capture score, the single biggest gap, and 3 to 5 concrete follow-up questions for the next call.

## Inputs

- One or more local transcript files. Accepted formats:
  - Plain text with speaker labels (any layout where a speaker name precedes their words)
  - WebVTT (`.vtt`)
  - SubRip (`.srt`)
- Users can export these from Fireflies, Gong, Zoom, Teams, or any call recorder. No integration is required: this skill reads local files only.
- Optional: which speaker(s) are on the selling side. If not provided, infer it from context (who asks discovery questions, who presents, whose company is being sold to) and state the inference in the report so the user can correct it.

If a transcript has no speaker labels at all, say so, score only what can still be attributed with certainty (usually nothing above level 1), and recommend re-exporting with speaker names.

## Extraction rules (non-negotiable)

These rules exist because a scorecard built on paraphrase is worse than no scorecard: it launders guesses into data.

1. **Verbatim quotes only.** Every score above 0 must cite at least one quote copied exactly from the transcript, including filler words. Never paraphrase, tidy, or compress a quote. If you cannot find the exact words, the evidence does not exist.
2. **Correct speaker attribution.** Every quote carries the speaker's name (as labeled in the transcript) and their side (customer or seller). Attribution must match the transcript. Include the timestamp when the format provides one.
3. **Customer words outrank seller words.** Levels 2 and 3 require evidence spoken by the customer. A seller stating the pain, the impact, or the deadline proves nothing about the customer. A seller statement that the customer explicitly confirms ("yes, exactly", "that's right") counts as level 1 evidence at most, quoted with both turns.
4. **No evidence means score 0.** Never infer a dimension from industry knowledge, from the company's website, or from what "must have been discussed". Absence of evidence is scored as absence.
5. **Closed enums only.** Scores are integers 0, 1, 2, or 3. No halves, no "2 leaning 3".
6. **Flag contradictions, never resolve them silently.** If the customer gives two conflicting statements (two different deadlines, two different decision makers), quote both, score the dimension on the weaker reading, and list the contradiction explicitly in the report.
7. **Null over guessing.** Any report field with no supporting transcript content is written as "not surfaced", never estimated.

## Scoring

Score each of the five dimensions 0 to 3 using `rubric.md` in this skill folder. The generic anchor shape is:

- **0** = not surfaced on the call
- **1** = mentioned but shallow (named, not explored)
- **2** = explored with specifics (customer describes it concretely in their own words)
- **3** = quantified or confirmed by the customer (numbers, dates, consequences, or an explicit customer confirmation of the full picture)

Read the per-dimension anchors in `rubric.md` before scoring: each dimension refines what "specifics" and "quantified" mean for that dimension. Score strictly. When evidence sits between two levels, assign the lower one.

### Overall capture score

```
Capture score = (S + P + I + CE + D) / 15 * 100, rounded to the nearest whole number
```

Interpretation bands:

| Band | Reading |
|---|---|
| 0 to 33 | Discovery did not happen. This was a pitch or a chat. |
| 34 to 59 | Partial capture. Enough to continue, not enough to forecast. |
| 60 to 79 | Solid discovery with named gaps. |
| 80 to 100 | Strong capture. Verify Critical Event and Decision are customer-confirmed, not rep-assumed. |

The five dimensions are equally weighted in the capture score, but NOT in the gap analysis below: a weak Impact or Critical Event is more expensive than a weak Situation, because deals without them slip regardless of how good the fit is.

### Biggest gap

The biggest gap is the lowest-scoring dimension. Break ties by this priority order (most expensive gap first): Impact, Critical Event, Decision, Pain, Situation. Impact and Critical Event lead the order because they are the dimensions most commonly missing from real calls and the ones that most directly predict slippage.

## Follow-up questions

For every dimension scoring 0 or 1 (and optionally 2), generate follow-up questions for the next call. Output 3 to 5 questions total, prioritized:

1. Impact and Critical Event gaps first, always.
2. Then Decision, Pain, Situation.

Rules for the questions themselves:

- Anchor each question in something the customer actually said, quoting or referencing their words. A follow-up that ignores the last call signals the rep was not listening.
- Impact questions should connect the stated pain to one of three business outcomes: revenue up, cost down, or customer experience improved. Ask what the problem is costing them, or what hitting the goal is worth.
- Critical Event questions must test the date, not just find one. The core move: "What happens if that date slips?" A date without consequences is a wish, not a critical event. Also separate the customer's deadline from the seller's quarter: only the customer's counts.
- Decision questions cover two distinct halves: process (who is involved, who signs, what steps including legal, security, procurement) and criteria (what they are evaluating against, and how the options rank). Ask about both if both are dark.
- Pain questions dig from symptom toward source: ask for a recent concrete instance, what triggered it, and what they have already tried.
- Situation questions fill specific factual holes (team size, current tools, volumes), never generic "tell me about your business".

Format each question with the gap it closes and the evidence hook it builds on. See `report-template.md`.

## Single-call mode

1. Read the transcript file(s) for the one call. Identify speakers and sides.
2. Extract candidate evidence per dimension: walk the transcript once, collecting verbatim quotes that bear on any of the five dimensions.
3. Score each dimension against `rubric.md`, applying the extraction rules above.
4. Compute the capture score and the biggest gap.
5. Generate prioritized follow-up questions.
6. Render the single-call report from `report-template.md`.

## Multi-call mode

When given multiple transcripts (multiple calls on one deal, or calls across a team):

1. Score every call independently using the single-call procedure. Never let one call's evidence bleed into another call's scores.
2. Build the score matrix: one row per call, one column per dimension, plus capture score.
3. **Trend (same deal, calls in time order):** show whether each dimension is climbing. Healthy discovery climbs: Situation and Pain early, Impact and Critical Event by mid-funnel, Decision before proposal. A dimension stuck at 0 or 1 across three or more calls is a stalled deal signal regardless of how warm the calls feel.
4. **Team pattern (calls across reps):** compute the average score per dimension across all calls. The systematically weakest dimension is an operating-model gap, not a rep gap: if every rep skips Impact, the fix is not coaching one rep, it is fixing the question set, the call structure, and the stage gates that let unquantified deals advance. Name the weakest dimension, show the per-rep spread on it, and say explicitly whether the pattern is systemic (most reps weak) or individual (one outlier).
5. Render the multi-call report from `report-template.md`.

## Output discipline

- Follow `report-template.md` structurally. Do not invent extra sections.
- Every quote in the report must survive a Ctrl-F check against the source transcript.
- Keep judgment out of the evidence blocks: quotes are quotes, interpretation lives in the score rationale.
- If the user asks for a score without providing transcripts, refuse: this skill scores evidence, not memory.
