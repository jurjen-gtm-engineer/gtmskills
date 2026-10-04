#!/usr/bin/env python3
"""Coverage rates and the per-rep heatmap from scored calls.

Input:  scores.jsonl, one object per call matching references/score_schema.json
Output: <out>/org.json, <out>/per_rep.json, <out>/coverage.md

Coverage rule (the whole diagnostic turns on this):
  covered  = score >= 3
  excluded = score is null (not applicable)
  a score of 1 IS in the denominator; a null is NOT.

Status layer (stricter, deal-review bar, spiced-rubric.md "Two layers"):
  qualified rate = status == "qualified" / scored calls that carry a status
  Calls without a status (older score files) are left out of that denominator,
  and the column reads n/a when no call carries one.
"""
import argparse, json, math, sys
from collections import defaultdict

SCORED_AXES = ["situation", "pain", "impact", "critical_event", "decision"]
MOVE_AXES = ["second_question", "customer_supplied_number", "what_breaks", "demo_pivot"]
COVERAGE_BAR = 3
MASTERY_BAR = 4
STATUSES = ("qualified", "partial", "gap")
FOLLOW_UP_AXES = ("impact", "critical_event", "decision")

# WbD, ~57,000 calls, Aug 2026 webinar. Vendor data, self-reported.
WBD_BENCHMARK = {"impact": 0.206, "critical_event": 0.217, "decision": 0.068}
WBD_LIFT = {
    "impact": "+44% revenue per account",
    "critical_event": "21% shorter cycle (66d to 52d)",
    "decision": "+15.5% win rate",
}


def wilson(k, n, z=1.96):
    """95% Wilson score interval. Correct at small n, which is the whole point:
    a rep with 2/8 is not 'a 25% rep'."""
    if n == 0:
        return (0.0, 0.0, 0.0)
    p = k / n
    d = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / d
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (p, max(0.0, centre - half), min(1.0, centre + half))


def load(path):
    calls, bad = [], []
    with open(path) as fh:
        for i, line in enumerate(fh, 1):
            line = line.strip()
            if not line:
                continue
            try:
                calls.append(json.loads(line))
            except json.JSONDecodeError as e:
                bad.append((i, str(e)))
    return calls, bad


def validate(calls):
    """A score of 3+ without a verbatim quote is a scoring failure, not a data point.
    Impact at 3+ additionally needs a customer speaker: the bar is customer-articulated."""
    errors = []
    for c in calls:
        cid = c.get("call_id", "?")
        axes = c.get("axes", {})
        for ax in SCORED_AXES:
            cell = axes.get(ax)
            if cell is None:
                errors.append(f"{cid}: axis '{ax}' missing")
                continue
            s = cell.get("score")
            if s is None:
                continue
            if s >= COVERAGE_BAR and not (cell.get("quote") or "").strip():
                errors.append(f"{cid}: {ax} scored {s} with no quote")
            if ax == "impact" and s >= COVERAGE_BAR and not (cell.get("speaker") or "").strip():
                errors.append(f"{cid}: impact scored {s} with no speaker attribution")
            st = cell.get("status")
            if st is None:
                continue
            if st not in STATUSES:
                errors.append(f"{cid}: {ax} has unknown status '{st}'")
            elif st == "gap" and s >= COVERAGE_BAR:
                errors.append(f"{cid}: {ax} scored {s} but marked gap (gap means 1-2)")
            elif st in ("partial", "qualified") and s < COVERAGE_BAR:
                errors.append(f"{cid}: {ax} scored {s} but marked {st} (needs 3+)")
            elif st == "qualified" and "customer" not in (cell.get("speaker") or "").lower():
                errors.append(f"{cid}: {ax} marked qualified without a customer quote")
            if (st in ("partial", "gap") and ax in FOLLOW_UP_AXES
                    and not (cell.get("follow_up") or "").strip()):
                errors.append(f"{cid}: {ax} is {st} with no follow_up question")
    return errors


def rate(calls, axis, bar=COVERAGE_BAR):
    n = k = 0
    for c in calls:
        cell = c["axes"].get(axis) or {}
        s = cell.get("score")
        if s is None:
            continue
        n += 1
        if s >= bar:
            k += 1
    return k, n


def status_rate(calls, axis):
    """Qualified count over scored calls that carry a status. None when nothing carries one."""
    n = k = 0
    for c in calls:
        cell = c["axes"].get(axis) or {}
        if cell.get("score") is None or cell.get("status") is None:
            continue
        n += 1
        if cell["status"] == "qualified":
            k += 1
    return k, n


def move_rate(calls, axis):
    n = k = 0
    for c in calls:
        v = (c["axes"].get(axis) or {}).get("observed")
        if v is None:
            continue
        n += 1
        if v:
            k += 1
    return k, n


def block(calls):
    out = {"n_calls": len(calls), "scored": {}, "moves": {}}
    for ax in SCORED_AXES:
        k, n = rate(calls, ax)
        p, lo, hi = wilson(k, n)
        km, _ = rate(calls, ax, MASTERY_BAR)
        kq, nq = status_rate(calls, ax)
        out["scored"][ax] = {
            "covered": k, "denominator": n, "coverage": round(p, 4),
            "ci95": [round(lo, 4), round(hi, 4)],
            "mastery_rate": round(km / n, 4) if n else 0.0,
            "qualified_rate": round(kq / nq, 4) if nq else None,
            "qualified_denominator": nq,
            "wbd_benchmark": WBD_BENCHMARK.get(ax),
            "lift_when_present": WBD_LIFT.get(ax),
        }
    for ax in MOVE_AXES:
        k, n = move_rate(calls, ax)
        p, lo, hi = wilson(k, n)
        out["moves"][ax] = {"observed": k, "denominator": n,
                            "rate": round(p, 4), "ci95": [round(lo, 4), round(hi, 4)]}
    return out


def pct(x):
    return f"{100 * x:.1f}%"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("scores")
    ap.add_argument("--out", default="coverage")
    ap.add_argument("--min-calls-per-rep", type=int, default=8,
                    help="Below this a per-rep coverage rate is reported as indicative only.")
    ap.add_argument("--allow-invalid", action="store_true")
    a = ap.parse_args()

    import os
    os.makedirs(a.out, exist_ok=True)

    calls, bad = load(a.scores)
    if bad:
        print(f"! {len(bad)} unparseable lines: {bad[:3]}", file=sys.stderr)
    errors = validate(calls)
    if errors:
        print(f"! {len(errors)} validation failures:", file=sys.stderr)
        for e in errors[:20]:
            print("   " + e, file=sys.stderr)
        if not a.allow_invalid:
            print("\nFix the scoring pass, or re-run with --allow-invalid to proceed knowingly.",
                  file=sys.stderr)
            sys.exit(2)

    org = block(calls)
    org["validation_failures"] = len(errors)

    by_rep = defaultdict(list)
    for c in calls:
        by_rep[c["rep"]].append(c)

    per_rep = {}
    for rep, rc in sorted(by_rep.items()):
        b = block(rc)
        b["sufficient_sample"] = len(rc) >= a.min_calls_per_rep
        per_rep[rep] = b

    segments = {}
    for key in ("segment", "region"):
        groups = defaultdict(list)
        for c in calls:
            v = c.get(key)
            if v:
                groups[v].append(c)
        if groups:
            segments[key] = {g: block(gc) for g, gc in sorted(groups.items())}

    json.dump(org, open(f"{a.out}/org.json", "w"), indent=2)
    json.dump(per_rep, open(f"{a.out}/per_rep.json", "w"), indent=2)
    if segments:
        json.dump(segments, open(f"{a.out}/segments.json", "w"), indent=2)

    L = []
    L.append("# SPICED coverage\n")
    L.append(f"{len(calls)} calls, {len(by_rep)} reps. "
             f"Coverage = scored 3 or higher. Mastery = 4 or higher. "
             f"Qualified = passes the deal-review test on a customer quote.\n")
    L.append("## Org view: is this a training problem?\n")
    L.append("| Dimension | Coverage | 95% CI | Mastery | Qualified | WbD 57k benchmark | Lift when present |")
    L.append("|---|---|---|---|---|---|---|")
    for ax in SCORED_AXES:
        d = org["scored"][ax]
        bm = pct(d["wbd_benchmark"]) if d["wbd_benchmark"] else "n/a"
        q = pct(d["qualified_rate"]) if d["qualified_rate"] is not None else "n/a"
        L.append(f"| {ax.replace('_', ' ').title()} | {pct(d['coverage'])} | "
                 f"{pct(d['ci95'][0])} to {pct(d['ci95'][1])} | {pct(d['mastery_rate'])} | {q} | "
                 f"{bm} | {d['lift_when_present'] or ''} |")
    L.append("\nCoverage is reported per dimension, not cumulatively. Compare coverage, not Qualified, "
             "against the WbD benchmark: the benchmark counts a dimension as present, which is the 3+ bar. "
             "The gap between Coverage and Qualified is the share of calls where the topic came up "
             "but would not survive a deal review.\n")

    L.append("## The four Outcome Seller moves\n")
    L.append("| Move | Rate | 95% CI | n |")
    L.append("|---|---|---|---|")
    for ax in MOVE_AXES:
        d = org["moves"][ax]
        label = ax.replace("_", " ")
        if ax == "demo_pivot":
            label += " (anti-pattern: pain straight to demo, no impact on the table)"
        L.append(f"| {label} | {pct(d['rate'])} | {pct(d['ci95'][0])} to {pct(d['ci95'][1])} | {d['denominator']} |")

    L.append("\n## Per-rep heatmap: who and how bad?\n")
    L.append("| Rep | Calls | " + " | ".join(x.replace("_", " ").title() for x in SCORED_AXES) + " | Demo pivot |")
    L.append("|---|---|" + "---|" * (len(SCORED_AXES) + 1))
    for rep, b in sorted(per_rep.items(), key=lambda kv: -kv[1]["scored"]["impact"]["coverage"]):
        flag = "" if b["sufficient_sample"] else " *"
        cells = [pct(b["scored"][ax]["coverage"]) for ax in SCORED_AXES]
        L.append(f"| {rep} | {b['n_calls']}{flag} | " + " | ".join(cells) +
                 f" | {pct(b['moves']['demo_pivot']['rate'])} |")
    thin = [r for r, b in per_rep.items() if not b["sufficient_sample"]]
    if thin:
        L.append(f"\n`*` under {a.min_calls_per_rep} calls: indicative only, read the CI in `per_rep.json` "
                 f"before drawing a conclusion. Affects: {', '.join(sorted(thin))}.")
    L.append("\nThe dark bands are the coaching plan. This is a coaching input, never a compensation input: "
             "the moment coverage is compensated, reps learn to say the words and the diagnostic dies.\n")
    open(f"{a.out}/coverage.md", "w").write("\n".join(L) + "\n")

    print("\n".join(L))
    print(f"\n-> {a.out}/org.json, {a.out}/per_rep.json, {a.out}/coverage.md")


if __name__ == "__main__":
    main()
