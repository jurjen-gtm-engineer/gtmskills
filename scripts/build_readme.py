#!/usr/bin/env python3
"""Build README.md from catalog.json, so the skill tables never drift from the folders."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
cat = json.loads((ROOT / "catalog.json").read_text())
REPO = "jurjen-gtm-engineer/gtmskills"
CALL = "https://cal.com/jurjen-koning-neuralflow/30min?utm_source=gtmskills"
total = sum(len(g["skills"]) for g in cat["groups"])

out = []
w = out.append
w('<p align="center"><img src="https://img.shields.io/badge/gtmskills-Open%20source%20GTM%20skills%20for%20coding%20agents-0b1f3a?style=flat-square&labelColor=24292f" alt="gtmskills: open source GTM skills for coding agents" /></p>')
w("")
w('<h3 align="center">Find what holds your growth back, then build the fix</h3>')
w("")
w(f'<p align="center">{total} go-to-market skills for Claude Code and other coding agents. Each one states what it needs, does one job, and leaves a file you can use: a scorecard, an ICP, a cost estimate, a message. Sorted by growth stage, so you run what fits where you are.</p>')
w("")
w(f'<p align="center"><a href="docs/getting-started.md"><b>Install a skill</b></a> &nbsp;·&nbsp; <a href="{CALL}"><b>Book a call</b></a></p>')
w("")
w('<p align="center"><sub>✓&nbsp;Free&nbsp;and&nbsp;MIT&nbsp;licensed &nbsp; ✓&nbsp;One&nbsp;command&nbsp;to&nbsp;install &nbsp; ✓&nbsp;Credits&nbsp;on&nbsp;every&nbsp;borrowed&nbsp;idea</sub></p>')
w("")
w("```bash")
w(f"npx skills add {REPO} --skill gtm-readiness-scan -g")
w("```")
w("")
w("## Why this exists")
w("")
w("Most GTM prompts give advice. These skills do the work and show their sources. A score comes with the quote behind it. A cost comes with the row math. A method that came from someone else carries that person's name and a link.")
w("")
w("The stage comes first. A scale playbook before product-market fit burns money. A founder-led motion after GTM fit caps growth. So every skill sits in a stage, and the assessments tell you which stage you are in.")
w("")
w("## A retyped prompt, a template, or a skill")
w("")
w("| | **gtmskills** | A prompt you retype | A template |")
w("|---|:---:|:---:|:---:|")
for row in [
    "Installs into Claude Code, Codex, Cursor and other skills.sh hosts with one command",
    "Says which inputs it needs and stops when they are missing",
    "Leaves a file: a scorecard, a profile, an estimate, a message",
    "Runs the math in a script you can read and rerun",
    "Names the source of every framework it uses",
]:
    yes_prompt = "✅" if row.startswith("Installs") else "❌"
    w(f"| **{row}** | ✅ | {yes_prompt} | ❌ |")
w("")
w("Scripts ship with the skills where a number has to be right: the cost estimates, the growth check, the call scoring and the domain resolver.")
w("")
w("## Ask in your agent")
w("")
w("**Find out where you stand.** Say \"run the GTM readiness scan\" or \"benchmark my funnel\". You answer the questions, the agent scores them and names the two weakest spots.")
w("")
w("**Price the work before you start.** Say \"what will the data cost to map 3,000 accounts?\" The agent fills a scope file, runs the calculator and gives you a range for the proposal.")
w("")
w("**Turn a signal into a message.** Say \"write a PQS email for this prospect\" and paste what you know. The agent picks the honest lane, writes the email and checks it against the rules.")
w("")
w("## Three steps")
w("")
w("| 1. Install | 2. Find your stage | 3. Run the skill that fits |")
w("|---|---|---|")
w(f"| `npx skills add {REPO} -g` installs all {total}. Add `--skill <name>` for one. | Run `gtm-readiness-scan` or `bowtie-benchmark`. The result names your stage. | Pick from the stage table below, or read [docs/stages.md](docs/stages.md). |")
w("")
w("More in [docs/getting-started.md](docs/getting-started.md).")
w("")
w("## The skills")
w("")
for g in cat["groups"]:
    w(f"### {g['name']} ({len(g['skills'])})")
    w("")
    w(g["line"])
    w("")
    w("| Skill | What it does | Credit |")
    w("|---|---|---|")
    for s in g["skills"]:
        w(f"| [`{s['slug']}`](skills/{s['slug']}) | {s['line']} | {s.get('credit', '')} |")
    w("")
w("## People and libraries we point you to")
w("")
w("We did not make these. We use them, and you should know them. Each link opens the maker's own repo.")
w("")
w("| Library | By | What it is |")
w("|---|---|---|")
for o in cat["others"]:
    w(f"| [{o['name']}]({o['url']}) | {o['by']} | {o['line']} |")
w("")
w("The ideas in this repo come from people who taught them first: Jacco van der Kooij and Winning by Design (bowtie, SPICED, growth states), Mark Roberge (Science of Scaling), Jordan Crawford and [Blueprint GTM](https://blueprintgtm.com) (PQS, PVP, win-loss rewind, the playbook method), Eric Nowoslawski and Growth Engine X (prompt rules, cold outbound), Josh Braun (the voice of a cold email), Petra Hajal (data you cannot buy), Patrick Spychalski and The Kiln (scoring in Clay), Jacob Dietle (context systems) and Elias Stråvik (how to ship skills as open source). See [CREDITS.md](CREDITS.md). If we credited you wrongly or missed you, open an issue and we fix it.")
w("")
w("## Free, or done with you")
w("")
w("| Self-serve | Done with you |")
w("|---|---|")
w(f"| **Free.** Every skill, MIT licensed. Install, run, change what you like. | **Let's talk.** We run the diagnostic, build the data and the plays with your team, and hand over a system you own. [Book a call]({CALL}). |")
w("")
w("## Questions")
w("")
w("**Which agents does it work with?** Any host that loads skills from skills.sh: Claude Code, Codex, Cursor, OpenCode and others.")
w("")
w("**Do I need API keys?** Most skills need none. A few use tools you may already pay for, such as Clay, a search API or a call recorder. Each skill lists its own inputs.")
w("")
w("**Can I use the numbers in a deck?** The benchmarks come from the sources named in each skill. Name the source when you use one, and treat vendor numbers as self-reported.")
w("")
w("**Something is wrong or missing.** [Open an issue](https://github.com/jurjen-gtm-engineer/gtmskills/issues/new).")
w("")
w("## License")
w("")
w("[MIT](LICENSE) © 2026 [Jurjen Koning](https://www.linkedin.com/in/jurjenkoning/), Neuralflow. Two skills are by Jacob Dietle and keep his notice.")
w("")
(ROOT / "README.md").write_text("\n".join(out))
print(f"README.md written, {total} skills")
