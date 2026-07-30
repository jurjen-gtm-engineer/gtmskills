---
name: battlecard-builder
description: Build competitive battlecards in 30 minutes using AI-powered research and a 3-type framework (Core Competitor, Quick Reference, Objection Handler). Battlecards that are simple, current, and actually get used mid-call.
---

# Skill: Battlecard Builder

## Purpose

Build competitive battlecards in 30 minutes using AI-powered research and a 3-type framework. Battlecards that are simple, current, and actually get used mid-call.

## Inputs

- **Your company name** (required)
- **Competitor name** (required)
- **Your solution:** 2-3 sentences
- **Their solution:** 2-3 sentences
- **Typical buyer:** Role, company size, main concerns
- **Win/loss context** (optional): Why you won/lost last 3 deals against them

## The 3 Essential Battlecard Types

### Type 1: Core Competitor Battlecard
**Use for:** Competitive deals, prep, and onboarding.

Sections:
- **Company Snapshot:** Who they are, who they serve, how they're positioned (2-3 sentences)
- **Pricing Intelligence:** Per-user pricing, add-ons, hidden costs, contract terms
- **Top 5 Competitor Strengths:** What they genuinely win on
- **Top 5 Competitor Weaknesses:** Where they underperform (implementation time, UI complexity, TCO, support, contract rigidity)
- **Discovery Questions:** Questions that spotlight your edge ("How quickly do you need to see ROI?", "What's your rollout timeline?", "Had issues with past vendors?")
- **Common Objections + Responses:** Acknowledge concern in 2 sentences, then redirect with a question
  - "They have more features" → "They do, but most teams use 10-15. Which features actually matter for your team?"
  - "They're the industry standard" → "They are for many. But what critical features is the industry missing today?"
  - "They're cheaper" → "Totally. But what's the total cost including add-ons, implementation, and customization?"
  - "Our leadership prefers them" → "What is often overlooked is dedicated teams for specific niches. What would it take for your team to feel confident switching?"
  - "They integrate with everything" → "Long list, but do their integrations truly plug-and-play with your tech stack?"
  - "We've already signed a contract" → "I wish you the best. Out of curiosity, what's the plan if things don't go as expected in the first few months?"
- **Proof Points:** Short, sticky success stories with specific outcomes

### Type 2: Quick Reference Card
**Use for:** Discovery calls, when a competitor comes up unexpectedly.

Sections:
- **3 Key Differentiators:** Short, punchy phrases
- **3 Discovery Questions:** Reveal where competitor struggles
- **1 Memorable Proof Point:** Results, timeline, or brand
- **30-Second Positioning:** Quick contrast statement

### Type 3: Objection Handler
**Use for:** When common objections come up during calls.

Sections:
- **Top 5 Competitor Weaknesses:** Exact words prospects use (no polishing)
- **Natural 2-Sentence Responses:** Acknowledge concern, redirect with question
- **Redirect Questions:** Shift from defending to discovering
- **Supporting Proof Points:** Stats, quotes, or examples (under 50 words each)

## Process

### Minutes 0-10: Gather Intel

Collect quickly (use web search):
- Competitor's main website claim and positioning
- Their pricing structure
- Why you lost the last 3 deals to them (one sentence each)
- Why you won the last 3 deals against them (what tipped it)
- Their latest product update or announcement

### Minutes 10-20: Run Core Prompts

**Foundation Builder:** Generate 5 differentiators, 6 objections with natural responses, 3 questions exposing weaknesses, proof points for each differentiator.

**Weakness Finder (Insight Chain):**
1. Find 3 non-obvious weaknesses customers discover after purchasing (focus on implementation, scalability, support)
2. Convert weaknesses into discovery questions (curious, not aggressive)
3. Build proof points for each weakness (under 50 words)

**Scenario-Specific Prompts:**
- **Price objections:** Hidden costs, ROI comparison, value-shift question, customer story
- **Feature comparisons:** Quality vs quantity, feature adoption question, time-to-value, complexity concerns
- **Incumbent situations:** Common pain points after year 2, migration path, renewal question, switch success story

### Minutes 20-30: Strengthen Weak Spots

Review the battlecard for gaps. Run targeted prompts:
- Missing proof points → "Generate 3 specific proof points for [differentiator]"
- Weak objection responses → "Strengthen this response: [paste]. Acknowledge concern, redirect to strength."
- Need better questions → "Create 3 discovery questions that identify if a prospect will struggle with [competitor weakness]"
- Polish language → "Make these responses conversational. Remove corporate speak. Keep under 40 words. Add redirect question. Include specifics."

## Maintenance: 2-Week Refresh Cycle

**Week 1 Check (15 min):**
- What objection had no good answer?
- What competitor claim surprised you?
- What worked well?

**Week 2 Update (15 min):**
Run the Update Engine prompt with:
- Recent losses and reasons
- New competitor changes
- Field feedback on what's working/not
- Current battlecard content

### The 3 Failure Points (Why Battlecards Die)
1. **Created in isolation:** no input from people actually selling
2. **Never updated:** market changes, battlecard doesn't
3. **Too complex:** information overload on a single card kills usage

**The Update Rule:** If your battlecards are over 3 months old without updates, they're hurting more than helping.

### ROI Math
- 30 minutes to create, 15 minutes bi-weekly to maintain
- Even 10% improvement in competitive win rate = significant revenue
- Example: $50K avg deal, 10 competitive deals/month, 30% win rate → 40% with battlecards = 1 extra deal/month = $600K annual impact

## Output

**Save to:** `outputs/[company]-vs-[competitor]-battlecard.md` (relative to your working directory)

## Notes

Discovery questions in this skill pair well with the SPICED discovery framework (Situation, Pain, Impact, Critical Event, Decision): use the battlecard's discovery questions to surface Pain and Impact tied to the competitor's weaknesses.
