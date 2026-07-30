---
name: conversational-intelligence
description: Extract structured intelligence from call transcripts, from any transcript source (Fireflies, Gong, or plain files exported locally). Mines conversations for handoff context, competitive intelligence, expansion signals, and closed-lost analysis.
version: 1.0
---

# Conversational Intelligence Extractor

## Purpose

Turn call transcripts into structured, actionable intelligence. Works from any call transcript source: Fireflies, Gong, Chorus, or plain transcript files exported locally. Outputs JSON-structured insights that drive handoff automations, competitive displacement campaigns, expansion plays, and product feedback loops.

## Required Tools

- **A call transcript source**: any of the following works
  - Fireflies (API or MCP, if connected)
  - Gong or Chorus exports
  - Plain transcript files on disk (`.txt`, `.vtt`, `.srt`, JSON, markdown)
- **Optional: an enrichment tool of your choice** (Clay, Apollo, or any data provider) to enrich mentioned companies and contacts. The skill works fully without it.

## Inputs

### Required
- `extraction_type`: One of: `handoff` | `competitive` | `expansion` | `closed-lost` | `full` (runs all)
- `target`: One of:
  - A transcript ID or file path (specific call)
  - A company name/domain (pulls all recent calls mentioning that company)
  - A date range + keyword (searches across all calls)

### Optional
- `output_label`: A label (e.g. the account name) used in output filenames
- `enrich`: Boolean, default false. Enrich mentioned companies/contacts via your enrichment tool of choice
- `output_format`: `json` | `markdown` | `both` (default: `both`)

## Process

### Step 1: Retrieve Transcripts

Based on the `target` input, pull the right transcripts from your transcript source.

**If transcript ID or file path provided:**
```
→ Fetch that transcript (and its AI summary, if your source provides one)
```

**If company name/domain provided:**
```
→ Search your transcript source for the company name (limit ~10 results)
→ For each result: fetch the full transcript
```

**If date range + keyword:**
```
→ Search your transcript source by keyword within the date range (limit ~20 results)
→ For each result: fetch the full transcript
```

With local files, "search" means grepping the transcript directory for the company name or keyword and filtering by file date.

**IMPORTANT:** When your source provides both a summary and a full transcript, always pull both. The summary gives quick orientation; the transcript gives verbatim quotes and speaker attribution.

### Step 2: Extract Structured Intelligence

Run extraction based on `extraction_type`. For `full`, run all four in sequence.

#### 2A: Handoff Extraction (`handoff`)

Extract from ALL pre-sale conversations to build complete customer context.

**Schema:**
```json
{
  "handoff_intelligence": {
    "account_name": "string",
    "extraction_date": "YYYY-MM-DD",
    "calls_analyzed": "number",
    "icp_alignment": "string: fit assessment with specific evidence",
    "org_structure": "string: reporting lines, team sizes, relevant departments",
    "primary_challenges": [
      {
        "challenge": "string: specific problem",
        "severity": "critical | high | medium",
        "quote": "string: verbatim from transcript",
        "speaker": "string: name and role"
      }
    ],
    "red_flags": [
      {
        "flag": "string: risk description",
        "source": "string: which call, who mentioned it",
        "mitigation": "string: suggested approach"
      }
    ],
    "expansion_potential": "string: adjacent use cases or teams mentioned",
    "buying_motivations": [
      "string: specific reasons they chose us (verbatim language)"
    ],
    "key_stakeholders": [
      {
        "name": "string",
        "role": "string",
        "influence": "decision_maker | influencer | end_user | champion | blocker",
        "concerns": ["string: specific concerns raised"],
        "communication_style": "string: brief note on how they communicate"
      }
    ],
    "implementation_context": {
      "timeline_expectations": "string",
      "technical_requirements": "string",
      "success_criteria": "string: what does 'working' look like to them"
    }
  }
}
```

**Edge cases:**
- If org structure is unclear, note "Org structure not discussed: confirm in first CX call"
- If no red flags found, set to empty array (don't invent risks)
- For influence level, default to "end_user" if role is ambiguous

#### 2B: Competitive Intelligence Extraction (`competitive`)

Scan all transcripts for competitor mentions, budget data, renewal timelines.

**Schema:**
```json
{
  "competitive_intelligence": {
    "account_name": "string",
    "extraction_date": "YYYY-MM-DD",
    "calls_analyzed": "number",
    "competitors_detected": [
      {
        "competitor_name": "string",
        "competitor_domain": "string: if identifiable",
        "current_spend": "string or null: '$X annually/monthly'",
        "contract_end_date": "string or null: 'YYYY-MM-DD' or 'QX YYYY'",
        "renewal_timeline": "imminent | within_3_months | within_6_months | beyond_6_months | unknown",
        "primary_frustrations": ["string: use exact customer language"],
        "satisfaction_level": "satisfied | neutral | frustrated | actively_looking_to_switch",
        "mentioned_by": {
          "name": "string",
          "role": "string",
          "influence_level": "decision_maker | influencer | end_user",
          "specific_quote": "string: verbatim"
        },
        "displacement_opportunity": {
          "probability": "high | medium | low",
          "rationale": "string: why this is/isn't a good displacement target",
          "recommended_approach": "string: specific campaign angle"
        }
      }
    ],
    "tool_stack_mentioned": ["string: all tools/vendors mentioned"],
    "budget_signals": [
      {
        "amount": "string",
        "context": "string: what it's for",
        "speaker": "string"
      }
    ]
  }
}
```

**Edge cases:**
- If no budget mentioned, set `current_spend` to null: NEVER estimate
- Vague timelines ("sometime next year") → extract as full year range "Q1-Q4 YYYY"
- Only mark "actively_looking_to_switch" if they explicitly mention evaluating alternatives
- If multiple people mention the same competitor, create ONE entry with multiple quotes

#### 2C: Expansion Signal Extraction (`expansion`)

Detect upsell/cross-sell signals from customer conversations.

**Schema:**
```json
{
  "expansion_signals": {
    "account_name": "string",
    "extraction_date": "YYYY-MM-DD",
    "calls_analyzed": "number",
    "signals": [
      {
        "signal_type": "new_use_case | new_team | new_geography | increased_usage | feature_request | integration_need",
        "description": "string: what they want",
        "current_state": "string: what they do today",
        "desired_state": "string: what they're looking for",
        "urgency": "immediate | near_term | exploratory",
        "mentioned_by": {
          "name": "string",
          "role": "string",
          "quote": "string: verbatim"
        },
        "recommended_action": "string: specific next step"
      }
    ],
    "product_feedback": [
      {
        "type": "feature_request | improvement | bug_report | praise",
        "description": "string",
        "speaker": "string",
        "business_justification": "string: why they need it"
      }
    ]
  }
}
```

#### 2D: Closed-Lost Analysis (`closed-lost`)

Process transcripts from lost deals to find systematic failure patterns.

**Schema:**
```json
{
  "closed_lost_analysis": {
    "account_name": "string",
    "extraction_date": "YYYY-MM-DD",
    "calls_analyzed": "number",
    "primary_loss_category": "missing_capability | pricing | competitor | timing | internal_politics | no_budget | champion_left | bad_fit | other",
    "detailed_reason": "string: specific explanation with evidence",
    "stakeholder_objections": [
      {
        "stakeholder_role": "string",
        "objection": "string: specific concern",
        "severity": "deal_killer | major_concern | minor_concern",
        "quote": "string: verbatim",
        "was_addressed": "yes | partially | no",
        "how_addressed": "string or null"
      }
    ],
    "competitive_factor": {
      "competitor_chosen": "string or null",
      "why_they_won": "string: specific reasons",
      "could_we_have_won": "string: honest assessment"
    },
    "deal_stage_lost": "string: where in pipeline",
    "recovery_possibility": "high | medium | low",
    "recovery_rationale": "string: what would need to change",
    "lessons": [
      {
        "category": "sales_process | product_gap | positioning | pricing | timing",
        "insight": "string: what we should learn from this",
        "actionable": "boolean: can we act on this now"
      }
    ]
  }
}
```

**Edge cases:**
- If rep marked "pricing" but transcripts reveal a different issue, note the discrepancy
- Don't simplify: capture the full chain of objections that led to the loss
- For `recovery_possibility`, only mark "high" if there's a clear trigger event (e.g., contract renewal, champion returning)

### Step 3: Enrich (optional, if `enrich` = true)

For every company and key stakeholder mentioned in the extracted intelligence, enrich mentioned companies via your enrichment tool of choice:

**Company enrichment:**
```
→ Enrich each company domain for data points like: Tech Stack, Open Jobs, Recent News, Annual Revenue, Competitors
```

Cross-reference enrichment data with transcript mentions:
- Do their open jobs validate the challenges mentioned? (e.g., hiring data engineers → confirms data quality pain)
- Does their tech stack confirm or contradict tool mentions from calls?
- Does revenue/headcount context help size the opportunity?

**Contact enrichment (for key stakeholders):**
```
→ Find and enrich contacts at the company matching the stakeholder roles mentioned
```

Append enrichment results to the extracted intelligence under an `enrichment` key.

### Step 4: Generate Output

Based on `output_format`:

**JSON output:** Clean, validated JSON matching the schemas above. Save to `conversational-intelligence-[output_label]-[date].json` in your working directory.

**Markdown output:** Human-readable report with:
- Executive summary (3-5 bullet points of highest-value findings)
- Detailed findings organized by extraction type
- Verbatim quotes with speaker attribution
- Recommended next actions (prioritized)
- Enrichment insights (if applicable)

Save markdown to `conversational-intelligence-[output_label]-[date].md` in your working directory.

### Step 5: Identify Actionable Workflows

Based on extracted intelligence, recommend specific workflows to trigger:

| Signal Found | Recommended Action |
|---|---|
| Competitor with renewal < 3 months + frustration | Displacement campaign targeting the frustrated stakeholder |
| New use case mentioned by decision maker | Expansion play with specific use case positioning |
| Red flag on implementation concerns | Proactive mitigation in first CX call |
| Champion identified across multiple calls | Champion enablement sequence with supporting materials |
| Budget amount + timeline confirmed | Fast-track opportunity with specific pricing |
| Product gap caused deal loss | Product feedback ticket with verbatim customer language |

## Quality Checks

Before outputting, validate:

- [ ] Every quote is verbatim from the transcript (not paraphrased)
- [ ] Speaker attribution matches the transcript (correct name + role)
- [ ] No fields are estimated: null if not mentioned
- [ ] Predefined options use ONLY allowed values
- [ ] Logical consistency (e.g., if renewal_timeline is set, competitor_name must exist)
- [ ] Enrichment data cross-referenced with transcript mentions (flag contradictions)

## Example Usage

### Mine a specific call for competitive intelligence
```
extraction_type: competitive
target: [transcript ID or file path]
enrich: true
```

### Build handoff package for closing deal
```
extraction_type: handoff
target: "acme.com"  (pulls all calls mentioning Acme)
output_label: acme
enrich: true
output_format: both
```

### Analyze lost deals this quarter
```
extraction_type: closed-lost
target: keyword:"closed lost" from:2026-01-01 to:2026-03-31
enrich: false
output_format: markdown
```

### Full intelligence sweep for account planning
```
extraction_type: full
target: "example.com"
output_label: example
enrich: true
output_format: both
```

## Common Workflows

### Workflow: Deal Handoff Automation
```
1. conversational-intelligence (handoff) → Extract all pre-sale context
2. Optional enrichment → Add firmographic + technographic depth
3. Output → Structured handoff doc for CX team
```

### Workflow: Competitive Displacement Campaign
```
1. conversational-intelligence (competitive) → Find competitor mentions + frustrations
2. Optional enrichment → Validate competitor data, find decision makers
3. Write a displacement email targeting the frustrated stakeholder
4. Build a follow-up sequence timed to the renewal date
```

### Workflow: Quarterly Account Intelligence
```
1. conversational-intelligence (full) → Sweep all calls for account
2. Optional enrichment → Current company data
3. Output → Account intelligence brief for CS/sales planning
```
