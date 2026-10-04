---
name: recent-news
description: Find and summarize recent news about a company for timely outreach
metadata:
  version: "1.0"
---

# Recent News Summarization

You are finding and summarizing recent news about a company to enable timely, relevant outreach.

## Input

User provides:
- Company name
- Optionally: time frame (default: last 3 months)
- Optionally: news type focus (funding, leadership, product, etc.)

## Process

1. **Search for News**

   **Search Pattern:**
   ```
   "[Company name]" + one of:
   - "funding" / "raises" / "Series"
   - "announces" / "launches"
   - "hires" / "appoints" / "new CEO"
   - "acquisition" / "acquires"
   - "partnership" / "partners with"
   ```

2. **Summarize Findings**

   **Prompt Pattern:**
   ```
   From these news results about [Company]:
   [CONTENT]

   Provide a 1-2 sentence summary of the most significant recent development.
   Focus on: funding, leadership changes, product launches, partnerships, or expansion.
   Note the date and source.
   ```

3. **Output Format**

   ```
   Company: [Company Name]

   Recent News Summary:
   [1-2 sentence summary of key development]

   Details:
   - Event: [What happened]
   - Date: [When]
   - Source: [Publication/URL]
   - Significance: [Why it matters]

   Outreach Angles:
   - Congratulatory: "Congrats on [news] - exciting times at [Company]..."
   - Relevance hook: "Given your recent [news], you might be thinking about..."
   - Timing angle: "With [news], now might be a good time to..."

   Trigger Classification:
   - [ ] Funding (growth mode, budget available)
   - [ ] Leadership change (new priorities, fresh perspective)
   - [ ] Product launch (innovation focus)
   - [ ] Partnership (integration opportunity)
   - [ ] Expansion (scaling challenges)
   ```

## Example

**Input:** Brightframe (fictional)

**Output:**
```
Company: Brightframe

Recent News Summary:
Brightframe launched a new AI design feature last month, adding automated brand kit generation to its Studio product.

Details:
- Event: AI feature launch (Studio expansion)
- Date: [month and year]
- Source: [publication and URL]
- Significance: Indicates continued AI investment and design automation focus

Outreach Angles:
- Congratulatory: "Congrats on the Studio expansion - the AI features look impressive..."
- Relevance hook: "Given your AI investments, you might be thinking about scaling your data infrastructure..."
- Timing angle: "With Studio growing, your engineering team is probably focused on..."

Trigger Classification:
- [x] Product launch (innovation focus)
```

## Related Skills

- `/company-goals` - Infer goals from job postings
- `/company-mission` - Understand their direction
- `/pain-qualified-segment` - Connect news to pain indicators

---

Examples are illustrative. Company names, prices and numbers in them are placeholders or may be out of date, so check the live source before you rely on any detail.
