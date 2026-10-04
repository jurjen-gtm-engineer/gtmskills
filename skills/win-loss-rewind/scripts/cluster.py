#!/usr/bin/env python3
"""
cluster.py, Phase 3 auto-segmentation helper for win-loss-rewind.

Clusters accounts on OPERATIONAL features only. It refuses to run if a
firmographic column (headcount, industry, revenue, ...) is present in the
feature set, because those are leakage: cluster on them and you just
rediscover the Apollo filter.

Naming the clusters is NOT done here. That is a Cynical Buyer sub-agent step
(see SKILL.md Phase 3). This script only assigns numeric cluster labels and
reports centroids + member lists for the sub-agent to name.

Input CSV: one row per domain, operational features only (already scaled or
raw numeric / 0-1). Reserved non-feature columns: domain, outcome, split,
company_name.

Usage:
    python cluster.py features.csv --k 4
    python cluster.py features.csv --k auto --out clustered.csv
"""

import argparse
import re
import sys

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

RESERVED = {"domain", "outcome", "split", "company_name"}
# Whole-word firmographic markers. Matched on word boundaries (so "region" does
# NOT trip "region_expand", which is an operational event, not a firmographic).
# Kept deliberately narrow and unambiguous; the human gate catches the rest.
FIRMOGRAPHIC_TOKENS = (
    "headcount", "employees", "employee", "industry", "vertical",
    "revenue", "arr", "acv", "mrr", "sector", "funding",
)


def _guard_firmographics(feature_cols):
    def is_leak(col):
        words = set(re.split(r"[^a-z0-9]+", col.lower()))
        return any(tok in words for tok in FIRMOGRAPHIC_TOKENS)

    leaks = [c for c in feature_cols if is_leak(c)]
    if leaks:
        sys.exit(
            "ERROR: firmographic columns in the feature set: "
            + ", ".join(leaks)
            + "\nStrip them and recluster. Cluster on operational signals only."
        )


def _pick_k(X, kmin=2, kmax=8):
    """Crude silhouette-free elbow via inertia ratio; min cluster size handled after."""
    from sklearn.metrics import silhouette_score
    best_k, best_s = kmin, -1
    for k in range(kmin, min(kmax, len(X) - 1) + 1):
        labels = KMeans(n_clusters=k, random_state=42, n_init=10).fit_predict(X)
        if len(set(labels)) < 2:
            continue
        s = silhouette_score(X, labels)
        if s > best_s:
            best_k, best_s = k, s
    return best_k


def main():
    ap = argparse.ArgumentParser(description="Phase 3 operational clustering (no firmographics).")
    ap.add_argument("csv")
    ap.add_argument("--k", default="auto", help="number of clusters, or 'auto' (silhouette)")
    ap.add_argument("--min-size", type=int, default=5, help="minimum cluster size (default 5)")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    df = pd.read_csv(args.csv)
    feature_cols = [c for c in df.columns if c not in RESERVED]
    if not feature_cols:
        sys.exit("ERROR: no feature columns found.")
    _guard_firmographics(feature_cols)

    X = StandardScaler().fit_transform(df[feature_cols].fillna(0).values)
    k = _pick_k(X) if args.k == "auto" else int(args.k)
    labels = KMeans(n_clusters=k, random_state=42, n_init=10).fit_predict(X)
    df["cluster"] = labels

    sizes = df["cluster"].value_counts().sort_index()
    small = sizes[sizes < args.min_size]
    print(f"k={k}. cluster sizes:\n{sizes.to_string()}", file=sys.stderr)
    if not small.empty:
        print(
            f"WARNING: clusters {list(small.index)} are below min size {args.min_size}. "
            "Merge or drop before naming (they overfit).",
            file=sys.stderr,
        )

    # Centroids in original feature space for the naming sub-agent.
    print("\n=== cluster centroids (mean of each operational feature) ===")
    centroids = df.groupby("cluster")[feature_cols].mean().round(3)
    print(centroids.to_string())

    print("\n=== members per cluster (domain) ===")
    for c in sorted(df["cluster"].unique()):
        members = df.loc[df["cluster"] == c, "domain"].tolist()
        print(f"cluster {c} ({len(members)}): {', '.join(map(str, members[:25]))}"
              + (" ..." if len(members) > 25 else ""))

    if args.out:
        df.to_csv(args.out, index=False)
        print(f"\nWrote {args.out}", file=sys.stderr)


if __name__ == "__main__":
    main()
