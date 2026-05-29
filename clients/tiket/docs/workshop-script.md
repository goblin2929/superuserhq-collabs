# Claude Code Intermediate: Beyond Cowork
## Full Workshop Script — Gamma Slide Deck + Speaker Notes

**Audience:** 25 non-technical Tiket staff (B2B Sales, TDD/Content, Marketing) — 3 weeks Cowork experience
**Speakers:** Tina (lead) + Yaohong (demos)
**Duration:** 120 min + break | **Date:** May 29, 2026 — Jakarta

---

# SECTION 0 — WHY WE'RE HERE (15 min)

---

## SLIDE 1: Title

**VISUAL:** Full-bleed title slide
- "Claude Code Intermediate: Beyond Cowork"
- Novastacks AI × Superuser HQ logos
- Tiket.com Team — May 2026 — Jakarta

**SPEAK (Tina, 1 min):**
> Welcome. Quick show of hands — who's used Cowork every day this past week? [pause for hands] Great. Who's built at least one skill? [pause] Good. You're not beginners. You've been using Claude for 3 weeks and you've built things that work.
>
> So today is NOT Claude 101. Today is about what comes after Cowork — how to go from using Claude as a personal assistant to building systems that run your operations. You've learned how to talk to Claude. Now we're going to learn how to architect around it.

---

## SLIDE 2: The Role Has Changed

**VISUAL:** Side-by-side JD comparison: "Campaign Manager 2024" vs "GTM Engineer / Gen Marketer 2026"

**The JD comparison:**

| | Old JD (Campaign Manager, 2024) | New JD (GTM Engineer / Gen Marketer, 2026) |
|---|---|---|
| **Primary job** | Execute campaigns | Design systems that execute campaigns |
| **Content** | Write the blog, manage the calendar | Build the skill that writes, schedules, optimizes |
| **Data** | Pull reports, build dashboards | Curate insights from agent-generated analysis |
| **Tools** | Master Canva, HubSpot, GA | Orchestrate agents that USE Canva, HubSpot, GA |
| **Collaboration** | 5-10 human stakeholders per project | You + your agents do more, fewer human dependencies |
| **Salary signal** | $60-90K | $125-250K+ (GTM Engineer at Ramp, Notion, Anthropic) |

**The skill shift:**

| Campaign Manager (2024) | GTM Engineer (2026) |
|---|---|
| 1. Manual content production | 1. Agent harness design |
| 2. Tool-specific expertise (HubSpot, GA, Canva,) | 2. Workflow architecture |
| 3. Cross-dept coordination | 3. Human-agent coordination |
| 4. Analytics & reporting | 4. Quality system design |
| 5. Project management | 5. Deterministic vs probabilistic thinking |
| 6. Campaign setup & execution | 6. Data pipeline thinking |
| 7. Single-channel mastery | 7. Strategic insight curation |
| **In common:** Campaign strategy, execution, performance review |

**SPEAK (Tina, 3 min):**
> Before we get into the tools — the job description has changed. Left column: campaign manager JD in 2024. Right column: what companies like Notion, Anthropic, Ramp, and Toast are hiring for right now — they call it "GTM Engineer" or "Gen Marketer."
>
> The old job was execution. The new job is orchestration — design the system, then supervise it.
>
> Clay coined "GTM Engineer" in 2023. By January 2026, 3,000+ open roles on LinkedIn. Emily Kramer, ex-VP Marketing at Asana, says: **"With tools, you are the operator. With agents, you are the manager."**
>
> That's why you're here. Not to learn a tool. To learn the skill set.

---

## SLIDE 3: What This Is / What This Isn't

**VISUAL:** Two columns
- Left: "THIS IS" (green) — Vocabulary. Mental model. Real examples. Coordination skills.
- Right: "THIS IS NOT" (red) — Beginner course. Engineering class. Tool tour. Sales pitch.

**SPEAK (Tina, 1 min):**
> This IS about giving you the vocabulary and mental model. By the end, you'll say things like "that should be a hook, not a rule" or "let's put that in an agent with haiku" — and your team will understand.
>
> This is NOT about making you engineers. You won't write code. You WILL learn how to design workflows.

---

## SLIDE 4: AI Automation vs AI Augmentation

**VISUAL:** Two columns with architecture infographic:

| | AI Automation (n8n, Zapier) | AI Augmentation (Claude) |
|---|---|---|
| **What it does** | Follows rules: "if this, then that" | Thinks, reasons, writes, analyzes |
| **Strengths** | Reliable, predictable, runs 24/7 | Creative, adaptive, handles ambiguity |
| **Weaknesses** | Can't think, can't adapt, can't write | Can drift, can fabricate, needs guardrails |
| **Example** | "New lead → send Slack notification" | "Analyze this partner's decline and draft a re-engagement plan" |
| **You learned this in** | Your n8n workshop | Your Cowork training |

**Infographic:** Side-by-side architecture — same task ("Pull partner data, analyze decline, send email"):
- n8n: 6-8 nodes wired together + Airtable to view results (setup: 2-4 hours)
- Claude Code: one prompt + MCP tools, result in terminal (setup: 5 minutes)

**SPEAK (Tina, 3 min):**
> You've had two AI workshops. One on n8n, one on Cowork. They're fundamentally different things.
>
> **n8n is AI automation.** "If this happens, do that." Reliable. Predictable. But can't think.
>
> **Claude is AI augmentation.** It thinks alongside you — co-thinking, co-working, co-creating. It can analyze, write, adapt.
>
> They're not competing. They're complementary. n8n handles the predictable parts. Claude handles the parts that need judgment. Today we're learning how to combine both.

---

## SLIDE 5: Four Ways to Use Claude — Same Brain, Different Harness

**VISUAL:** Four cards in a row:

| | Claude.ai | Cowork | Claude Code | Console |
|---|---|---|---|---|
| **Metaphor** | Google that understands you | Your personal assistant | Your team's operating system | The control tower |
| **Interface** | Web browser | Desktop app | Terminal / IDE | Web dashboard |
| **What Claude can do** | Answer, write, analyze | Read files, run skills, browse, do tasks | Use tools, follow rules, run agents, remember | Run autonomously for hours/days in the cloud |
| **Runs on** | Anthropic's servers | Your computer (sandboxed VM) | Your computer (full access) | Anthropic's cloud |
| **Best for** | Quick tasks | Daily knowledge work (80%) | Reusable systems for teams | Long-running / overnight jobs |

**Your Cowork capabilities (you already have these):**
- **Local file access** — no 20-file/30MB limits. Reads directly from your computer.
- **Skills** — reusable workflows you trigger with one click.
- **Memory** — claude.md, memory.md. The more you teach it, the better it gets.
- **Connectors** — Gmail, Google Drive, Notion, Calendar.
- **Scheduled tasks** — set a workflow to run daily.

**Your immediate next step — do this today or tomorrow:**

1. **Do the work manually** with Cowork. Go back and forth.
2. **Give feedback.** "Too dense. Lead with metrics. Keep it under 300 words."
3. **Tell Cowork to remember.** It saves corrections to memory.md.
4. **Tell Cowork: "reverse-engineer this into a skill."**
5. **Install the skill.** One click. Now it's repeatable.
6. **Schedule it.** Daily or weekly.

That's Cowork at its maximum. Skills from experience, not templates.

**But here's where you'll hit the ceiling:**
- Skills can't enforce rules — Claude might still ignore them on the 30th run
- Memory drifts on long conversations (context rot)
- Connectors are pre-built — can't connect your internal booking API
- Scheduled tasks are single-person — no team sharing or version control
- No quality gates — bad output at 6am gets sent without validation

**Claude Code** adds the enterprise layer: enforcement (hooks), specialization (agents), version control (git), team coordination, and open protocol connections (MCP).

**Console** (platform.claude.com) is the builder's dashboard — where Managed Agents are configured and monitored. Your engineering team uses it to deploy agents that serve your team at scale.

**SPEAK (Tina, 5 min):**
> [Walk through the 4 interfaces. Spend most time on Cowork capabilities (they know this) → ceiling (why it's not enough) → Code as the answer → Console as awareness.]

---

# SECTION 1 — FEATURES & THE GAP (45 min)

---

## SLIDE 6: Feature Breakdown — Connectors vs MCP vs Plugins

**VISUAL:** Three columns comparing integration approaches:

| | Cowork Connectors | Claude Code MCP | n8n Nodes |
|---|---|---|---|
| **What's available** | Gmail, Drive, Notion, Calendar | Anything with an API | 400+ pre-built integrations |
| **Who decides** | Anthropic builds them | You configure them | n8n community builds them |
| **Your internal tools** | ❌ Not possible | ✅ Connect your own APIs | ✅ Via HTTP node |
| **Can it think?** | ✅ Claude brain | ✅ Claude brain | ❌ No brain |
| **Can it chain judgment?** | Limited | ✅ Full reasoning chain | ❌ Just data routing |

**SPEAK (Tina, 3 min):**
> Before the demos, let me clarify three terms people confuse.
>
> **Connectors** are Cowork's way of reaching external tools. Toggle on Gmail, Claude reads your emails. Simple. But limited to what Anthropic has built.
>
> **MCP — Model Context Protocol** — is Claude Code's approach. Think of it as a USB port. You can plug in ANYTHING with an API — Google Sheets, HubSpot, Ahrefs, your internal booking system. The model is the same. The connections are open.
>
> **Plugins** are pre-built skill packs from Anthropic's marketplace or GitHub. One-click install. Someone else built them, you benefit.
>
> Now let me show you the difference with real tasks.

---

## SLIDE 7: What is an Agent? — n8n vs LLM vs Agent

**VISUAL:** Three-row comparison:

| | n8n Workflow | Claude Conversation | Agent |
|---|---|---|---|
| **What it is** | A fixed sequence of steps | A single chat session | A persistent specialist with role, tools, and memory |
| **Can it think?** | ❌ Follows rules only | ✅ Thinks, reasons, writes | ✅ Thinks within a defined scope |
| **Has memory?** | ❌ Stateless between runs | ❌ Forgets between sessions | ✅ Remembers across sessions |
| **Has specific tools?** | ✅ Whatever nodes you wire | ✅ Whatever Claude can access | ✅ Only the tools YOU assign |
| **Has a role?** | ❌ Generic automation | ❌ General-purpose assistant | ✅ Defined role (writer, analyst, chief-of-staff) |
| **Can improve over time?** | ❌ Same every run | ❌ No persistent learning | ✅ Learns from past sessions |

**Two types of agents:**

| | Local Agent (Claude Code) | Managed Agent (Console) |
|---|---|---|
| **Where it runs** | Your laptop terminal | Anthropic's cloud |
| **Defined in** | `.claude/agents/` as a markdown file | Console UI or API (Agent + Environment + Session + Events) |
| **Survives laptop shutdown** | ❌ Stops when you close terminal | ✅ Runs for hours/days/weeks |
| **Built-in caching/compaction** | ❌ You manage context | ✅ Anthropic handles it |
| **Cost** | Your API subscription | API tokens + $0.08/session-hour |
| **Best for** | Interactive work, development | Overnight batch jobs, production |

**SPEAK (Tina, 4 min):**
> "Agent" is the most overloaded word in AI. Let me sort it out.
>
> An **n8n workflow** follows fixed steps. "If lead arrives, send notification." Reliable but can't think.
>
> A **Claude conversation** thinks brilliantly but has no memory between sessions and no specific role.
>
> An **agent** is a Claude conversation with a persistent role, specific tools, and memory that improves over time. My linkedin-writer agent checks its own rejections.md before writing. It remembers what I deleted last time. That's an agent.
>
> **Local agents** run on your laptop. **Managed agents** run on Anthropic's cloud and survive your laptop shutting down. Same concepts — different infrastructure.

---

## SLIDE 8: DEMO 1 — Influencer Research (Cowork vs Code)

**VISUAL:** Split screen — Cowork on left, Claude Code on right

**THE PROMPT (same for both):**
> "Find premium travel influencers for the Indonesian market, focusing on overseas content on Instagram. Record each influencer's profile, performance metrics, URL, and contact info in a Google Sheet."

**What happens in Cowork:**
- Can search the web and find some influencer names
- Cannot systematically extract Instagram profile data (no Instagram connector)
- Cannot write structured data to Google Sheets (Sheets connector is read-limited for structured operations)
- Output: a text list in the chat window. You copy-paste manually.

**What happens in Claude Code:**
- MCP to Google Sheets → creates structured spreadsheet
- Web search + vision-first scraping → extracts real Instagram profile data
- Structures everything into columns (name, handle, followers, engagement rate, content focus, contact)
- Output: a live Google Sheet with 15+ influencers, ready to share with the team.

**SPEAK (Tina, 5 min):**
> Same prompt. Same brain. Different result. Cowork gives you a text list you have to copy-paste. Code gives you a live spreadsheet your team can use immediately.
>
> The difference? MCP. Claude Code can write directly to Google Sheets, scrape Instagram profiles, and structure data — because we connected those tools via MCP. Cowork's connectors don't support this.

---

## SLIDE 9: DEMO 2 — Google Search Console Analysis (Cowork vs Code)

**VISUAL:** Split screen — Cowork on left, Claude Code on right

**THE PROMPT (same for both):**
> "Call Google Search Console to analyze all user queries and page performance period-over-period for GoFreight. First two weeks of April vs last period."

**What happens in Cowork:**
- "I don't have access to Google Search Console." Dead end.
- No GSC connector exists in Cowork.

**What happens in Claude Code:**
- MCP to Google Search Console → pulls real query data
- Analyzes period-over-period: impressions, clicks, CTR, position changes
- Identifies rising queries, declining pages, new opportunities
- Generates a formatted report with actionable insights

**SPEAK (Tina, 5 min):**
> This one is brutal. Cowork simply says "I can't." The tool doesn't exist in its connector library.
>
> In Code, we connected GSC via MCP. Claude pulls real data — 5,000+ queries — analyzes period-over-period, and surfaces the insights. Same brain. One can't even start. The other delivers a complete analysis.
>
> This is why MCP matters. You're not limited to what Anthropic pre-builds. You connect what YOU need.

---

## SLIDE 10: DEMO 3 — Video Ad Creation Pipeline (Cowork vs Code)

**VISUAL:** Split screen — Cowork on left, Claude Code on right

**THE PROMPT (same for both):**
> "I have a vision API (HeyGen or Seedance). Create a TikTok ad video for this Tiket.com activity page: https://www.tiket.com/en-sg/to-do/trip-pendakian-gunung-rinjani-by-rineh-adventure. Use a local-looking AI avatar, real photos from the page with animations, highlight activities as hook/description, VO should be throughout the video. Walk me through the plan first."

**What happens in Cowork:**
- Can draft a script and storyboard (text output)
- Cannot scrape the page for real photos (browser extension unreliable)
- Cannot call HeyGen/Seedance API (no connector)
- Cannot orchestrate a multi-step video pipeline
- Output: a written plan. You do all the execution yourself.

**What happens in Claude Code:**
- Web scrape page (vision-first) → extracts real activity photos + descriptions
- Drafts video script: hook → activity highlights → CTA
- Calls HeyGen/Seedance API via MCP → configures avatar, VO, animations
- Orchestrates the pipeline: scrape → script → API call → asset assembly
- Output: a production plan with downloaded assets, script, and API calls ready to execute

**SPEAK (Tina, 5 min):**
> This is the most ambitious demo. Same prompt. Cowork gives you a script — which is useful! But you still have to go to HeyGen yourself, upload photos yourself, configure the avatar yourself.
>
> Code orchestrates the entire pipeline. It scrapes the page for real photos, writes the script, calls the video API, and assembles everything. You review and approve. That's the difference between a personal assistant that ADVISES and an operating system that EXECUTES.

---

# SECTION 1.5 — NAMING THE PIECES (20 min)

---

## SLIDE 11: The .claude/ Folder — Your Team's Operating System

**VISUAL:** Real directory tree from Tina's setup:

```
~/.claude/
├── CLAUDE.md                  ← constitution (90 lines — communication style, verification rules, MCP instructions)
├── settings.json              ← permissions, 5 hook categories, status line, plugins
├── hooks/
│   └── memory-extract.sh      ← auto-saves learnings at end of each session
├── agents/                     ← 2 global agents (deep-researcher, hermeneutic-thinker)
├── commands/                   ← 60+ slash commands (/linkedin-writer, /prospect-audit, /chief-of-staff...)
└── skills/                     ← 70+ skills (content-production, bookkeeping, aeo-audit, n8n-expert...)

~/novastacks/.claude/
└── agents/                     ← 15 project-level specialists
    ├── linkedin-writer.md      ← writes posts, learns from past rejections
    ├── chief-of-staff.md       ← tracks leads, preps meetings, sends emails
    ├── marketing-data-analyst.md ← diagnoses traffic drops, creates dashboards
    ├── content-writer.md       ← executes briefs in any client's voice
    ├── n8n-specialist.md       ← builds and debugs n8n workflows
    └── ... 10 more
```

**SPEAK (Tina, 3 min):**
> This is my actual setup. Not a demo. 60 commands, 70 skills, 15 project agents, 5 hook categories. One person built this over 3 months.
>
> **The brain is the same for everyone. The harness is what makes it yours.**

---

## SLIDE 12: Personal Capabilities vs Enterprise System

**VISUAL:** Two columns:
- Left: "Cowork — Personal" — skills, memory, connectors, scheduled tasks
- Right: "Code — Enterprise" — + hooks, agents, rules, commands, git, permissions

| What you have in Cowork | What Code adds on top |
|---|---|
| Skills (reusable workflows) | + **Commands** — one-line shortcuts that trigger workflows |
| Memory (claude.md, memory.md) | + **PROGRESS.md** — state tracking for multi-session work |
| Connectors (Gmail, Drive, Notion) | + **MCP** — open protocol, connect ANY tool, your own APIs |
| Scheduled tasks | + **Hooks** — guaranteed enforcement that CAN'T be skipped |
| Personal instructions | + **CLAUDE.md as constitution** — team-wide, version-controlled |
| — | + **Agents** — dedicated specialists with their own tools and cost tier |
| — | + **Rules** — context guardrails that load only when relevant |
| — | + **Git** — version control, branches, team coordination |
| — | + **Permissions** — allow/deny lists for what Claude can touch |

**SPEAK (Tina, 3 min):**
> Cowork is powerful. You already have skills, memory, connectors, scheduled tasks. So what does Code actually add?
>
> Cowork's capabilities are **personal** — they live on your machine, serve one person, and rely on Claude following instructions voluntarily. Code's capabilities are **systemic** — they enforce behavior, specialize agents, coordinate teams, and guarantee quality through code, not trust.
>
> That's the difference. Not more features. A different layer: **enforcement, specialization, version control, team coordination.**

---

## SLIDE 13: Skills in Code — Auto-Invoke + Commands

**SPEAK (Tina, 3 min):**
> You already know skills from Cowork. In Code, skills **auto-invoke**:
>
> 1. Claude scans your `skills/` folder on session start
> 2. Reads the `name:` and `description:` from each file
> 3. You type "write a blog post about hotel trends"
> 4. Claude matches against skill descriptions → auto-loads the right skill
> 5. You never typed a command. It just knew.
>
> **The `description:` field is the most important line in your skill file.** "Use when writing blog content for any client" — good. "Content writing tool" — useless.
>
> **Commands** are new — one-liner shortcuts. `/partner-report Marriott` triggers a skill. You type 3 words, Claude does 15 minutes of work. Skills are the cookbook. Commands are the speed-dial buttons.

---

# ☕ BREAK (10 min)

---

# SECTION 2 — THE HARNESS: WHY AI HALLUCINATES & HOW TO STOP IT (30 min)

---

## SLIDE 14: The Context Window — Why Claude "Forgets"

**VISUAL:** Use Anthropic's official context window diagram (source: https://platform.claude.com/docs/images/context-window.svg)

Simplified:
```
Turn 1:  [User message] [Claude response]              ← 2% used
Turn 5:  [ALL previous + msg] [Claude response]         ← 15% used
Turn 15: [ALL previous + msg] [Claude response]         ← 75% used ⚠️
Turn 20: [ALL previous + msg] [Claude response]         ← 95% used 🔴 CONTEXT ROT
```

**SPEAK (Tina, 4 min):**
> The ONE thing about Claude that affects everything else. The **context window** is Claude's working memory — a whiteboard. Everything has to fit: your instructions, conversation history, files it read, its own responses.
>
> Current models: up to 1 million tokens. Sounds like a lot. But it fills up fast — every turn is additive. By Turn 15-20, you've used 75-95%.
>
> **As the whiteboard fills, Claude's accuracy drops.** Anthropic calls this "context rot." Your instructions from the beginning are now competing with thousands of lines of accumulated data. The signal gets drowned by noise.
>
> **This is why your Cowork output sometimes gets weird.** First 10 messages, great. By message 40, Claude forgets your brand voice and starts making things up. That's context rot.

---

## SLIDE 15: The Post-Mortem — prospect-audit v2 vs v3

**VISUAL:** Two architecture diagrams side by side:

**v2 — The Monolith (shipped bad reports to clients):**
```
One agent, one file (1,791 lines), one context window

Phase 0: Competitor Discovery      ← ~5K tokens
Phase 1: Domain Metrics + Tech    ← +15K tokens
Phase 2: Page Crawling             ← +30K tokens (raw HTML)
Phase 3: Keyword Analysis          ← +20K tokens
Phase 4: Lighthouse Performance    ← +10K tokens
Phase 5: LLM Visibility Testing   ← +12K tokens
Phase 6: AEO Scoring               ← +5K tokens
Phase 7: Report Generation         ← 🔴 ~100K+ tokens accumulated
                                      Instructions from Phase 0 are DROWNING
```

**v3 — The Decomposed System (zero shipped errors post-Gate 3):**
```
Orchestrator (238 lines) — does almost nothing itself
  │
  ├── Spawns COLLECT subagent (443 lines, fresh context)
  │     └── Writes to raw-data/ files
  │
  ├── Gate 1: validate_raw_data.py ← Python, exit 0/1
  │     └── Missing files? Malformed data? → RETRY with fresh agent
  │
  ├── Spawns REPORT subagent (474 lines, fresh context)
  │     └── Reads from raw-data/ files (canonical source)
  │
  ├── Gate 2: validate_json_output.py ← Python, exit 0/1
  │     └── Missing fields? Scores out of range? Placeholder text?
  │
  └── Gate 3: validate_claims_vs_raw.py ← Python, exit 0/1
        └── Keyword count matches raw file? CWV values match correct domain?
```

**SPEAK (Tina, 7 min):**
> Let me tell you what happened to us.
>
> We built `prospect-audit-v2` — a 1,791-line skill that runs 8 phases of data collection, scoring, and report generation. Pulled data from 5 APIs, analyzed competitors, generated a 20-page HTML report. Impressive.
>
> Then it shipped a report to a client with fabricated numbers. Said a company ranked #1 for a keyword — real rank was #5. Said a brand had "zero defensive content" — they actually had a 50-question FAQ page. Copied one company's website speed metrics into another company's section.
>
> Why? By Phase 7, the agent had accumulated 100,000+ tokens. The scoring rules we wrote in Phase 0 were drowning under 20,000 tokens of raw API output. The model didn't "decide" to lie. It drifted. The signal got lost.
>
> We had to rewrite client reports. **The skill wasn't the problem. The architecture was.**
>
> v3 fixed it with three changes:
>
> 1. **Context isolation** — split into 3 agents. The report agent NEVER sees the API response logs. It only reads the saved, validated files. Fresh whiteboard.
>
> 2. **Deterministic gates** — Python scripts between agents. Gate 1 checks: did you actually collect all the data? Gate 2 checks: is the JSON valid? Gate 3 cross-validates: does the report say "27,659 keywords" when the raw file says 15,164? If any gate fails → exit code 1 → retry with a fresh agent. The model CANNOT hallucinate past a Python exit code.
>
> 3. **Reference isolation** — v2 loaded all 1,791 lines into every phase. v3 gives each agent only the references it needs. The collect agent gets API patterns. The report agent gets the JSON schema and anti-pattern rules. No cross-contamination.
>
> | | v2 | v3 |
> |---|---|---|
> | File structure | 1 file, 1,791 lines | Orchestrator + 2 subagents + 7 scripts + 4 references |
> | Context at report time | ~100-150K tokens (all phases) | ~10-15K tokens (fresh) |
> | Validation | Bash script run by the agent | 3 Python gates with exit codes |
> | Cross-validation | None | Gate 3: numeric comparison against raw files |
> | Data contract | Conversation memory | Filesystem (raw-data/ directory) |
> | Shipped hallucinations | Blue Buffalo (keyword inflation), Kong Dental (CWV swap) | Zero post-Gate 3 |
> | Cost | $0.41-0.52 | $0.48-1.01 |
>
> The thesis: **context window pollution causes hallucination. The fix is context isolation + deterministic external validation.** Every building block we're teaching today — agents, hooks, gates — is a response to this problem.

---

## SLIDE 16: The Concepts — Agent, Hook, Gate

**VISUAL:** Three cards:
- Agent: "Isolated specialist. Fresh context window. Specific tools."
- Hook: "Harness-level enforcement. YOUR system runs it, not Claude. Can't be skipped."
- Gate: "Deterministic validation between agents. Python, not prompts. Exit 0 or exit 1."

**SPEAK (Tina, 3 min):**
> Three concepts from that story:
>
> **Agent** = a specialist with its own context window. The collect agent never sees the report agent's conversation. Each gets a fresh whiteboard. That's how you prevent context rot in complex workflows.
>
> **Hook** = a script YOUR system runs, not Claude. Before every file write, check for credential leaks. After every markdown edit, verify document coherence. Before every git commit, run quality checks. Claude can't skip a hook — it's a tripwire in the operating system.
>
> My real hooks:
> - **PreToolUse (Edit/Write):** blocks writes to .env, credentials, secrets
> - **PostToolUse (Edit/Write):** re-reads and verifies every markdown file Claude edits
> - **Stop:** macOS notification with open task count + auto-extracts lessons to MEMORY.md
>
> **Gate** = deterministic validation between agents. Python script, exit 0 or exit 1. "Does the report say 27,659 keywords? Does the raw file say 15,164? If they don't match → exit 1 → retry." The model cannot explain away a Python exit code.
>
> Together: agents give you isolation, hooks give you enforcement, gates give you validation. That's the harness.

---

## SLIDE 17: The Philosophy Table

**VISUAL:** The building block table:

| Piece | Role | One-liner |
|-------|------|-----------|
| **CLAUDE.md** | The Constitution | What Claude must always do, without exception. |
| **Skills** | The Procedures | How to execute. Detailed, step-by-step, loaded on demand. |
| **Hooks** | The Guarantees | Enforcement that absolutely cannot be skipped. |
| **MEMORY.md** | The Learnings | What was discovered, mistakes caught, decisions made. |
| **Agents** | The Specialists | Dedicated team members with their own role and tools. |
| **Rules** | The Guardrails | Standards that load only when relevant files are touched. |
| **Commands** | The Shortcuts | One-liners that trigger entire workflows. |
| **PROGRESS.md** | The State | Where we are. What's done, what's next, what's blocked. |

**SPEAK (Tina, 2 min):**
> Write this down — it's the most important frame of the day.
>
> Constitution. Procedures. Guarantees. Learnings. State. Specialists. Guardrails. Shortcuts. That's what turns personal capabilities into a reliable system.

---

# SECTION 3 — BUILD A WORKFLOW LIVE (30 min)

---

## SLIDE 18: "Now let me show you the build"

**SPEAK (Tina → Yaohong, 1 min):**
> You've seen the gap. You've understood the concepts. Now Yaohong is going to build a real workflow from scratch — live, in the terminal.

---

## SLIDE 19-23: Yaohong Demo — Building a Pipeline

**VISUAL:** Live terminal screen

### Layer 1: Raw Data Fetch
**SPEAK (Yaohong):** "I'll start with a simple data pull — partner performance data."

### Layer 2: Enrich with Context
**SPEAK (Yaohong):** "Now adding web research — their recent news, market position. Two data sources combined."

### Layer 3: Analyze
**SPEAK (Yaohong):** "Now Claude analyzes. Finds trends. Flags issues. It's thinking, not just copying."

### Layer 4: Format and Save
**SPEAK (Yaohong):** "Format as a clean report. Save to file. That's a deliverable."

### Layer 5: Wrap into a Skill + Command
**SPEAK (Yaohong):** "Now the magic. I wrap all 4 steps into a `/partner-report` command. Anyone on the team can run it."

---

## SLIDE 24: The Pattern

**VISUAL:** Pipeline diagram: Fetch → Enrich → Analyze → Format → Save → (wrap into command)

**SPEAK (Tina, 3 min):**
> Every agentic workflow has the same shape: fetch data, add context, analyze, format, save. The only things that change are the data sources and the output format.
>
> [Job bridge — Sales]: Fetch partner data → enrich with meeting notes → analyze booking trends → format as call prep brief → `/call-prep Marriott`. Done.
>
> [Job bridge — Content]: Fetch keyword rankings → competitor analysis → gap analysis → content calendar → `/content-plan Q3`. Done.
>
> [Job bridge — Marketing]: Fetch campaign performance → CRM data → ROI by channel → weekly brief → `/weekly-brief`. Done.

---

# SECTION 4 — IMPROVE IT: WORKSHOP DISCUSSION (15 min)

---

## SLIDE 25: Pick 2 Workflows

**VISUAL:** "Your turn. What's the workflow you'd automate?"

**SPEAK (Tina, 15 min):**
> I want 2 volunteers. Tell me a task you do weekly that takes more than 2 hours. We'll design the workflow together — right now.
>
> For each workflow, we'll answer:
> - What's the skill? (the repeatable procedure)
> - What's the agent? (does it need a specialist?)
> - Where's the hook? (what must be enforced?)
> - What are the data sources? (MCP connections needed?)
> - What's the output? (file, spreadsheet, email, Slack message?)

---

# SECTION 5 — TEAM-AGENT COLLABORATION (10 min)

---

## SLIDE 26: The Safety Envelope

**VISUAL:** Three concentric circles:
- Outer: "Permissions" — what Claude CAN'T do
- Middle: "Hooks" — what the system ENFORCES
- Inner: "Rules" — what Claude SHOULD do

**SPEAK (Tina, 2 min):**
> How do you trust an agent not to break things? Three layers:
> - **Permissions** block actions entirely. Claude literally cannot force-push or send bulk emails.
> - **Hooks** enforce checks. Before every commit, quality check. After every file write, verify formatting.
> - **Rules** guide behavior. "Blog posts should be warm and concrete." Guidance, not enforcement.

---

## SLIDE 27: "Git is the new Notion"

**VISUAL:** Translation table:

| Git | You already know this as... |
|-----|---------------------------|
| `git pull` | Hitting refresh in Google Docs |
| `git commit` | "Save version" with a note |
| `git push` | Sharing / publishing |
| `main branch` | The "published" page |

**SPEAK (Tina, 3 min):**
> Everything lives in git. Agents work on branches. You review their work. YOU decide when it lands on main. Without this, the "published" version is whatever an agent did at 3am. With it, you're always in control.
>
> Five commands. That's all you need. You learned Notion. You learned ClickUp. Git is smaller than both.

---

## SLIDE 28: Yaohong's Real Experience

**SPEAK (Yaohong, 5 min):**
> [PLACEHOLDER — Yaohong fills in from personal experience]
> - "Here's how I actually use agents day-to-day"
> - "What's worked — the win that surprised me most"
> - "What's been painful — the honest friction"
> - "My one recommendation for this room"

---

# CLOSE — THE MONDAY PLAN (10 min)

---

## SLIDE 29: Recap in 60 Seconds

**VISUAL:** 5 takeaways:

1. Automation (n8n) vs Augmentation (Claude). Claude Code combines both — thinking + reliability.
2. Context rot is real. Isolation + gates + hooks = the fix.
3. One folder (`.claude/`) = your team's AI operating system.
4. Agents are specialists. Skills are procedures. Hooks are enforcement. Permissions are the wall.
5. Git is how you coordinate. Main branch = truth. You always decide what lands.

---

## SLIDE 30: Your Week 1 Checklist

**VISUAL:** Checklist:

- [ ] Use the Jeff Su 6-step in Cowork: do manually → feedback → remember → skill → install → schedule
- [ ] Open your terminal and run `git pull` in the team repo
- [ ] Read the `.claude/CLAUDE.md` file — that's your team's handbook
- [ ] Pick ONE task you do weekly that takes > 2 hours
- [ ] Write the baseline: what task, how long, how often, what quality
- [ ] Bring that baseline to the next session — we'll build the skill together

---

## SLIDE 31: Resources

**VISUAL:** QR codes / links:

- 📖 Reference Guide — full deep-dive (HTML)
- 🛠 Skills Guide — build your first production skill
- 🔀 Git for Non-Engineers — the 5-command guide
- 📊 AI Impact Report Template — the one-pager for VPs
- 🧰 Agentic Tools Cheatsheet — what else is out there

---

## SLIDE 32: Q&A

**SPEAK (Tina, 5 min):**
> Open floor. Ask anything.

---

## SLIDE 33: Closing

**VISUAL:** "Same brain. Bigger operating system."

**SPEAK (Tina, 1 min):**
> The best time to start was 3 weeks ago — and you did, with Cowork. The next best time is now. Same brain, bigger operating system.
>
> Thank you. Go build something.

---

# APPENDIX 0 — Trainer Prep Checklist

**Tina — before workshop:**
- [ ] Screenshot real `~/.claude/` directory → for Slide 11
- [ ] Screenshot CLAUDE.md (first 30 lines) → for Slide 11
- [ ] Prepare Demo 1: Google Sheets MCP connected, Instagram search workflow tested
- [ ] Prepare Demo 2: GSC MCP connected to GoFreight, PoP analysis tested
- [ ] Prepare Demo 3: HeyGen/Seedance API access confirmed, Tiket.com page scrape tested
- [ ] Print the philosophy table (Slide 17) as a handout

**Yaohong — before workshop:**
- [ ] Test full 5-layer pipeline end-to-end at least twice → Slides 19-23
- [ ] Prepare `/partner-report` skill template (Layer 5)
- [ ] Prepare fallback: if API is down, have mock data ready
- [ ] Fill in Slide 28 (personal experience): examples, wins, pain points
- [ ] Test screen sharing + terminal font size

**Both — day of:**
- [ ] Run `git pull` in the demo repo
- [ ] Test projector + screen sharing before audience arrives
- [ ] QR code ready for resources (Slide 31)
- [ ] Agree on hand-off cues

---

# APPENDIX A — Gamma Slide Construction Notes

## Design Theme: Anthropic-Branded

### Color Palette

| Role | Color | Hex |
|---|---|---|
| **Primary background** | Warm light | `#FAF9F5` |
| **Text / dark bg** | Near-black | `#141413` |
| **Secondary text** | Mid gray | `#B0AEA5` |
| **Subtle bg** | Light gray | `#E8E6DC` |
| **Primary accent** | Terracotta | `#D97757` |
| **Secondary accent** | Blue | `#6A9BCC` |
| **Tertiary accent** | Green | `#788C5D` |

### Typography

| Role | Font | Fallback |
|---|---|---|
| Headings | Poppins | Arial |
| Body text | Lora | Georgia |
| Code | JetBrains Mono | Courier New |

### Gamma Setup

1. Background: `#FAF9F5` | Text: `#141413`
2. Accent 1: `#D97757` (terracotta) | Accent 2: `#6A9BCC` (blue) | Accent 3: `#788C5D` (green)
3. Fonts: Heading = Poppins, Body = Lora

---

# APPENDIX B — v2 vs v3 Deep Dive (Reference)

## v2 — The Monolith

- **1,791 lines**, single file, single agent
- 8 phases (0-7) in one context window
- ~100-150K tokens accumulated by Phase 7
- Validation: bash script run BY the agent (advisory, not blocking)
- **Shipped errors:** Blue Buffalo (keyword count 27,659 vs actual 15,164), Kong Dental (CWV values swapped between domains)

## v3 — The Decomposed System

- **Orchestrator** (238 lines) + **Collect subagent** (443 lines) + **Report subagent** (474 lines)
- 7 Python scripts (3 validation gates + page analyzer + 3 test files)
- 4 reference files (API patterns, market defaults, JSON schema, anti-patterns)
- Each subagent: fresh context, ~10-15K tokens, reads from disk not conversation

## The 3 Gates

| Gate | Script | What it catches |
|---|---|---|
| Gate 1 | `validate_raw_data.py` | Missing/empty files, suspicious identical Lighthouse scores |
| Gate 2 | `validate_json_output.py` | Missing JSON fields, scores outside 0-10, placeholder text, CWV incompleteness |
| Gate 3 | `validate_claims_vs_raw.py` | Keyword count inflation, CWV attribution swaps, ETV drift > 5% |

## Why the LLM Cannot Bypass Gates

The orchestrator runs Python scripts and checks exit codes. Exit 0 = pass. Exit 1 = fail → re-spawn fresh subagent with error list. The model cannot "explain away" a Python exit code. File existence is binary. Numeric comparison is deterministic. That's the engineering thesis: **deterministic validation between probabilistic agents.**

---

# APPENDIX C — Job-Specific Bridges

### Sales
- `/call-prep Hilton Jakarta` — pulls meeting notes, booking data, contract status → one-page brief
- "Response time to partner inquiries dropped from 48h to 4h"

### Content
- `/blog-draft "hotel distribution trends"` — researches, pulls SEO data, writes in brand voice
- "We automated the weekly content brief. 6 hours → 45 minutes of review."

### Marketing
- Campaign performance → CRM data → ROI by channel → weekly brief → Slack
- Hook: prevent campaign asset finalization without brand guideline check
- Permissions: allow analytics read, deny bulk email send

---

# APPENDIX D — Tools Glossary

**AI Interfaces**
| Tool | What it is | When to use |
|---|---|---|
| Claude.ai | Web chat | Quick Q&A |
| Claude Cowork | Desktop app with skills + connectors | Daily workflows (80%) |
| Claude Code | Terminal harness with agents, hooks, git | Team systems (20%) |
| Console | Builder dashboard at platform.claude.com | Managed Agents, prompt testing, monitoring |

**Integration Protocols**
| Tool | What it is |
|---|---|
| MCP | "USB ports" — connect Claude to any tool with an API |
| Cowork Connectors | Pre-built integrations (Gmail, Drive, Notion, Calendar) |
| n8n Nodes | 400+ pre-built automation integrations |

**Data & Analytics**
| Tool | What it is |
|---|---|
| Google Analytics (MCP) | Website traffic and behavior |
| Google Search Console (MCP) | Organic search performance |
| DataForSEO (API) | Keyword data, SERP, backlinks, AI mentions |
| Ahrefs (MCP) | Backlinks, domain ratings, keywords |
| HubSpot (MCP) | CRM — contacts, deals, engagement |

**Communication**
| Tool | What it is |
|---|---|
| Gmail (MCP) | Send, read, draft emails |
| Google Calendar (MCP) | Events, scheduling |
| Slack (webhook) | Notifications, summaries |

---

# APPENDIX E — Source Credits

**Raymond Houch (lifehacker.tw):** 3-tier framework, "commander/executor" metaphor, safety architecture, "create skill after 3rd repetition" rule
**thisweb.dev:** Full primitive anatomy, hooks event types, rules with paths:
**Pietro Montaldo (LinkedIn):** "Skills create an abstraction layer over work itself"
**Michael J. Silva (LinkedIn):** "Runtime layer is where real value accrues, model is commodity"
**Emily Kramer (MKT1):** "Gen Marketer" concept, "With tools you are the operator, with agents you are the manager"
**Clay.com:** "GTM Engineer" coined 2023, 3,000+ roles by Jan 2026
**Jeff Su:** Cowork 7 capabilities, skills-from-experience workflow, outcome-first prompting
**Fortune Magazine:** "The Supervisor Class"
**Stanford HAI:** Prompt refinement <3% improvement vs harness-level 28-47%
**Anthropic Docs:** Context windows, Managed Agents (4 concepts), MCP protocol
