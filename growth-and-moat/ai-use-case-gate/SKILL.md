---
name: ai-use-case-gate
description: Run a proposed AI use case for a GTM team through a strict pre-build gate; constraint check first, then the chocolate teapot ship test, then capability-ladder placement, guardrails, and a one-page go/no-go verdict.
---

# AI Use Case Gate

A strict gate that a proposed AI use case (or a list of candidates) must pass BEFORE anything gets built. Most AI builds in go-to-market fail for a reason that has nothing to do with the model: they accelerate work that was never the bottleneck, they ship output that looks right and fails on contact with its job, or they jump three rungs of capability at once and collapse. This skill catches all three failure modes up front, when the fix costs a conversation instead of a rebuild.

The frameworks in this skill (the constraint framing, the chocolate teapot test, the prompt-to-routine capability ladder, and the context-over-model view of slop) are credited at concept level to Winning by Design, from their AI in GTM webinar, July 2026. Everything here is restated in original wording.

## When to use this skill

- Someone proposes an AI build for a GTM team: "we should have an agent that...", "can we automate...", "I want AI to write our..."
- A team has a backlog of candidate AI use cases and needs to rank or kill them.
- An AI build already exists but nobody can say what number it moves. Re-run it through the gate as if it were new.

## When NOT to use this skill

- The build decision is already made and funded, and the ask is implementation help. The gate is a pre-build instrument. Running it after commitment produces theater, not a decision.
- Pure personal-productivity experiments with no team dependency and no external output. Let people play; the gate is for things that will touch customers, systems, or the team's shared workflow.

## Core doctrine

1. **Aim before ambition.** AI pointed at a non-constraint produces impressive demos and an untouched revenue number. Speeding up a step that was never the bottleneck creates more work in progress, not more output. Constraint diagnosis is a precondition for any AI deployment, which is the theory of constraints applied to an AI rollout.
2. **The gate is a gate, not a critique.** It runs fast and its output is one of three things: ship, add context, or add a guardrail. It exists to protect three assets: positioning (question 1), the client relationship (question 2), and the company (question 3).
3. **Generic output is the alarm, not the verdict.** When output sounds like anything a competitor could get by typing the same prompt, that is a context failure, not a model failure. The model solved the problem it was given; a generic problem gets a generic answer. The fix is richer input, starting with real artifacts that show what good looks like.
4. **Start one rung lower than ambition suggests.** Teams that skip rungs of the capability ladder end up with one-off demos and no compounding. The rung you can operate reliably today beats the rung you can demo today.
5. **One job per agent.** A build that evaluates existing customers AND sources new prospects in the same run does neither well. Every build that passes the gate owns exactly one job, stated in one sentence.

## The gate, step by step

Run the steps in order. Each step can kill the use case. Do not skip ahead to the ladder or the guardrails for a use case that has not survived the constraint check.

### Step A: Constraint check (the first kill point)

Before evaluating the use case at all, establish what the revenue engine's current binding constraint is. Do not accept the proposer's assertion of the constraint; interview for it.

**Interview technique:** ask the user one question at a time, up to five questions. One at a time matters because each answer changes what the next question should be, and because people genuinely answer five sequential questions but skim a block of fifteen. Time-boxing at five keeps the gate fast enough that people actually run it.

Question territory to draw from (adapt to the answers as they come, never fire these as a block):

1. Where does revenue growth actually stall right now: not enough qualified conversations, conversations that do not convert, deals that stall late, customers that do not expand, or customers that leave?
2. If you doubled the volume at the top of the funnel tomorrow, would the number move, or would something downstream choke first?
3. Which step in the process does everyone quietly work around because it is messy, manual, or badly instrumented?
4. What was the last thing that measurably moved the revenue number, and what did it relieve?
5. If the proposed build worked perfectly, which specific metric changes, and who would notice within a month?

**The test:** does the proposed use case operate directly on the binding constraint you just identified?

- **Yes:** proceed to Step B.
- **No:** automatic no-go. Write the explanation into the verdict: name the actual constraint, name what the proposal accelerates instead, and state the mechanism of failure (the bottleneck still meters output, so hours saved at a non-constraint never become revenue downstream). Offer the redirect: what would a build aimed at the actual constraint look like?

Be alert to the standard trap: it is easier to automate what you understand, and the constraint is usually the messy, human, poorly instrumented step. Proposals cluster at the easy non-constraints (faster emails, prettier decks, more content) precisely because impressive output is easy to produce there.

**Note for the constraint that moves:** if the use case passes, record in the verdict that constraints relocate once relieved. A build aimed at today's constraint needs a review date, because a permanent build against a temporary constraint becomes tomorrow's ornament.

### Step B: The chocolate teapot test (the ship gate)

A chocolate teapot looks beautiful, is made of something delicious, and has the exact shape of a useful object. Pour hot water into it and you have a puddle. That is what an AI build becomes when it is attractive, fast, correctly shaped, and fails at the precise moment it meets its real job. Three questions, asked in order:

**1. What is our moat?**
If everything this build produces could be produced by a competitor typing a comparable prompt into the same model, there is no moat in it. What does this build know, reach, or encode that is genuinely ours: our win history, our voice, our customer data, our process opinions? If the honest answer is "nothing yet", the build is not dead, but it must be fed proprietary context before it earns a go.
The fast diagnostic: **if sample output sounds generic, that is the slop signal.** The fix is more context (real artifacts, not descriptions of artifacts), not a better model.

**2. Is it ready to pass over?**
Honest self-assessment of the output against its actual audience. Directionally-right is fine for a colleague reviewing a draft at midnight; it is not fine for a client, a prospect, or an exec. Define who receives this output and what standard "ready" means for that receiver. If it is not ready, do not iterate blindly: write down the specific failure as a guardrail, and encode that guardrail into the build's instructions so the next run starts past the failure instead of repeating it.

**3. What are the guardrails?**
Who gets access, what the build can reach, and which tool class fits this job. The structural choice that matters most: a corpus-bounded tool cannot hallucinate beyond what you gave it, while a web-connected assistant buys research reach and pays for it in invention risk. Neither is correct in general; choosing the right one per job IS the guardrail. A guardrail that lives in someone's head is not a guardrail: it must be written into the build itself.

Any question without a defensible answer stops the gate. The output of a failed teapot test is never "cancel forever"; it is one of "add context" (question 1 or 2 failed) or "add guardrail" (question 3 failed), followed by a re-run.

### Step C: Place it on the capability ladder

If the use case survives A and B, decide what KIND of thing gets built. Five rungs, each a behavior change with its own unlock:

| Rung | What it is | The unlock |
|---|---|---|
| 1. Prompt | Chat interaction, one task at a time, iterated by hand | Speed on a single task |
| 2. Skill | A recurring prompt promoted into a named, reusable unit, invoked by name or fired on intent | Consistency; nobody hunts through a prompt library |
| 3. Agent | The build invokes tools and touches real systems (CRM, call recordings, calendar) instead of the clipboard | Reach into your systems |
| 4. Workflow | A packaged chain where the output of one step is the input of the next | Compounding; this is where real productivity gain appears and where most teams never arrive |
| 5. Scheduled routine | The workflow fires on a schedule or a trigger with no human prompting it | Leverage; work happens without anyone asking |

Rules for placement:

- **Start one rung lower than ambition suggests.** If the proposal says "autonomous agent", gate it in as a skill first. If it says "runs every morning", gate it in as an on-demand workflow first. A rung is earned by reliable operation at the rung below, not granted by the pitch.
- **Rung 5 requires trust in the guardrails.** Nothing runs unattended until its guardrails have held through supervised runs at rung 4.
- **Teach the rung, not the vendor word.** Different platforms name these rungs differently and the naming shifts constantly. The verdict names the rung in this ladder's terms; translate to whatever the team's stack calls it as a footnote, never as the primary label.
- Record both the entry rung (where the build starts) and the target rung (where it may graduate to, and what evidence graduates it).

### Step D: Guardrails and the source of truth

Make the guardrails from Step B concrete and name the ground the build stands on:

1. **Source of truth, named explicitly.** Which documents, datasets, or systems is this build allowed to treat as true? State it in the build's own instructions in the form: the inputs provided are the only source of truth. A build without a named source of truth will invent, and it will invent confidently.
2. **Citation requirement.** Output claims travel with their source. Uncited claims are treated as unverified by default.
3. **Access boundary.** Who can run it, and what systems it can read versus write. Write access is a separate, later grant from read access.
4. **Corpus-bounded or web-connected.** Decide per job and record why. Research jobs may earn web reach; anything client-facing that must not invent gets bounded to the named corpus.
5. **Escalation line.** The specific conditions under which the build stops and hands to a human, written as concrete triggers, not vibes.

### Step E: The one-page verdict

Produce a single page. No appendices, no hedging. Sections, in order:

1. **Verdict: GO or NO-GO.** One sentence of justification. For a no-go, name the constraint mismatch or the failed teapot question, and what would have to change for a re-run.
2. **The constraint it operates on.** Named, with the metric that will show movement and the review date for re-checking that the constraint has not relocated.
3. **The single job.** One sentence: this build does X for Y. If the sentence needs an "and", split the proposal into two candidates and gate them separately. One job per agent.
4. **The rung.** Entry rung, target rung, and the graduation evidence required.
5. **The guardrails.** The full Step D list, concrete enough to paste into the build's instructions.
6. **What good looks like.** Reference examples SUPPLIED BY THE USER: a winning email, a real deliverable they were proud of, a transcript of the motion done well. Descriptions of quality do not count; only artifacts count. If the user cannot produce a single example of good, record that as a risk: nobody can steer a build toward a standard nobody can show. Taste cannot be outsourced to the model.
7. **The anti-pattern checklist.** Explicit pass/fail on the three checks below.

## The three anti-pattern checks (mandatory in every verdict)

**1. Single-threaded builder risk.**
Who besides the builder can run, modify, and debug this? If the answer is nobody, the builder is the runtime, and the build is stuck the day they are sick, promoted, or gone. The work can be real and the output good, and it still does not compound if it lives on one person's machine. A go verdict requires a named second operator and a stated home for the build that the team can reach.

**2. Shadow AI as a demand signal.**
Is anyone on the team already doing this job with unapproved tools? Unsanctioned usage is not primarily a compliance problem; it is evidence of unmet demand, and it means ungoverned output is already flowing. If shadow usage exists, the gate treats it as a point in favor of building (demand is proven) and as urgency for the guardrails (the ungoverned version is live today). Ask directly; people will tell you if the question is not framed as an audit.

**3. Generic output as the slop alarm.**
Before the verdict is final, look at real sample output from the closest existing approximation (even a rung-1 prompt version). If it reads like something any competitor could generate, the alarm fires: the build is context-starved. This is a people failure, not a model failure. The remedy is always the same pair: show it what good looks like (artifacts from section 6 of the verdict), and bind it to the named source of truth. A build that ships while the alarm is ringing is a chocolate teapot with a schedule.

## Handling a list of candidates

When gating multiple candidates at once:

1. Run the constraint interview ONCE (Step A applies to the revenue engine, not to each candidate).
2. Sort candidates into "operates on the constraint" and "does not". The second group gets a batch no-go with the shared explanation; do not spend teapot time on them.
3. Run Steps B through E on the survivors, one verdict page each.
4. Rank surviving GO verdicts by (a) directness of action on the constraint and (b) lowest entry rung, cheapest first. The best first build is the lowest rung that touches the constraint, because it ships fastest and teaches the most about whether the constraint diagnosis was right.
5. Recommend at most one build to start now. Parallel first-builds split the second-operator pool and multiply single-threaded risk.

## Failure patterns this gate exists to prevent

A short field catalog, kept here so the gate's questions stay motivated:

- **The acceleration mirage.** Team output metrics improve (more emails, more decks, more variants), revenue does not, because the accelerated step was never the bottleneck. Caught by Step A.
- **The end-to-end overreach arc.** A fully autonomous outbound build works briefly on novelty, then burns the market: reputation damage, prospect fatigue, and a net position worse than before the build. Root causes are scope too broad and missing human checkpoints between probabilistic steps. Caught by Step C (start lower) and Step D (escalation line).
- **Confidence stacking.** Chained AI steps without deterministic checks between them: each step's slight variance feeds the next as fact, and errors compound with rising confidence. Caught by Step C (workflow rung requires named checkpoints) and Step D (citation requirement).
- **Building on sand.** AI layered onto bad underlying data guarantees confident wrong output; the model does not know your CRM is dirty. Caught by Step D (source of truth must be named, and naming it forces the question of whether it deserves the title).
- **The hero build.** One brilliant operator vibe-builds something genuinely useful that dies with their laptop. Caught by anti-pattern check 1.

## Worksheet

For a fill-in version of the full gate (constraint, three teapot questions, rung, guardrails, one job), use `gate-worksheet.md` in this skill's folder. The worksheet is the artifact to complete WITH the user in a working session; this SKILL.md is the doctrine for running it well.
