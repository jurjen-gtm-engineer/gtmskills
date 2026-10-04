# Get your first result in ten minutes

## What you need

- A coding agent that loads skills from skills.sh: Claude Code, Codex, Cursor, OpenCode or another host.
- Node.js with `npx`.
- Python 3 for the skills that ship a script (the cost estimates, the growth check, call scoring, the domain resolver).

## Install

One skill:

```sh
npx skills add jurjen-gtm-engineer/gtmskills --skill gtm-readiness-scan -g
```

All of them:

```sh
npx skills add jurjen-gtm-engineer/gtmskills -g
```

`-g` installs for your user, so every project finds the skill. Leave it out to install into the current project only. To see what is in the repo without installing, add `--list`.

## Get the first result

In your agent, say:

```
Run the GTM readiness scan, quick version
```

The agent asks 24 questions, scores 8 domains from 0 to 5, names your two weakest domains and tells you which growth stage you are in.

Have funnel numbers at hand? Say:

```
Benchmark my funnel
```

The agent asks for your metrics, compares each one to companies with your deal size, and writes a scorecard with the biggest leaks.

## Pick the next skill

The result names your stage. [stages.md](stages.md) lists the skills per stage and the order we run them in.

## Three good second steps

- **You have won and lost deals in a CRM.** Run `win-loss-rewind` to find the situations that predict a buyer.
- **You are about to build a list.** Run `tam-data-cost-estimate` first, so you know the data cost before you spend it.
- **You have call recordings.** Run `spiced-call-scorecard` on a few calls, or `outcome-seller-scoring` on a whole archive.

## Stay up to date

```sh
npx skills update -g
```

Something not working? [Open an issue](https://github.com/jurjen-gtm-engineer/gtmskills/issues/new).
