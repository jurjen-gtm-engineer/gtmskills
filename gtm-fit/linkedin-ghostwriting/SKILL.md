---
name: linkedin-ghostwriting
description: Draft ranked LinkedIn post options for a founder or executive, grounded in fresh signal and gated against repetition. Use when someone asks "what should our CEO/founder post", "next posts for [exec]", "draft exec thought leadership", "a repost/reshare", or "an industry-news take" for a named executive. Produces 3 ranked, typed options per exec, each 6 lines or fewer, each with an attachment.
---

# Executive LinkedIn Content Engine

A repeatable engine for founder- and executive-led LinkedIn content. It exists to solve the two failure modes of exec ghostwriting: posts that repeat what the exec already said, and posts that read like marketing ad-copy instead of the person. One pass, no dead drops. Output: **3 ranked options per exec, each 6 lines or fewer, each with an attachment.** Deliver to the exec (or their reviewer) to approve and post by hand. This engine never posts externally.

## Required inputs (gather before drafting)

1. **A voice card per exec** - their real diction, the arguments they own, what they will never say, 1-2 gold-standard past posts. Build this from their actual posting history, not a persona guess.
2. **A post ledger** - every post that has gone out, with its hook, its core argument, its attachment, and any performance note. This is what the anti-repeat gate diffs against.
3. **A fresh signal feed** - this week's news, competitor moves, earnings, regulatory shifts, and reshare candidates on the exec's beat. Verify the date at the primary source, not the commentary's date. A one-day-old article about an undated event is not a one-day-old event.
4. **A repost-sources list** - accounts and publications the exec plausibly follows, for the reshare slot.

## Hard format gates (fail = fix before delivering)

1. **6 lines or fewer per post.** Draft tight from the first pass.
2. **Every post has an attachment:** a reshare, a shared article/news link, or a graphic. For a graphic, recommend single image vs carousel and say why, and deliver a ready-to-paste image-generation prompt (palette by hex, exact minimal headline text, aspect ratio, and a no-logos / no-fake-data / spell-text-exactly constraint). Keep any AI-generated image logo-free and overlay the real logo afterward.
3. **3 ranked options per exec, one of each type,** each with a one-line "why" and a post order:
   - (1) an article / industry-news share plus comment
   - (2) a reshare (a company-page post from the last week, or a relevant industry post)
   - (3) thought leadership plus a graphic recommendation
4. **Voice + hygiene:** an anchor test (does the first line earn the scroll-stop), no em dashes, no banned words, no emoji, close on a genuine question, no self-plug or self-congratulation.

## The steps

**1. Read the history first.** Before anything, read the ledger and the last few live posts: what argument, what attachment, what landed. This feeds the anti-repeat gate and keeps the cadence honest.

**2. Mine the signal, then decide.** Read the full research corpus, not just any pre-suggested angles. The strategist generates the angles from everything; a researcher's one-line routing is one more raw signal, never the plan. Respect verification caveats before an exec states anything as fact.

**3. Anti-repeat gate.** Diff every candidate angle against the ledger and the exec's off-limits list. Kill or re-angle anything on the off-limits list, in the same argument family as a recent post, or inside an 8-week same-argument cooldown. Also diff against options the exec already rejected - a deleted draft is a rejection, never re-serve it. A near-miss goes up as a flagged judgment call, never as a clean recommendation.

**4. Angle select and format lock.** Pick the 3 types per exec, assign the attachment per slot, recommend image vs carousel for the graphic, and rank. If the same event fits two execs, it can appear on both - never the same take, never the same week.

**5. Messenger / lane fit (hard check on shares and reshares).** The exec must plausibly follow that source and their audience must care about it - not just "is the argument sound". Route the peg to the exec whose lane it is (regulatory to the policy voice, product/build to the builder, numbers/valuation to the finance voice). A finance exec commenting on a niche UX article is a stretch even when the angle is real.

**6. Draft in voice, then two finishing passes.** Draft each option 6 lines or fewer against the voice card and closest real samples. Then run: (a) the `anti-slop` skill to strip AI tells, and (b) the `human-mannerisms` skill to add at least one real human move (a mid-sentence aside, an undercut, an oddly-specific real detail) calibrated to the exec's voice. One or two moves, never invented detail.

**7. Tone gate.** Read each draft against the voice card: does it sound like this exec, not generic industry copy, and will it get read (fold, scannability, no wall of text). Explicitly flag marketer / ad-copy lines and deadline / urgency-pitch closers, not just AI slop. A clean-but-flat post with zero human moves is a fail, not a pass.

**8. QA gate.** Independent scan: em-dash, banned words, emoji, anchor test, no-plug, line count, attachment present, and clean-room (no internal names, tool paths, pricing floors, or unnamed-client leaks in the post).

**9. Score and rank.** Score each on a hook rubric and on commercial value (audience precision, proof / defensibility, narrative fit, why-now). Below bar gets one revision, then rank the three.

**10. Deliver as ranked options.** 3 typed options per exec, each with its attachment and (for the graphic) an image/carousel recommendation. Keep every dependency, recency caveat, and posting-sequence note in the delivery notes, not on the post itself.

**11. Close the loop.** After the exec picks, edits, or posts: append the chosen post to the ledger (hook, angle, attachment, their edits verbatim, outcome). If they rewrote it, that rewrite is the new gold line - update the voice card. Add the angle to the off-limits map. Post-publication performance feeds the next run's scoring.

## Never

Post or reshare externally on the exec's behalf. Name a client without clearance. Leak internal or pricing intel into a post. Ship a bare text post with no attachment. Exceed the line limit. Re-run an off-limits angle.

---

*Author: Gali (Kidoz Inc.). Contributed under the MIT License. Requires the `anti-slop` and `human-mannerisms` skills for the finishing passes.*
