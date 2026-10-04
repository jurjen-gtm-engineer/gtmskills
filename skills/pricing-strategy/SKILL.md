---
name: pricing-strategy
description: Infer a company's pricing model from their website or public information
metadata:
  version: "1.0"
---

# Pricing Strategy Analysis

You are analyzing a company's pricing strategy from their public pricing page or descriptions.

## Input

User provides either:
- Company name (will search for pricing)
- Pricing page URL
- Pricing page content

## Process

1. **Search for Pricing**

   If only company name provided:
   ```
   Search: "[Company] pricing"
   Look for: pricing page, plans, packages
   ```

2. **Extract Pricing Model**

   **Prompt Pattern:**
   ```
   From this pricing page/information:
   [CONTENT]

   Extract:
   1. Pricing model type (per seat, usage-based, flat rate, freemium, etc.)
   2. Price tiers and their names
   3. Starting price point
   4. Enterprise/custom pricing availability
   5. Free tier details (if any)
   ```

3. **Output Format**

   ```
   Company: [Company Name]

   Pricing Model: [Type]

   Tiers:
   | Tier | Price | Key Features |
   |------|-------|--------------|
   | [Name] | [Price] | [Features] |

   Free Tier: [Yes/No - details]
   Enterprise: [Available/Contact sales]

   Strategic Insights:
   - Market positioning: [Premium/Mid-market/SMB]
   - Sales motion: [Self-serve/Sales-assisted/Enterprise]
   - Competitive angle: [How this compares to market]
   ```

## Example

**Input:** Calendly pricing

**Output:**
```
Company: Calendly

Pricing Model: Freemium with per-seat pricing

Tiers:
| Tier | Price | Key Features |
|------|-------|--------------|
| Free | $0 | 1 calendar, basic scheduling |
| Standard | $10/seat/mo | Unlimited calendars, integrations |
| Teams | $16/seat/mo | Round robin, team pages |
| Enterprise | Custom | SSO, advanced admin |

Free Tier: Yes - limited to 1 event type, 1 calendar
Enterprise: Available - contact sales

Strategic Insights:
- Market positioning: Mid-market with SMB entry point
- Sales motion: Product-led with sales assist for enterprise
- Competitive angle: Strong free tier for adoption, upsell on team features
```

## Outreach Application

Use pricing insights to:
- Match prospect's likely budget/tier
- Reference their pricing model in personalization
- Understand their go-to-market motion

## Related Skills

- `/company-mission` - What they do
- `/saas-identification` - Is it SaaS?
- `/b2b-or-b2c` - Who they sell to

---

Examples are illustrative. Company names, prices and numbers in them are placeholders or may be out of date, so check the live source before you rely on any detail.
