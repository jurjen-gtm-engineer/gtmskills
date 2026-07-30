# Phase 7: Data Accessibility Eval (Optional QA Gate)

## Purpose

Evaluate every data source in the assembled playbook for real-world accessibility, cost, and operationalizability. This is an optional Phase 7 QA gate of the Cannonball GTM Playbook Generator.

**Problem this solves:** playbooks that reference enterprise-only databases, deprecated APIs, or theoretically-available-but-practically-inaccessible data create false confidence. This eval ensures every play can actually be executed with tools the user has or can reasonably obtain.

## Inputs

- **The Phase 6 assembled playbook** (`playbooks/[company]-playbook.md`)

## Process

### 1. Extract all data sources

Parse every play in the playbook and build a master list of unique data sources referenced. For each source, capture:
- Source name
- How it is used in the play(s)
- What specific fields or data points the play depends on

### 2. Score each data source on accessibility

Rate each source on a 1-5 scale across four dimensions:

| Dimension | 5 (best) | 3 (middle) | 1 (worst) |
|-----------|----------|------------|-----------|
| **Cost** | Free / open data | Affordable self-serve subscription | Enterprise-only contract pricing |
| **API/Scrape** | Public API, no auth | API with a paid key at self-serve rates | No API, no scraping possible, manual only |
| **Data Freshness** | Real-time or daily | Monthly updates | Static one-time snapshot |
| **Automation Path** | Native integration in a common enrichment platform | Agent-based scraping or a simple HTTP action works | No automated path, fully manual |

**Composite Accessibility Score** = average of the 4 dimensions (1-5 scale)

### 3. Classify each source

| Score | Classification | Action |
|-------|---------------|--------|
| **4.0-5.0** | Green: fully accessible | No changes needed |
| **3.0-3.9** | Yellow: accessible with effort | Add a note to the play about setup requirements |
| **2.0-2.9** | Orange: questionable | Flag in the eval output. Consider whether an alternative source exists |
| **1.0-1.9** | Red: inaccessible for most | **Must replace or remove.** Enterprise databases, paywalled datasets, deprecated APIs |

### 4. Cross-check play viability

For each play, derive a **Play Executability** rating:
- If ALL data sources are Green (4.0+): fully executable
- If ANY source is Yellow (3.0-3.9): executable with noted setup
- If ANY source is Orange (2.0-2.9): needs source substitution or a DATA REQUIREMENT callout
- If ANY source is Red (1.0-1.9): **the play must be revised or removed**

### 5. Verify the data actually exists

For critical data sources, run a quick verification:
- **Fetch the source URL:** does the page load? Is the data still there?
- **Check whether the API is live:** does the endpoint return data?
- **Test scrapability:** can an agent or HTTP action actually extract the fields needed?

Do not verify every source. Focus on:
- Any source scoring Yellow or Orange
- Sources critical to the play's core insight (the "money data point")
- Sources you have not personally used before

### 6. Check for enterprise-only traps

Some data products commonly cited in playbooks (financial-markets terminals, private-market intelligence platforms, analyst-firm research, full-suite contact databases) are sold on enterprise contracts only. Flag any play whose core insight depends on such a source.

**Rule:** if a play's core insight depends on an enterprise-only source AND the user does not already have access, the play needs an accessible alternative or a clear "requires [source] subscription" mark.

### 7. Suggest alternatives for Red and Orange sources

For each flagged source, suggest:
1. A free or cheap alternative that provides similar data
2. An automation workaround (agent scraping, an HTTP API action)
3. Whether the play can work without that specific source (degraded but still viable)

### 8. Generate the eval report

```markdown
## Data Accessibility Eval: [Company] Playbook

### Summary
- Total unique data sources: [N]
- Green (fully accessible): [N] ([%])
- Yellow (accessible with effort): [N] ([%])
- Orange (questionable): [N] ([%])
- Red (inaccessible): [N] ([%])

### Overall Playbook Executability: [GREEN/YELLOW/ORANGE/RED]

### Source-by-Source Scoring

| Source | Cost | API/Scrape | Freshness | Automation | Composite | Classification |
|--------|------|-----------|-----------|------------|-----------|---------------|
| [Source 1] | [X] | [X] | [X] | [X] | [X.X] | [Green/Yellow/Orange/Red] |

### Play Executability

| Play | Score | Sources Used | Executability | Issues |
|------|-------|-------------|--------------|--------|
| Play 1 | [X.X/10] | Source A, B, C | [Fully Executable / Needs Setup / Needs Revision / Remove] | [None / specific issue] |

### Flags & Recommendations

#### Red flags (must fix)
- [Source X] used in Play [N]: [reason it is inaccessible]. **Suggested alternative:** [alternative]

#### Yellow flags (note required)
- [Source Y] used in Play [N]: [setup requirement]. Add a note to the play.

#### Verified sources
- [Source Z]: confirmed accessible via [method] on [date]
```

## When to run

- **Always** after Phase 6 assembly, before relying on the playbook
- **Re-run** if the playbook is updated with new plays or sources
- **Skip** only if all sources in the playbook are already well-known and verified

## Integration with Phase 6

If the eval flags Red sources, loop back to Phase 5 (Play Generation) to:
1. Replace the inaccessible source with an alternative
2. Revise the play's targeting logic and message to work with the alternative
3. Re-score the play (a source substitution may change the composite score)
4. Re-assemble in Phase 6

## Output

Save the eval report to: `playbooks/[company]-data-eval.md`

This is an internal QA document, NOT part of the playbook itself.
