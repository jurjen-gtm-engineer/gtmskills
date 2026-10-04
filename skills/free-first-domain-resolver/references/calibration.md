# Calibration

These are this build's own defaults. They are not Jordan Crawford's tuned values. Tune them on a hand-labeled slice before a big run. All values live in `scripts/calibration.py`.

## Name-match cutoffs (token-set ratio, 0 to 100)

| Band | Default | Meaning |
|---|---|---|
| STRONG | ≥ 85 | the page is confidently this company |
| MAYBE | 60 to 84 | needs a corroborator or the model tier |
| REJECT | < 60 | this candidate is the wrong company |

We use a pure-python token-set ratio (no fuzzy-match dependency) plus two special cases:
- **acronym match**: `bmc.org` for "Boston Medical Center", `ssim.com` for "Southside Internal Medicine". First letters of the distinctive tokens == the domain label.
- **domain-label match**: "Anderson Plumbing Heating and Air" → `andersonplumbingheatingandair.com` (the whole mouthful).

## Generic-name guard

A name with fewer than `DISTINCTIVE_TOKEN_FLOOR` (=2) distinctive tokens (after stripping `GENERIC_TOKENS`) can text-match the wrong business. For these, a strong name-match is **not** enough on its own, we require a corroborator (phone match, address, or a `sameAs` identity link). "Summit Roofing" with no city and a dozen live candidates → MAYBE → `needs_review`, never a guess. This is the guard that stops a common name from matching the wrong business.

## Disqualifiers (a candidate is never accepted if…)

- it is a **directory / social / aggregator** (`BLACKLIST_DOMAINS`: linkedin, facebook, yelp, crunchbase, zoominfo, wikipedia, …), a raw top search hit is one of these as often as the real site.
- it is a **gov/.mil portal** and the company name isn't governmental.
- the page is **parked / for-sale / suspended** (`PARKED_MARKERS`).
- **DNS dead** or **unreachable**.

## Corroborators (need ≥ `MIN_CORROBORATORS` = 1)

`og:site_name` name match · JSON-LD `Organization` · `sameAs` link present · MX record · redirect-stable to a real site · phone match.

## Short-circuit (no model call)

A source that *knows* the domain (owned table / Knowledge Graph) + the page agrees + not disqualified → accept immediately. Most of the list clears here without ever touching search or a model.

## Geographic escalation

When the doubt is *which location* (not which company), a fraction-of-a-cent Places lookup returns the phone, and a phone match settles it deterministically, a matching phone beats a model's guess. `PHONE_RESCUES_MAYBE` lets a confirmed phone match rescue a MAYBE name-match.

## The final gate

```
CONFIRMED  iff  name_match ≥ STRONG  AND  corroborators ≥ 1  AND  not disqualified
                (and, if generic name, a phone/address/sameAs corroborator)
MAYBE      ->  ambiguous bucket  (the model / sub-agent tier decides, or needs_review)
REJECT     ->  no candidate; if all candidates reject -> needs_review
```

**The discipline that matters most:** when nothing confirms, return `needs review`. A blank is a row a human fixes in a minute; a confident wrong domain poisons every downstream step. Never emit a guess.

## Cost note (the model tier)

The ambiguous bucket is handed to sub-agents of your coding agent, on a small and cheap model. Do not assume the newest model is the cheapest: check the live price table. Most rows never reach this tier.
