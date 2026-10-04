---
name: icp-agent
description: "Define, refine, and validate an Ideal Customer Profile using the Science of Scaling framework. Two modes: Quick Start (structured analysis from inputs) or Deep Dive (CRM data analysis with scoring model)."
---

# Skill: ICP Agent

## Purpose

Define, refine, and validate an Ideal Customer Profile using the Science of Scaling framework. Two modes: Quick Start (structured analysis from inputs) or Deep Dive (CRM data analysis with scoring model).

This skill combines Mark Roberge's Red/Yellow/Green framework with ICP expansion methodology and a data-driven analysis approach.

## Inputs

- **Company name** (required)
- **Mode:** Quick Start or Deep Dive
- **For Quick Start:** Product description, top 5-10 best customers, why they chose you, common objections from poor-fit prospects
- **For Deep Dive:** CSV of closed-won/lost deals (12-24 months), customer success metrics if available

## Process

### Quick Start Mode (10-15 minutes)

#### Step 1: Gather Context

Ask the user about:
- What their product does and who it's for
- Top 5-10 best customers (company name, industry, size)
- Why those customers chose them over alternatives
- Common objections from poor-fit prospects

#### Step 2: Build the ICP Profile

Produce a structured ICP with these components:

1. **FIRMOGRAPHICS:** Industry, company size (employees + revenue), geography, growth stage
2. **TECHNOGRAPHICS:** Tech stack signals, tools they use, infrastructure indicators
3. **BUYING TRIGGERS:** Events or conditions that create urgency to buy
4. **PAIN POINTS:** Specific problems the product solves for this profile
5. **DISQUALIFIERS:** Red flags that indicate a poor fit
6. **BUYER PERSONAS:** Key titles involved in the buying process

For each component, provide specific, observable criteria, not vague descriptions.

#### Step 3: Apply Red / Yellow / Green Classification

Using the Science of Scaling framework, classify each attribute:

| Attribute | GREEN (Target) | YELLOW (Inbound Only) | RED (Disqualify) |
|-----------|---------------|----------------------|------------------|
| Employee Count | [ideal range] | [adjacent range] | [outside range] |
| Industry | [core verticals] | [adjacent verticals] | [excluded] |
| Geography | [primary markets] | [secondary markets] | [not served] |
| Tech Stack | [ideal tools] | [acceptable tools] | [incompatible] |
| Key Roles | [must-have roles] | [nice-to-have] | [missing critical] |

Include a **Change History** section: document the date, what changed, and which customers moved as a result.

#### Step 4: Phase-Appropriate Recommendations

Based on the company's scaling phase (PMF / GTM Fit / Growth):

- **PMF:** Keep ICP tight. Validate hypothesis by talking to 20-40 customers (50% bullseye, 50% periphery). Measure success via retention, not close rate.
- **GTM Fit:** 90% of resources on proven ICP. 10% on 2-3 expansion experiments. Each experiment = mini-startup with its own PMF journey.
- **Growth:** Segment matrix (Product x Market x Channel) classified as Scale / Experiment / Ignore.

### Deep Dive Mode (45-60 minutes)

#### Step 1: Upload and Analyze CRM Data

Load the CSV with pandas. For each attribute, calculate:
- Distribution (% of customers in each category)
- Correlation with deal size (do larger deals come from specific segments?)
- Correlation with sales cycle length (do certain segments close faster?)
- Correlation with retention (if available)

#### Step 2: Identify Best Customer Profile

Segment by ACV (top 25% = "Best Customers"). Compare Best vs Rest across all attributes. Identify hero signals: the 1-3 attributes that most powerfully separate best from rest. A hero signal must be observable from the outside (so it can drive prospecting) and must discriminate strongly (a large gap in prevalence between Best and Rest, not a few percentage points).

#### Step 3: Build Scoring Model

Create a weighted scoring model based on the analysis:

- **Layer 1 (Account Fit, 0-100):** Firmographic/technographic signals weighted by discrimination power
- **Layer 2 (Engagement, 0-100):** Behavioral signals if available
- **Layer 3 (ACV Potential):** Bucketed from actual data distribution

Weight each signal by how strongly it separates best customers from the rest in the data, not by intuition. Define tier routing: Tier 1 / Tier 2 / Tier 3 / Disqualify.

#### Step 4: Produce ICP Document

Output format:
1. **Primary ICP:** Highest LTV + fastest cycles + best retention
2. **Secondary ICP:** Worth pursuing with modified approach
3. **Disqualification Criteria:** Consistently underperforming segments
4. **Red/Yellow/Green Scorecard:** Observable attributes with classifications
5. **Scoring Model:** Weighted criteria with decision tree for account qualification
6. **ICP Expansion Roadmap:** 90/10 allocation plan with experiment hypotheses

## Key Principles (from Science of Scaling)

- **LTV over CAC:** Define ICP by maximum lifetime value, not minimum acquisition cost
- **Tight then expand:** Constrained ICP for 0-5-20M, then experiment with 10% of resources
- **Retention is the measure:** ICP fitness = customer success, not close rate
- **Hold the line:** If a rep brings a $1M deal from a red company, tear it up
- **Distractions vs opportunities:** If it doesn't require 40%+ of dev resources to serve = opportunity. Otherwise = distraction.
- **Division hopping:** For enterprise expansion, start with a small deal to get the logo and security clearance, then expand across divisions

## Output

**Save to:** `[company]-icp-definition.md` in your working directory.
