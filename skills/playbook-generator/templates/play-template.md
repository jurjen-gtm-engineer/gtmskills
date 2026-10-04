# Play Template

## Play Header Format

Each play uses a clean badge-style header with methodology type:

```
### {{PLAY_TYPE}} | {{METHODOLOGY_TYPE}} | {{DATA_TYPE}} | {{SCORE_LABEL}} ({{SCORE}}/10)
### {{PLAY_TITLE}}
```

Example:
```
### PQS | Regulatory Triggers | Public Data | Strong (9.1/10)
### {{EXAMPLE_PLAY_TITLE}}
```

### Methodology Types

Classify each play into one of these types:

| Type | When to use |
|------|-------------|
| **Regulatory Triggers** | Play driven by compliance deadlines, enforcement actions, regulatory filings, government citations |
| **Multi-Signal Composite** | Play cross-referencing 3+ data sources to create a unique convergence signal |
| **Install Base Detection** | Play targeting existing users of a specific tool/platform with optimization opportunities |
| **Custom Research** | Play built on proprietary analysis/benchmarking delivered as the value |
| **Competitor Intelligence** | Play using competitive positioning data (tech stack, market share, switching signals) |
| **Technology Detection** | Play driven by tech stack identification (stack detectors, page-source search, job postings) |
| **Account Mapping** | Play focused on contact/decision-maker discovery and deal mapping |
| **Market Sizing** | Play quantifying untapped opportunity or addressable market for the prospect |
| **Contact Discovery** | Play identifying the right person/team handling a specific situation |

Most playbooks should have a mix. Regulatory Triggers and Multi-Signal Composite are the most common types among high-scoring plays.

---

## Play Types

### PVP (Permissionless Value Proposition)
- "I already did the work": transfers value IN the email itself
- Recipient would pay to receive this intelligence, even if they never buy
- The email isn't "please": it's proof you understand their business
- Highest scores (9.0+) when the value is delivered, not promised

### PQS (Pain-Qualified Segment)
- A group unified by a pain point, not demographics
- Re-describes their situation so precisely they think "how did you know?"
- Reveals something they don't know or haven't connected
- Ends with an Inquisition (asks for truth, not time)

---

## Data Types

- **Public Data:** government databases, regulatory filings, public records, court filings
- **Internal Data:** the company's own proprietary data/analysis
- **Public + Internal:** synthesis of both (most powerful, hardest to replicate)

---

## Score Labels

- **Strong (9.0-10):** highly specific, immediately actionable, defensible data, multi-source convergence
- **Strong (8.0-8.9):** very specific, good data, clear value
- **Okay (7.5-7.9):** decent specificity, some generic elements
- **Weak (below 7.5):** too generic, weak data, limited value. Do NOT include in the playbook.

---

## Play Structure

### {{PLAY_TITLE}}

**What's the play?**
{{TARGETING_LOGIC, 100-150 words}}

> This section explains the complete targeting logic: WHO you're targeting, WHAT data you're cross-referencing, and WHY this specific combination creates urgency. Include the regulatory mechanics, business dynamics, or competitive pressures that make this play work. Name specific databases, deadline calculations, and convergence points. The reader should understand exactly how to execute this play and why it's defensible.

**Why this works**
{{PSYCHOLOGICAL_REASONING, 80-120 words}}

> This section explains the psychology and strategic reasoning. Why will the prospect respond? What makes this different from generic outreach? What do they learn from this message that they didn't know? Why can't they just delete this? Be specific about the emotional or business response this triggers. Reference what competitors can or can't replicate.

**Data Sources**
{{DATA_SOURCES_WITH_FIELDS}}

> List each data source with the specific fields used. Format:
> - Source Name (url if applicable): field_1, field_2, field_3, description of what it provides

**The message:**

```
Subject: {{SUBJECT_LINE}}

{{MESSAGE_BODY, 60-80 words}}
```

> **Show the math INLINE, not in a table.** Write the derivation into the sentence and name the specific record. State the calculation in the copy: `12 custodians account for 620,000 of the 840,000 emails (74%)`, `rate moved 0.89 to 1.05 (18% jump) in Q2`. Put the retrievable identifier inline: `inspection #1598334 on November 18, 2025 (penalty: $43,200)`. The message body IS the receipt. No separate worksheet block appears in the deliverable.

**Receipts** *(INTERNAL working copy only, strip from the deliverable)*
{{RECEIPTS, one line per figure used in the message}}

> A QA discipline, not a client-facing artifact. One line for every number, date, count, percentage, or deadline: `{{figure}}` -> {{source + field(s)}} -> {{calculation}} -> {{retrievable record ID + where to pull it}}. Every figure must resolve to a record the buyer could look up. A number with no retrievable record is invented: cut it, or the play caps at 7.5. The client-facing expression of these receipts is the inline specificity above plus the Data Sources reference table.

**Make it yours** *(INTERNAL note, strip from the deliverable)*
{{ONE_LINE: the buyer's-eye pass's single weakest line, flagged for the human rewrite. The deliverable expresses the human last-mile ONCE, in the closing "How to use the drafts" note, not per play.}}

**DATA REQUIREMENT** *(include for Internal Data and Public + Internal plays)*
{{DATA_REQUIREMENT_DESCRIPTION}}

> Explain what proprietary data is needed to execute this play. What must the company collect, track, or have access to? Why can't competitors replicate this? For Public + Internal plays, explain which parts are public vs proprietary and how the synthesis creates unique value.

---

## Message Rules

### The Structure: Situation, Insight, Inquisition

Every message follows this structure, with enough room to land the insight properly:

1. **Situation:** name their exact condition with specific data (dates, numbers, identifiers)
2. **Insight:** reveal something they don't know or haven't connected. Include quantified consequences, deadline calculations, or hidden convergence points.
3. **Inquisition:** ask for truth, not time. Route to the right person or validate the situation.

---

### PQS Messages (Pain-Qualified Segment)

**Situation:**
- Name the exact condition with verifiable specifics
- Tools, dates, numbers, permit IDs, violation records, contract terms
- "Your facility received 3 communication-related violations during the November state inspection"

**Insight:**
- One unique revelation about their situation
- Include quantified consequences or hidden deadline connections
- "The regulator requires a 23-day correction plan or the facility faces program termination"
- **Show the derivation inline.** Write the calculation into the sentence, not a footnote: "620,000 of 840,000 emails (74%)", "0.89 to 1.05, an 18% jump". The reader sees the math without leaving the message.
- **Anchor against a benchmark.** Compare the prospect to a peer, national, or prior-period baseline: "moved from better-than-national to worse-than-national", "vs the average across the other 135". The delta is what creates urgency; a raw number without a comparison is weaker.

**Inquisition:**
- Ask for truth, not time. Route to the person handling this.
- "Who's coordinating the emergency remediation?"
- "Is legal already handling the response filing?"
- "Is someone already evaluating screening tools?"
- NEVER: "Would you be open to a call?" / "Can we schedule 15 minutes?"

**Key rule:** say NOTHING about your product. Only re-describe their situation.

---

### PVP Messages (Permissionless Value Proposition)

**Value Delivery:**
- Lead with the work you already did
- "Tracked your last 12 inbound leads from [local platform] in [zip code]: 8 of them booked"
- The intelligence IS the message

**Impact:**
- Connect the data to their specific situation with quantified impact
- "You're barely active there but it's your highest-converting source"

**Lightweight Offer:**
- Offer the deliverable or ask who should receive it
- "Want the list of which posts drove those 8 bookings?"
- The ask is lightweight because you've already proven value

**Key rule:** the value is IN the message, not promised for later. The email isn't "please": it's proof.

---

### Subject Line Rules

- **3-9 words.** Below 3 is too cryptic. Above 9 is describing instead of labeling.
- **Aim for 3-5 words on the highest-confidence plays.** When the data is unimpeachable, the shortest subject wins (the body delivers the rest).
- **Label, not a pitch.** A subject names the situation; it does not pitch a benefit.
- **Lead with the specific data, not the framing.** "Your repeat-violation status" beats "Heads up about your inspection findings."
- **Use specific identifiers, dates, codes** when available: citation codes, case numbers, dollar figures, exact dates.
- **No brand name. No fluff. No cleverness.** No hooks ("Quick question"), no follow-ups ("Following up"), no benefits ("Transform your X").
- **Use the prospect's possessive** when it makes the subject feel like inside knowledge: a "Your ..." prefix is the most common strong opener.

---

### Language Rules

**ALWAYS:**
- Use specific numbers, not ranges: "$340 per order" not "significant costs", "22% rework rate" not "high rework"
- Name specific entities (tools, permits, people, regulations, case numbers)
- Include exact dates or time windows: "March 1st abatement deadline" not "upcoming deadline"
- Reference specific regulations/requirements
- Write at an 8th-grade reading level
- **Keep the total message to 60-80 words**
- Format as: Situation, Insight, Inquisition
- Include deadline calculations when applicable
- **Every play must include at least 2 specific numbers** (dollar amounts, percentages, dates, counts)
- **PQS messages must end with a routing question:** "Who's handling the February 12th abatement deadline?", "Is legal already involved?", "Is one system tracking documentation across all 3 sites?"

**NEVER:**
- Use "companies like yours"
- Say "research shows" or "industry data suggests"
- Include any product positioning in PQS messages
- Use hedge words (might, could, possibly)
- Use "Quick question" as a subject
- Lead with case studies or customer logos
- Include a CTA that asks for time instead of truth: NEVER "Would you be open to a call?", "Can we schedule 15 minutes?", "Do you have time this week?"
- Personalize to the person ("I saw you went to [university]") instead of the condition
- Use vague quantifiers ("significant", "many", "often", "growing", "increasing")

---

## Scoring

### Single Composite Score

Each play gets a single score (1-10) based on internal evaluation of:
- **Specificity:** company-specific data vs generic claims
- **Data Availability:** public API/database vs hard-to-obtain
- **Existential Impact:** business survival risk vs minor annoyance
- **Actionability:** can act today vs unclear next steps
- **Data Depth:** Data Key stacking (1 key is baseline, 2+ is Venn-diagram targeting) plus temporal indicators (leading = active risk warning, trailing = materialized consequences with dollar amounts). Plays with 2+ Data Keys and both indicator types are the strongest.
- **Buyer's-eye read:** read the message AS the persona. Does it feel like inside knowledge or a database readout? Would they feel seen or handled? Is there a line worth forwarding? A message strong on data but reading as a lifeless record-dump **caps at 8.0** regardless of the other lenses. Producer-side scoring cannot see this failure; only the buyer's-eye pass catches it.
- **Receipts complete:** every number in the message traces to a retrievable record in the Receipts block. Any un-sourced figure caps the play at 7.5.

The multi-criteria breakdown is used internally for QA but NOT shown in the playbook output. Only the composite score and label appear in the play header. The **Receipts** and **Make it yours** blocks are INTERNAL working copy only: strip them from the deliverable. Their client-facing expression is the inline math and record IDs in the body, the Data Sources reference table, and the single closing "How to use the drafts" note.

### Score Thresholds

- **9.0+:** must include. Lead plays. Multi-source data convergence, company-specific, immediate urgency.
- **8.0-8.9:** strong plays worth including if they add a unique angle.
- **7.5-7.9:** only include if no better alternative exists for that segment.
- **Below 7.5:** do not include. If the best play for a segment scores below 7.5, the data isn't strong enough.

### Quality Over Quantity

Generate as many plays as the data supports, not a fixed number. If only 4 plays score 8.0+, the playbook has 4 plays. If 16 plays score 8.0+, the playbook has 16 plays. Never pad with weak plays to hit a count.

---

## DATA REQUIREMENT Callout

Include a DATA REQUIREMENT block on every play that uses **Internal Data** or **Public + Internal** data:

```
**DATA REQUIREMENT**
This play requires [specific data needed] with [specific fields].

[Explain why this is proprietary / why competitors can't replicate it.]
```

For **Public Data** plays, DATA REQUIREMENT is optional: only include it if the data source requires special access or cross-referencing.
