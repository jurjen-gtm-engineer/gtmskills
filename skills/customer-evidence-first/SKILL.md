---
name: customer-evidence-first
description: Start GTM strategy from why customers actually bought, not what you sell (Jordan Crawford)
metadata:
  version: "1.0"
---

# Customer Evidence First

You are applying Jordan Crawford's "Customer Evidence First" methodology, starting your GTM strategy from the real, quantifiable reasons customers bought, not from what you think you sell.

## Core Philosophy

Start with the real, quantifiable reason customers bought. Invert the process: don't start from what you sell.

Traditional approach: Here's what we sell → Find people who might want it
Customer Evidence First: Here's why customers bought → Find more like them

## Input

User provides:
- Customer win data (deals closed, customer interviews, CRM notes)
- Or: description of best customers and what they said during sales process
- Optionally: product/service being sold

## Process

1. **Extract the Real Reasons**

   **Prompt Pattern:**
   ```
   From this customer data: [CUSTOMER INFO]

   Extract the REAL reasons they bought, not features, but:
   - What situation were they in?
   - What triggered the search?
   - What was the cost of NOT solving?
   - What alternatives did they consider?
   - What made them choose us specifically?

   Look for patterns across customers, not just individual stories.
   ```

2. **Identify the Trigger Events**

   ```
   What specific events or situations PRECEDED these customers reaching out?

   Look for:
   - External pressures (regulatory, competitive, market)
   - Internal changes (new hire, growth, problem surfaced)
   - Timing factors (budget cycle, quarter end, renewal)

   These triggers are the "why now" for future prospects.
   ```

3. **Build the Evidence-Based Positioning**

   ```
   Based on why customers actually bought:

   - What problem should we lead with?
   - What trigger events should we target?
   - What proof points resonate most?
   - What objections were overcome?
   ```

4. **Output Format**

   ```
   ## Customer Evidence Analysis

   ### Why Customers Actually Bought

   | Customer Pattern | Real Reason | Trigger Event |
   |------------------|-------------|---------------|
   | [Pattern 1] | [Reason] | [Trigger] |
   | [Pattern 2] | [Reason] | [Trigger] |

   ### The Inverted Positioning

   **Traditional pitch:** [What we think we sell]
   **Evidence-based pitch:** [What customers actually bought]

   ### Trigger Events to Target

   1. [Trigger 1] - indicates [reason to buy]
   2. [Trigger 2] - indicates [reason to buy]

   ### Proof Points That Convert

   - "[Customer quote about real reason]"
   - "[Quantified outcome that mattered]"

   ### Objections Already Overcome

   | Objection | How Won Customers Overcame It |
   |-----------|-------------------------------|
   | [Objection 1] | [What convinced them] |

   ### Application to Outbound

   Target: [Who to target based on evidence]
   Message: [What to say based on real reasons]
   Timing: [When to reach out based on triggers]
   ```

## Example

**Input:** "We sell sales enablement software. Best customers: mid-market SaaS, 50-200 employees, AE teams of 10-30."

**Output:**
```
## Customer Evidence Analysis

### Why Customers Actually Bought

| Customer Pattern | Real Reason | Trigger Event |
|------------------|-------------|---------------|
| Rapid AE growth | New hires ramping too slowly | Hired 5+ AEs in 90 days |
| Lost competitive deals | Reps couldn't find right content | Lost to competitor with better demos |
| New sales leader | VP wanted to professionalize org | VP Sales hired in last 6 months |
| Series B pressure | Board wanted faster growth metrics | Recent funding + revenue targets |

### The Inverted Positioning

**Traditional pitch:** "Sales enablement platform with content management and analytics"

**Evidence-based pitch:** "Cut new AE ramp time from 6 months to 6 weeks, critical when you're scaling fast and every rep needs to produce now"

### Trigger Events to Target

1. **5+ AE hires in 90 days** - ramping pain is acute
2. **New VP Sales** - mandate to change things
3. **Lost competitive deal** - urgency to fix sales process
4. **Series B in last 6 months** - pressure to scale

### Proof Points That Convert

- "Our new AEs hit quota in month 2 instead of month 5"
- "Win rate against [Competitor] went from 30% to 55%"
- "VP Sales at [Customer]: 'This is the first thing I implemented'"

### Objections Already Overcome

| Objection | How Won Customers Overcame It |
|-----------|-------------------------------|
| "We have a shared drive" | Showed time wasted searching |
| "Reps won't use it" | Showed Slack integration, no new habits |
| "Too expensive" | ROI'd against one recovered deal |

### Application to Outbound

**Target:** Series B SaaS, 10+ AEs, new sales leader OR rapid hiring
**Message:** Lead with ramp time reduction, not features
**Timing:** Within 30 days of trigger event
```

## Key Principles

1. **Customers Don't Buy Features**: They buy outcomes and escape from pain

2. **Your Best Source Is Won Deals**: Not lost deals, not marketing surveys, actual closed business

3. **Triggers > Firmographics**: Who they are matters less than what they're experiencing

4. **Proof Points Come From Customers**: Not from your marketing team

## Related Skills

- `/pain-qualified-segment` - Build segments from evidence
- `/list-is-the-message` - Turn evidence into self-evident messaging
- `/recent-news` - Find trigger events
- `/company-goals` - Detect hiring triggers

## Credits

The Customer Evidence First idea is Jordan Crawford ([Blueprint GTM](https://blueprintgtm.com))'s. The prompts and wording here are ours.

---

Examples are illustrative. Company names, prices and numbers in them are placeholders or may be out of date, so check the live source before you rely on any detail.
