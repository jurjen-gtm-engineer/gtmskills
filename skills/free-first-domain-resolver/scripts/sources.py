"""Discovery tiers for the free-first domain resolver.

Each tier returns a list of `Candidate` dicts: {domain, source, phone?, address?,
raw?}. Cheapest first. The orchestrator (resolve.py) stops at the first candidate
that *verifies*, so order matters more than completeness.
"""
from __future__ import annotations

import os
import re
import sqlite3
from typing import Optional

import requests
import tldextract

UA = {"User-Agent": "Mozilla/5.0 (compatible; free-first-domain-resolver/1.0)"}
TIMEOUT = 12


# --------------------------------------------------------------------------- #
# normalization
# --------------------------------------------------------------------------- #
_WS = re.compile(r"\s+")
_NONALNUM = re.compile(r"[^a-z0-9 ]+")


def normalize_name(name: str) -> str:
    """Lowercase, strip punctuation, collapse whitespace. Used as a join key."""
    n = (name or "").lower()
    n = n.replace("&", " and ")
    n = _NONALNUM.sub(" ", n)
    return _WS.sub(" ", n).strip()


def name_tokens(name: str) -> list[str]:
    return [t for t in normalize_name(name).split(" ") if t]


def registrable_domain(url_or_domain: str) -> Optional[str]:
    """Return the registrable domain (example.co.uk) or None."""
    if not url_or_domain:
        return None
    ext = tldextract.extract(url_or_domain.strip())
    if not ext.domain or not ext.suffix:
        return None
    return f"{ext.domain}.{ext.suffix}".lower()


# --------------------------------------------------------------------------- #
# tier 0: existing
# --------------------------------------------------------------------------- #
def from_existing(existing_domain: Optional[str]) -> list[dict]:
    d = registrable_domain(existing_domain or "")
    return [{"domain": d, "source": "existing"}] if d else []


# --------------------------------------------------------------------------- #
# tier 1: owned local table (free)
# --------------------------------------------------------------------------- #
def from_owned_table(
    conn: Optional[sqlite3.Connection], name: str, zip_code: Optional[str]
) -> list[dict]:
    if conn is None:
        return []
    key = normalize_name(name)
    cur = conn.cursor()
    rows = []
    if zip_code:
        cur.execute(
            "SELECT domain, phone, address FROM businesses "
            "WHERE name_key=? AND zip=? AND domain IS NOT NULL AND domain!='' LIMIT 5",
            (key, str(zip_code).strip()),
        )
        rows = cur.fetchall()
    if not rows:  # fall back to name-only (no geographic pin -> weaker, but a candidate)
        cur.execute(
            "SELECT domain, phone, address FROM businesses "
            "WHERE name_key=? AND domain IS NOT NULL AND domain!='' LIMIT 5",
            (key,),
        )
        rows = cur.fetchall()
    out = []
    for domain, phone, address in rows:
        d = registrable_domain(domain)
        if d:
            out.append(
                {"domain": d, "source": "owned_table", "phone": phone, "address": address}
            )
    return out


# --------------------------------------------------------------------------- #
# tier 2: Google Knowledge Graph (free, 100k/day)
# --------------------------------------------------------------------------- #
def from_knowledge_graph(name: str, api_key: Optional[str]) -> list[dict]:
    if not api_key:
        return []
    try:
        r = requests.get(
            "https://kgsearch.googleapis.com/v1/entities:search",
            params={"query": name, "key": api_key, "limit": 3,
                    "types": "Organization,Corporation,LocalBusiness"},
            headers=UA, timeout=TIMEOUT,
        )
        r.raise_for_status()
        data = r.json()
    except Exception:
        return []
    out = []
    for item in data.get("itemListElement", []):
        result = item.get("result", {})
        url = result.get("url")  # KG's "official site"
        d = registrable_domain(url or "")
        if d:
            out.append({
                "domain": d, "source": "knowledge_graph",
                "kg_name": result.get("name"),
                "sameAs": [u for u in (result.get("detailedDescription", {}) or {})
                           .get("url", "").split() if u],
            })
    return out


# --------------------------------------------------------------------------- #
# tier 3: Serper (one cheap Google search)
# --------------------------------------------------------------------------- #
def from_serper(name: str, api_key: Optional[str], hint: str = "") -> list[dict]:
    if not api_key:
        return []
    q = f"{name} {hint}".strip()
    try:
        r = requests.post(
            "https://google.serper.dev/search",
            headers={"X-API-KEY": api_key, "Content-Type": "application/json"},
            json={"q": q, "num": 8}, timeout=TIMEOUT,
        )
        r.raise_for_status()
        data = r.json()
    except Exception:
        return []
    out, seen = [], set()
    for res in data.get("organic", []):
        d = registrable_domain(res.get("link", ""))
        if d and d not in seen:
            seen.add(d)
            out.append({"domain": d, "source": "serper", "title": res.get("title")})
    return out


# --------------------------------------------------------------------------- #
# tier 4: Google Places Text Search (fraction of a cent)
# --------------------------------------------------------------------------- #
def from_places(name: str, api_key: Optional[str], hint: str = "") -> list[dict]:
    if not api_key:
        return []
    try:
        r = requests.post(
            "https://places.googleapis.com/v1/places:searchText",
            headers={
                "Content-Type": "application/json",
                "X-Goog-Api-Key": api_key,
                "X-Goog-FieldMask":
                    "places.displayName,places.websiteUri,"
                    "places.internationalPhoneNumber,places.formattedAddress",
            },
            json={"textQuery": f"{name} {hint}".strip(), "maxResultCount": 3},
            timeout=TIMEOUT,
        )
        r.raise_for_status()
        data = r.json()
    except Exception:
        return []
    out = []
    for p in data.get("places", []):
        d = registrable_domain(p.get("websiteUri", ""))
        if d:
            out.append({
                "domain": d, "source": "places",
                "places_name": (p.get("displayName") or {}).get("text"),
                "phone": p.get("internationalPhoneNumber"),
                "address": p.get("formattedAddress"),
            })
    return out


def open_owned_db(path: Optional[str]) -> Optional[sqlite3.Connection]:
    if not path or not os.path.exists(path):
        return None
    return sqlite3.connect(path)
