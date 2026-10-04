<p align="center"><img src="https://img.shields.io/badge/gtmskills-Open%20source%20GTM%20skills%20for%20coding%20agents-0b1f3a?style=flat-square&labelColor=24292f" alt="gtmskills: open source GTM skills for coding agents" /></p>

<h3 align="center">Find what holds your growth back, then build the fix</h3>

<p align="center">55 go-to-market skills for Claude Code and other coding agents. Each one states what it needs, does one job, and leaves a file you can use: a scorecard, an ICP, a cost estimate, a message. Sorted by growth stage, so you run what fits where you are.</p>

<p align="center"><a href="docs/getting-started.md"><b>Install a skill</b></a> &nbsp;·&nbsp; <a href="https://cal.com/jurjen-koning-neuralflow/30min?utm_source=gtmskills"><b>Book a call</b></a></p>

<p align="center"><sub>✓&nbsp;Free&nbsp;and&nbsp;MIT&nbsp;licensed &nbsp; ✓&nbsp;One&nbsp;command&nbsp;to&nbsp;install &nbsp; ✓&nbsp;Credits&nbsp;on&nbsp;every&nbsp;borrowed&nbsp;idea</sub></p>

```bash
npx skills add jurjen-gtm-engineer/gtmskills --skill gtm-readiness-scan -g
```

## Why this exists

Most GTM prompts give advice. These skills do the work and show their sources. A score comes with the quote behind it. A cost comes with the row math. A method that came from someone else carries that person's name and a link.

The stage comes first. A scale playbook before product-market fit burns money. A founder-led motion after GTM fit caps growth. So every skill sits in a stage, and the assessments tell you which stage you are in.

## A retyped prompt, a template, or a skill

| | **gtmskills** | A prompt you retype | A template |
|---|:---:|:---:|:---:|
| **Installs into Claude Code, Codex, Cursor and other skills.sh hosts with one command** | ✅ | ✅ | ❌ |
| **Says which inputs it needs and stops when they are missing** | ✅ | ❌ | ❌ |
| **Leaves a file: a scorecard, a profile, an estimate, a message** | ✅ | ❌ | ❌ |
| **Runs the math in a script you can read and rerun** | ✅ | ❌ | ❌ |
| **Names the source of every framework it uses** | ✅ | ❌ | ❌ |

Scripts ship with the skills where a number has to be right: the cost estimates, the growth check, the call scoring and the domain resolver.

## Ask in your agent

**Find out where you stand.** Say "run the GTM readiness scan" or "benchmark my funnel". You answer the questions, the agent scores them and names the two weakest spots.

**Price the work before you start.** Say "what will the data cost to map 3,000 accounts?" The agent fills a scope file, runs the calculator and gives you a range for the proposal.

**Turn a signal into a message.** Say "write a PQS email for this prospect" and paste what you know. The agent picks the honest lane, writes the email and checks it against the rules.

## Three steps

| 1. Install | 2. Find your stage | 3. Run the skill that fits |
|---|---|---|
| `npx skills add jurjen-gtm-engineer/gtmskills -g` installs all 55. Add `--skill <name>` for one. | Run `gtm-readiness-scan` or `bowtie-benchmark`. The result names your stage. | Pick from the stage table below, or read [docs/stages.md](docs/stages.md). |

More in [docs/getting-started.md](docs/getting-started.md).

## The skills

### Assessments (5)

Start here. Each one tells you where your revenue engine stands and which skills to run next.

| Skill | What it does | Credit |
|---|---|---|
| [`gtm-readiness-scan`](skills/gtm-readiness-scan) | A 24-question quick scan or a 120-question deep scan. Scores 8 domains from 0 to 5 and names your weakest ones. |  |
| [`bowtie-benchmark`](skills/bowtie-benchmark) | Asks for your funnel metrics, benchmarks each one for your deal size, and writes a scorecard with the biggest leaks. | Benchmarks recreated from Winning by Design |
| [`crm-scorecard`](skills/crm-scorecard) | Turns a raw CRM export from any CRM into bowtie conversion rates, benchmarked, with the top two leaks named. | Built on Winning by Design's bowtie |
| [`spiced-call-scorecard`](skills/spiced-call-scorecard) | Scores call transcripts on the five SPICED dimensions with word-for-word evidence, and writes the follow-up questions. | SPICED is a Winning by Design framework |
| [`gtm-diagnostic`](skills/gtm-diagnostic) | Measures the full revenue engine, names the main cause, and produces a 30-60-90 day plan. | Built on Winning by Design's frameworks |

### Product-market fit (6)

Prove who to sell to and why they buy.

| Skill | What it does | Credit |
|---|---|---|
| [`customer-dossier`](skills/customer-dossier) | One timeline per account from CRM, calls, billing, usage and support, with the source on every field. | Concept from Jordan Crawford's The Dossier |
| [`win-loss-rewind`](skills/win-loss-rewind) | Works back from won, lost and churned customers to the situations that predict a buyer, checked on a 20% holdout. | Method by Jordan Crawford, Blueprint GTM |
| [`icp-agent`](skills/icp-agent) | Defines your ideal customer profile as red, yellow and green, with a weighted scoring model. | Red, yellow, green from Mark Roberge's Science of Scaling |
| [`icp-objection-mapping`](skills/icp-objection-mapping) | Role-plays your most skeptical buyer before a campaign, so the copy answers the objections first. |  |
| [`conversational-intelligence`](skills/conversational-intelligence) | Pulls handoff notes, competitor mentions, expansion signals and loss reasons out of call transcripts. |  |
| [`blueprint-swarm`](skills/blueprint-swarm) | Reads hundreds of calls in parallel and checks its own output for made-up claims. | Based on Jordan Crawford's open-source Blueprint Swarm |

### GTM fit (13)

Build a sales motion that repeats and pays for itself.

| Skill | What it does | Credit |
|---|---|---|
| [`meeting-prep`](skills/meeting-prep) | A research brief for any sales meeting, with SPICED questions written for that contact and company. | Uses Winning by Design's SPICED and Science of Scaling's six questions |
| [`battlecard-builder`](skills/battlecard-builder) | A competitor battlecard in 30 minutes that reps can use in the middle of a call. | Three-card framework from Science of Scaling |
| [`pqs-pvp-messaging`](skills/pqs-pvp-messaging) | Turns one signal or data point about a prospect into a cold email that mirrors their situation or hands them an insight. | PQS and PVP by Jordan Crawford, voice rules by Josh Braun |
| [`research-playbook`](skills/research-playbook) | A 10-minute method to find one real signal per prospect for a cold email. |  |
| [`qa-checklist`](skills/qa-checklist) | The standard a cold email has to pass before it ships, with a score. |  |
| [`follow-up-sequences`](skills/follow-up-sequences) | A multi-touch sequence where each email brings a new reason to reply. |  |
| [`tam-data-cost-estimate`](skills/tam-data-cost-estimate) | Prices a market map before you build it: one-off data cost, monthly cost and subscriptions, each as a range. |  |
| [`crm-enrichment-cost-estimate`](skills/crm-enrichment-cost-estimate) | Estimates the yearly Clay credits and actions to enrich the records already in your CRM. | Model follows Clay's public scoping template |
| [`free-first-domain-resolver`](skills/free-first-domain-resolver) | Turns company names into verified domains, free sources first, and refuses to guess when it cannot confirm. | Idea by Jordan Crawford, Blueprint GTM |
| [`claygent-prompt-generator`](skills/claygent-prompt-generator) | Writes Clay research prompts in the order that keeps the cost per row low. |  |
| [`claygent-builder`](skills/claygent-builder) | Builds a Clay research agent, tests it, and improves it until the output is good enough to trust. |  |
| [`gtm-ai-brief`](skills/gtm-ai-brief) | Turns a task you keep doing by hand into a written brief an AI can run, tested before it ships. |  |
| [`playbook-generator`](skills/playbook-generator) | One company domain in, a full outbound playbook out: pain segments, data sources and messages. | Method by Jordan Crawford, Blueprint GTM |

### Growth and moat (5)

Scale the motion, measure it, and defend it.

| Skill | What it does | Credit |
|---|---|---|
| [`outcome-seller-scoring`](skills/outcome-seller-scoring) | Scores recorded calls per rep on SPICED, then simulates what closing the coaching gap is worth in revenue. | Built on Winning by Design's SPICED and Outcome Seller webinar |
| [`compound-growth-check`](skills/compound-growth-check) | Takes six or more quarters of revenue and tells you whether growth is compounding or decaying. | Growth states from Winning by Design |
| [`ai-use-case-gate`](skills/ai-use-case-gate) | A go or no-go check for an AI idea before anyone builds it. |  |
| [`epistemic-context-grounding`](skills/epistemic-context-grounding) | Makes the AI check what is actually known before it designs a solution. | By Jacob Dietle, MIT licence |
| [`context-gap-analysis`](skills/context-gap-analysis) | Lists what the AI needs to know, checks what exists, and finds the simplest way forward. | By Jacob Dietle, MIT licence |

### Clay prompts (26)

Small research and scoring prompts for Clay columns and Claygent. One job each.

| Skill | What it does | Credit |
|---|---|---|
| [`prompt-engineering-rules`](skills/prompt-engineering-rules) | Five rules for enrichment prompts that stay cheap and reliable at volume. | Rules taught by Eric Nowoslawski, Growth Engine X |
| [`metaprompter`](skills/metaprompter) | Asks the AI what context, examples and edge cases a prompt is missing, then rewrites it. | Technique taught by Eric Nowoslawski, Growth Engine X |
| [`b2b-or-b2c`](skills/b2b-or-b2c) | Classifies a company as B2B, B2C or both, and suggests the tone to match. |  |
| [`saas-identification`](skills/saas-identification) | Decides whether a company is SaaS, and what that means for the message. |  |
| [`company-mission`](skills/company-mission) | Pulls a one-sentence mission from a company's LinkedIn or About page. |  |
| [`company-goals`](skills/company-goals) | Reads a company's open jobs and infers what it is trying to do this year. |  |
| [`ideal-customer-profiles`](skills/ideal-customer-profiles) | Finds the buyers, users and industries a company serves, from its public content. |  |
| [`pricing-strategy`](skills/pricing-strategy) | Pulls a company's pricing model, tiers and sales motion from its pricing page. |  |
| [`recent-news`](skills/recent-news) | Finds a company's most relevant recent news and turns it into outreach angles. |  |
| [`glassdoor-rating`](skills/glassdoor-rating) | Finds and reads a company's Glassdoor rating, and says when it is safe to mention. |  |
| [`data-point-research`](skills/data-point-research) | Designs fit signals that data providers do not sell, with a prompt to detect each one. | "Build data you can't buy" by Petra Hajal |
| [`plg-company-detection`](skills/plg-company-detection) | Detects whether a company is product-led: freemium, free trial, hybrid or sales-led. | Approach by Petra Hajal |
| [`multi-product-detection`](skills/multi-product-detection) | Detects whether a company sells one product, several, or a suite. | Approach by Petra Hajal |
| [`product-complexity-detection`](skills/product-complexity-detection) | Rates how complex a company's product is, from docs, reviews, jobs and pricing. | Approach by Petra Hajal |
| [`pain-qualified-segment`](skills/pain-qualified-segment) | Defines a segment by two to five signals that show active pain, not only company size. | Concept by Jordan Crawford, Blueprint GTM |
| [`list-is-the-message`](skills/list-is-the-message) | Builds a list around one detectable tension, so the message follows from why each lead is on it. | Idea by Jordan Crawford, Blueprint GTM |
| [`customer-evidence-first`](skills/customer-evidence-first) | Builds positioning from the real reasons won customers bought, not from features. | Idea by Jordan Crawford, Blueprint GTM |
| [`permissionless-value-proposition`](skills/permissionless-value-proposition) | Writes outreach that gives a useful insight from public data before it asks for anything. | Concept by Jordan Crawford, Blueprint GTM |
| [`lead-scoring`](skills/lead-scoring) | Designs a lead score from fit, intent and custom signals, with point tables and action tiers. |  |
| [`icp-scoring-dynamic`](skills/icp-scoring-dynamic) | Builds a weighted ICP score from enriched data that returns JSON with hot, warm and nurture tiers. | Approach by Patrick Spychalski, The Kiln |
| [`clean-job-titles`](skills/clean-job-titles) | Turns long LinkedIn job titles into clean titles with seniority and function. |  |
| [`role-focus`](skills/role-focus) | Describes what a job title usually cares about: metrics, pains and authority. |  |
| [`linkedin-posts-summary`](skills/linkedin-posts-summary) | Sums up a prospect's recent LinkedIn posts into themes and hooks you can use. |  |
| [`email-subject-line`](skills/email-subject-line) | Writes three personal subject lines under eight words from prospect research. |  |
| [`email-opening-line`](skills/email-opening-line) | Writes a personal first line that continues from the subject line. |  |
| [`playbook-pitch-generation`](skills/playbook-pitch-generation) | Generates a pitch per account: angle, hook, proof point, objection and next step. | Approach by Patrick Spychalski, The Kiln |

## People and libraries we point you to

We did not make these. We use them, and you should know them. Each link opens the maker's own repo.

| Library | By | What it is |
|---|---|---|
| [GTM workspace skills](https://github.com/eliasstravik/gtm-skills) | Elias Stråvik | One git-backed workspace for your company facts, ICPs and personas, plus saved workflows that run locally or on Vercel. |
| [Call and pipeline audits](https://github.com/zime-ai/zime-gtm-skills) | Zime | One sales call transcript or CRM export in, one audit out, with a quote behind every finding. Covers MEDDICC, BANT, SPICED-style discovery, deal risk and pipeline stage checks. |
| [Cold outbound](https://github.com/growthenginenowoslawski/coldoutboundskills) | Growth Engine X | Eric Nowoslawski's team on domain setup, list building, deliverability and cold email copy. |
| [Clay agent plugins](https://github.com/clay-run/agent-plugins) | Clay | Clay's own skills for tables, workflows, audiences and searches, plus skills from Clay's community. |
| [Clay tables from code](https://github.com/leszek-lammel-advisory/rex) | Leszek Lammel | Rex: design a Clay table as a file, import it, and check what it will cost before it runs. Unofficial, not made by Clay. |
| [GTM engineering skills](https://github.com/getaero-io/gtm-eng-skills) | Deepline | Prospecting, enrichment, scoring and plays that run against a data warehouse. |
| [Revenue orchestration](https://github.com/getcargohq/cargo-skills) | Cargo | Skills for building and running go-to-market workflows in Cargo. |
| [Context OS quickstart](https://github.com/jacob-dietle/gtm-context-os-quickstart) | Jacob Dietle | A starter for a knowledge system your AI builds on over time. Two of his skills ship in our repo, with credit. |
| [Open Source GTM directory](https://github.com/eliasstravik/open-source-gtm) | Elias Stråvik | A community list of public repos for GTM teams: products, agent skills, libraries, templates and learning material. |

The ideas in this repo come from people who taught them first: Jacco van der Kooij and Winning by Design (bowtie, SPICED, growth states), Mark Roberge (Science of Scaling), Jordan Crawford and [Blueprint GTM](https://blueprintgtm.com) (PQS, PVP, win-loss rewind, the playbook method), Eric Nowoslawski and Growth Engine X (prompt rules, cold outbound), Josh Braun (the voice of a cold email), Petra Hajal (data you cannot buy), Patrick Spychalski and The Kiln (scoring in Clay), Jacob Dietle (context systems) and Elias Stråvik (how to ship skills as open source). See [CREDITS.md](CREDITS.md). If we credited you wrongly or missed you, open an issue and we fix it.

## Free, or done with you

| Self-serve | Done with you |
|---|---|
| **Free.** Every skill, MIT licensed. Install, run, change what you like. | **Let's talk.** We run the diagnostic, build the data and the plays with your team, and hand over a system you own. [Book a call](https://cal.com/jurjen-koning-neuralflow/30min?utm_source=gtmskills). |

## Questions

**Which agents does it work with?** Any host that loads skills from skills.sh: Claude Code, Codex, Cursor, OpenCode and others.

**Do I need API keys?** Most skills need none. A few use tools you may already pay for, such as Clay, a search API or a call recorder. Each skill lists its own inputs.

**Can I use the numbers in a deck?** The benchmarks come from the sources named in each skill. Name the source when you use one, and treat vendor numbers as self-reported.

**Something is wrong or missing.** [Open an issue](https://github.com/jurjen-gtm-engineer/gtmskills/issues/new).

## License

[MIT](LICENSE) © 2026 [Jurjen Koning](https://www.linkedin.com/in/jurjenkoning/), Neuralflow. Two skills are by Jacob Dietle and keep his notice.
