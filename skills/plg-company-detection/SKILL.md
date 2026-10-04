---
name: plg-company-detection
description: AI prompt to detect PLG (product-led growth) companies from public sources (Petra Hajal)
metadata:
  version: "1.0"
---

# PLG Company Detection

You are using Petra Hajal's methodology for detecting Product-Led Growth (PLG) companies, a signal that can't be bought from standard data providers but predicts fit for many B2B solutions.

## Why This Matters

Build data you can't buy. (Idea credited to Petra Hajal.)

PLG status is a strong predictor for:
- High support/CS volume (self-serve = more users)
- Usage-based expansion opportunities
- Product analytics and activation tools
- Onboarding and in-app guidance solutions

Standard databases categorize by industry, not growth model. You have to detect it.

## Input

User provides:
- Company website URL
- Or: Company name for research
- Context on why PLG status matters for their use case

## Process

1. **Analyze Public Sources**

   **Sources to Check:**
   - Website homepage and pricing page
   - Sign-up flow (self-serve vs. contact sales)
   - Job postings (growth, PLG, product roles)
   - Funding announcements (PLG often mentioned)
   - Company blog/content

2. **Detection Prompt**

   **Claygent/AI Prompt:**
   ```
   Analyze {{Company Website}} to determine if this is a PLG (Product-Led Growth) company.

   Check for these PLG indicators:

   SIGN-UP FLOW:
   - Is there a "Free trial" or "Start free" button?
   - Can users sign up without talking to sales?
   - Is credit card required or "No credit card needed"?

   PRICING MODEL:
   - Is there a freemium tier ($0 or "Free forever")?
   - Is pricing transparent and public?
   - Are there usage-based or seat-based tiers?

   GROWTH SIGNALS:
   - Job postings for "Growth PM", "PLG", "Product-Led" roles?
   - Content about product-led growth on their blog?
   - Focus on activation, onboarding, or user experience?

   PRODUCT ACCESS:
   - Can you access the product immediately after signup?
   - Is there a product tour or interactive demo?
   - Self-serve upgrade path?

   Return:
   - PLG Status: Yes / No / Hybrid (PLG + Sales)
   - Model Type: Pure PLG / Freemium / Free Trial / Sales-Led
   - Key Evidence: [Top 3 signals observed]
   - Confidence: High / Medium / Low

   If insufficient data, return: "Unable to determine - [what's missing]"
   ```

3. **Output Format**

   ```
   ## PLG Analysis: [Company]

   ### PLG Status: [Yes/No/Hybrid]
   ### Model Type: [Pure PLG/Freemium/Free Trial/Sales-Led]

   ### Evidence

   | Signal | Finding | Source |
   |--------|---------|--------|
   | Sign-up flow | [Finding] | [URL] |
   | Pricing model | [Finding] | [URL] |
   | Growth signals | [Finding] | [Source] |
   | Product access | [Finding] | [Source] |

   ### Confidence Level: [High/Medium/Low]

   [Explanation of confidence]

   ### Implications

   If selling [X], PLG status suggests:
   - [Implication 1]
   - [Implication 2]
   ```

## Example

**Input:** "Check if Notion is a PLG company"

**Output:**
```
## PLG Analysis: Notion

### PLG Status: Yes
### Model Type: Freemium

### Evidence

| Signal | Finding | Source |
|--------|---------|--------|
| Sign-up flow | "Get Notion free" CTA, no sales required | notion.so homepage |
| Pricing model | Free tier for personal use, transparent pricing | notion.so/pricing |
| Growth signals | Multiple "Growth" roles, PLG-focused content | Notion careers, blog |
| Product access | Instant access after signup, product tour | Sign-up flow |

### Confidence Level: High

Clear PLG signals across all indicators. Notion is a canonical PLG company.

### Implications

If selling customer success tools, PLG status suggests:
- High volume of self-serve users (support scale challenge)
- Focus on activation and engagement metrics
- Likely interested in in-app messaging/onboarding
```

## PLG Indicators Cheat Sheet

**Strong PLG Signals:**
- "Start free" or "Try free" prominent CTA
- Public pricing page
- No credit card for trial
- Self-serve signup
- Product immediately accessible
- Freemium tier exists

**Hybrid (PLG + Sales) Signals:**
- Free trial AND "Talk to sales"
- Self-serve for SMB, sales for enterprise
- "Contact us" for custom pricing
- PLG for acquisition, sales for expansion

**Sales-Led Signals:**
- "Request demo" or "Contact sales" only
- No pricing page
- "Let's talk" instead of "Sign up"
- Calendar booking for product access

## Related Skills

- `/data-point-research` - Framework for custom signals
- `/product-complexity-detection` - Related PLG signal
- `/multi-product-detection` - Related signal
- `/company-goals` - Job posting analysis

## Credits

"Build data you can't buy" is Petra Hajal's line and approach. The prompts and wording here are ours.

---

Examples are illustrative. Company names, prices and numbers in them are placeholders or may be out of date, so check the live source before you rely on any detail.
