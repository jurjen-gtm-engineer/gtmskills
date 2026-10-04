---
name: product-complexity-detection
description: AI prompt to detect product complexity from public sources (Petra Hajal)
metadata:
  version: "1.0"
---

# Product Complexity Detection

You are using Petra Hajal's methodology for detecting product complexity, a signal that can't be bought from standard data providers but predicts fit for certain solutions.

## Why This Matters

Build data you can't buy. (Idea credited to Petra Hajal.)

Product complexity is a strong predictor for:
- Need for customer success/support tools
- Onboarding and training solutions
- Documentation platforms
- Implementation services

Standard databases don't capture this. You have to detect it.

## Input

User provides:
- Company website URL
- Or: Company name for research
- Context on why complexity matters for their use case

## Process

1. **Analyze Public Sources**

   **Sources to Check:**
   - Product documentation (help center, docs site)
   - User reviews (G2, Capterra, TrustRadius)
   - Job postings (implementation, support, CS roles)
   - Pricing page (tiers, enterprise features)
   - Customer case studies (implementation mentions)

2. **Detection Prompt**

   **Claygent/AI Prompt:**
   ```
   Analyze {{Company Website}} and related public sources to assess product complexity.

   Check for these complexity indicators:

   DOCUMENTATION:
   - Does the product have extensive documentation? (Help center, docs site)
   - Are there video tutorials or training materials?
   - Is there a certification program?

   USER FEEDBACK:
   - Do G2/Capterra reviews mention "learning curve" or "implementation time"?
   - Are there complaints about complexity or praise for depth?

   SUPPORT STRUCTURE:
   - Are there implementation specialists or onboarding roles in job postings?
   - Is there a professional services offering?
   - Multiple support tiers (basic, premium, enterprise)?

   PRODUCT SIGNALS:
   - Multiple pricing tiers with feature gating?
   - API/integrations section prominent?
   - Enterprise or "Contact Sales" tier?

   Return:
   - Complexity Score: Low / Medium / High
   - Key Evidence: [Top 3 signals observed]
   - Confidence: High / Medium / Low

   If insufficient data, return: "Unable to determine - [what's missing]"
   ```

3. **Output Format**

   ```
   ## Product Complexity Analysis: [Company]

   ### Complexity Score: [Low/Medium/High]

   ### Evidence

   | Signal | Finding | Source |
   |--------|---------|--------|
   | Documentation depth | [Finding] | [URL/Source] |
   | User review themes | [Finding] | [G2/Capterra] |
   | Support structure | [Finding] | [Careers/Website] |
   | Product indicators | [Finding] | [Pricing/Features] |

   ### Confidence Level: [High/Medium/Low]

   [Explanation of confidence]

   ### Implications

   If selling [X], this complexity level suggests:
   - [Implication 1]
   - [Implication 2]
   ```

## Example

**Input:** "Check product complexity for Salesforce"

**Output:**
```
## Product Complexity Analysis: Salesforce

### Complexity Score: High

### Evidence

| Signal | Finding | Source |
|--------|---------|--------|
| Documentation depth | Extensive Trailhead learning platform with certifications | trailhead.salesforce.com |
| User review themes | "Steep learning curve" is a recurring theme in reviews | G2 reviews |
| Support structure | Multiple CS, Implementation, and Admin roles posted | LinkedIn |
| Product indicators | 4 product clouds, each with 3+ pricing tiers | salesforce.com/pricing |

### Confidence Level: High

Multiple strong signals across all categories. Salesforce is definitionally complex.

### Implications

If selling customer success tools, this complexity suggests:
- High need for onboarding/training solutions
- Likely existing budget for implementation support
- Pain around time-to-value for new users
```

## Complexity Indicators Cheat Sheet

**High Complexity:**
- Certification programs
- Professional services team
- Implementation timeline mentioned
- "Learning curve" in reviews
- Enterprise sales motion

**Medium Complexity:**
- Help center exists
- Onboarding emails/sequences
- Some training content
- Mixed review feedback
- Self-serve + sales-assist

**Low Complexity:**
- Minimal documentation
- No training needed
- "Easy to use" in reviews
- Pure self-serve
- Single pricing tier

## Related Skills

- `/data-point-research` - Framework for custom signals
- `/plg-company-detection` - Related complexity signal
- `/multi-product-detection` - Related complexity signal
- `/saas-identification` - Basic classification

## Credits

"Build data you can't buy" is Petra Hajal's line and approach. The prompts and wording here are ours.

---

Examples are illustrative. Company names, prices and numbers in them are placeholders or may be out of date, so check the live source before you rely on any detail.
