---
name: email-subject-line
description: Generate personalized email subject lines under 8 words using prospect research
metadata:
  version: "1.0"
---

# Email Subject Line Generation

You are generating personalized email subject lines using research data about the prospect.

## Core Principles

Keep subject under 8 words, in second person ('your'/'you'), and reference something relevant.

**Why Snippets Work:**
- AI drifts with long outputs
- One sentence = better quality control
- Easier to enforce constraints

## Input

User provides:
- Prospect's name and/or company
- Research insight (recent post, news, company context)
- Campaign angle or value prop

## Process

1. **Identify Personalization Hook**

   What makes this subject relevant to THIS person?
   - Their content (post, article, podcast)
   - Company news (funding, launch, hire)
   - Role-specific angle
   - Shared context (industry, challenge)

2. **Generate Subject Options**

   **Prompt Pattern:**
   ```
   Create 3 email subject lines for [Prospect] at [Company].

   Context: [Research insight]
   Campaign angle: [What we're reaching out about]

   Rules:
   - Maximum 7 words
   - Use "your" or "you" (second person)
   - Reference the specific insight
   - No clickbait or misleading

   Examples of good patterns:
   - "Your insights on [topic]"
   - "Your [Company]'s [recent thing]"
   - "Quick thought on [their content]"
   - "For [Company]'s [initiative]"
   ```

3. **Output Format**

   ```
   Prospect: [Name] at [Company]
   Hook: [What we're referencing]

   Subject Line Options:

   1. [Subject] - [Why this works]
   2. [Subject] - [Why this works]
   3. [Subject] - [Why this works]

   Recommended: [#X] because [reason]

   Full Email Preview:
   Subject: [Recommended subject]
   Preview text hint: [First line that complements subject]
   ```

## Examples

**Input:**
- Prospect: Sarah Chen, VP Sales at TechCorp
- Research: Posted about remote sales management, mentioned async video
- Angle: Our tool helps with async sales communication

**Output:**
```
Prospect: Sarah Chen at TechCorp
Hook: Her LinkedIn post about async video for sales teams

Subject Line Options:

1. "Your async video approach" - Direct reference to her content
2. "Your take on remote sales" - Broader topic she cares about
3. "For TechCorp's distributed team" - Company-specific

Recommended: #1 because it's most specific to her actual content

Full Email Preview:
Subject: Your async video approach
Preview text hint: "Just read your post about replacing standups with async video..."
```

**Input:**
- Prospect: Mike Johnson, CTO at FinanceApp
- Research: Company just raised Series B, hiring heavily for engineering
- Angle: We help scale engineering teams

**Output:**
```
Prospect: Mike Johnson at FinanceApp
Hook: Recent Series B and engineering hiring surge

Subject Line Options:

1. "Scaling after Series B" - References their stage
2. "Your engineering growth" - Direct to his priority
3. "FinanceApp's next 10 engineers" - Specific and company-focused

Recommended: #2 because it speaks to his direct responsibility

Full Email Preview:
Subject: Your engineering growth
Preview text hint: "Congrats on the Series B - saw you're hiring 15+ engineers..."
```

## Anti-Patterns

**Don't:**
- "Quick question" (too generic)
- "Can we chat?" (no value)
- "I'd love to..." (self-focused)
- "[Company] + [Your Company]" (feels salesy)
- ALL CAPS or excessive punctuation

**Do:**
- Reference their world, not yours
- Be specific to THIS person
- Create curiosity without clickbait
- Sound like a human, not a marketer

## Related Skills

- `/linkedin-posts-summary` - Find content to reference
- `/recent-news` - Company news for hooks
- `/email-opening-line` - What comes after subject
- `/role-focus` - Role-specific angles

---

Examples are illustrative. Company names, prices and numbers in them are placeholders or may be out of date, so check the live source before you rely on any detail.
