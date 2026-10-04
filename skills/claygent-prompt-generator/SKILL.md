---
name: claygent-prompt-generator
description: Generate cache-optimized Claygent prompts with all static logic first and {{variables}} at the bottom for Clay API cached inputs
---

# Skill: Claygent Prompt Generator

Generate production-ready Claygent prompts optimized for Clay's API cached inputs. All static instruction content goes first (cached across rows), all `{{variables}}` that need manual column mapping in Clay go at the bottom (dynamic per row).

**This is a prompt-only skill**: no webhook testing, no iteration loop. For full build-test-iterate, use `claygent-builder` instead.

## How Claygent Actually Works: ONE Prompt

Claygent has **a single prompt field** (plus an optional JSON schema field). There is NO separate system prompt field. Everything (identity, definitions, decision tree, examples, output format, guardrails, task instructions, and row variables) goes into one unified prompt.

**Deliverable count by task type:**
- **No web browsing needed** (pure text analysis on data passed in): 2 artefacts, `Prompt` + `JSON Schema`
- **Web browsing needed** (agent navigates to URLs): 2 artefacts, `Prompt` + `JSON Schema` (browsing instructions live inside the prompt, not as a separate field)

The prompt is structured with the static block first (cached) and `{{variables}}` grouped at the very bottom under a "Row Data" section (dynamic per row).

## Why Cache-Optimized Structure Matters

OpenAI's **cached inputs** feature reuses prior compute when requests share an identical prefix, billing cached input tokens at up to **90% discount** (GPT-5 suite). Two conditions must be met:

1. **Prompt must be at least 1,024 tokens**: below this threshold, caching never triggers
2. **Prefix must be identical across requests**: all variability pushed to the very end

When you run a Claygent across 10,000 rows:
- **Static block** (identity, logic, examples, format) = identical prefix, cached across all rows, billed at up to 90% discount
- **Variable block** (company name, website, etc.) = only part that changes per row, billed at standard rate

Wrong structure (variables scattered throughout) = every request unique = no caching = full input cost per row.
Right structure (variables at bottom, static block at least 1,024 tokens) = prefix cached = massive cost savings at scale.

**Reference:** OpenAI's prompt caching documentation covers the pricing details and the 1,024-token threshold.

## Inputs

- **Task description** (required): What the Claygent should do
- **Input variables** (required): What Clay columns feed into this prompt (e.g., company domain, company name, LinkedIn URL)
- **Output fields** (required): What structured data the Claygent should return
- **Complexity hint** (optional): Simple / Medium / Advanced (auto-detected if not provided)

## Process

### Step 1: Classify & Scope

Determine:

| Complexity | Criteria | Example Count |
|------------|----------|---------------|
| **Simple** | Binary yes/no, single field, one page visit | 3 examples |
| **Medium** | Multi-field, classification with reasoning, 2-3 pages | 5 examples |
| **Advanced** | Multi-step research, conditional logic, chain of thought | 10 examples |

Apply the 10-minute rule: if a human couldn't do this in 10 minutes of manual research, break it into multiple Claygent calls.

Apply the "One Task Per Prompt" rule: if the task has two distinct jobs (e.g., enrich + classify), split into two separate prompts.

### Step 2: Build the Static Block (Cached: top of the single prompt)

This is the top portion of the Claygent prompt, the cached prefix. Build it using the 6 reliability patterns in order. Everything below goes ABOVE the Row Data section in the final single prompt.

**Section 1: Identity + Scope** (2-3 sentences)
```
You are a [specific role] that [specific capability].
Your job is to [one task] by [method].
You output [format] and nothing else.
```
Anti-pattern: "You are a helpful AI assistant" is too generic.

**Section 2: Definitions**
- Every classification value defined with concrete criteria
- No ambiguous terms: if two values overlap, specify the tiebreaker
- Plain language, no jargon

**Section 3: Decision Tree**
```
Evaluate in order (stop at first match):
1. If [condition A] -> classify as [X]
2. If [condition B] AND [condition C] -> classify as [Y]
...
N. If none of the above -> classify as "unknown" with reason
```
Rules: exhaustive, ordered by priority, mutually exclusive, always ends with default.

**Section 4: Good vs Bad Examples**
Paired correct/incorrect examples with reasoning. Cover: happy path, edge cases, missing data, adversarial.

Show the WRONG answer and explain WHY it's wrong.

**Section 5: Output Format Contract**
Field-by-field spec:
```
- `field_name` (type): Description. Valid values: [...]. When to use each: [...]
- `confidence` (string): "high" | "medium" | "low"
  - high: Multiple clear signals confirm
  - medium: Some signals but ambiguity
  - low: Limited data, best guess
- `reasoning` (string): 1-2 sentences, key evidence only. No disclaimers.
```

**Section 6: Scope Constraints & Guardrails**
What NOT to do:
- Max pages to visit
- No form submission, no login
- No assumptions from domain name alone
- "If unsure, return unknown"
- Handle: site down, non-English, timeout, parked domain, SPA with no content

The "purple" sentinel: `If you cannot determine [field], return the exact string "purple"` (visually distinct, easy to filter, impossible to confuse with real data).

### Step 3: Build the Variable Block (Dynamic: bottom of the single prompt)

This is the tail of the single Claygent prompt. Keep the instructions portion under 200 words. All intelligence lives in the static block above.

Structure, in this exact order, appended directly after the static block:

```
## Task

[One sentence: what to do with the data below.]

## Instructions

1. [Step 1]
2. [Step 2]
3. [Step 3]
(3-5 max)

## Fallback

If [failure condition], return [fallback output].

## Output

Return JSON matching the schema.

---

## Row Data (select columns in Clay)

Company Name: {{Company Name}}
Company Website: {{Company Website}}
[additional variables as needed]
```

**CRITICAL: All `{{variables}}` MUST be in the "Row Data" section at the very bottom of the single prompt.** No variables anywhere else. This is what enables Clay API caching: everything above the Row Data section is identical across rows and gets cached.

### Step 4: Build JSON Schema

Clay-compliant JSON schema following OpenAI Structured Outputs rules:

1. Root = `{ "type": "object" }`
2. `"additionalProperties": false` on every object
3. All properties in `"required"` array
4. `"anyOf": [{"type": "string"}, {"type": "null"}]` for optional fields (NOT oneOf/allOf/not)
5. No validation keywords (no minLength, maxLength, minimum, maximum, pattern, format)
6. `"enum"` for fixed value sets
7. Arrays need explicit `"items"` definition
8. Nested objects need `additionalProperties: false` and full `required`
9. No `$ref` or `$defs`: inline everything
10. Max 5 levels of nesting

Schema must be directly pasteable into Clay's "Click JSON Schema" field.

### Step 5: Assemble & Output

Deliver the complete prompt package as a single copy-paste-ready output with clear section markers.

## Output Format

```
# Claygent Prompt: [Task Name]

◆ CONFIGURATION
- Complexity: [Simple / Medium / Advanced]
- Recommended model: [Claygent Neon / GPT-4 / Claude]
- Estimated credits/row: [Low / Medium / High]
- Input variables: [list of {{variables}} user must map in Clay]

◆ PROMPT (paste into Clay's single Claygent prompt field: one prompt, not split)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Static block from Step 2: identity, definitions, decision tree, examples, output contract, guardrails. NO {{variables}}]

[Task block from Step 3: task + instructions + fallback + output instruction. NO {{variables}}]

---
## Row Data (select columns in Clay)

[Variable]: {{Variable}}
[Variable]: {{Variable}}
...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

◆ JSON SCHEMA (paste into Clay "Click JSON Schema" field)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{
  [schema from Step 4]
}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

◆ CLAY SETUP NOTES
- Columns to create/map: [list with types]
- Conditional formula suggestion: [if applicable: skip rows missing key data]
- Cache behavior: Everything above the "Row Data" section is cached across all rows. Only {{variables}} are dynamic per row.
- Task type: [Text-only (no web browsing) / Web browsing]. Deliverable is always `Prompt + JSON Schema` regardless.
```

## Quality Checklist (Run Internally)

Before delivering, verify:

- [ ] Single unified prompt (NOT split into system + task: Claygent has one prompt field)
- [ ] Zero `{{variables}}` anywhere in the static block
- [ ] All `{{variables}}` grouped at the very bottom under "Row Data"
- [ ] Static block (everything above Row Data) exceeds **1,024 tokens** (required for OpenAI cached inputs)
- [ ] Decision tree is exhaustive (every input hits exactly one leaf)
- [ ] Default/unknown case exists
- [ ] Examples cover: happy path, edge case, missing data
- [ ] JSON schema passes all 10 OpenAI Structured Outputs rules
- [ ] Task prompt under 200 words (excluding Row Data section)
- [ ] "Purple" sentinel or equivalent for unfindable fields
- [ ] No generic AI preamble ("As a helpful AI...")
- [ ] Scope constraints include max page visits
