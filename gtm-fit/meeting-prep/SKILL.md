---
name: meeting-prep
description: Pre-call research agent that produces a structured brief for any sales meeting. Combines web research with SPICED discovery prep and 6 non-negotiable discovery questions, customized per contact and company.
---

# Skill: Meeting Prep Agent

## Purpose

Pre-call research agent that produces a structured brief for any sales meeting. Combines web research with SPICED discovery methodology (Situation, Pain, Impact, Critical Event, Decision) and 6 non-negotiable discovery questions.

## Inputs

- **Company name** (required)
- **Contact name and title** (required)
- **Meeting type:** Discovery / Demo / Follow-up / Expansion
- **Your company context** (optional): What you sell, ICP summary, key differentiators
- **Battlecard** (optional): If competing against a specific vendor

## Process

### 1. Company Research

Use web search to gather:
- What they do, who they serve, business model
- Recent news or developments (funding, hiring, product launches, exec changes)
- Company size, revenue estimate, growth trajectory
- Tech stack signals (from job postings, BuiltWith, etc.)

Use your data enrichment tool if available.

### 2. Contact Research

Research the contact:
- Current role and likely responsibilities
- Career background (previous companies, trajectory, look for patterns)
- LinkedIn activity (recent posts, shared articles, commented topics)
- Any public content they've created (podcasts, talks, articles)
- Tone and language patterns from their public content

### 3. ICP Fit Assessment

If ICP is provided, score the account:
- Green / Yellow / Red classification with reasoning
- Key fit signals present
- Key fit signals missing
- Potential disqualifiers to watch for

### 4. SPICED Prep

Prepare structured discovery inputs:

**Situation Hypotheses:** 2-3 likely situations based on company research
- Reference specific data: "[Company] posted 3 SDR roles last month" or "[Company] just raised Series B"

**Pain Hypotheses:** 2-3 likely pains tied to the situations
- Map to problems your product solves

**Impact Questions to Ask:**
- "What is the impact you want to achieve?" (open)
- "Other customers in [their industry] typically want to [impact 1/2/3]. Is that similar?"

**Critical Event Hypotheses:** What might create time pressure?
- Fiscal year end, board meeting, product launch, hiring plan, compliance deadline

### 5. The 6 Non-Negotiable Discovery Questions (Customized)

Prepare customized versions of each question for this specific meeting:

1. **Opening:** "What brought you to [your company] today?" (inbound) / "Why did you take this meeting with me today?" (outbound)
2. **Understanding Reality:** "What's your process for [challenge your product solves] today? Can you walk me through it step-by-step?"
3. **Finding the Breaking Point:** "When did you first realize this was becoming a problem?"
4. **Calculating the Cost:** "What happens to your team's productivity if this problem persists for another quarter?"
5. **Checking Organizational Alignment:** "If I asked your leadership team how big of a priority this is, what would they say?"
6. **Setting Up Next Steps:** "Looking at the clock, we have a few minutes left. Do you mind if we take a moment to align on next steps?"

For each, include:
- The momentum killer to watch for
- The follow-up that digs deeper

### 6. Conversation Starters

2-3 relevant talking points based on their situation:
- Reference specific recent events ("I saw you just opened a new office in...")
- Industry trend relevant to their role
- Something specific about their career path or team growth

### 7. Positioning Notes

- How your product specifically addresses their likely needs
- Relevant case study or proof point from a similar company
- Key differentiators vs likely alternatives they're evaluating
- Competitive landmines to set (questions that expose competitor weaknesses)

### 8. Battlecard Integration (if provided)

If a battlecard is provided or the prospect is evaluating a known competitor:
- Pull relevant objection responses
- Prepare redirect questions
- Identify proof points to reference
- Note competitive landmines to set during discovery

## Output Format

```
# Meeting Prep: [Contact] at [Company]
Date: [YYYY-MM-DD]

## Executive Summary (3 bullets max)

## Company Context
- What they do, who they serve
- Recent developments
- Size / stage / growth signals

## Contact Background
- Role, responsibilities, trajectory
- Public content / interests
- Communication style cues

## ICP Fit: [GREEN/YELLOW/RED]
- [Fit reasoning]

## SPICED Prep
### Situation Hypotheses
### Pain Hypotheses
### Impact Questions
### Critical Event Hypotheses

## Discovery Questions (Customized)
[6 questions with momentum killers + follow-ups]

## Conversation Starters
1. [Starter]
2. [Starter]
3. [Starter]

## Positioning Notes
- Key value prop alignment
- Relevant proof point
- Competitive considerations

## Red Flags to Watch For
- [Disqualification signals]
```

## Output

**In-context only:** this is a pre-meeting brief, not saved to file. If the user wants to save it: `outputs/[company]-[contact]-prep.md` (relative to your working directory).
