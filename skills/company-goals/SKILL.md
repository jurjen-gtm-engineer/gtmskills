---
name: company-goals
description: Infer company strategic goals from their job postings and hiring patterns
metadata:
  version: "1.0"
---

# Company Goals from Job Listings

You are inferring a company's strategic priorities from their current job postings.

## Input

User provides:
- Company name
- Optionally: careers page URL
- Optionally: specific job listing content

## Process

1. **Gather Job Data**

   **Search/Scrape Pattern:**
   ```
   Visit [Company] careers page or search "[Company] jobs"

   Count open positions by category:
   - Sales
   - Marketing
   - Engineering
   - Product
   - Customer Success
   - Operations
   - Data/Analytics
   ```

2. **Analyze Hiring Patterns**

   **Prompt Pattern:**
   ```
   Based on these job postings for [Company]:
   [JOB DATA]

   Infer the company's current strategic priorities:
   1. What functions are they investing in most?
   2. What does the hiring pattern suggest about their stage/focus?
   3. Are there any urgent signals ("urgently hiring", multiple similar roles)?
   4. What capabilities are they trying to build?
   ```

3. **Output Format**

   ```
   Company: [Company Name]

   Job Posting Analysis:
   | Category | Open Roles | % of Total |
   |----------|------------|------------|
   | [Category] | [Count] | [%] |

   Inferred Priorities:
   1. [Priority 1] - Evidence: [hiring pattern]
   2. [Priority 2] - Evidence: [hiring pattern]

   Strategic Signals:
   - Growth stage: [Early/Growth/Scale/Mature]
   - Primary focus: [Product/Sales/Operations]
   - Urgency indicators: [Yes/No - details]

   Outreach Angles:
   - "I see you're investing heavily in [function] - we help teams like yours..."
   - "With [X] open [role] positions, scaling [capability] seems to be a priority..."
   - "Your hiring for [roles] suggests you're focused on [goal]..."
   ```

## Example

**Input:** Company with 20 open roles

**Output:**
```
Company: TechCorp

Job Posting Analysis:
| Category | Open Roles | % of Total |
|----------|------------|------------|
| Sales | 8 | 40% |
| Engineering | 6 | 30% |
| Marketing | 3 | 15% |
| Customer Success | 2 | 10% |
| Operations | 1 | 5% |

Inferred Priorities:
1. Revenue expansion - Evidence: 40% of roles in sales, including 3 enterprise AEs
2. Product development - Evidence: Hiring senior engineers and a VP Engineering
3. Brand building - Evidence: New CMO and content marketing roles

Strategic Signals:
- Growth stage: Growth (post-Series B typical pattern)
- Primary focus: Sales-led growth with product investment
- Urgency indicators: Yes - "urgently hiring" on enterprise AE roles

Outreach Angles:
- "I see you're scaling your enterprise sales team - we help teams like yours..."
- "With 8 open sales roles, ramping new AEs quickly seems critical..."
- "Your VP Engineering search suggests you're building out the platform..."
```

## Related Skills

- `/recent-news` - Correlate hiring with news
- `/company-mission` - Understand strategic direction
- `/role-focus` - Understand specific role priorities

---

Examples are illustrative. Company names, prices and numbers in them are placeholders or may be out of date, so check the live source before you rely on any detail.
