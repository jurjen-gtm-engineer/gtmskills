---
name: free-first-domain-resolver
description: Resolve a list of company names to verified domains for a fraction of a cent per name instead of a per-row vendor fee. Runs a cost waterfall (owned Google Maps table and Google Knowledge Graph for free, then one cheap search, then Google Places) and verifies every domain against what the page declares about itself (title, Open Graph, JSON-LD), never the SSL certificate. Refuses to guess: anything it cannot confirm is flagged "needs review" instead of returning a confident wrong domain. Use when someone has a CSV of company names and needs domains (the same move works for LinkedIn URLs and parent companies). Based on Jordan Crawford's free-first resolver idea (Blueprint GTM). Not for finding contact emails or enriching people.
metadata:
  version: "1.0"
---

# Free-First Domain Resolver

Company name to domain for a whole list: cheapest source first, verified, with a hard refusal instead of a guess. The idea comes from Jordan Crawford's *On the Edge* ([edge.blueprintgtm.com](https://edge.blueprintgtm.com)). The code and the thresholds here are our own build.

**Why this exists.** Per-row vendors charge per lookup and do not check the answer. Most rows clear on free sources, and every domain can be verified against the site itself. A wrong domain is worse than a blank: a human fixes a blank in a minute, while a confident wrong domain poisons every later step. So this tool refuses when it is not sure.

## The waterfall (stop on first CONFIRMED)

| Tier | Source | Cost | Notes |
|---|---|---|---|
| 0 | **Existing** domain on the row | free | a candidate to verify, not to trust |
| 1 | **Owned local table** (a Google Maps export you already have) | free | small-business tail, plus the phone that pins geography |
| 2 | **Google Knowledge Graph** API | free within its daily quota | returns the official site for companies Google knows |
| 3 | **Serper** (one Google search) | a fraction of a cent | pull the candidate, let verification throw out the rest |
| 4 | **Google Places** Text Search | a fraction of a cent | new or non-US companies not in the owned table; returns website and phone |
| 5 | **Model judge** (semantic remainder only) | sub-agents | parent vs subsidiary, rebrand, directory vs official. Most rows never reach it |

Every tier costs more than the one above it, and most of a list clears in tiers 1 and 2. Check the live price pages before a big run; prices change.

**Spend rule:** free when it is right and fast, a fraction of a cent when that makes it sure, never a flat vendor fee for work the website will confirm.

## Verification: ask the page, not the certificate

The Python pipeline fetches each candidate (deterministic: `requests` plus an HTML parse) and scores **page-declared identity**:

- `<title>`, Open Graph `og:site_name` and `og:title` name match: the free signal that fires most often
- JSON-LD `Organization` (name plus `sameAs` LinkedIn or Wikipedia): strong corroboration
- DNS and MX liveness: a real running business
- phone and address: the geographic confirmer (which "Riverside Dental")
- redirects followed to the final domain (`gong.com` to `gong.io`)

**Never the SSL certificate.** It is often blank on brands and always uninformative on free certificates. It names the issuer, not the owner.

## How to run

```bash
cd skills/free-first-domain-resolver
python3 -m pip install -r requirements.txt

# 1. (once) build the owned free table from a Google Maps export
python3 scripts/build_owned_table.py --input ~/data/google_maps_export.csv --db data/owned.sqlite

# 2. resolve a list. Input CSV needs a name column; zip, city, phone and domain are optional.
python3 scripts/resolve.py \
  --input companies.csv --output resolved.csv \
  --name-col company --zip-col zip --owned-db data/owned.sqlite
```

`resolve.py` writes three files next to `--output`:

- `resolved.csv`: every row plus `resolved_domain, status, source_tier, confidence, signals, phone`
- `resolved.needs_review.csv`: nothing could confirm, a human fixes these
- `resolved.ambiguous.csv`: the name matched but there are several live candidates or a parent vs subsidiary question. This goes to the model tier

### API keys (environment variables, all optional)

- `GOOGLE_KG_API_KEY`: Knowledge Graph Search API (enable it on your Google Cloud project first)
- `SERPER_API_KEY`: Serper.dev (tier 3)
- `GOOGLE_PLACES_API_KEY`: Places Text Search (tier 4)

With zero keys it still runs tiers 0 and 1 plus verification. Rows that need search land in `needs_review`.

## The model tier (sub-agents, not a model call from Python)

After `resolve.py`, spawn sub-agents of your coding agent over `resolved.ambiguous.csv` only. For each ambiguous row give the sub-agent the name, the live candidates and the page-declared identity for each, and ask it to pick the official domain or return `needs_review`. Default to `needs_review` when uncertain. Batch about 25 rows per sub-agent. This is the only expensive tier and most rows never reach it.

## Calibration

The defaults are explicit and tunable. They live in `references/calibration.md` and `scripts/calibration.py`:

- **Short-circuit:** a source that knows the domain, the page agrees, not disqualified: accept, no model.
- **Name match:** strong at 85 or more, maybe from 60 to 84, reject under 60 (token-set ratio), with a **generic-name guard** (a common name needs a corroborator: phone, address or `sameAs`).
- **Geographic escalation:** doubt about which location is settled by a Places phone match.
- **CONFIRMED** needs a strong name match AND at least one corroborator AND no disqualifier. Anything else is `needs review`.

Tune these on a hand-labeled slice before you trust a big run.

## Discipline (do not skip)

1. **Never emit a guess.** No confirmation means `needs review`.
2. **Verify against the page, never the certificate.**
3. **Own the data, do not rent each lookup.** Build the owned table from your own Google Maps scrape, and do not redistribute data files you bought or were given.
4. **Log what you dropped.** If a run skips a tier (missing key, rate limit), say so in the summary. Silent truncation reads as "covered everything".
5. The same move resolves LinkedIn URLs, parent companies and rebrands. **Verify, do not buy.**

## Files

- `scripts/resolve.py`: orchestrator and CLI (the waterfall and the bucketing)
- `scripts/sources.py`: discovery tiers (existing, owned table, Knowledge Graph, Serper, Places)
- `scripts/verify.py`: page-declared-identity verification, DNS, redirects, disqualifiers
- `scripts/calibration.py`: thresholds, generic-name list, directory and government blacklist
- `scripts/build_owned_table.py`: builds the free local table from a Google Maps export
- `references/calibration.md`: the thresholds, explained
- `requirements.txt`

## Credits

The free-first waterfall, "verify against the page, not the certificate" and "refuse instead of guess" are Jordan Crawford's ideas, published in *On the Edge* by [Blueprint GTM](https://blueprintgtm.com). He ships his own installed tool with his own tuned thresholds. This is an independent build with our own defaults. For a Google Maps export, see the list-building skills in [coldoutboundskills](https://github.com/growthenginenowoslawski/coldoutboundskills) by Growth Engine X.
