# gtmskills

Open-source GTM skills and knowledge for revenue teams that want to run GTM Engineering themselves, organized by growth stage.

Built by [Jurjen Koning](https://www.linkedin.com/in/jurjenkoning/) (NeuralFlow). These skills run in [Claude Code](https://claude.com/claude-code) and encode the methodology behind our client work: Winning by Design's Revenue Architecture, Stage 2 Capital's Science of Scaling, and the GTM Engineering practices we use in production.

## Why stages first

Across 50+ GTM diagnostics, Winning by Design found the standardized Operating Model is the single strongest predictor of compounding growth: +0.96 correlation when present, -0.98 when absent. But the right playbook depends entirely on where you are. Running a scale playbook before Product-Market Fit burns capital; running founder-led motions past GTM Fit caps growth. So everything here is segmented by stage:

| Stage | You are here if... | Folder |
|---|---|---|
| **Product-Market Fit** | Customers renew and realize value, but you are still proving who to sell to and why they buy | [`product-market-fit/`](./product-market-fit) |
| **GTM Fit** | You have proof and now need a repeatable, profitable sales motion with unit economics that work | [`gtm-fit/`](./gtm-fit) |
| **Growth & Moat** | The motion repeats and now you scale it, instrument it, and defend it | [`growth-and-moat/`](./growth-and-moat) |

Not sure which stage you are in? Start in [`assessments/`](./assessments): four assessments that run right here in Claude Code, or use the hosted versions: [GTM Scan](https://www.gtmscan.app) (readiness across 8 domains with AI coaching) and [Bowtie Benchmarks](https://bowtie-benchmarks.vercel.app) (CR1-CR8 against benchmarks for your ACV band).

## How to use

Each skill is a folder with a `SKILL.md` that Claude Code picks up automatically.

```bash
git clone https://github.com/jurjen-gtm-engineer/gtmskills.git
cp -r gtmskills/product-market-fit/customer-dossier ~/.claude/skills/
```

Then ask Claude Code to use the skill by name. Every skill states its required inputs and produces a concrete deliverable, not advice.

## Skills

| Skill | Where | What it does |
|---|---|---|
| [`gtm-readiness-scan`](./assessments/gtm-readiness-scan) | Assessments | 24-question GTM maturity self-assessment: 8 domains scored 0-5, overall readiness index, company archetype, and which stage folder to start in |
| [`bowtie-benchmark`](./assessments/bowtie-benchmark) | Assessments | Your 12 funnel metrics against CR1-CR8 benchmarks for your ACV band, with a per-metric leak diagnosis |
| [`crm-scorecard`](./assessments/crm-scorecard) | Assessments | Computes CR1-CR8 from your actual CRM export (any CRM), cohort-first, benchmarked, with a data-quality preflight |
| [`spiced-call-scorecard`](./assessments/spiced-call-scorecard) | Assessments | Scores call transcripts on the five SPICED dimensions 0-3 with verbatim evidence, plus team-level pattern analysis |
| [`customer-dossier`](./product-market-fit/customer-dossier) | Product-Market Fit | Builds a ground-truth customer dossier per account: one timeline, provenance on every field, conflicts surfaced. The foundation for ICP analysis |
| [`gtm-ai-brief`](./gtm-fit/gtm-ai-brief) | GTM Fit | Turns a recurring manual GTM task into a written, testable AI brief (Trigger / Inputs / Steps / Output / Guardrails) |
| [`compound-growth-check`](./growth-and-moat/compound-growth-check) | Growth & Moat | Classifies your ARR trajectory (compounding / decaying) from 6+ quarters and places you on the 10-state growth ladder |
| [`ai-use-case-gate`](./growth-and-moat/ai-use-case-gate) | Growth & Moat | Go/no-go gate for AI builds in GTM: constraint check, ship gate, capability-ladder placement, guardrails |

More coming. The roadmap follows the stage folders: each gets skills for its diagnostic, its data foundation, and its highest-leverage plays.

## Principles

These skills follow the rules we hold in client work:

1. **Deterministic first.** An LLM call has to justify itself against a deterministic alternative.
2. **Evidence over vibes.** Claims carry sources; scores carry rubrics; signals carry dates.
3. **The dossier describes, never reasons.** Data assembly and judgment are separate steps.
4. **Stage before playbook.** Diagnose where you are before choosing what to run.

## License

MIT
