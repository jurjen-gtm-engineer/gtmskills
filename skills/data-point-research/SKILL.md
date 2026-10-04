---
name: data-point-research
description: Design custom data points that predict fit but can't be bought from standard providers
metadata:
  version: "1.0"
---

# Data Point Research

You are designing custom data points that predict customer fit, signals that can't be bought from standard data providers but can be researched or inferred.

## Core Concept

Build data you can't buy.

Standard data: Employee count, industry, funding stage
Custom data: "Has free trial option", "Support team > 20 people", "Uses competitor X"

## Input

User provides:
- Their ICP or target segment
- What their product does / pain it solves
- Optionally: existing customer patterns to analyze

## Process

1. **Identify Predictive Signals**

   **Prompt Pattern:**
   ```
   For a company selling [PRODUCT/SERVICE] to [ICP]:

   What specific, non-standard data points would strongly predict fit?

   Think about:
   - Website indicators (features, pages, content)
   - Hiring patterns (specific roles, urgency)
   - Tech stack combinations (not just "uses Salesforce")
   - Business model indicators (pricing model, customer type)
   - Operational signals (support structure, team ratios)
   ```

2. **Design Detection Methods**

   For each data point, define:
   - What to look for
   - Where to find it
   - How to validate it

3. **Output Format**

   ```
   ## Custom Data Points for [ICP/Product]

   ### High-Signal Data Points

   | Data Point | Why It Predicts Fit | Detection Method |
   |------------|---------------------|------------------|
   | [Point 1] | [Reason] | [How to find] |
   | [Point 2] | [Reason] | [How to find] |

   ### Detection Playbooks

   #### Data Point: [Name]

   **What to Look For:**
   - [Specific indicator 1]
   - [Specific indicator 2]

   **Where to Find It:**
   - [Source 1]: [What to check]
   - [Source 2]: [What to check]

   **Claygent/AI Prompt:**
   ```
   Visit [URL pattern].
   Look for [specific element].
   Return: [Yes/No/Value] based on [criteria].
   If not found, return "Not found".
   ```

   **Validation:**
   - Manual spot-check: [What to verify]
   - False positive risk: [High/Medium/Low]

   ### Scoring Model

   | Data Point | Weight | Reason |
   |------------|--------|--------|
   | [Point 1] | [+X] | [Why weighted this way] |
   | [Point 2] | [+X] | [Why weighted this way] |

   Total threshold for "High Fit": [Score]
   ```

## Examples

**Input:** "We sell AI customer service software. Best customers have high support volume and are PLG."

**Output:**
```
## Custom Data Points for AI Support Software

### High-Signal Data Points

| Data Point | Why It Predicts Fit | Detection Method |
|------------|---------------------|------------------|
| Has free trial/freemium | Indicates PLG model, high volume | Website pricing page |
| Support team size > 20 | High support volume | LinkedIn search, job postings |
| CS job postings | Active investment in support | Job board scraping |
| Login button on homepage | Has end-user product | Website scan |
| Multiple pricing tiers | PLG with expansion potential | Pricing page analysis |
| "Help center" or "Support" prominent | Support is key function | Website structure |

### Detection Playbooks

#### Data Point: Has Free Trial / PLG Model

**What to Look For:**
- "Free trial" or "Try free" CTA
- "Freemium" mentioned
- Self-serve signup flow
- Credit card not required messaging

**Where to Find It:**
- Homepage: CTAs and hero section
- Pricing page: Tier structure
- Sign-up flow: Self-serve vs "Contact sales" only

**Claygent/AI Prompt:**
```
Visit {{Company Website}}/pricing (or homepage if no pricing page).
Does this company offer a free trial or freemium tier?
Look for: "free trial", "try free", "freemium", "$0", "no credit card"
Return: "Yes - [type]" if found, "No - Sales-led only" if contact sales only, "Unknown" if unclear.
```

**Validation:**
- Manual spot-check: Visit 10 companies, verify accuracy
- False positive risk: Low (clear signals)

#### Data Point: Support Team Size > 20

**What to Look For:**
- Number of people with "Support", "Customer Success", "Help Desk" in title
- Support-related job postings volume

**Where to Find It:**
- LinkedIn: Company page → People → Filter by title keywords
- Job boards: Search "[Company] support" or "customer success"

**Claygent/AI Prompt:**
```
Search LinkedIn for [Company] employees with titles containing:
"Support", "Customer Success", "Help Desk", "Customer Service"
Return approximate count: "<10", "10-20", "20-50", "50+"
If unable to determine, return "Unknown".
```

**Validation:**
- Cross-reference with company size (ratio check)
- False positive risk: Medium (title variations)

### Scoring Model

| Data Point | Weight | Reason |
|------------|--------|--------|
| Free trial/PLG | +30 | Core ICP indicator |
| Support team 20+ | +25 | Volume signal |
| CS job postings | +20 | Active investment |
| Login on homepage | +15 | End-user product |
| Multiple pricing tiers | +10 | PLG indicator |

Total threshold for "High Fit": 60+
```

## Key Principles

1. **Specific > Generic**: "Has free trial" beats "is SaaS"

2. **Detectable > Theoretical**: If you can't find it reliably, it's not useful

3. **Predictive > Descriptive**: Focus on what correlates with becoming a customer

4. **Validated > Assumed**: Test with actual customer data

## Related Skills

- `/pain-qualified-segment` - Use data points to define segments
- `/company-goals` - Job postings as data source
- `/saas-identification` - One type of custom classification
- `/ideal-customer-profiles` - Connect data points to ICP

## Credits

"Build data you can't buy" is Petra Hajal's line and approach. The prompts and wording here are ours.

---

Examples are illustrative. Company names, prices and numbers in them are placeholders or may be out of date, so check the live source before you rely on any detail.
