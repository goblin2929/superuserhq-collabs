# Claude Code Intermediate Workshop — 2-Hour Speaking Notes

**Title:** Claude Code Intermediate: Beyond Cowork
**Audience:** 25 non-technical Tiket staff (B2B Sales, TDD/Content, Marketing) — 3 weeks Cowork experience, built workflows, NOT Claude 101
**Speakers:** Tina (narrative/facilitation) + Yaohong (technical demos)
**Date:** April 20, 2026 — Jakarta
**Duration:** 120 min

---

## Quick Reference: Sources Integrated

- [thisweb.dev/.claude folder structure](https://thisweb.dev/post/claude-code-structure) — 8 building blocks, folder anatomy
- [cc.lifehacker.tw](https://cc.lifehacker.tw/) — Raymond's 3-tier framework, non-engineer focus, batch use cases
- [Raymond: Desktop vs Terminal](https://raymondhouch.com/lifehacker/digital-workflow/claude-code-desktop-vs-terminal/) — 3 interfaces, portability, "AI handles code, you handle content"
- [YouTube: Raymond's beginner tutorial](https://youtu.be/xo7dE80ktu4) — zero-to-agent for non-engineers
- LinkedIn posts: Anthropic's Managed Agents, enterprise agent architecture

---

## TIMING OVERVIEW

| Block | Duration | Topic | Format |
|-------|----------|-------|--------|
| 0 | 5 min | Welcome + Why You're Here | Talk |
| 1 | 15 min | Three Tiers + The Evolution | Talk + visual |
| 2 | 15 min | The Eight Building Blocks | Talk + code samples |
| 3 | 15 min | The .claude/ Folder — Your Team's OS | Talk + demo |
| — | 10 min | BREAK | |
| 4 | 15 min | Yaohong Demo 1: Live API Call | Demo |
| 5 | 20 min | Yaohong Demo 2: Build-Up Pipeline | Demo |
| 6 | 10 min | Human + Agent Coordination (Git) | Talk |
| 7 | 10 min | ROI: Proving It Works to Leadership | Talk |
| 8 | 5 min | Wrap + What's Next | Talk |
| **Total** | **120 min** | | |

---

## BLOCK 0 — Welcome + Why You're Here (5 min)

### TALKING HIGHLIGHT
> "You've used Cowork for 3 weeks. You can chat with Claude, build projects, run skills. Today we go beyond that — not to make you engineers, but to give you the vocabulary and mental model engineers have been using for 20 years. By the end, you'll be able to design workflows that an entire team can run, with safety rails, without asking IT for permission."

### Key points to hit
- You're NOT beginners anymore — acknowledge their 3 weeks
- This is NOT a tool tour or sales pitch
- What you'll walk out with: **vocabulary** (the 8 primitives), **mental model** (where things live and why), **templates** (steal-ready examples), **coordination muscle** (how to work alongside agents)
- "If you can use Notion, you can learn everything we'll cover today"

### Metaphor
> "Think of Cowork as WhatsApp — great for 1-on-1 conversations, but try running a 25-person operation through it. Claude Code is Slack — channels, permissions, bots, shared workspace. Same brain behind both, different operating system."

---

## BLOCK 1 — Three Tiers + The Evolution (15 min)

### TALKING HIGHLIGHT
> "There are three ways to use Claude. You're on the second floor. Today we're showing you the third floor exists — and what you can see from up there."

### Three Tiers (source: Raymond)
**Level 1 — Claude.ai (Web)**
- Q&A, translation, writing, file analysis
- "You ask questions. Claude answers."
- 🗣️ "This is where everyone starts. It's Google that understands context."

**Level 2 — Cowork (Desktop)**
- Projects, skills, local file read/write, connectors
- "You give Claude a workspace. It does things for you."
- 🗣️ "This is where you are now. You've built projects, uploaded skills. It's powerful."
- **But**: each person configures separately, no shared standards, no safety rails, no version control

**Level 3 — Claude Code (Terminal/Desktop)**
- Git-based shared workspace, hooks, rules, permissions, agents, commands
- "You build a system. Claude operates inside it. The whole team shares the same rules."
- 🗣️ "This is what we cover today. It's not harder — it's more structured."

### The Key Insight (source: Raymond)
> "You are the commander. The AI is the executor."

Cowork blurs this — it feels like a conversation. Claude Code makes the relationship explicit: you write the instructions, Claude follows them, and the system enforces the boundaries.

### Why Non-Engineers Should Care
- "If you've ever said 'did everyone get the latest version?' — that's the problem Claude Code solves."
- "If you've ever worried 'what if the AI sends the wrong thing to a client?' — that's what permissions solve."
- "If you've ever wished Cowork could just run something at 6am without you waking up — that's what hooks and agents solve."

### Transition Metaphor
> "Cowork is a great notebook. Claude Code is a shared filing cabinet with locks, labels, and a receptionist who follows your rules even when you're not in the office."

---

## BLOCK 2 — The Eight Building Blocks (15 min) %% i think this need to be 30 mins and explain more elaboratively for exmaple hook - how to use hook, put a placeholder for real-life example. explanation wise this site explain so much better than current speaker note.  also u can suggest a few tina's workflow for hook and edxplain why. or use current skill with hook to demontrate%%

### TALKING HIGHLIGHT
> "Cowork gives you two primitives: Instructions and Skills. Claude Code gives you eight. Those extra six aren't 'advanced features' — they're what makes a system enterprise-safe."

### The Eight Primitives — teach in pairs

**Pair 1: What Claude knows (always-loaded context)**
| Primitive | What it is | Metaphor |
|-----------|-----------|----------|
| **CLAUDE.md** | Project brief — always loaded | "Employee handbook everyone gets on day 1" |
| **MEMORY.md** | Persistent notes across sessions | "A journal — Claude remembers so you don't repeat yourself" |

🗣️ "In Cowork, each person writes their own Custom Instructions. In Code, there's ONE CLAUDE.md the whole team can share — most people share via git. Update it once, everyone gets it."

**Pair 2: What Claude can do (reusable procedures)**
| Primitive | What it is | Metaphor |
|-----------|-----------|----------|
| **Skills** | Work manuals — multi-step procedures | "A recipe in your cookbook — step-by-step" |
| **Commands** | One-liner shortcuts to trigger workflows | "A keyboard shortcut — one keystroke, one action" |

🗣️ "Commands are for speed. Skills are for depth. `/partner-report Marriott` is a command that triggers a skill that runs 5 steps."

**Pair 3: Who does what (delegation)**
| Primitive | What it is | Metaphor |
|-----------|-----------|----------|
| **Agents** | Specialist sub-workers with own role + tools + model | "A consultant you call in for a specific job" |
| **Rules** (with paths:) | Domain guardrails that load only when relevant files are touched | "Context-aware seatbelts — only click in when needed" |

🗣️ "Agents are the biggest unlock for teams. Instead of one AI doing everything, you build specialists: a researcher, a writer, an editor, a QA checker. Each has its own personality, its own tools, its own cost tier."

**Pair 4: What keeps it safe (enforcement)**
| Primitive | What it is | Metaphor |
|-----------|-----------|----------|
| **Hooks** | Event-triggered scripts that run OUTSIDE Claude | "A tripwire — invisible until it catches something" |
| **settings.json** (permissions) | Allow/deny lists for what Claude can do | "A keycard system — different access for different roles" |

🗣️ "Hooks are the only place that GUARANTEES execution. You can write 'always lint before committing' in CLAUDE.md — Claude will forget. Put it in a hook — the system runs it every time, because your shell runs it, not the model."

### The Primitive Coverage Table
Show side-by-side: Cowork has 2 primitives. Code has 8. The extra 6 = enterprise-safe.

🗣️ "This isn't about features. It's about answering the question every VP will ask: 'How do we let marketing use AI agents without giving them nuclear launch codes?' The answer is these six."

---

## BLOCK 3 — The .claude/ Folder — Your Team's OS (15 min)

### TALKING HIGHLIGHT
> "Everything we just covered lives in one folder. Committed to git. Shared across the team. That folder IS your team's AI operating system."

### Show the folder tree %% make note to check if we have real example from either Yaohong or Tina's directory. (I think we should have a block for trainer prep placeholder- what to do - so we can use that to note what Tina or Yaohon need to add or do next) %%
```
.claude/
├── CLAUDE.md              # project brief
├── settings.json          # permissions + hooks
├── agents/                # specialist sub-agents
│   ├── feedback-editor.md
│   └── partner-researcher.md
├── commands/              # slash-commands
│   └── partner-report.md
├── hooks/                 # event-triggered scripts
│   └── lint-check.sh
├── rules/                 # domain guardrails (lazy-loaded)
│   ├── blog-voice.md
│   └── outreach-tone.md
└── skills/                # reusable procedures
    └── sales-proposal/
        └── SKILL.md
```

### Key distinctions to explain %% so what's best practice - need to explain better what should be claude.md existing and screenshot Tina set up %%

| This...   | is NOT this... | Because...                                                                               |
| --------- | -------------- | ---------------------------------------------------------------------------------------- |
| CLAUDE.md | Rules          | CLAUDE.md loads every conversation. Rules only load when matching files are touched.     |
| Skills    | Commands       | Skills are manuals. Commands are shortcuts.                                              |
| Hooks     | Rules          | Hooks are enforced by your shell. Rules are guidance loaded into Claude's context.       |
| Agents    | Skills         | Agents are specialists you delegate TO. Skills are procedures you tell Claude to follow. |

### The Layering System
```
~/.claude/            ← personal (your defaults)
    ↓ inherits
./.claude/            ← project (shared via git)
    ↓ inherits
settings.local.json   ← personal overrides (gitignored)
```

🗣️ "Three layers. Personal defaults at the top. Shared project rules in the middle. Your local overrides at the bottom. The VP writes the company CLAUDE.md. The team lead writes the project CLAUDE.md. You write your personal settings. Everyone stays aligned."

### The Portability Argument (source: Raymond)
> "CLAUDE.md and Skills are plain text files. If a stronger AI emerges tomorrow, you connect these files to the new brain — zero data loss. Your team's operating system isn't locked to any vendor."

🗣️ "This is the argument for your VP: we're not building on quicksand. Everything we create is a text file in a git repo. Worst case, Claude disappears tomorrow and we plug the same files into whatever comes next."

---

## ☕ BREAK (10 min)

---

## BLOCK 4 — Yaohong Demo 1: Live API Call (15 min)

### TALKING HIGHLIGHT (Tina frames it)
> "Everything you've seen in Cowork — the chat, the skills, the projects — all of that runs on Anthropic's servers, talking to Anthropic's connectors. The next thing Yaohong is going to show you is Claude talking to YOUR system. Tiket's internal data. In real time."

### Demo: Call Tiket's internal hotel API from Claude Code
- Show Claude Code terminal
- Run: call the hotel partner API → display real data they recognize
- The reaction: "Wait, it can talk to OUR systems?"

🗣️ Yaohong: "This is the moment. Cowork can browse the web, but it can't call your internal APIs. Code can. This is the bridge between 'AI that helps me write' and 'AI that helps me operate.'"

### After demo — Tina explains WHY this matters
- MCP = the USB port analogy
- "You can plug in Google Sheets, Gmail, HubSpot, Notion, Slack, and your own internal APIs"
- "Cowork has pre-approved connectors. Code has an open protocol."

---

## BLOCK 5 — Yaohong Demo 2: Build-Up Pipeline (20 min)

### TALKING HIGHLIGHT (Tina frames it)
> "That API call Yaohong just did? That was one step. Now watch what happens when we chain steps together."

### The Five Layers (build each live)
| Layer | What happens | Audience reaction |
|-------|-------------|-------------------|
| 1. Raw API call | "Remember this? Let's start here." | Familiar callback |
| 2. Enrich with context | Add web research about the partner | "Oh, it pulls from multiple places" |
| 3. Analyze | Ask Claude to rank, flag issues, find trends | "It's not just fetching — it's thinking" |
| 4. Format and save | Generate a formatted report, save to file | "That's a ready-to-share deliverable" |
| 5. Wrap into a skill | `/partner-report` — one command, whole pipeline | "Anyone on the team can run this" |

### After demo — Tina explains the design pattern
🗣️ "What you just saw is the pattern. Every agentic workflow is the same shape: fetch → enrich → analyze → format → save. The only things that change are the data sources and the output format. Once you see the pattern, you can build your own."

### Connection between Demo 1 and Demo 2
🗣️ "Demo 1 planted the seed: 'Code can talk to our API.' Demo 2 grew it: 'And here's what happens when you chain that into a pipeline.' The narrative arc is intentional. One data point becomes a system."

---

## BLOCK 6 — Human + Agent Coordination (10 min)

### TALKING HIGHLIGHT
> "The tool that makes all of this work for a team isn't Claude. It's git. And git is the new Notion."

### The Reframe
- Engineers have used git for 20 years to coordinate with each other
- The same tools work for coordinating with agents
- "Notion = last write wins. Git = every change is tracked, every version recoverable, conflicts are surfaced."

### Five Moves (the only git they need)
| Command | Translation |
|---------|------------|
| `git pull` | Hit refresh before you start |
| `git status` | What did I change? |
| `git add + commit` | Save with a note |
| `git push` | Share with the team |
| `git log` | What happened, by whom, when |

🗣️ "That's it. Five commands. You learned Notion. You learned ClickUp. Git is smaller than both — it just looks intimidating because engineers hoard it."

### Main Branch Discipline
> "The main branch is the version of truth. Nothing broken, nothing half-finished lives on main."

🗣️ "Without this discipline, you wake up to find the 'published' version is whatever an agent did at 3am. With it, the agent works on a branch, you review, YOU decide when it lands on main."

### Worktrees (the power move)
🗣️ "This is the trick most engineers don't even know: worktrees. You can have yourself working in one folder and an agent working in another — same project, different branches, zero interference. Like having two desks."

---

## BLOCK 7 — ROI: Proving It Works to Leadership (10 min)

### TALKING HIGHLIGHT
> "Everything we covered today is useless if you can't walk into a leadership meeting and prove it's working. The number one reason AI projects die isn't that the AI didn't work — it's that nobody could prove it did."

### The Discipline
1. **Baseline before you build** — 5 questions: what task, how often, who does it, how long, what quality?
2. **Target you commit to** — "80 hrs/week → 12 hrs/week, rework ≤ 5%"
3. **Outcome you measure** — real numbers, not vibes

### The One-Page Report Template
- **Headline** (one sentence a VP can act on)
- **KPI tiles** (before/after, percent change)
- **What changed** (3 bullets max)
- **What it unlocked** (the follow-on wins — this is where savings become growth)
- **The ask** (always end on an ask)

### The Translation Rule
🗣️ "Never say 'we built a skill with frontmatter and hooks.' Say 'we automated partner reports and saved Rina 3 days a week.' The VP doesn't want to hear how the engine works. The VP wants to know how fast the car is going."

| Don't say | Do say |
|-----------|--------|
| "We built a Claude Code skill" | "We automated the weekly partner report" |
| "We're using sub-agents" | "Different AI specialists handle research, writing, QA — we can scale without hiring" |
| "We implemented a PreToolUse hook" | "We added a safety check that prevents destructive changes without human approval" |

---

## BLOCK 8 — Wrap + What's Next (5 min)

### TALKING HIGHLIGHT
> "You walked in knowing how to chat with Claude. You're walking out knowing how to build a system around it. The difference is the difference between having a contractor and having a team."

### Recap in 60 seconds
1. Three tiers: Web → Cowork → Code. You just leveled up.
2. Eight building blocks, not two. That's what makes it enterprise-safe.
3. One folder (`.claude/`) = your team's AI operating system. Text files. In git. Portable.
4. Agents are specialists. Skills are procedures. Hooks are enforcement. Permissions are the safety envelope.
5. Git is how you coordinate. Main branch = truth. Branches = work. Merge = your decision.
6. Prove ROI with baselines, not vibes. Numbers a VP can act on.

### What to do this week
- [ ] Run `git pull` in your team's repo
- [ ] Open the `.claude/` folder and read CLAUDE.md
- [ ] Try running one existing skill: `/sales-proposal [client name]`
- [ ] Write a 90-minute baseline for one task you want to automate
- [ ] Come back next session with that baseline — we'll build the skill together

### Final line
> "The best time to start was 3 weeks ago, and you did — with Cowork. The next best time is now. Same brain, bigger operating system."

---

## YAOHONG'S SECTION — Human/Agent Coordination Personal Sharing

**[PLACEHOLDER — Yaohong to fill in]**

### Suggested structure
Based on historical Slack conversations, Yaohong talks about:

**How I actually use agents day-to-day**
- Pull 2–3 representative Slack moments
- What was the task? Which agent? What did the hand-off look like?

**What's worked well (pros)**
- Concrete win #1 (e.g., a pipeline that saved hours)
- Concrete win #2 (e.g., a skill that became reusable across projects)
- Concrete win #3 (e.g., an unexpected use case)

**What's been painful (cons)**
- Honest friction #1 (e.g., context loss between sessions)
- Honest friction #2 (e.g., over-trusting an output)
- Honest friction #3 (e.g., tool/auth/setup pain)

**My recommendation for this room**
- Given the audience (B2B Sales, TDD/Content, Marketing) — what's the ONE habit to adopt this week?
- And the ONE trap to avoid?

---

## APPENDIX: Reference Materials

### Source: Raymond (cc.lifehacker.tw)
- Three-tier framework: Web → Cowork → Code
- "You are the commander, AI is the executor"
- Time investment: "Basic operation 1-2 days; complete AI Agent workflow about 1-2 weeks"
- Safety architecture: "Trash bin + dangerous command blacklist + permission modes"
- Target audience: "Solopreneurs, personal brands, solo operators wanting to build AI systems"

### Source: Raymond (Desktop vs Terminal)
- Three interfaces, one brain (Desktop, Terminal, VS Code)
- "I ignored 90% of the code display" — switching to terminal + Obsidian
- Portability argument: "CLAUDE.md and Skills are portable assets — if stronger AI emerges, connect to new brain, zero data loss"
- Recommendation: beginners → desktop; advanced → terminal; hybrid for most

### Source: thisweb.dev (.claude folder structure)
- Full .claude/ folder anatomy with all 8 primitives
- Hooks event types: PreToolUse, PostToolUse, SubagentStart/Stop, FileChanged, Stop
- Rules with `paths:` frontmatter — lazy-loading pattern
- settings.json: personal global vs project shared vs local override
- Permissions: allow/deny lists
- Agents: custom frontmatter with name, description, tools, model
- Skills: SKILL.md with auto-discovery
- Commands: slash-invoked, argument-hint, $ARGUMENTS variable

### Source: User direction
- "Git is the new Notion/ClickUp/Trello for non-tech workers"
- Human/agent coordination via worktrees, main branch
- OpenClaw as deployment option 3 (self-hosted 24/7)
- Agentic tools ecosystem cheatsheet
- AI Impact Report template — ROI, not technology
- Agents deep dive: built-in vs custom vs managed (cloud)
- Three trigger methods: auto, direct specify, @mention

---

## COMPANION DELIVERABLES

| Deliverable | File | Status |
|-------------|------|--------|
| Main workshop guide (HTML) | workshop-guide.html | Draft |
| Skills hands-on guide (HTML) | skills-guide.html | Draft |
| Cowork vs Code comparison (HTML) | cowork-vs-code-comparison.html | Draft |
| Git for Non-Engineers (HTML) | git-for-non-engineers.html | Draft |
| OpenClaw primer (HTML) | openclaw.html | Draft |
| Agentic tools cheatsheet (HTML) | agentic-tools-cheatsheet.html | Draft |
| AI Impact Report template (HTML) | ai-impact-report.html | Draft |
| Demo strategy (Yaohong) | docs/specs/2026-04-10-technical-demo-strategy-design.md | Draft |
| Speaking notes (this file) | workshop-speaking-notes.md | Draft |
