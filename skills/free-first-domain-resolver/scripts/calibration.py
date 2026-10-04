"""Calibrated thresholds for the free-first domain resolver.

These are this build's own defaults, not Jordan Crawford's tuned values. Tune them on a hand-labeled
slice before trusting a big run. See references/calibration.md for rationale.
"""

# --- name-match cutoffs (token-set ratio, 0-100) -------------------------------
NAME_MATCH_STRONG = 85   # >= this -> confident the page is this company
NAME_MATCH_MAYBE = 60    # [MAYBE, STRONG) -> needs a corroborator or the judge
# < NAME_MATCH_MAYBE -> reject this candidate outright

# --- generic-name guard -------------------------------------------------------
# A name with NO distinctive token (all words are generic, e.g. "The Services
# Group") can match the wrong business on text alone. A single distinctive brand
# token ("Gong", "Anthropic") is fine. When a name has zero distinctive tokens,
# a strong text match is NOT enough on its own -- require a hard corroborator
# (phone match / address / sameAs identity link).
# (The other risk -- many real businesses sharing one name, "Summit Roofing" in
# 12 cities -- is handled at the search tier: >1 candidate confirming -> ambiguous.)
DISTINCTIVE_TOKEN_FLOOR = 1
GENERIC_TOKENS = {
    "the", "and", "of", "for", "group", "company", "co", "corp", "corporation",
    "inc", "incorporated", "llc", "ltd", "limited", "plc", "gmbh", "bv", "nv",
    "holdings", "holding", "services", "service", "solutions", "systems",
    "international", "global", "partners", "associates", "enterprises",
    "consulting", "consultants", "technologies", "technology", "tech",
    "industries", "industrial", "national", "american", "us", "usa",
    "center", "centre", "clinic", "dental", "medical", "law", "agency",
    # very common small-business surnames/words that collide a lot
    "smith", "johnson", "anderson", "summit", "riverside", "premier",
    "elite", "first", "city", "metro", "valley", "north", "south", "east", "west",
}

# --- disqualifiers: a candidate domain that is one of these is never accepted --
# directories / social / aggregators (a top search hit is often one of these)
BLACKLIST_DOMAINS = {
    "linkedin.com", "facebook.com", "twitter.com", "x.com", "instagram.com",
    "youtube.com", "tiktok.com", "pinterest.com", "yelp.com", "yellowpages.com",
    "bbb.org", "crunchbase.com", "glassdoor.com", "indeed.com", "zoominfo.com",
    "apollo.io", "rocketreach.co", "wikipedia.org", "mapquest.com",
    "tripadvisor.com", "manta.com", "dnb.com", "bloomberg.com", "owler.com",
    "google.com", "maps.google.com", "amazon.com", "etsy.com", "wordpress.com",
    "wixsite.com", "godaddy.com", "squarespace.com", "blogspot.com", "medium.com",
}
# gov / institutional portals: accept only if the name itself is governmental
GOV_TLDS = (".gov", ".mil", ".gov.uk", ".gouv.fr", ".overheid.nl")

# parked / for-sale / dead landers
PARKED_MARKERS = (
    "this domain is for sale", "buy this domain", "domain for sale",
    "parked free", "godaddy.com/domainsearch", "sedoparking.com",
    "hugedomains.com", "is parked", "courtesy of", "default web page",
    "future home of something", "account suspended",
)

# --- liveness / corroboration -------------------------------------------------
REQUIRE_DNS = True       # candidate must resolve
COUNT_MX_AS_CORROBORATOR = True

# --- final gate ---------------------------------------------------------------
# CONFIRMED requires: name-match >= STRONG AND >=1 corroborator AND not disqualified.
# Corroborators: og:site_name match, JSON-LD Organization, redirect-stable,
# MX record present, phone match, sameAs link present.
MIN_CORROBORATORS = 1

# A confirmed phone match alone can rescue a MAYBE name-match (geographic case).
PHONE_RESCUES_MAYBE = True
