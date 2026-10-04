#!/usr/bin/env python3
"""
score_prospect.py, Phase 7 deliverable.

Takes a domain (or CSV of domains) plus a discriminator.json produced in Phase 7,
and returns a fit_score per archetype using the SAME public signals the
discriminator was built on.

This is a scaffold. The signal-extraction functions are intentionally left as
clearly marked stubs because the real implementation pulls each signal through
your enrichment providers (scraper / job-posting data / LinkedIn data / registries).
Wire each stub to its provider per reference/enrichment-providers.md. Keep the
deterministic-first rule: html2text + regex before any paid call.

discriminator.json schema (one object per archetype):
{
  "archetype": "two-state legal-ops shop",
  "threshold": 0.60,
  "signals": [
    {"key": "state_registrations_18mo", "weight": 0.55, "extractor": "registrations", "params": {"min": 2}},
    {"key": "compliance_role_6mo",      "weight": 0.45, "extractor": "careers_role", "params": {"keywords": ["compliance","GRC"]}}
  ]
}

Usage:
    python score_prospect.py --discriminator discriminator.json --domain acme.com
    python score_prospect.py --discriminator discriminator.json --csv prospects.csv --out scored.csv
"""

import argparse
import json
import sys


# ---------------------------------------------------------------------------
# Signal extractors. Each returns 1 (signal present) or 0 (absent) for a domain.
# Replace the stub bodies with real provider / scraper / registry pulls.
# Deterministic-first: try html2text + regex before any paid provider.
# ---------------------------------------------------------------------------

def extract_registrations(domain: str, params: dict) -> int:
    """STUB: count public professional/regulatory registrations in prior 18mo.
    Wire to the relevant registry source (e.g. SoS portal, KvK, DNB register).
    Return 1 if count >= params.get('min', 1) else 0."""
    raise NotImplementedError("wire extract_registrations to its registry source")


def extract_careers_role(domain: str, params: dict) -> int:
    """STUB: is a role matching params['keywords'] posted in the prior N months?
    Deterministic-first: html2text on /careers, regex the keywords; fall back to
    theirstack / predictleads only on the residual. Return 1 if present else 0."""
    raise NotImplementedError("wire extract_careers_role to careers scrape + theirstack")


def extract_tech_change(domain: str, params: dict) -> int:
    """STUB: did the company adopt/drop a platform in the window? (builtwith/HG)."""
    raise NotImplementedError("wire extract_tech_change to builtwith / HG Insights")


def extract_github_quiet(domain: str, params: dict) -> int:
    """STUB: did a relevant public repo go quiet >= params['months']? (GitHub API)."""
    raise NotImplementedError("wire extract_github_quiet to the GitHub API")


EXTRACTORS = {
    "registrations": extract_registrations,
    "careers_role": extract_careers_role,
    "tech_change": extract_tech_change,
    "github_quiet": extract_github_quiet,
}


def score_domain(domain: str, discriminator: list) -> dict:
    """Return {archetype: {"fit_score": float, "looks_like": bool, "signals": {...}}}."""
    result = {}
    for arch in discriminator:
        per_signal, fit = {}, 0.0
        for s in arch["signals"]:
            fn = EXTRACTORS.get(s["extractor"])
            if fn is None:
                raise SystemExit(f"unknown extractor: {s['extractor']}")
            present = int(fn(domain, s.get("params", {})))
            per_signal[s["key"]] = present
            fit += s["weight"] * present
        result[arch["archetype"]] = {
            "fit_score": round(fit, 3),
            "looks_like": fit >= arch["threshold"],
            "signals": per_signal,
        }
    return result


def main():
    ap = argparse.ArgumentParser(description="Score a prospect domain against archetype discriminators.")
    ap.add_argument("--discriminator", required=True, help="path to discriminator.json")
    ap.add_argument("--domain", help="single domain to score")
    ap.add_argument("--csv", help="CSV with a 'domain' column to score in bulk")
    ap.add_argument("--out", help="optional output CSV for --csv mode")
    args = ap.parse_args()

    with open(args.discriminator) as f:
        discriminator = json.load(f)

    if args.domain:
        print(json.dumps(score_domain(args.domain, discriminator), indent=2))
    elif args.csv:
        import pandas as pd
        df = pd.read_csv(args.csv)
        rows = []
        for d in df["domain"]:
            scores = score_domain(d, discriminator)
            row = {"domain": d}
            for arch, v in scores.items():
                row[f"fit::{arch}"] = v["fit_score"]
                row[f"looks_like::{arch}"] = v["looks_like"]
            rows.append(row)
        out = pd.DataFrame(rows)
        if args.out:
            out.to_csv(args.out, index=False)
            print(f"Wrote {args.out}", file=sys.stderr)
        else:
            print(out.to_string(index=False))
    else:
        ap.error("provide --domain or --csv")


if __name__ == "__main__":
    main()
