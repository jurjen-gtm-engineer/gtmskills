"""Verification: ask the page who it is, never the SSL certificate.

verify_candidate() fetches the candidate domain, follows redirects to the final
domain, extracts page-declared identity (title / Open Graph / JSON-LD), checks
DNS+MX liveness, screens disqualifiers (parked / blacklist / gov), and scores a
name match. Returns a verdict dict the orchestrator turns into CONFIRMED /
MAYBE / REJECT.
"""
from __future__ import annotations

import json
import re
from typing import Optional

import requests
import tldextract

import calibration as C
from sources import name_tokens, normalize_name, registrable_domain, UA, TIMEOUT

try:
    import dns.resolver  # dnspython
    _HAVE_DNS = True
except Exception:
    _HAVE_DNS = False


# --------------------------------------------------------------------------- #
# pure-python token-set ratio (0-100), so we carry no fuzzy-match dependency
# --------------------------------------------------------------------------- #
def token_set_ratio(a: str, b: str) -> int:
    ta, tb = set(name_tokens(a)), set(name_tokens(b))
    if not ta or not tb:
        return 0
    inter = ta & tb
    # Jaccard-ish on the smaller set: how much of the shorter name is covered
    base = len(inter) / min(len(ta), len(tb))
    # bonus when one is a subset of the other (acronyms aside)
    if ta <= tb or tb <= ta:
        base = max(base, 0.9)
    return int(round(base * 100))


def acronym_match(name: str, domain: str) -> bool:
    """bmc.org for 'Boston Medical Center', ssim.com for 'Southside Internal Medicine'."""
    toks = [t for t in name_tokens(name) if t not in C.GENERIC_TOKENS] or name_tokens(name)
    if len(toks) < 2:
        return False
    acro = "".join(t[0] for t in toks)
    label = tldextract.extract(domain).domain.lower()
    return acro == label and len(acro) >= 2


def distinctive_token_count(name: str) -> int:
    return len([t for t in name_tokens(name) if t not in C.GENERIC_TOKENS])


# --------------------------------------------------------------------------- #
# liveness
# --------------------------------------------------------------------------- #
def dns_alive(domain: str) -> bool:
    if not _HAVE_DNS:
        return True  # can't check -> don't block
    try:
        dns.resolver.resolve(domain, "A", lifetime=6)
        return True
    except Exception:
        try:
            dns.resolver.resolve(domain, "AAAA", lifetime=6)
            return True
        except Exception:
            return False


def has_mx(domain: str) -> bool:
    if not _HAVE_DNS:
        return False
    try:
        return len(dns.resolver.resolve(domain, "MX", lifetime=6)) > 0
    except Exception:
        return False


# --------------------------------------------------------------------------- #
# page-declared identity
# --------------------------------------------------------------------------- #
_TITLE = re.compile(r"<title[^>]*>(.*?)</title>", re.I | re.S)
_META = re.compile(r'<meta[^>]+>', re.I)
_JSONLD = re.compile(
    r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', re.I | re.S
)


def _meta_content(html: str, prop: str) -> Optional[str]:
    for tag in _META.findall(html):
        if re.search(rf'(property|name)=["\']{re.escape(prop)}["\']', tag, re.I):
            m = re.search(r'content=["\'](.*?)["\']', tag, re.I)
            if m:
                return m.group(1).strip()
    return None


def _jsonld_org(html: str) -> dict:
    out = {"name": None, "sameAs": []}
    for block in _JSONLD.findall(html):
        try:
            data = json.loads(block)
        except Exception:
            continue
        items = data if isinstance(data, list) else [data]
        # handle @graph
        flat = []
        for it in items:
            if isinstance(it, dict) and "@graph" in it:
                flat.extend(it["@graph"])
            else:
                flat.append(it)
        for it in flat:
            if not isinstance(it, dict):
                continue
            t = it.get("@type", "")
            t = t if isinstance(t, str) else " ".join(t)
            if any(k in t for k in ("Organization", "Corporation", "LocalBusiness")):
                out["name"] = out["name"] or it.get("name")
                sa = it.get("sameAs")
                if isinstance(sa, str):
                    out["sameAs"].append(sa)
                elif isinstance(sa, list):
                    out["sameAs"].extend(sa)
    return out


def fetch_identity(domain: str) -> dict:
    """Fetch https://domain, follow redirects, return declared identity + final domain."""
    info = {"reachable": False, "final_domain": None, "title": None,
            "og_site_name": None, "og_title": None, "jsonld_name": None,
            "sameAs": [], "text_sample": "", "parked": False}
    html = ""
    for scheme in ("https://", "http://"):
        try:
            r = requests.get(scheme + domain, headers=UA, timeout=TIMEOUT,
                             allow_redirects=True)
            info["reachable"] = True
            info["final_domain"] = registrable_domain(r.url) or domain
            html = r.text or ""
            break
        except Exception:
            continue
    if not html:
        return info
    sample = re.sub(r"<[^>]+>", " ", html[:20000]).lower()
    info["text_sample"] = sample
    info["parked"] = any(m in sample for m in C.PARKED_MARKERS)
    mt = _TITLE.search(html)
    if mt:
        info["title"] = re.sub(r"\s+", " ", mt.group(1)).strip()
    info["og_site_name"] = _meta_content(html, "og:site_name")
    info["og_title"] = _meta_content(html, "og:title")
    org = _jsonld_org(html)
    info["jsonld_name"] = org["name"]
    info["sameAs"] = org["sameAs"]
    return info


# --------------------------------------------------------------------------- #
# the verdict
# --------------------------------------------------------------------------- #
def _phone_digits(p: Optional[str]) -> str:
    return re.sub(r"\D", "", p or "")[-9:]  # last 9 digits, country-code agnostic


def verify_candidate(name: str, candidate: dict,
                     expected_phone: Optional[str] = None) -> dict:
    """Return {verdict: CONFIRMED|MAYBE|REJECT, domain, name_match, corroborators, signals}."""
    domain = candidate["domain"]
    signals: list[str] = []
    corroborators = 0

    # --- disqualifiers first (cheap) ---
    if domain in C.BLACKLIST_DOMAINS or registrable_domain(domain) in C.BLACKLIST_DOMAINS:
        return _v("REJECT", domain, 0, 0, ["blacklisted_directory"])
    if domain.endswith(C.GOV_TLDS) and "government" not in normalize_name(name) \
            and "city of" not in normalize_name(name):
        return _v("REJECT", domain, 0, 0, ["gov_portal_name_mismatch"])

    if C.REQUIRE_DNS and not dns_alive(domain):
        return _v("REJECT", domain, 0, 0, ["dns_dead"])

    ident = fetch_identity(domain)
    if not ident["reachable"]:
        return _v("REJECT", domain, 0, 0, ["unreachable"])
    if ident["parked"]:
        return _v("REJECT", domain, 0, 0, ["parked"])

    final = ident["final_domain"] or domain
    if final != domain:
        signals.append(f"redirect:{domain}->{final}")
        domain = final
        if domain in C.BLACKLIST_DOMAINS:
            return _v("REJECT", domain, 0, 0, signals + ["redirects_to_directory"])

    # --- name match against page-declared identity ---
    declared = " ".join(filter(None, [
        ident["og_site_name"], ident["jsonld_name"], ident["title"], ident["og_title"],
    ]))
    nm = token_set_ratio(name, declared)
    # also try matching against the domain label itself (anderson... case)
    nm = max(nm, token_set_ratio(name, tldextract.extract(domain).domain))
    if acronym_match(name, domain):
        nm = max(nm, C.NAME_MATCH_STRONG)
        signals.append("acronym_match")

    # --- corroborators ---
    if ident["og_site_name"] and token_set_ratio(name, ident["og_site_name"]) >= C.NAME_MATCH_MAYBE:
        corroborators += 1; signals.append("og_site_name")
    if ident["jsonld_name"]:
        corroborators += 1; signals.append("jsonld_org")
    if ident["sameAs"]:
        corroborators += 1; signals.append(f"sameAs:{len(ident['sameAs'])}")
    if C.COUNT_MX_AS_CORROBORATOR and has_mx(domain):
        corroborators += 1; signals.append("mx")
    if "redirect:" in " ".join(signals):
        corroborators += 1  # redirect-stable to a real site

    phone_match = False
    cand_phone = candidate.get("phone")
    if expected_phone and cand_phone and \
            _phone_digits(expected_phone) and _phone_digits(expected_phone) == _phone_digits(cand_phone):
        phone_match = True
        corroborators += 1
        signals.append("phone_match")

    # --- generic-name guard ---
    generic = distinctive_token_count(name) < C.DISTINCTIVE_TOKEN_FLOOR  # i.e. zero distinctive tokens
    if generic:
        signals.append("generic_name")

    # --- final gate ---
    if nm >= C.NAME_MATCH_STRONG and corroborators >= C.MIN_CORROBORATORS:
        if generic and not (phone_match or "sameAs" in " ".join(signals)
                            or any(s.startswith("sameAs") for s in signals)):
            # common name + no geographic/identity corroborator -> don't assert
            return _v("MAYBE", domain, nm, corroborators, signals + ["generic_needs_corroborator"])
        return _v("CONFIRMED", domain, nm, corroborators, signals)

    if C.PHONE_RESCUES_MAYBE and phone_match and nm >= C.NAME_MATCH_MAYBE:
        return _v("CONFIRMED", domain, nm, corroborators, signals + ["phone_rescue"])

    if nm >= C.NAME_MATCH_MAYBE:
        return _v("MAYBE", domain, nm, corroborators, signals)

    return _v("REJECT", domain, nm, corroborators, signals + ["name_mismatch"])


def _v(verdict, domain, nm, corr, signals):
    return {"verdict": verdict, "domain": domain, "name_match": nm,
            "corroborators": corr, "signals": signals}
