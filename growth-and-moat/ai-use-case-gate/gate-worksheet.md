# AI Use Case Gate: Worksheet

Fill this in per use case, in order. Any section can kill the candidate; if it does, stop there and write the verdict. Frameworks credited at concept level to Winning by Design (AI in GTM webinar, July 2026), restated in original wording.

**Use case name:** ____________________
**Proposed by:** ____________________
**Date:** ____________________
**One-sentence description of what it would do:** ____________________

---

## Section A: Constraint check

Run the interview first (one question at a time, up to five questions). Record what you learned:

**Q1 asked:** ____________________
**Answer:** ____________________

**Q2 asked:** ____________________
**Answer:** ____________________

**Q3 asked:** ____________________
**Answer:** ____________________

**Q4 asked (if needed):** ____________________
**Answer:** ____________________

**Q5 asked (if needed):** ____________________
**Answer:** ____________________

**The binding constraint of the revenue engine right now is:**
____________________

**Metric that proves the constraint (the number that is stuck):**
____________________

**Does this use case operate DIRECTLY on that constraint?**
- [ ] YES: continue to Section B
- [ ] NO: automatic no-go. Skip to the verdict and write the explanation: what the proposal accelerates instead, and why hours saved at a non-constraint never reach the revenue number.

**Constraint review date** (constraints relocate once relieved): ____________

---

## Section B: The chocolate teapot test

Beautiful, delicious, correctly shaped, and useless the moment hot water goes in. Three questions; every one needs a defensible written answer.

**1. What is our moat?**
What does this build know, reach, or encode that a competitor typing a comparable prompt could not reproduce?
____________________
____________________
- [ ] Sample output sounds specific to us
- [ ] Sample output sounds generic --> SLOP ALARM: the fix is more context (real artifacts), not a better model. Do not proceed until fed.

**2. Is it ready to pass over?**
Who receives the output? ____________________
What does "ready" mean for that receiver? ____________________
Is current output at that standard?
- [ ] Yes
- [ ] No --> write the specific failure below as a guardrail and encode it into the build's instructions before re-testing:
____________________

**3. What are the guardrails?**
Who gets access: ____________________
What the build can reach: ____________________
Tool class for this job:
- [ ] Corpus-bounded (cannot invent beyond what we gave it; right for client-facing output)
- [ ] Web-connected (research reach, invention risk; right for research jobs)
Why this class: ____________________

**Teapot result:**
- [ ] Pass: continue
- [ ] Fail on Q1 or Q2 --> remedy is ADD CONTEXT, then re-run
- [ ] Fail on Q3 --> remedy is ADD GUARDRAIL, then re-run

---

## Section C: Rung on the capability ladder

Circle the AMBITION rung, then commit to starting ONE RUNG LOWER.

| Rung | | Ambition? | Entry? |
|---|---|---|---|
| 1 | Prompt (chat, one task, by hand) | [ ] | [ ] |
| 2 | Skill (named, reusable, invoked or intent-fired) | [ ] | [ ] |
| 3 | Agent (invokes tools, touches real systems) | [ ] | [ ] |
| 4 | Workflow (output of one step feeds the next) | [ ] | [ ] |
| 5 | Scheduled routine (fires on trigger or schedule, unprompted) | [ ] | [ ] |

**Entry rung:** ______
**Target rung:** ______
**Graduation evidence required to move up one rung:**
____________________

Reminder: rung 5 is forbidden until guardrails have held through supervised rung-4 runs. Name the rung in ladder terms; vendor words for these rungs shift constantly.

---

## Section D: Guardrails and source of truth

**Source of truth (the ONLY inputs the build may treat as true):**
1. ____________________
2. ____________________
3. ____________________

Paste into the build's instructions: "The inputs listed here are the only source of truth."

**Citation rule:** every claim in output carries its source. Uncited = unverified.
- [ ] Encoded in the build's instructions

**Access boundary:**
Read access: ____________________
Write access (separate, later grant): ____________________

**Escalation line (concrete triggers that stop the build and hand to a human):**
1. ____________________
2. ____________________

---

## Section E: The single job

**This build does ______________________ for ______________________.**

If that sentence needed an "and", STOP: split into two candidates and gate each separately. One job per agent.

---

## Section F: Anti-pattern checks (all three mandatory)

**1. Single-threaded builder risk**
Second named operator (can run, modify, debug): ____________________
Where the build lives so the team can reach it: ____________________
- [ ] PASS (both filled in)
- [ ] FAIL (builder is the runtime; no go until fixed)

**2. Shadow AI check**
Is anyone already doing this job with unapproved tools? ____________________
If yes: demand is proven (point in favor) and ungoverned output is live today (urgency for Section D).
- [ ] Checked, answer recorded

**3. Slop alarm**
Reviewed real sample output from the closest existing approximation?
- [ ] Output is distinct: pass
- [ ] Output reads generic: ALARM. Feed artifacts of what good looks like plus the named source of truth, then re-check. Never ship while the alarm rings.

---

## Verdict (one page, no appendices)

**GO / NO-GO:** ______
**One-sentence justification:** ____________________
**Constraint it operates on + metric + review date:** ____________________
**The single job (one sentence):** ____________________
**Entry rung / target rung / graduation evidence:** ____________________
**Guardrails (from Section D, paste-ready):** ____________________
**What good looks like** (user-supplied artifacts, not descriptions; list them):
1. ____________________
2. ____________________
If no artifact of good exists, record as a risk: taste cannot be outsourced, someone must show the standard before the model can hold it.

**Anti-pattern checks:** 1 [ ] pass 2 [ ] checked 3 [ ] pass

**If NO-GO, what would have to change for a re-run:**
____________________
