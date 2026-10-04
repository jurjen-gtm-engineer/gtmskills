---
name: multi-product-detection
description: AI prompt to detect multi-product company structure from public sources (Petra Hajal)
metadata:
  version: "1.0"
---

# Multi-Product Detection

You are using Petra Hajal's methodology for detecting multi-product company structure, a signal that can't be bought from standard data providers but predicts fit for certain solutions.

## Why This Matters

Build data you can't buy. (Idea credited to Petra Hajal.)

Multi-product structure is a strong predictor for:
- Platform/integration complexity
- Cross-sell and upsell dynamics
- Need for unified analytics/reporting
- Product management tools
- Customer success complexity

Standard databases don't capture this. You have to detect it.

## Input

User provides:
- Company website URL
- Or: Company name for research
- Context on why multi-product matters for their use case

## Process

1. **Analyze Public Sources**

   **Sources to Check:**
   - Product/solutions pages
   - Pricing page structure
   - Navigation and site architecture
   - Blog/content for product announcements
   - Job postings (product team structure)

2. **Detection Prompt**

   **Claygent/AI Prompt:**
   ```
   Analyze {{Company Website}} to determine if this company has multiple products or a single product.

   Check for these multi-product indicators:

   PRODUCT PAGES:
   - Are there multiple distinct product pages?
   - Does the navigation show "Products" with dropdown?
   - Are products branded separately?

   PRICING STRUCTURE:
   - Separate pricing pages per product?
   - "Suite" or "Platform" pricing?
   - Bundle discounts mentioned?
   - "Add-on" products?

   NAMING/BRANDING:
   - Separate product names (e.g., "Company X" vs "Company Suite" vs "Company Analytics")?
   - Sub-brands or product lines?
   - "Platform" language suggesting multiple modules?

   ACQUISITION HISTORY:
   - Recent acquisitions integrated as products?
   - "Formerly [Company]" anywhere?

   Return:
   - Product Structure: Single / Multi-Product / Suite/Platform
   - Products Identified: [List if multiple]
   - Key Evidence: [Top 3 signals observed]
   - Confidence: High / Medium / Low

   If insufficient data, return: "Unable to determine - [what's missing]"
   ```

3. **Output Format**

   ```
   ## Multi-Product Analysis: [Company]

   ### Product Structure: [Single/Multi-Product/Suite]

   ### Products Identified

   | Product | Description | Standalone? |
   |---------|-------------|-------------|
   | [Product 1] | [Brief description] | [Yes/No] |
   | [Product 2] | [Brief description] | [Yes/No] |

   ### Evidence

   | Signal | Finding | Source |
   |--------|---------|--------|
   | Product pages | [Finding] | [URL] |
   | Pricing structure | [Finding] | [URL] |
   | Naming/branding | [Finding] | [Source] |

   ### Confidence Level: [High/Medium/Low]

   [Explanation of confidence]

   ### Implications

   If selling [X], multi-product structure suggests:
   - [Implication 1]
   - [Implication 2]
   ```

## Example

**Input:** "Check if HubSpot has multiple products"

**Output:**
```
## Multi-Product Analysis: HubSpot

### Product Structure: Multi-Product (Suite)

### Products Identified

| Product | Description | Standalone? |
|---------|-------------|-------------|
| Marketing Hub | Marketing automation | Yes |
| Sales Hub | CRM and sales tools | Yes |
| Service Hub | Customer service | Yes |
| CMS Hub | Website/content | Yes |
| Operations Hub | Data sync and automation | Yes |
| Commerce Hub | Payments and commerce | Yes |

### Evidence

| Signal | Finding | Source |
|--------|---------|--------|
| Product pages | Six distinct "Hub" products with separate pages | hubspot.com/products |
| Pricing structure | Each Hub priced separately, bundle discounts available | hubspot.com/pricing |
| Naming/branding | Consistent "[X] Hub" naming convention | Navigation |

### Confidence Level: High

Clear multi-product structure with distinct products and pricing.

### Implications

If selling integration/data tools, multi-product structure suggests:
- Data silos between Hubs
- Need for unified reporting across products
- Complex customer journey across products
```

## Multi-Product Indicators Cheat Sheet

**Multi-Product Signals:**
- "Products" dropdown in navigation
- Separate pricing pages
- Distinct product names
- "Add [Product]" or "Upgrade" CTAs
- Product-specific job postings

**Suite/Platform Signals:**
- "Platform" or "Suite" branding
- Bundle pricing prominent
- "All-in-one" messaging
- Unified dashboard mentioned
- Cross-product features highlighted

**Single Product Signals:**
- No "Products" section
- One pricing page with tiers
- Features, not products
- Single product name throughout

## Related Skills

- `/data-point-research` - Framework for custom signals
- `/product-complexity-detection` - Related signal
- `/plg-company-detection` - Related signal
- `/pricing-strategy` - Pricing page analysis

## Credits

"Build data you can't buy" is Petra Hajal's line and approach. The prompts and wording here are ours.

---

Examples are illustrative. Company names, prices and numbers in them are placeholders or may be out of date, so check the live source before you rely on any detail.
