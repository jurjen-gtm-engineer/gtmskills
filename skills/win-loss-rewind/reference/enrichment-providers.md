# Enrichment providers per signal (Phase 0 + Phase 2)

Deterministic-first: a plain HTML-to-text fetch plus regex before any paid provider. Use a paid scraper only on the residual the free fetch cannot handle. The provider names below are examples of the category, not a requirement. Use the stack you already have.

| Signal type | Free-first path | Paid provider (residual only) |
|-------------|-----------------|-------------------------------|
| Domain resolves / real page (Phase 0) | HTML-to-text fetch | a scraping API such as Firecrawl |
| LinkedIn company exists + active (Phase 0) | none | a LinkedIn company data provider |
| Headcount sanity check (Phase 0) | LinkedIn page parse | People Data Labs, Crustdata |
| Careers page roles posted | HTML-to-text on /careers + regex | TheirStack, PredictLeads |
| Hiring velocity change | none | PredictLeads, TheirStack |
| Website self-description change (new region/product/compliance page) | HTML-to-text | a scraping API (JS-rendered residual) |
| Tech-stack adopt/drop over time | none | BuiltWith, HG Insights |
| Leadership / headcount inflection | none | a LinkedIn data provider, Crustdata |
| Funding / M&A event | web search API | PredictLeads |
| Regulatory / professional registrations | direct registry fetch (chamber of commerce, financial regulator register, Secretary of State) | a scraping API on the registry residual |
| GitHub public-org activity (technical buyers) | GitHub REST API (free) | none |
| Pain themes from calls (Phase 4) | n/a | the `blueprint-swarm` skill (sub-agents) |

## Rules

- Keep each company's data in its own workspace or account. Check which workspace is active before any data operation.
- Per-row LLM extraction runs as sub-agents, not as model API calls inside the scripts.
- Every paid call must justify why a free deterministic step could not do it first.
