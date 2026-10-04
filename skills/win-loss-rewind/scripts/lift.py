#!/usr/bin/env python3
"""
lift.py, Phase 6 backcast and validation for win-loss-rewind.

Computes, for every candidate signal, the prevalence lift on the TRAIN set and
on the held-out 20% INDEPENDENTLY, plus a Fisher-exact p-value on the train 2x2.

Lift definition (matches Crawford's "13% of Best vs 2.4% of Rest = 5.4x"):

    lift = P(signal present | outcome positive) / P(signal present | outcome negative)

A signal with high train lift whose holdout lift collapses toward ~1.0 is a
training-set coincidence (the vowel-name failure mode). It is killed.

Input CSV schema (one row per account):
    domain        : str   join key
    outcome       : int   1 = positive (won/healthy/expanded), 0 = negative (lost/churned)
    split         : str   "train" or "holdout"   (carved in Phase 1, fixed seed)
    <signal cols> : int   0/1 per candidate signal (everything not in the reserved set)

Usage:
    python lift.py panel_with_signals.csv
    python lift.py panel_with_signals.csv --min-holdout-lift 1.5 --out verdicts.csv

No LLM, no network. Deterministic.
"""

import argparse
import sys

import numpy as np
import pandas as pd
from scipy.stats import fisher_exact

RESERVED = {"domain", "outcome", "split", "company_name", "cluster", "archetype"}


def _prevalence(series_signal: pd.Series, series_outcome: pd.Series, positive: int) -> float:
    """P(signal == 1 | outcome == positive). NaN if the group is empty."""
    mask = series_outcome == positive
    n = int(mask.sum())
    if n == 0:
        return float("nan")
    return float((series_signal[mask] == 1).sum()) / n


def _lift(df: pd.DataFrame, signal: str) -> float:
    """Prevalence ratio: P(signal|pos) / P(signal|neg). Guards against /0."""
    p_pos = _prevalence(df[signal], df["outcome"], 1)
    p_neg = _prevalence(df[signal], df["outcome"], 0)
    if not np.isfinite(p_neg) or p_neg == 0.0:
        # No negatives carry the signal. If positives do, lift is effectively
        # very large; report inf so it is visibly an edge case, not a clean number.
        if np.isfinite(p_pos) and p_pos > 0:
            return float("inf")
        return float("nan")
    return p_pos / p_neg


def _fisher_p(df: pd.DataFrame, signal: str) -> float:
    """Two-sided Fisher exact on the 2x2 of signal vs outcome (small-sample safe)."""
    a = int(((df[signal] == 1) & (df["outcome"] == 1)).sum())  # signal+ outcome+
    b = int(((df[signal] == 1) & (df["outcome"] == 0)).sum())  # signal+ outcome-
    c = int(((df[signal] == 0) & (df["outcome"] == 1)).sum())  # signal- outcome+
    d = int(((df[signal] == 0) & (df["outcome"] == 0)).sum())  # signal- outcome-
    try:
        _, p = fisher_exact([[a, b], [c, d]], alternative="two-sided")
        return float(p)
    except ValueError:
        return float("nan")


def evaluate(panel: pd.DataFrame, min_holdout_lift: float, max_p: float) -> pd.DataFrame:
    for col in ("outcome", "split"):
        if col not in panel.columns:
            sys.exit(f"ERROR: required column '{col}' missing from input CSV.")

    panel = panel.copy()
    panel["outcome"] = panel["outcome"].astype(int)
    train = panel[panel["split"] == "train"]
    holdout = panel[panel["split"] == "holdout"]

    if train.empty:
        sys.exit("ERROR: no rows with split == 'train'.")
    if holdout.empty:
        sys.exit("ERROR: no rows with split == 'holdout'. Phase 1 must carve a holdout.")

    # Holdout thinness guard (the "< 4 per cluster / per group" caveat).
    h_pos = int((holdout["outcome"] == 1).sum())
    h_neg = int((holdout["outcome"] == 0).sum())
    thin = h_pos < 4 or h_neg < 4
    if thin:
        print(
            f"WARNING: thin holdout (positives={h_pos}, negatives={h_neg}). "
            "Holdout lift is noisy; treat 'survives' verdicts with caution.",
            file=sys.stderr,
        )

    signals = [c for c in panel.columns if c not in RESERVED]
    if not signals:
        sys.exit("ERROR: no signal columns found (everything was reserved).")

    rows = []
    for sig in signals:
        train_lift = _lift(train, sig)
        holdout_lift = _lift(holdout, sig)
        p = _fisher_p(train, sig)

        survives = (
            np.isfinite(train_lift)
            and train_lift >= min_holdout_lift
            and np.isfinite(holdout_lift)
            and holdout_lift >= min_holdout_lift
            and np.isfinite(p)
            and p <= max_p
        )
        if np.isinf(train_lift) or np.isinf(holdout_lift):
            # inf means a zero-prevalence denominator; flag for manual review
            verdict = "review (zero-denominator)"
        elif survives:
            verdict = "SURVIVES"
        elif np.isfinite(train_lift) and train_lift >= min_holdout_lift and (
            not np.isfinite(holdout_lift) or holdout_lift < min_holdout_lift
        ):
            verdict = "KILL (holdout collapse)"
        else:
            verdict = "KILL (weak)"

        rows.append(
            {
                "signal": sig,
                "train_lift": round(train_lift, 2) if np.isfinite(train_lift) else train_lift,
                "holdout_lift": round(holdout_lift, 2) if np.isfinite(holdout_lift) else holdout_lift,
                "train_fisher_p": round(p, 4) if np.isfinite(p) else p,
                "train_prev_pos": round(_prevalence(train[sig], train["outcome"], 1), 3),
                "train_prev_neg": round(_prevalence(train[sig], train["outcome"], 0), 3),
                "verdict": verdict,
            }
        )

    out = pd.DataFrame(rows).sort_values(
        by=["verdict", "holdout_lift"], ascending=[True, False], na_position="last"
    )
    return out


def main():
    ap = argparse.ArgumentParser(description="Phase 6 train/holdout lift validation.")
    ap.add_argument("csv", help="panel CSV with domain, outcome, split, and 0/1 signal columns")
    ap.add_argument("--min-holdout-lift", type=float, default=1.5,
                    help="minimum lift required on BOTH train and holdout to survive (default 1.5)")
    ap.add_argument("--max-p", type=float, default=0.10,
                    help="maximum train Fisher-exact p-value to survive (default 0.10)")
    ap.add_argument("--out", default=None, help="optional path to write the verdict CSV")
    args = ap.parse_args()

    panel = pd.read_csv(args.csv)
    verdicts = evaluate(panel, args.min_holdout_lift, args.max_p)

    pd.set_option("display.max_rows", None)
    pd.set_option("display.width", 160)
    print(verdicts.to_string(index=False))

    n_survive = int((verdicts["verdict"] == "SURVIVES").sum())
    print(f"\n{n_survive} of {len(verdicts)} signals survived train + holdout.", file=sys.stderr)
    if n_survive == len(verdicts) and len(verdicts) > 1:
        print(
            "NOTE: every signal survived. Be suspicious of the holdout, not pleased. "
            "A healthy run usually kills at least one coincidence.",
            file=sys.stderr,
        )

    if args.out:
        verdicts.to_csv(args.out, index=False)
        print(f"Wrote {args.out}", file=sys.stderr)


if __name__ == "__main__":
    main()
