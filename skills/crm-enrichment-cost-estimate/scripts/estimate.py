#!/usr/bin/env python3
"""CRM enrichment usage estimate: yearly data credits and platform actions.

Deterministic. No network, no dependencies. Follows the model of Clay's public
Data Credit and Actions Scoping Template:

  audience         = CRM volume x share relevant + new records sourced
  field credits    = credits each x coverage x audience x runs per year   (0 on your own API key)
  field actions    = audience x runs per year x 3 if waterfall, else x 1  (coverage and own key do not lower actions)
  signal credits   = credits each x checks per year x audience
  signal actions   = checks per year x audience
  export actions   = exports per year x audience

Signals are counted once, in their own block.

Usage:
  python3 estimate.py --scope scope.json [--out estimate.md]
"""
import argparse
import json
import sys

OBJECTS = ("account", "contact")


def fail(msg):
    sys.exit(f"scope error: {msg}")


def load(path):
    with open(path) as fh:
        scope = json.load(fh)
    if "audience" not in scope:
        fail("'audience' is required")
    for obj in OBJECTS:
        a = scope["audience"].get(obj)
        if a is None:
            fail(f"audience.{obj} is required (use zeros to leave it out)")
        for key in ("crm_volume", "share_relevant"):
            if key not in a:
                fail(f"audience.{obj} misses '{key}'")
        if not 0 <= a["share_relevant"] <= 1:
            fail(f"audience.{obj}.share_relevant must be between 0 and 1")
    for block in ("fields", "signals", "exports"):
        for item in scope.get(block, []):
            if item.get("object") not in OBJECTS:
                fail(f"{block} item {item.get('name', '?')}: object must be 'account' or 'contact'")
    for f in scope.get("fields", []):
        for key in ("name", "credits_each", "runs_per_year"):
            if key not in f:
                fail(f"field {f.get('name', '?')} misses '{key}'")
        if not 0 <= f.get("coverage", 1.0) <= 1:
            fail(f"field {f['name']}: coverage must be between 0 and 1")
    return scope


def estimate(scope):
    aud = {
        o: scope["audience"][o]["crm_volume"] * scope["audience"][o]["share_relevant"]
        + scope["audience"][o].get("new_records", 0)
        for o in OBJECTS
    }
    blocks = {o: {"credits": 0.0, "actions": 0.0, "export_actions": 0.0} for o in OBJECTS}
    signals = {"credits": 0.0, "actions": 0.0}
    rows = []
    for f in scope.get("fields", []):
        n = aud[f["object"]]
        runs = f["runs_per_year"]
        credits = 0.0 if f.get("own_api_key") else f["credits_each"] * f.get("coverage", 1.0) * n * runs
        actions = n * runs * (3 if f.get("waterfall") else 1)
        blocks[f["object"]]["credits"] += credits
        blocks[f["object"]]["actions"] += actions
        rows.append(("field", f["object"], f["name"], credits, actions))
    for s in scope.get("signals", []):
        n = aud[s["object"]]
        credits = s["credits_each"] * s["checks_per_year"] * n
        actions = s["checks_per_year"] * n
        signals["credits"] += credits
        signals["actions"] += actions
        rows.append(("signal", s["object"], s["name"], credits, actions))
    for e in scope.get("exports", []):
        actions = e["per_year"] * aud[e["object"]]
        blocks[e["object"]]["export_actions"] += actions
        rows.append(("export", e["object"], e["name"], 0.0, actions))
    total_credits = sum(b["credits"] for b in blocks.values()) + signals["credits"]
    total_actions = sum(b["actions"] + b["export_actions"] for b in blocks.values()) + signals["actions"]
    return {"audience": aud, "blocks": blocks, "signals": signals, "rows": rows,
            "total_credits": total_credits, "total_actions": total_actions}


def render(scope, r):
    out = [f"# CRM enrichment usage estimate: {scope.get('name', 'unnamed scope')}", ""]
    out += ["## Audience", "", "| Object | Audience |", "|---|---|"]
    for o in OBJECTS:
        out.append(f"| {o.title()}s | {r['audience'][o]:,.0f} |")
    out += ["", "## Line items (per year)", "", "| Type | Object | Name | Data credits | Actions |", "|---|---|---|---|---|"]
    for kind, obj, name, credits, actions in r["rows"]:
        out.append(f"| {kind} | {obj} | {name} | {credits:,.0f} | {actions:,.0f} |")
    out += ["", "## Totals (per year)", "", "| Block | Data credits | Actions | Credits per record |", "|---|---|---|---|"]
    for o in OBJECTS:
        b = r["blocks"][o]
        per = b["credits"] / r["audience"][o] if r["audience"][o] else 0
        out.append(f"| {o.title()} enrichment | {b['credits']:,.0f} | {b['actions']:,.0f} | {per:.1f} |")
    out.append(f"| Signals | {r['signals']['credits']:,.0f} | {r['signals']['actions']:,.0f} | |")
    for o in OBJECTS:
        out.append(f"| {o.title()} exports | 0 | {r['blocks'][o]['export_actions']:,.0f} | |")
    out.append(f"| **Total** | **{r['total_credits']:,.0f}** | **{r['total_actions']:,.0f}** | |")
    cp, ap = scope.get("price_per_credit"), scope.get("price_per_action")
    if cp is not None or ap is not None:
        cur = scope.get("currency", "USD")
        cost = r["total_credits"] * (cp or 0) + r["total_actions"] * (ap or 0)
        out += ["", f"At {cp or 0:g} per credit and {ap or 0:g} per action: {cur} {cost:,.0f} per year."]
    out += ["", "This is an estimate. Real usage depends on the workflows and data sources you pick.",
            "A waterfall that falls through to a second or third paid provider costs more credits than shown.",
            "Credits on your own API key are zero here, but that provider's subscription is a separate cost.", ""]
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--scope", required=True, help="scope JSON file")
    ap.add_argument("--out", help="write the markdown here instead of printing it")
    args = ap.parse_args()
    scope = load(args.scope)
    text = render(scope, estimate(scope))
    if args.out:
        with open(args.out, "w") as fh:
            fh.write(text)
    else:
        print(text)


if __name__ == "__main__":
    main()
