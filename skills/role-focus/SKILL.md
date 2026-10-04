---
name: role-focus
description: Analyze what a job title emphasizes to personalize outreach by role
metadata:
  version: "1.0"
---

# Role Focus Analysis

You are analyzing what a specific job title/role emphasizes to enable role-based personalization.

## Input

User provides:
- A job title (e.g., "CTO", "VP of Sales", "Director of Marketing")
- Optionally: company context or job description

## Process

1. **Analyze Role**

   **Prompt Pattern:**
   ```
   For the role: [JOB TITLE]

   Describe what this role typically focuses on:
   1. Primary responsibilities
   2. Key metrics they're measured on
   3. Common pain points
   4. What they care about when evaluating solutions
   5. Decision-making authority (budget, team, strategy)
   ```

2. **Generate Personalization Angles**

   Based on role focus, suggest:
   - Opening lines that resonate
   - Pain points to reference
   - Metrics to mention
   - Tone adjustments

3. **Output Format**

   ```
   Role: [Job Title]

   Primary Focus:
   - [Focus area 1]
   - [Focus area 2]

   Key Metrics:
   - [Metric 1]
   - [Metric 2]

   Common Pain Points:
   - [Pain 1]
   - [Pain 2]

   Decision Authority:
   - Budget: [Yes/No/Influence]
   - Team: [Size/scope]
   - Strategy: [Sets/Executes/Influences]

   Personalization Angles:
   - Opening: "As a [role], you're likely focused on [focus area]..."
   - Pain reference: "Many [roles] tell us [pain point]..."
   - Metric hook: "If [metric] is a priority..."
   ```

## Example

**Input:** CTO

**Output:**
```
Role: CTO

Primary Focus:
- Technology strategy and architecture
- Engineering team leadership
- Technical debt vs. innovation balance
- Security and compliance
- Build vs. buy decisions

Key Metrics:
- System uptime/reliability
- Engineering velocity
- Technical debt ratio
- Security incident rate
- Time to market for features

Common Pain Points:
- Scaling infrastructure with growth
- Hiring and retaining engineers
- Legacy system modernization
- Balancing security with speed
- Vendor sprawl and integration complexity

Decision Authority:
- Budget: Yes (technology stack)
- Team: Large (engineering org)
- Strategy: Sets technical direction

Personalization Angles:
- Opening: "As a CTO, you're likely focused on scaling your tech infrastructure while managing complexity..."
- Pain reference: "Many CTOs tell us vendor sprawl is eating into their team's productivity..."
- Metric hook: "If engineering velocity is a priority, you might find this interesting..."
```

## Related Skills

- `/clean-job-titles` - Standardize verbose titles first
- `/ideal-customer-profiles` - Match role to ICP
- `/pain-qualified-segment` - Role-specific pain indicators

---

Examples are illustrative. Company names, prices and numbers in them are placeholders or may be out of date, so check the live source before you rely on any detail.
