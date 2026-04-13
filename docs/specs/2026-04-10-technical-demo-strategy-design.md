# Technical Demo Strategy — Yaohong's Airtime Allocation

**Workshop:** Claude Code for B2B Marketing & Sales (Tiket)
**Date:** 20 April 2026
**Role:** Technical co-lecturer (Yaohong), paired with Tina on facilitation/narrative

---

## Context

- 25 participants: B2B Sales, TDD/Content, Marketing — non-technical
- Audience has used Claude Cowork for 3 weeks — enthusiastic, not skeptical
- End-to-end pipeline demos land hardest with this audience
- Yaohong owns all live technical demos; Tina leads framing and facilitation

---

## Core Principle: Two Moments, Not Six

Instead of spreading demos across every block, concentrate technical airtime into **two high-impact demo moments**. Everything else is support mode (walk around, troubleshoot, unblock).

Why:
- Two moments they'll remember, not four they'll blur together
- Leaves more breathing room for hands-on time (where non-technical people actually learn)
- Reduces demo failure surface area
- Keeps Yaohong fresh and focused for the moments that matter

---

## Demo 1: The Hook

| | |
|---|---|
| **When** | Block 1 — Opening (first 20 min) |
| **Duration** | ~3 minutes |
| **What** | Call Tiket's internal hotel API from Claude Code → display real data they recognize |
| **Why this works** | Cowork cannot do this — it can only talk to pre-approved connectors. Pulling *their own data* from a system they use daily creates the "wait, it can talk to *our* systems?" reaction. This is the strongest proof that Code unlocks something Cowork cannot. |
| **Setup required** | Internal API access or mock endpoint with real-looking Tiket data. Must be confirmed with Tiket before workshop. |

**What it replaces:** The original Block 1 plan had a competitor research demo — but Cowork can already browse the web and do research. A competitor brief isn't a real differentiator for people who've been using Cowork for 3 weeks.

---

## Demo 2: The Hero — Build-Up Pipeline

| | |
|---|---|
| **When** | Block 3 — Core Concepts (30 min block) |
| **Duration** | ~15 minutes |
| **What** | Start from the same hotel API call (callback to Demo 1), then layer complexity live until it becomes a full pipeline |
| **Why this works** | They see *how* pipelines get built, not just the end result. Demystifies the process. Each layer is a natural "aha" moment. If something breaks mid-way, the earlier layers still demonstrated value. |

### The Layers

Build each layer live, pausing briefly between each to let it land:

| Layer | What Happens | Audience Reaction |
|---|---|---|
| **Layer 1: Raw API call** | "Remember this from earlier? Let's start here." Pull hotel partner data from the internal API. | Familiar — they saw this in Block 1 |
| **Layer 2: Enrich with context** | Add email context or web research about the partner. Combine two data sources. | "Oh, it can pull from multiple places" |
| **Layer 3: Analyze** | Ask Claude to identify trends, flag issues, or rank partners by a metric. | "It's not just fetching — it's thinking" |
| **Layer 4: Format and save** | Generate a formatted report (Markdown or HTML), save to file. | "That's a ready-to-share deliverable" |
| **Layer 5 (stretch): Reusable skill** | Wrap the whole pipeline into a `/partner-report` skill. Run it with one command. | "Anyone on the team can run this" |

### Connection Between Demo 1 and Demo 2

This is intentional. Demo 1 plants the seed ("Code can talk to our API"). Demo 2 calls back to it ("remember that API call? Now watch what happens when we chain it"). The audience experiences a narrative arc, not two disconnected demos.

---

## All Other Blocks: Support Mode

| Block | Yaohong's Role |
|---|---|
| **Block 2** — Terminal Comfort (20 min) | Walk around, help people who get stuck. No prepared demo. |
| **Block 4** — MCPs & Skills (20 min) | Available for technical questions. Tina leads concept explanation. |
| **Break** (15 min) | Prep breakout materials, test API connectivity |
| **Block 5** — Guided Build (45 min) | Float between breakout groups, unblock technical issues. Be the "rescue" when someone's stuck. |
| **Block 6** — Show & Tell (30 min) | Answer "can it do X?" questions live. Quick improvised demos if time allows. |

---

## Dependencies / Still Needed

| Item | Status | Owner |
|---|---|---|
| Tiket internal API access or mock endpoint | Needed from Tiket | Yaohong to follow up |
| Sample API response with real-looking hotel partner data | To prepare | Yaohong |
| Build-Up Pipeline tested end-to-end before workshop | To do | Yaohong |
| `/partner-report` skill template (Layer 5) | To build | Yaohong |
| Fallback plan if API is unavailable day-of | To design | Yaohong |

---

## Fallback Plan

If the internal API is unavailable on workshop day:
- Use a **local mock API** (simple Python/Node server returning realistic Tiket hotel data)
- Demo 1 still works — the audience sees Claude Code calling an API endpoint
- Demo 2 pipeline layers still work — the data just comes from localhost instead of production
- Prepare this in advance so the switch is seamless

---

## Success Criteria

After Yaohong's two demo moments, participants should:
1. Understand that Claude Code can connect to systems Cowork cannot (Demo 1)
2. See how simple steps chain into powerful pipelines (Demo 2)
3. Believe they could eventually build something similar (build-up approach demystifies it)
4. Be excited to try it themselves in the breakout session (Block 5)
