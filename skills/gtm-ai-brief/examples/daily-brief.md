# AI Brief: Daily GTM Brief

<!--
Reference build 1 of 2. Adapted at concept level from a Winning by Design
webinar on AI in GTM (July 2026); wording original, company generic.

This is the highest-value starter build and the one most likely to survive as a
habit: what changed, and what needs attention, before the day starts.
Adapting it to your stack usually takes one edit: substitute your actual
systems (your CRM, your call recorder, your chat tool) into the Inputs section.
-->

**Owner:** [account executive / team lead running this brief]
**Version / date:** v1.0, [date]
**Good example attached:** [path to one hand-written morning summary the owner was proud of]
**Synthetic test set:** [path to fake CRM extract + fake call notes used for validation]

---

## Trigger

Every weekday at 07:00, before the working day starts.

Today: run manually first thing in the morning. Intended end state: scheduled, so the brief is waiting when the day begins.

## Inputs

In priority order:

1. **CRM: open opportunities and accounts owned by me or my team**, restricted to records modified in the last 24 hours. *This is the source of truth for deal state. When any other input disagrees with the CRM about the state of a deal, the CRM wins, and the disagreement itself is worth flagging.*
2. **Call recordings or call notes from yesterday**, for calls involving me or my team.
3. **Calendar: today's meetings**, mine and my direct team's.
4. **Email and chat threads from the last 24 hours** involving my accounts.
5. **Target account trigger events**: news, leadership changes, funding, product launches at named target accounts (list maintained separately and referenced here).
6. **Industry headlines** from [named publications or feeds], last 24 hours only.
7. **The attached good example**: match its tone, structure and length.

The inputs above are the only source of truth. Do not supplement from general knowledge.

## Steps

In this order. The order matters.

1. Pull all inputs for the last 24 hours. Note any input that returned nothing, and say so in the brief rather than papering over it.
2. Identify what changed in the business overnight: deal stage changes, new inbound, replies received, anything that moved.
3. Summarize the important calls from yesterday: for each, one line on what happened and one line on the agreed next step.
4. Cross-reference today's calendar against the CRM: for each external meeting today, state the account, the deal state, and the last touch.
5. Scan target accounts for trigger events. Only include events from the last 24 hours; an old event presented as fresh is worse than no event.
6. Select at most three industry headlines that plausibly affect us or our accounts, one line each on why it matters to us. This is the reading everyone intends to do and defers; do it for them.
7. Distill a "focus for today": the two or three items from all of the above that most deserve attention, with a one-line reason each.
8. Assemble the output in the format below, then check it against the guardrails before finishing.

## Output

A single markdown brief, readable in under three minutes, with exactly these sections in this order:

1. **Focus for today**: 2 to 3 bullets, each with a one-line reason.
2. **What changed overnight**: max 5 bullets.
3. **Yesterday's calls**: one line per call, what happened plus next step.
4. **Today's meetings**: one line per external meeting, account plus deal state plus last touch.
5. **Trigger events at target accounts**: only if fresh (last 24 hours); otherwise write "none fresh".
6. **Worth reading**: max 3 headlines, one line each on relevance to us.

Hard length limit: one page. If content overflows, cut from the bottom sections, never from Focus.

## Guardrails

- Never invent information not present in the inputs. If a section has no data, write "nothing today" rather than filling it.
- The inputs listed above are the only source of truth. The CRM is authoritative for deal state.
- Every claim carries its source: which system or thread it came from.
- Trigger events must be dated, and only events from the last 24 hours count as fresh. Never present an undated or old event as a reason to act today.
- Do not editorialize about colleagues' performance in the calls section; report what happened and the next step.
- Flag conflicts between inputs explicitly (for example, an email thread implying a deal is dead while the CRM shows it open) instead of silently choosing one.
- If an input source was unreachable, say so at the top of the brief.

---

## Test log

| Date | Test set | Failure observed | Guardrail or step added |
|---|---|---|---|
| [date] | Synthetic CRM extract, 20 rows incl. 2 contradictions | Brief silently picked one side of a contradiction | Added the conflict-flagging guardrail |
| [date] | Same set plus fake call notes | Presented a 3-week-old funding event as a fresh trigger | Added the 24-hour freshness guardrail and dating requirement |

## Graduation status

- **Current rung:** 1 (prompt): run manually each morning with inputs gathered by hand.
- **Next rung requires:** save as a named skill so it is invoked, not retyped. Rung 3 requires connecting the CRM, calendar and call-notes inputs. Rung 5 requires scheduling the 07:00 trigger, which the team should only do once the guardrails have held across the test log above.
