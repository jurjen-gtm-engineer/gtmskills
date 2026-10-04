# Scoring rubric: 9 axes

Score each axis 1 to 5 on a single call. **4 and up is mastery, 3 is sufficient, 3 is the coverage boundary.**

Every score of 3 or higher requires a verbatim quote with speaker attribution. No quote means the score drops to 2.

The anchors below are the calibration surface. When Phase 2 calibration disagrees with a human at the 2/3 boundary, edit the anchor wording here and re-score. Never hand-adjust a score.

## Two layers: coverage and status

The 1-5 score answers **"was it raised?"** (coverage bar 3, comparable to the WbD 57k benchmark). The **status** answers **"would this survive a deal review?"** It is the stricter layer. The idea of a deal-review evidence bar comes from Winning by Design's AI for GTM course; the wording of the tests below is this repo's own.

| Status | Rule |
|---|---|
| `gap` | Score 1 or 2. Includes every case with no quote: **if you cannot quote it, it did not happen.** |
| `partial` | Score 3 or higher, but the axis fails its **Qualified when** test below. |
| `qualified` | Score 3 or higher **and** passes the **Qualified when** test, on a verbatim **customer** quote. |

Score honestly rather than generously, and flag anything inferred rather than heard. A topic coming up is not evidence. For every `partial` or `gap` on Impact, Critical Event and Decision, write the `follow_up`: the exact question that closes the gap, phrased the way the rep would actually send it.

The status applies to the five SPICED axes only. The four Outcome Seller moves stay binary.

---

## Axis 1: Situation (S)

Binary ICP gate in SPICED, scored here for how well the rep established it.

| Score | Anchor |
|---|---|
| 1 | Situation never established. Rep does not know the account's shape at the end of the call. |
| 2 | Firmographics only, and mostly from the rep's own research read back at the customer. |
| 3 | Customer describes their current process, tooling or org in their own words, unprompted or on one question. |
| 4 | Rep establishes the specific operational situation that could produce the pain, with a follow-up. |
| 5 | Situation established and explicitly connected forward to pain: "so when X happens, what does that cost you". |

**Qualified when** the rep could describe their model, their team and their tooling well enough to **predict where their handoffs break**.
**Trap:** the customer only confirmed what the rep read out. That is the rep's research, not the customer's situation. Rep reads research back, customer says "yes, that's right": score 2, `gap`.

## Axis 2: Pain (P)

| Score | Anchor |
|---|---|
| 1 | No pain surfaced. |
| 2 | Rep asserts a pain from the playbook; customer neither confirms nor elaborates. |
| 3 | Customer names a problem in their own words. |
| 4 | Customer names the problem and the rep peels one layer (frequency, who it hits, what they tried). |
| 5 | Pain traced back to the situation that produces it, so it is diagnostic rather than a complaint. |

**Qualified when** a **named person** described a consequence **they personally absorbed**, and it arrived **unprompted**.
**Trap:** pain the rep suggested and the customer nodded at. A real problem described by someone who does not feel it (a consultant, a gatekeeper) is `partial`.

## Axis 3: Impact (I) **[carries the 1.44x]**

**The bar is a customer-articulated consequence, ideally with a number in it.** A rep saying the word "impact" is not impact. A rep asserting "so that's costing you a lot" is not impact.

| Score | Anchor |
|---|---|
| 1 | Impact never raised. |
| 2 | Rep asserts the value ("this usually saves teams 20%"). Customer does not take it up. |
| 3 | **Customer** articulates a consequence of the pain in their own words, qualitatively. Coverage starts here. |
| 4 | Customer quantifies it, or accepts and refines a quantification: hours, headcount, deals, euros, error rate. |
| 5 | Quantified in the customer's own units *and* both directions tested: what happens if solved, and what happens if not. |

**The diagnostic question, from the Outcome Seller fork:** on hearing pain, did the rep ask "if that problem were solved, what would happen to your business, and what happens if it is not?" or did they pivot to a demo? See Axis 9.

**Qualified when** they **did the arithmetic out loud**, or accepted the rep's number **without discounting it**.
**Trap:** a number the rep supplied is not the customer's number. A rep benchmark the customer did not take up stays at score 2. A qualitative consequence in the customer's words is score 3 and `partial`.

## Axis 4: Critical Event (CE) **[carries the 21% cycle compression]**

**A date is not a critical event. A date the customer can justify under one follow-up is.**

| Score | Anchor |
|---|---|
| 1 | No timing discussed. |
| 2 | A timeline for the *deal* ("we'd want to decide this quarter"). This is a preference, not a CE. |
| 3 | A customer date tied to something in their business. Coverage starts here. |
| 4 | Rep tests it: "what's happening that day", "what happens if you don't have this". |
| 5 | The consequence of slipping is on the record and it is real. Example: "the whole team is already booked to fly in for the launch that week." |

**Qualified when** there is a **date with a consequence attached that exists whether or not they buy from the seller**.
**Trap:** the seller's quarter end is not the customer's critical event. A date that only exists because of the seller's proposal, pricing deadline or quarter is score 2 at most.

## Axis 5: Decision (D) **[carries the +15.5% win rate]**

The rarest dimension in the WbD data: 6.8% coverage.

| Score | Anchor |
|---|---|
| 1 | Decision process never raised. |
| 2 | A name only ("I'd need to run it by my boss"), no process. |
| 3 | Criteria or process surfaced: who is involved, what steps, what the bar is. Coverage starts here. |
| 4 | Both criteria and process, with the roles mapped. |
| 5 | Decision mapped to the **impact** rather than to the pain: who is involved in the outcome, and who signs off on the number the customer just gave. |

**Qualified when** the rep can **name the signer**, state their **criteria in the customer's words**, and list the **steps to signature including procurement, legal and security**.
**Trap:** "they have a process" without the steps. Criteria in the seller's language ("they want ROI") instead of theirs is `partial`.

---

## The four Outcome Seller moves

Binary per call: observed / not observed / not applicable. These are the coachable units. "Sell on outcomes" is not coachable; one follow-up question in one moment is.

## Axis 6: The second question

On hearing pain, the rep asks what solving it is worth **before** offering the solution. Observed or not.

## Axis 7: The customer supplies the number

The rep asks for the quantification and lets the customer produce it, rather than supplying a benchmark. "Distributed team on spreadsheets, mistakes cost roughly $1,000 each, this many per month" said by the customer.

## Axis 8: "What breaks"

The rep tests a stated date with a consequence question. Observed or not.

## Axis 9: Demo pivot **[anti-pattern]**

The rep hears pain and moves to a demo, a deck or a feature walkthrough without the impact on the table. **This is the single most diagnostic moment on a recording.** Flag it with a timestamp and the quote.

Not a failing in itself: the demo still happens in the outcome-seller motion. It happens **after** the impact is on the table, which is what changes the price the conversation can carry. Score the ordering, not the demo.

---

## Not applicable

Any axis can be `null` with a reason. A first call that legitimately never reached decision criteria is not the same as a rep who avoided them. `null` is excluded from the coverage denominator; a score of 1 is not. Getting this wrong in either direction is the second-most common way a coverage number becomes indefensible.
