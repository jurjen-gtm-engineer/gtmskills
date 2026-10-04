---
name: pain-qualified-segment
description: Build segments based on tension heuristics that indicate active pain points, not just firmographics
metadata:
  version: "1.0"
---

# Pain Qualified Segment

You are building segments based on "tension heuristics" - data points that indicate a prospect is experiencing active pain, not just matching firmographic criteria.

## Core Concept

Identify your best performing segment, not just by revenue bracket, but by nuanced, calculated data (e.g., specific tech usage, personnel ratios, unique business pain-points).

Traditional ICP: "Companies with 500+ employees in Finance"
Pain Qualified: "Companies with 500+ employees in Finance that just lost their CISO and have 3+ compliance job postings"

## Input

User provides:
- Target ICP or segment criteria
- Pain points your solution addresses
- Optionally: customer data to analyze

## Process

1. **Identify Tension Indicators**

   **Prompt Pattern:**
   ```
   For this ICP: [DESCRIPTION]
   And this pain point: [PAIN]

   What 2-5 measurable or inferable signals would indicate this pain is ACTIVE right now?

   Consider:
   - Personnel ratios (e.g., sales engineers vs total staff)
   - Recent changes (funding + hiring freeze, leadership departure)
   - External pressures (regulatory deadline, competitive threat)
   - Capability gaps (job postings for roles they lack, tech stack gaps)
   - Timing factors (end of quarter, budget cycle, contract renewal)
   ```

2. **Define the Segment**

   **Structure:**
   ```
   Segment Name: [Descriptive name]

   Base ICP:
   - [Firmographic criteria]

   Tension Heuristics (2-5):
   1. [Signal] - indicates [pain]
   2. [Signal] - indicates [pain]
   3. [Signal] - indicates [pain]

   Data Sources to Detect:
   - [Signal 1]: [How to find/measure]
   - [Signal 2]: [How to find/measure]
   ```

3. **Output Format**

   ```
   ## Pain Qualified Segment: [Name]

   ### Why This Segment

   The combination of [base criteria] + [tension signals] indicates:
   - The problem is acute right now
   - External pressure is forcing change
   - Timing is favorable for a solution

   ### Definition

   **Base Criteria:**
   - [Firmographic 1]
   - [Firmographic 2]

   **Tension Heuristics:**
   | Signal | What It Indicates | How to Detect |
   |--------|-------------------|---------------|
   | [Signal 1] | [Pain indicator] | [Data source] |
   | [Signal 2] | [Pain indicator] | [Data source] |

   ### The List Is the Message (Jordan Crawford's phrase)

   Because you know WHY they're on this list:
   - Messaging writes itself
   - Personalization is substantive, not cosmetic
   - "Why you, why now" is obvious

   **Outreach Angle:**
   "[We noticed/Given that] [tension signal], [companies like yours/you might be] [experiencing pain]. [Value prop]..."

   ### Detection Workflow

   1. Start with [base criteria] filter
   2. Enrich with [data needed for tension signals]
   3. Score/flag where [X of Y tension signals] present
   4. Route high-tension accounts to immediate outreach
   ```

## Examples

**Input:** "We sell security compliance software. ICP is mid-market SaaS companies."

**Output:**
```
## Pain Qualified Segment: Compliance-Pressured SaaS

### Why This Segment

Companies facing compliance pressure with capability gaps:
- Regulatory or customer pressure is forcing action
- They lack internal expertise to handle it
- Timing is urgent (audits, renewals, enterprise deals)

### Definition

**Base Criteria:**
- SaaS company
- 100-1000 employees
- B2B (enterprise customers likely)

**Tension Heuristics:**
| Signal | What It Indicates | How to Detect |
|--------|-------------------|---------------|
| No CISO or security leader | Capability gap | LinkedIn search, org chart |
| "SOC 2" in job postings | Active compliance initiative | Job board scraping |
| Enterprise customer logos | Compliance requirements from customers | Website analysis |
| Recent Series B+ | Pressure to professionalize | Funding data |
| Security vendor on their stack | Already investing, may need more | Technographic data |

### The List Is the Message (Jordan Crawford's phrase)

**Outreach Angle:**
"I noticed you're hiring for security roles and have enterprise customers like [Customer], compliance requirements can be overwhelming when you're scaling. We help SaaS companies get SOC 2 ready without hiring a full security team..."

### Detection Workflow

1. Filter: SaaS, 100-1000 employees, B2B
2. Enrich: Job postings, customer logos, funding, tech stack
3. Score: 3+ tension signals = high priority
4. Route: High-tension to AE, others to nurture
```

## Key Principles

1. **Tension > Firmographics**: A small company with acute pain beats a perfect-fit company with no urgency

2. **Measurable Signals**: If you can't detect it, you can't target it

3. **The "Why" Drives Messaging**: Knowing why they're on the list makes personalization substantive

4. **Dynamic, Not Static**: Tension changes, signals should trigger re-evaluation

## Related Skills

- `/data-point-research` - Find the data to detect tension
- `/company-goals` - Job postings reveal priorities
- `/recent-news` - Events that create tension
- `/role-focus` - Who feels the pain

## Credits

Pain-qualified segments, tension heuristics and "the list is the message" are Jordan Crawford ([Blueprint GTM](https://blueprintgtm.com))'s concepts. The prompts and wording here are ours.

---

Examples are illustrative. Company names, prices and numbers in them are placeholders or may be out of date, so check the live source before you rely on any detail.
