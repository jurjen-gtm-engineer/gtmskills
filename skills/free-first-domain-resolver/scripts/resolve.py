#!/usr/bin/env python3
"""Free-first domain resolver, the waterfall orchestrator.

Reads a CSV of company names, runs the cost waterfall (existing -> owned table ->
Knowledge Graph -> Serper -> Places), verifies every candidate against the page,
stops on the first CONFIRMED, and refuses to guess: rows it can't confirm land
in needs_review; name-matched-but-ambiguous rows land in the ambiguous bucket
for the model/sub-agent tier.

Usage:
  python3 resolve.py --input in.csv --output out.csv \
      --name-col company [--zip-col zip] [--city-col city] \
      [--phone-col phone] [--domain-col domain] [--owned-db data/owned.sqlite]
"""
from __future__ import annotations

import argparse
import csv
import os
import sys

import calibration as C
import sources as S
import verify as V


def confidence(verdict: dict) -> float:
    if verdict["verdict"] == "CONFIRMED":
        return round(min(1.0, verdict["name_match"] / 100 *
                         (0.6 + 0.1 * verdict["corroborators"])), 3)
    if verdict["verdict"] == "MAYBE":
        return round(min(0.6, verdict["name_match"] / 100 * 0.6), 3)
    return 0.0


def resolve_row(row, cols, owned_conn, keys):
    name = (row.get(cols["name"]) or "").strip()
    if not name:
        return {"status": "needs_review", "reason": "empty_name"}
    zip_code = row.get(cols["zip"]) if cols["zip"] else None
    city = row.get(cols["city"]) if cols["city"] else None
    phone = row.get(cols["phone"]) if cols["phone"] else None
    existing = row.get(cols["domain"]) if cols["domain"] else None
    hint = " ".join(filter(None, [city, zip_code]))

    maybes = []

    def verify_tier(cands):
        """Verify a tier's candidates; return (confirmed_verdicts, also collect MAYBEs)."""
        confirmed = []
        seen = set()
        for cand in cands:
            d = cand.get("domain")
            if not d or d in seen:
                continue
            seen.add(d)
            v = V.verify_candidate(name, cand, expected_phone=phone or cand.get("phone"))
            v["source"] = cand["source"]
            v["phone_match"] = "phone_match" in v["signals"]
            if v["verdict"] == "CONFIRMED":
                confirmed.append(v)
            elif v["verdict"] == "MAYBE":
                maybes.append(v)
        return confirmed

    def settle(confirmed):
        """Pick a winner from a tier's confirmed verdicts, or None if genuinely ambiguous."""
        if not confirmed:
            return None
        domains = {v["domain"] for v in confirmed}
        if len(domains) == 1:
            return confirmed[0]
        # multiple distinct domains confirmed -> only OK if phone uniquely disambiguates
        phone_hits = [v for v in confirmed if v.get("phone_match")]
        if len(phone_hits) == 1:
            return phone_hits[0]
        return None  # a dozen live candidates, nothing proves which -> ambiguous

    # tier 0-2: authoritative sources (existing / owned table / Knowledge Graph).
    # First confirmation wins -- the source already "knows" the domain.
    for tier in (
        S.from_existing(existing),
        S.from_owned_table(owned_conn, name, zip_code),
        S.from_knowledge_graph(name, keys["kg"]),
    ):
        confirmed = verify_tier(tier)
        if confirmed:
            return _confirmed(settle(confirmed) or confirmed[0])

    # tier 3-4: search tiers. Here multiple confirmations is the wrong-domain risk,
    # so settle() requires a unique winner; otherwise the row is ambiguous.
    for tier in (
        S.from_serper(name, keys["serper"], hint),
        S.from_places(name, keys["places"], hint),  # also the geographic-escalation phone
    ):
        confirmed = verify_tier(tier)
        winner = settle(confirmed)
        if winner:
            return _confirmed(winner)
        if confirmed:  # >1 confirmed, no unique winner -> feed the judge
            for v in confirmed:
                maybes.append(v)

    # nothing confirmed. Distinguish "ambiguous" (real candidates, judge can decide)
    # from "needs_review" (nothing plausible at all).
    if maybes:
        # dedupe candidate domains for the judge
        cands = sorted({m["domain"] for m in maybes})
        best = max(maybes, key=lambda m: (m["name_match"], m["corroborators"]))
        return {
            "status": "ambiguous",
            "resolved_domain": "",
            "candidates": "|".join(cands),
            "source_tier": "multiple",
            "confidence": confidence(best),
            "signals": ";".join(best["signals"]),
        }
    return {"status": "needs_review", "resolved_domain": "", "candidates": "",
            "source_tier": "", "confidence": 0.0, "signals": "no_candidate_verified"}


def _confirmed(v):
    return {
        "status": "confirmed",
        "resolved_domain": v["domain"],
        "candidates": v["domain"],
        "source_tier": v["source"],
        "confidence": confidence(v),
        "signals": ";".join(v["signals"]),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--name-col", required=True)
    ap.add_argument("--zip-col")
    ap.add_argument("--city-col")
    ap.add_argument("--phone-col")
    ap.add_argument("--domain-col")
    ap.add_argument("--owned-db")
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    cols = {"name": args.name_col, "zip": args.zip_col, "city": args.city_col,
            "phone": args.phone_col, "domain": args.domain_col}
    keys = {"kg": os.getenv("GOOGLE_KG_API_KEY"),
            "serper": os.getenv("SERPER_API_KEY"),
            "places": os.getenv("GOOGLE_PLACES_API_KEY")}

    skipped = [t for t, k in (("knowledge_graph", keys["kg"]), ("serper", keys["serper"]),
                              ("places", keys["places"])) if not k]
    if skipped:
        print(f"[warn] no API key for: {', '.join(skipped)}, those tiers are skipped; "
              f"rows needing them will land in needs_review.", file=sys.stderr)

    owned_conn = S.open_owned_db(args.owned_db)
    if args.owned_db and owned_conn is None:
        print(f"[warn] owned table not found at {args.owned_db}, tier 1 skipped.",
              file=sys.stderr)

    with open(args.input, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = reader.fieldnames or []
    if args.limit:
        rows = rows[: args.limit]

    extra = ["resolved_domain", "status", "source_tier", "confidence", "signals", "candidates"]
    out_fields = fieldnames + [c for c in extra if c not in fieldnames]

    base, _ = os.path.splitext(args.output)
    counts = {"confirmed": 0, "ambiguous": 0, "needs_review": 0}
    all_out, ambiguous, needs_review = [], [], []

    for i, row in enumerate(rows, 1):
        res = resolve_row(row, cols, owned_conn, keys)
        merged = dict(row)
        merged.update({k: res.get(k, "") for k in extra})
        all_out.append(merged)
        counts[res["status"]] = counts.get(res["status"], 0) + 1
        if res["status"] == "ambiguous":
            ambiguous.append(merged)
        elif res["status"] == "needs_review":
            needs_review.append(merged)
        if i % 50 == 0:
            print(f"  …{i}/{len(rows)}  "
                  f"confirmed={counts['confirmed']} "
                  f"ambiguous={counts['ambiguous']} "
                  f"needs_review={counts['needs_review']}", file=sys.stderr)

    _write(args.output, out_fields, all_out)
    if ambiguous:
        _write(f"{base}.ambiguous.csv", out_fields, ambiguous)
    if needs_review:
        _write(f"{base}.needs_review.csv", out_fields, needs_review)

    n = len(rows) or 1
    print(f"\nDone. {len(rows)} rows.")
    print(f"  confirmed     {counts['confirmed']:>6}  ({counts['confirmed']*100//n}%)")
    print(f"  ambiguous     {counts['ambiguous']:>6}  -> {base}.ambiguous.csv (run sub-agent judge)")
    print(f"  needs_review  {counts['needs_review']:>6}  -> {base}.needs_review.csv (human)")
    if skipped:
        print(f"  note: skipped tiers (no key): {', '.join(skipped)}")


def _write(path, fields, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)


if __name__ == "__main__":
    main()
