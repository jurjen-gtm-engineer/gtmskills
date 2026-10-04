#!/usr/bin/env python3
"""TAM data cost estimate: price a market map before you build it.

Deterministic. No network, no dependencies. Reads a scope file (JSON) and prints
the three numbers for a proposal: one-off build data, monthly run data, and tool
subscriptions, each as a low to high range.

Usage:
  python3 estimate.py --scope scope.json [--out estimate.md]

Row math:
  company rows = accounts in scope (per tier)
  contact rows = accounts x qualifying titles per account (per tier)
  field cost   = rows x coverage x unit cost
  monthly      = new accounts per month (all fields once) + rows x refreshes per year / 12
"""
import argparse
import json
import sys

# Rough per-row price bands by field type. Sanity checks only: your provider's
# real price list always wins. A field priced outside its band gets flagged.
BANDS = {
    "free": (0.0, 0.0),
    "cheap_deterministic": (0.005, 0.03),
    "llm_research": (0.003, 0.05),
    "contact_email": (0.03, 0.15),
    "premium": (0.15, 0.60),
}


def fail(msg):
    sys.exit(f"scope error: {msg}")


def load(path):
    with open(path) as fh:
        scope = json.load(fh)
    for key in ("tiers", "fields"):
        if not scope.get(key):
            fail(f"'{key}' is required and cannot be empty")
    for t in scope["tiers"]:
        for key in ("name", "accounts", "titles_per_account"):
            if key not in t:
                fail(f"tier {t.get('name', '?')} misses '{key}'")
        if t["accounts"] < 0 or t["titles_per_account"] < 0:
            fail(f"tier {t['name']} has a negative number")
    names = {t["name"] for t in scope["tiers"]}
    for f in scope["fields"]:
        for key in ("name", "object", "unit_cost_low", "unit_cost_high"):
            if key not in f:
                fail(f"field {f.get('name', '?')} misses '{key}'")
        if f["object"] not in ("company", "contact"):
            fail(f"field {f['name']}: object must be 'company' or 'contact'")
        if f["unit_cost_low"] > f["unit_cost_high"]:
            fail(f"field {f['name']}: unit_cost_low is above unit_cost_high")
        if not 0 <= f.get("coverage", 1.0) <= 1:
            fail(f"field {f['name']}: coverage must be between 0 and 1")
        unknown = set(f.get("tiers", names)) - names
        if unknown:
            fail(f"field {f['name']} names unknown tiers: {sorted(unknown)}")
        if f.get("band") and f["band"] not in BANDS:
            fail(f"field {f['name']}: unknown band '{f['band']}'")
    return scope


def rows_for(field, tiers, accounts_override=None):
    """Rows this field is paid on, before coverage."""
    total = 0.0
    for t in tiers:
        if t["name"] not in field.get("tiers", [x["name"] for x in tiers]):
            continue
        accounts = t["accounts"] if accounts_override is None else accounts_override[t["name"]]
        total += accounts if field["object"] == "company" else accounts * t["titles_per_account"]
    return total


def estimate(scope):
    tiers = scope["tiers"]
    total_accounts = sum(t["accounts"] for t in tiers)
    contact_rows = sum(t["accounts"] * t["titles_per_account"] for t in tiers)
    new_per_month = scope.get("new_accounts_per_month", 0)
    # New accounts arrive in the same tier mix as the build.
    new_by_tier = {
        t["name"]: (new_per_month * t["accounts"] / total_accounts if total_accounts else 0)
        for t in tiers
    }
    lines, build, monthly = [], [0.0, 0.0], [0.0, 0.0]
    gate = scope.get("field_gate", 250)
    for f in scope["fields"]:
        cov = f.get("coverage", 1.0)
        rows = rows_for(f, tiers) * cov
        new_rows = rows_for(f, tiers, new_by_tier) * cov
        refresh = f.get("refreshes_per_year", 0)
        lo, hi = f["unit_cost_low"], f["unit_cost_high"]
        b = (rows * lo, rows * hi)
        m = ((new_rows + rows * refresh / 12) * lo, (new_rows + rows * refresh / 12) * hi)
        flags = []
        if f.get("band"):
            band_lo, band_hi = BANDS[f["band"]]
            if hi > band_hi:
                flags.append(f"above the {f['band']} band (max {band_hi})")
            elif hi < band_lo:
                flags.append(f"below the {f['band']} band (min {band_lo}), check the price")
        if b[1] > gate and not f.get("cheaper_alternative"):
            flags.append(f"over {gate} in total: name a cheaper alternative and why you pay instead")
        lines.append({"field": f, "rows": rows, "build": b, "monthly": m, "flags": flags})
        build[0] += b[0]; build[1] += b[1]
        monthly[0] += m[0]; monthly[1] += m[1]
    subs = sum(s["monthly"] for s in scope.get("subscriptions", []))
    return {
        "accounts": total_accounts, "contact_rows": contact_rows, "lines": lines,
        "build": build, "monthly": monthly, "subscriptions": subs,
    }


def money(cur, lo, hi):
    if round(lo) == round(hi):
        return f"{cur} {lo:,.0f}"
    return f"{cur} {lo:,.0f} to {hi:,.0f}"


def render(scope, r):
    cur = scope.get("currency", "EUR")
    out = [f"# TAM data cost estimate: {scope.get('name', 'unnamed scope')}", ""]
    out += ["## Scope this estimate assumes", ""]
    out += ["| Tier | Accounts | Qualifying titles per account | Contact rows |", "|---|---|---|---|"]
    for t in scope["tiers"]:
        out.append(f"| {t['name']} | {t['accounts']:,} | {t['titles_per_account']:g} | {t['accounts'] * t['titles_per_account']:,.0f} |")
    out.append(f"| **Total** | **{r['accounts']:,}** | | **{r['contact_rows']:,.0f}** |")
    out += ["", f"New accounts per month: {scope.get('new_accounts_per_month', 0):,}", ""]
    out += ["## Priced fields", ""]
    out += ["| Field | Object | Paid rows | Unit cost | One-off build | Per month | Flags |", "|---|---|---|---|---|---|---|"]
    for l in r["lines"]:
        f = l["field"]
        out.append(
            f"| {f['name']} | {f['object']} | {l['rows']:,.0f} | {f['unit_cost_low']:g} to {f['unit_cost_high']:g} "
            f"| {money(cur, *l['build'])} | {money(cur, *l['monthly'])} | {'; '.join(l['flags']) or 'none'} |"
        )
    out += ["", "## The three numbers", ""]
    out += ["| Line | What it covers | Amount |", "|---|---|---|"]
    out.append(f"| **One-off build data** | The full mapping and enrichment run, once | {money(cur, *r['build'])} |")
    out.append(f"| **Monthly run data** | New accounts plus the refreshing fields | {money(cur, *r['monthly'])} per month |")
    out.append(f"| **Tool subscriptions** | Contracted by the client directly | {cur} {r['subscriptions']:,.0f} per month |")
    flagged = [l for l in r["lines"] if l["flags"]]
    out += ["", f"Fields flagged: {len(flagged)} of {len(r['lines'])}.",
            "This is a range from the unit costs you entered. Change the scope and the number moves with it.", ""]
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
