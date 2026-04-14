# Skills Guide Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build `clients/tiket/docs/skills-guide.html` — a hands-on workshop companion for Block 3 that walks participants through building a `/sales-proposal` skill.

**Architecture:** Single self-contained HTML file matching the `workshop-guide.html` design system. No build tools, no external JS. CSS variables + Google Fonts + inline scroll animation script.

**Tech Stack:** HTML, CSS (design system from workshop-guide.html), vanilla JS (IntersectionObserver for fade-in)

**Spec:** `docs/specs/2026-04-14-skills-guide-design.md`

**Design reference:** `clients/tiket/docs/workshop-guide.html` — copy the full CSS design system from this file (`:root` variables, all component classes, responsive breakpoints). Do NOT recreate or subset the CSS.

---

### Task 1: Scaffold — HTML boilerplate, CSS, top banner, nav, hero, Cowork callout

**Files:**
- Create: `clients/tiket/docs/skills-guide.html`

**Design reference:** Read `clients/tiket/docs/workshop-guide.html` lines 1–608 for the complete CSS design system. Copy it in full — same `:root` variables, same component classes, same responsive breakpoints.

- [ ] **Step 1: Create the HTML file with full design system**

Create `clients/tiket/docs/skills-guide.html` with:
- DOCTYPE, charset, viewport meta
- Google Fonts link (same as workshop-guide: Source Serif 4, Lora, DM Sans, JetBrains Mono)
- Full CSS from workshop-guide.html (all `:root` variables, all component classes, responsive rules)
- Top banner (Novastacks AI left / Superuser HQ right) — same markup as workshop-guide.html
- Sticky nav with 4 anchors: `See It`, `Build It`, `Make It Yours`, `Share It`

- [ ] **Step 2: Add the hero section**

```html
<div class="hero fade-in">
  <div class="hero-logos">
    <img src="novastacks-logo-color.png" alt="Novastacks AI">
    <span class="x">&times;</span>
    <svg width="28" height="28" viewBox="0 0 28 28" fill="none">
      <rect width="28" height="28" rx="6" fill="#2C2520"/>
      <text x="5" y="20" fill="white" font-family="DM Sans" font-size="14" font-weight="700">SH</text>
    </svg>
  </div>
  <div class="hero-badge">Block 3 &mdash; Hands-On</div>
  <h1>Building Your First Skill</h1>
  <p class="hero-sub">Sales Proposal Generator &mdash; from zero to a working <code style="font-family:'JetBrains Mono',monospace; background:var(--terra-light-bg); padding:2px 8px; border-radius:4px; font-size:15px; color:var(--terra);">/sales-proposal</code> command.</p>
  <div class="hero-meta">
    <span><span class="dot"></span>Tiket.com Team</span>
    <span><span class="dot"></span>April 2026</span>
    <span><span class="dot"></span>30 min exercise</span>
  </div>
</div>
```

- [ ] **Step 3: Add the Cowork pivot callout**

Immediately below the hero, add a terracotta banner:

```html
<div class="container">
  <div class="terra-banner fade-in">
    Cowork has skills too &mdash; ZIP uploads in Settings, per-person.
    <div class="sub">We're building in Code because skills live in your shared repo. Build once, everyone gets it.</div>
  </div>
</div>
```

- [ ] **Step 4: Verify in browser**

Run: `open clients/tiket/docs/skills-guide.html`

Expected: Cream background, dual-color top banner, sticky nav with 4 items, hero with badge/title/subtitle/meta, terracotta Cowork callout below. Logos load from same directory. Responsive on mobile.

- [ ] **Step 5: Commit**

```bash
git add clients/tiket/docs/skills-guide.html
git commit -m "feat: scaffold skills guide with design system, hero, and nav"
```

---

### Task 2: Section 1 — See It In Action

**Files:**
- Modify: `clients/tiket/docs/skills-guide.html`

- [ ] **Step 1: Add the "See It In Action" section**

Add a `<section id="see-it">` after the Cowork callout. Contains:

**Section header** using standard component:
```html
<div class="sec-num">01 &mdash; See It</div>
<h2 class="sec-title">See It In Action</h2>
<p class="sec-desc">Before we build anything, here's what the finished skill looks like when you run it.</p>
```

**Terminal mockup** — a `.card-dark` containing a `.code-block` that shows the user invoking the skill:
```
$ claude
> /sales-proposal Marriott Indonesia

Generating sales proposal for Marriott Indonesia...
```

**Output card** — a `.card` below the terminal showing the proposal output Claude would generate. Structure it with clear headings:

1. **Client Overview** — "Marriott Indonesia operates 35+ properties across Jakarta, Bali, and Surabaya. Key opportunity: streamlining their OTA channel distribution to increase direct-to-platform bookings."
2. **Proposed Solution** — "Tiket.com Premium Partner Program: dedicated account management, real-time inventory sync via API, priority placement in search results, co-branded marketing campaigns during peak travel seasons."
3. **Pricing Structure** — A small table with three tiers (Starter/Growth/Enterprise) and features.
4. **Next Steps** — "1. Schedule technical integration call (Week 1). 2. Pilot program with 3 Jakarta properties (Weeks 2-4). 3. Performance review and full rollout decision (Week 6)."

**Caption** below the output card:
```html
<div class="terra-banner fade-in">
  This is what you'll build in the next 20 minutes.
</div>
```

Use `.fade-in` class on each block for scroll animation.

- [ ] **Step 2: Style the output card**

The output card should use the `.card` class with internal structure. Format the proposal sections using:
- `<h4>` with `font-family: 'Source Serif 4'` for section headings (Client Overview, Proposed Solution, etc.)
- `<p>` with `card-desc` class for body text
- A small inline table for pricing tiers using the existing table styles but compact
- Use a thin left border in terracotta (`border-left: 3px solid var(--terra)`) to visually group each proposal section

- [ ] **Step 3: Verify in browser**

Run: `open clients/tiket/docs/skills-guide.html`

Expected: Dark terminal mockup showing `/sales-proposal Marriott Indonesia`, followed by a white card with the formatted proposal output (4 sections), followed by the "20 minutes" callout. All fade-in on scroll.

- [ ] **Step 4: Commit**

```bash
git add clients/tiket/docs/skills-guide.html
git commit -m "feat: add See It In Action section with terminal mockup and sample output"
```

---

### Task 3: Section 2 — Build It

**Files:**
- Modify: `clients/tiket/docs/skills-guide.html`

- [ ] **Step 1: Add the "Build It" section header**

Add a `<section id="build-it">` with standard section header:
```html
<div class="sec-num">02 &mdash; Build It</div>
<h2 class="sec-title">Build It</h2>
<p class="sec-desc">Four steps. Follow along in your terminal.</p>
```

- [ ] **Step 2: Add Step 1 — Create the file**

Use the `.steps` / `.step` / `.step-num` / `.step-line` / `.step-content` component pattern from workshop-guide.html:

```html
<div class="steps fade-in">
  <div class="step">
    <div class="step-left">
      <div class="step-num">1</div>
      <div class="step-line"></div>
    </div>
    <div class="step-content">
      <h4>Create the skill folder</h4>
      <p>Skills live in <code>.claude/skills/</code>. Each skill gets its own folder with a <code>SKILL.md</code> file inside.</p>
      <div class="code-block"><span class="prompt">$</span> mkdir -p .claude/skills/sales-proposal</div>
    </div>
  </div>
  <!-- Steps 2-4 follow same pattern -->
</div>
```

- [ ] **Step 3: Add Step 2 — Write the frontmatter**

Second `.step` in the steps container. Content:

```html
<h4>Write the frontmatter</h4>
<p>Open <code>.claude/skills/sales-proposal/SKILL.md</code> in any text editor. Start with the header:</p>
<div class="code-block"><span class="comment"># Copy this exactly into SKILL.md</span>
---
name: sales-proposal
description: Use when creating a sales proposal for a potential hotel or travel partner
---</div>
```

Add two annotation items below the code block (use a `.grid-2` with small `.card` elements):

- **`name`** — "What you type after `/` to run this skill. Keep it lowercase with hyphens."
- **`description`** — "Tells Claude when to suggest this skill automatically. Start with 'Use when...'"

- [ ] **Step 4: Add Step 3 — Write the skill content**

Third `.step`. This is the main content block — the actual skill body participants type out.

The skill content (add below the frontmatter in the same SKILL.md):

```markdown
# Sales Proposal Generator

You are a B2B sales specialist at tiket.com. Generate a professional sales proposal for the given client.

The user will provide: client name and any known context about the prospect.

## Proposal Sections

### 1. Client Overview
- Brief summary of the client's business and market position
- Key challenges or opportunities you'll address

### 2. Proposed Solution
- How tiket.com's platform solves their needs
- Specific features and integrations relevant to them
- Expected outcomes with concrete metrics

### 3. Pricing Structure
- Present three tiers: Starter, Growth, Enterprise
- List what's included at each level

### 4. Next Steps
- Proposed timeline with weekly milestones
- Key contacts and immediate action items

## Tone
Professional but warm. Data-driven. Focus on ROI and partnership value. Use specifics — not vague promises.
```

Display this in a `.code-block`. After the block, add: "Save the file. That's your entire skill."

- [ ] **Step 5: Add Step 4 — Run it**

Fourth `.step` (final — no `.step-line` after the number):

```html
<h4>Run it</h4>
<p>Open Claude Code and try your new skill:</p>
<div class="code-block"><span class="prompt">$</span> claude
<span class="prompt">&gt;</span> /sales-proposal Marriott Indonesia</div>
<p style="margin-top:12px;">Claude reads your SKILL.md, follows your instructions, and generates a structured proposal. Try it now.</p>
```

- [ ] **Step 6: Verify in browser**

Run: `open clients/tiket/docs/skills-guide.html`

Expected: Four numbered steps with terracotta circles and connector lines. Each step has a heading, description, and code block. The skill content code block shows the full 20-line SKILL.md. Frontmatter annotations appear in a 2-column grid.

- [ ] **Step 7: Commit**

```bash
git add clients/tiket/docs/skills-guide.html
git commit -m "feat: add Build It section with 4-step skill creation walkthrough"
```

---

### Task 4: Section 3 — Make It Yours

**Files:**
- Modify: `clients/tiket/docs/skills-guide.html`

- [ ] **Step 1: Add the "Make It Yours" section**

Add a `<section id="make-it-yours">` with standard header:
```html
<div class="sec-num">03 &mdash; Customize</div>
<h2 class="sec-title">Make It Yours</h2>
<p class="sec-desc">The skill works as-is, but you can customize it for your team's specific needs. Here are the lines to change.</p>
```

- [ ] **Step 2: Add before/after comparison panels**

Use the `.compare-panels` / `.panel-warm` / `.panel-cool` component pattern for 2-3 customization examples:

**Example 1 — Company context:**
- Panel warm (before): `You are a B2B sales specialist at tiket.com.`
- Panel cool (after): `You are a B2B sales specialist at tiket.com, focused on hotel partnerships in Southeast Asia. Our key differentiator is real-time inventory sync and 45M+ monthly active users.`

**Example 2 — Proposal sections:**
- Panel warm (before): Three tiers — Starter, Growth, Enterprise
- Panel cool (after): Custom tiers — Partnership Pilot, Standard Partner, Strategic Alliance

**Example 3 — Tone:**
- Panel warm (before): `Professional but warm. Data-driven.`
- Panel cool (after): `Confident and consultative. Lead with market data and case studies. Mirror the client's formality level.`

Label the warm panel "Default" and the cool panel "Customized" using `<h4>` inside each panel.

- [ ] **Step 3: Verify in browser**

Run: `open clients/tiket/docs/skills-guide.html`

Expected: Three side-by-side comparison panels showing before/after customization options. Warm (terracotta-tinted) on left, cool (blue-gray) on right. Responsive — stacks on mobile.

- [ ] **Step 4: Commit**

```bash
git add clients/tiket/docs/skills-guide.html
git commit -m "feat: add Make It Yours section with customization examples"
```

---

### Task 5: Section 4 — Share It, Footer, and Scroll Animation

**Files:**
- Modify: `clients/tiket/docs/skills-guide.html`

- [ ] **Step 1: Add the "Share It" section**

Add a `<section id="share-it">` with standard header:
```html
<div class="sec-num">04 &mdash; Team</div>
<h2 class="sec-title">Share It</h2>
<p class="sec-desc">Your skill works locally. Three commands to share it with everyone.</p>
```

Add a code block with the git commands:
```html
<div class="code-block fade-in"><span class="prompt">$</span> git add .claude/skills/sales-proposal/SKILL.md
<span class="prompt">$</span> git commit -m "add sales-proposal skill"
<span class="prompt">$</span> git push</div>
```

Below it, add a description block explaining what happens on the other end:
```html
<div class="card fade-in" style="margin-top:24px;">
  <h4>Your teammate's side</h4>
  <div class="code-block" style="margin-top:12px;"><span class="prompt">$</span> git pull
<span class="prompt">$</span> claude
<span class="prompt">&gt;</span> /sales-proposal Hyatt Regency Bali</div>
  <p class="card-desc" style="margin-top:12px;">Same skill. Same output structure. Same quality. No ZIP files, no manual uploads, no "did you get the latest version?" conversations.</p>
</div>
```

Add the governance callout:
```html
<div class="terra-banner fade-in" style="margin-top:32px;">
  One repo. One version. 25 people. No ZIP files.
  <div class="sub">Update the skill once &mdash; everyone gets the new version on their next <code style="color:rgba(255,255,255,0.9); font-family:'JetBrains Mono',monospace;">git pull</code>.</div>
</div>
```

- [ ] **Step 2: Add the footer**

```html
<footer>
  <strong>Novastacks AI &times; Superuser HQ</strong>
  <div class="footer-sub">Skills Guide &mdash; April 2026</div>
</footer>
```

- [ ] **Step 3: Add the scroll animation script**

Add before `</body>` — same IntersectionObserver pattern as workshop-guide.html:

```html
<script>
document.addEventListener('DOMContentLoaded', () => {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); });
  }, { threshold: 0.1 });
  document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));
});
</script>
```

- [ ] **Step 4: Add active nav highlighting script**

Add nav scroll-tracking (same as workshop-guide.html) so the active section highlights in the sticky nav:

```html
<script>
document.addEventListener('DOMContentLoaded', () => {
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav a');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        navLinks.forEach(link => link.classList.remove('active'));
        const active = document.querySelector('.nav a[href="#' + entry.target.id + '"]');
        if (active) active.classList.add('active');
      }
    });
  }, { threshold: 0.3 });
  sections.forEach(s => observer.observe(s));
});
</script>
```

- [ ] **Step 5: Final verification in browser**

Run: `open clients/tiket/docs/skills-guide.html`

Full page check:
- Top banner renders with dual colors
- Sticky nav shows 4 items, highlights on scroll
- Hero has badge, title, subtitle, meta
- Cowork callout appears below hero
- Section 1: terminal mockup + proposal output card + "20 minutes" callout
- Section 2: 4 numbered steps with code blocks, frontmatter annotations in grid
- Section 3: 3 before/after comparison panels
- Section 4: git commands + teammate card + governance banner
- Footer renders dark
- All `.fade-in` elements animate on scroll
- Mobile responsive (stack grids, adjust padding)

- [ ] **Step 6: Commit**

```bash
git add clients/tiket/docs/skills-guide.html
git commit -m "feat: add Share It section, footer, and scroll animations"
```
