---
name: playbook-pitch-generation
description: Generate company-specific pitch ideas and playbooks per account using AI (Patrick Spychalski)
metadata:
  version: "1.0"
---

# Playbook Pitch Generation

You are applying Patrick Spychalski's methodology for generating company-specific pitch ideas and playbooks, using AI to create tailored approaches for each account based on enriched data.

## Core Concept

Generate 'playbook' pitch ideas per account... Auto-generate company-specific slide decks with OpenAI. (Idea credited to Patrick Spychalski.)

Instead of generic pitches, generate:
- Account-specific angles
- Relevant proof points
- Customized value propositions
- Tailored objection handling

## Input

User provides:
- Company data (enriched fields)
- Your product/service value propositions
- Relevant case studies or proof points
- Optionally: ICP score and signals

## Process

1. **Analyze Account Context**

   **Prompt Pattern:**
   ```
   For this company: {{company_name}}

   Available data:
   - Industry: {{industry}}
   - Size: {{employees}}
   - Tech stack: {{tech_stack}}
   - Recent news: {{news}}
   - Job postings: {{jobs}}
   - ICP signals: {{signals}}

   Identify:
   - Primary business challenge based on data
   - Most relevant use case for our solution
   - Potential objections given their context
   - Best proof point to reference
   ```

2. **Generate Pitch Playbook**

   **Claygent Prompt:**
   ```
   Based on this company data:
   - Company: {{company_name}}
   - Industry: {{industry}}
   - Size: {{employees}}
   - Tech stack: {{tech_stack}}
   - Recent signals: {{signals}}

   And these value propositions:
   [LIST YOUR VALUE PROPS]

   Generate a pitch playbook:

   1. LEAD ANGLE: Which value prop is most relevant and why?

   2. HOOK: One sentence that connects their situation to our solution

   3. PROOF POINT: Which case study or metric to lead with?

   4. LIKELY OBJECTION: What will they push back on?

   5. OBJECTION RESPONSE: How to address it?

   6. CALL TO ACTION: What's the appropriate next step?

   Format as JSON:
   {
     "lead_angle": "",
     "hook": "",
     "proof_point": "",
     "likely_objection": "",
     "objection_response": "",
     "cta": ""
   }
   ```

3. **Output Format**

   ```
   ## Pitch Playbook: [Company Name]

   ### Account Context

   | Factor | Value | Implication |
   |--------|-------|-------------|
   | Industry | [X] | [What this means] |
   | Size | [X] | [What this means] |
   | Tech stack | [X] | [What this means] |
   | Key signal | [X] | [What this means] |

   ### Recommended Approach

   **Lead Angle:** [Value prop to lead with]

   **Why This Angle:** [Connection to their context]

   ### The Pitch

   **Hook:** "[One sentence opener]"

   **Proof Point:** [Case study or metric]
   - "[Specific quote or number]"

   **Value Statement:** [How we help given their context]

   ### Objection Handling

   **Likely Objection:** "[Expected pushback]"

   **Response:** "[How to address]"

   ### Call to Action

   [Appropriate next step given their stage]

   ### Supporting Materials

   - Slide deck focus: [Key slides to emphasize]
   - Case study: [Most relevant]
   - Demo focus: [Features to highlight]
   ```

## Example

**Input:**
- Company: Acme SaaS (500 employees, Series C, uses Salesforce, hiring 10 AEs)
- Our product: Sales enablement platform
- Value props: 1) Faster rep ramp, 2) Higher win rates, 3) Content findability

**Output:**
```
## Pitch Playbook: Acme SaaS

### Account Context

| Factor | Value | Implication |
|--------|-------|-------------|
| Size | 500 employees | Mid-market, likely has process gaps |
| Funding | Series C | Pressure to scale efficiently |
| Tech | Salesforce | Integration is easy |
| Signal | Hiring 10 AEs | Ramping is top priority |

### Recommended Approach

**Lead Angle:** Faster rep ramp

**Why This Angle:** With 10 AEs being hired, their #1 pain is getting new reps productive. Win rates and content are secondary until ramp is solved.

### The Pitch

**Hook:** "With 10 AEs starting, you're probably spending more time onboarding than selling, we helped [Similar Company] cut ramp time from 6 months to 8 weeks."

**Proof Point:** TechCorp case study
- "New AEs hit quota in month 2 instead of month 5"
- "VP Sales said 'This paid for itself with the first cohort'"

**Value Statement:** We turn tribal knowledge into a repeatable playbook so new reps learn from your best performers, not just their manager.

### Objection Handling

**Likely Objection:** "We already have a shared drive with sales content"

**Response:** "That's actually the #1 thing we hear. The issue isn't having content, it's that reps can't find the right content in the moment. Our customers saw reps spending 30% less time searching after switching."

### Call to Action

"Want to see how [Similar Company] structured their onboarding? I can walk through their playbook in 15 minutes."

### Supporting Materials

- Slide deck focus: Ramp time ROI calculator, TechCorp case study
- Case study: TechCorp (similar size, similar hiring velocity)
- Demo focus: Playbook builder, content search, manager dashboard
```

## Scaling Playbook Generation

For bulk account preparation:
```
For each account in this list, generate a pitch playbook.

Use these value props: [PROPS]
Use these case studies: [STUDIES]

Match the best angle based on:
- Industry → relevant case study
- Size → appropriate metrics
- Signals → primary pain point

Output as CSV: company, lead_angle, hook, proof_point, cta
```

## Key Principles

1. **Context-Driven**: Pitch changes based on their situation
2. **Signal-Based**: Let data pick the angle
3. **Proof-First**: Lead with evidence, not claims
4. **Objection-Ready**: Anticipate pushback

## Related Skills

- `/icp-scoring-dynamic` - Score drives playbook priority
- `/customer-evidence-first` - Source for proof points
- `/list-is-the-message` - Segment-level messaging
- `/role-focus` - Persona-specific angles

## Credits

The per-account playbook pitch idea follows Patrick Spychalski ([The Kiln](https://thekiln.com)). The prompts and wording here are ours.

---

Examples are illustrative. Company names, prices and numbers in them are placeholders or may be out of date, so check the live source before you rely on any detail.
