# Phase 2: EDP Analysis

## Purpose

Identify Existential Data Points using the EDP Analysis Framework. This is Phase 2 of the Cannonball GTM Playbook Generator.

## Inputs

- **Phase 1 context** (in-context from the previous phase)

## Process

### 1. Load Phase 1 research

Use the company research context from Phase 1. Extract the ICP, persona, and situational triggers.

### 2. Execute the EDP Analysis Framework (VERBATIM)

Execute the prompt in `prompts/edp-analysis-framework.md` **exactly as written**. Do not paraphrase it.

When executing:
- Replace `[INSERT CATEGORY]` with the company's product category from Phase 1
- Replace `[INSERT CATEGORY NAME]` with the same
- Replace `[PASTE YOUR RESEARCH FINDINGS HERE]` with the full Phase 1 research output
- Replace `[ADD ANY OTHER RELEVANT INFORMATION]` with any additional context provided

### 3. Classify EDPs: Data Key vs Enrichment

For each EDP, classify its role:

| EDP | Classification | Rationale |
|-----|---------------|-----------|
| ... | **Data Key**: defines a segment boundary, makes a hidden pain findable at scale | ... |
| ... | **Enrichment**: enhances messaging but does not define the segment | ... |

**Data Key criteria:** does this EDP create a boundary condition that separates one segment from another? Can it find companies competitors literally cannot see? If yes, it is a Data Key. If it only makes existing targeting more specific, it is Enrichment.

**Stacking check:** can multiple Data Keys point at the same segment (Venn-diagram targeting)? Flag segments where 2-3 Data Keys overlap; these will produce the strongest plays in Phase 5.

### 4. Score wedges (E/T/D)

For each EDP identified, apply wedge scoring:

| Wedge | E (Existentiality, 1-10) | T (Timing, 1-10) | D (Data Availability, 1-10) | Total |
|-------|--------------------------|-------------------|----------------------------|-------|

### 5. Stress-test each EDP

For every candidate EDP, ask:
- Does it create genuine urgency?
- Is it behavioral, not demographic?
- Can it be observed from public data?

An EDP failing any of the three is demoted to Enrichment or dropped.

## References

- `prompts/edp-analysis-framework.md`: **exact prompt, execute verbatim**
- `knowledge/methodology.md`: core methodology

## Output

**In-context only. Do NOT save to file.** This analysis informs play generation but is NOT included in the final playbook output.

Include:
- 3-5 scored EDPs with Urgency / Universality / Measurability / Actionability / Defensibility ratings
- **Data Key vs Enrichment classification** for each EDP
- **Data Key stacking opportunities:** which segments have 2-3 overlapping Data Keys
- E/T/D wedge scoring table
- Primary EDP recommendation with comprehensive justification
- 4-6 pain-based segments with TAM estimates, pain intensity, conversion rate potential, ACV range, sales efficiency factor, ARR estimate, and overall segment score
- Strategic recommendations (segment prioritization, PVP ideas, messaging themes, data collection strategies)
