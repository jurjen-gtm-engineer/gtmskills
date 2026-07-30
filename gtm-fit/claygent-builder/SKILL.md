---
name: claygent-builder
description: Generate production-ready Claygent configurations (system prompt + task prompt + JSON schema + examples), test them via Clay webhook, and iterate until quality hits 8.0+
---

# Skill: Claygent Builder

## Purpose

Generate production-ready Claygent configurations (system prompt + task prompt + JSON schema + examples), test them via Clay webhook, and iterate until quality hits 8.0+. Replaces manual prompt-test-rewrite cycles with a structured loop.

**This is a standalone skill**: not part of any sequential workflow. Invoke independently.

## Inputs

- **Task description** (required): What the Claygent should do (e.g., "Classify whether a company is B2B SaaS from their website")
- **Clay webhook URL** (required for testing): The webhook URL from a Clay table set up for testing
- **Input variables** (required): What data Clay sends per row (e.g., company domain, company name)
- **Output fields** (required): What structured data the Claygent should return
- **Test domains/data** (optional): If not provided, auto-generated in Step 8
- **Model preference** (optional): Claygent Neon (default), GPT-4, or Claude

## Process

### Step 1: Webhook Setup

**This step is BLOCKING: cannot proceed to testing without it.**

Ask the user for their Clay webhook URL. Explain the setup if needed:

1. User creates a Clay table with **Webhook** as the source
2. User copies the webhook URL from Clay
3. User pastes the webhook URL into Claude Code

Start the local webhook listener for receiving Clay's callback results (`webhook-listener.py` lives in this skill's folder):

```bash
python3 webhook-listener.py &
```

If ngrok is available, start a tunnel to expose the listener:
```bash
ngrok http 8765
```

The public ngrok URL becomes the `callback_url` sent to Clay in each test batch.

**Fallback (no ngrok or tunnel):** Poll for results via Clay's API/MCP tools, or ask the user to manually copy results from the Clay UI.

Reference: `clay-test-template.md` (in this skill's folder) for detailed Clay table setup instructions.

### Step 2: Native Integration Check

**This step is BLOCKING: if a native integration solves the task, stop here.**

Check if Clay's 150+ native integrations or existing Claybooks already solve this task without needing a Claygent. Native integrations are:
- Cheaper (no AI credits)
- Faster (direct API calls)
- More reliable (structured APIs vs web scraping)

**Decision:**
- If a native integration solves it completely: recommend that instead, stop here
- If a native integration solves part of it: recommend hybrid approach (native + Claygent for the gap)
- If no native integration applies: proceed to Step 3

### Step 3: Classify Complexity

Classify the task:

| Complexity | Criteria | Example Count |
|------------|----------|---------------|
| **Simple** | Binary yes/no, single field extraction, one page visit | 3 examples |
| **Medium** | Multi-field extraction, classification with reasoning, 2-3 page visits | 5 examples |
| **Advanced** | Multi-step research, conditional logic, multiple sources, chain of thought | 10 examples |

Also determine:
- **Recommended model**: Claygent Neon (default), GPT-4 (complex reasoning), Claude (nuanced classification)
- **Estimated credits per row**: based on complexity and expected page visits
- **Expected fields**: list all output fields with types

### Step 4: Generate System Prompt

Build the system prompt with exactly 6 sections:

**Section 1: Identity + Scope**
- Specific role statement (not generic "helpful AI")
- Bounded capabilities (what this agent does and nothing else)
- 2-3 sentences maximum

**Section 2: Definitions**
- Every classification value defined with concrete criteria
- No ambiguous terms: if two values could overlap, specify the tiebreaker
- Use plain language, not jargon

**Section 3: Decision Tree**
- Exhaustive if/then logic
- Ordered by priority (most common/clear cases first)
- Every possible input hits exactly one leaf
- Always ends with a default/unknown case

**Section 4: Good vs Bad Examples**
- Paired correct/incorrect examples with reasoning
- Cover: happy path, edge cases, missing data
- Show the WRONG answer and explain WHY it's wrong

**Section 5: Output Format Contract**
- Field-by-field spec matching the JSON schema
- Valid values for each enum field with when-to-use criteria
- Confidence level definitions (high/medium/low)

**Section 6: Scope Constraints**
- What NOT to do (max pages, no form submission, no assumptions from domain name alone)
- Classify vs unknown boundary
- "If unsure, return unknown": false confidence is worse than admitting uncertainty

### Step 5: Generate Task Prompt

Keep SHORT: under 200 words. All intelligence lives in the system prompt.

Structure:
1. **Task statement**: one sentence describing what to do
2. **Input variables**: `{{Company Website}}`, `{{Company Name}}`, etc. (Clay template syntax)
3. **Instructions**: 3-5 numbered, specific steps
4. **Fallback behavior**: one sentence for when things go wrong
5. **Output instruction**: "Return JSON matching the schema."

### Step 6: Generate JSON Schema

Build a Clay-compliant JSON schema following OpenAI Structured Outputs rules. Validate against ALL 10 rules before outputting:

1. Root = `{ "type": "object" }`
2. `"additionalProperties": false` on every object
3. All properties in `"required"` array
4. `"anyOf": [{"type": "string"}, {"type": "null"}]` for optional fields (NOT oneOf/allOf/not)
5. No validation keywords (no minLength, maxLength, minimum, maximum, pattern, format)
6. `"enum"` for fixed value sets
7. Arrays need explicit `"items"` definition
8. Nested objects also need `additionalProperties: false` and full `required`
9. No `$ref` or `$defs`: inline everything
10. Maximum 5 levels of nesting

The schema must be directly pasteable into Clay's "Click JSON Schema" field: no wrapping, no modification.

### Step 7: Generate Examples

Generate input/output pairs based on complexity (3/5/10 from Step 3).

Each example must include:
- **Input:** The exact data Clay would send (domain, company name, etc.)
- **Expected output:** The exact JSON matching the schema
- **Reasoning:** Why this is the correct output (2-3 sentences)
- **Edge case tested:** What boundary this example covers

Coverage requirements:
- Clear positives (unambiguous matches)
- Clear negatives (unambiguous non-matches)
- Edge cases (ambiguous inputs that test decision tree boundaries)
- Missing data (what happens when key info is unavailable)
- Adversarial (inputs designed to confuse, e.g., marketing copy that mimics a different category)

### Step 8: Source Test Domains

If the user provided test data, use that. Otherwise, auto-generate a balanced test batch:

- **3-4 clear positives**: companies that obviously match the classification
- **2-3 clear negatives**: companies that obviously don't match
- **2-3 edge cases**: ambiguous companies that test decision boundaries

Use web search to find appropriate companies if the task domain is niche.

For each test domain, note the **expected classification** (ground truth) so results can be scored.

### Step 9: Test via Clay Webhook

**This step is BLOCKING: must achieve 8.0+ quality score.**

Send test batch to Clay webhook via `curl`:

```bash
curl -X POST "CLAY_WEBHOOK_URL" \
  -H "Content-Type: application/json" \
  -d '{
    "domain": "example.com",
    "prompt": "[full task prompt with variables resolved]",
    "prompt_version": "v1",
    "callback_url": "NGROK_URL/results",
    "json_schema": { ... }
  }'
```

Send one request per test domain. Wait for Clay to process (Claygent takes 1-5 minutes per row).

Read results from `./clay-results/*.json` (written by the webhook listener).

Score each result on the 7-criterion rubric:

| # | Criterion | Weight | Score |
|---|-----------|--------|-------|
| 1 | Accuracy | 25% | Compare to expected ground truth |
| 2 | Consistency | 20% | Same logic applied across all test rows? |
| 3 | Completeness | 15% | All fields populated correctly? |
| 4 | Edge case handling | 15% | Graceful handling of ambiguous/missing data? |
| 5 | Reasoning quality | 10% | Does reasoning match classification? |
| 6 | Schema compliance | 10% | Output matches JSON schema exactly? |
| 7 | Cost efficiency | 5% | Minimal pages visited? |

Calculate weighted average. Decision:
- **< 8.0**: MUST iterate (proceed to Step 10)
- **8.0 - 8.9**: SHOULD iterate (optional, recommend if easy wins exist)
- **9.0+**: STOP, production-ready

### Step 10: Iterate

Analyze the Clay output, focusing on **agent steps** (where it navigated, what it read, where it went wrong).

Common failure patterns and fixes:

| Failure | Fix |
|---------|-----|
| Wrong page visited | Add navigation instructions: "Visit /pricing first, then /about" |
| Timeout on JS-heavy sites | Add constraint: "If homepage doesn't load in 30s, classify from domain + meta tags" |
| Misclassification on edge case | Add specific example for that edge case in Section 4 |
| Missing field | Add explicit instruction for that field in the decision tree |
| Inconsistent confidence | Tighten confidence definitions in Section 5 |
| Non-English site mishandled | Add guardrail: "For non-English sites, use visual signals (pricing layout, business imagery)" |

**Bump prompt version** and update changelog:
```
v1: Initial prompt, generated from task description
v2: Fixed: [specific issue found in test results]
v3: Added: [specific improvement based on agent step analysis]
```

Re-send to Clay webhook with updated prompt. Max 3 iterations.

If after 3 iterations the score is still below 8.0, report the persistent issues and recommend:
- Breaking the task into simpler sub-tasks (multiple Claygent columns)
- Switching models (e.g., Neon to GPT-4 for complex reasoning)
- Adding pre-enrichment steps (native integrations) to reduce what Claygent must figure out

## Output

Save final deliverable to `outputs/claygent-[task-slug].md` (e.g., `outputs/claygent-b2b-saas-qualification.md`).

### Deliverable Structure

```
# Claygent: [Task Name]
## Built with Claygent Builder

◆

## Native Integration Check
[Result: Claygent required / hybrid approach / native sufficient]
[If hybrid: which native integrations supplement the Claygent]

◆

## Configuration Summary
- **Complexity:** [Simple / Medium / Advanced]
- **Model:** [Claygent Neon / GPT-4 / Claude]
- **Credits/row:** [Estimate]
- **Quality score:** [Final rubric score] (v[N], [N] iterations)
- **Test results:** [X/Y correct on test batch]

◆

## System Prompt
[Copy-paste ready for Clay's system prompt field]

◆

## Task Prompt
[Copy-paste ready for Clay's Claygent prompt field]

◆

## JSON Schema
[Copy-paste ready for Clay's "Click JSON Schema" field, exact Clay-compliant format]

◆

## Examples ([3/5/10])

### Example 1: [Description]
**Input:** [domain / company data]
**Expected Output:**
```json
{ ... }
```
**Reasoning:** [Why this is correct]
**Edge case tested:** [What boundary this covers]

[Repeat for all examples]

◆

## Test Results

### Rubric Scores (v[final])
| Criterion | Weight | Score | Notes |
|-----------|--------|-------|-------|
| Accuracy | 25% | X.X | ... |
| Consistency | 20% | X.X | ... |
| Completeness | 15% | X.X | ... |
| Edge case handling | 15% | X.X | ... |
| Reasoning quality | 10% | X.X | ... |
| Schema compliance | 10% | X.X | ... |
| Cost efficiency | 5% | X.X | ... |
| **Weighted Total** | **100%** | **X.X** | |

### Per-Domain Results
| Domain | Expected | Got | Correct? | Notes |
|--------|----------|-----|----------|-------|
| ... | ... | ... | ... | ... |

### Version History
[Changelog from v1 to final version]

◆

## Deployment Notes
- **Test protocol:** Run on 10 new rows before scaling. Check accuracy > 80%.
- **Conditional logic:** [Any Clay formula conditions to add, e.g., skip rows without website]
- **Known limitations:** [Edge cases that remain, cost considerations]
- **Scaling notes:** [Credit estimates at 100/1000/10000 rows]
```
