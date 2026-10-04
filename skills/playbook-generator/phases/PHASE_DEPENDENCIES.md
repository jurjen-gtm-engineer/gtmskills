# Phase Dependencies: Cannonball GTM Playbook Generator

## Execution Order

Phases MUST be executed sequentially. Each phase depends on the output of the previous one.

```
Phase 1: Company Research        -> (in-context)
    | (provides company profile, ICP, persona, situational triggers)
Phase 2: EDP Analysis            -> (in-context, informs plays, NOT in output)
    | (provides scored EDPs, pain-based segments)
Phase 3: Pain Segment Scoring    -> (in-context, informs play selection, NOT in output)
    | (provides quantitatively scored segments, top 2-3 selected)
Phase 4: Data Source Discovery   -> (in-context)
    | (provides per-segment data sources, access-path mapping)
Phase 5: Play Generation         -> (in-context)
    | (provides PVP/PQS plays, bad email, hard vs soft comparison)
Phase 6: Scoring & Assembly      -> playbooks/[company]-playbook.md (ONLY file saved)
    | (optional)
Phase 7: Data Accessibility Eval -> playbooks/[company]-data-eval.md (internal QA)
```

## Dependency Map

| Phase | Reads From | Produces |
|-------|-----------|----------|
| 01-company-research | (web + knowledge) | Company profile, ICP, persona |
| 02-edp-analysis | Phase 1 context | EDPs, pain segments (internal only) |
| 03-pain-segment-scoring | Phase 2 context | Scored segments (internal only) |
| 04-data-source-discovery | Phase 1 + 3 context | Data sources per segment |
| 05-play-generation | Phases 1-4 context | PVP/PQS plays, bad email |
| 06-scoring-assembly | Phases 1-5 context | Final playbook (only file saved) |
| 07-data-accessibility-eval (optional) | The assembled playbook | Accessibility eval report |

## Per-Phase References

| Phase | References |
|-------|-----------|
| 01 | `knowledge/methodology.md` |
| 02 | `prompts/edp-analysis-framework.md`, `knowledge/methodology.md` |
| 03 | `prompts/pain-segment-evaluator.md` |
| 04 | `prompts/data-source-discovery.md`, `knowledge/data-source-discovery-guide.md` |
| 05 | `templates/play-template.md`, `knowledge/methodology.md` |
| 06 | `templates/playbook-template.md`, `templates/play-template.md` |
| 07 | the assembled playbook |

## Constraints

- **User-excluded data sources** may not appear anywhere
- **NO static catalog:** data sources discovered fresh every time
- **60-80 words** per play message
- **No product pitching** in any play
- **Quality over quantity:** all plays 8.0+, could be 4 or 16
- **Separate PQS/PVP sections** in output
- **Rich narratives:** "What's the play?" 100-150 words, "Why this works" 80-120 words
- **DATA REQUIREMENT callouts** on Internal/Hybrid plays
- Phase prompts must be executed **verbatim** (no paraphrasing)
- EDP and segment tables are **internal analysis only**, NOT in output
