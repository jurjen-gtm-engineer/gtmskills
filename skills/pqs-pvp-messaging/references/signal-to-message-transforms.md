# Signal → Message Transforms

The mechanical core of this skill: given a raw signal, how do you derive each line of the email? This file is the lookup table. It also holds the lane classifier and the Data-Key / Leading / Trailing framework that decides PQS vs PVP.

---

## The universal pipeline (every message, both types)

```
SIGNAL  →  SITUATION  →  SECOND-ORDER PROBLEM  →  WHY  →  [VALUE]  →  ASK
 raw       restate as     the bite they              the          PQS: proof    low-friction
 fact      their reality  didn't budget/notice      mechanism     PVP: the      binary or gift
                                                                  quantified
                                                                  insight
```

- **PQS stops the value at recognition + (optional) a named case.** The give is "you get my world."
- **PVP replaces the value with stitched data they can't generate.** The give is the intelligence itself.

The work is identical up to the WHY. The fork is whether you have a **data cocktail** (→ PVP) or only the **situation** (→ PQS).

---

## The lane classifier (do this first, every time)

Score the data you have on these four. All four YES → PVP-viable. Otherwise PQS.

| Test | Pass condition |
|---|---|
| **Independence** | Useful to them even if they never reply |
| **Concreteness** | Contains a name / number / date / location specific to *this* prospect |
| **Asymmetry** | They are not already tracking this themselves |
| **Relevance** | The insight's domain = what your product does |

> Honesty check: if the "data" is just the signal restated ("you're hiring," "you migrated"), that's a **situation**, not a cocktail → PQS. A PVP needs at least two sources whose *combination* says something new.

---

## Finding the bite (the highest-leverage move in PQS)

The bite is the second-order problem the signal implies but the prospect hasn't connected. Generate it by interrogating the signal:

1. **"This happened. So what breaks next?"**: the downstream consequence.
2. **"Whose budget is that on?"**: if the answer is "nobody planned for it," that's the bite.
3. **"What do they feel but can't name?"**: the anxiety/uncertainty under the obvious problem (e.g. "not knowing how long the exposure lasts").
4. **"What does every vendor get wrong about this situation?"**: the structural blind spot.

The strongest bites are *unbudgeted* (a cost nobody scoped) or *unnamed* (a feeling they can't articulate).

---

## Signal-type → message-move lookup

| Signal type | Likely lane | Situation line | Typical bite | PVP upgrade (data to stitch) |
|---|---|---|---|---|
| **Tech adoption** (BuiltWith, job ad names a tool) | PQS, PVP if version-detectable | "looks like you run [tool]" | the hidden cost/limit of that tool at their scale | tool version × known CVE/limitation × their subdomain headers |
| **Migration / re-platform** (ERP, patient record system, cloud move) | PQS | "you're moving to [system] while [old] is still core" | the rebuild/backlog nobody scoped onto the program budget | which integrations break × migration timeline × peer migration outcomes |
| **Regulation / new law** (NIS2, DORA, a published vulnerability) | PQS, PVP if registry-backed | "the [law] is coming and names you as [category]" | the burden of proof becomes a hard requirement with a penalty | who's-affected registry (Data Key) × enforcement actions + $ (Trailing) |
| **Hiring** (role posted) | PQS (avoid the differentiation trap) | "you've got [role] open" | what that hire will inherit / can't fix alone | role × tenure of opening × what peers who hired this role then needed |
| **M&A / merger** | PQS | "you merged with [party] on [date]" | two systems/processes now overlap with no single source of truth | both orgs' tech stacks × integration backlog estimate |
| **Funding round** | PVP-leaning (everyone sends the lazy version) | DON'T lead with "congrats on the raise" | what the raise commits them to that they haven't staffed | raise size × stated use-of-funds × hiring/spend pattern of peers post-raise |
| **Permit / license filing** | PVP (gold) | the filing itself, specific | the opportunity/obligation the filing creates | permit registry × adjacent activity × dollar value |
| **Pricing / cost exposure** | PVP | their current price/cost vs cohort | they're leaving money on the table / overpaying | aggregated cohort pricing × their geo/segment |
| **Idle asset / utilization** | PVP | the asset's idle state, from public records | the revenue it's not earning | asset registry × demand signal nearby × $ rental/sale value |
| **Their own customers/leads** | PVP (naming-three) | name 3 of their customers | a specific fact about each they don't know | their customer list × public signals on each |
| **No signal, broad ICP** | PQS-segment | the shared reality of everyone in the segment | the cost the whole segment quietly carries | (none, this is segment-level recognition, the floor of PQS) |

---

## The Data-Key / Leading / Trailing framework (PVP data architecture)

A PVP gets stronger the more of these three you stack. (Source: Cannonball "Three Keys to Navigating Public Data.")

| Concept | Role | Makes the message feel like… | Example source |
|---|---|---|---|
| **Data Key** | the source that makes the segment real + findable; the boundary condition | "they know who I am" | CISA KEV, NPPES, SoS filings, BuiltWith, permit registries |
| **Leading indicator** | a detectable signal the problem is **active now**, before consequences hit | a timely **warning** | a CVE-affected version live, a permit filed nearby, a price index spiking |
| **Trailing indicator** | proof the pain **already materialized for peers**, with a dollar amount | **credibility + urgency** without pushing | regulator settlements, court records, "nine operators your size were fined for this" |

**Stacking:**
- 1 key = a nameable, findable segment.
- 2 keys = Venn-diagram targeting (two angles on the same prospect).
- 3 keys + both indicator types = the message nearly writes itself.

**Ideal PVP combination:** Data Key + Leading indicator (the warning) + Trailing indicator (the priced proof). That's the secure-file-transfer PVP in the swipe file: platform and version (key) × live vulnerability on their build (leading) × regulator settlements (trailing).

---

## The earned-right gate (before you send)

Ask yourself (the question is from Crawford's Cannonball newsletter): have I done enough work with this data to earn a place in this person's inbox?

If the only thing you can say is the signal restated, you have *not* earned a PVP, ship a clean PQS instead. The Data Keys/indicators are not just analytical tools; they are the permission check for whether the message deserves to exist.

---

## Worked transform, start to finish

**Raw signal:** "Hospital X went live with a new patient record system on June 1."

1. **Lane check:** do I have stitched external data they are not tracking? No. I have the go-live fact plus domain knowledge. **Lane C, PQS.**
2. **Situation:** "I saw you have been working in the new patient record system since June 1."
3. **So what breaks next?** The record system is the easy part. Everything around it (medication, finance, the regional care chain) connects separately. That is the **bite**.
4. **Why:** each of those is a separate integration that has to be set up again. If one lags, data falls between the cracks during the switch.
5. **Confirm:** "Is the work on those surrounding connections on someone's desk yet?"
6. **PVP upgrade path (noted for later):** if I could pull which surrounding systems this hospital runs (public tenders, IT job ads, case studies), the known integration gaps of the new system, and a peer hospital's incident after go-live, that becomes a Lane A PVP. Until then, the PQS is the honest message to ship.

---

## Quick reference: the moves in one screen

- **PQS = mirror + bite + confirm.** No data cocktail required. Recognition is the give.
- **PVP = stitch 2 to 5 sources → quantify the opportunity → predict their future → offer more value.** The data is the give.
- **Bite** = the unbudgeted or unnamed second-order problem. Find it with "so what breaks next, and whose budget is that on?"
- **Lane honesty** beats ambition: a real PQS > a fake PVP.
- **Stack Data Key + Leading + Trailing** to make a PVP hard to ignore.
- **Gates:** qualification (hard-disqualify, not headcount) · quantification (10× believable?) · communication (feels seen, not sold) · permissionless-gift (forwardable + actionable without context).
