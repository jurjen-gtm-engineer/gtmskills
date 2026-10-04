---
name: outcome-seller-scoring
description: Turn call recordings into a per-rep SPICED coverage heatmap and a 50,000-run Monte Carlo of rep-level revenue. Scores every call on the 5 SPICED axes plus the 4 Outcome Seller moves, marks each SPICED axis Qualified / Partial / Gap against WbD's quote-or-Gap deal-review bar, reports coverage and qualified rate per dimension (org view and per-rep view), then simulates P10/P50/P90 revenue per rep per month, splits the team on the 80% ladder, ranks which lever closes the gap, and prices the coaching case by simulating the middle cohort at top-cohort coverage. Use for "score these calls", "rep scorecard", "SPICED coverage", "call archive diagnostic", "how much revenue is coaching worth", "Monte Carlo the reps", or a free call-assessment offer. Built on Winning by Design's SPICED and Jacco van der Kooij's Outcome Seller webinar (Aug 2026). Not for extracting competitive or handoff notes from calls (conversational-intelligence) or a quick SPICED score on a few transcripts (spiced-call-scorecard).
metadata:
  version: "1.1"
---

# Outcome Seller Scoring

## What this is

Two machines wired together, from Jacco van der Kooij's Aug 2026 WbD webinar:

1. **Coverage.** Score every recorded call against SPICED, report the fraction of calls on which each dimension was genuinely raised. Coverage is a behaviour metric, so unlike win rate it is coachable weekly, per person. Reference numbers from ~57,000 calls: Impact 20.6%, Critical Event 21.7%, Decision 6.8%.
2. **Monte Carlo.** Run 50,000 simulations on the *rep*, not the funnel, from ranged metrics (min, max, **mode**). Output P10/P50/P90 revenue per rep per month, a three-cohort split against the 80% ladder, and a sensitivity ranking of which lever actually closes the gap.

**The wiring is the point, and it is this skill's addition, not WbD's.** Jacco runs these as two separate exercises. Coupling them means the recordings supply the behaviour deltas that move the simulation, so the question stops being "how are the reps performing" and becomes **"what is this coaching gap worth in ARR, with a probability attached."** That is the deliverable.

**Deterministic-first.** In the webinar the Monte Carlo is run by asking an LLM to simulate. This skill does not. `montecarlo.py` runs the real thing in numpy with a fixed seed, so the number is reproducible and anyone can recompute it. An LLM narrating a distribution is a memory, not a number. The LLM's job here is scoring calls, which is the part that genuinely needs judgment.

## The evidence this rests on

| Dimension | Coverage (57k calls) | Lift when present |
|---|---|---|
| Impact | 20.6% | +44% revenue per account (1.44x) |
| Critical Event | 21.7% | 21% shorter cycle (66 days to 52) |
| Decision | 6.8% | +15.5% win rate |

These are Winning by Design's own numbers, from anonymised client data, as presented in the Outcome Seller webinar. They are single-study, self-reported vendor data. When you put one in a deck, name the source and say so.

---

## What a recording has to yield

This is the intake contract. Ask for it before you promise an output.

**Per call, required:**
- Transcript with **speaker attribution** (who said what). A transcript without speakers cannot be scored: the whole rubric turns on whether the *customer* articulated the impact or the *rep* asserted it.
- Rep name (or a stable pseudonym), call date, account, **call type**.
- Call type must be discovery or qualification. Filter out renewals, check-ins, support and internal calls before scoring. Scoring a renewal for critical-event coverage produces noise.
- Duration. Drop calls under 10 minutes: a 6-minute reschedule is a structural zero, not a coverage failure.

**Per rep, for the Monte Carlo, from the CRM (not from the recordings):**
opportunities per month, disqualification rate, win rate **measured after qualification**, ACV, discount level, sales cycle. Pull 90 days and ask for min, max and **mode** per metric.

**If the CRM metrics are not available**, the simulation can still run off team-level ranges with per-rep coverage as the only differentiator (see Phase 4, coverage-bridge mode), but say clearly in the deliverable that the per-rep spread is modelled from behaviour, not measured from outcomes.

### The sample-size ladder

Do not sell an output the sample cannot carry. This is the most common way this deliverable fails.

| Calls available | What you can honestly deliver |
|---|---|
| **1 call** | A scorecard and a coaching note for one rep. No coverage rate. A single call is one Bernoulli draw. |
| **5 calls, 1 rep** | A rep-level pattern with wide error bars. This is WbD's own free-assessment size, and it is a sales motion, not a diagnostic. |
| **8+ calls per rep** | A per-rep coverage rate with a Wilson interval attached. Report the interval, always. |
| **20+ calls, 5+ reps** | The heatmap and the cohort split. |
| **100+ calls, 10+ reps** | The full Monte Carlo with per-rep ranges and a defensible sensitivity ranking. |

At every tier the coverage rate carries its confidence interval into the report. At 8 calls a rep with 2 impact-covered calls has a 95% Wilson interval of roughly 7% to 55%. That is not a rep who "raises impact 25% of the time", and a heatmap cell that pretends otherwise will get the whole deliverable thrown out on the first challenge.

---

## Phase gate

Run **one phase, then stop for review.** Do not run the simulation on scores nobody has checked.

---

## Phase 1: Intake and filter

1. Pull transcripts. Any call recorder works (Fireflies, Gong, a CRM's call recordings) and so do raw transcript files. Use `conversational-intelligence` if you also need competitive or handoff extraction from the same archive: this skill is the scoring lane only.
2. Build `calls.jsonl`, one object per call: `call_id`, `rep`, `date`, `account`, `call_type`, `duration_min`, `transcript`.
3. Apply the filters above. **Report what you dropped and why.** A drop rate over 40% usually means the archive is mostly not discovery, which changes the engagement.
4. Print the ladder position: calls, reps, calls per rep (min/median/max).

**Stop. Confirm the corpus and the ladder tier with the operator before scoring.**

## Phase 2: Calibration (do not skip)

An LLM scoring against a rubric it also wrote will agree with itself. Anchor first.

1. Pick 5 calls spanning the expected range. Have a human (the team's own sales leader, ideally, not the person running this skill) score them blind on the 9 axes.
2. Score the same 5 with the rubric.
3. Compare. Target: within 1 point on 80% of cells, and **zero disagreements on the coverage boundary** (score 3). A cell where the human says 2 and the model says 3 flips a coverage bit and is the only disagreement that actually matters.
4. If the boundary disagrees, tighten the anchor wording in `references/spiced-rubric.md` for that axis and re-run. Do not adjust scores by hand.

Record the calibration result in the deliverable. It is the answer to "how do we know your AI got this right", and having one is a differentiator against a vendor who does not.

**Stop. Show the calibration table.**

## Phase 3: Score

Fan out one **sub-agent per call**. Each sub-agent gets: the transcript, `references/spiced-rubric.md`, and `references/score_schema.json`. Each returns one JSON object.

Hard rules for the scorer, restated in every sub-agent prompt:

- **Score "raised", not "mentioned".** A rep saying the word impact is not impact. The bar for Impact is a **customer-articulated consequence, ideally with a number in it**. Without this rule the coverage rate inflates and the diagnostic dies.
- **Return the quote that justified the score**, verbatim with speaker attribution, in the same object. A score without its quote is unauditable and gets deleted.
- **Never estimate.** If the dimension never came up, score it 1 and set the quote to null. Do not infer from context.
- **The Critical Event bar is "what breaks".** A date is a preference. A date the customer can justify under one follow-up question is a critical event.
- **Set the status on every SPICED axis: `qualified`, `partial` or `gap`** (the "Two layers" section of `references/spiced-rubric.md`). The score says the topic was raised; the status says it would survive a deal review. Apply each axis's **Qualified when** test strictly: a number the rep supplied is not the customer's number, the seller's quarter end is not the customer's critical event, and a customer who only confirmed the rep's research has not described their situation. Qualified needs a customer quote. Score honestly rather than generously.
- **Write the `follow_up` for every `partial` or `gap` on Impact, Critical Event and Decision**: the exact question that closes it, phrased the way the rep would send it.
- **Return two moments, not one.** `blind_spot`: what they said, what the rep said, what the rep should have said. `strongest_moment`: the quote, why it worked, written so it can be handed to the team. Then `crm_summary`. The positive moment is not decoration: a scorecard that only finds faults gets rejected by the reps it is meant to coach.

Write to `scores.jsonl`. Validate every object against the schema before proceeding: any object missing a quote on a score of 3 or higher is a scoring failure, not a data point. `coverage.py` also fails on a status that contradicts its score, a `qualified` without a customer speaker, and a missing `follow_up`.

**Stop. Spot-check 10 scored calls against their quotes before aggregating.**

## Phase 4: Coverage and the heatmap

`python3 coverage.py scores.jsonl --out coverage/`

Produces:
- **Org view.** Coverage rate per dimension across the whole corpus, with a Wilson interval, next to the WbD 57k benchmark. This answers "is this a training problem": a 6.8% decision rate is not twelve people with a habit, it is an organisation that never taught the move.
- **Per-rep heatmap.** One row per rep, one column per axis, coverage rate with n. The dark bands are the coaching plan.
- **Segment cuts.** By region, segment, tenure and cohort if the metadata supports it. A single org-wide number hides the distribution that makes the case.
- **The demo-pivot count.** The one anti-pattern axis: the moment a rep hears pain and goes straight to a demo. It is the single most diagnostic moment on a recording and it reads as a *behaviour*, not a score, which makes it the easiest thing to coach on Monday.

**Read Coverage next to Qualified.** Coverage (3+) is the number to hold against the WbD benchmark, because the benchmark counts a dimension as present. Qualified is the deal-review number. The gap between them is the share of calls where the topic came up but would not survive a deal review, and on Impact and Critical Event that gap is usually the coaching plan: reps raise it, they do not land it.

Attach the lift to every coverage number. Coverage alone reads as process policing; coverage plus "+44% revenue per account when present" reads as money left on the table.

**Stop. Review the heatmap.**

## Phase 5: Monte Carlo

`python3 montecarlo.py --config sim_config.json --n 50000 --seed 42 --out sim/`

**Distribution.** Triangular on (min, mode, max) per metric. Triangular is the correct family precisely because Jacco insists on the mode: the average of 6 and 12 is 9, but the population is dense at 7 and 8, and a symmetric distribution models a team you do not have. Use lognormal for ACV instead when the ACV spread is over 3x (a $38k to $150k platform), because a triangular ACV understates the tail that a single large deal puts in a rep's month.

**Revenue identity per rep per month:**

```
qualified_opps = opps_per_month * (1 - disqualification_rate)
revenue        = qualified_opps * win_rate * ACV * (1 - discount_rate)
```

Win rate is applied **after** qualification. If it is not measured that way in the client's CRM, fix the input or the whole model is wrong, because every team quietly moves that marker until the number looks acceptable.

**Outputs:**
1. **P10/P50/P90 per rep per month.** Note the convention: WbD's P10 is the level 90% of runs clear (the pessimistic end). `montecarlo.py` reports both conventions explicitly labelled, because getting this backwards inverts the board conversation.
2. **The skew, and a terminology trap.** Expect the mass to pile on the **left**, with a thin tail of high performers to the right. The cause is not discounting or seasonality, it is that **more reps sit at the low end of win rate than the high end**. That shape is the argument against planning on the average. Note that "leans left" in the source means mass-on-the-left, which is **statistically positive skew**: reading it as negative skew inverts the finding, so the script reports `mass_on_the_left` as a boolean rather than making anyone interpret the sign. If the distribution comes back symmetric or right-massed, the modes were probably guessed rather than pulled.
3. **Three-cohort split on the 80% ladder.** Only meaningful with **per-rep metrics from the CRM**. In coverage-bridge mode the whole spread between reps comes from call behaviour, which explains far less of real rep variance than the CRM does, and the script marks the table `behaviour_only` and refuses to present it as a finding. Do not put a behaviour-only cohort table in front of a client. With measured inputs: mid = 80% of top, low = 80% of mid, so low is roughly 64% of top. Compare each cohort against where the ladder says it should be. **Expect the anomaly in the middle**: in the source case the middle group sat at ~$20.4k where the ladder said ~$24.8k.
4. **Sensitivity, two ways.** One-at-a-time swing (move each metric min to max, hold the rest at mode) and a global Spearman rank correlation between each sampled input and the simulated output across all 50,000 runs. The global pass is the honest one because it accounts for interaction, and it costs nothing since the samples already exist. Report both; if they disagree, the OAT ranking is the one to distrust.

**In the source case opportunity volume ranked last**, behind price, discount, win rate, sales cycle and qualification. That is the uncomfortable finding for anyone who sells list building, and it is the reason to run this **before scoping another pipeline-generation sprint**: if price, discount and win rate outrank opportunity count, more leads buys the team very little and the honest recommendation is downstream work. Saying that out loud is worth more than the sprint.

**But do not expect that ranking, verify it.** Every term in the identity is multiplicative, so the ranking is driven by each metric's **relative spread**, not by anything intrinsic. On ranges where opportunity count varies as widely as win rate, volume ranks first, and it deserves to. The script prints the coefficient of variation next to every coefficient so the reader can see what is driving the order. This is also why guessed ranges are worse than no ranges: they produce a confident ranking that points at the wrong lever.

**Stop. Review the distribution and the cohort split.**

## Phase 6: The coaching case (the coupled output)

This is where the two machines meet.

`python3 montecarlo.py --config sim_config.json --coverage coverage/per_rep.json --scenario middle_to_top --out sim/`

The bridge maps a rep's measured coverage onto their metric modes:

| Coverage axis | Moves | Anchor |
|---|---|---|
| Impact | ACV mode, up to 1.44x | +44% revenue per account |
| Decision | win-rate mode, up to 1.155x | +15.5% win rate |
| Critical Event | sales-cycle mode, down to 0.79x, which raises opps per month | 66 days to 52 |

**This bridge is an inference and must be labelled as one in every client-facing artefact.** WbD's lift is measured **binary and per call** (was the dimension present on this call, yes or no). Applying it as a **linear scaler on a rep's coverage rate** is our extrapolation, not their claim, and it almost certainly overstates the low end (a rep at 0% coverage does not sell at a 1.0x floor for unrelated reasons). `montecarlo.py` therefore also runs a **conservative variant** that applies only half the published lift, and the deliverable reports the range between them. If the coaching case only survives at full lift, it does not survive.

**The headline scenario:** hold everything else fixed and lift the middle cohort's coverage to the top cohort's measured coverage. Not to a theoretical maximum, to what people **in this same company, selling this same product** already do. Report the delta as monthly and annualised revenue with a probability attached, never as a point estimate.

**Why the middle cohort.** The instinct is to fire the bottom or clone the top. Bottom performers are expensive to lift, top performers are already at ceiling. The middle is a large population sitting measurably below its own tier, and it is the only one where a coaching intervention has both room and receptiveness.

Hand the output to whoever runs call coaching: the dark bands become the weekly call-review themes, two or three calls on the **same** theme per 60-minute session.

## Phase 7: Deliver

Lead with the coverage table and the recoverable revenue, not with the method. Nobody asked for a scoring harness. Put the result first, give every chart a title that states its finding, and keep the method in an appendix.

---

## Cautions, all of them load-bearing

- **Coverage becomes a target.** Reps learn to say the words. This is why the customer-articulated-with-a-number bar matters, and why the heatmap is a **coaching input, never a compensation input**. Put that sentence in the deliverable, in writing, before the client's VP Sales has the idea themselves.
- **The Monte Carlo is a system-wide model.** It absorbs whatever was happening (a budget freeze, seasonality, a bad quarter) into the ranges rather than isolating it. That is a feature for "what is this team capable of" and a trap for "why did last quarter miss". Do not answer the second question with this tool.
- **The ranges are the model.** Garbage ranges produce a confident garbage distribution, and the mode is the field most often guessed. If the client cannot produce a mode from the CRM, that is a finding about their data, and it belongs in the report.
- **The 80% ladder is a heuristic**, presented by WbD as historically true and not derived. Treat a cohort gap as a flag to investigate, not as a target to manage to.
- **Grading your own homework.** Phase 2 exists for this reason. Skipping it makes every number downstream unfalsifiable.
- **Vendor data.** The lifts are WbD's own, self-reported, from anonymised client data, and several figures in the source transcript are garbled. The dataset size and the specific *negative* findings (6.8% decision coverage, volume ranking last) raise credibility, because nobody invents unflattering numbers about their own methodology. Cite it as WbD's data, named.

## Files

| File | Purpose |
|---|---|
| `references/spiced-rubric.md` | The 9 axes with 1-5 anchors, plus the Qualified / Partial / Gap status layer and each axis's **Qualified when** test. The calibration surface: edit anchors here, never hand-adjust a score. |
| `references/score_schema.json` | Per-call output contract. A score of 3+ without a verbatim quote is a validation failure. |
| `coverage.py` | Coverage and qualified rates with Wilson intervals, per-rep heatmap, segment cuts. Exits non-zero on unquoted scores, inconsistent statuses or missing follow-ups unless `--allow-invalid`. |
| `montecarlo.py` | 50,000-run simulation, cohort split, two-pass sensitivity, coverage bridge, scenario. Fixed seed. |
| `examples/make_fixture.py` | Synthetic 137-call corpus shaped like the source case, for smoke-testing the harness. **Never ship a number that came out of it.** |
| `examples/sim_config.json` | Source-case team ranges. Replace with your own 90-day min/max/mode. |
| `examples/sim_config_measured.json` | Same, plus per-rep CRM overrides. This is the shape that makes the cohort split real. |

Smoke test, end to end:

```bash
python3 examples/make_fixture.py
python3 coverage.py examples/scores.jsonl --out examples/coverage
python3 montecarlo.py --config examples/sim_config_measured.json     --coverage examples/coverage/per_rep.json --scenario middle_to_top --out examples/sim
```

Related skills in this repo: `spiced-call-scorecard` (a quick SPICED score on a few transcripts), `conversational-intelligence` (account extraction from the same archive), `gtm-diagnostic` (this fits as one finding with a number attached), `meeting-prep` (prep for a single call).

## Credits

SPICED is a Winning by Design framework. The coverage numbers, the 80% ladder, the mode-based ranges and the rep-level Monte Carlo idea come from Jacco van der Kooij's Outcome Seller webinar (Winning by Design, August 2026). The scoring harness, the numpy simulator, the Wilson intervals, the conservative half-lift variant and the coupling of coverage to the simulation are original to this repo.
