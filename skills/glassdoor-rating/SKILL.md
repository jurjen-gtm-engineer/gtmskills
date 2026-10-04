---
name: glassdoor-rating
description: Find and interpret a company's Glassdoor rating for culture insights
metadata:
  version: "1.0"
---

# Glassdoor Rating Analysis

You are finding and interpreting a company's Glassdoor rating to understand employee sentiment and company culture.

## Input

User provides:
- Company name
- Optionally: specific aspects to focus on (culture, leadership, compensation)

## Process

1. **Find Glassdoor Data**

   **Search Pattern:**
   ```
   Search: "[Company name] Glassdoor rating"
   or: "[Company name] Glassdoor reviews"

   Extract:
   - Overall rating (X.X/5)
   - Number of reviews
   - Key themes from reviews
   ```

2. **Analyze Rating**

   **Prompt Pattern:**
   ```
   Based on Glassdoor information for [Company]:
   [CONTENT]

   Extract:
   1. Overall rating
   2. CEO approval (if available)
   3. Common positive themes
   4. Common concerns/negatives
   5. Recent trend (improving/declining)
   ```

3. **Output Format**

   ```
   Company: [Company Name]

   Glassdoor Overview:
   - Rating: [X.X]/5
   - Reviews: [Number]
   - CEO Approval: [X%] (if available)
   - Recommend to Friend: [X%] (if available)

   Sentiment Analysis:
   - Overall: [Positive / Mixed / Negative]
   - Trend: [Improving / Stable / Declining]

   Common Themes:
   Positives:
   - [Theme 1]
   - [Theme 2]

   Concerns:
   - [Theme 1]
   - [Theme 2]

   Outreach Applications:
   - Positive (4.0+): "I saw you're rated highly on Glassdoor for culture - speaks to leadership..."
   - Mixed (3.0-3.9): Use cautiously, focus on other angles
   - Low (<3.0): Avoid referencing; may indicate internal challenges

   Caution: Glassdoor data should complement, not drive, outreach strategy.
   ```

## Examples

**Input:** Company with 4.2 rating

**Output:**
```
Company: TechCorp

Glassdoor Overview:
- Rating: 4.2/5
- Reviews: 847
- CEO Approval: 89%
- Recommend to Friend: 85%

Sentiment Analysis:
- Overall: Positive
- Trend: Stable (similar to last year)

Common Themes:
Positives:
- Great work-life balance
- Strong engineering culture
- Competitive compensation

Concerns:
- Fast pace can be stressful
- Rapid growth means some process gaps
- Limited career paths in some teams

Outreach Applications:
- "I noticed you're consistently rated highly for engineering culture on Glassdoor..."
- "Companies that prioritize work-life balance like yours tend to..."
- Safe to reference; indicates healthy culture

Caution: Focus on professional context, not as primary personalization.
```

**Input:** Company with 2.8 rating

**Output:**
```
Company: StruggleCorp

Glassdoor Overview:
- Rating: 2.8/5
- Reviews: 234
- CEO Approval: 45%
- Recommend to Friend: 38%

Sentiment Analysis:
- Overall: Negative
- Trend: Declining (down from 3.2 last year)

Common Themes:
Positives:
- Good product and mission
- Some strong teams

Concerns:
- Leadership turnover
- Unclear direction
- Compensation below market

Outreach Applications:
- DO NOT reference Glassdoor directly
- May indicate internal challenges; be sensitive
- Focus on product/mission strengths instead
- Could be opportunity: "Companies going through change often need..."

Caution: Low rating may signal instability; adjust expectations accordingly.
```

## Ethical Considerations

- Use Glassdoor data tactfully
- Don't mention low ratings directly to prospects
- Focus on genuine connection, not manipulation
- Glassdoor is one data point, not the full picture

## Related Skills

- `/recent-news` - Correlate with company news
- `/company-goals` - Hiring patterns may explain culture
- `/company-mission` - Understand their direction

---

Examples are illustrative. Company names, prices and numbers in them are placeholders or may be out of date, so check the live source before you rely on any detail.
