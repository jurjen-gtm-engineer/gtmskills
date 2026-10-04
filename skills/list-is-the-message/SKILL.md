---
name: list-is-the-message
description: Build segments where the "why" is so clear that messaging writes itself (Jordan Crawford)
metadata:
  version: "1.0"
---

# List Is the Message

You are applying Jordan Crawford's "List Is the Message" methodology, building segments where knowing WHY someone is on the list makes the messaging self-evident.

## Core Philosophy

By understanding 'why' a lead is on the list, messaging becomes self-evident and deeply personalized.

Traditional approach: Build list → Write generic messaging → Try to personalize
List Is the Message: Define tension → Build list around it → Messaging is obvious

## Input

User provides:
- Target segment or ICP
- Pain point or opportunity to address
- Available data sources

## Process

1. **Define the Tension**

   **Prompt Pattern:**
   ```
   For this segment: [DESCRIPTION]
   And this pain point: [PAIN]

   What specific, detectable event or situation would indicate this pain is ACTIVE right now?

   The tension must be:
   - Specific enough that we know exactly why they qualify
   - Detectable through data/research
   - Directly tied to the problem we solve
   ```

2. **Build the List Criteria**

   ```
   Now define the list:

   WHO: [Base firmographic criteria]
   PLUS: [Tension signal 1]
   PLUS: [Tension signal 2]

   This combination means everyone on the list is experiencing [specific pain] because [specific reason].
   ```

3. **Extract the Self-Evident Message**

   ```
   For someone on this list, complete this sentence:

   "We're reaching out because we noticed [tension signal], which usually means [pain they're experiencing]. [Value prop]..."

   The message should feel like it writes itself because the "why" is so clear.
   ```

4. **Output Format**

   ```
   ## List Is the Message: [Segment Name]

   ### The Tension

   [Specific event/situation being targeted]

   ### List Criteria

   **Base:** [Firmographics]
   **Tension Signals:**
   - [Signal 1] - indicates [pain]
   - [Signal 2] - indicates [pain]

   ### The Self-Evident Message

   Because we know WHY they're on this list, the opening writes itself:

   "[Opening that directly addresses the tension]"

   ### Why This Works

   - Personalization is substantive, not cosmetic
   - The "why you, why now" is obvious
   - No AI invention needed, just adaptation

   ### Channel Adaptations

   **Email:** [Version]
   **LinkedIn:** [Version]
   **Cold call opener:** [Version]
   ```

## Example

**Input:** "We sell compliance automation. Target is SaaS companies that just got enterprise customers and now face SOC 2 requirements."

**Output:**
```
## List Is the Message: First Enterprise Customer

### The Tension

SaaS companies that recently closed their first enterprise deal and are now facing compliance requirements they've never dealt with before.

### List Criteria

**Base:** SaaS company, 50-500 employees, B2B
**Tension Signals:**
- Added enterprise logo to website in last 90 days
- Posted SOC 2 or compliance-related job opening
- No CISO or security leader on LinkedIn

### The Self-Evident Message

Because we know WHY they're on this list, the opening writes itself:

"Congrats on landing [Enterprise Customer], I'm guessing the security questionnaire was a wake-up call. Most teams at your stage scramble to get SOC 2 ready while trying not to slow down product..."

### Why This Works

- We know the EXACT trigger (enterprise customer)
- We know the EXACT pain (compliance requirements)
- We know the EXACT timing (it's happening now)

### Channel Adaptations

**Email:** "Congrats on landing [Customer], I'm guessing their security questionnaire was a wake-up call..."

**LinkedIn:** "Saw you just added [Customer] to your customer page. Big milestone! Curious how you're handling the compliance requirements that usually come with enterprise deals..."

**Cold call:** "Hi [Name], I noticed [Company] just landed [Customer], congrats. Quick question: are you handling the SOC 2 requirements in-house or looking for help?"
```

## Key Principles

1. **The Why Must Be Specific**: "Growing companies" is not a tension. "Just raised Series B and has 15 open engineering roles" is.

2. **Messaging Is Adaptation, Not Invention**: AI's role is to reformat the message for channels, not create the core insight.

3. **Every List Member Gets the Same Core Message**: Because they share the same tension, the core message applies to all, only details change.

## Related Skills

- `/pain-qualified-segment` - Define the tension heuristics
- `/data-point-research` - Find detectable signals
- `/permissionless-value-proposition` - Lead with value
- `/email-opening-line` - Channel adaptation

## Credits

"The list is the message" is Jordan Crawford ([Blueprint GTM](https://blueprintgtm.com))'s idea. The prompts and wording here are ours.

---

Examples are illustrative. Company names, prices and numbers in them are placeholders or may be out of date, so check the live source before you rely on any detail.
