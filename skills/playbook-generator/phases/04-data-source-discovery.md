# Phase 4: Data Source Discovery

## Purpose

Dynamically discover data sources for the selected segments. This is Phase 4 of the Cannonball GTM Playbook Generator.

**CRITICAL: `knowledge/data-source-discovery-guide.md` is a thinking pattern, not a lookup table.** Read it to internalize HOW to discover sources (which agencies regulate which industries, which fields create urgency, which stacks form cascades), then go discover the right sources for THIS specific company. The guide calibrates the search; it does not constrain the output.

## Inputs

- **Phase 3 context** (in-context): scored segments
- **Phase 1 context** (in-context): industry context and ICP

## Process

### 1. Load previous phase context

Use Phase 3 segment scoring context to identify the top segments selected for targeting. Use Phase 1 context for industry context and ICP.

### 1b. Build the CENSUS before you hunt triggers

Discovery has **two jobs, in this order**. Do not skip to the second.

1. **Census: who is the universe, and what unique ID joins them?** Reach for the highest rung of the ground-truth ladder first (see the guide): a government registry with a unique ID (rung 1) or a legally mandated disclosure (rung 2), not an aggregator. Name the **join key** explicitly (registry number, tax ID, legal-entity identifier, license number); if the sources you picked share no key, the cascade in step 7 cannot exist.
2. **Trigger: what dated event creates urgency on this census?** This is what regulator databases and the discovery prompt below are for.

**Rank every candidate on the five multiplied factors** (ground-truth distance, join-key quality, coverage, free bulk access, update cadence) and apply the **two hard gates that override the score**:
- **Provenance:** original source or the publisher's own copy, never a scrape, and it carries a real date. A scrape can inform a lead; it can never be the foundation of the TAM.
- **Personally verified:** treat any claim of "free bulk business data" as false until you have personally downloaded the file. Do not cite a source you have not opened.

**Also compute the clock:** the strongest leading indicator is usually arithmetic, not a field. A public date plus a known contractual clock (lease end, certification validity, support end-of-life, refresh cycle, funding runway, exec tenure, regulatory grace period) produces a buying window no vendor sells. Ask this explicitly for the ICP before settling for a purchasable field.

**And check for dead ends** before proposing any source (is it live, actually free, storable under its terms?), and never propose a provider filter without a **known-answer probe**: many APIs silently ignore unsupported filters and return confident-looking results.

### 2. Execute the Data Source Discovery prompt (VERBATIM)

For **each top segment**, execute the prompt in `prompts/data-source-discovery.md` **exactly as written**.

When executing for each segment:
- Frame the discovery around the specific pain point and EDP for that segment
- Consider the industry, geography, and operational context from Phase 1
- Generate 10-15 potential sources in the first pass, evaluate in the second pass, select 3-5 in the final pass

### 3. Check enrichment-platform reach

For each discovered data source, check whether the user's enrichment platform (Clay or similar) can:
- Access or enrich that data source natively
- Automate the data collection (HTTP actions, agent-based scraping)
- Cross-reference it with other signals

If no automated path exists, note the manual effort honestly. This feeds the accessibility eval in Phase 7.

### 4. Classify temporal role: leading vs trailing indicator

For each discovered source, classify its temporal role:

| Source | Temporal Role | Rationale |
|--------|--------------|-----------|
| ... | **Leading**: detectable signal that the problem is active, before consequences hit | ... |
| ... | **Trailing**: confirmation that the pain has already materialized for others (enforcement actions, settlements, penalties with dollar amounts) | ... |
| ... | **Neutral**: enrichment data without a temporal dimension | ... |

**Per-segment check:** does each target segment have at least one leading indicator? Ideally both leading and trailing. A data key plus a strong leading indicator can carry a segment. Adding a trailing indicator (with dollar amounts) is what makes the message credible and urgent.

### 5. Evaluate signal quality

For each source, evaluate using the Signal Quality Framework:
- **High Value / Easy Access:** must have at least 2 per segment
- **High Value / Hard Access:** maximum 1 per segment
- **Low Value sources:** exclude

### 6. Map integration paths

For each recommended source, document:
- How the data can be accessed (bulk download, API, scrape, manual)
- What enrichment steps are needed
- How to validate the signal

### 7. Find the cascades

Check which selected sources share an entity ID. When 2+ agencies have data on the same facility or entity within a 90-day window, that convergence is the play. Look for cascades before single-source signals.

## Constraints

- **Respect user-excluded sources.** If the user named any data sources as off-limits, they may not appear anywhere in this phase or downstream.
- **The guide teaches the method, it does not supply the answer.** Run fresh discovery against THIS company's industry, geography, customer base, and supplier network. Most strong plays use sources no catalog enumerates, because every company sits at a unique cross-section of regulators.
- **Map the target's CUSTOMERS' regulators, not just the target's own.** For B2B products (which is most of what this skill runs against), the regulators that create buying urgency sit on the customers' industries. Enumerate the top 2-3 customer industries (from the target's case studies and logos) and identify the dominant regulator plus its dated or temporal field for each. Skip this only when the target sells purely to consumers or to unregulated SMBs.
- **Multi-agency cascade preferred.**
- **NO generic sources.** Each source must have a direct connection to the segment's EDP.

## References

- `prompts/data-source-discovery.md`: **exact prompt, execute verbatim**
- `knowledge/data-source-discovery-guide.md`: how to find and rank sources

## Output

**In-context only. Do NOT save to file.** This feeds Phase 5.

Include:
- Per-segment data source recommendations (3-5 sources each)
- For each source: overview, signal quality evaluation, implementation approach
- Access-path mapping (how each source is reached: bulk, API, scrape, manual)
- **Leading/trailing indicator classification** per source
- **Temporal coverage check** per segment (does it have both leading and trailing?)
- Cross-segment source synergies
- Multi-source convergence opportunities (which sources can be stacked for stronger plays)
- Confirmation that no user-excluded sources are used
