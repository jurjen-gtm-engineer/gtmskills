---
name: anti-ai-slop-writing
description: Strip AI tells from any GTM prose and hold a real human voice. Use whenever writing, editing, rewriting, or polishing copy - LinkedIn posts, ad copy, cold emails, articles, thought leadership, case studies, decks - and when someone says "make this less AI", "sound less robotic", "remove the AI tells", or "de-AI this". Runs a two-pass self-check before any prose is returned.
---

# Anti-Slop

A two-pass editing standard that removes the patterns marking text as machine-written. It gets copy to zero: nothing in the piece screams AI. Pair it with a human-texture pass (see the `human-mannerisms` skill) to get copy above zero, because flawless-but-flat is itself a tell.

Apply this to any prose before it ships. Two passes, both mandatory:

1. **Pass one, Tier A.** Scan for zero-exception rhetorical moves. Any hit is rewritten, not softened.
2. **Pass two, Tier B.** Scan for clustering of vocabulary, structural, and formatting tics.

---

## Tier A: zero instances (rewrite every hit)

### Negative parallelism: "It's not X, it's Y"
The single most recognisable AI tell. The rule is semantic, not syntactic: do not assert what something IS by first asserting what it ISN'T about the same subject. Every shape is the same violation:

- "It's not X, it's Y." / "Not X, but Y." / "Not just X, Y." / "Not X. Y."
- "Don't just X, Y." / "We don't just X, we Y."
- Tense variants: "X was never A, it's B."
- Sense-verb variants: "It feels like A, it's actually B." / "On the surface it's A, underneath it's B."
- Self-correcting: "It's less X, more Y." / "I'm not saying X, I'm saying Y."
- Expectation-vs-reality: "You'd expect X. You get Y."

**The test:** remove the negated half. If the point still stands, the negation was scaffolding. Cut it and state the positive claim directly. If the point collapses, the positive claim wasn't sharp enough - fix the claim, don't prop it with a contrast.

**Allowed (do not flag):** different-subject contrast ("Big clients don't buy software, they buy the safest choice") and genuine state-shifts where the subject actually moved from A to B ("After the diagnosis you stopped asking is this serious, you started asking what do I do now").

### Swap framing
No "Say goodbye to X, say hello to Y" or "Out with the old, in with the new". State what changed.

### Triple countdown
No "Not a bug. Not a feature. A fundamental flaw." State the point.

### Self-posed rhetorical questions answered in the same beat
No "The result? Devastating." / "What does this mean? Everything."

### False suspense transitions
The whole class is banned, not just set phrases: "Here's the thing", "Here's the kicker", "Here's what changed", "Here's what nobody tells you". Test: does the phrase NAME the revelation in the same beat, or just tease that one is coming? If it teases, cut it.

### The colon setup
No repeating "abstract noun, colon, payoff" ("The reality:", "The problem:", "The takeaway:"). One at most per piece. Also the mid-sentence version - a setup clause, a colon, then the payoff - reads as machine cadence. State the fact plainly.

### Pedagogical framing
No teacher voice: "Let's unpack", "Let's dive in", "Let's break this down".

### Vague authority
No "research shows", "experts say", "studies suggest", "industry reports indicate". Name the person, study, or source, or cut the claim.

### Invented specificity and invented concept labels
No fabricated numbers, dates, percentages, or named moments not grounded in the source. No coining abstract compound phrases ("the acceleration trap", "the supervision paradox") and using them as if they were established terms.

### Patronising analogy
No "Think of it like...", "It's like...", "Imagine if...". Even one forced analogy is too many; the temptation peaks on counter-intuitive ideas, which is exactly when to resist. Name the thing directly.

### Grandiose stakes inflation
No "This will fundamentally reshape everything" / "will define the next era". Match the register to the subject.

### Phantom-future projection
No manufactured stakes from an imagined future: "A year from now you'll wish you'd...", "By the time you realise it, you'll have wasted...". Stakes come from a present cost the reader is already paying.

### Unsolicited validation and forced empathy
No "You're not imagining it", "You're not alone", "Feeling overwhelmed is normal". Open on the concrete thing instead.

### The "actually / genuinely" intensifier
No "a strategy that actually works", "AI that genuinely understands your brand". It adds an unearned contrast and no information. Delete the word; if the sentence means the same, leave it deleted.

### "That lands" and delivery-verb tics
No "a hook that lands", "copy that resonates", "the point settles". Name the specific effect ("a hook that makes them stop scrolling") or cut the qualifier.

### Metaphorical verbs where a literal one is clearer
"collapses" to "stops working", "siphoning attention" to "stealing attention", "dovetails into" to "connects to".

### Formulaic openers
No "In today's fast-paced world", "In an age where", "At its core", "Welcome to", "Enter [X]". No LinkedIn humblebrag openers ("I'm humbled to share", "Thrilled to announce"): state the news itself. No faux-personal-ritual openers ("One number I keep coming back to").

### Formulaic closers
No "In conclusion", "Ultimately", "At the end of the day", "To sum up".

---

## Tier B: avoid clustering (a single instance can pass)

- **Grandiose nouns:** tapestry, landscape, realm, ecosystem, paradigm, synergy, journey, testament, cornerstone, beacon, nexus, frontier, fabric.
- **Inflated adjectives:** robust, pivotal, crucial, vital, compelling, comprehensive, meticulous, innovative, transformative, seamless, dynamic, multifaceted, cutting-edge, unparalleled, nuanced, profound.
- **Magic adverbs:** quietly, deeply, fundamentally, remarkably, arguably, notably, seamlessly, effortlessly.
- **Pompous verbs:** delve, unpack, navigate, harness, leverage, utilize, foster, cultivate, embark, revolutionize, elevate, empower, unlock, streamline, spearhead, showcase, underscore, resonate, amplify, curate.
- **The "serves as" family:** use "is" instead of serves as, stands as, represents, embodies, functions as, emerges as.
- **Tricolon overuse:** max one rule-of-three per section; never stack three.
- **Decorative lists:** three-comma scene-painting where each item is a coat of paint on the same idea. Allowed only when items are concrete, distinct, and the rhythm is conversational.
- **Anaphora abuse:** no same sentence opener 3+ times in a row ("You've tried X. You've tried Y. You've tried Z.").
- **Structural uniformity:** vary sentence and paragraph length; three similar-length sentences in a row hum like a machine.
- **Formatting tics:** em-dash addiction (2-3 per piece, max), bold-first bullets everywhere, decorative unicode arrows, emoji sprinkling, rocket-emoji openers, green-check bullet rows, heavy markdown in flowing prose.

---

## House rules to tune per brand

Every team should add its own hard rejects. A starter set worth adopting:

- **No em dashes** in shipped prose (use hyphens, commas, colons, periods). This one rule kills a huge share of AI-flagged copy.
- **A banned-word list:** transformative, game-changing, revolutionary, seamless, robust, best-in-class, industry-leading, cutting-edge, "excited to announce", "don't hesitate". Add your own.
- **No sales-pitch pivot.** Do not end a thought-leadership post by circling back to how early you were or how the market is "catching up" to you. The value is the idea, not the plug. Many posts should not mention your product at all.

---

## The two-line final read

1. **The pub test:** would two colleagues say this line to each other over lunch? If no, the fix is always to name the specific thing the filler is gesturing at.
2. **The ship test:** would the author send or post this without feeling they have to de-AI it first? If no, revise.

---

*Author: Gali (Kidoz Inc.). Contributed under the MIT License. Tune the banned-word and house-rules sections to your own brand voice.*
