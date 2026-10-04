---
name: prompt-engineering-rules
description: Eric Nowoslawski's 5 rules for efficient AI prompts in Clay workflows
metadata:
  version: "1.0"
---

# AI Prompt Engineering Rules

You are applying Eric Nowoslawski's five rules for efficient AI prompts, critical for running AI at scale in Clay workflows without wasting credits or getting bad outputs.

## Context

These rules come from Eric Nowoslawski of Growth Engine X, who runs enrichment prompts at very high volume.

At scale, prompt quality directly impacts:
- Credit costs (bad prompts = wasted runs)
- Output quality (unclear prompts = unusable results)
- Filtering effort (no safeguards = manual cleanup)

## The 5 Rules

### Rule 1: 10-Minute Manual Research Rule

Only automate what you'd actually look up manually.

**Principle:** If you wouldn't spend 10 minutes researching this manually, don't ask AI to do it.

**Why It Matters:**
- AI research has costs (credits, latency)
- If the data isn't worth manual effort, it's not worth automated effort
- Prevents "nice to have" data bloat

**Application:**
```
Before adding an AI enrichment, ask:
- Would I manually research this for a prospect?
- Would this data change my approach?
- Is this worth 10 minutes per company?

If no → Don't automate it
If yes → Proceed to build the prompt
```

### Rule 2: One Task Per Prompt

Have AI do one thing at a time. Break out enrichment and classification steps.

**Principle:** Each prompt should accomplish exactly one task.

**Why It Matters:**
- Multi-task prompts have lower accuracy
- Harder to debug when something fails
- Can't conditionally run parts

**Bad (Multi-task):**
```
Find the company's tech stack, determine if they're PLG,
score their ICP fit, and write a personalized opening line.
```

**Good (Single-task):**
```
Prompt 1: Identify technologies used (tech_stack)
Prompt 2: Is this a PLG company? (plg_status) [uses tech_stack]
Prompt 3: Calculate ICP score (score) [uses tech_stack, plg_status]
Prompt 4: Write opening line (opening) [uses score, relevant data]
```

### Rule 3: Safeguards in Prompts

Output 'purple' for missing data. Reliably filter errors later.

**Principle:** Define explicit outputs for when data is missing or uncertain.

**Why It Matters:**
- AI will hallucinate if not told to abstain
- Consistent error outputs enable filtering
- Easier to spot-check quality

**Implementation:**
```
[Your prompt here]

IMPORTANT:
- If the information cannot be found, return exactly: "NOT_FOUND"
- If you are uncertain, return exactly: "UNCERTAIN"
- Do not guess or make assumptions
- Do not return empty strings
```

**Why "Purple":** Any distinctive, filterable string works. Eric uses "purple" because:
- It's visually obvious in data review
- Easy to filter in Clay/spreadsheets
- Never appears in real data

### Rule 4: Examples in Prompts

Give AI plenty of examples. Use metaprompter ('what do you need to improve this prompt?')

**Principle:** Show, don't just tell. Include examples of desired output.

**Why It Matters:**
- Examples calibrate AI understanding
- Reduces ambiguity
- Improves consistency across runs

**Implementation:**
```
Determine if this company is B2B or B2C based on their website.

Examples:
- Salesforce.com → B2B (sells to businesses)
- Nike.com → B2C (sells to consumers)
- Shopify.com → B2B (sells to businesses who sell to consumers)
- Amazon.com → B2C (primarily consumer marketplace)

Now analyze: {{company_website}}
Return: B2B, B2C, or BOTH
```

**Metaprompter Technique:**
```
Here's my prompt: [YOUR PROMPT]

What additional context, examples, or clarifications would
help you produce better results for this task?
```

### Rule 5: Chain of Thought

For complex prompts, ask AI to explain its reasoning before answering to improve accuracy.

**Principle:** Have AI show its work before giving the final answer.

**Why It Matters:**
- Reasoning improves accuracy
- Makes errors debuggable
- Better for complex classifications

**Implementation:**
```
Determine if this company would benefit from our solution.

Company: {{company_name}}
Data: {{enriched_data}}

First, explain your reasoning:
- What does this company do?
- What signals indicate they might need [solution type]?
- What signals indicate they might NOT need it?

Then provide your conclusion:
- FIT: High / Medium / Low
- KEY_REASON: [One sentence]
```

## Putting It All Together

**Well-Engineered Prompt:**
```
TASK: Determine if {{company_name}} is a PLG (product-led growth) company.

CONTEXT: Check their website at {{company_website}} for self-serve signup,
free trials, or freemium tiers.

EXAMPLES:
- Notion.so → PLG (free tier, self-serve signup)
- Salesforce.com → NOT_PLG (contact sales required)
- HubSpot.com → HYBRID (free tools + sales motion)

REASONING: Before answering, note:
1. Is there a "Sign up free" or "Start trial" button?
2. Is pricing publicly available?
3. Can you access the product without talking to sales?

OUTPUT:
- Return: PLG, NOT_PLG, or HYBRID
- If website is unavailable or unclear, return: UNABLE_TO_DETERMINE
```

## Anti-Patterns to Avoid

| Anti-Pattern | Problem | Fix |
|--------------|---------|-----|
| Vague prompts | AI guesses intent | Be specific |
| Multi-task prompts | Lower accuracy | One task per prompt |
| No examples | Inconsistent output | Add 3-5 examples |
| No safeguards | Hallucinations | Define fallback outputs |
| No reasoning | Mysterious errors | Add chain of thought |

## Related Skills

- `/metaprompter` - Prompt improvement technique
- `/data-point-research` - Custom signals to detect
- `/icp-scoring-dynamic` - Complex scoring prompts
- `/plg-company-detection` - Example well-engineered prompt

## Credits

The five rules are taught by Eric Nowoslawski ([Growth Engine X](https://github.com/growthenginenowoslawski/coldoutboundskills)). The explanations and examples here are ours.

---

Examples are illustrative. Company names, prices and numbers in them are placeholders or may be out of date, so check the live source before you rely on any detail.
