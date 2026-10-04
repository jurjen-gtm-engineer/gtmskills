---
name: company-mission
description: Extract a company's mission statement from their LinkedIn or website
metadata:
  version: "1.0"
---

# Company Mission Extraction

You are extracting a company's mission statement from available sources.

## Input

User provides either:
- A company name
- A company LinkedIn URL
- A company website URL
- Company description text

## Process

1. **Identify Source**
   - If URL provided, note the source type
   - If just company name, suggest using LinkedIn Company page or About page

2. **Extract Mission**

   From the company's LinkedIn description or About page, generate a one-liner mission statement.

   **Prompt Pattern:**
   ```
   Based on this company description/about page:
   [CONTENT]

   What is this company's mission in one sentence?
   Focus on: who they serve, what problem they solve, what outcome they enable.
   ```

3. **Output Format**

   ```
   Company: [Company Name]
   Mission: [One sentence mission statement]
   Source: [Where extracted from]

   Example Usage:
   - Outreach personalization: "I see [Company]'s mission is to [mission]..."
   - ICP matching: Does this mission align with our target customers?
   ```

## Example

**Input:** Canva's LinkedIn description

**Output:**
```
Company: Canva
Mission: Canva's mission is to empower everyone to design anything and publish anywhere.
Source: LinkedIn Company Description

Example Usage:
- "I see Canva's mission is democratizing design - that resonates with our approach to..."
```

## Related Skills

- `/ideal-customer-profiles` - Who the company serves
- `/pricing-strategy` - How they monetize
- `/b2b-or-b2c` - Business model classification

---

Examples are illustrative. Company names, prices and numbers in them are placeholders or may be out of date, so check the live source before you rely on any detail.
