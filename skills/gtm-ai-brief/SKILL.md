---
name: gtm-ai-brief
description: Turn a GTM task someone keeps doing manually (or keeps prompting ad hoc) into a written, testable AI brief using the Trigger / Inputs / Steps / Output / Guardrails scaffold, tested against synthetic data before it ships.
---

# GTM AI Brief

Most GTM automation fails the same way: someone types a clever prompt, gets a decent result once, and never writes anything down. The next run drifts. The teammate who copies the prompt gets something worse. Nothing compounds.

This skill fixes that by producing a **brief**: a short written specification of one GTM task, structured as Trigger / Inputs / Steps / Output / Guardrails, tested against synthetic data before anyone relies on it. The brief is the artifact that graduates a one-off prompt into a repeatable unit of work.

The five-part scaffold and the two reference builds in this skill are adapted, at concept level, from a Winning by Design webinar on AI in GTM (July 2026). The wording here is original.

## When to use this skill

- The user describes a GTM task they do repeatedly by hand (prep, recaps, list triage, account research, reporting).
- The user says some version of "I keep prompting this from scratch" or "the output is different every time."
- The user wants to hand a working prompt to a teammate and have it produce the same quality.
- The user wants to eventually schedule something (a daily brief, an automatic pre-call prep) and needs the specification first.

Do not use this skill to build the automation infrastructure itself (schedulers, integrations, pipelines). This skill produces the specification and proves it works. Wiring it up comes after, and the graduation path at the end tells the user what that takes.

## The scaffold

Every brief has exactly five parts. Most bad AI builds are missing two or three of them.

| Part | The question it answers |
|---|---|
| **Trigger** | What makes this run? Manual, on a schedule, or on an event. |
| **Inputs** | Where does the context come from? Files, systems, or an interview of the user. |
| **Steps** | In what order? Explicitly ordered. Unordered instructions are where quality goes to die. |
| **Output** | What artifact, exactly? Format named precisely. One word here changes the whole result. |
| **Guardrails** | What must it never do? Grounding rules, source of truth, citation requirements. |

The empty scaffold with per-section guidance lives in `brief-template.md`. Two complete worked examples live in `examples/`.

## Process

Run the six phases in order. Do not skip the gate in phase 2.

### Phase 1: Interview, one question at a time

Interview the user to extract the task. **One question at a time, up to five questions.** Never dump a wall of questions: each answer changes what the next question should be, and people answer five sequential questions but skim a block of fifteen.

Cover, in whatever order the conversation demands:

1. **The task.** What do you do, in your own words, start to finish? What does a single run look like?
2. **The trigger.** What tells you it is time to do this? A time of day, a calendar event, a request from someone, a signal in a system?
3. **The inputs.** What do you look at while doing it? Which systems, files, threads, notes? Which of those is authoritative when they disagree?
4. **The definition of good.** How do you know a run went well? What did the best version you ever produced have that the average version lacked?
5. **The failure modes.** What has gone wrong before? What would make you refuse to send the output to a colleague or customer?

Stop at five questions. If real ambiguity remains, write the brief anyway and let the test phase surface it. Something concrete to react to beats a longer interrogation.

### Phase 2: The two-element gate (hard requirement)

Slop is a context problem, not a model problem. A model given a generic problem returns a generic answer, and that is correct behavior, not a defect. So before writing anything, require two elements from the user:

1. **At least one example of what good looks like.** A real past output the user rates as good: an actual brief they wrote by hand, a prep doc that worked, an email that got the meeting. Not a description of good. An artifact. If they have nothing, have them produce one by hand right now, or pick the best of several past attempts. A description of quality is not a substitute for an instance of it.

2. **A named source of truth.** The explicit statement of which input wins when inputs conflict, and the boundary the model may not reach past. "The CRM is authoritative for deal state." "These three documents are the only source of truth; do not supplement from general knowledge."

**A brief without both elements does not ship.** Say so plainly. Writing the brief anyway produces a specification for generating slop faster, which is worse than no brief, because it looks finished.

### Phase 3: Write the brief

Fill the scaffold in `brief-template.md`. Rules of craft:

- **Trigger:** write the real trigger even if today the user will run it manually. "Intended: every weekday at 07:00. Today: run manually" is a fine trigger line. The gap between intended and current trigger is the graduation path (phase 6).
- **Inputs:** name each input specifically, in priority order, and mark the source of truth. "The CRM" is weak; "open opportunities modified in the last 7 days, from the CRM export" is a brief. Reference the good example directly: "match the tone and structure of the attached example."
- **Steps:** number them. State the order and say the order matters. Include the reasoning steps, not just the retrieval steps ("first gather, then rank by X, then draft").
- **Output:** name the exact artifact and its skeleton. "A one-page markdown brief with these four sections, each 3 bullets max" beats "a summary." If length matters, state it. If the output ends in something specific (questions, a recommendation, a table), say exactly what.
- **Guardrails:** write them as prohibitions and obligations. "Never invent a fact not present in the inputs." "Cite the input every claim came from." "If an input is missing, say so instead of filling the gap." Restate the source of truth here even though it appears under Inputs; guardrails are read in isolation more often than any other section.

### Phase 4: Generate synthetic test data and run the brief

Never ship an untested brief, and never test on live customer data first. Generate realistic synthetic inputs matched to the task:

- **Call-based briefs** (pre-call prep, call coaching, recap generation): generate several short fake discovery-call transcripts, 300 to 600 words each, with realistic messiness: interruptions, a vague answer, a buried objection, one participant who talks too much. Vary the scenario across transcripts (different industries, deal stages, temperaments).
- **Pipeline or account briefs:** generate a fake CRM extract with 10 to 30 rows, including the ugly cases: stale records, missing fields, two records that contradict each other.
- **Inbox or message briefs:** generate a fake thread history with mixed signal quality.

Synthetic data is not a compromise; it is faster than sanitizing production data and safer than not testing. It also lets you plant known traps (a contradiction, a missing field, a tempting fact that is NOT in the inputs) and check whether the guardrails catch them.

Then **run the brief against the synthetic data and show the user the outputs.** All of them, not a curated best one. The user reacting to real outputs is where the definition of good sharpens.

### Phase 5: Iterate the guardrails from what the test reveals

Read the test outputs adversarially, with the user, against three questions:

- **Did it invent anything?** Any claim not traceable to an input becomes a new guardrail ("never infer X; if X is not in the inputs, write 'unknown'").
- **Did it vary run to run in a way that matters?** Variance usually means a missing or ambiguous Step. Tighten the ordering or add the missing step.
- **Did it miss the point?** Output that is accurate but useless means the Output section is underspecified or the good example was not referenced hard enough.

Fold every finding back into the brief, then re-run against the same synthetic data until the output is stable and the user would send it. Two or three loops is normal. The iteration IS the skill being transferred here: the competence is steering from a mediocre first response to a good fourth one, and the brief is where that steering gets written down so nobody has to redo it.

Keep the synthetic test set with the brief. It is the regression test for every future edit.

### Phase 6: The graduation path

Close every engagement by placing the brief on the capability ladder and stating what graduation takes. The ladder (concept from the same Winning by Design material):

1. **Prompt.** Chat mode, run by hand, iterated by hand.
2. **Skill.** The prompt promoted into a named, reusable unit, invoked by name or fired on intent.
3. **Agent.** The unit invokes tools: the CRM, the call recorder, the calendar. It touches systems instead of the clipboard.
4. **Workflow.** The output of one step becomes the input of the next. This is where real productivity gains appear, and where most teams stop climbing.
5. **Routine.** The workflow runs on a schedule or a trigger with no human prompting it: a brief before you wake up, prep fired 30 minutes before any discovery call on the calendar.

A freshly written brief sits at **rung 1**: it is a tested prompt. Tell the user exactly that, then state what graduation requires:

- **To rung 2:** save the brief as a named unit in whatever system the team uses, so it is invoked, not retyped.
- **To rung 3:** replace the manually gathered inputs with connected sources. The Inputs section already names them; each named input becomes a connector to wire up.
- **To rung 5:** the Trigger section already states the intended schedule or event. Graduation means the team trusts the Guardrails enough to let it run unattended, which is precisely why the guardrails were tested against planted traps in phase 4 and not just written down.

Each rung is a behavior change, not a feature. Do not promise that buying a tool moves anyone up the ladder.

## The two reference builds

These are the canonical worked examples, kept compact here and written out in full in `examples/`. When a user's task resembles one of these, start from the example instead of a blank scaffold.

### Reference build 1: the daily brief

What changed, and what needs attention, before the day starts. The highest-value starter build and the one most likely to survive as a habit. Contents that earn the read: what happened overnight, important calls the team had yesterday, today's focus, trigger events at target accounts, and the industry reading everyone intends to do and defers. Its value scales with input coverage; substituting your actual systems into the Inputs line is normally the only edit required. Full version: `examples/daily-brief.md`.

### Reference build 2: the five-minute pre-call brief

Just-in-time prep for a call you were pulled into on short notice. Runs in a few minutes: what the inbound request was and the email history, who the person is, the decision-making picture at the company, what they have said publicly about what they want, where your solution maps to it, and then the step that separates a useful brief from a research dump: **two or three context-rich impact questions to ask on the call.** That final step converts research into the thing you actually say, without scripting the call. Full version: `examples/pre-call-brief.md`.

## Operating notes

- **Certify the process, not the artifact.** Anyone with a model can produce a plausible brief. What proves this skill ran correctly is the trail: the interview answers, the good example, the named source of truth, the synthetic test outputs, and the guardrail edits they caused. If a brief arrives without that trail, treat it as untested.
- **Missing Steps is the most common defect** and produces run-to-run variance. **Missing Guardrails is the most expensive defect** and produces confident invention. Check for these two first in any brief you are asked to review.
- **Output format is the cheapest quality lever.** Before rewriting Steps, try tightening the Output section.
- One brief, one job. A brief that preps calls and also scores the pipeline does neither well. Split it.
