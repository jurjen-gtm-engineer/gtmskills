# AI Brief: [task name]

<!--
The five-part scaffold below is adapted at concept level from a Winning by Design
webinar on AI in GTM (July 2026). Fill every section. A brief with an empty
section is not done; a brief without a good example and a named source of truth
does not ship at all.
-->

**Owner:** [who is accountable for this brief and its edits]
**Version / date:** [bump on every guardrail change]
**Good example attached:** [link or path to a real past output the owner rates as good]
**Synthetic test set:** [link or path to the test inputs this brief was validated against]

---

## Trigger

[What makes this run?]

<!--
Guidance:
- Three options: manual, on a schedule, or on an event. Pick one and be exact:
  "every weekday at 07:00", "30 minutes before any discovery call on the calendar",
  "when a reply arrives in the shared inbox".
- Write the INTENDED trigger even if the brief is run manually today. The gap
  between intended and current is the graduation path.
- A brief with no trigger is a prompt someone has to remember, which means it
  will be forgotten.
-->

## Inputs

[Where does the context come from? List each input specifically, in priority order.]

<!--
Guidance:
- Name inputs concretely: not "the CRM" but "open opportunities modified in the
  last 7 days, exported from the CRM".
- Mark exactly ONE source of truth: the input that wins when inputs conflict,
  and the boundary the model may not reach past. This is mandatory.
- Reference the good example as an input: "match the tone, structure and length
  of the attached example."
- If an input is gathered by interviewing the operator, say so: "ask me one
  question at a time, up to five questions" is a legitimate input line.
- Swapping a system name here (your call recorder, your CRM) is normally the
  only edit needed to adapt someone else's brief.
-->

## Steps

[Numbered. The order matters; say so.]

<!--
Guidance:
- State the order explicitly. Do not leave sequencing up to chance: unordered
  instructions are the most common defect in AI builds and produce output that
  varies run to run.
- Include the reasoning steps, not only the retrieval steps: gather, THEN rank
  by X, THEN draft, THEN check against the guardrails.
- If a step depends on a previous step's output, name that dependency.
- Keep it to one job. If the steps describe two different deliverables, this
  should be two briefs.
-->

1. [ ]
2. [ ]
3. [ ]

## Output

[The exact artifact: format, skeleton, length.]

<!--
Guidance:
- Name the format precisely: a one-page markdown brief, a five-row table, a
  three-paragraph email, a single chat message. One word here changes the whole
  run, which makes this the cheapest quality lever in the scaffold.
- Give the skeleton: section headers, bullets per section, ordering.
- If the output must END in something specific (a recommendation, two or three
  questions, a yes/no with reasons), state it; the ending is what gets used.
- State length limits. Unbounded outputs bloat until nobody reads them.
-->

## Guardrails

[What must this never do? Prohibitions and obligations.]

<!--
Guidance:
- The two non-negotiables, always present:
  1. "Never invent information not present in the inputs. If something is
     missing, say 'unknown' instead of filling the gap."
  2. "The inputs listed above are the only source of truth." Restate the named
     source of truth here even though it appears under Inputs; this section is
     read in isolation more often than any other.
- Require citations: every claim travels with the input it came from.
- Add one guardrail per failure the synthetic test revealed. Guardrails written
  from imagined failures are decoration; guardrails written from observed
  failures are the reason this brief can eventually run unattended.
- Missing guardrails is the most EXPENSIVE defect in the scaffold: it produces
  confident invention.
-->

---

## Test log

<!--
Keep the trail. The evidence this brief works is the process, not the artifact:
what was tested, what failed, which guardrail each failure produced. A brief
without a test log should be treated as untested.
-->

| Date | Test set | Failure observed | Guardrail or step added |
|---|---|---|---|
| | | | |

## Graduation status

<!--
Where this brief sits on the capability ladder (prompt, skill, agent, workflow,
routine) and the single next action that moves it one rung up.
-->

- **Current rung:** [1 prompt / 2 skill / 3 agent / 4 workflow / 5 routine]
- **Next rung requires:** [e.g. "save as a named skill", "connect the CRM input", "schedule the trigger"]
