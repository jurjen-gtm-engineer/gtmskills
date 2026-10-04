# Data Source Discovery Guide (A Thinking Pattern)

> **Read this to learn the method, not to copy from a list.**
>
> This guide teaches HOW to discover public data sources for any company: which regulators own which pain, which fields create urgency, which stacks form cascades. It deliberately contains no exhaustive catalog. Every company sits at a unique intersection of regulators (its industry's agency, its customers' agencies, its suppliers' agencies, its geography's registries), so the right sources for one playbook will rarely be the right sources for the next. Every playbook must do its own discovery.
>
> **Attribution:** the source-ranking model (ground-truth ladder, join-key primacy, census-before-trigger, provenance gates) is based on concepts from Jordan Crawford (Blueprint GTM), restated in this skill's own words.

---

## The five discovery questions

Before Phase 4 proposes a single source, answer these for the target:

1. Which agencies regulate the target's *customers* (not just the target)?
2. Which agencies regulate the target's *suppliers* and the materials they handle?
3. What national or regional database equivalents exist in the target's geography?
4. What dated or temporal field in those databases creates urgency on a 30-180 day window?
5. Which two databases share an entity ID (facility number, provider number, tax ID, registration number) such that a cross-reference becomes a cascade?

If you answer those five questions for the target, you will discover the right sources for that specific company.

---

## Two jobs, in order: census, then trigger

Every list build is *first* a **census** problem (who is the universe, and what unique ID joins them?) and *only then* a **trigger** problem (what dated event creates urgency?). Most regulator databases are trigger sources. Registries and mandated disclosures are census sources. Skip the census and you are enriching a list somebody else already photocopied. A trigger source with no census underneath it is a list of events, not a list of accounts.

---

## How to rank ANY source: five multiplied factors

The factors MULTIPLY, not add: a zero on any one zeroes the source.

| Factor | The question to ask the source |
|---|---|
| **Ground-truth distance** | How close is this to the actual event? A registry that recorded a real license beats a database that guessed at it. |
| **Join-key quality** | Does every row carry a unique ID that connects it to other files without fuzzy name-matching? |
| **Coverage** | The whole universe, or a self-selected slice? |
| **Free bulk access** | Can you download the entire thing, or only peek one record at a time? |
| **Update cadence** | Refreshed weekly, or frozen years ago? |

### The ground-truth ladder (six rungs)

| Rung | What it is | Generic examples |
|---|---|---|
| **1** | Government registry with a unique ID: someone had to legally register and got a number | National provider registries, license rosters, company registers |
| **2** | Legally mandated disclosure | Securities filings, statutory annual accounts, franchise disclosures |
| **3** | Certification and professional directories | Board certifications, trade-body credential lists |
| **4** | Platform data with real-world grounding: proves a storefront exists, and stops there | Map platforms, open geodata |
| **5** | Association membership lists: self-selected, often a fraction of the real market | Industry-association member directories |
| **6** | Scraped aggregators and resold B2B databases: stale, lineage gone | Most of what gets sold as "a database" |

Most vendors sell rung six and call it a database. The census you actually want lives on rungs one and two, and much of it is public.

### Two hard gates that override any score

1. **Provenance.** The source must be the original or the publisher's own copy, never somebody's scrape, and it must carry a real date. A scrape can inform a lead; it can never be the foundation a total addressable market is built on.
2. **Personally verified.** Treat any claim of "free bulk business data" as false until you have personally downloaded the file. Do not cite a source in a play until you have opened it and confirmed the fields you need exist.

---

## The join key decides everything after that

A clean unique key outranks any richness a source is missing.

- **With a key:** multiple registry files joined on a shared identifier, zero fuzzy matching, in one pass.
- **Without a key:** entity resolution guessing which "Smith Plumbing" is which, and an over-merged mess you have to split back apart.

Common key families (varies by country): healthcare provider numbers, employer tax IDs, government-contractor entity IDs, legal-entity identifiers, chamber-of-commerce or company-register numbers, transport-operator numbers, license numbers.

**Two files sharing an ID is not a nice-to-have. It is the play.** A play built on two files that share a unique ID beats a play built on fuzzy name-matching, every time.

**Dedup rule:** fold duplicate entities into one row, carrying the full history. An account appearing in three source files is your strongest account; a pipeline that lists it three times destroys exactly the signal that made it strongest. Key on a stable ID (domain, registry number, normalized profile URL), never a company name.

---

## Where to look: source families

Illustrative families, not a catalog. Every jurisdiction has its own versions.

| Family | Examples of what lives there | Typical role |
|---|---|---|
| Company registers | National business registries, formation dates, officer names, industry codes | Census |
| Securities and financial regulators | Public filings, enforcement actions, consent orders | Census + trigger |
| Workplace safety regulators | Inspections, citations, severity classes, abatement deadlines | Trigger |
| Environmental regulators | Facility permits, violations, enforcement | Trigger |
| Health and care regulators | Facility ratings, deficiency findings, inspection dates | Trigger |
| Food and drug regulators | Warning letters, inspection observations, recalls | Trigger |
| Transport regulators | Operator registrations, safety scores, filing deadlines | Census + trigger |
| Courts and dockets | Lawsuits, parties, filing dates | Trigger |
| Public procurement | Tenders, awards, award dates (renewal clocks) | Trigger |
| Permits and parcels | Building permits, ownership rolls, valuations | Census + trigger |
| Breach and vulnerability portals | Disclosed breaches, known-exploited-vulnerability lists with due dates | Trigger |
| Technographic detectors | Tech-stack identification services, page-source pattern search | Enrichment + segment boundary |
| Jobs and people platforms | Job postings, headcount, tenure, hiring velocity | Enrichment |
| Review platforms | Customer and employee reviews with dates and text | Customer-voice anchor |
| Grants, awards, certifications | Innovation grants, industry awards, certification rosters | Segment boundary |

**Map the target's CUSTOMERS' regulators, not just the target's own.** For B2B products, the regulators that create buying urgency usually sit on the customers' industries. Enumerate the target's top 2-3 customer industries (from its case studies and logo wall) and identify the dominant regulator plus its dated field for each. Skip this only when the target sells purely to consumers or to unregulated SMBs.

---

## Compute the clock

The strongest timing signals are often **arithmetic, not data**: a public date plus a known contractual clock equals a buying window no vendor can resell.

Ask of every ICP: what contractual clock is ticking on this buyer, which public record starts it, and what window does the subtraction produce? Candidates:

- Lease or contract end dates
- Certification validity periods
- Software or hardware support end-of-life
- Asset refresh cycles
- Funding runway (roughly 18-24 months from a round)
- Executive tenure (roughly 18-24 months to show results)
- Regulatory grace periods after a filing or citation

A playbook whose leading indicators are all fields someone could buy has left the defensible signal on the table.

---

## Dead-end awareness

Half the value of source discovery is knowing what is broken. Before proposing any source, check:

- **Is it still live?** Government portals get discontinued and reorganized; links people still pass around may be dead.
- **Is it actually free?** Some frequently recommended registries are paid despite their reputation.
- **Do the terms allow storage?** Some platform APIs prohibit storing the names and addresses you pull. Read the terms before building on them.
- **Can it vanish?** A lead dump you do not control can go dark overnight. That is rung six in one sentence.
- **Aggregators locate, they never corroborate.** An aggregator is one voice, not a second opinion. The register behind it is the real source.

---

## Probe every provider filter with a known-answer test

Many data APIs, handed a filter they do not support, silently ignore it and return confident-looking results. You ship a list built on a query that never ran, and nothing in the response tells you. Before any play depends on a provider filter:

1. Run it against records whose answer you already know.
2. Verify the right rows came back.
3. Verify the filter changed the result set at all (same query with and without it; identical counts means it was ignored).

---

## Multi-agency cascade patterns (highest value)

Plays that score 9.0+ frequently stack multiple agencies on the **same facility or entity**. The cascade is the play. Generic patterns:

- Safety regulator + environmental regulator + industry regulator on the same facility
- Transport regulator + safety regulator on the same operator number
- Multiple financial regulators on the same institution
- Regulator finding + court docket + review-platform complaints on the same company

When a target appears in 2+ databases within a 90-day window, that convergence is the message. Lead with the timeline, not the violation.

---

## Customer-discovery families (vendor-architecture-dependent)

When the ICP is "users of vendor X," the discovery method depends on the vendor's architecture, not on the buyer or vertical. Pick the family before picking a tool.

- **Family A: Embed.** The vendor distributes a JS snippet customers integrate into their own sites (schedulers, chat widgets, analytics). Discover via page-source pattern search on the snippet URL.
- **Family B: Tenant.** The platform hosts customers at subdomains (`customer.vendor-cloud.example`). Discover via web-crawl indices, then verify with HTTP headers.
- **Family C: Logo wall.** The vendor publishes customer logos on a /customers page (legal-approved, near-perfect precision, lowest volume). Discover via a simple crawl of the logo grid.

Diagnose first: applying Family A's tool to a Family B vendor yields zero results.

---

## Source-scoring rubric (run in Phase 4 on every proposed source)

Every source proposed in Phase 4 must clear this scorecard before being included in plays. Re-run it on every refresh, not just at first build: sources disappear, costs shift, coverage changes.

| Dimension | What it measures | 1 (poor) | 5 (good) |
|---|---|---|---|
| **Ground-truth distance** | How far is this from the real-world event? (the six-rung ladder above) | Rung 5-6: association list, scraped aggregator | Rung 1-2: registry with a unique ID, or mandated disclosure |
| **Join-key quality** | Does every row carry a unique ID that joins to other files with no fuzzy matching? | No key: name and address only | Clean unique key (registry number, tax ID, license number) |
| **Coverage** | What share of the target segment appears in this source? | Under 10% (only the largest accounts) | Over 70% |
| **Bulk access** | Can this be queried without paying, and downloaded whole? | Paid API only, one record at a time | Free bulk download of the full file |
| **Data quality / cadence** | Is the data dated, structured, reliable, refreshed? | Stale text, frozen years ago | Versioned, dated, ID-keyed, refreshed weekly or monthly |
| **Cost** | What does it cost per query at the volume needed? | Expensive per query or vendor lock-in | Free or one-time extraction |

A source must score 3+ on every dimension AND 4+ on at least two dimensions to be included. A source scoring under 3 on any single dimension is excluded regardless of how strong the others are. The provenance and personally-verified gates (above) override the score entirely.

Remember the five factors MULTIPLY: a perfectly fresh, richly fielded source with no join key and no bulk download still cannot build you a market.
