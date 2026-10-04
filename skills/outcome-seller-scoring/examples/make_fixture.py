#!/usr/bin/env python3
"""Synthetic corpus shaped like the WbD source case: 12 reps, ~12 calls each,
impact coverage clustered near 20%, decision near 7%. For smoke-testing the harness
only. Never ship a number that came out of this."""
import json, random
random.seed(7)
REPS = [f"Rep {c}" for c in "ABCDEFGHIJKL"]
# 3 who essentially never raise impact, most occasional, a couple running the full cycle
SKILL = {r: s for r, s in zip(REPS, [0.05,0.05,0.08,0.15,0.18,0.20,0.22,0.25,0.28,0.45,0.55,0.62])}
rows = []
for rep in REPS:
    s = SKILL[rep]
    for i in range(random.randint(9, 15)):
        def sc(p, floor=1):
            return 3 + random.randint(0, 2) if random.random() < p else random.randint(floor, 2)
        imp = sc(s); dec = sc(s * 0.35); ce = sc(s * 1.05)
        def cell(v, cust=False):
            return {"score": v, "na_reason": None,
                    "quote": "…verbatim…" if v >= 3 else None,
                    "speaker": ("Customer" if cust else "Rep") if v >= 3 else None,
                    "timestamp": "00:14:02" if v >= 3 else None,
                    # synthetic: real scorers judge the 'Qualified when' test, not the score
                    "status": "gap" if v <= 2 else ("qualified" if v >= 4 else "partial"),
                    "follow_up": None if v >= 4 else "…exact follow-up question…"}
        rows.append({
            "call_id": f"{rep.replace(' ','')}-{i:02d}", "rep": rep,
            "date": "2026-07-15", "account": f"acct-{i}", "call_type": "discovery",
            "duration_min": round(random.uniform(22, 55), 1),
            "segment": random.choice(["Enterprise", "Mid-market"]), "region": "EMEA",
            "axes": {
                "situation": cell(sc(0.85), True), "pain": cell(sc(0.72), True),
                "impact": cell(imp, True), "critical_event": cell(ce, True),
                "decision": cell(dec, True),
                "second_question": {"observed": imp >= 3, "quote": None, "speaker": None, "timestamp": None},
                "customer_supplied_number": {"observed": imp >= 4, "quote": None, "speaker": None, "timestamp": None},
                "what_breaks": {"observed": ce >= 4, "quote": None, "speaker": None, "timestamp": None},
                "demo_pivot": {"observed": imp < 3 and random.random() < 0.6, "quote": None, "speaker": None, "timestamp": None},
            },
            "coaching_note": None,
        })
with open("examples/scores.jsonl", "w") as f:
    for r in rows:
        f.write(json.dumps(r) + "\n")
print(f"{len(rows)} calls, {len(REPS)} reps -> examples/scores.jsonl")
