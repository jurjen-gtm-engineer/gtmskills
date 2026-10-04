#!/usr/bin/env python3
"""Compound Growth Check.

Takes a quarterly ARR series and answers one question: is this growth
system compounding, or does it just look healthy?

Method (concept credit: Winning by Design, Jacco van der Kooij):
    first derivative   delta X_t  = X_t - X_(t-1)          (QoQ ARR growth)
    second derivative  delta2 X_t = delta X_t - delta X_(t-1)
                                  = X_t - 2*X_(t-1) + X_(t-2)

A system compounds when the second derivative stays positive: growth
itself is growing, because output feeds next-period input. A system that
grows in a straight line has a second derivative oscillating around zero,
the signature of bought (paid-for) growth rather than earned growth.

Usage:
    python compound_check.py data.csv
    python compound_check.py "1.2,1.5,1.9,2.4,3.0,3.8"
    python compound_check.py data.csv --unit millions --nrr 1.15
    python compound_check.py "10,12,15,19,24,31" --cost-growth 0.20

CSV format: two columns, "quarter" and "arr", header row optional.

Output: a single JSON object on stdout with growth rates, deltas, the
trajectory classification, the 10-state ladder placement, confidence,
and caveats. Stdlib only, no third-party imports.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys

# ---------------------------------------------------------------------------
# The 10-state growth ladder (concept: Winning by Design)
#
# Three macro phases:
#   States 1-4  Accelerated Growth (effort and volume driven)
#   States 5-7  Compound Growth (feedback and learning loops)
#   States 8-10 Autonomous Growth (orchestration and self-correction)
# "The Wall" sits between states 7 and 8: the shift from selling a great
# product to helping the customer succeed.
#
# The ARR bands below are heuristic and deliberately overlapping: revenue
# scale narrows the candidate set, the trajectory classification picks
# within it. Bands are in US dollars of annualized recurring revenue.
# ---------------------------------------------------------------------------

STATES = [
    {"number": 1, "name": "Unstructured", "phase": "Accelerated Growth",
     "low": 0, "high": 3_000_000},
    {"number": 2, "name": "Structured", "phase": "Accelerated Growth",
     "low": 2_000_000, "high": 20_000_000},
    {"number": 3, "name": "Scalable", "phase": "Accelerated Growth",
     "low": 5_000_000, "high": 50_000_000},
    {"number": 4, "name": "Accelerated", "phase": "Accelerated Growth",
     "low": 10_000_000, "high": 100_000_000},
    {"number": 5, "name": "Sustainable", "phase": "Compound Growth",
     "low": 20_000_000, "high": 200_000_000},
    {"number": 6, "name": "Exponential", "phase": "Compound Growth",
     "low": 50_000_000, "high": 500_000_000},
    {"number": 7, "name": "Compounding", "phase": "Compound Growth",
     "low": 100_000_000, "high": 2_000_000_000},
    {"number": 8, "name": "Durable", "phase": "Autonomous Growth",
     "low": 200_000_000, "high": 5_000_000_000},
    {"number": 9, "name": "Orchestrated", "phase": "Autonomous Growth",
     "low": 500_000_000, "high": 10_000_000_000},
    {"number": 10, "name": "Autonomous", "phase": "Autonomous Growth",
     "low": 1_000_000_000, "high": float("inf")},
]

UNIT_MULTIPLIERS = {
    "dollars": 1.0,
    "thousands": 1_000.0,
    "millions": 1_000_000.0,
}


# ---------------------------------------------------------------------------
# Input parsing
# ---------------------------------------------------------------------------

def parse_input(source: str) -> tuple[list[str], list[float]]:
    """Parse either a CSV file path or a comma-separated ARR string.

    Returns (quarter_labels, arr_values).
    """
    if os.path.isfile(source):
        return _parse_csv(source)
    # Treat as inline comma-separated values.
    parts = [p.strip() for p in source.split(",") if p.strip()]
    try:
        values = [float(p) for p in parts]
    except ValueError:
        _fail(f"Input is neither an existing CSV file nor a comma-separated "
              f"list of numbers: {source!r}")
    labels = [f"Q{i + 1}" for i in range(len(values))]
    return labels, values


def _parse_csv(path: str) -> tuple[list[str], list[float]]:
    labels: list[str] = []
    values: list[float] = []
    with open(path, newline="", encoding="utf-8-sig") as fh:
        rows = [r for r in csv.reader(fh) if any(cell.strip() for cell in r)]
    if not rows:
        _fail(f"CSV file is empty: {path}")
    start = 0
    # Skip a header row if the second column is not numeric.
    first = rows[0]
    if len(first) >= 2 and not _is_number(first[1]):
        start = 1
    elif len(first) == 1 and not _is_number(first[0]):
        start = 1
    for i, row in enumerate(rows[start:], start=start + 1):
        if len(row) >= 2:
            label, raw = row[0].strip(), row[1].strip()
        else:
            label, raw = f"Q{len(values) + 1}", row[0].strip()
        if not _is_number(raw):
            _fail(f"Row {i} of {path}: ARR value {raw!r} is not a number")
        labels.append(label or f"Q{len(values) + 1}")
        values.append(float(raw))
    return labels, values


def _is_number(text: str) -> bool:
    try:
        float(text)
        return True
    except ValueError:
        return False


def resolve_unit(values: list[float], unit: str) -> str:
    """Resolve --unit auto. Heuristic: values of 100,000 or more are read
    as raw dollars, smaller values as millions. Pass an explicit unit for
    ARR expressed in thousands."""
    if unit != "auto":
        return unit
    return "dollars" if max(values) >= 100_000 else "millions"


# ---------------------------------------------------------------------------
# Derivatives (simple finite differences, matching the published QoQ charts)
# ---------------------------------------------------------------------------

def compute_derivatives(arr: list[float]) -> tuple[list, list]:
    """Return (delta, delta2). delta[0] is None; delta2[0] and delta2[1]
    are None."""
    n = len(arr)
    delta = [None] + [arr[i] - arr[i - 1] for i in range(1, n)]
    delta2 = [None, None] + [delta[i] - delta[i - 1] for i in range(2, n)]
    return delta, delta2


def trailing_window_classification(delta2: list, window: int = 8):
    """Classify only the trailing N quarters of delta2 values.

    Rule:
        at least 60% positive          -> compounding
        under 50% positive             -> decompounding
        exactly 50% and average <= 0   -> decompounding (oscillates around 0)
        otherwise                      -> inflection

    Returns (classification, pct_positive, window) or (None, None, None)
    when there are not enough real delta2 values.
    """
    real = [x for x in delta2 if x is not None]
    if len(real) < window:
        return None, None, None
    tail = real[-window:]
    n_pos = sum(1 for x in tail if x > 0)
    pct_pos = 100.0 * n_pos / window
    avg = sum(tail) / window
    if pct_pos >= 60.0:
        return "compounding", pct_pos, window
    if pct_pos < 50.0 or (pct_pos == 50.0 and avg <= 0.0):
        return "decompounding", pct_pos, window
    return "inflection", pct_pos, window


# ---------------------------------------------------------------------------
# Trajectory classification
# ---------------------------------------------------------------------------

def classify_trajectory(arr: list[float], delta: list, delta2: list) -> dict:
    """Classify the full series as one of:
        compounding    at least 60% of delta2 values positive AND the last
                       three readings mostly positive
        decompounding  delta2 oscillates around zero (under 50% positive,
                       or exactly 50% with average at or below zero)
        decay          ARR itself declining (both of the last two deltas
                       negative)
        inflection     growth positive but the compound signal is mixed
                       or recently flipped

    A trailing-8-quarter window is also classified; when the full series
    says inflection but the recent window says decompounding, the recent
    state wins.
    """
    delta2_real = [x for x in delta2 if x is not None]
    n_real = len(delta2_real)
    n_pos = sum(1 for x in delta2_real if x > 0)
    n_neg = sum(1 for x in delta2_real if x < 0)
    pct_pos = 100.0 * n_pos / n_real if n_real else 0.0
    avg_delta2 = sum(delta2_real) / n_real if n_real else 0.0

    recent_delta = [d for d in delta[-2:] if d is not None]
    last_three_delta2 = delta2[-3:]
    last_three_positive = sum(
        1 for x in last_three_delta2 if x is not None and x > 0
    )

    if recent_delta and all(d < 0 for d in recent_delta):
        classification = "decay"
    elif n_real >= 4 and pct_pos >= 60.0 and last_three_positive >= 2:
        classification = "compounding"
    elif n_real >= 4 and (pct_pos < 50.0
                          or (pct_pos == 50.0 and avg_delta2 <= 0.0)):
        classification = "decompounding"
    else:
        classification = "inflection"

    t_class, t_pct, t_window = trailing_window_classification(delta2, 8)
    if classification == "inflection" and t_class == "decompounding":
        classification = "decompounding"

    return {
        "classification": classification,
        "n_delta2": n_real,
        "n_positive_delta2": n_pos,
        "n_negative_delta2": n_neg,
        "pct_positive_delta2": round(pct_pos, 1),
        "avg_delta2": round(avg_delta2, 4),
        "last_three_delta2": [
            round(x, 4) if x is not None else None for x in last_three_delta2
        ],
        "trailing_8q": (
            {"classification": t_class,
             "pct_positive_delta2": round(t_pct, 1),
             "window": t_window}
            if t_class is not None else None
        ),
    }


def verdict_text(classification: str, arr: list[float], traj: dict) -> dict:
    """Headline and explanation for the trajectory verdict."""
    first, last = arr[0], arr[-1]
    growth = (last - first) / first if first else 0.0
    pct = traj["pct_positive_delta2"]
    n = traj["n_delta2"]
    last3 = ", ".join(
        f"{x:+.2f}" if x is not None else "n/a"
        for x in traj["last_three_delta2"]
    )
    span = f"ARR moved from {first:,.1f} to {last:,.1f} ({growth:+.0%})."

    if classification == "compounding":
        return {
            "headline": "The growth system is compounding.",
            "explanation": (
                f"{span} More importantly, the second derivative (the change "
                f"in growth itself) is positive in {pct:.0f}% of quarters and "
                f"the last three readings ({last3}) lean positive. Output is "
                f"feeding next-period input: the compound engine is on."
            ),
        }
    if classification == "decompounding":
        return {
            "headline": "ARR looks healthy, but the system does not compound.",
            "explanation": (
                f"{span} But the second derivative oscillates around zero "
                f"({pct:.0f}% positive across {n} quarters, last three: "
                f"{last3}). Every time it dips below zero the compound engine "
                f"resets: momentum built in one quarter is wiped out in the "
                f"next. This is the signature of growth being bought, not "
                f"earned, and bought growth stops the moment the spend stops."
            ),
        }
    if classification == "decay":
        return {
            "headline": "The system is in decay.",
            "explanation": (
                f"ARR has fallen from {first:,.1f} to {last:,.1f}. The first "
                f"derivative is negative, so there is no compound check to "
                f"perform: either the market is contracting, retention has "
                f"collapsed, or both. The question shifts to what acquisition "
                f"and retention floor would stop the bleeding."
            ),
        }
    return {
        "headline": "The system is at an inflection.",
        "explanation": (
            f"{span} The second derivative is mixed: {pct:.0f}% positive, "
            f"last three readings ({last3}). The compound engine is "
            f"sputtering, not yet broken and not yet compounding. The next "
            f"two to three quarters decide which way it tips."
        ),
    }


# ---------------------------------------------------------------------------
# 10-state ladder placement
# ---------------------------------------------------------------------------

def classify_growth_state(
    arr_dollars: float,
    classification: str,
    quarters_analyzed: int,
    yoy_growth_rate,
    quarters_since_peak: int,
    nrr=None,
    cost_growth_rate=None,
) -> dict:
    """Place the company on the 10-state ladder.

    Revenue scale narrows the candidate states, the trajectory
    classification picks within the candidate set, optional NRR and cost
    growth rate refine the pick, and confidence reflects how much
    evidence backed the call.
    """
    candidates = [s for s in STATES if s["low"] <= arr_dollars <= s["high"]]
    if not candidates:
        candidates = [STATES[0]] if arr_dollars < 1_000_000 else [STATES[-1]]

    if classification == "compounding":
        compounding_state = _state_by_name("Compounding")
        exponential_state = _state_by_name("Exponential")
        sustainable_state = _state_by_name("Sustainable")
        if nrr is not None and nrr > 1.3 and compounding_state in candidates:
            state = compounding_state
            reasoning = (f"Revenue compounding with NRR {nrr:.0%}: "
                         f"outputs are reliably becoming inputs.")
        elif (cost_growth_rate is not None and yoy_growth_rate is not None
              and yoy_growth_rate > cost_growth_rate
              and exponential_state in candidates):
            state = exponential_state
            reasoning = ("Revenue growing faster than costs: "
                         "exponential economics.")
        elif (cost_growth_rate is not None
              and sustainable_state in candidates):
            state = sustainable_state
            reasoning = "Compounding with sustainable economics."
        else:
            state = candidates[-1]
            reasoning = ("Second derivative is positive: strong compounding "
                         "detected, so the highest scale-consistent state "
                         "applies. Limited data for a finer placement.")
    elif classification == "decompounding":
        state = candidates[len(candidates) // 2]
        reasoning = ("ARR still grows but the compound rate keeps resetting: "
                     "a middle state for this revenue scale, held there by "
                     "bought rather than earned growth.")
    elif classification == "inflection":
        state = candidates[0]
        reasoning = ("At an inflection point: compounding may stop without "
                     "intervention, so the conservative (lowest) "
                     "scale-consistent state applies.")
    else:  # decay
        state = candidates[0]
        reasoning = (f"Compounding has decayed and entropy is pulling toward "
                     f"a lower state. ARR peaked {quarters_since_peak} "
                     f"quarter(s) ago.")

    confidence, conf_notes = _estimate_confidence(
        quarters_analyzed, classification, cost_growth_rate, nrr
    )

    return {
        "state_number": state["number"],
        "state": state["name"],
        "phase": state["phase"],
        "position_vs_wall": (
            "above the Wall (states 8-10)" if state["number"] >= 8
            else "below the Wall (states 1-7)"
        ),
        "confidence": round(confidence, 2),
        "confidence_notes": conf_notes,
        "reasoning": reasoning,
        "candidate_states": [s["name"] for s in candidates],
    }


def _state_by_name(name: str) -> dict:
    return next(s for s in STATES if s["name"] == name)


def _estimate_confidence(
    quarters_analyzed: int,
    classification: str,
    cost_growth_rate,
    nrr,
) -> tuple[float, list[str]]:
    """Confidence in the state placement, 0 to 0.95."""
    confidence = 0.5
    notes = ["base 0.50 with ARR series and derivatives only"]
    if quarters_analyzed >= 12:
        confidence += 0.15
        notes.append("+0.15 for 12+ quarters of data")
    elif quarters_analyzed >= 8:
        confidence += 0.10
        notes.append("+0.10 for 8+ quarters of data")
    if quarters_analyzed < 6:
        confidence -= 0.15
        notes.append("-0.15 for fewer than 6 quarters (low-confidence run)")
    if cost_growth_rate is not None:
        confidence += 0.10
        notes.append("+0.10 for cost growth rate provided")
    if nrr is not None:
        confidence += 0.10
        notes.append("+0.10 for NRR provided")
    if classification in ("compounding", "decay"):
        confidence += 0.05
        notes.append("+0.05 for a strong, unambiguous trajectory signal")
    return max(0.05, min(confidence, 0.95)), notes


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def run_check(
    labels: list[str],
    values: list[float],
    unit: str,
    company: str = "Company",
    nrr=None,
    cost_growth_rate=None,
) -> dict:
    n = len(values)
    if n < 3:
        _fail("Need at least 3 quarters of ARR for a second-derivative "
              "calculation (6 or more recommended).")

    caveats: list[str] = []
    if n < 6:
        caveats.append(
            f"LOW CONFIDENCE: only {n} quarters supplied. The check runs, "
            f"but with fewer than 6 quarters the classification can flip on "
            f"a single noisy quarter. Treat the verdict as indicative only."
        )

    multiplier = UNIT_MULTIPLIERS[unit]
    arr_dollars_latest = values[-1] * multiplier

    delta, delta2 = compute_derivatives(values)
    traj = classify_trajectory(values, delta, delta2)
    classification = traj["classification"]
    verdict = verdict_text(classification, values, traj)

    # YoY growth: latest ARR snapshot vs the snapshot 4 quarters earlier.
    yoy = None
    if n >= 5 and values[-5] > 0:
        yoy = (values[-1] - values[-5]) / values[-5]

    peak_index = max(range(n), key=lambda i: values[i])
    quarters_since_peak = (n - 1) - peak_index

    state = classify_growth_state(
        arr_dollars=arr_dollars_latest,
        classification=classification,
        quarters_analyzed=n,
        yoy_growth_rate=yoy,
        quarters_since_peak=quarters_since_peak,
        nrr=nrr,
        cost_growth_rate=cost_growth_rate,
    )

    if state["state_number"] >= 8:
        caveats.append(
            "Placement above the Wall (states 8-10) cannot be verified from "
            "ARR alone: it requires evidence of orchestration and "
            "customer-success-driven loops, not just revenue scale."
        )
    if unit == "millions" and max(values) >= 10_000:
        caveats.append(
            "Unit heuristic read these values as millions, which implies "
            "ARR above $10B. If the values are in thousands or dollars, "
            "rerun with an explicit --unit flag."
        )

    growth_rates_pct = [
        round(100.0 * delta[i] / values[i - 1], 2)
        if delta[i] is not None and values[i - 1] else None
        for i in range(n)
    ]

    return {
        "company": company,
        "unit": unit,
        "quarters": labels,
        "arr": values,
        "arr_latest_dollars": arr_dollars_latest,
        "delta_arr": [round(d, 4) if d is not None else None for d in delta],
        "qoq_growth_rate_pct": growth_rates_pct,
        "delta2_arr": [round(d, 4) if d is not None else None for d in delta2],
        "yoy_growth_rate": round(yoy, 4) if yoy is not None else None,
        "trajectory": {**traj, **verdict},
        "growth_state": state,
        "caveats": caveats,
    }


def _fail(message: str) -> None:
    json.dump({"error": message}, sys.stdout, indent=2)
    print()
    sys.exit(1)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Compound Growth Check: derivatives of quarterly ARR, "
                    "trajectory classification, 10-state ladder placement."
    )
    parser.add_argument(
        "input",
        help="Path to a CSV (columns: quarter, arr) or a comma-separated "
             "list of ARR values, oldest first.",
    )
    parser.add_argument(
        "--unit", choices=["auto", "dollars", "thousands", "millions"],
        default="auto",
        help="Unit of the ARR values (default auto: 100,000 and above reads "
             "as dollars, below that as millions).",
    )
    parser.add_argument("--company", default="Company",
                        help="Company name for the output.")
    parser.add_argument("--nrr", type=float, default=None,
                        help="Net revenue retention as a decimal, "
                             "for example 1.15 for 115%%.")
    parser.add_argument("--cost-growth", type=float, default=None,
                        dest="cost_growth",
                        help="YoY cost growth rate as a decimal, "
                             "for example 0.20 for 20%%.")
    args = parser.parse_args()

    labels, values = parse_input(args.input)
    unit = resolve_unit(values, args.unit)
    result = run_check(
        labels, values, unit,
        company=args.company, nrr=args.nrr,
        cost_growth_rate=args.cost_growth,
    )
    json.dump(result, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
