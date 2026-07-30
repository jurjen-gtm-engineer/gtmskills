# Report Template: GTM Readiness Scan

Use this structure verbatim when producing `gtm-readiness-report.md`. Replace everything in `{curly braces}`. Omit nothing. No em dashes or en dashes anywhere in the output.

---

# GTM Readiness Report: {Company Name}

**Date:** {YYYY-MM-DD}
**Assessment:** GTM Readiness Quick Scan v1.0 (24 questions, 8 domains)
**Mode:** {Interactive interview | Answers file}
**Respondent:** {name or role, if given}

## 1. Headline

**GTM Readiness Index: {X.X} / 5.0 ({Readiness level})**

{Two or three sentences: the readiness level and its implication from the index interpretation table, the archetype, and the single most important finding. If a stage mismatch was flagged, it leads here.}

## 2. Scores

| # | Domain | Subcategory scores | Domain score | Interpretation |
|---|--------|--------------------|--------------|----------------|
| 1 | ICP & Market Definition | 1A: {n} / 1B: {n} / 1C: {n} | {X.X} | {band} |
| 2 | Sales Process & Qualification | 2A: {n} / 2B: {n} / 2C: {n} | {X.X} | {band} |
| 3 | Messaging & Positioning | 3A: {n} / 3B: {n} / 3C: {n} | {X.X} | {band} |
| 4 | Pipeline & Revenue Metrics | 4A: {n} / 4B: {n} / 4C: {n} | {X.X} | {band} |
| 5 | Tech Stack & RevOps | 5A: {n} / 5B: {n} / 5C: {n} | {X.X} | {band} |
| 6 | Outbound & Demand Generation | 6A: {n} / 6B: {n} / 6C: {n} | {X.X} | {band} |
| 7 | Sales Enablement & Team | 7A: {n} / 7B: {n} / 7C: {n} | {X.X} | {band} |
| 8 | Growth Engine & Scalability | 8A: {n} / 8B: {n} / 8C: {n} | {X.X} | {band} |

**Overall GTM Readiness Index: {X.X} (average of the 8 domain scores)**

## 3. Company archetype

**Archetype: {Searching | Building | Scaling | Optimizing}**

| Input | Value | Band matched |
|---|---|---|
| Revenue | {value} | {archetype band} |
| Employees | {value} | {archetype band} |
| Growth rate | {value} | {archetype band} |

{One paragraph: the archetype's one-line profile, its common challenges, and its warning and message, from SKILL.md Step 4.}

{If a stage mismatch was flagged: one paragraph naming the mismatch (index band vs archetype expectation) and what it means. Otherwise write: "No stage mismatch: the readiness index is consistent with the archetype."}

## 4. The 3 weakest domains

Ranked lowest first. Ties broken by the lowest single subcategory score.

### 4.1 {Domain name}: {X.X} ({band})

- **Weakest subcategory:** {ID and name}, scored {n}: "{short quote or paraphrase of the anchor the user selected}"
- **What the next level looks like:** {paraphrase of the anchor one level above the current score}
- **Recommended action:** {one concrete action that closes exactly that gap, derived from the difference between the current anchor and the next one}

### 4.2 {Domain name}: {X.X} ({band})

{same structure}

### 4.3 {Domain name}: {X.X} ({band})

{same structure}

## 5. Cross-domain patterns

{List each triggered pattern from SKILL.md Step 5 with the numbers that triggered it, e.g. "Strategy without execution: Domains 1-4 average 3.2 vs Domains 5-8 average 1.9 (gap 1.3)." If none triggered, write: "No cross-domain patterns triggered (all group gaps below 1.0)."}

## 6. Recommended focus

{One paragraph tying it together: given the archetype, the index, and the 3 weakest domains, what is the single focus for the next quarter. Anchored to scores, not generic advice.}

**Your stage:** {Product-Market Fit | GTM Fit | Growth & Moat}

Start with the skills in this repo's matching stage folder:

- Searching: [`product-market-fit/`](../../product-market-fit)
- Building: [`gtm-fit/`](../../gtm-fit)
- Scaling or Optimizing: [`growth-and-moat/`](../../growth-and-moat)

{Keep only the line matching the determined archetype; delete the other two.}

## 7. Next step

This Quick Scan is directional: one question per subcategory. The hosted version at https://www.gtmscan.app adds AI coaching, and the GTM Readiness Deep Scan there runs 120 questions (5 per subcategory) with evidence prompts and interview guidance for a comprehensive evaluation.

---

*Scored on the 0-5 maturity scale: 0 non-existent, 1 ad-hoc, 2 developing, 3 defined, 4 managed, 5 optimized. Scores reflect current state as reported by the respondent, not verified evidence.*

---

## Deep Scan sections (only when the Deep Scan tier ran)

### Subcategory heatmap

All 24 subcategory scores in one table so the spread inside each domain is visible.

| Domain | A | B | C |
|---|---|---|---|
| 1. ICP & Market Definition | {0.0} | {0.0} | {0.0} |
| 2. Sales Process & Qualification | {0.0} | {0.0} | {0.0} |
| 3. Messaging & Positioning | {0.0} | {0.0} | {0.0} |
| 4. Pipeline & Revenue Metrics | {0.0} | {0.0} | {0.0} |
| 5. Tech Stack & RevOps | {0.0} | {0.0} | {0.0} |
| 6. Outbound & Demand Generation | {0.0} | {0.0} | {0.0} |
| 7. Sales Enablement & Team | {0.0} | {0.0} | {0.0} |
| 8. Growth Engine & Scalability | {0.0} | {0.0} | {0.0} |

### Disagreement log

Every question where participants disagreed by 2 or more points. Disagreement is a finding: it means the organization does not share one picture of reality.

| Question | Positions | Settled score | Note |
|---|---|---|---|
| {Q2B.3} | {VP Sales: 4, RevOps: 1} | {2} | {why} |

### Evidence appendix

Per domain, the evidence and rationale captured per question. A scored answer with no evidence behind it is flagged: the score rests on opinion.

#### Domain {n}: {name}

- {Q1A.1}: score {n}. Evidence: {document, dashboard, example, or "none provided (flagged)"}
