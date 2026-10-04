---
name: pqs-pvp-messaging
description: "Write a PQS (Pain-Qualified Segment) or PVP (Permissionless Value Proposition) cold email from one signal or data point about a prospect. Covers only the message itself: the email that mirrors their situation (PQS) or hands them intelligence they could not build themselves (PVP). PQS and PVP are Jordan Crawford's concepts (Blueprint GTM); the voice rules follow Josh Braun. Not for campaign design, sequences, sending setup or segmentation, not for building the segment (pain-qualified-segment, list-is-the-message) and not for grading a finished draft (qa-checklist)."
---

# PQS / PVP Messaging: the message, nothing else

> Your only job in this skill: take **one signal or piece of data** about a prospect and turn it into a **PQS or PVP email** that earns a reply. Not the campaign. Not the list. Not the infra. The message.

This is the message-craft core of Jordan Crawford's (Blueprint GTM) methodology, paired with Josh Braun's "Stop Persuading" voice. Targeting, segment proof, send settings and A/B tests are out of scope. Here we go from **signal → words**.

**Deep reference (load when you need depth):**
- `references/pqs-pvp-swipe-file.md`: annotated example messages (all invented, to teach the pattern)
- `references/signal-to-message-transforms.md`: signal type to message move lookup, the Data Key / Leading / Trailing framework, the lane classifier

---

## The one idea underneath both (read first)

**Crawford's core claim: selling power comes from information asymmetry.** Know more about the buyer's situation than they expect a stranger to know.

Both PQS and PVP are the same move: *manufacture more knowledge about the buyer's actual situation than the buyer expects a stranger to have, then hand it over as a gift they can use without ever replying.* They differ only in **how much** asymmetry you have and **what you do with it**:

| | **PQS**: Pain-Qualified Segment | **PVP**: Permissionless Value Proposition |
|---|---|---|
| What you have | A detectable **situation/pain** they already feel | **Data they could not generate themselves** (2+ sources stitched) |
| What the message does | **Mirrors** their reality back so precisely they self-identify | **Delivers intelligence**: names, numbers, dates, locations |
| The give | Recognition ("this person gets my world") | Independent value ("I'd pay for this") |
| Prospect awareness | Knows the problem | Has the problem, doesn't yet see the urgency |
| The gift test | Would they think *"how did they know?"* | Could they **forward it to a peer who'd act on it without context?** |
| Mentions your product? | **No** | **No** |

Crawford's own framing (in his Cannonball newsletter) is that **most companies cannot reach a true PVP**, and that is fine. A real PQS already beats nearly all the outbound in a buyer's inbox. PQS is not a consolation prize; it is the workhorse. PVP is the rare weapon you reach for only when you actually have stitched, non-obvious data.

---

## STEP 0: Pick the lane before you write a word

Start with a classifier, not a template. **Answer honestly, the lane sets what's achievable:**

```
Do I have a piece of EXTERNAL data about THIS prospect that:
  (a) they did not generate / are not tracking themselves, AND
  (b) is concrete (a name, number, date, location, filing, permit, price), AND
  (c) stays useful even if they never buy from me, AND
  (d) connects to the value my product creates?

├── YES to all four → LANE A: PVP-viable. Write a PVP. (Highest ceiling.)
│
├── Partial (I have a real detectable situation + one soft data point,
│   but nothing forwardable) → LANE B: PQS-primary, PVP-upside.
│   Write a PQS now; note what extra data source would upgrade it to PVP later.
│
└── NO (I only know the situation/pain they're in, no external data cocktail)
    → LANE C: PQS-only. Write a PQS. Don't fake a PVP, a "clever first line
      stapled to a demo request" is the #1 PVP failure.
```

**The litmus test for Lane A (memorize it):**
> If the email is useful on its own, without your product, it is a PVP. If it is a clever first line stapled to a demo request, it is not.

If you're not sure, you're in Lane B/C. Write the PQS. A great PQS beats a fake PVP every time.

---

## PQS: the anatomy

**Definition (after Blueprint GTM):** a message that mirrors a prospect's exact situation, shares an insight they have not connected yet, and asks a low-friction question. Zero product. The qualification happens inside the message, only people who actually have the pain reply.

### The 4 moves (this is the whole structure)

```
1. SITUATION, restate the signal as THEIR lived reality (factual, verifiable)
2. THE BITE, name the second-order problem they likely did NOT budget for / notice
3. THE WHY, the mechanism that makes the bite true (or makes it get worse)
4. CONFIRM, one low-friction question. Not a meeting. A yes/no or "does this resonate?"
```

That maps 1:1 onto Braun's 4T (Trigger → Think/poke → [Third-party proof, optional] → Talk). In a 2-email sequence, **proof (a type+size+outcome case, never named)** usually lives in email 2, not email 1, keep email 1 pure recognition.

### How each line is built from the signal

| Move | Question you answer | Where it comes from |
|---|---|---|
| **Situation** | "What is objectively true about them right now?" | the raw signal, restated in *their* words (not yours) |
| **The bite** | "What's the consequence of this that they probably haven't connected or budgeted?" | the second-order effect, the thing that's *downstream* of the signal |
| **The why** | "Why does that consequence happen / get worse?" | the mechanism (a how the system breaks, a timeline, a structural fact) |
| **Confirm** | "What can they answer in 5 words without commitment?" | a neutral, genuinely-answerable-either-way question |

### The bite is the skill

Anyone can restate a signal. The value is in **the bite**: the non-obvious second-order problem. Find it by asking: *"This happened. So what breaks next that they're not staring at?"*

- Signal: "moving to a new ERP while the old one still runs the core." Bite: "part of the integrations do not migrate, they get rebuilt, and that rebuild is rarely on the program's budget."
- Signal: "opened a second warehouse." Bite: "stock now lives in two places, and the first thing to break is the promise date on the webshop."
- Signal: "runs payment terminal X." Bite: "when a chargeback hits, does anyone still pull the evidence, or has the team quietly decided it is not worth it?"

### PQS rules (hard)

- **No product, no pitch, no feature list, no "we help…".** The message is 100% about them.
- **One idea per email.** Don't stack three bites.
- **Their words, not yours.** Mine review sites, call transcripts, job ads, their own site. "Would a customer say this over coffee?"
- **Crispy, not vague.** A specific number/timeframe/system beats an adjective. Specific = believable.
- **Confirm, don't persuade.** End on a neutral question. Give them room to say "no, you're off base." (Detachment.)
- **You-to-I ratio ≥ 3:1** (target 5:1). Count "you/your" vs "I/we/our." Below 3:1 → rewrite.

### PQS skeleton (fill, then cut)

```
Subject: {{first_name}}, [2-word topic, lowercase, looks like a colleague]

{{first_name}}, [SITUATION, one sentence, the signal as their reality].

[THE WHY, the mechanism, one sentence] [THE BITE, the unbudgeted second-order problem, one sentence].

[CONFIRM, low-friction question, answerable in 5 words, not a meeting].
```

---

## PVP: the anatomy

**Definition (after Blueprint GTM):** a message so specific and valuable the prospect would pay to receive it. The data is the message. It delivers business intelligence before anyone asked, independently useful whether they ever buy or not.

### The 7 rules: real PVP vs fake

A message is a PVP **only if** it is:
1. **Independently useful**: they gain value without replying.
2. **Related to your value prop**: the insight lives in the domain your product serves.
3. **Based on data they're not tracking**: public registries, filings, permits, pricing, payments, their own back-end if you have it.
4. **Interpreted, not dumped**: raw data isn't a PVP; the *insight* on top of it is.
5. **Beyond pain identification**: do not name the problem, **quantify the opportunity**.
6. **An information asymmetry**: you know something they don't.
7. **Concrete**: names, numbers, dates, locations. No directional claims ("utilization is probably low" fails; "crane 14 has had no transit permit on file since March" passes).

> If it fails rule 1 or 7, it is not a PVP. Downgrade to a PQS and stop pretending.

### The data architecture (where the asymmetry comes from)

A PVP is a **data cocktail**: 2 to 5 public sources stitched so the combination says something no single source does:

| Layer | Crawford term | What it is | Example |
|---|---|---|---|
| **Who** | Data Key | the source that makes the segment real + findable | NPPES physician registry, BuiltWith tech tag, SoS filings |
| **What's changing** | Leading indicator | a detectable signal the problem is **active now** | a new permit filed 0.5mi away, a CVE dropped, a price index +22% |
| **What already cost others** | Trailing indicator | proof the pain materialized for peers, with a $ amount | a regulator settlement, "nine operators your size were fined for this last year" |

**1 data key** = nameable segment. **2 keys** = Venn-diagram targeting. **3 keys woven** = the message nearly writes itself. One data point is forgettable; three woven together are compelling.

### Build process: FIND → PEA

**FIND (how you assemble the asymmetry):**
1. **Focus**: pick a micro-cohort (20 to 50 companies sharing one observable trait). The list IS the message. Tighter cohort → sharper insight.
2. **Investigate**: find the *existential data point* (the metric that flips you from nice-to-have to must-have) and stitch the 2 to 5 source cocktail.
3. **Narrate**: write the message in PEA shape (below).
4. **Deploy**: verify and send (out of scope here, but note: the insight must be *true for this specific prospect*, not the cohort average).

**PEA (the message shape):**
```
PREVIEW, the hook. ~120 chars, must work as a phone-notification subject. The specific fact.
ENGAGE, enough of the insight to prove you did real work: the names, numbers, dates, the interpretation.
ASK, low-friction: "want me to send the full analysis?"  NOT "book a 30-min demo."
```

### The message must PREDICT, not benchmark

Telling someone they score worse than their peers is not a sales message. Telling them what is about to happen to them, and what the ones who came out well did, is. (The predict-over-benchmark point is Crawford's.)

A benchmark describes; a PVP **predicts the buyer's future** using your data. The shape:

> "We have watched **N** [things like yours]. The **X** that [succeeded] all did [specific variable at a specific threshold]. The **Y** that [failed] were [outside that threshold]. You are about to [their move]. I do not know your numbers, but here is the spread. Want the [adjacent] version?"

Note the moves: a real count, a measurable threshold, "I do not know your numbers" to stay honest, and the buyer does the math against their own plan. No meeting ask.

### 4 delivery shapes (when a plain PVP feels too blunt)

| Shape | Mechanic | Why it works |
|---|---|---|
| **Praise for the past** | Turn a warning into praise for what they already left behind: "Good that you moved off [old approach]. Nine teams your size that stayed on it got hit by [consequence]." | No defense kicks in. The buyer is the hero of the sentence. |
| **Reply to their newsletter** | Subscribe to their company newsletter, then reply to an issue with a concrete rewrite. Add the decision-maker by hand. | The message is already in their inbox. The rewrite is the gift. |
| **Name three** | Name three of their actual customers and tell them one specific thing about each that they did not know. | One is a fluke, two a coincidence, three means you have data. |
| **Not sure whose this is** | "Not sure if this belongs to [name] or [name]. Noticed [specific thing]. Thought you should know. There is more if useful." | No ask, so nothing to push back on. |

These four shapes come from Jordan Crawford's work; the wording and examples here are ours.

### PVP rules (hard)

- **Quantify the opportunity, don't name the pain.** Captain-Obvious ("food costs are rising") is dead on arrival; "concrete is up 22% in your county in 45 days, here are three other suppliers" lands.
- **Every claim cites a specific number from data.** No directional language.
- **Still no product.** The product comes *after* they reply to the value.
- **The insight must be true for THIS prospect**, not the cohort. If you can only speak to the average, you have a PQS, not a PVP.

---

## The voice layer (Braun): applies to PQS and PVP both

The data is the *what*; Braun is the *how*. Run every draft through these:

- **Stop persuading.** Create a moment of reflection; let them conclude. Pushing triggers the Zone of Resistance.
- **Poke the bear with illumination questions.** Neutral, genuinely answerable either way, "how do you know X isn't happening between Y?" Never leading ("wouldn't you agree…").
- **The "without" formula.** (Desired result) *without* (the thing that sucks). Makes the benefit concrete.
- **Be crispy.** Put a movie in their head. Specific detail = believable (length-implies-strength).
- **Detach.** "No worries if I'm off base." You're the prize. Never needy, never urgent, never "just checking in."
- **End on a high note.** A genuine, specific compliment or a "thank you".
- **Cut fluff (3 passes).** Kill "I hope this finds you well," "I wanted to reach out," "just," "that," jargon. Wait a minute, cut again. Target ~40% shorter.
- **Write for one person** at their desk Tuesday morning with 47 unread emails.

**Length:** E1 70 to 90 words, E2 50 to 70, E3 40 to 60 (excl. signature/PS). Shorter than that lacks credibility; longer gets skipped.

**CTA:** binary, value-based, answerable in ≤5 words. *Never* a meeting request. "Worth exploring?" / "Want me to send it?" / "Is this of interest, or am I way off base?"

---

## QA: the gates every message must pass

Run all three gates plus the copy hard rules before shipping.

**1. The three-gate discipline (Crawford):**
- **Qualification gate**: is there a data-driven hard-disqualify that is NOT employee count? (If anyone could be on this list, the message will be generic.)
- **Quantification gate**: with perfect info, do I actually believe this prospect would 10× benefit? If not, I'm guessing.
- **Communication gate**: does the language make them feel *seen* and *helped*, so the power dynamic is "I'm trying to help you," not "please get on a call"?

**2. The permissionless-gift test (the load-bearing copy gate):**
> Could the recipient forward this to a peer in the same role, and the peer act on it **without any extra context**? Yes → gift (PVP). No → it's a pitch. (For PQS the softer version: would they think *"how did they know?"*)

**3. Empathy, not data-theater (Crawford):**
The common LLM failure is showing off the data work ("look how much I dug up"). That is theater. **Read the draft aloud to a real customer and listen for the no.** If it sounds like a research report, rewrite it as one human helping another.

**4. The 3-pass rule before you trust a draft:**
Pass 1 is confident, well-formatted, and often wrong. Pass 2: push back, what's the actual count, the threshold, the supporting number? Pass 3: bring a real customer into the room. Skip any pass and the message goes generic.

**5. Copy hard rules:**
- **No em dashes or en dashes** anywhere in outbound copy. They read as AI-written. Use periods or "without".
- **No banned words:** innovative, market leader, AI-powered, delve, leverage, robust, seamless, streamline, cutting-edge, unlock, elevate, empower.
- **No generic AI personalization** ("I saw you help companies do X"). Signal or data based only, or skip it.
- **Case studies:** describe type, size and outcome, and **never name the company** in PQS proof. The name-three PVP is the deliberate exception and uses their customers, not yours.
- **No P.S. as filler**, and no signature inside the body if the sender tool appends one.
- Every number must be traceable to a real source. No invented metrics, no invented cases.

**Self-score:** all three gates pass + permissionless-gift test passes + no hard-rule violation = ship. Any gate fails = revise. (For a scored check, run the `qa-checklist` skill in this repo.)

---

## Output format

When you produce a message, return it like this (and **save the copy to disk**: copy that lives only in chat gets lost):

```markdown
## [Prospect / cohort]: [PQS | PVP]: lane [A/B/C]

**Signal / data used:** [the raw input]
**Asymmetry:** [what you know that they don't expect you to]
**Data cocktail (PVP only):** [source 1 × source 2 × source 3 → the insight]
**The bite / existential data point:** [the second-order problem or quantified opportunity]

### Email 1
Subject: [...]

[body]

### Email 2 (optional, threaded: adds NEW value, never "just following up")
[body]

### Email 3 (optional, new thread: breakup / redirect)
[body]

**Variables:** {{first_name}}, {{company_name}}, [...]  (+ where each comes from)

### QA
- [ ] Lane honest (no fake PVP)
- [ ] 3 gates pass (qualification / quantification / communication)
- [ ] Permissionless-gift / "how did they know" test passes
- [ ] No product mention
- [ ] Crispy: every claim has a specific number/date/name
- [ ] You-to-I ≥ 3:1
- [ ] Word count in range
- [ ] No em dash, no banned words
- [ ] Numbers traceable, cases real
```

---

## The five anti-patterns that kill these messages

| Anti-pattern | Fix |
|---|---|
| Fake PVP, clever line + demo request | If it's not independently useful, write a PQS. |
| Naming the pain instead of quantifying the opportunity | "Concrete is up 22% in your county," not "costs are rising." |
| Data-theater, showing off the research | Empathy brain. Read it aloud to a real customer. |
| Mentioning the product in PQS/PVP | Delete it. The product comes after the reply. |
| Directional claims | Every claim cites a specific number from data, or it's cut. |

---

*This skill is message craft only. To build the segment first, use `pain-qualified-segment`, `list-is-the-message` or `permissionless-value-proposition` in this repo. For the full outbound setup (domains, lists, deliverability, sending), see [coldoutboundskills](https://github.com/growthenginenowoslawski/coldoutboundskills) by Growth Engine X.*

## Credits

PQS, PVP, the data cocktail, Data Key with leading and trailing indicators, the three gates and the delivery shapes are Jordan Crawford's concepts ([Blueprint GTM](https://blueprintgtm.com), the Cannonball newsletter, *On the Edge*). The voice layer (stop persuading, poke the bear, the "without" formula, detachment) is Josh Braun's ([joshbraun.com](https://joshbraun.com)). This skill is our own write-up of how we apply them. All example messages are invented.
