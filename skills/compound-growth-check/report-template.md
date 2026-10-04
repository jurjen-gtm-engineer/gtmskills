# Compound Growth Check: {{company}}

**Verdict: {{headline}}**

{{company}} is **{{classification}}** ({{pct_positive_delta2}}% of second-derivative readings positive across {{n_delta2}} quarters). On the 10-state growth ladder this places the company at **state {{state_number}}: {{state}}** ({{phase}}, {{position_vs_wall}}), confidence **{{confidence}}**.

*Concept credit: the compound check and the 10-state growth ladder are Winning by Design concepts (Jacco van der Kooij's Growth Architecture framework), applied here at concept level.*

---

## The math

| Quarter | ARR | Delta (growth) | Delta2 (change in growth) |
|---|---|---|---|
| {{quarter_1}} | {{arr_1}} | n/a | n/a |
| {{quarter_2}} | {{arr_2}} | {{delta_2}} | n/a |
| {{quarter_3}} | {{arr_3}} | {{delta_3}} | {{delta2_3}} |
| ... | ... | ... | ... |

{{One sentence naming the quarters where delta2 flipped sign, if any, and the trailing-8-quarter read when available.}}

## What the trajectory says

{{The script's explanation, expanded: what the delta2 pattern means for this company specifically. Two to four sentences. For decompounding, name the reset quarters. For compounding, name how long the streak has held.}}

## What typically causes this pattern

{{The matching cause block from SKILL.md Step 3.4, tailored to what is known about this company. Three to five bullet points, most likely cause first.}}

- {{cause_1}}
- {{cause_2}}
- {{cause_3}}

## What to check next

{{The matching check block from SKILL.md Step 3.5, as concrete questions the operator can answer with their own data. Ranked, biggest expected information gain first.}}

1. {{check_1}}
2. {{check_2}}
3. {{check_3}}

## Ladder placement reasoning

{{growth_state.reasoning}} Candidate states at this revenue scale: {{candidate_states}}. Confidence build-up: {{confidence_notes as a short list}}.

## Caveats

{{Every caveat from the script output, including the low-confidence caveat when fewer than 6 quarters were supplied and the Wall caveat on any state 8+ placement. Close with:}} This check reads only the ARR series. The state placement is a hypothesis with the confidence shown, not a verified assessment.
