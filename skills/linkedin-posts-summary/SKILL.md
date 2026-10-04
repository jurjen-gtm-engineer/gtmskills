---
name: linkedin-posts-summary
description: Summarize a prospect's recent LinkedIn posts for personalized outreach
metadata:
  version: "1.0"
---

# LinkedIn Posts Summary

You are summarizing a prospect's recent LinkedIn posts to find personalization hooks for outreach.

## Input

User provides:
- Person's name and LinkedIn URL
- Or: pasted content from their recent posts
- Optionally: number of posts to analyze (default: 3-5)

## Process

1. **Gather Post Content**

   If URL provided, look for recent posts covering:
   - Thought leadership content
   - Industry commentary
   - Personal updates
   - Shared articles with commentary

2. **Summarize Each Post**

   **Prompt Pattern:**
   ```
   For each LinkedIn post from [Person]:
   [POST CONTENT]

   Extract:
   1. Main topic/theme
   2. Key point or opinion expressed
   3. Any quotable phrases
   4. Engagement level (if visible)
   ```

3. **Output Format**

   ```
   Person: [Name]
   LinkedIn: [URL]
   Posts Analyzed: [N]

   Post Summaries:

   Post 1: [Date if known]
   - Topic: [Main theme]
   - Key point: [Their opinion/insight]
   - Quotable: "[Direct quote if impactful]"

   Post 2: [Date if known]
   - Topic: [Main theme]
   - Key point: [Their opinion/insight]
   - Quotable: "[Direct quote if impactful]"

   Themes Across Posts:
   - [Theme 1]: Mentioned in [X] posts
   - [Theme 2]: Mentioned in [X] posts

   Personalization Hooks:
   - "I loved your post about [topic] - especially the point about [specific insight]..."
   - "Your take on [theme] resonated with me, particularly [quote]..."
   - "I've been following your thoughts on [topic] and wanted to share..."

   Tone/Style Notes:
   - Writing style: [Data-driven / Storytelling / Provocative / Educational]
   - Engagement approach: [Questions / Hot takes / How-tos / Personal stories]
   ```

## Example

**Input:** 3 posts from a VP of Sales

**Output:**
```
Person: Sarah Chen
LinkedIn: linkedin.com/in/example-profile
Posts Analyzed: 3

Post Summaries:

Post 1: January 15
- Topic: Remote sales team management
- Key point: Async video updates > daily standups for distributed teams
- Quotable: "The best sales teams I've seen don't need to be in the same room, they need to be on the same page."

Post 2: January 8
- Topic: AI in sales
- Key point: AI should augment reps, not replace human connection
- Quotable: "AI can write the email, but only humans can build the relationship."

Post 3: January 2
- Topic: 2026 sales predictions
- Key point: Personalization at scale will separate winners from losers
- Quotable: N/A

Themes Across Posts:
- Remote/distributed teams: 2 posts
- AI in sales: 2 posts
- Human connection: 2 posts

Personalization Hooks:
- "Your post about async video updates resonated, we've seen similar results with our customers..."
- "I loved your take on AI augmenting rather than replacing reps. That's exactly our philosophy..."
- "Your point about 'same page, not same room' is spot on..."

Tone/Style Notes:
- Writing style: Provocative with practical insights
- Engagement approach: Hot takes backed by experience
```

## Related Skills

- `/role-focus` - Understand their professional priorities
- `/recent-news` - Company context for their posts
- `/company-mission` - Connect their content to company direction

---

Examples are illustrative. Company names, prices and numbers in them are placeholders or may be out of date, so check the live source before you rely on any detail.
