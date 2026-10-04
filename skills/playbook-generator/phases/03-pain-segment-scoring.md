# Phase 3: Pain Segment Scoring

## Purpose

Quantitatively score pain segments using the Pain-Based Segment Evaluator. This is Phase 3 of the Cannonball GTM Playbook Generator.

## Inputs

- **Phase 2 context** (in-context from the previous phase)

## Process

### 1. Load Phase 2 EDP analysis

Use the EDP analysis context from Phase 2. Extract:
- The recommended primary EDP
- The 4-6 pain-based segments
- Any ACV/CAC estimates from the company research

### 2. Execute the Pain-Based Segment Evaluator (VERBATIM)

Execute the prompt in `prompts/pain-segment-evaluator.md` **exactly as written**. Do not paraphrase it.

When executing:
- Use ACV from Phase 1/2 research (or estimate from pricing page analysis)
- Estimate CAC based on the company's GTM motion (PLG vs sales-led vs hybrid)
- Feed in all pain-based segments from Phase 2

### 3. Score each segment

For each segment, calculate using the exact scoring methodology from the prompt:

- **Pain Intensity Ratio (0-1):** critical to minimal
- **Conversion Rate (0-100%):** based on pain visibility and solution cost
- **Sales Efficiency Factor (0.5-1.5):** ACV vs CAC ratio
- **Overall Segment Viability (0-100):** composite score

### 4. Apply the economic formula

For each segment:
```
ARR Potential = TAM x Pain Intensity x Conversion Rate x ACV x Sales Efficiency
```

### 5. Apply the data-moat gate

Before ranking, run the data-moat gate on every segment: **can public data actually PROVE this pain?** A segment whose pain leaves no public trace is auto-rejected here, before it ever becomes a message. Do not soften it or message around it. If every candidate segment fails the gate, report a clean no-fit rather than forcing a segment through.

### 6. Rank and select

- Rank all segments by Overall Viability Score
- Select the top 2-3 segments (any scoring 7.0+ is worth testing, 8.0+ is priority, 9.0+ deserves the entire focus)
- These become the target segments for data source discovery

## References

- `prompts/pain-segment-evaluator.md`: **exact prompt, execute verbatim**

## Output

**In-context only. Do NOT save to file.** This analysis informs play selection but is NOT included in the final playbook output.

Include:
- Scored segment table with all metrics (TAM, Pain Intensity, Conversion Rate, Sales Efficiency, ARR Potential, Overall Score)
- Data-moat gate result per segment (can public data prove the pain?)
- Detailed evaluation for each segment
- Final ranked list with priority order
- Top segments selected for play generation
