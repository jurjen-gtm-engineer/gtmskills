---
name: metaprompter
description: Use AI to improve AI prompts by asking what context is missing (Eric Nowoslawski)
metadata:
  version: "1.0"
---

# Metaprompter

You are applying Eric Nowoslawski's Metaprompter technique, using AI to improve AI prompts by asking what additional context, examples, or clarifications would help.

## Core Concept

Use metaprompter ('what do you need to improve this prompt?') (Idea credited to Eric Nowoslawski.)

Instead of guessing how to improve a prompt, ask the AI itself:
- What's unclear?
- What examples would help?
- What edge cases should be handled?

## Input

User provides:
- Current prompt that needs improvement
- Optionally: examples of poor outputs
- Optionally: specific issues they've noticed

## Process

1. **The Metaprompt**

   ```
   Here is a prompt I'm using for [TASK]:

   ---
   [YOUR CURRENT PROMPT]
   ---

   I want to improve this prompt's accuracy and consistency.

   Please analyze it and tell me:

   1. CLARITY: What parts of the instructions are ambiguous?

   2. MISSING CONTEXT: What background information would help
      you perform this task better?

   3. EXAMPLES NEEDED: What examples of input/output pairs
      would clarify my expectations?

   4. EDGE CASES: What scenarios might cause problems or
      inconsistent outputs?

   5. OUTPUT FORMAT: Is the expected output format clear?
      What would make it clearer?

   6. SAFEGUARDS: What fallback behaviors should be defined
      for missing/bad data?

   Then provide a REVISED PROMPT incorporating these improvements.
   ```

2. **Iterate Based on Feedback**

   After getting the metaprompt response:
   - Review suggested improvements
   - Add the examples it requested
   - Clarify the ambiguous parts
   - Define the edge case handling

3. **Output Format**

   ```
   ## Metaprompt Analysis

   ### Original Prompt
   [The prompt being improved]

   ### Issues Identified

   | Category | Issue | Suggested Fix |
   |----------|-------|---------------|
   | Clarity | [Issue] | [Fix] |
   | Context | [Issue] | [Fix] |
   | Examples | [Issue] | [Fix] |
   | Edge Cases | [Issue] | [Fix] |

   ### Improved Prompt

   ```
   [The revised, improved prompt]
   ```

   ### Key Improvements Made
   - [Improvement 1]
   - [Improvement 2]
   - [Improvement 3]
   ```

## Example

**Input:** Current prompt for company categorization

**Original Prompt:**
```
Tell me if this company is B2B or B2C based on their website.
```

**Metaprompt Analysis:**

### Issues Identified

| Category | Issue | Suggested Fix |
|----------|-------|---------------|
| Clarity | "Based on their website" is vague | Specify what to look for |
| Context | No definition of B2B vs B2C | Add clear definitions |
| Examples | No examples provided | Add 4-5 examples |
| Edge Cases | What about companies that do both? | Add BOTH category |
| Output Format | Just "tell me" is ambiguous | Specify exact format |
| Safeguards | No handling for unclear cases | Add fallback output |

### Improved Prompt

```
TASK: Classify {{company_name}} as B2B, B2C, or BOTH based on {{company_website}}.

DEFINITIONS:
- B2B: Primarily sells products/services to other businesses
- B2C: Primarily sells products/services to individual consumers
- BOTH: Significant revenue from both business and consumer customers

WHAT TO CHECK:
- Who is the target customer on the homepage?
- What does the pricing page target?
- Are there "Enterprise" or "Business" sections?
- Is there a consumer purchase flow?

EXAMPLES:
- salesforce.com → B2B (CRM for businesses)
- nike.com → B2C (sells shoes to consumers)
- amazon.com → BOTH (consumer marketplace + AWS for businesses)
- shopify.com → B2B (sells to businesses, even though those businesses are B2C)
- slack.com → B2B (team communication for companies)

OUTPUT:
- Return exactly one of: B2B, B2C, BOTH
- If website is inaccessible or unclear, return: UNABLE_TO_DETERMINE
- Do not explain or add commentary, just the classification
```

### Key Improvements Made
- Added clear definitions of categories
- Specified exactly what to look for
- Included diverse examples including edge cases
- Added BOTH category for mixed business models
- Defined safeguard output for unclear cases
- Specified exact output format

## When to Use Metaprompting

**Use When:**
- Prompt outputs are inconsistent
- Getting unexpected results
- Scaling up a prompt to more volume
- Creating a prompt for others to use
- Output quality isn't meeting standards

**Quick Metaprompt:**
```
What would you need to know to do this task better?
[YOUR PROMPT]
```

**Detailed Metaprompt:**
```
Analyze this prompt for:
1. Ambiguities
2. Missing context
3. Needed examples
4. Edge cases
5. Output format clarity
6. Safeguards needed

Then provide an improved version.

[YOUR PROMPT]
```

## Iterative Improvement

For important prompts, iterate:

**Round 1:** Get initial improvements
**Round 2:** Test improved prompt, note failures
**Round 3:** Metaprompt again with failure examples
**Round 4:** Test and refine

```
Here's my prompt and some examples where it failed:

PROMPT: [Current version]

FAILURES:
- Input: [X], Expected: [Y], Got: [Z]
- Input: [A], Expected: [B], Got: [C]

How should I modify the prompt to handle these cases?
```

## Related Skills

- `/prompt-engineering-rules` - Full prompting framework
- `/icp-scoring-dynamic` - Complex prompts to improve
- `/plg-company-detection` - Example well-crafted prompt
- `/product-complexity-detection` - Another example

## Credits

The metaprompter technique is taught by Eric Nowoslawski ([Growth Engine X](https://github.com/growthenginenowoslawski/coldoutboundskills)). The prompts and wording here are ours.

---

Examples are illustrative. Company names, prices and numbers in them are placeholders or may be out of date, so check the live source before you rely on any detail.
