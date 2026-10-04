---
name: icp-scoring-dynamic
description: Calculate dynamic ICP scores from enriched data using Claygent (Patrick Spychalski)
metadata:
  version: "1.0"
---

# Dynamic ICP Scoring

You are applying Patrick Spychalski's methodology for dynamic ICP scoring, using Claygent to calculate fit scores from multiple enriched data points in real-time.

## Core Concept

Uses Claygent to calculate dynamic ICP score from enriched data, match tech usage and company characteristics. (Idea credited to Patrick Spychalski.)

Instead of static ICP lists, build scoring that:
- Updates as data changes
- Combines multiple signals
- Weights factors by importance
- Generates actionable tiers

## Input

User provides:
- ICP definition or characteristics
- Available data fields (enriched data)
- Optionally: weights for different factors
- Optionally: historical win data for calibration

## Process

1. **Define Scoring Dimensions**

   **Prompt Pattern:**
   ```
   For this ICP: [ICP DESCRIPTION]

   Define scoring dimensions from these available data fields: [FIELDS]

   Categories:
   - FIRMOGRAPHIC FIT: Company characteristics that match ICP
   - TECH FIT: Technology/tools that indicate fit
   - BEHAVIORAL FIT: Signals that indicate active need
   - TIMING FIT: Factors that indicate readiness

   For each dimension, specify:
   - Which data fields to use
   - How to score (points for each value)
   - Weight relative to other dimensions
   ```

2. **Build the Scoring Prompt**

   **Claygent Scoring Prompt:**
   ```
   Calculate ICP score for this company using the following rules:

   FIRMOGRAPHIC SCORE (max 30 points):
   - Employee count 100-500: +15 points
   - Employee count 501-2000: +10 points
   - Industry is [target industry]: +10 points
   - B2B company: +5 points

   TECH SCORE (max 25 points):
   - Uses [Target Tech 1]: +15 points
   - Uses [Target Tech 2]: +10 points
   - Has [Complementary Tech]: +5 points
   - Uses [Competitor]: -10 points

   BEHAVIORAL SCORE (max 25 points):
   - Hiring for [relevant role]: +15 points
   - Recent funding: +10 points
   - Growth indicators: +10 points

   TIMING SCORE (max 20 points):
   - Trigger event in last 30 days: +20 points
   - Trigger event in last 90 days: +10 points

   Input data:
   - Employee count: {{employee_count}}
   - Industry: {{industry}}
   - Tech stack: {{tech_stack}}
   - Open roles: {{job_postings}}
   - Recent funding: {{funding}}
   - Recent news: {{news}}

   Return JSON:
   {
     "firmographic_score": X,
     "tech_score": X,
     "behavioral_score": X,
     "timing_score": X,
     "total_score": X,
     "tier": "Hot/Warm/Nurture/Low",
     "top_signals": ["signal1", "signal2", "signal3"]
   }
   ```

3. **Output Format**

   ```
   ## Dynamic ICP Scoring Model: [Name]

   ### Scoring Dimensions

   **Firmographic Fit (max [X] points)**
   | Field | Value | Points |
   |-------|-------|--------|
   | [Field] | [Target value] | +[X] |
   | [Field] | [Target value] | +[X] |

   **Tech Fit (max [X] points)**
   | Technology | Points | Rationale |
   |------------|--------|-----------|
   | [Tech] | +[X] | [Why] |

   **Behavioral Fit (max [X] points)**
   | Signal | Points | Rationale |
   |--------|--------|-----------|
   | [Signal] | +[X] | [Why] |

   **Timing Fit (max [X] points)**
   | Trigger | Points | Rationale |
   |---------|--------|-----------|
   | [Trigger] | +[X] | [Why] |

   ### Score Tiers

   | Score | Tier | Action |
   |-------|------|--------|
   | 80-100 | Hot | Immediate outreach |
   | 60-79 | Warm | Prioritized sequence |
   | 40-59 | Nurture | Marketing automation |
   | <40 | Low | Monitor for changes |

   ### Claygent Implementation

   ```prompt
   [Full scoring prompt for copy/paste]
   ```

   ### Required Data Fields

   - [Field 1]: Source: [Enrichment provider]
   - [Field 2]: Source: [Enrichment provider]
   ```

## Example

**Input:** "ICP: Mid-market SaaS companies using Salesforce, showing growth signals"

**Output:**
```
## Dynamic ICP Scoring Model: Growth SaaS Fit

### Scoring Dimensions

**Firmographic Fit (max 30 points)**
| Field | Value | Points |
|-------|-------|--------|
| Employees | 100-500 | +15 |
| Employees | 501-2000 | +10 |
| Business model | SaaS/B2B | +10 |
| Revenue | $10M-$100M | +5 |

**Tech Fit (max 25 points)**
| Technology | Points | Rationale |
|------------|--------|-----------|
| Salesforce | +15 | Core integration |
| HubSpot Marketing | +10 | Complementary tool |
| Outreach or Salesloft | +5 | Sales tech mature |
| Competitor X | -10 | Already solved |

**Behavioral Fit (max 25 points)**
| Signal | Points | Rationale |
|--------|--------|-----------|
| RevOps job posting | +15 | Active pain |
| 5+ sales hires open | +10 | Scaling sales |
| SDR/BDR roles open | +5 | Outbound investment |

**Timing Fit (max 20 points)**
| Trigger | Points | Rationale |
|---------|--------|-----------|
| Funding < 90 days | +15 | Budget available |
| New CRO/VP Sales | +10 | Fresh mandate |
| Tech review season (Q4) | +5 | Buying cycle |

### Score Tiers

| Score | Tier | Action |
|-------|------|--------|
| 80-100 | Hot | AE direct outreach within 24h |
| 60-79 | Warm | SDR multi-touch sequence |
| 40-59 | Nurture | Weekly content, monthly check |
| <40 | Low | Quarterly review |

### Claygent Implementation

```prompt
Calculate ICP score for {{company_name}}:

FIRMOGRAPHIC (30 max):
- Employees 100-500: +15, 501-2000: +10
- SaaS/B2B: +10
- Revenue $10M-$100M: +5

TECH (25 max):
- Salesforce: +15
- HubSpot Marketing: +10
- Outreach/Salesloft: +5
- [Competitor]: -10

BEHAVIORAL (25 max):
- RevOps job posting: +15
- 5+ sales hires: +10
- SDR/BDR hiring: +5

TIMING (20 max):
- Funding <90 days: +15
- New CRO/VP Sales: +10

Data: Employees={{employees}}, Industry={{industry}}, Tech={{tech_stack}}, Jobs={{jobs}}, Funding={{funding}}

Return JSON: {"firmographic": X, "tech": X, "behavioral": X, "timing": X, "total": X, "tier": "Hot/Warm/Nurture/Low", "signals": []}
```
```

## Key Principles

1. **Dynamic > Static**: Score updates as data changes
2. **Multi-dimensional**: Combine firmographic + tech + behavioral + timing
3. **Weighted**: Not all signals are equal
4. **Actionable Tiers**: Score maps to specific actions

## Related Skills

- `/lead-scoring` - Full scoring model design
- `/pain-qualified-segment` - Behavioral signals
- `/data-point-research` - Custom signals to include
- `/playbook-pitch-generation` - Use scores to customize pitch

## Credits

The dynamic scoring approach follows Patrick Spychalski ([The Kiln](https://thekiln.com)). The prompts and wording here are ours.

---

Examples are illustrative. Company names, prices and numbers in them are placeholders or may be out of date, so check the live source before you rely on any detail.
