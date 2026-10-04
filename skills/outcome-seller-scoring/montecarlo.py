#!/usr/bin/env python3
"""Monte Carlo on the rep, not the funnel.

Real simulation in numpy with a fixed seed, not an LLM narrating a distribution.
A number you cannot recompute is a memory.

  revenue/rep/month = opps * (1 - disqualification) * win_rate * ACV * (1 - discount)

Win rate is applied AFTER qualification. If the client's CRM does not measure it that
way, fix the input: every team quietly moves that marker until the number looks fine.

Usage:
  python3 montecarlo.py --config sim_config.json --n 50000 --seed 42 --out sim/
  python3 montecarlo.py --config sim_config.json --coverage coverage/per_rep.json \
                        --scenario middle_to_top --out sim/
"""
import argparse, json, math, os, sys
import numpy as np

METRICS = ["opps_per_month", "disqualification_rate", "win_rate", "acv",
           "discount_rate", "sales_cycle_days"]
# The five that actually appear in the monthly revenue identity. sales_cycle_days does not:
# it enters only via the coverage bridge, by changing at-bats per month.
IDENTITY_METRICS = [m for m in METRICS if m != "sales_cycle_days"]

# WbD Aug 2026, ~57,000 calls. Vendor data, self-reported, named in the deliverable.
LIFT = {"impact": 0.44, "decision": 0.155, "critical_event": -0.21}
LADDER = 0.80  # mid = 80% of top, low = 80% of mid


def sample(rng, spec, n):
    """Triangular on (min, mode, max). Triangular is the right family precisely because
    Jacco insists on the mode: the average of 6 and 12 is 9, but the population is dense
    at 7 and 8, and a symmetric distribution models a team you do not have.

    Lognormal when the spread is wide (a $38k-$150k platform), because triangular
    understates the tail a single large deal puts in a rep's month."""
    lo, mode, hi = spec["min"], spec.get("mode"), spec["max"]
    if mode is None:
        mode = (lo + hi) / 2.0
        spec["_mode_guessed"] = True
    if not (lo <= mode <= hi):
        raise ValueError(f"mode {mode} outside [{lo}, {hi}]")
    dist = spec.get("dist", "auto")
    if dist == "auto":
        dist = "lognormal" if (lo > 0 and hi / lo >= 3.0) else "triangular"
    if dist == "lognormal":
        mu = math.log(max(mode, 1e-9))
        # 90% of mass inside [lo, hi]
        sigma = (math.log(hi) - math.log(max(lo, 1e-9))) / (2 * 1.6449)
        sigma = max(sigma, 1e-6)
        return np.clip(rng.lognormal(mu + sigma ** 2, sigma, n), lo, hi)
    if lo == hi:
        return np.full(n, float(lo))
    return rng.triangular(lo, mode, hi, n)


def apply_bridge(spec_set, cov, baseline_cov, strength):
    """Map measured coverage onto metric modes.

    INFERENCE, NOT WbD'S CLAIM, and it must be labelled as one in every client artefact.
    WbD's lift is binary and per call (was the dimension present, yes or no). Applying it
    as a linear scaler on a rep's coverage RATE is our extrapolation.

    Normalised against the corpus mean coverage so a team-average rep lands at 1.0x.
    Without that normalisation the baseline metrics, which already reflect current
    coverage, get the lift applied twice.
    """
    out = json.loads(json.dumps(spec_set))
    adj = {}
    for axis, metric, sign in (("impact", "acv", 1), ("decision", "win_rate", 1),
                               ("critical_event", "sales_cycle_days", 1)):
        if axis not in cov:
            continue
        delta = cov[axis] - baseline_cov.get(axis, 0.0)
        mult = 1.0 + delta * LIFT[axis] * strength
        mult = max(0.25, mult)
        out[metric]["mode"] = out[metric]["mode"] * mult
        out[metric]["min"] = min(out[metric]["min"], out[metric]["mode"])
        out[metric]["max"] = max(out[metric]["max"], out[metric]["mode"])
        adj[metric] = round(mult, 4)
    # A shorter cycle means more at-bats: scale opportunity volume inversely.
    if "sales_cycle_days" in adj and adj["sales_cycle_days"] != 1.0:
        m = 1.0 / adj["sales_cycle_days"]
        for k in ("min", "mode", "max"):
            out["opps_per_month"][k] *= m
        adj["opps_per_month"] = round(m, 4)
    return out, adj


def run(rng, specs, n):
    s = {m: sample(rng, specs[m], n) for m in METRICS if m in specs}
    qualified = s["opps_per_month"] * (1.0 - s["disqualification_rate"])
    rev = qualified * s["win_rate"] * s["acv"] * (1.0 - s["discount_rate"])
    return rev, s


def summarise(rev):
    p = np.percentile(rev, [10, 50, 90])
    return {
        "mean": float(rev.mean()),
        "pct_10": float(p[0]), "pct_50": float(p[1]), "pct_90": float(p[2]),
        # The KB carries two conflicting P-conventions. Name both, never a bare "P90".
        "floor_90pct_of_runs_clear": float(p[0]),
        "upside_10pct_of_runs_exceed": float(p[2]),
        "skew": float(((rev - rev.mean()) ** 3).mean() / rev.std() ** 3),
        # Terminology trap. The source says the distribution "leans left", meaning the MASS
        # piles on the left with a thin tail of high performers to the right. That is
        # statistically POSITIVE skew. Reading it as negative skew inverts the finding.
        "mass_on_the_left": bool(((rev - rev.mean()) ** 3).mean() > 0),
    }


def sensitivity(rng, specs, n, rev, samples):
    """Two passes. Global (Spearman over the existing draws) accounts for interaction and
    costs nothing. OAT is the intuitive one. If they disagree, distrust OAT."""
    from scipy.stats import spearmanr
    glob = {}
    spread = {}
    for m, v in samples.items():
        glob[m] = round(float(spearmanr(v, rev).statistic), 4)
        spread[m] = round(float(v.std() / abs(v.mean())), 4) if v.mean() else None

    oat = {}
    base = {m: specs[m].get("mode", (specs[m]["min"] + specs[m]["max"]) / 2) for m in specs}
    for m in specs:
        vals = []
        for end in ("min", "max"):
            pt = dict(base)
            pt[m] = specs[m][end]
            q = pt["opps_per_month"] * (1 - pt["disqualification_rate"])
            vals.append(q * pt["win_rate"] * pt["acv"] * (1 - pt["discount_rate"]))
        oat[m] = round(abs(vals[1] - vals[0]), 2)

    ranked = {k: v for k, v in sorted(glob.items(), key=lambda kv: -abs(kv[1]))
              if k in IDENTITY_METRICS}
    return {
        "global_spearman": ranked,
        "excluded": {m: glob[m] for m in glob if m not in IDENTITY_METRICS},
        "oat_swing_eur": {k: v for k, v in sorted(oat.items(), key=lambda kv: -kv[1])
                          if k in IDENTITY_METRICS},
        "relative_spread_cv": spread,
        "agree": list(ranked)[:3] == [k for k in oat if k in IDENTITY_METRICS][:3],
        "note": ("Every term in the revenue identity is multiplicative, so this ranking is "
                 "driven by each metric's RELATIVE spread (see relative_spread_cv). Guessed "
                 "ranges produce a confident garbage ranking. sales_cycle_days is excluded: "
                 "it is not in the monthly identity and acts only through the coverage "
                 "bridge on opportunity volume."),
    }


def cohorts(per_rep_p50, basis="measured"):
    """Three cohorts against the 80% ladder. The middle group is usually the anomaly:
    bottom performers are expensive to lift, top performers are at ceiling, the middle is
    a large population sitting below its own tier with room and receptiveness."""
    reps = sorted(per_rep_p50.items(), key=lambda kv: -kv[1])
    n = len(reps)
    if n < 3:
        return None
    cut = max(1, n // 3)
    groups = {"top": reps[:cut], "middle": reps[cut:n - cut] or reps[cut:cut + 1], "low": reps[n - cut:]}
    means = {g: float(np.mean([v for _, v in m])) for g, m in groups.items()}
    expected = {"top": means["top"], "middle": means["top"] * LADDER,
                "low": means["top"] * LADDER * LADDER}
    return {
        "members": {g: [r for r, _ in m] for g, m in groups.items()},
        "actual_p50": {g: round(v, 2) for g, v in means.items()},
        "ladder_expected": {g: round(v, 2) for g, v in expected.items()},
        "gap_vs_ladder": {g: round(means[g] - expected[g], 2) for g in means},
        "operating_at": {g: round(means[g] / expected[g], 4) if expected[g] else None for g in means},
        "basis": basis,
        "note": "The 80% ladder is a WbD heuristic, presented as historically true and not "
                "derived. Treat a gap as a flag to investigate, not a target to manage to.",
        "warning": (None if basis == "measured" else
                    "BEHAVIOUR-ONLY BASIS. No per-rep CRM metrics were supplied, so the entire "
                    "spread between these reps comes from the coverage bridge. Real rep variance "
                    "is far wider than call behaviour alone explains, so the ladder comparison "
                    "is NOT meaningful here. Do not put this cohort table in front of a client "
                    "without per-rep opportunities, win rate, ACV and discount from the CRM."),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    ap.add_argument("--coverage", help="coverage/per_rep.json from coverage.py")
    ap.add_argument("--scenario", choices=["none", "middle_to_top", "all_to_top"], default="none")
    ap.add_argument("--n", type=int, default=50000)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--out", default="sim")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)

    cfg = json.load(open(a.config))
    team = cfg["team"]
    rng = np.random.default_rng(a.seed)

    guessed = [m for m, s in team.items() if s.get("mode") is None]
    if guessed:
        print(f"! no mode supplied for {guessed}: falling back to the midpoint. "
              f"The mode is the field most often guessed, and the ranges ARE the model.",
              file=sys.stderr)

    result = {"n_runs": a.n, "seed": a.seed, "config": a.config}

    team_rev, team_samples = run(rng, team, a.n)
    result["team_baseline"] = summarise(team_rev)
    result["sensitivity"] = sensitivity(rng, team, a.n, team_rev, team_samples)

    cov = {}
    baseline_cov = {}
    if a.coverage:
        per_rep_cov = json.load(open(a.coverage))
        for rep, b in per_rep_cov.items():
            cov[rep] = {ax: b["scored"][ax]["coverage"] for ax in ("impact", "decision", "critical_event")}
        for ax in ("impact", "decision", "critical_event"):
            baseline_cov[ax] = float(np.mean([c[ax] for c in cov.values()]))
        result["baseline_coverage"] = {k: round(v, 4) for k, v in baseline_cov.items()}

    reps = cfg.get("reps") or {r: {} for r in cov}
    per_rep = {}
    for rep, override in reps.items():
        specs = json.loads(json.dumps(team))
        specs.update(override)
        adj = {}
        if rep in cov:
            specs, adj = apply_bridge(specs, cov[rep], baseline_cov, cfg.get("bridge_strength", 1.0))
        rev, _ = run(rng, specs, a.n)
        per_rep[rep] = summarise(rev)
        per_rep[rep]["bridge_multipliers"] = adj
        per_rep[rep]["coverage"] = cov.get(rep)
    result["per_rep"] = per_rep

    if per_rep:
        p50 = {r: v["pct_50"] for r, v in per_rep.items()}
        measured = any(cfg.get("reps", {}).get(r) for r in per_rep)
        result["cohorts"] = cohorts(p50, "measured" if measured else "behaviour_only")

    if a.scenario != "none" and cov and result.get("cohorts"):
        target = {ax: float(np.mean([cov[r][ax] for r in result["cohorts"]["members"]["top"]]))
                  for ax in ("impact", "decision", "critical_event")}
        movers = (result["cohorts"]["members"]["middle"] if a.scenario == "middle_to_top"
                  else result["cohorts"]["members"]["middle"] + result["cohorts"]["members"]["low"])
        result["scenario"] = {"name": a.scenario, "movers": movers,
                              "target_coverage": {k: round(v, 4) for k, v in target.items()},
                              "variants": {}}
        for label, strength in (("full_lift", 1.0), ("conservative_half_lift", 0.5)):
            total_now = total_then = 0.0
            detail = {}
            for rep in movers:
                specs = json.loads(json.dumps(team))
                specs.update(reps.get(rep, {}))
                s_now, _adj = apply_bridge(specs, cov[rep], baseline_cov, strength)
                s_then, _ = apply_bridge(specs, target, baseline_cov, strength)
                r_now, _ = run(rng, s_now, a.n)
                r_then, _ = run(rng, s_then, a.n)
                detail[rep] = {"p50_now": round(float(np.percentile(r_now, 50)), 2),
                               "p50_then": round(float(np.percentile(r_then, 50)), 2)}
                total_now += float(np.percentile(r_now, 50))
                total_then += float(np.percentile(r_then, 50))
            result["scenario"]["variants"][label] = {
                "monthly_p50_now": round(total_now, 2),
                "monthly_p50_after": round(total_then, 2),
                "monthly_delta": round(total_then - total_now, 2),
                "annualised_delta": round((total_then - total_now) * 12, 2),
                "per_rep": detail,
            }
        result["scenario"]["caveat"] = (
            "The coverage-to-metric bridge is OUR inference. WbD measure the lift binary and "
            "per call; applying it as a linear scaler on a coverage rate is an extrapolation. "
            "Report the range between full_lift and conservative_half_lift. If the coaching "
            "case only survives at full lift, it does not survive.")

    json.dump(result, open(f"{a.out}/simulation.json", "w"), indent=2)

    b = result["team_baseline"]
    print(f"\n{a.n:,} runs, seed {a.seed}\n")
    print("Team baseline, revenue per rep per month")
    print(f"  mean   {b['mean']:>12,.0f}")
    print(f"  P10    {b['pct_10']:>12,.0f}   (90% of simulated months clear this)")
    print(f"  P50    {b['pct_50']:>12,.0f}   (the planning anchor)")
    print(f"  P90    {b['pct_90']:>12,.0f}   (10% of months exceed this)")
    print(f"  skew   {b['skew']:>12.3f}   " + (
        "mass on the left, a long underperforming tail: expected"
        if b["mass_on_the_left"] else
        "mass on the RIGHT: unexpected, check whether the modes were pulled or guessed"))

    s = result["sensitivity"]
    print("\nSensitivity, global (Spearman rank correlation across all runs)")
    for m, r in s["global_spearman"].items():
        print(f"  {m:<24} {r:+.3f}   (relative spread {s['relative_spread_cv'][m]:.2f})")
    print("  " + s["note"].replace(". ", ".\n  "))
    print(f"\n  OAT ranking agrees on the top 3: {s['agree']}")
    if "opps_per_month" in list(s["global_spearman"])[-2:]:
        print("  -> opportunity volume ranks at the bottom. More leads buys this client very "
              "little; the honest recommendation is downstream work.")

    if result.get("cohorts"):
        c = result["cohorts"]
        print("\nCohorts against the 80% ladder")
        if c.get("warning"):
            print("  ! " + c["warning"])
        for g in ("top", "middle", "low"):
            print(f"  {g:<7} actual {c['actual_p50'][g]:>10,.0f}   ladder says "
                  f"{c['ladder_expected'][g]:>10,.0f}   operating at "
                  f"{100 * c['operating_at'][g]:.0f}%   ({len(c['members'][g])} reps)")

    if result.get("scenario"):
        print(f"\nScenario: {result['scenario']['name']}")
        for label, v in result["scenario"]["variants"].items():
            print(f"  {label:<24} +{v['monthly_delta']:,.0f}/mo   "
                  f"+{v['annualised_delta']:,.0f}/yr")
        print("  " + result["scenario"]["caveat"])

    print(f"\n-> {a.out}/simulation.json")


if __name__ == "__main__":
    main()
