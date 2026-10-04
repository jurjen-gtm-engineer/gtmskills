---
name: lead-scoring
description: Design lead scoring models using firmographic, behavioral, and custom data signals
metadata:
  version: "1.0"
---

# Lead Scoring Model Design

You are designing lead scoring models that prioritize prospects based on fit, intent, and custom signals.

## Input

User provides:
- ICP definition or target criteria
- Available data fields
- Optionally: historical win/loss data
- Optionally: sales team input on what matters

## Process

1. **Identify Scoring Dimensions**

   **Three Pillars:**
   - **Fit Score**: Do they match our ICP? (firmographics, technographics)
   - **Intent Score**: Are they showing buying signals? (behavior, timing)
   - **Custom Score**: Do they have our predictive indicators? (tension heuristics)

2. **Define Scoring Rules**

   **Prompt Pattern:**
   ```
   For this ICP: [DESCRIPTION]
   With these available data fields: [FIELDS]

   Create scoring rules across three dimensions:

   FIT (demographic match):
   - What criteria indicate strong fit?
   - What's a disqualifier?

   INTENT (buying signals):
   - What behaviors indicate interest?
   - What timing signals matter?

   CUSTOM (predictive indicators):
   - What non-standard signals predict success?
   - What patterns appear in best customers?
   ```

3. **Output Format**

   ```
   ## Lead Scoring Model: [Name]

   ### Scoring Dimensions

   **Fit Score (0-40 points)**
   | Criterion | Points | Rationale |
   |-----------|--------|-----------|
   | [Criterion 1] | +[X] | [Why] |
   | [Criterion 2] | +[X] | [Why] |
   | [Disqualifier] | -[X] | [Why] |

   **Intent Score (0-30 points)**
   | Signal | Points | Rationale |
   |--------|--------|-----------|
   | [Signal 1] | +[X] | [Why] |
   | [Signal 2] | +[X] | [Why] |

   **Custom Score (0-30 points)**
   | Indicator | Points | Rationale |
   |-----------|--------|-----------|
   | [Custom 1] | +[X] | [Why] |
   | [Custom 2] | +[X] | [Why] |

   ### Score Interpretation

   | Score Range | Priority | Action |
   |-------------|----------|--------|
   | 80-100 | Hot | Immediate AE outreach |
   | 60-79 | Warm | SDR sequence |
   | 40-59 | Nurture | Marketing automation |
   | <40 | Low | Deprioritize |

   ### Implementation

   **Data Requirements:**
   - [Field 1]: [Source]
   - [Field 2]: [Source]

   **Scoring Formula:**
   Total = Fit + Intent + Custom

   **Update Frequency:**
   - Fit: On data change
   - Intent: Real-time (behavior) or weekly (signals)
   - Custom: Per enrichment cycle
   ```

## Example

**Input:** "B2B SaaS selling to marketing teams. ICP is 200-2000 employees, using HubSpot or Marketo."

**Output:**
```
## Lead Scoring Model: Marketing SaaS Fit

### Scoring Dimensions

**Fit Score (0-40 points)**
| Criterion | Points | Rationale |
|-----------|--------|-----------|
| 200-2000 employees | +15 | Sweet spot for our solution |
| Uses HubSpot or Marketo | +15 | Tech stack fit |
| Marketing team 5+ | +10 | Budget and need |
| B2B company | +5 | Our focus |
| <50 employees | -20 | Too small |
| No marketing tech | -10 | Likely not ready |

**Intent Score (0-30 points)**
| Signal | Points | Rationale |
|--------|--------|-----------|
| Visited pricing page | +15 | High intent |
| Downloaded resource | +10 | Engaged |
| Marketing job posting | +10 | Investing in function |
| Competitor mentioned | +5 | In market |
| Attended webinar | +5 | Active interest |

**Custom Score (0-30 points)**
| Indicator | Points | Rationale |
|-----------|--------|-----------|
| Recent funding (6 mo) | +15 | Budget available |
| New CMO/VP Marketing | +10 | Fresh mandate |
| Multiple marketing tools | +5 | Complexity = need |
| Agency on team page | -5 | May outsource |

### Score Interpretation

| Score Range | Priority | Action |
|-------------|----------|--------|
| 80-100 | Hot | AE call within 24h |
| 60-79 | Warm | SDR 5-touch sequence |
| 40-59 | Nurture | Weekly email digest |
| <40 | Low | Quarterly check-in |

### Implementation

**Data Requirements:**
- Employee count: Clearbit/Apollo
- Tech stack: BuiltWith/HG Insights
- Job postings: LinkedIn/Indeed scrape
- Funding: Crunchbase
- Page visits: HubSpot/Segment

**Scoring Formula:**
Total = Fit (max 40) + Intent (max 30) + Custom (max 30)

**Update Frequency:**
- Fit: On data enrichment
- Intent: Real-time from website
- Custom: Weekly signal refresh
```

## Best Practices

1. **Start Simple**: 5-7 rules, not 50
2. **Validate with Sales**: Do scores match their intuition?
3. **Test with Historical Data**: Do high scores correlate with wins?
4. **Iterate Monthly**: Refine based on results

## Related Skills

- `/pain-qualified-segment` - Tension-based scoring inputs
- `/data-point-research` - Custom signals to include
- `/company-goals` - Intent from hiring
- `/recent-news` - Timing signals

## Credits

The tension-heuristic idea used for custom signals comes from Jordan Crawford ([Blueprint GTM](https://blueprintgtm.com)).

---

Examples are illustrative. Company names, prices and numbers in them are placeholders or may be out of date, so check the live source before you rely on any detail.
