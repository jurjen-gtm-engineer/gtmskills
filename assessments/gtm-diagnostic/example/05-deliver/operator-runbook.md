# Operator Runbook: Sentinel Cloud Defense

**Week 5 deliverable** | What Maya (CRO), Carlos (VP Sales), Sarah (VP Marketing), and the RevOps team do, day by day.

> This runbook assumes the executive deck has been approved. Day 0 = the morning after exec sign-off.

---

## Day 0: Pre-launch

**Owner: Maya (CRO)**

- [ ] Forward the executive deck to Maya's direct reports
- [ ] Schedule the kickoff meeting with VP Sales + VP CS + RevOps lead + the diagnostic lead (Day 1)
- [ ] Send the all-hands note to the S&M team announcing the 90-day plan (template below)
- [ ] Calendar-block 30 min/week for 12 weeks on Maya's calendar for sprint check-ins

**All-hands note template:**
> Team: over the past 5 weeks we've completed a full GTM diagnostic. The key finding: our marketing is working, our AEs are working, our product is converting. The single biggest opportunity is one conversion step that loses 96% of our marketing-qualified leads.
>
> Starting Monday we're launching a 90-day plan to fix this. It does NOT mean hiring more SDRs (yet) or replacing anyone. It means rebuilding our sequence library, fixing our routing, and enforcing a "Dial First" policy that already exists on paper.
>
> Carlos and Sarah will walk through specifics with their teams this week. Expect a high-energy 30 days.

---

## Day 1 (Monday Week 1): Phase 1 Kickoff

**Owner: VP Sales (Carlos)**

Morning standup with the SDR team (30 min):
- [ ] Walk through "what the data shows": share the bowtie slide (Slide 3 of the exec deck)
- [ ] Reframe the problem: *"We're not failing as SDRs. The system is misaligned. Here's how we fix it."*
- [ ] Announce: the new default sequence drops Friday; Dial-First enforcement starts Monday Week 2

**RevOps (Aaron):**
- [ ] Begin building the "MQL Phone-First v1" sequence in the sales engagement platform
  - 5 touches over 7 days: D1 call+email, D2 call, D4 call+email, D6 email, D7 call+voicemail
- [ ] Begin the Phase 1 dashboard build (touch coverage by SDR, sequence assignment %)

**VP Sales:**
- [ ] Walk through the phased plan with SDR managers (1:1, 30 min each)
- [ ] Identify which SDR managers need extra coaching support

---

## Days 2-5 (Tue-Fri Week 1): Phase 1 Build

**RevOps:**
- [ ] Day 3: First draft of the v1 sequence ready for review
- [ ] Day 4: VP Sales + CRO approve the sequence
- [ ] Day 5: Sequence published. MQL routing logic switched to assign to v1 by default

**VP Sales:**
- [ ] Day 5: Re-route the 270 MQLs currently stuck in the "Working" queue (assign to v1)
- [ ] Day 5: Brief SDR managers on Week 2 Dial-First enforcement

**Sarah (VP Marketing):**
- [ ] Verify MQL scoring hasn't drifted in the last 30 days (control for a confounder)
- [ ] Begin building tier-segment routing logic (for Phase 2)

**Friday End-of-Week 1 checkpoint (15 min, Maya + VPs):**
- v1 sequence live
- Routing logic switched
- Backlog re-routed
- Activity dashboard 80% built

---

## Days 8-14 (Week 2): Dial-First Enforcement

**VP Sales, daily ritual (15 min each AM):**
- [ ] Pull yesterday's dial counts per SDR from the dashboard
- [ ] Share the leaderboard in the SDR team channel
- [ ] DM the bottom-3 SDRs with their numbers + offer help

**SDR Managers, weekly ritual (Wed afternoon, 30 min each):**
- [ ] Review each direct report's sequence mix
- [ ] Coach anyone <80% on the v1 sequence
- [ ] Surface tool/training blockers

**RevOps:**
- [ ] Day 10: Touch-coverage dashboard fully live
- [ ] Day 12: First weekly Phase 1 metrics report published

**CFO (Michelle):**
- [ ] Day 14: Approve the SDR comp adjustment (10% bonus on the touch-coverage SLA)
- [ ] Communicate to the SDR team by Day 15

**Friday End-of-Week 2 checkpoint:**
- Avg dials/SDR/day baseline = 11
- Target by Day 14 = 22
- Stretch target = 30 (benchmark)

---

## Days 15-28 (Weeks 3-4): Sustained Phase 1

**Daily ops continue:** dial leaderboard, sequence-mix monitoring, daily blockers surfaced

**Weekly Phase 1 metrics email (RevOps to all stakeholders):**
- Touch coverage by SDR
- Sequence-assignment % (target 95%+ on v1)
- Avg dials per day
- MQLs in the "Working" queue 30+ days (target <5%)

**Mid-Week 3, CRO 30-day milestone preview:**
- [ ] Pull preliminary CR2 numbers from in-flight data
- [ ] Identify any SDRs significantly below target: coaching plan
- [ ] Identify any SDRs significantly above target: share their approach

---

## Day 30: Phase 1 Milestone Review

**Owner: RevOps + the diagnostic team**

**Measurement (Day 30 morning):**
- [ ] Pull cohort metrics for the Days 1-30 MQLs
- [ ] Calculate observed CR2 (target: >=12%)
- [ ] Touch coverage, sequence mix, dial counts, all by SDR

**Review meeting (Day 30 PM, 60 min):**
- Attendees: Maya, Carlos, Sarah, Aaron (RevOps), the diagnostic lead
- Agenda:
  - 10 min: data review
  - 20 min: what's working / what's not
  - 20 min: Phase 2 launch readiness
  - 10 min: decisions

**Decision tree:**
- If CR2 >= 12%: proceed to Phase 2
- If 8% <= CR2 < 12%: diagnose blockers, narrow the Phase 2 scope
- If CR2 < 8%: re-diagnose with the diagnostic team; do not launch Phase 2 yet

---

## Days 31-60: Phase 2

**Owner: VP Sales + VP CS (Linda)**

### Sales side
- [ ] Day 31: Begin tier-by-segment sequence builds (SMB / MM / MM+ variants)
- [ ] Days 32-45: SDR discovery training (external trainer, 2hr/wk for 6 weeks)
- [ ] Day 50: v2 sequences live, A/B-tested against v1

### Customer Success side
- [ ] Day 31: Build the adoption-milestone template for the AE-to-CSM handoff
- [ ] Day 35: New handoff template live for all new wins
- [ ] Day 40: CSM 7-day SLA in effect (down from the 45-day default)
- [ ] Day 45: Detection-tuning service for SMB onboarding launched

### Hiring
- [ ] Day 40: Begin sourcing for the Phase 3 expansion-role hire (lead time 30+ days)

**Day 60 milestone review:**
- Target: CR2 >= 18% AND CR5 >= 70%
- Same decision tree as Day 30

---

## Days 61-90: Phase 3

**Owner: CRO + the new expansion role**

- [ ] Day 65: Expansion role filled (offer accepted by Day 75)
- [ ] Day 70: Expansion playbook drafted (expansion triggers, offers, cadence)
- [ ] Day 75: Compensation plan for the expansion role approved
- [ ] Day 80: Segment the existing-customer base for expansion readiness (CSM team)
- [ ] Day 85: Quarterly expansion campaign launched to the Tier-1 base
- [ ] Day 90: Full diagnostic re-measurement: all CRs, forecast re-run

**Day 90 milestone review:**
- Re-run the diagnostic
- Re-forecast P50 ARR vs target
- Decide: Phase 4 launch OR re-diagnose

---

## Weekly cadence (sustained through 90 days)

| Day | Time | Meeting | Attendees |
|---|---|---|---|
| Monday | 9:00 AM | SDR team standup | Carlos + SDRs |
| Monday | 10:00 AM | Phase metrics review | Carlos + Aaron + diagnostic team |
| Wednesday | 2:00 PM | SDR manager 1:1s | Carlos + each SDR manager |
| Thursday | 3:00 PM | Cross-functional sprint check-in | Maya + VPs + Aaron + diagnostic team |
| Friday | 4:00 PM | Weekly metrics email | Aaron to all stakeholders |

---

## What to do when something breaks

| Symptom | First diagnostic question | Action |
|---|---|---|
| Touch coverage falls below 80% | Is it 1 SDR or all SDRs? | If 1: coaching call. If all: manager review. |
| Dial count plateau | Is it morale or capacity? | Survey SDRs anonymously. If capacity: Phase 2 hire conversation. |
| CR2 lifting slower than expected | Are the SDRs reaching the right contacts? | Review call recordings; upgrade the Quality factor |
| Sequence mix slipping (<95% on v1) | Is the routing logic working? | RevOps audit; check the MQL routing handoff |
| AEs complaining about lead quality | Is CR3 dropping? | Look at AE-accept rate by SDR. If CR3 holds: quality is fine, AEs are responding to the volume increase. |

---

## What success looks like at handover (Day 90)

- CR2 >= 18% (sustained 30+ days)
- CR5 >= 70%
- ARR run-rate trending toward 54M+ P50
- All Phase 1+2 changes operationalized (not dependent on the diagnostic team's involvement)
- Phase 3 expansion role producing first deals
- Maya can defend the entire plan to her board without notes

---

## Handover artifacts (diagnostic team to Sentinel ops team)

At Day 90:
- All working files in this folder (versioned)
- Operator runbook (this file): owned by Carlos
- Phase 1 dashboard: owned by Aaron
- Phase 2 sequences: owned by Carlos (with Aaron tooling support)
- Expansion playbook: owned by the new expansion role
- Forecast model: re-run quarterly by Aaron, with diagnostic-team support if needed

An optional Phase 4 engagement (annual operating plan + monthly probability re-forecast) is scoped separately.
