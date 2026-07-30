---
name: gtm-readiness-scan
description: Run the 24-question GTM Readiness Quick Scan as an interactive interview (or from a pre-filled answers file), score 8 domains 0-5, compute the GTM Readiness Index, determine the company archetype, and produce a report with the 3 weakest domains and a recommended focus.
---

# GTM Readiness Scan

A self-assessment of go-to-market maturity: 24 questions across 8 domains, each answered on a 0-5 maturity scale with six written anchors per question. Output is a scored report with an overall GTM Readiness Index, a company archetype, the 3 weakest domains, and a pointer to the stage folder in this repo where the matching skills live.

A hosted version with AI coaching lives at https://www.gtmscan.app. A deeper 120-question interview-led version (5 questions per subcategory, with evidence prompts and interview guidance) exists there as well. This skill is the free, self-run Quick Scan.

## Files in this skill

| File | Purpose |
|---|---|
| `SKILL.md` | This file: workflow, scoring math, archetype logic |
| `questionnaire.md` | The full 24 questions with all six answer anchors per question |
| `report-template.md` | The output report structure |

## Inputs

Two modes. Ask the user which one applies before doing anything else.

**Mode A: Interactive interview.** No inputs required. You ask the questions in conversation.

**Mode B: Pre-filled answers file.** The user provides a file with 24 scores. Accept any format you can parse unambiguously (markdown, YAML, CSV, plain list), as long as every answer maps to a question ID (Q1A through Q8C, or the full IDs Q1A.1 through Q8C.1) and an integer 0-5. Example:

```yaml
company: Example B.V.
profile:
  revenue: "3M"        # annual revenue, any currency
  employees: 25
  growth_rate: "80%"   # year over year
answers:
  Q1A: 3
  Q1B: 2
  Q1C: 1
  Q2A: 3
  Q2B: 2
  Q2C: 2
  Q3A: 2
  Q3B: 3
  Q3C: 1
  Q4A: 2
  Q4B: 2
  Q4C: 1
  Q5A: 3
  Q5B: 1
  Q5C: 2
  Q6A: 2
  Q6B: 1
  Q6C: 2
  Q7A: 2
  Q7B: 1
  Q7C: 2
  Q8A: 2
  Q8B: 2
  Q8C: 1
```

File-mode rules: never invent a missing score. If any of the 24 answers is missing, ambiguous, or outside 0-5, ask for it. Non-integer scores are not valid: each answer is one of the six anchors, not a blend. If the profile block is missing, ask the three profile questions from Step 1.

## Workflow

Run the steps in order. Do not skip the profile questions and do not compute anything until all 24 answers are in.

### Step 0: Setup

1. Ask: interview or answers file?
2. Ask for the company name (used in the report header).
3. State the ground rules to the user before the first question:
   - Score the organization as it is today, not where it plans to be.
   - When in doubt, score lower: optimism bias is the most common assessment error.
   - "We don't know" scores 0. Lack of visibility is itself a gap.
   - Time required for the interview: 20 to 30 minutes.

### Step 1: Profile (archetype inputs)

Ask three questions. These do not affect the scores; they determine the archetype in Step 4.

1. Annual revenue (any currency, rough band is fine)
2. Number of employees
3. Year-over-year growth rate

### Step 2: The 24 questions

Read `questionnaire.md` in this folder. For each of the 24 questions, in order (Domain 1 through Domain 8, subcategory A then B then C):

1. Present the question and all six answer anchors (0 through 5), verbatim from `questionnaire.md`.
2. Ask the user to pick the single anchor that best describes the organization today.
3. Record the integer score. If the user answers in prose instead of picking a number, map the prose to the closest anchor, state which anchor you picked and why, and let the user correct you.
4. One question at a time. Do not batch. Do not editorialize between questions beyond a one-line acknowledgment.

In file mode, skip the interview and validate the 24 scores instead.

### Step 3: Scoring math

Apply exactly this math, nothing else:

- **Subcategory score** = the single question score (integer 0-5). One question per subcategory, so no averaging at this level.
- **Domain score** = average of the 3 subcategory scores within the domain, reported to one decimal (0.0-5.0).
- **Overall GTM Readiness Index** = average of the 8 domain scores, reported to one decimal (0.0-5.0).

Note the index is the average of the 8 domain averages, not the average of the 24 raw scores. With 3 questions per domain these are numerically identical, but compute it as domains first so the report shows the same intermediate numbers the methodology defines.

Interpret each domain score with this table:

| Domain score | Interpretation | Recommendation |
|---|---|---|
| 0.0-1.0 | Critical gap: significant risk to GTM success | Immediate attention. Foundational work needed before scaling. |
| 1.1-2.0 | Early stage: some awareness, no systematic capability | Build the basics. Document, standardize, assign ownership. |
| 2.1-3.0 | Developing: foundations in place but inconsistent | Focus on consistency, documentation, cross-functional alignment. |
| 3.1-4.0 | Solid: defined capabilities with room for optimization | Shift from building to measuring and improving. |
| 4.1-5.0 | Advanced: mature, measured, continuously improving | Maintain and extend the advantage. Compound intelligence. |

Interpret the overall index with this table:

| Index | Readiness level | Implication |
|---|---|---|
| 0.0-1.5 | Not ready to scale | Fundamental capabilities missing. Scaling now burns cash without results. Focus on foundations. |
| 1.6-2.5 | Foundation building | Core elements emerging. Keep building before investing heavily in growth. Prioritize the lowest-scoring domains. |
| 2.6-3.5 | Ready for controlled growth | The GTM engine is functional. Growth is possible with careful management. Optimize weak domains while growing. |
| 3.6-4.5 | Scalable | Strong foundation supports confident scaling. Focus on efficiency, intelligence, compounding advantages. |
| 4.6-5.0 | Best-in-class | Mature, data-driven GTM engine. Focus on maintaining edge, innovation, new markets or segments. |

### Step 4: Archetype determination

Four archetypes, defined by company profile:

| Archetype | Revenue | Employees | Growth rate | One-line profile |
|---|---|---|---|---|
| Searching | 0-1M | 1-10 | 0-50% | Finding product-market fit. Founder does most selling, experimenting with positioning, validating willingness to pay. |
| Building | 1-5M | 10-50 | 50-100% | Creating repeatable process. Transitioning from founder-led to team-led selling, building playbooks, hiring first reps. |
| Scaling | 5-20M | 50-200 | 70-150% | Accelerating growth. Proven model ready for acceleration, building specialized teams, systems straining under volume. |
| Optimizing | 20M+ | 200+ | 30-70% | Market leadership. Established position, optimizing efficiency, building compounding growth loops, expanding into new segments. |

Determination logic, in priority order:

1. **Revenue decides.** If the revenue band clearly matches one archetype, that is the archetype.
2. **Employees break boundary cases.** If revenue sits on a boundary (or the user gave only a vague band), use employee count.
3. **Growth rate breaks remaining ties.** The growth bands overlap by design (Building and Scaling both include 70-100%), so growth rate is a tiebreaker only, never the primary signal.
4. **Still tied: pick the earlier archetype.** Same logic as scoring lower when in doubt. Running a later-stage playbook too early is the more expensive error.

Also flag a **stage mismatch** when the index and the archetype disagree by more than one readiness band. Examples: a Scaling-profile company (revenue 5-20M) with an index below 2.5 is scaling on an unready engine, that is the headline finding. A Searching-profile company with an index above 3.5 likely over-built infrastructure before validating the market.

Archetype context for the report (challenges and guidance per archetype):

- **Searching.** Common challenges: ICP clarity, first repeatable sale, message-market fit, pricing validation. Warning: do not over-invest in scaling infrastructure until you know what works. Message: build a strong foundation before scaling.
- **Building.** Common challenges: sales process documentation, pipeline predictability, first sales hires, quota setting. Warning: process debt is harder to fix than technical debt. Message: build systems before aggressive scaling.
- **Scaling.** Common challenges: team scaling, tech stack integration, demand generation at scale, maintaining win rates while growing. Warning: ignore infrastructure at your own peril. Message: strengthen the foundation during rapid expansion.
- **Optimizing.** Common challenges: RevOps maturity, growth compounding, market expansion, operational efficiency at scale. Warning: past success does not guarantee future growth. Message: reinvent to reignite growth.

Map the archetype to a growth stage and repo folder:

| Archetype | Growth stage | Repo folder |
|---|---|---|
| Searching | Product-Market Fit | `product-market-fit/` |
| Building | GTM Fit | `gtm-fit/` |
| Scaling | Growth & Moat | `growth-and-moat/` |
| Optimizing | Growth & Moat | `growth-and-moat/` |

### Step 5: Cross-domain patterns

Check the domain scores against these five patterns and report any that apply:

1. **Execution without foundation** (Domains 6-7 score higher than Domains 1-4): active team, not strategically grounded. Risk of wasted effort and inconsistent results.
2. **Strategy without execution** (Domains 1-4 score higher than Domains 5-8): good strategic thinking, poor operational capability. Invest in execution infrastructure.
3. **Tool-heavy, process-light** (Domain 5 high, Domain 7 low): over-investment in technology without the people and processes to use it.
4. **Person-dependent, system-weak** (Domain 7 high, Domain 8 low): strong individuals, weak systems. Growth constrained by key-person dependency.
5. **Outbound-dominant, inbound-absent** (6A high, 6C low): over-reliance on outbound creates fragility. Invest in demand generation for resilience.

For patterns 1, 2 and the sub-checks, "higher" means a gap of at least 1.0 between the group averages (or the two subcategory scores for pattern 5). Do not report a pattern on a gap smaller than that.

### Step 6: The report

Write the report to `gtm-readiness-report.md` in the user's working directory (ask before overwriting an existing file), following `report-template.md` in this folder exactly. Requirements:

- All 8 domain scores with their 3 subcategory scores visible.
- The 3 weakest domains ranked (lowest first; break ties by the lowest single subcategory score within the domain), each with its interpretation band and the specific subcategory dragging it down.
- Recommended focus: for each of the 3 weakest domains, one concrete next action derived from the anchor one level above the current score (the anchor text itself describes what the next maturity level looks like, so the gap between current and next anchor IS the action).
- The archetype section including stage mismatch flag if triggered.
- The pointer to the matching stage folder in this repo.
- The closing pointer to https://www.gtmscan.app for the hosted version with AI coaching and the 120-question Deep Scan.

After writing the file, give the user a 5-line summary in chat: index, readiness level, archetype, the 3 weakest domains, the recommended stage folder.

## Hard rules

- Never adjust, round up, or reinterpret a score the user gave. The user's anchor choice is final.
- Never present fewer than the six anchors. The anchors are the instrument; a bare "rate this 0-5" produces inflated scores.
- Scores are integers at question level. Averages at domain and index level are reported to one decimal.
- No em dashes or en dashes in the report output. Use commas, colons, parentheses.
- The report states facts from the scores. Do not pad it with generic GTM advice that is not anchored to a specific domain score.
