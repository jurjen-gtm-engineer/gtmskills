---
name: saas-identification
description: Determine if a company is a SaaS business based on their description
metadata:
  version: "1.0"
---

# SaaS Identification

You are determining whether a company operates a SaaS (Software as a Service) business model.

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

   Determine if this is a SaaS company by checking for:
   1. Software product (not physical goods)
   2. Subscription/recurring revenue model
   3. Cloud-hosted/web-based delivery
   4. Self-service or sales-led software

   Return: Yes (SaaS), No (Not SaaS), or Partial (SaaS component)
   ```

2. **Output Format**

   ```
   Company: [Company Name]

   SaaS Classification: [Yes / No / Partial]

   Evidence:
   - Product type: [Software / Hardware / Service / Hybrid]
   - Revenue model: [Subscription / One-time / Usage / Mixed]
   - Delivery: [Cloud / On-premise / Both]
   - Customer interaction: [Self-serve / Sales-led / Both]

   If SaaS:
   - SaaS Category: [Vertical / Horizontal]
   - Primary function: [CRM / Marketing / DevOps / etc.]

   If Not SaaS:
   - Business type: [E-commerce / Services / Manufacturing / etc.]

   Messaging Implications:
   - [How to adjust outreach based on classification]
   ```

## Examples

**Input:** Canva description

**Output:**
```
Company: Canva

SaaS Classification: Yes

Evidence:
- Product type: Software (design platform)
- Revenue model: Subscription (monthly/annual plans)
- Delivery: Cloud (web-based, browser access)
- Customer interaction: Self-serve with team sales

If SaaS:
- SaaS Category: Horizontal (cross-industry)
- Primary function: Design / Creative

Messaging Implications:
- Reference SaaS-specific metrics (MRR, churn, expansion)
- Discuss scaling challenges familiar to SaaS
- "As a fellow SaaS company, you know the importance of..."
```

**Input:** Red Bull description

**Output:**
```
Company: Red Bull

SaaS Classification: No

Evidence:
- Product type: Physical goods (beverages)
- Revenue model: Product sales
- Delivery: Retail distribution
- Customer interaction: B2C retail

If Not SaaS:
- Business type: Consumer goods / Beverages

Messaging Implications:
- Don't use SaaS-specific language
- Focus on distribution, retail, brand metrics
- Different buying process and stakeholders
```

**Input:** Shopify description

**Output:**
```
Company: Shopify

SaaS Classification: Yes

Evidence:
- Product type: Software (e-commerce platform)
- Revenue model: Subscription + transaction fees
- Delivery: Cloud (web-based)
- Customer interaction: Self-serve with enterprise sales

If SaaS:
- SaaS Category: Vertical (e-commerce focused)
- Primary function: E-commerce / Retail enablement

Messaging Implications:
- Reference e-commerce SaaS metrics
- Understand merchant-focused priorities
- "Supporting merchants at scale is complex..."
```

## Related Skills

- `/b2b-or-b2c` - Business model classification
- `/pricing-strategy` - How they charge
- `/company-mission` - What they do

---

Examples are illustrative. Company names, prices and numbers in them are placeholders or may be out of date, so check the live source before you rely on any detail.
