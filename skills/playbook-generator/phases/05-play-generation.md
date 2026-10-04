# Phase 5: Play Generation

## Purpose

Generate PVP and PQS plays using the discovered data sources and the Cannonball messaging methodology. This is Phase 5 of the Cannonball GTM Playbook Generator.

## Quality Bar

- **Narrative depth:** "What's the play?" is 100-150 words, "Why this works" is 80-120 words
- **Message length:** 60-80 words with Situation, Insight, Inquisition
- **Data convergence:** the best plays stack 3-4 data sources
- **DATA REQUIREMENT callouts:** every Internal/Hybrid play explains what data is needed
- **Message anatomy:** math stated inside the sentence, every headline number paired with a benchmark, the record identifier inline, confidence label in the play header (`PVP | Public + Internal | Strong (9.6/10)`)

## Inputs

- **All previous phase context** (in-context, not files):
  - Phase 1: company profile, ICP, persona
  - Phase 2: EDPs, pain segments
  - Phase 3: scored segments, top selections
  - Phase 4: discovered data sources, access paths

## Process

### 1. Synthesize previous phases

Combine all previous phase context:
- Target segments (from Phase 3)
- Available data sources per segment (from Phase 4)
- EDP and pain context (from Phase 2)
- Company profile and persona (from Phase 1)

### 2. Generate PVP plays

**PVP = Permissionless Value Proposition**

For each target segment with good data availability, create PVP plays following the `templates/play-template.md` format.

Each PVP must:
- Deliver value IN the message itself
- Be based on data from discovered sources (Phase 4)
- Use the Situation, Insight, Inquisition structure
- Stay within 60-80 words
- Reference specific data from specific sources
- Include NO product mentions
- Have a "What's the play?" section of 100-150 words explaining targeting logic
- Have a "Why this works" section of 80-120 words explaining psychology
- Include a DATA REQUIREMENT callout if using Internal or Public + Internal data

### 3. Generate PQS plays

**PQS = Pain-Qualified Segment**

For segments where PQS is the right approach, create plays following the `templates/play-template.md` format.

Each PQS must:
- Mirror the segment's exact situation with specificity
- Reveal something they do not know
- Quantify consequences using EDP data
- End with a routing question or truth-seeking inquisition
- Stay within 60-80 words
- Include NO product mentions
- Have a "What's the play?" section of 100-150 words
- Have a "Why this works" section of 80-120 words
- Include a DATA REQUIREMENT callout if using Internal or Public + Internal data

### 4. Push for multi-source convergence and temporal depth

The best plays stack multiple data sources AND cover the temporal dimension. For every play, run two checks:

**Data Key stacking (from Phase 2):**
- How many Data Keys support this play? (1 is good, 2 is strong, 3 means the messaging writes itself)
- Can I add a second Data Key that creates Venn-diagram targeting on the same segment?
- Plays with 2+ Data Keys should be flagged for highest scoring potential

**Temporal indicator coverage (from Phase 4):**
- Does this play have a **leading indicator** (active risk, warning-based messaging)?
- Does this play have a **trailing indicator** (materialized consequences with dollar amounts, credibility-based messaging)?
- The best plays have BOTH: the leading indicator makes it feel like a timely warning, the trailing indicator proves what happens to companies that wait

For every play, ask:
- Can I cross-reference a second data source to make this more specific?
- Can I add a deadline calculation from a regulatory database? (leading indicator)
- Can I add enforcement actions or settlement data to prove the pain is real? (trailing indicator)
- Can I layer industry data on top of company-specific data?

A top-scoring play typically combines a tech-detection or registry data key with a regulatory or court-record trailing indicator, 3-4 sources total. Aim for that level of convergence.

### 4b. Write receipts and run the buyer's-eye pass (per play)

For every play, before scoring:

**Show the math inline and keep an internal receipt.** In the message body, write the derivation into the sentence and name the retrievable record: "620,000 of 840,000 emails (74%)", "inspection #1598334 on Nov 18, 2025 (penalty: $43,200)". Separately, keep an INTERNAL receipt line per figure (figure, source and field, calculation, retrievable record ID) as a QA gate. Any number that cannot resolve to a record the buyer could look up is invented: cut it, or the play caps at 7.5. The receipt worksheet is internal working copy, stripped from the deliverable.

**Anchor every headline number against a benchmark.** Pair each metric with a peer, national, or prior-period comparison. The delta is the urgency. A raw number with no comparison is weaker.

**Buyer's-eye pass.** Re-read the drafted message AS the named persona: does it feel like inside knowledge or a database readout? Would they feel seen or handled? Is there one line worth forwarding? A lifeless record-dump caps at 8.0 no matter how deep the data. Note the single weakest line for the human rewrite.

**Trust the targeting, not the copy.** The machine is trusted for the segment, the record, and the proof, not the words. The deliverable does NOT stamp DRAFT on each message or add per-play "make it yours" blocks. The human last-mile appears ONCE, in the closing "How to use the drafts" note.

### 5. Create the bad email example

Generate a REALISTIC "typical SDR email" for this specific company:
- Use the company's actual product language and positioning
- Write a full email a real SDR would send today (not template placeholders)
- Include: generic subject line, congratulations on something obvious, feature bullets, meeting request
- The reader should cringe because they have seen this exact email 1,000 times
- Write a specific teardown explaining why THIS email fails for THIS company's prospects

### 6. Create the hard data vs soft signal comparison

**Soft (what everyone does):** a specific example of a soft signal for this company's vertical, e.g. "I see you're hiring for [role]" (job postings, everyone sees this).

**Hard (what works):** an actual data point from one of the plays above, e.g. "Your facility received 3 communication-related violations during the November state inspection."

### 7. Quality over quantity

Generate as many plays as the data supports at 8.0+ quality:
- If only 4 plays score 8.0+, generate 4 plays
- If 16 plays score 8.0+, generate 16 plays
- NEVER pad with weak plays to hit a target count
- Every play must earn its spot in the playbook

## References

- `templates/play-template.md`: play format, message rules, scoring
- `knowledge/methodology.md`: core methodology

## Output

**In-context only. Do NOT save to file.** This feeds Phase 6.

Include:
- Bad email example (realistic, company-specific)
- Hard data vs soft signal comparison
- All PVP plays (fully formatted per template)
- All PQS plays (fully formatted per template)
- Each play with complete documentation: title, targeting logic, reasoning, data sources, message (with inline math, record IDs, and a benchmark anchor), DATA REQUIREMENT (if applicable)
- Internal-only per play (stripped from the deliverable): receipts worksheet, buyer's-eye weakest-line note
