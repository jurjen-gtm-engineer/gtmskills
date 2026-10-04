# Pain-Based Segment Evaluator Prompt

## Purpose

This prompt helps evaluate pain-based market segments identified through research, calculating their economic potential and scoring their viability. It transforms qualitative pain analysis into quantifiable business opportunities.

## Required Inputs

To evaluate pain-based segments, I need the following inputs:

1. Average Contract Value (ACV) in $ for your solution
2. Customer Acquisition Cost (CAC) in $ for your typical acquisition process
3. Pain-based segment information from prior research
4. Any specific constraints or assumptions you want to apply

## Evaluation Process

I will analyze each identified pain-based segment and provide the following:

1. Segment ARR Forecast calculation
2. Conversion Rate assessment
3. Pain Intensity scoring
4. Sales Efficiency evaluation
5. Overall Segment Viability Score

For each segment, I will:

1. Extract key data points from your research
2. Apply the segment forecasting formula
3. Calculate economic potential
4. Assess implementation viability
5. Rank segments by opportunity

## Scoring Methodology

I will use the following scoring scales and ranges:

### Pain Intensity Ratio (0-1)

- **0.9-1.0:** Critical/existential pain (severe regulatory/financial consequences)
- **0.7-0.8:** Significant operational pain (major inefficiency/cost impact)
- **0.5-0.6:** Moderate but persistent pain (ongoing friction/waste)
- **0.3-0.4:** Minor but noticeable pain (irritation without major consequences)
- **0.1-0.2:** Minimal pain (barely perceptible/easily worked around)

### Conversion Rate (0-100%)

- **15-20%:** High (pain is visible, solution cost far below pain cost, easy implementation)
- **8-14%:** Moderate (moderately visible pain, solution cost below pain cost)
- **5-7%:** Low (low visibility pain, solution cost near pain cost, complex implementation)
- **1-4%:** Very low (hidden pain, expensive solution, high implementation effort)

### Sales Efficiency Factor (0.5-1.5)

- **1.3-1.5:** Excellent (ACV significantly exceeds CAC)
- **1.0-1.2:** Good (ACV moderately exceeds CAC)
- **0.7-0.9:** Fair (ACV slightly exceeds or equals CAC)
- **0.5-0.6:** Poor (CAC exceeds ACV)

### Overall Segment Viability (0-100)

- **80-100:** Prime opportunity (immediate pursuit)
- **60-79:** Strong opportunity (high priority)
- **40-59:** Moderate opportunity (consider testing)
- **20-39:** Weak opportunity (deprioritize)
- **0-19:** Poor opportunity (avoid)

## Assumptions

I will clearly state all assumptions made in the evaluation, including:

- Market penetration rates based on segment characteristics
- Implementation timeframes
- Competitive factors
- Scaling considerations
- Resource requirements

## Sample Output Format

For each segment, I will provide:

```markdown
## [Segment Name] Evaluation

### Segment Profile
- TAM: [Size of segment]
- Description: [Brief description of pain point]
- Existential Data Point: [Key metric/indicator]

### Scoring Factors
- Pain Intensity: [Score] - [Justification]
- Conversion Rate: [Score] - [Justification]
- Sales Efficiency: [Score] - [Justification]

### Economic Analysis
- Formula: [TAM] x [Pain Intensity] x [Conversion Rate] x [ACV] x [Sales Efficiency] = [ARR Potential]
- Current State Economics: [CAC analysis with current sales approach]
- Improved Economics: [Projected improvement with pain-based targeting]
- Payback Period: [Months to recover acquisition costs]

### Overall Viability Score: [Score]/100
[Brief explanation of score and recommendation]

### Key Assumptions
- [Assumption 1]
- [Assumption 2]
- [Assumption 3]
```

## Final Ranking

After evaluating all segments, I will provide a ranked summary with:

1. Priority order for targeting
2. Relative economic potential
3. Implementation complexity
4. Resource requirements
5. Recommended next steps

## What's Next?

I'll then recommend specific actions for your highest-potential segments, including:

- Messaging strategies
- Channel recommendations
- Testing approaches
- Required resources
