# Phase 6: Scoring & Assembly

## Purpose

Score plays, rank them, and assemble the final playbook. This is Phase 6 (final) of the Cannonball GTM Playbook Generator.

## Inputs

- **All previous phase context** (in-context, not files):
  - Phase 1: company profile, ICP, persona
  - Phase 2: EDPs, pain segments (NOT included in output)
  - Phase 3: scored segments (NOT included in output)
  - Phase 4: discovered data sources, access paths
  - Phase 5: generated plays, bad email, hard vs soft comparison

## Process

### 1. Score each play (internal only)

For each play from Phase 5, calculate the composite score:

| Criterion | Score (1-10) |
|-----------|--------------|
| **Specificity** | Company-specific data vs generic claims |
| **Data Availability** | Public API or bulk file vs proprietary data |
| **Existential Impact** | Business survival vs minor annoyance |
| **Actionability** | Can act today vs unclear next steps |
| **Data Depth** | Data Key stacking plus temporal indicator coverage (see guide below) |

**Composite Score** = (Specificity + Data Availability + Existential Impact + Actionability + Data Depth) / 5

**Two hard caps applied after the composite (both catch failures the composite hides):**
- **Buyer's-eye cap:** read the message AS the persona. If it reads as a record-dump rather than inside knowledge (feels handled not seen, nothing worth forwarding), cap the play at **8.0** no matter how deep the data. Note the weakest line for the human rewrite.
- **Receipts cap:** if any number in the message lacks a retrievable record in its receipts worksheet (a record the buyer could look up), cap the play at **7.5**. A claim you cannot source is a claim you cannot send.

**Buyer's-eye thresholds:** a PQS message must clear 7.0 when graded as the buyer; a PVP gift must clear 8.5 (a gift that is not worth having is worse than no gift). Below the bar: rewrite or kill, never ship.

**Data Depth scoring guide:**
- **9-10:** 2+ Data Keys plus both leading and trailing indicators. Venn-diagram targeting with full temporal proof.
- **7-8:** 1 Data Key plus both indicators, OR 2+ Data Keys plus one indicator
- **5-6:** 1 Data Key plus one indicator (leading or trailing, not both)
- **3-4:** 1 Data Key only, no temporal dimension: enrichment-level data, not segment-defining
- **1-2:** no clear Data Key: segment based on hunch, not a findable boundary condition

**This scoring table is for internal use only. It is NOT included in the output.** Only the composite score appears in each play's header badge.

### 2. Filter and rank

- **Remove** any play scoring below 8.0 (below 7.5: never include; 7.5-7.9: only if no better alternative)
- **Rank** PQS plays by score (highest first)
- **Rank** PVP plays by score (highest first)
- **Final gate (the competitor test):** every surviving play must be hyper-specific, factually grounded, and non-obvious. A message a competitor selling the same category could send word-for-word fails and goes back to Phase 5.
- **Clean no-fit is valid:** if no plays survive, write up what was tried and where the data ran out. Do not invent plays.

### 3. Assemble the final playbook

Use `templates/playbook-template.md` as the base format.

**Sections to include (in order):**

1. **Who is [sender]?** Short intro from the sender identity provided at the start (or leave the placeholder)
2. **The Old Way:** realistic bad email example from Phase 5 (no template placeholders)
3. **The New Way: Intelligence-Driven GTM:** hard vs soft signals, PQS/PVP definitions
4. **Diamond separator**
5. **Company Overview:** company name, Core Problem, Target ICP, Buyer Persona, Key Differentiators (from Phase 1)
6. **Diamond separator**
7. **PQS Plays: Mirroring Exact Situations:** all PQS plays ranked by score. Section header: "These messages demonstrate such precise understanding of the prospect's current situation that they feel genuinely seen."
8. **Diamond separator**
9. **PVP Plays: Delivering Immediate Value:** all PVP plays ranked by score. Section header: "These messages provide actionable intelligence before asking for anything."
10. **Diamond separator**
11. **What Changes:** old way / new way / why this works triptych, ending with the "How to use the drafts" note
12. **Data Sources Reference:** table with Source, Key Fields, Used For

**Sections NOT to include:**
- EDP scoring tables (internal analysis only)
- Pain-based segment scoring tables (internal analysis only)
- Tool operationalization (internal only)
- Implementation / rollout plan (internal only)
- Quality checklist (internal only)
- Per-play scoring criteria tables (only the composite score in the header)
- Receipts worksheets (internal QA only; expressed inline as record IDs in the body plus the Data Sources table)
- Per-play "make it yours" or DRAFT labels (the human last-mile appears once in the closing note)

### 4. Quality checklist (internal, NOT in output)

Run the full checklist from `SKILL.md` before saving. If any check fails, fix before saving.

## References

- `templates/playbook-template.md`: master playbook format
- `templates/play-template.md`: play format, scoring, message rules

## Output

Save to: `playbooks/[company]-playbook.md` (in the working directory, NOT inside the skill folder).

This is the **final deliverable**. Optionally continue to Phase 7 (`phases/07-data-accessibility-eval.md`) to audit source accessibility before relying on the playbook.
