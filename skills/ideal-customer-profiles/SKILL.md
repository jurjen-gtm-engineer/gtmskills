---
name: ideal-customer-profiles
description: Identify who a company serves based on their description and content
metadata:
  version: "1.0"
---

# Ideal Customer Profile Extraction

You are identifying a company's ideal customer profiles (ICPs) from their public content.

## Input

User provides either:
- A company name
- Company description/about text
- Company website URL

## Process

1. **Analyze Content**

   From the company's description, identify:
   - Job titles they mention as customers
   - Industries they serve
   - Company sizes they target
   - Use cases they highlight

2. **Extract ICPs**

   **Prompt Pattern:**
   ```
   Based on this company description:
   [CONTENT]

   List the typical customer job titles or types this company serves.
   Include:
   - Primary buyer personas (who makes the purchase decision)
   - End users (who uses the product daily)
   - Industries/verticals mentioned
   ```

3. **Output Format**

   ```
   Company: [Company Name]

   Primary Buyers:
   - [Job title 1]
   - [Job title 2]

   End Users:
   - [Job title/type 1]
   - [Job title/type 2]

   Industries Served:
   - [Industry 1]
   - [Industry 2]

   Outreach Application:
   - If prospect matches these personas → higher relevance signal
   - Personalization angle: "You serve [similar persona] - we help companies like yours..."
   ```

## Example

**Input:** Canva's description

**Output:**
```
Company: Canva

Primary Buyers:
- Marketing Directors
- Creative Directors
- Brand Managers

End Users:
- Graphic designers
- Social media managers
- Content creators
- Non-designers who need to create visuals

Industries Served:
- Marketing/Advertising
- Education
- Small businesses
- Enterprise marketing teams

Outreach Application:
- "I see you cater to marketing teams and content creators - we help similar companies..."
```

## Related Skills

- `/company-mission` - What problem they solve
- `/b2b-or-b2c` - Business model type
- `/pain-qualified-segment` - Tension indicators for targeting

---

Examples are illustrative. Company names, prices and numbers in them are placeholders or may be out of date, so check the live source before you rely on any detail.
