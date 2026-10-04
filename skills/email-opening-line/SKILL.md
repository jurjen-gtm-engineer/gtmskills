---
name: email-opening-line
description: Generate personalized email opening lines that hook with relevance
metadata:
  version: "1.0"
---

# Email Opening Line Generation

You are generating personalized opening lines for cold emails that hook with genuine relevance.

## Core Principles

The first line should continue from the subject's context and flatter or connect.

**Effective Patterns:**
- "Just read your [post/article] on X..."
- "Just listened to your interview about Y..."
- "Noticed [Company] recently [achievement]..."

## Input

User provides:
- Prospect name and company
- Subject line (to avoid repetition)
- Research insight being referenced
- Optionally: campaign angle

## Process

1. **Connect to Subject**

   The opening must:
   - Continue the subject's thread
   - Add NEW value (not repeat subject)
   - Feel like natural continuation

2. **Generate Opening Line**

   **Prompt Pattern:**
   ```
   Given this subject line: [SUBJECT]
   And this research: [INSIGHT]

   Write ONE opening sentence that:
   - Starts with "Just read..." or "Noticed..." or similar
   - References the specific content/insight
   - Includes a genuine compliment or observation
   - Doesn't repeat the exact words from subject
   - Is 15-25 words

   The subject introduces the topic; the opening line shows you actually engaged with it.
   ```

3. **Output Format**

   ```
   Subject: [The subject line]
   Research Used: [What we're referencing]

   Opening Line:
   "[Generated opening sentence]"

   Why It Works:
   - [Reason 1]
   - [Reason 2]

   Transition to Body:
   "[Opening line] [Bridge sentence to value prop]..."
   ```

## Examples

**Input:**
- Subject: "Your insights on remote work"
- Research: Sarah's interview on TechCrunch about team culture in hybrid settings
- Angle: Our tool helps remote teams stay aligned

**Output:**
```
Subject: Your insights on remote work
Research Used: TechCrunch interview about hybrid team culture

Opening Line:
"Just read your TechCrunch interview, your point about 'culture not requiring a room' really resonated with how we think about distributed teams."

Why It Works:
- Shows I read the actual interview (not just saw headline)
- Quotes something specific (proves engagement)
- Connects to a shared perspective (builds rapport)

Transition to Body:
"Just read your TechCrunch interview, your point about 'culture not requiring a room' really resonated with how we think about distributed teams. I'm curious how you're handling [specific challenge]..."
```

**Input:**
- Subject: "Scaling after Series B"
- Research: Company announced $30M Series B last week, CEO quoted about "aggressive hiring"
- Angle: We help onboard engineers at scale

**Output:**
```
Subject: Scaling after Series B
Research Used: Series B announcement, CEO quote on hiring

Opening Line:
"Congrats on the $30M round, saw the CEO mention 'aggressive hiring' and figured you're about to feel the growing pains of scaling an engineering org."

Why It Works:
- Timely congratulations (everyone likes recognition)
- Quotes specific detail (proves I did research)
- Empathizes with upcoming challenge (relevant hook)

Transition to Body:
"Congrats on the $30M round, saw the CEO mention 'aggressive hiring' and figured you're about to feel the growing pains of scaling an engineering org. When we hit that stage, onboarding became our biggest bottleneck..."
```

## Critical Rules

1. **Never Repeat Subject Exactly**
   - Subject: "Your async video approach"
   - BAD opener: "I saw your async video approach..."
   - GOOD opener: "Just read your post about replacing standups with video updates, that's exactly what we did last year."

2. **Include Specific Detail**
   - BAD: "Loved your recent post"
   - GOOD: "Loved your point about 'context over control' in your Tuesday post"

3. **Be Genuine**
   - Only compliment if you mean it
   - Observation is better than empty flattery

## Related Skills

- `/email-subject-line` - What comes before
- `/linkedin-posts-summary` - Find content details
- `/recent-news` - Company news for reference
- `/role-focus` - Role-appropriate angles

---

Examples are illustrative. Company names, prices and numbers in them are placeholders or may be out of date, so check the live source before you rely on any detail.
