---
name: playbook-generator
description: >
  Cannonball GTM Playbook Generator. 6-phase intelligence-driven playbook workflow
  using EDP methodology and pain-based segmentation. ALWAYS execute all 6 phases
  sequentially (research, EDP analysis, segment scoring, data source discovery,
  play generation, scoring and assembly). NEVER generate a playbook in one shot.
---

# Cannonball GTM Playbook Generator

Generate intelligence-driven GTM playbooks using Existential Data Point (EDP) analysis, pain-based segmentation, and situation-mirroring messages.

**Attribution:** the underlying methodology (pain-based segmentation, EDP thinking, PQS/PVP message formats, the playbook engine concept) is based on the public teachings of Jordan Crawford (Blueprint GTM), restated here in this skill's own words. This repo contains the engine only: no example playbooks and no original third-party content.

## The Cannonball Way

1. **Find the Existential Data Point (EDP):** the metric so critical it determines business survival
2. **Score pain-based segments:** quantify which segments feel the most acute EDP-driven pain
3. **Dynamically discover data sources:** find public data that reveals who is experiencing the pain RIGHT NOW
4. **Generate intelligence-driven plays:** PVP and PQS messages that mirror situations, not pitch products
5. **Assemble a playbook so good the reader asks "how do I run this?"**

## Input Required

- Company domain (required)
- Additional context (optional): GTM challenges, known ICP, constraints, excluded data sources
- Optional: sender identity (name, role, company) for the playbook intro. If not provided, leave the placeholder.

## Output

A single playbook saved to `playbooks/[company]-playbook.md` in your working directory with:
- Company overview with core problem, ICP, persona, differentiators
- Realistic "bad email" teardown showing the old way
- Hard data vs soft signal comparison
- PQS plays (separate section): mirroring exact situations
- PVP plays (separate section): delivering immediate value
- DATA REQUIREMENT callouts on plays needing internal data

**NOT in the output (internal working analysis only):** EDP scoring tables, segment scoring tables, tool operationalization, implementation guidance, quality checklist, per-play multi-criteria tables.

---

## 6-Phase Workflow: EXECUTE SEQUENTIALLY

```
Phase 1: Company Research        -> (in-context)
    |
Phase 2: EDP Analysis            -> (in-context, informs targeting, NOT shown in output)
    |
Phase 3: Pain Segment Scoring    -> (in-context, informs play selection, NOT shown in output)
    |
Phase 4: Data Source Discovery   -> (in-context)
    |
Phase 5: Play Generation         -> (in-context)
    |
Phase 6: Scoring & Assembly      -> playbooks/[company]-playbook.md (ONLY output)
```

All phases execute in-context using `phases/0X-*.md`. Only the final assembled playbook is saved. Run ONE phase at a time, summarize progress, then continue. Never skip a phase and never generate the playbook in a single pass: one-shot playbooks skip the analysis that makes the plays specific.

An optional Phase 7 (`phases/07-data-accessibility-eval.md`) audits every data source in the finished playbook for real-world accessibility before you rely on it.

**Phase prompts:** `prompts/edp-analysis-framework.md`, `prompts/pain-segment-evaluator.md`, `prompts/data-source-discovery.md`

**Templates:** `templates/playbook-template.md`, `templates/play-template.md`

**Methodology:** `knowledge/methodology.md` (core concepts), `knowledge/data-source-discovery-guide.md` (how to find and rank sources)

---

## Key Concepts

### Existential Data Point (EDP)
The critical metric that transforms a nice-to-have into a must-have. Used internally to guide play generation, not shown in output.

### Pain-Based Segments
Segments defined by WHERE they sit relative to the EDP, not by demographics. Used internally to prioritize plays, not shown in output.

### PVP (Permissionless Value Proposition)
Delivers value IN the message. The recipient would pay consulting fees for this intelligence.

### PQS (Pain-Qualified Segment)
Mirrors the prospect's exact situation so precisely they think "how did you know?"

---

## Rules

### Core discipline

1. **The message IS the list.** Targeting precision equals message accuracy.
2. **Phase prompts are verbatim.** Execute `prompts/*.md` exactly as written.
3. **Discover sources fresh every time.** `knowledge/data-source-discovery-guide.md` teaches a thinking pattern, not a lookup table. Every company sits at a unique intersection of regulators (its industry's agency, its customers' agencies, its suppliers' agencies, its geography's registries). Do fresh discovery per playbook.
4. **Respect excluded sources.** If the user names data sources that are off-limits (for legal, commercial, or client-specific reasons), never use them anywhere in the playbook.
5. **60-80 words per message.** Enough for Situation + Insight + Inquisition.
6. **No product mentions.** Only describe their situation (PQS) or deliver value (PVP).
7. **PVP over PQS** when good public data exists.
8. **Specificity beats personalization.** Specific data beats "I saw your LinkedIn."
9. **Phases execute sequentially.** Never skip a phase.
10. **Quality over quantity.** All plays 8.0+. Could be 4 or 16. Never pad with weak plays.
11. **Target 9-13 plays per playbook.** Push harder on discovery before settling for fewer.
12. **Separate PQS and PVP sections.** PQS under "Mirroring Exact Situations," PVP under "Delivering Immediate Value."
13. **DATA REQUIREMENT callouts.** Every Internal/Hybrid data play gets a callout block.
14. **Realistic bad email.** Full company-specific email, no template placeholders.
15. **Rich play narratives.** "What's the play?" is 100-150 words, "Why this works" is 80-120 words.
16. **Multi-source data convergence.** The best plays stack 3-4 data sources. Plays scoring 9.0+ cross-reference at least 3.

### Data and evidence

17. **Data sources MUST be accessible:** freely available, scrapable, supported by common enrichment platforms, or clearly marked as proprietary. NEVER reference paid subscription APIs as if they were freely accessible.
18. **Specific numbers always.** Every play must include at least 2 specific numbers. NEVER "significant", "many", "often".
19. **PQS must end with a routing question** that asks for truth, not time: "Who's handling the deadline?" NEVER "Would you be open to a call?"
20. **Play-type mix as a sanity check.** Strong playbooks usually lean on regulatory triggers and multi-signal composites, with custom research, install-base detection, and account mapping behind them. If your playbook is mostly custom research with no regulatory layer, you have probably missed the regulators relevant to the ICP: recheck Phase 4.
21. **Multi-agency cascade pattern.** For plays scoring 9.0+, prefer signals where the same facility or entity shows up in 2+ regulatory databases within a 90-day window. The cascade is the play. Lead with the timeline, not the violation.
22. **Cite exact regulatory codes when available:** citation classes, deficiency tags, observation codes, percentile thresholds. Generic "compliance issues" loses to a named citation code with an issue date and an abatement deadline.
23. **Temporal indicator coverage.** Every 9.0+ play has BOTH a leading indicator (a future deadline, expiration, or threshold approach) AND a trailing indicator (a materialized consequence with a dollar amount or count). Plays with only one cap at 8.5.
24. **Check the current date before referencing any deadline.** A passed deadline changes the play from "upcoming pressure" to "post-deadline emergency".

### Segmentation gates

25. **Concentric Circle Test (Phase 1 gate).** Segment size must land in the 100-2,000 company band. Above 50,000: you defined the market, not a segment. Below 50: you defined an account list. If your candidate segment is "B2B SaaS" or "manufacturers in Germany," go narrower. Within the company, the same role can have different cores (a CEO cares about cost, a technical lead fears system failure): surface the persona-specific core in Phase 5 messaging.
26. **The size-band anti-pattern.** Never gate on firmographic size bands ("50-1,000 employees," "$10M-$100M revenue") as the primary segment definition. Nobody wakes up different the day they hire one more employee. Two companies of identical size can be in completely different situations. Define segments by situation (the EDP), not size.
27. **Metadata vs reality gate.** Every play must be grounded in customer-voice signal: a transcript quote, a public review, a regulatory finding the customer is named in, a press statement, an employer-review complaint, a consumer-review complaint, an investor-call transcript. Plays resting purely on CRM or database metadata without a customer-voice anchor cap at 7.5. Structured database fields create an illusion of completeness.
28. **Confidence by data depth.** Score the underlying data depth honestly: rich data (3+ transcript-grade signals) earns high confidence and eligibility for 9.0+ scores; metadata-only data is low confidence and gets flagged for audit; thin data returns "Unknown / Insufficient Data" rather than a fabricated play. Silence beats false certainty.
29. **Rule-based first, then AI synthesis.** Phase 5 generates the rule-based plays first (clean regulatory triggers, verifiable cascades, dated deadlines), then layers AI synthesis to catch what rules miss (root cause vs symptom). Hybrid coverage is substantially broader than either alone.
30. **Balance public and internal data.** A playbook that is mostly internal data is brittle (works for only one customer's data set); a playbook that is entirely public data leaves defensibility on the table (competitors can copy it). The public-plus-internal synthesis layer is where proprietary benchmarks earn their keep.
31. **Balance PVP and PQS.** Aim for roughly equal counts. Heavily PQS means you spot situations but deliver no value; heavily PVP means the prospect never sees themselves in the message.
32. **Include a people-data layer.** Professional-network data (headcount, roles, tenure, hiring) is the cheapest, most current enrichment layer. Include it in at least one play unless the target segment is genuinely consumer.
33. **Playbook length sanity check.** A finished playbook typically lands between 2,000 and 4,500 words. Under 2,000: the plays are probably thin. Over 4,500: you are probably padding the "Why this works" sections.

### Message craft

34. **Show the math behind every number, INLINE, not in a table.** Write the derivation into the message sentence with the retrievable identifier inline: "12 custodians account for 620,000 of 840,000 emails (74%)", "inspection #1598334 on Nov 18, 2025 (penalty: $43,200)". The message body IS the receipt. Separately, keep an INTERNAL Receipts worksheet (one line per figure: figure, source and field, calculation, retrievable record ID) as a QA gate. Every number must resolve to a record the buyer could look up, or cut it (or the play caps at 7.5). The worksheet is internal working copy, stripped from the deliverable.
35. **Manufacture vs evaluate: trust the targeting, not the copy.** The engine is trusted for the segment, the record, and the proof. It is NOT trusted for the words. Every drafted message is a plausible-but-unverified draft that tends to read like a database read back to you: specific, competent, lifeless. The deliverable carries the human last-mile instruction ONCE, in a closing "How to use the drafts" note (not a DRAFT label on every play): take each angle to a real customer who lives in that pain, confirm it lands, then rewrite in a human voice. Never present generated copy as send-ready.
36. **Buyer's-eye pass.** After producer-side scoring, read each message AS the named persona: (a) does this feel like inside knowledge or a database readout? (b) would I feel seen, or handled? (c) is there one line I would forward to a colleague? (d) would I reply, ignore, or resent it? A message that scores high on specificity but reads as a record-dump caps at 8.0 regardless of data depth. Note the single weakest line for the human rewrite.
37. **Anchor every number against a benchmark.** State each headline metric against a peer, national, or prior-period baseline, because the delta is the urgency: "moved from better-than-national to worse-than-national", "0.89 to 1.05". A number with no benchmark is a fact; a number with a benchmark is a problem.

### Source discipline (Phase 4 hard gates)

38. **Census before trigger, and rank the source before you use it.** Phase 4 has two jobs in order: build the census (who is the universe, and what unique ID joins them?) and then attach the trigger (what dated event creates urgency?). Rank every candidate source on five multiplied factors (ground-truth distance, join-key quality, coverage, free bulk access, update cadence). Two hard gates override any score: the source must be the original or the publisher's own copy (never a scrape) and carry a real date; and never cite a source in a play until you have personally verified the file exists and is downloadable. A play built on two files that share a unique ID (a provider number, tax ID, registry number, legal-entity identifier) beats a play built on fuzzy name-matching, every time.
39. **Compute the clock.** The best timing signal is often arithmetic, not a field anyone sells: a public date plus a known contractual clock equals a buying window. Ask of every ICP: what contractual clock is ticking on this buyer, which public record starts it, and what window does the subtraction produce? Candidates: lease or contract end, certification validity, support end-of-life, asset refresh cycle, funding runway (roughly 18-24 months from a round), exec tenure (roughly 18-24 months to show results), regulatory grace period.
40. **Probe every provider filter with a known-answer test.** Many data APIs, handed a filter they do not support, silently ignore it and return confident-looking results. Before any play depends on a provider filter, run it against records whose answer you already know, and verify both that the right rows came back AND that the filter changed the result set at all (same query with and without it; identical counts means it was ignored). Note: enrichment APIs generally cannot search past employers; "used to work at X" requires web research.
41. **The data-moat gate: reject a vertical whose pain leaves no public trace.** Before a vertical becomes a segment, score it on one thing first: can public data actually PROVE this pain? A vertical whose pain leaves no public trace is auto-rejected before it ever becomes a message. This gate runs in Phase 3.
42. **Two high-feasibility sources, or no segment.** Map the data across four lanes (government, competitive, timing, operational) and write down the exact fields you will use (not "safety records" but `inspection_number, issuance_date, violation_type, penalty_amount`). Do not build a segment until at least TWO sources rate high-feasibility. A pile of "maybe" sources does not clear the bar. Grade the segment's own confidence in plain terms: built straight off the record is high; the moment it must guess at something the record does not show (headcount, budget), the confidence drops and the playbook says so. No fake certainty.
43. **Buyer's-eye scoring thresholds.** A pain-qualified message must clear 7.0 when graded as the buyer. A true gift (a PVP someone would thank you for whether or not they buy) must clear 8.5. Below the bar: rewritten or killed, never shipped. The gift bar is higher because a gift that is not worth having is worse than no gift.
44. **The competitor test, plus the clean no-fit.** Final gate before any play ships, three parts, all required: hyper-specific, factually grounded, non-obvious. A message a competitor selling the same category could send word-for-word fails. And a clean "no fit" is a valid output: if nothing in the public record connects to what the company sells, write up what you tried and where the data ran out. Do not invent a play. A clean no-fit is worth more than a confident wrong one.
45. **No false alives: verify a record is live before it becomes proof.** An HTTP 200 is not proof of life; a parked domain still loads. Four free checks before any enrichment spend: wire checks (does the domain resolve, are the nameservers a known parking company, is there any MX record), read the body for sentinel phrases ("this domain is for sale"), the garbage-page trick (request a URL that cannot exist; a real site returns 404, an empty shell serves its homepage), and the certificate-transparency heartbeat (first certificate is the birthday, steady renewals are a pulse, stopped renewals are a death certificate with a date). Prefer a false dead (costs coverage) over a false alive (poisons the list): hold the row rather than ship the poison.
46. **Adjudicate evidence before it becomes truth.** Two sources with separate lineage must agree (two aggregators agreeing is one bad copy machine quoting another). Aggregators never corroborate: they nominate a candidate, they never confirm one. Only positive evidence settles a row: presence proves, absence escalates, never kills. Identity must be proven, not resembled (name plus place plus jurisdiction; a directory that mentions an org does not prove it IS the org). When sources conflict, the newer page beats the grander site. Confidence bands: commit at 0.85 and above, commit the negative at 0.20 and below, hold everything in between. Never guess.

---

## Quality Checklist (Internal, NOT in output)

Before declaring the playbook complete, verify ALL of these:

- [ ] All plays score 8.0+ (no padding with weak plays)
- [ ] All plays use specific data (no "companies like yours")
- [ ] All messages 60-80 words with Situation, Insight, Inquisition
- [ ] Zero product pitching in any PQS message
- [ ] No user-excluded data sources referenced anywhere
- [ ] PQS and PVP plays are in separate sections
- [ ] DATA REQUIREMENT callouts on all Internal/Hybrid data plays
- [ ] "What's the play?" is 100-150 words per play
- [ ] "Why this works" is 80-120 words per play
- [ ] Bad email example is realistic and company-specific (no template placeholders)
- [ ] Every number in every message resolves to a retrievable record (internal Receipts worksheet complete, then stripped)
- [ ] Math shown INLINE in each message body (derivation in the sentence, record ID inline)
- [ ] Every headline number anchored against a benchmark
- [ ] Buyer's-eye pass run on every message; record-dump messages capped at 8.0
- [ ] Human last-mile appears ONCE in the closing "How to use the drafts" note
- [ ] Data sources table complete with Key Fields and Used For
- [ ] Company Overview section present (Core Problem, ICP, Persona, Differentiators)
- [ ] Diamond separators between major sections
- [ ] NO EDP scoring tables in output
- [ ] NO segment scoring tables in output
- [ ] NO tool operationalization section in output
- [ ] NO implementation / rollout section in output
- [ ] NO quality checklist in output

If any check fails, go back to the relevant phase and fix.
