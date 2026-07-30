---
name: blueprint-swarm
description: Multi-agent call-data analysis at scale. Reads hundreds of call transcripts and CRM exports in parallel, extracts churn timelines, win patterns, competitive intel, product gaps, and playbook material, with source-tagged quotes and an Opus auditor that kills hallucinated output. Based on Jordan Crawford's open-source Blueprint Swarm.
version: 1.0
---

# Blueprint Swarm: Multi-Agent Call Intelligence

> **Attribution:** This skill is based on Jordan Crawford's open-source **Blueprint Swarm** project: **github.com/SantaJordan/blueprint-swarm** (Jordan Crawford, Blueprint, April 2026). If you use this methodology, credit the original repo.

## Purpose

Single analysts tap out at ~30 calls and start pattern-matching off recency. The gold in call data is **the aggregate**: how many churned accounts had a champion departure beforehand, how many days in advance the warning signal appeared, which gap keeps showing up across unrelated accounts.

This skill runs a swarm: many Sonnet analyst agents read batches in parallel, an Opus auditor kills any output with paraphrased or fabricated quotes, and a synthesis agent dedupes findings and scores confidence by independent-batch agreement.

## When to invoke

- You have hundreds of recorded calls (Gong/Chorus/Fireflies/raw transcripts) and nobody has ever read them all.
- Need to answer: *why are we losing? why are we winning? what gap keeps coming up? who else are they evaluating?*
- Building a playbook from real customer language.
- Closed-lost autopsy at scale.
- Pre-launch competitive intel sweep before a campaign.

For a **single transcript or single account**, prefer the `conversational-intelligence` skill: that's the surgical tool. Use this skill when the question is about patterns *across* records.

## Required inputs

- `data_dir`: absolute path to a directory of call data. Mixed formats fine.
- `output_dir`: where to write results. Defaults to `swarm-analysis/<run_timestamp>/` in the current working directory.
- `analysis_type` (optional, asked in Weigh phase): `churn` | `wins` | `competitive` | `product_gaps` | `playbook` | `full`.

Optional:
- `batch_size`: default 10 records per analyst agent.
- `wave_size`: default 6-10 concurrent agents per wave.
- `audit_threshold`: default 7/10. Below = block Merge.

## Inputs auto-detected (Scan phase)

- Gong JSON exports
- Chorus exports
- Fireflies transcripts (JSON or markdown)
- CSV exports from your CRM
- Raw `.txt` / `.vtt` / `.srt` transcripts
- PDFs (call notes, QBR decks)

If the directory has only CRM metadata and **zero transcripts**, abort Scan with a warning (Jordan's "2,400-account analysis" cautionary tale: an analysis run on metadata alone produces confident-sounding but hollow findings). Surface that the input is metadata-only and ask the user to confirm before proceeding (output will be much weaker).

---

## The S.W.A.R.M. method: five phases

Execute sequentially. Do not skip Audit.

### 1. Scan
Profile the directory:
- Count records per format.
- Sample 3 records, show structure.
- Report what analyses are feasible with what's there (e.g. "no closed-lost reason field → churn timelines will rely on transcript signals only").

Output: `scan_report.md` in the run directory.

### 2. Weigh
Recommend analysis types ranked by data fit. Present as a numbered list with reasoning. **User picks**, do not auto-select. Possible types:

| Type | Needs | Outputs |
|------|-------|---------|
| `churn` | Churned accounts + their pre-churn calls | Timeline reconstruction, lead-time histograms, intervention-window map |
| `wins` | Closed-won deals + discovery/demo calls | What pain resonated, who championed, language that moved the deal |
| `competitive` | Any calls mentioning competitors | Competitor mention frequency, displacement hooks, where we lose head-to-head |
| `product_gaps` | Any transcripts with feature/capability talk | Ranked gap list with frequency + account context |
| `playbook` | Wins + losses both | Pain-qualified segments, value props validated by customer language |
| `full` | All of the above | Combined report |

### 3. Audit (pre-run)
**This is the step everyone skips. Don't.**

- Pick 3-4 sample records.
- Run the chosen analyst prompt against them in front of the user.
- Show extracted output.
- User confirms quality OR adjusts the prompt before launching the wave.

Refuse to proceed past Audit if user hasn't seen sample output.

### 4. Run
Pre-prepare batch files. Each analyst gets a self-contained batch: no exploring, no searching, just **read → think → write structured output**.

Launch waves of 6-10 concurrent Sonnet analyst agents (use the Agent tool, `subagent_type: general-purpose` unless a more specific agent fits, multiple in a single message for parallelism).

After all analysts in all waves finish, launch the **Opus auditor** as a single Agent call. Its job:

7-point quality check on a sample of 20 random findings:
1. Quote present and verbatim against source? (paraphrase = flag)
2. Quote fabricated? (critical fail → score 0)
3. Speaker correctly attributed?
4. Account/date correctly tagged?
5. Finding actually supported by the cited quote (not over-extrapolated)?
6. Confidence claim proportional to evidence?
7. Finding non-trivial (not "customer mentioned the product")?

Auditor returns `quality_score` (0-10) and per-finding flags. **If score < `audit_threshold`, halt and report. Do NOT proceed to Merge.**

### 5. Merge
Synthesis agent (single Opus Agent call) takes all batch outputs:
- Dedupes findings.
- Confidence scoring: **HIGH = 3+ independent batches confirmed; MEDIUM = 2 batches; LOW = 1 batch.**
- Drops anything the auditor flagged.
- Emits three artefacts in the run directory:
  - `findings.json`: structured for downstream tools
  - `report.md`: Slack/email-ready narrative
  - `playbook.html`: interactive, every quote linked back to source record

---

## The six agent roles

| Agent | Model | Job |
|-------|-------|-----|
| Classifier | Sonnet | Categorize each record (won/lost/expansion/support/discovery/etc.) before analysts run |
| Churn analyst | Sonnet | Reconstruct full pre-churn timeline: support spikes, champion departure, gap raised, intervention windows |
| Win analyst | Sonnet | What closed it? Which pain resonated? Champion language? Objections overcome? |
| Pattern extractor | Sonnet | Structured pull per record: pains, competitors, gaps, buying signals |
| Synthesis | Opus | Cross-batch dedupe + confidence scoring |
| Auditor | Opus | 7-point hallucination check on 20 random findings; can kill the run |

In `full` mode, every record passes through Classifier → relevant analyst(s) → Pattern extractor.

---

## Methodology: what makes this not a summarizer

These three rules are non-negotiable. Strip them and you're shipping AI mush.

1. **Pain-qualified segmentation.** Classify records by *the situation that made the customer need us*, not by firmographics. Segments defined by shared pain predict behavior; segments defined by industry/size mostly don't.
2. **Specificity breeds trust.** Standard is "47 of 312 churned accounts (15%) had a champion departure within 60 days of cancellation, citing [3 specific accounts with quotes]." Standard is NOT "many customers mentioned competitors."
3. **Source-tagged everything.** Every finding carries: `account_name`, `call_date`, `speaker_role`, `verbatim_quote`, `record_id`. No exceptions. The HTML output makes this clickable; the JSON makes it greppable.

---

## Output structure

```
<output_dir>/swarm-analysis/<timestamp>/
├── scan_report.md
├── weigh_recommendation.md
├── audit_sample.md           # Phase 3 user-confirmation artefact
├── batches/
│   ├── batch_001_input.json
│   ├── batch_001_output.json
│   └── ...
├── auditor_report.json       # 7-point check
├── synthesis_log.md          # what was deduped, confidence math
├── findings.json             # final, audited
├── report.md                 # narrative
└── playbook.html             # interactive, source-linked
```

---

## Overnight execution (large datasets)

For >300 records:
1. Run inside `tmux` so a disconnect doesn't kill the run.
2. Save state after every wave (`batches/wave_N_state.json`).
3. On a rate-limit, wait for reset and auto-resume from last completed wave.
4. Send a completion notification when Merge finishes (if a notification tool is available).

---

## Composition with other skills

- **Feed your playbook generation process**: `findings.json` from a `playbook` run becomes research input. Saves a week of manual transcript reading.
- **Feed your cold email copywriting**: pain-segment findings + verbatim quotes become segment evidence and openers grounded in real customer language.
- **Feed your funnel/conversion analysis**: churn timeline data layers on top of stage-conversion analysis from your CRM export. Tells you *why* the conversion is leaking, not just where.
- **Feed `icp-objection-mapping`**: surfaced objections from win/loss calls become the inputs to red-team campaigns before launch.
- **Augments `conversational-intelligence`**: that skill is the surgical tool for one transcript; this is the swarm tool for the whole library.

---

## Compound learning hook

After each run, append to a local `debrief-log.md`:
- Audit score for this run
- Which agent role had the most flagged findings (improvement target)
- Any methodology adjustments made mid-run

When 3+ runs show the same failure pattern (e.g. "auditor consistently flags speaker attribution on Fireflies VTT files"), promote it to a permanent rule in this SKILL.md.

---

## Failure modes to refuse

- **Metadata-only input.** If there are zero transcripts and only CRM fields, surface this in Scan and require explicit user override before continuing.
- **Auditor below threshold.** Never silently ship findings that failed the 7-point check. Halt, report, ask the user how to proceed.
- **Confidence inflation.** Single-batch findings ship as LOW. Do not reclassify upward without independent confirmation.
- **Quote paraphrasing.** Verbatim only. If the source isn't available verbatim, the quote field is empty and the finding drops a confidence tier.
