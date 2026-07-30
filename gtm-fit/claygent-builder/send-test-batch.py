#!/usr/bin/env python3
"""Send test batch to a Clay webhook. Example: B2B SaaS qualification Claygent.

Set your own Clay webhook URL via the CLAY_WEBHOOK_URL environment variable,
or replace the placeholder below with the webhook URL from your Clay table.
"""

import json
import os
import sys
import time

import requests

WEBHOOK_URL = os.environ.get("CLAY_WEBHOOK_URL", "")

if not WEBHOOK_URL:
    sys.exit("Set CLAY_WEBHOOK_URL to your Clay table's webhook URL before running.")

PROMPT_TEMPLATE = """You are a B2B SaaS classification agent. Your job is to visit a company website and determine whether the company is a B2B SaaS business. You output structured JSON and nothing else.

DEFINITIONS:
- "b2b_saas": Software delivered via the cloud, sold to businesses, with recurring revenue (subscription, per-seat, usage-based).
- "b2c_saas": Software delivered via the cloud, sold to individual consumers.
- "non_saas": Hardware, physical products, professional services, consulting, agencies.
- "unknown": Site is down, parked, under construction, or content is too ambiguous.

DECISION TREE (evaluate in order, stop at first match):
1. Site unreachable, parked, or under construction -> "unknown"
2. Software + per-seat/subscription pricing + business customers -> "b2b_saas" (high confidence)
3. Software + business customers + cloud delivery, no pricing visible -> "b2b_saas" (medium confidence)
4. Software sold to individual consumers -> "b2c_saas"
5. Physical products, hardware, or non-software services -> "non_saas"
6. Consulting/agency that uses software but doesn't sell it -> "non_saas"
7. Serves both B2B and B2C -> classify by PRIMARY revenue source, note ambiguity
8. Insufficient info after homepage + one page -> "unknown"

EXAMPLES:
CORRECT: slack.com -> b2b_saas (high). Cloud messaging for teams. Per-user pricing. Enterprise features.
CORRECT: nike.com -> non_saas (high). Physical products. E-commerce retailer.
CORRECT: workday.com -> b2b_saas (high). Cloud HR/finance software. Enterprise customers. Subscription model.
WRONG: accenture.com -> Do NOT classify as b2b_saas. They sell consulting, not software -> non_saas.
WRONG: shopify.com -> DO classify as b2b_saas. They sell software to businesses. Their customers selling to consumers doesn't make Shopify B2C.

TASK: Visit {domain} and classify whether it is a B2B SaaS business.
1. Check homepage for product/service description
2. Look for pricing page (/pricing, /plans): strongest signal
3. Check for business customer indicators (logos, case studies, team features)
4. Visit max 3 pages total

CONSTRAINTS:
- Do NOT classify from domain name alone: visit the site
- Require 2+ signals for "high" confidence
- If unsure -> "unknown"
- No disclaimers in reasoning

Return JSON matching the schema."""

JSON_SCHEMA = {
    "type": "object",
    "properties": {
        "is_b2b_saas": {"type": "boolean"},
        "classification": {"type": "string", "enum": ["b2b_saas", "b2c_saas", "non_saas", "unknown"]},
        "confidence": {"type": "string", "enum": ["high", "medium", "low"]},
        "reasoning": {"type": "string"},
        "primary_evidence": {"type": "string"}
    },
    "required": ["is_b2b_saas", "classification", "confidence", "reasoning", "primary_evidence"],
    "additionalProperties": False
}

TEST_DOMAINS = [
    ("notion.so", "b2b_saas"),
    ("hubspot.com", "b2b_saas"),
    ("linear.app", "b2b_saas"),
    ("mcdonalds.com", "non_saas"),
    ("nike.com", "non_saas"),
    ("workday.com", "b2b_saas"),
    ("canva.com", "b2c_saas"),
]

print(f"Sending {len(TEST_DOMAINS)} test rows to Clay...")

for i, (domain, expected) in enumerate(TEST_DOMAINS):
    prompt = PROMPT_TEMPLATE.format(domain=domain)
    payload = {
        "domain": domain,
        "prompt": prompt,
        "prompt_version": "v1",
        "json_schema": json.dumps(JSON_SCHEMA),
        "expected_classification": expected,
    }
    try:
        r = requests.post(WEBHOOK_URL, json=payload, timeout=10)
        print(f"[{i+1}/{len(TEST_DOMAINS)}] {domain} -> {r.status_code} {r.text[:200]}")
    except Exception as e:
        print(f"[{i+1}/{len(TEST_DOMAINS)}] {domain} -> ERROR: {e}")
    time.sleep(1)

print("\nAll rows sent. Set up Claygent column in Clay with the prompt from /prompt column.")
print("JSON schema for Claygent:")
print(json.dumps(JSON_SCHEMA, indent=2))
