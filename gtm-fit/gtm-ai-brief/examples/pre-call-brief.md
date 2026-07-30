# AI Brief: Five-Minute Pre-Call Brief

<!--
Reference build 2 of 2. Adapted at concept level from a Winning by Design
webinar on AI in GTM (July 2026); wording original, company generic.

Just-in-time prep for a call you were pulled into on short notice. The whole
run should take two to three minutes, so the brief is ready before the call
starts. The final step, two or three context-rich impact questions, is what
separates a useful brief from a research dump: it converts the research into
the thing you actually say, without producing a scripted call.
-->

**Owner:** [seller / solutions person who takes short-notice calls]
**Version / date:** v1.0, [date]
**Good example attached:** [path to one hand-written prep doc that led to a good call]
**Synthetic test set:** [path to several short fake discovery transcripts + fake email threads]

---

## Trigger

Manual today: run the moment a short-notice call lands on the calendar, with the invite or the person's name and company as the starting input.

Intended end state: fires automatically 30 minutes before any external discovery call on the calendar.

## Inputs

In priority order:

1. **The inbound request itself**: the meeting invite, the form fill, or the message that caused this call. *This, plus our email history with this person, is the source of truth for what they asked for. If public information suggests a different agenda than the request states, the request wins and the difference is flagged.*
2. **Full email and message history** with this person and anyone else from their company.
3. **CRM record** for the company: prior deals, prior contacts, notes.
4. **Public information about the person**: role, tenure, background, recent posts.
5. **Public information about the company**: what they do, size, recent news, anything they have said publicly about what they are looking for or struggling with.
6. **Our own solution map**: the short internal document listing what we sell and the problems each part solves.
7. **The attached good example**: match its structure and brevity.

## Steps

In this order. The order matters: the impact questions in step 6 must be built from what steps 1 through 5 found, not generated generically.

1. Establish the ask: what was the inbound request, and what does the email history add or contradict? One short paragraph.
2. Profile the person: who are they, what is their role, how long in it, what do they appear to care about? Three bullets max.
3. Sketch the decision picture at the company: who else is likely involved in a decision like this, and where does this person sit in it? Label inference as inference.
4. Collect what they have said publicly about what they are looking for: their words, quoted or closely paraphrased, with the source.
5. Map our solutions to their stated need: for each relevant part of our offering, one line connecting it to something found in steps 1 through 4. No mapping without a found reason.
6. **Write two or three context-rich impact questions** to ask on the call. Each question must be built from a specific fact found above, and each must point at business impact (revenue, cost, risk, customer experience), not at feature curiosity. Good shape: "You mentioned [found fact]. What does that cost you today?" or "If [found situation] does not change this year, what happens to [thing they said they care about]?" A question that could be asked of any prospect fails this step.
7. Assemble the output and check it against the guardrails.

## Output

A single brief readable in under five minutes, with exactly these sections:

1. **The ask**: one paragraph, what they requested and the relevant history.
2. **Who they are**: 3 bullets.
3. **Decision picture**: 2 to 3 bullets, inference clearly labeled.
4. **In their own words**: 2 to 3 quoted or paraphrased statements with sources.
5. **Where we fit**: max 3 lines, each anchored to a found fact.
6. **Ask these**: 2 or 3 context-rich impact questions.

The brief ends with the questions. Nothing after them: the questions are what you carry into the room. This is prep, not a script; the questions open a conversation, they do not run it.

## Guardrails

- Never invent facts about the person or the company. Everything in sections 1 through 5 must trace to a named input; anything uncertain is labeled as inference.
- The inbound request and our email history are the source of truth for what this call is about. Public research colors the picture; it does not overwrite the ask.
- No solution mapping without a found reason. If the research surfaced no hook for a part of our offering, leave that part out rather than forcing it.
- Every impact question must reference a specific found fact. Generic discovery questions ("what are your priorities this year?") are banned from section 6.
- Respect the time budget: if research is incomplete when time runs out, ship the brief with gaps marked "unknown" rather than shipping late or filling gaps.
- If the person cannot be confidently identified (common name, multiple matches), say so at the top and brief on the company only. A confidently wrong person profile is the worst failure this brief can produce.

---

## Test log

<!--
Tested against synthetic data: several short fake discovery-call transcripts
(300 to 600 words each, different industries and temperaments, with planted
traps: a buried objection, a vague answer, one identity ambiguity) plus fake
email threads. Generating the fake transcripts takes seconds and lets the brief
be tuned before any real prospect data touches it.
-->

| Date | Test set | Failure observed | Guardrail or step added |
|---|---|---|---|
| [date] | 5 fake transcripts + threads | Impact questions were generic, could be asked of anyone | Added the found-fact requirement to step 6 and the guardrail banning generic questions |
| [date] | Same set, one planted identity ambiguity | Brief profiled the wrong same-named person with full confidence | Added the identity-confidence guardrail |

## Graduation status

- **Current rung:** 1 (prompt): run manually when a call lands, inputs pasted by hand.
- **Next rung requires:** save as a named skill invoked with just a name and company. Rung 3 requires connecting email, calendar and CRM inputs. Rung 5 requires wiring the trigger to the calendar so the brief fires 30 minutes before any discovery call, which should wait until the identity and invention guardrails have held across the test log.
