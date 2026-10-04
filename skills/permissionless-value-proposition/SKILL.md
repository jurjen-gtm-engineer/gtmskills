---
name: permissionless-value-proposition
description: Create independently valuable outreach by combining public data for actionable insights (Jordan Crawford)
metadata:
  version: "1.0"
---

# Permissionless Value Proposition (PVP)

You are creating Permissionless Value Propositions, outreach that delivers genuine value from public data BEFORE asking for anything in return.

## Core Concept

Create independently valuable outreach by combining public data for actionable insights.

Traditional outreach: "Hi, we sell X. Want to buy?"
PVP outreach: "I noticed [insight from public data]. This usually means [actionable implication]. If useful, happy to share more..."

The value is delivered without permission. The prospect benefits even if they never respond.

## Input

User provides:
- Target prospect or segment
- Public data available about them
- Your solution's domain

## Process

1. **Identify Public Data Sources**

   **Prompt Pattern:**
   ```
   For this prospect/segment: [DESCRIPTION]

   What public data is available that others aren't combining?

   Sources to consider:
   - Company website (pricing, features, job postings)
   - LinkedIn (team structure, hires, posts)
   - News (funding, launches, partnerships)
   - Regulatory/government filings
   - Industry databases
   - Review sites (G2, Glassdoor)
   - Social media
   - Job boards
   ```

2. **Create the Insight Combination**

   ```
   Take these data points: [DATA POINTS]

   Combine them into an insight that:
   - The prospect might not know themselves
   - Has actionable implications
   - Relates to a problem your solution addresses
   - Demonstrates genuine understanding of their situation

   Formula: [Data A] + [Data B] = [Non-obvious insight]
   ```

3. **Craft the PVP**

   ```
   Structure the outreach to lead with value:

   1. The observation (what you noticed)
   2. The implication (what it usually means)
   3. The value (insight or resource offered)
   4. The soft ask (only if interested)

   The prospect should benefit from reading this even if they never reply.
   ```

4. **Output Format**

   ```
   ## PVP: [Insight Name]

   ### The Data Combination

   **Public Data Used:**
   - [Data point 1] from [Source]
   - [Data point 2] from [Source]
   - [Data point 3] from [Source]

   **The Insight:**
   [Data 1] + [Data 2] = [Non-obvious conclusion]

   ### The PVP Message

   Subject: [Value-focused subject]

   "[Observation about their situation].

   This usually means [implication]. [Companies in similar situations / Our research shows] [actionable insight].

   [Optional: specific resource or finding to share]

   [Soft ask only if relevant]"

   ### Why This Is Permissionless

   - Value delivered: [What they get]
   - No ask required: [They benefit regardless of response]
   - Demonstrates: [What this shows about you]

   ### Scaling This PVP

   **Data needed:** [What to collect]
   **Detection method:** [How to find qualifying prospects]
   **Volume potential:** [How many prospects fit this pattern]
   ```

## Example

**Input:** "We help companies optimize cloud costs. Looking at SaaS companies with recent funding."

**Output:**
```
## PVP: Post-Funding Cloud Spend

### The Data Combination

**Public Data Used:**
- Funding announcement from Crunchbase (Series B, $30M)
- Job postings from careers page (15 engineering roles)
- Tech stack from BuiltWith (AWS, heavy on compute services)

**The Insight:**
$30M raise + 15 engineering hires + AWS-heavy stack = cloud bill likely to 3x in 12 months

### The PVP Message

Subject: Your AWS spend post-Series B

"Congrats on the $30M round. With 15 engineering roles open, you're probably about to see your AWS bill grow faster than your headcount.

Most companies at your stage see cloud costs 3x within a year of scaling engineering, and by the time it's painful, there's usually $200-400K/year in waste baked in.

I put together a quick benchmark of what companies your size typically spend on compute vs. what's actually needed. Happy to share if useful, no pitch, just data.

Either way, good luck with the scale-up."

### Why This Is Permissionless

- **Value delivered:** Benchmark data they'd otherwise have to research
- **No ask required:** They get the insight whether they respond or not
- **Demonstrates:** We understand their situation and the problem we solve

### Scaling This PVP

**Data needed:** Funding data, job posting count, tech stack
**Detection method:** Crunchbase alerts + LinkedIn job scraping + BuiltWith
**Volume potential:** ~200 companies/month match this pattern
```

## Classic PVP Example

Connecting crane utilization permits to wind turbine installations, creating leads and delivering value before even pitching your offering. (Idea credited to Jordan Crawford.)

The data is public (permits). The insight is valuable (which sites are active). The value is delivered without permission.

## Key Principles

1. **Lead With Value**: The ask (if any) comes last and is optional

2. **Combine, Don't Collect**: Single data points aren't insights. Combinations are.

3. **Be Genuinely Useful**: If they can't benefit without buying from you, it's not a PVP

4. **Demonstrate Expertise**: The insight shows you understand their world

## Related Skills

- `/data-point-research` - Find unique data to combine
- `/list-is-the-message` - Build segments from PVP patterns
- `/recent-news` - One source for PVP data
- `/company-goals` - Another source for PVP data

## Credits

The Permissionless Value Proposition (PVP) is Jordan Crawford ([Blueprint GTM](https://blueprintgtm.com))'s concept. The prompts and wording here are ours.

---

Examples are illustrative. Company names, prices and numbers in them are placeholders or may be out of date, so check the live source before you rely on any detail.
