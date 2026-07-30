# Phase 1: Company Research

## Purpose

Deep web and ICP research on the target company. This is Phase 1 of the Cannonball GTM Playbook Generator.

## Inputs

- **Company domain** (required), e.g. `example.com`
- **Additional context** (optional): any specifics about the company or its GTM challenges

## Process

### 1. Fetch and analyze the website

Fetch the company domain and extract:

1. **What they sell:** core product or service offering
2. **Who they sell to:** target customers (industries, company sizes)
3. **Value proposition:** main benefits and outcomes claimed
4. **Pricing model:** if visible (seats, usage, flat fee, tiers)
5. **Differentiators:** what makes them unique vs competitors

### 2. Define the ICP using the 3-question framework

Apply the three-question discovery framework from `knowledge/methodology.md`:

1. **Surface level:** "Can they use this product?" (features, compatibility, basic fit)
2. **Functional level:** "Why do they need this?" (use cases they already know)
3. **Situational level (CRITICAL):** "What CHANGED in their customer's organization that made them need this NOW?"

Output format:
```
TARGET ICP:
- Industries: [specific verticals]
- Company Size: [revenue range, employee count]
- Operational Context: [key processes, workflows, technologies]
- Geographic Focus: [if applicable]
- Situational Hypotheses: [3-5 situations that create urgency]
```

### 3. Map the primary persona

```
PRIMARY PERSONA:
- Title: [specific job title]
- Key Responsibilities: [what they do daily]
- KPIs: [what they're measured on]
- Blind Spots: [what they don't know but should]
- Pain Points: [daily frustrations tied to situational triggers]
```

### 4. Identify situational triggers

List 3-5 situations where the target company's customers would need this solution NOW. These must be:

- **Behavioral, not demographic:** what changed, not who they are
- **Observable:** can be detected from public data
- **Time-sensitive:** the pain has a window

### 5. Apply the Concentric Circle Test (Phase 1 gate)

Before exiting Phase 1, validate the proposed primary segment (a concept from Jordan Crawford, Blueprint GTM):

**Layer 1: Segment.** Does the segment number 100-2,000 companies?
- **Over 50,000 companies: you defined the market.** Refuse to exit Phase 1. Pick a vertical inside the market (orthodontists, not "healthcare").
- **Under 50 companies: you defined an account list.** Broaden until the segment is real.
- **100-2,000: continue.**

**Layer 2: Company.** Within that segment, do most companies cluster around the same core challenge? If you find yourself picking the "least-bad" companies, the segment is wrong, not the company filter. Redo Layer 1.

**Layer 3: Person.** Inside the typical target company, what is the persona-specific *core*? The same company can have multiple cores: the CEO cares about cost; the technical lead fears system failure; the ops VP cares about SLA compliance. Surface 2-3 personas with their distinct cores so Phase 5 can vary the messaging by persona.

**Output the Concentric Circle Test result explicitly:** segment size estimate, the dominant core challenge per persona, and a one-line justification that the segment is neither the market nor an account list.

### 6. Anti-pattern check: firmographic size bands

If the proposed ICP gates primarily on firmographic bands (employee count ranges, revenue ranges), **flag it and redo**. Nobody wakes up different the day they hire one more employee. Two companies of identical size can be in completely different situations. Define segments by *situation* (the EDP), not size.

## References

- `knowledge/methodology.md`: core methodology

## Output

**In-context only. Do NOT save to file.** This feeds Phase 2.

Include:
- Company profile (what they sell, who to, value prop, pricing, differentiators)
- ICP definition with situational hypotheses
- Primary persona map (title, KPIs, blind spots, pain points)
- 3-5 situational triggers ranked by observability
- Key differentiators vs competitors
- Concentric Circle Test result
