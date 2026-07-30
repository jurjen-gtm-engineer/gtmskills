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
| [`gtm-readiness-scan`](./assessments/gtm-readiness-scan) | Assessments | GTM maturity assessment: 24-question Quick Scan or full 120-question Deep Scan interview. 8 domains scored 0-5, readiness index, company archetype, and which stage folder to start in |
| [`bowtie-benchmark`](./assessments/bowtie-benchmark) | Assessments | Your 12 funnel metrics against CR1-CR8 benchmarks for your ACV band, with a per-metric leak diagnosis |
| [`crm-scorecard`](./assessments/crm-scorecard) | Assessments | Computes CR1-CR8 from your actual CRM export (any CRM), cohort-first, benchmarked, with a data-quality preflight |
| [`spiced-call-scorecard`](./assessments/spiced-call-scorecard) | Assessments | Scores call transcripts on the five SPICED dimensions 0-3 with verbatim evidence, plus team-level pattern analysis |
| [`gtm-diagnostic`](./assessments/gtm-diagnostic) | Assessments | The full 5-week GTM diagnostic sprint: normalized bowtie, cohort-first CR1-CR8, Swiss-Cheese causal model, probabilistic forecast, and a 30-60-90 plan ordered by probability lift. Ships a complete fictional worked example |
| [`customer-dossier`](./product-market-fit/customer-dossier) | Product-Market Fit | Builds a ground-truth customer dossier per account: one timeline, provenance on every field, conflicts surfaced. The foundation for ICP analysis |
| [`gtm-ai-brief`](./gtm-fit/gtm-ai-brief) | GTM Fit | Turns a recurring manual GTM task into a written, testable AI brief (Trigger / Inputs / Steps / Output / Guardrails) |
| [`compound-growth-check`](./growth-and-moat/compound-growth-check) | Growth & Moat | Classifies your ARR trajectory (compounding / decaying) from 6+ quarters and places you on the 10-state growth ladder |
| [`ai-use-case-gate`](./growth-and-moat/ai-use-case-gate) | Growth & Moat | Go/no-go gate for AI builds in GTM: constraint check, ship gate, capability-ladder placement, guardrails |
| [`icp-agent`](./product-market-fit/icp-agent) | Product-Market Fit | Red/Yellow/Green ICP definition with a weighted scoring model |
| [`icp-objection-mapping`](./product-market-fit/icp-objection-mapping) | Product-Market Fit | Role-plays your skeptical ICP before campaigns, so objections get preempted in the copy |
| [`conversational-intelligence`](./product-market-fit/conversational-intelligence) | Product-Market Fit | Structured intelligence from call transcripts: handoff, competitive, expansion, closed-lost |
| [`blueprint-swarm`](./product-market-fit/blueprint-swarm) | Product-Market Fit | Parallel sub-agent analysis of hundreds of calls/records with an adversarial hallucination auditor |
| [`meeting-prep`](./gtm-fit/meeting-prep) | GTM Fit | Discovery-call prep: research, fit assessment, SPICED hypotheses, six non-negotiable questions |
| [`battlecard-builder`](./gtm-fit/battlecard-builder) | GTM Fit | Competitive battlecard in 30 minutes |
| [`research-playbook`](./gtm-fit/research-playbook) | GTM Fit | The 10-minute per-prospect signal research method |
| [`qa-checklist`](./gtm-fit/qa-checklist) | GTM Fit | Ship-ready cold email QA standard with scoring |
| [`follow-up-sequences`](./gtm-fit/follow-up-sequences) | GTM Fit | Multi-touch sequence strategy with value-prop rotation |
| [`claygent-prompt-generator`](./gtm-fit/claygent-prompt-generator) | GTM Fit | Cache-optimized Claygent prompts that cut per-row enrichment cost |
| [`claygent-builder`](./gtm-fit/claygent-builder) | GTM Fit | Builds and tests Claygent enrichment agents end to end |
| [`playbook-generator`](./gtm-fit/playbook-generator) | GTM Fit | Cannonball GTM playbook engine: 6-phase EDP workflow producing intelligence-driven PQS/PVP playbooks (methodology by Jordan Crawford, Blueprint GTM; engine only) |
| [`epistemic-context-grounding`](./growth-and-moat/epistemic-context-grounding) | Growth & Moat | Ground decisions in verified domain knowledge before designing (by Jacob Dietle, MIT) |
| [`context-gap-analysis`](./growth-and-moat/context-gap-analysis) | Growth & Moat | Enumerate required context and verify it exists before acting (by Jacob Dietle, MIT) |

## Sibling repos

Two more of our skill libraries are already public and complement this one: [coldoutboundskills](https://github.com/growthenginenowoslawski/coldoutboundskills) (30 skills for cold outbound: domain setup, list building, deliverability, campaign craft) and its companion ABM library abxskills (13 skills for account-based engines). Skills that live there are not duplicated here.

More coming. The roadmap follows the stage folders: each gets skills for its diagnostic, its data foundation, and its highest-leverage plays.

## Principles

These skills follow the rules we hold in client work:

1. **Deterministic first.** An LLM call has to justify itself against a deterministic alternative.
2. **Evidence over vibes.** Claims carry sources; scores carry rubrics; signals carry dates.
3. **The dossier describes, never reasons.** Data assembly and judgment are separate steps.
4. **Stage before playbook.** Diagnose where you are before choosing what to run.

## License

MIT
