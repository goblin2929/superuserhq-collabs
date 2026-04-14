# Skills Guide — Design Spec

| | |
|---|---|
| **Deliverable** | `clients/tiket/docs/skills-guide.html` |
| **Purpose** | Hands-on workshop companion for Block 3 (Skills & Team Sharing, 30 min) |
| **Audience** | 25 non-technical tiket staff (B2B sales, content, marketing) who've used Cowork 3 weeks but never used skills |
| **Design** | Match `workshop-guide.html` design system (cream/terracotta, Source Serif + DM Sans + JetBrains Mono, scroll fade-in) |

---

## Approach

**Build-first, explain-as-you-go (Approach C):** Start with the finished skill running, then reverse-engineer it step by step. Non-technical learners absorb better when they've seen the result before writing YAML.

## Cowork Skills Treatment

**Option B — one-line pivot.** A callout box at the top:

> "Cowork has skills too (ZIP uploads in Settings, per-person). We're building in Code because skills live in your shared repo — build once, everyone gets it."

No side-by-side comparison. No further Cowork mention.

## Skill Being Built

**Sales Proposal Generator** (`/sales-proposal`) — a working 15-25 line SKILL.md that generates a structured sales proposal given a client name and context.

## Page Structure

### Top Banner + Nav
- Same dual-color banner (Novastacks AI / Superuser HQ) as workshop-guide.html
- Sticky nav with 4 section anchors: See It, Build It, Make It Yours, Share It

### Hero
- Badge: "Block 3 — Hands-On"
- Title: "Building Your First Skill"
- Subtitle: "Sales Proposal Generator"
- Meta: Tiket.com Team / April 2026 / 30 min exercise

### Cowork Pivot Callout
- Terracotta callout box immediately below hero
- One-sentence pivot (see above)

### Section 1 — See It In Action
- **Terminal mockup** (dark card, JetBrains Mono): shows someone typing `/sales-proposal Marriott Indonesia` and pressing enter
- **Output block** (white card): shows the structured proposal output — client overview, proposed solution, pricing structure, next steps
- **Caption:** "This is what you'll build in the next 20 minutes."

### Section 2 — Build It
Three sub-steps using the step component (numbered circles with connector lines):

**Step 1: Create the file**
- Code block: `mkdir -p .claude/skills/sales-proposal`
- Brief explanation: "Skills live in `.claude/skills/`. Each skill gets its own folder with a `SKILL.md` file."

**Step 2: Write the frontmatter**
- Code block showing the 3-line YAML header (`name`, `description`)
- Side annotations (not a wall of text) explaining each field:
  - `name` — what you type after `/`
  - `description` — tells Claude when to suggest this skill

**Step 3: Write the skill content**
- Code block showing the full skill body (~15-20 lines of markdown instructions)
- Content covers: role Claude should take, sections to include in the proposal (client overview, proposed solution, pricing, next steps), tone guidelines
- After the code block: "Save the file. That's it — your skill is ready."

**Step 4: Run it**
- Code block: `claude` then `/sales-proposal Marriott Indonesia`
- Brief "try it now" prompt

### Section 3 — Make It Yours
- A compact list or small grid of things to customize:
  - Company name / product lines
  - Proposal sections (add/remove)
  - Tone adjectives
  - Output format preferences
- Framed as "swap these lines" with before/after code highlights (using `panel-warm` / `panel-cool` comparison panels)

### Section 4 — Share It
- Three commands in a code block: `git add`, `git commit`, `git push`
- Then: teammate runs `git pull`, types `/sales-proposal` — same result
- **Governance callout** (terracotta banner): "One repo. One version. 25 people. No ZIP files."

### Footer
- Same dark footer as workshop-guide.html
- "Novastacks AI x Superuser HQ — April 2026"

## Visual Components Used

All from workshop-guide.html design system:

| Component | Usage |
|---|---|
| `.top-banner` | Dual-color header |
| `.nav` / `.nav-inner` | Sticky section navigation |
| `.hero` / `.hero-badge` | Page header |
| `.terra-banner` | Cowork pivot callout + governance callout |
| `.card-dark` + `.code-block` | Terminal mockups |
| `.card` | Output display |
| `.step` / `.step-num` / `.step-line` | Build steps |
| `.code-block` + `.prompt` + `.comment` | Code snippets |
| `.compare-panels` / `.panel-warm` / `.panel-cool` | Before/after customization |
| `footer` | Page footer |
| `.fade-in` | Scroll animations |

## What's NOT Included

- No deep Cowork vs Code comparison (handled in Block 1 / separate doc)
- No MCP server content (out of scope for Block 3)
- No agent workflows (covered in Block 2)
- No breakout exercise content (that's Block 4, separate briefs)

## Success Criteria

1. Facilitator can say "open the skills guide and scroll to Step 2" and everyone's in sync
2. Participant can follow along and have a working `/sales-proposal` skill by end of Block 3
3. Page is self-contained — no external dependencies beyond Google Fonts and logo images
