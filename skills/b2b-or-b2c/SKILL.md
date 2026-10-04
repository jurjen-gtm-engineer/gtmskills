---
name: b2b-or-b2c
description: Classify whether a company's business model is B2B, B2C, or both
metadata:
  version: "1.0"
---

# B2B or B2C Classification

You are classifying a company's business model to enable appropriate messaging tone and angle.

## Input

User provides:
- Company name
- Company description or website content

## Process

1. **Analyze Business Model**

   **Prompt Pattern:**
   ```
   Based on this company description:
   [CONTENT]

   Classify this company as:
   - B2B (sells to businesses)
   - B2C (sells to consumers)
   - Both (hybrid model)

   Explain your reasoning based on:
   - Who pays for the product
   - How the product is sold (self-serve vs sales-led)
   - Typical customer type mentioned
   ```

2. **Output Format**

   ```
   Company: [Company Name]

   Classification: [B2B / B2C / Both]

   Evidence:
   - Customer type: [Businesses / Consumers / Both]
   - Sales motion: [Self-serve / Sales-led / Hybrid]
   - Pricing model: [Enterprise / Consumer / Both]
   - Language used: [Professional / Consumer / Mixed]

   Confidence: [High / Medium / Low]

   Messaging Implications:
   - Tone: [Formal/Professional vs Casual/Friendly]
   - Value prop focus: [ROI/Efficiency vs Experience/Convenience]
   - Decision process: [Committee/Multiple stakeholders vs Individual]
   - Proof points: [Case studies/ROI vs Reviews/Social proof]
   ```

## Examples

**Input:** Calendly description

**Output:**
```
Company: Calendly

Classification: B2B

Evidence:
- Customer type: Professionals and teams
- Sales motion: Product-led with enterprise sales
- Pricing model: Per-seat, team plans
- Language used: Professional ("scheduling for teams")

Confidence: High

Messaging Implications:
- Tone: Professional but approachable
- Value prop focus: Productivity, time savings, team coordination
- Decision process: Individual purchase or team decision
- Proof points: Productivity metrics, team adoption stories
```

**Input:** Red Bull description

**Output:**
```
Company: Red Bull

Classification: B2C

Evidence:
- Customer type: Individual consumers
- Sales motion: Retail distribution
- Pricing model: Consumer product pricing
- Language used: Energy, lifestyle, sports

Confidence: High

Messaging Implications:
- Tone: Energetic, lifestyle-focused
- Value prop focus: Experience, energy, performance
- Decision process: Individual impulse/preference
- Proof points: Brand recognition, athlete endorsements
```

## Related Skills

- `/company-mission` - What they do
- `/ideal-customer-profiles` - Who they serve
- `/saas-identification` - Software model classification

---

Examples are illustrative. Company names, prices and numbers in them are placeholders or may be out of date, so check the live source before you rely on any detail.
