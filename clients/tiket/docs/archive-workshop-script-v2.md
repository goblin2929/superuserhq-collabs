# Claude Code Intermediate: Beyond Cowork
## Full Workshop Script — Gamma Slide Deck + Speaker Notes

**Audience:** 25 non-technical Tiket staff (B2B Sales, TDD/Content, Marketing) — 3 weeks Cowork experience
**Speakers:** Tina (lead) + Yaohong (demos)
**Duration:** 120 min | **Date:** April 20, 2026 — Jakarta

---

# ACT 1 — THE GAP (20 min)
*Purpose: Create surprise. Show them something Cowork can't do. Earn attention for the concepts that follow.*

---

## SLIDE 1: Title

**VISUAL:** Full-bleed title slide
- "Claude Code Intermediate: Beyond Cowork"
- Novastacks AI × Superuser HQ logos
- Tiket.com Team — April 2026 — Jakarta

**SPEAK (Tina, 1 min):**
> Welcome. Quick show of hands — who's used Cowork every day this past week? [pause for hands] Great. Who's built at least one project? [pause] Good. You're not beginners. You've been using Claude for 3 weeks and you've built things that work.
>
> So today is NOT Claude 101. Today is about what comes after Cowork — how to go from using Claude as a personal assistant to building systems that run your operations. You've learned how to talk to Claude. Now we're going to learn how to architect around it.
>
> One thing before we start — "Be willing to temporarily be bad at something in order to break through." The terminal will feel uncomfortable for about 2 days. That's normal. Push through that and you'll come out the other side with superpowers you didn't know existed.

---

## SLIDE 2: Why You're Here — The Role Has Changed

**VISUAL:** Side-by-side: "Marketing Campaign Manager 2023" JD vs "GTM Engineer / Gen Marketer 2026" JD. Key skill differences highlighted in terracotta.

**The JD comparison:**

|                   | Old JD (Campaign Manager, 2023)     | New JD (GTM Engineer / Gen Marketer, 2026)           |
| ----------------- | ----------------------------------- | ---------------------------------------------------- |
| **Primary job**   | Execute campaigns                   | Design systems that execute campaigns                |
| **Content**       | Write the blog, manage the calendar | Build the skill that writes, schedules, optimizes    |
| **Data**          | Pull reports, build dashboards      | Curate insights from agent-generated analysis        |
| **Tools**         | Master Canva, HubSpot, GA           | Orchestrate agents that USE Canva, HubSpot, GA       |
| **Collaboration** | 5-10 human stakeholders per project | You + your agents do more, fewer human dependencies  |
| **Salary signal** | $60-90K                             | $125-250K+ (GTM Engineer at Ramp, Notion, Anthropic) |

**The skill shift:**

| Campaign Manager (2024)                          | GTM Engineer (2026)                        |
| ------------------------------------------------ | ------------------------------------------ |
| 1. Manual content production                     | 1. Agent harness design                    |
| 2. Tool-specific expertise (HubSpot, GA, Canva,) | 2. Workflow architecture                   |
| 3. Cross-dept coordination                       | 3. Human-agent coordination                |
| 4. Analytics & reporting                         | 4. Quality system design                   |
| 5. Project management                            | 5. Deterministic vs probabilistic thinking |
| 6. Campaign setup & execution                    | 6. Data pipeline thinking                  |
| 7. Single-channel mastery                        | 7. Strategic insight curation              |
| **In common:** Campaign strategy, execution, performance review |

**SPEAK (Tina, 5 min):**
> Before we get into the tools — let me show you why you're actually here. It's not because your manager signed you up for a training. It's because the job description has changed.
>
> [Show the table]
>
> This is a real comparison. Left column: what a marketing campaign manager's JD looked like in 2023. Right column: what companies like Notion, Anthropic, Ramp, and Toast are hiring for right now — they call it "GTM Engineer" or "Gen Marketer."
>
> The old job was about execution: write the blog, manage the calendar, pull the report, run the campaign. The new job is about orchestration: design the system that writes, schedules, reports, and runs — and then supervise it.
>
> Now look at the skill table. Left column: the top skills of a campaign manager in 2024 — manual content, tool expertise, cross-dept coordination, analytics, project management. Right column: GTM Engineer in 2026 — agent harness design, workflow architecture, human-agent coordination, quality systems. The left column skills aren't disappearing. But agents handle the execution layer now. The right column skills didn't even exist 2 years ago. Today they're the highest-value skills in the market.
>
> Here's the one that hits home for most people in this room: **cross-department coordination.** In the old model, you needed 5-10 stakeholders to ship anything — a designer for the visual, a copywriter for the text, legal for compliance, analytics for the data, dev for the landing page. In the new model, your agents handle design, copy, data, and QA. You coordinate with 1-2 humans for final approvals. That's a fundamentally different way of working — and it requires a fundamentally different skill set.
>
> Clay coined the term "GTM Engineer" in 2023. By January 2026, there were 3,000+ open GTM Engineer roles on LinkedIn — 205% year-over-year growth. Emily Kramer, ex-VP Marketing at Asana, calls the new role "Gen Marketer" — a generalist who's fluent in AI and orchestrates agents instead of doing everything manually.
>
> Here's the key quote from her: **"With tools, you are the operator. With agents, you are the manager."** That's the shift.
>
>  McKinsey found teams using AI automation reduced manual workflow time by 60-80%. Stanford found that better prompts improve output by less than 3% — but better harness design improves output by 28-47%.
>
> So where are you today? With 3 weeks of Cowork, you're probably producing 2-5x your normal output. That's real. But the teams running full agentic workflows — with agents, hooks, rules, permissions, pipelines — they're at 10-100x. The gap between 3x and 10x isn't just effort. It's architecture. It's the skills we're going to cover today.
>
> Fortune Magazine called this "The Supervisor Class" — the idea that every professional becomes a supervisor of agents. Not replaced by agents. A supervisor of agents. The marketer who can design a system, review agent output, and refine the harness — that person is 10x more valuable than the one still writing every email by hand.
>
> That's why you're here. Not to learn a tool. To learn the skill set that's reshaping your career.

---

## SLIDE 3: What this is / What this isn't

**VISUAL:** Two columns
- Left: "THIS IS" (green) — Vocabulary. Mental model. Real examples. Coordination skills.
- Right: "THIS IS NOT" (red) — Beginner course. Engineering class. Tool tour. Sales pitch.


**SPEAK (Tina, 2 min):**
> Two things upfront.
>
> This IS about giving you the vocabulary and mental model that engineers have been using for 20 years. By the end, you'll be able to say things like "that should be a hook, not a rule" or "let's put that in an agent with haiku" — and your team will understand. Shared language is half the battle.
>
> This is NOT about making you engineers. You won't write code. You WILL learn how to design workflows — the thinking, not the syntax. Think of it as learning to be an architect, not a carpenter.
>
> [Tina personal bridge]: I run a 4-person marketing studio. Nobody on my team is an engineer. We all use Claude Code daily. If we can do it, you can do it.

---

## SLIDE 4: AI Automation vs AI Augmentation

**VISUAL:** Two columns, clearly separated:

|                         | AI Automation (n8n, Zapier)           | AI Augmentation (Claude)                                        |
| ----------------------- | ------------------------------------- | --------------------------------------------------------------- |
| **What it does**        | Follows rules: "if this, then that"   | Thinks, reasons, writes, analyzes                               |
| **Strengths**           | Reliable, predictable, runs 24/7      | Smarter, Creative, adaptive, handles ambiguity                  |
| **Weaknesses**          | Can't think, can't adapt, can't write | Can drift, can fabricate, needs guardrails                      |
| **Example**             | "New lead → send Slack notification"  | "Analyze this partner's decline and draft a re-engagement plan" |


**VISUAL (infographic):** Side-by-side architecture diagrams — same task: "Pull partner data from HubSpot, analyze decline, send re-engagement email"

```
n8n approach:                              Claude Code approach:
┌─────────────┐                            ┌─────────────────┐
│  Trigger     │                            │  You (terminal)  │
│  (schedule)  │                            │  "Analyze partner │
└──────┬──────┘                            │   decline and     │
       │                                    │   draft email"    │
       ▼                                    └────────┬─────────┘
┌─────────────┐                                      │
│  HubSpot    │  ← API node                          ▼
│  (get data) │                            ┌─────────────────┐
└──────┬──────┘                            │  Claude brain    │
       │                                    │  + MCP tools     │
       ▼                                    │                  │
┌─────────────┐                            │  ┌──────────┐   │
│  IF node    │  ← hardcoded rules         │  │ HubSpot  │   │
│  (decline?) │                            │  │ Gmail    │   │
└──────┬──────┘                            │  │ Sheets   │   │
       │                                    │  │ Ahrefs   │   │
       ▼                                    │  └──────────┘   │
┌─────────────┐                            └────────┬─────────┘
│  Template   │  ← fixed email                      │
│  (send)     │                              Thinks → Analyzes
└──────┬──────┘                              → Writes → Sends
       │                                             │
       ▼                                             ▼
┌─────────────┐                            ┌─────────────────┐
│  Airtable   │  ← separate UI             │  Result in your  │
│  (view it)  │    to see results           │  terminal + file │
└─────────────┘                            └─────────────────┘

Setup: 2-4 hours                           Setup: 5 minutes
Nodes: 6-8 to wire                         Tools: already connected via MCP
Interface: need Airtable/dashboard          Interface: built-in (terminal + files)
Changes: rewire nodes                      Changes: just ask differently
Can it think? ❌                            Can it think? ✅
Can it adapt? ❌                            Can it adapt? ✅
```

**SPEAK (Tina, 4 min):**
>
> **n8n is AI automation.** "If this happens, do that." New lead in HubSpot → send Slack notification. Form submitted → create ticket. It's reliable. It runs the same way every time. But it **can't think.** You know this — you've built these workflows. And you know the effort. You need a trigger node, an API node to pull data from HubSpot, an IF node for your rules, a template for the email, another node to send it, and then you need Airtable or a dashboard just to SEE the results. 6-8 nodes. 2-4 hours to wire up. And if the requirements change? You rewire the whole flow.
>
> **Claude is AI augmentation.** It thinks alongside you. It's a co-worker, a thinking partner, a co-creator. And here's the architectural difference — look at the diagram. Claude Code connects to the same tools you use in n8n — HubSpot, Gmail, Google Sheets, Canva, Apollo — but through MCP. The difference? You don't wire nodes. You just say what you want. And the interface is built in — you see the results right there. No separate Airtable view needed.
>
> What does augmentation give you that automation can't?
> - **Co-thinking** — "Here's our campaign data. What patterns do you see?"
> - **Co-working** — "Draft 5 versions of this partner email, each with a different angle"
> - **Co-creating** — "Build a competitor analysis framework we can reuse"
> - **Adaptation** — "The input changed. Figure out the right response."
>
> Automation says: "Do step 1, then step 2, then step 3." Augmentation says: "Here's the goal — figure out how to get there."
>
> Here's the key: **they're not competing. They're complementary.** n8n handles the predictable, repeatable parts — the things that should run the same way every time at 3am. Claude handles the parts that need judgment. Today we're learning how to build the system that combines both.

---

## SLIDE 5: Four Ways to Use Claude — Same Brain, Different Harness

**VISUAL:** Four cards in a row, same Claude logo on each, progressively more structure around it:

| | Claude.ai | Cowork | Claude Code | Console |
|---|---|---|---|---|
| **Metaphor** | Google that understands you | Your personal assistant | Your team's operating system | The control tower |
| **Interface** | Web browser | Desktop app | Terminal / IDE | Web dashboard |
| **What you do** | Ask a question | Give it a workspace + skills | Build the system it operates in | Configure agents, monitor, deploy |
| **What Claude can do** | Answer, write, analyze | Read your files, run skills, browse for you | Use tools, follow rules, run agents, remember | Run autonomously for hours/days in the cloud |
| **Runs on** | Anthropic's servers | Your computer (sandboxed VM) | Your computer (full access) | Anthropic's cloud infrastructure |
| **Memory** | Per-chat only | Per-project | Persistent across sessions | Persistent + checkpointed |
| **Who controls access** | Anthropic | Anthropic | You — your APIs, your rules | You — via API keys + config |
| **Setup needed** | None | None (built into desktop app) | Install + configure | API key + agent definition |
| **Best for** | Quick tasks | Daily knowledge work (80%) | Reusable systems for teams | Long-running / overnight jobs |
| **You learned this in** | — | Your Cowork training | Today's workshop | Today (intro) |

**SPEAK (Tina, 4 min):**
> Now — Claude.ai, Cowork, Claude Code, Console. Four names. Let me sort them out, because they all use the **same brain.** Same Sonnet, same Opus. The model is identical.
>
> The difference is the **harness** — how much structure, tools, and autonomy you wrap around that brain.
>
> **Claude.ai** — you ask a question, you get an answer. No memory, no tools, no files. It's a conversation. Everyone starts here. If you've ever used claude.ai in your browser, that's this.
>
> **Cowork** — this is where you are now. It's the Claude desktop app. You've been using it for 3 weeks, so let me name what you already have — because it's more than you think:
>
> - **Local file access** — unlike Claude.ai where you upload files (20 files max, 30MB each), Cowork reads directly from your computer. No limits. It delivers ready-to-use files straight to your folder.
> - **Skills** — reusable workflows you can trigger with one click. Some of you have already built these.
> - **Memory** — every time you tell Cowork "remember this," it saves to local files (claude.md, memory.md). The more you teach it, the better it gets at working the way you want.
> - **Connectors** — Gmail, Google Drive, Notion, Calendar. Cowork can read from and work inside tools you already use.
> - **Scheduled tasks** — set a workflow to run daily. Like inbox triage every morning.
> - **Safety** — it runs inside a sandboxed virtual machine. Claude can only access folders you explicitly grant.
>
> These capabilities **compound**. File access + connectors + memory + skills = you can build something like "every Monday, pull my team's weekly updates from Drive, standardize the format, and draft a consolidated report." That's powerful. For 80% of daily knowledge work, Cowork is the right tool.
>
> **Your immediate next step — do this today or tomorrow:**
>
> 1. **Do the work manually** with Cowork. Go back and forth. Ask it to draft a report, an email, a brief.
> 2. **Give feedback.** "Too dense. Lead with metrics. Keep it under 300 words." Edit the output yourself.
> 3. **Tell Cowork to remember.** It saves your corrections to memory.md. Next time, it won't make those mistakes.
> 4. **Tell Cowork: "reverse-engineer this into a skill."** It creates a reusable workflow from what you just did.
> 5. **Install the skill.** One click. Now it's repeatable.
> 6. **Schedule it.** Set it to run daily or weekly. Inbox triage every morning. Weekly report every Friday.
>
> That's Cowork at its maximum. Skills from experience, not templates. Teach it by doing, then automate what works.
>
> **But here's where you'll hit the ceiling:**
>
> - **Skills can't enforce rules.** You can write "never use the word synergy" in a skill. Claude might still use it on the 30th run. There's no guarantee.
> - **Memory drifts.** On long conversations, claude.md and memory.md compete with thousands of tokens of conversation history. Your instructions get drowned out — that's context rot, and we'll explain exactly why in a few minutes.
> - **Connectors are pre-built.** You can connect Gmail and Drive, but you can't connect your internal booking API or a custom database. You're limited to what Anthropic has built.
> - **Scheduled tasks are single-person.** There's no version control, no team coordination. Your colleague can't see or reuse your workflows.
> - **No quality gates.** If a scheduled task produces a bad report at 6am, there's nothing stopping it from sending that report. No validation, no human-in-the-loop enforcement.
>
> These aren't flaws — they're design boundaries. Cowork is a personal assistant. When you need enforcement, specialization, and team coordination, you need the enterprise layer.
>
> **Claude Code** — same brain, but now it has a full operating system. It runs in your terminal with full access to your computer. Everything Cowork has, plus: rules that can't be ignored, hooks that enforce quality automatically, custom agents that specialize, version control so the whole team shares one system, and persistent memory across sessions. More power, more control, more efficiency — but requires setup.
>
> Here's the metaphor: **Cowork is WhatsApp. Claude Code is Slack.** Same messages underneath, different operating system on top. WhatsApp is great for 1-on-1. But try running a 25-person operation through it.
>
> **Console** (platform.claude.com) — this is the builder's dashboard. You don't chat with Claude here. You configure, test, and deploy. This is where your engineering team or your Superuser HQ partner configures Managed Agents — the ones that run overnight on Anthropic's cloud without your laptop open. It also has a prompt playground for testing prompts across different models, evaluation tools, and usage monitoring. You don't need Console today, but knowing it exists means you can ask for the right things when you're ready to scale.
>
> The key distinction: **Cowork is optimized for completing tasks. Code is optimized for building systems. Console is optimized for deploying agents at scale.** And the most powerful capabilities — tool use, agents, persistent memory, custom rules — ship to Code first, then trickle down to Cowork later.
>

---

## SLIDE 6: The Common Problem — Smart But Unreliable

**VISUAL:** Spectrum diagram:
- Left end: "n8n / Zapier" — ✅ Reliable, ❌ Can't think
- Right end: "Claude (any interface)" — ✅ Can think, ❌ Drifts from rules
- Center (highlighted): "Claude Code + harness" — ✅ Can think + ✅ Stays reliable
- Bottom: "How do you get the thinking WITHOUT the chaos?"

**SPEAK (Tina, 5 min):**
> So here's the problem this whole workshop solves. You've now seen both sides.
>
> **n8n side: deterministic.** Reliable, predictable. But can't think.
>
> **Claude side: probabilistic.** Can think brilliantly. But doesn't always follow the rules. You tell it "never use the word synergy" and it'll use it on the 47th run. You tell it "always verify data before writing" and on run 23, it skips verification and makes up a number that looks plausible.
>
> This isn't a bug. It's the nature of language models. They're pattern-matchers, not rule-followers. The more context they accumulate, the more they drift from your instructions.
>
> [Tina personal bridge — the real story]:
>
> Let me tell you what happened to us. We built a skill called `prospect-audit-v2` — a 1,800-line skill that runs 8 phases of data collection, scoring, and report generation. SEO audits for prospects. It pulled data from 5 APIs, analyzed competitors, scored against rubrics, and generated a 20-page HTML report.
>
> And then it shipped a report to a client with fabricated numbers. The agent said a company ranked #1 for a keyword. The real rank was #5. It said a brand had "zero defensive content." The brand actually had a 50-question FAQ page.
>
> Why? By Phase 7, the agent had accumulated thousands of tokens of API responses, and the rules we wrote so carefully were *drowned out*. The instructions — "never fabricate data," "always cross-reference" — were competing with 20,000 tokens of raw output. The LLM didn't "decide" to lie. It just... drifted.
>
> We had to rewrite client reports. **The skill wasn't the problem. The architecture was.**
>
> v3 fixed it by splitting the monolith into isolated agents — one that only collects data, one that only scores — with Python validation scripts between them that CANNOT be hallucinated past. Deterministic gates inside a probabilistic system.
>
> That's the insight: **you need BOTH.** n8n's reliability + Claude's intelligence. That combination — probabilistic thinking wrapped in deterministic guardrails — that's what the harness gives you.
>
> | What you already know | Strength | Weakness |
> |----------|----------|----------|
> | n8n / Zapier (your automation workshop) | Reliable, predictable | Can't think, can't adapt |
> | Cowork (your Cowork training) | Can think, reason, write | Drifts from instructions, fabricates under pressure |
> | Claude Code + harness (today) | Thinking + reliability | Requires building the system — that's what we're here to learn |

---

## SLIDE 7: "Now let me show you the answer"

**VISUAL:** Single line in large text:
> "Let me show you."

**SPEAK (Tina → hand off to Yaohong, 1 min):**
> I could explain it. But that would be Cowork thinking — talking about something. Claude Code is about showing you.
>
> Yaohong is going to do something right now that Cowork literally cannot do. He's going to have Claude operate a computer — chain multiple tools, write files, build something real — live, in the terminal. Watch.

---

## SLIDE 8: DEMO 1 — "Code Does What Cowork Can't" (Yaohong)

**PURPOSE OF THIS DEMO:** Not about a specific API. It's about showing that Claude Code operates your computer — files, terminal, tools, multi-step actions — while Cowork can only chat. Pick ONE of these options based on what Yaohong can prep:

**OPTION A — Multi-tool pipeline (safest, no API needed):**
> Yaohong opens Claude Code. Says: "Research Marriott Indonesia's recent hotel openings, save findings to a file, then cross-reference with Google Trends data, and produce a one-page competitor brief." Claude searches the web, writes files, reads them back, chains 4 tools in one go. Cowork can chat about Marriott. Code builds a deliverable.

**OPTION B — MCP demo with Google Sheets (if connected):**
> Yaohong says: "Pull our partner tracking sheet from Google Sheets, find all partners with >10% booking decline, and draft a re-engagement email for each." Claude reads real data from Sheets via MCP, analyzes it, writes personalized emails. Cowork has Sheets connector but can't chain analysis + email drafting + file saving.

**OPTION C — Build a tool live (most impressive, needs confidence):**
> Yaohong says: "Create a simple web page that shows our top 5 hotel partners with their logos and stats." Claude writes HTML + CSS, opens it in a browser — a working tool built in 2 minutes. Cowork cannot create files on your computer.

**VISUAL:** Live terminal screen (Yaohong's laptop projected)

**SPEAK (Yaohong, 7 min):**
> [Yaohong runs the chosen demo]
>
> What you just saw: Claude didn't just answer a question. It operated your computer — searched, wrote files, read data, chained multiple steps, and produced a deliverable. Cowork can do one thing at a time in a chat window. Code orchestrates.

**NOTE:** This is the "gap" moment. Let it land. The audience should feel "wait — it can DO that?" Don't rush to explain.

---

## SLIDE 9: Why that matters

**VISUAL:** Two-column comparison
- Left: "Cowork" — Pre-approved connectors. Anthropic decides what Claude can access.
- Right: "Claude Code" — Open protocol (MCP). YOU decide what Claude can access. Your APIs, your databases, your tools.

**SPEAK (Tina, 3 min):**
> What Yaohong just showed you is the bridge. The bridge between "AI that helps me write" and "AI that helps me operate."
>
> In Cowork, Claude can only talk to tools Anthropic has pre-approved. In Code, there's something called MCP — Model Context Protocol. Raymond calls these "superpowers for your AI" — and that's not hype. Think of it as a USB port. You can plug in Google Sheets, Gmail, HubSpot, Notion, Slack — and your own internal APIs. Like what Yaohong just did.
>
> [Job bridge — Sales]: For sales, imagine pulling a partner's latest booking data, their contract terms, and their last 3 meeting notes — all in one command, before your call. That's what MCP enables.
>
> [Job bridge — Content]: For content, imagine Claude pulling your blog performance data from Analytics AND your keyword rankings from Ahrefs, then drafting next month's content plan. Two data sources, one workflow.
>
> [Job bridge — Marketing]: For marketing, imagine Claude pulling campaign performance from your ad platform, cross-referencing with CRM data, and generating a weekly performance brief — automatically, every Monday morning.
>
> That's what "beyond Cowork" means. Let's learn the system that makes it possible.

---

# ACT 2 — THE SYSTEM (25 min)
*Purpose: Teach vocabulary. The 8 building blocks + folder anatomy. This is the "learn the language" act.*

---

## SLIDE 10: The Harness — The Answer to "Smart But Unreliable"

**VISUAL:** Left side: brain icon labeled "The Model (same for everyone)." Right side: building block icons surrounding the brain, labeled "The Harness (what makes it yours)." Below: a directory tree showing a real `.claude/` folder. Subtitle: "The term 'agent harness' was popularized by Martin Fowler and Aakash Gupta ('2025 was agents, 2026 is agent harnesses'). The concept: the model is commodity, the harness is moat."

**SPEAK (Tina, 5 min):**
> So why can Claude Code do what you just saw — and Cowork cannot?
>
> It's not a smarter Claude. It's the same model. Same brain.
>
> The difference is something called the **harness**. Understanding this one concept will change how you think about AI tools.
>
> Imagine you hire the smartest person in the world. Genius-level. but with limited memory. But you drop them at a desk with no onboarding doc, no playbook, no access to your CRM, no knowledge of your customers, and nobody checking their work. What happens? They're smart — but they guess. They make mistakes. They can't access what they need. They have no memory of yesterday.
>
> Now imagine you give that same person: a detailed onboarding document. A memory system. Playbooks for every major task. Access to your actual tools — analytics, CRM, email. Specialized teammates they can delegate to. Clear boundaries on what they can and can't do. And automatic quality checks that run before and after every action.
>
> Same person. Completely different results.
>
> That whole support system — everything except the person's brain — that's the harness.
>
> The AI model is the brain. The harness is everything else — the tools, the memory, the rules, the safety checks. **The brain is the same for everyone. The harness is what makes it yours.**
>
> [Tina shows her real directory on screen]:
>
> Let me show you what a real harness looks like. This is my actual setup — not a demo:
>
> ```
> ~/.claude/
> ├── CLAUDE.md                  ← constitution (communication style, visual verification, scraping rules, MCP, memory protocol)
> ├── settings.json              ← permissions, 5 hook categories, status line, plugins
> ├── hooks/
> │   └── memory-extract.sh      ← auto-saves learnings at end of each session
> ├── agents/                     ← 2 global agents (deep-researcher, hermeneutic-thinker)
> ├── commands/                   ← 60+ slash commands (/linkedin-writer, /prospect-audit, /chief-of-staff...)
> └── skills/                     ← 70+ skills (content-production, bookkeeping, aeo-audit, n8n-expert...)
>
> ~/novastacks/.claude/
> └── agents/                     ← 15 project-level specialists
>     ├── linkedin-writer.md      ← writes posts, learns from past rejections
>     ├── chief-of-staff.md       ← tracks leads, preps meetings, sends emails
>     ├── marketing-data-analyst.md ← diagnoses traffic drops, creates dashboards
>     ├── content-writer.md       ← executes briefs in any client's voice
>     ├── n8n-specialist.md       ← builds and debugs n8n workflows
>     └── ... 10 more
> ```
>
> My CLAUDE.md is deliberately short — 90 lines. It starts with "Be brutally honest. Prioritize truth over comfort." Then mandatory rules: always screenshot-verify visual work, always use vision-first scraping. Then MCP service instructions for Google Workspace, Analytics, Ahrefs, HubSpot, DataForSEO. Then memory and skill creation protocols. Short, imperative, trigger-heavy — that's what makes a good constitution.
>
> My `settings.json` has 5 hook categories:
> - **SessionStart (compact):** reminds Claude of critical context after memory compaction
> - **PreToolUse (Edit/Write):** blocks any write to `.env`, credentials, or secrets files
> - **PostToolUse (Edit/Write):** auto-builds CSS for web projects + forces markdown coherence checks
> - **Notification:** macOS ping when Claude needs attention
> - **Stop:** two hooks — (1) macOS notification with open task count, (2) `memory-extract.sh` auto-scans session for lessons worth saving
>
> 60 commands. 70 skills. 15 project agents. 5 hook categories. One person built this over 3 months — not an engineering team.
>
> **The brain is the same for everyone. The harness is what makes it yours.**
>
> What we're about to do is break this down into its building blocks — so you understand each piece and can start building your own.

---

## SLIDE 11: Personal Capabilities vs Enterprise System

**VISUAL:** Two columns:
- Left: "Cowork — Personal" — skills, memory, connectors, scheduled tasks
- Right: "Code — Enterprise" — + hooks, agents, rules, commands, git, permissions
- Bottom: "Cowork has capabilities. Code has a system."

**SPEAK (Tina, 3 min):**
> Cowork is powerful. You already have skills, memory, connectors, scheduled tasks. That's a lot. So what does Code actually add?
>
> | What you have in Cowork | What Code adds on top |
> |---|---|
> | Skills (reusable workflows) | + **Commands** — one-line shortcuts that trigger workflows |
> | Memory (claude.md, memory.md) | + **PROGRESS.md** — state tracking for multi-session work |
> | Connectors (Gmail, Drive, Notion) | + **MCP** — open protocol, connect ANY tool, your own APIs |
> | Scheduled tasks | + **Hooks** — guaranteed enforcement that CAN'T be skipped |
> | Personal instructions | + **CLAUDE.md as constitution** — team-wide, version-controlled |
> | — | + **Agents** — dedicated specialists with their own tools and cost tier |
> | — | + **Rules** — context guardrails that load only when relevant |
> | — | + **Git** — version control, branches, team coordination |
> | — | + **Permissions** — allow/deny lists for what Claude can touch |
>
> Cowork's capabilities are **personal** — they live on your machine, serve one person, and rely on Claude following instructions voluntarily. Code's capabilities are **systemic** — they enforce behavior, specialize agents, coordinate teams, and guarantee quality through code, not trust.
>
> That's the difference. Not more features. A different layer: **enforcement, specialization, version control, team coordination.**
>
> Here's the philosophy — write this down, it's the most important frame of the day:
>
> | Piece | Role | One-liner |
> |-------|------|-----------|
> | **CLAUDE.md** | The Constitution | What Claude must always do, without exception. |
> | **Skills** | The Procedures | How to execute. Detailed, step-by-step, loaded on demand. |
> | **Hooks** | The Guarantees | Enforcement that absolutely cannot be skipped. |
> | **MEMORY.md** | The Learnings | What was discovered, mistakes caught, decisions made. |
> | **Agents** | The Specialists | Dedicated team members with their own role and tools. |
> | **Rules** | The Guardrails | Standards that load only when relevant files are touched. |
> | **Commands** | The Shortcuts | One-liners that trigger entire workflows. |
> | **PROGRESS.md** | The State | Where we are. What's done, what's next, what's blocked. |
>
> Constitution. Procedures. Guarantees. Learnings. State. Specialists. Guardrails. Shortcuts. That's the harness. That's what turns personal capabilities into a reliable system.
>
> But before we go through each piece — I need to explain the ONE constraint that makes ALL of these necessary.

---

## SLIDE 12: The Context Window — Why Claude "Forgets"

**VISUAL:** Use Anthropic's official context window diagram (source: https://platform.claude.com/docs/images/context-window.svg). Show the diagram with progressive token accumulation across turns. Add annotations in terracotta for the key insight.

Simplified version for Gamma slide:
```
Turn 1:  [User message] [Claude response]              ← 2% used
Turn 2:  [Turn 1 + User msg] [Claude response]         ← 8% used
Turn 3:  [Turn 1+2 + User msg] [Claude response]       ← 18% used
...
Turn 15: [ALL previous turns + msg] [Claude response]  ← 75% used ⚠️
Turn 20: [ALL previous turns + msg] [Claude response]  ← 95% used 🔴 CONTEXT ROT
```

Key callout box: "As token count grows, accuracy and recall DEGRADE. Anthropic calls this 'context rot.' This is why your output gets weird on long conversations."

**SPEAK (Tina, 4 min):**
> Before we dive into each building block, I need to explain the ONE thing about Claude that affects everything else. If you don't understand this, you'll think Claude is broken. It's not. It's a design constraint.
>
> It's called the **context window.** Think of it as Claude's working memory — like a whiteboard. Everything Claude can see when generating a response has to fit on this whiteboard. Your instructions, the conversation history, any files it read, its own responses — ALL of it.
>
> How big is the whiteboard? For current models, it's up to 1 million tokens. That sounds like a lot. But here's the thing — **it fills up fast.**
>
> [Show the diagram]
>
> Look at this. Turn 1: you send a message, Claude responds. Tiny. Turn 2: Claude has to carry forward ALL of Turn 1 plus your new message. Turn 3: ALL of Turn 1 and 2, plus your new message. It's additive. Every turn, the whiteboard gets more crowded.
>
> By Turn 15 or 20 — which is a normal working session — you've used 75-95% of the whiteboard. And here's the critical insight: **as the whiteboard fills up, Claude's accuracy drops.** Anthropic calls this "context rot." It's not that Claude gets dumber. It's that the instructions you gave at the beginning are now competing with thousands of lines of conversation, tool outputs, and accumulated data. The signal gets drowned by noise.
>
> **This is why your Cowork output sometimes gets weird.** You start a project, give clear instructions, and for the first 10 messages everything is great. By message 25, Claude starts forgetting your brand voice. By message 40, it's making things up. That's context rot.
>
> Now you understand why the v2 prospect audit failed. By Phase 7, the agent had accumulated 20,000+ tokens of API responses. Our scoring rules — written at the very beginning — were drowning at the bottom of a very crowded whiteboard.
>
> So what do you do about it? Three things:
>
> 1. **Keep instructions short and imperative.** That's why CLAUDE.md should be 90 lines, not 900. Every token in your constitution competes with everything else.
> 2. **Load skills on demand.** Don't put your entire playbook in the constitution. Put procedures in skills that load only when needed — that keeps the whiteboard clean.
> 3. **Split long workflows into isolated agents.** Each agent gets a fresh whiteboard. That's why v3 works and v2 didn't.
>
> Every building block we're about to learn — CLAUDE.md, skills, agents, hooks — is partly a response to this constraint. The harness isn't just about giving Claude capabilities. It's about **managing its working memory** so the right instructions are in context at the right time.
>
> That's the mental model. Now let's go through each piece — starting with what you already know.

---

# — GROUP A: FOUNDATIONS (What You Know, Deepened) —

## SLIDE 13: Skills & Memory — From Cowork to Code

**VISUAL:** Two columns showing the upgrade path:
- Left: "Cowork" — skills (manual install), memory (claude.md, memory.md per folder)
- Right: "Code" — skills (auto-invoke, shared via git) + commands (shortcuts) + PROGRESS.md (state)

**SPEAK (Tina, 4 min):**
> Let's start with what you already know. You've built skills in Cowork. You've used memory. Let me show you how Code takes those same concepts further.
>
> **Skills in Code auto-invoke.** In Cowork, you pick a skill manually. In Code, skills fire on their own. Here's how:
>
> 1. When you start a session, Claude Code scans your `skills/` folders
> 2. It reads the `name:` and `description:` fields from each skill file — just the header, not the full content
> 3. You type a normal message — "write a blog post about hotel distribution trends"
> 4. Claude reads your message against all the skill descriptions
> 5. Match found → Claude auto-loads the full skill and follows the procedure
> 6. You never typed a command. It just knew.
>
> This means **the `description:` field is the most important line in your skill file.** "Use when writing blog content for any client" — good. "Content writing tool" — useless. Claude never triggers it.
>
> **Commands** are new — one-liner shortcuts. `/partner-report Marriott` triggers a skill that pulls data, analyzes, formats, saves. You type 3 words, Claude does 15 minutes of work. Skills are the cookbook. Commands are the speed-dial buttons.
>
> And here's a practical rule from Raymond: "Create a skill when you've repeated the same instruction 3 or more times." Third time you type it, make it a skill.
>
> **Memory in Code persists across sessions.** In Cowork, claude.md and memory.md live in your folder. In Code, they're version-controlled and shared with the team via git. Plus you get **PROGRESS.md** — state tracking. "What's done, what's next, what's blocked." So when you come back tomorrow, Claude knows exactly where you left off.
>
> And skills in Code are shared via git — not ZIP upload. One person improves a skill, the whole team gets the update.
>
> [Job bridge — Sales]: `/call-prep Hilton Jakarta` — pulls meeting notes, recent booking data, contract status, generates a one-page brief. 30 seconds instead of 45 minutes of tab-switching. Or just say "prep me for the Hilton call" — Claude finds the skill automatically.
>
> [Job bridge — Content]: Say "write a blog post about hotel distribution trends" — the blog-draft skill fires on its own because the description matches. You don't need to remember the command name.

---

## SLIDE 14: Connectors → MCP — Same Idea, More Power

**VISUAL:** Two columns:
- Left: "Cowork Connectors" — Gmail, Drive, Notion, Calendar (pre-built, toggle on/off)
- Right: "Code MCP" — same tools + your internal APIs, custom databases, any tool with an API

**SPEAK (Tina, 3 min):**
> In Cowork, you connect Gmail, Drive, Notion, Calendar. Toggle on, Claude can read your emails, pull from Drive, write to Notion. You've done this.
>
> In Code, the same concept is called **MCP — Model Context Protocol.** Think of it as a USB port. Cowork gives you 4 pre-built USB devices. MCP lets you plug in ANYTHING — your internal booking API, your partner database, Ahrefs, HubSpot, Google Analytics, DataForSEO, Slack. If it has an API, you can connect it.
>
> The difference:
>
> | | Cowork Connectors | Code MCP |
> |---|---|---|
> | **What's available** | Gmail, Drive, Notion, Calendar | Anything with an API |
> | **Who decides** | Anthropic builds them | You configure them |
> | **Your internal tools** | ❌ Not possible | ✅ Connect your own APIs |
> | **Multiple tools at once** | Yes, but each is separate | Yes, and Claude chains them in one workflow |
>
> [Job bridge — Sales]: In Cowork, you can read partner emails from Gmail. In Code with MCP, Claude pulls booking data from your internal system, cross-references with the partner's email history, checks their contract terms, and drafts a re-engagement plan — all in one command.
>
> [Job bridge — Marketing]: In Cowork, you connect Google Drive. In Code with MCP, Claude pulls campaign performance from your ad platform, cross-references with CRM data from HubSpot, and generates a weekly brief — automatically, every Monday morning.
>
> MCP is where n8n and Claude converge. Remember Slide 4? n8n connects tools but can't think. Claude thinks but can't connect your internal tools. MCP gives Claude the connections. The harness gives it the reliability. That's the combination.

---

# — GROUP B: ENTERPRISE LAYER (What Code Adds) —

## SLIDE 15: The Constitution — CLAUDE.md for Teams

**VISUAL:** Two cards side by side
- Left: "Cowork: Personal Instructions" — each person writes their own, 25 people = 25 versions
- Right: "Code: CLAUDE.md" — one constitution, version-controlled, whole team shares it via git

**SPEAK (Tina, 3 min):**
> In Cowork, each person writes their own instructions. 25 people, 25 versions. Nobody knows what anyone else told Claude. In Code, there's ONE CLAUDE.md the whole team shares — via git. Update it once, everyone gets it.
>
> **CLAUDE.md is your Constitution.** Not a suggestion box — a constitution. Short, imperative, trigger-heavy. Every rule exists because something went wrong without it.
>
> [Tina shows real CLAUDE.md on screen]:
>
> Here's what my actual CLAUDE.md starts with — the first 6 sections:
> 1. **Communication Style** — "Be brutally honest. Prioritize truth over comfort."
> 2. **Visual Verification** — "Never score formatting as PASS based on API success alone. Screenshot and verify." Born from a bug where Google Docs headings bled into body text.
> 3. **Web Scraping** — "Use screenshots for extraction, NEVER CSS selectors." We got burned by selectors returning "Sponsored" instead of real data.
> 4. **Date Awareness** — "Always check today's date. Do NOT assume the year." Claude kept writing "2025" in 2026 reports.
> 5. **Memory Save Protocol** — Where and how Claude saves things it learns.
> 6. **MCP Integrations** — Which tools are connected and how to use each one.
>
> Notice: every rule came from a real mistake. The CLAUDE.md isn't aspirational — it's battle-tested.
>
> **MEMORY.md** is Claude's journal. "Blog posts over 2000 words rank better." "VP prefers bullet-point summaries." "Campaign naming: YYYYMM-channel-topic." In Cowork, this lives in your local folder. In Code, it's tracked in git so the whole team benefits from what anyone learns.

---

## SLIDE 16: Agents + The Agent Zoo

**VISUAL:** Two cards side by side
- Agents — "The **Specialists**. Dedicated team members with own role, tools, cost tier."
- Rules (with paths:) — "The **Context Guardrails**. Domain standards that load only when relevant."

**SPEAK (Tina, 4 min):**
> This is the biggest unlock. Cowork doesn't have agents. Code does.
>
> **Agents** are specialists you delegate to. Think of it like hiring consultants — you don't bring a $500/hour strategist to proofread emails. You bring a $50/hour editor. In Claude Code, each agent has its own role, its own tools, and its own cost tier (Haiku for cheap work, Sonnet for thinking, Opus for high-stakes).
>
> **Rules** are guardrails that only activate when relevant. A `blog-voice.md` rule with `paths: "content/blog/**"` — loads ONLY when Claude touches blog files. An `outreach-tone.md` rule loads only for sales emails. 5 minutes to write. Saves hundreds of "remember to..." reminders.
>
> Now let me show you real agents from my setup:
>
> ```
> novastacks/.claude/agents/
> ├── linkedin-writer.md       ← writes posts, has PERSISTENT MEMORY
> │                               (remembers past rejections, learns what performs)
> ├── chief-of-staff.md        ← tracks leads, preps meetings, sends emails
> │                               (tools: Gmail, Google Sheets, web search)
> ├── marketing-data-analyst.md ← diagnoses traffic drops, creates dashboards
> │                               (tools: Google Analytics, Search Console, Ahrefs, DataForSEO)
> ├── content-writer.md        ← executes briefs in any client's voice
> │                               (tools: web search, file read/write)
> ├── web-developer.md         ← builds and deploys website changes
> └── ... 10 more specialists
> ```
>
> The linkedin-writer agent gets BETTER over time. It checks rejections.md before writing — patterns that got killed and why. It checks wins.md — patterns that performed. If a pattern was rejected 2+ times, it won't use it. That's not possible in Cowork — there's no persistent agent memory.
>
> And notice: different tools for different jobs. The analyst has Analytics, Ahrefs. The writer has web search and files. You don't give the writer access to your analytics dashboard. That's the agent model.

---

## SLIDE 17: The Agent Zoo — 5 Types Sorted

**VISUAL:** 5-row taxonomy table with icons

**SPEAK (Tina, 5 min):**
> OK — "agents" is the most overloaded word in AI right now. Everyone calls everything an agent. Let me sort it out. There are 5 different things people mean, and they're all different:
>
> **1. Built-in sub-agents (you already have these)**
> Claude Code ships with 3: `Explore` (searches your codebase fast), `Plan` (writes step-by-step plans), and `general-purpose` (does research tasks). You never built these. Claude calls them automatically when it needs to. You've probably already seen Claude say "I'll use the Explore agent to find that file" — that's a sub-agent.
>
> A sub-agent is just: Claude spawning a second Claude to handle a piece of work, then getting the result back. Like asking a colleague to look something up while you keep working.
>
> **2. Your custom agents (you build these)**
> These live in `.claude/agents/`. I have 15 of them. Each is a markdown file with a role, tools, and instructions. When I type `/writer` or `/linkedin-writer`, Claude reads that agent file and becomes that specialist.
>
> Let me show you the difference between two of mine — because this is where it gets interesting:
>
> | | **writer** (content-writer.md) | **linkedin-writer** (linkedin-writer.md) |
> |---|---|---|
> | **Scope** | Any client, any content type | Novastacks LinkedIn only |
> | **Tools** | Bash, Read, Write, Edit, Glob, Grep, WebSearch | Read, Write, Edit, WebFetch, WebSearch (NO Bash, NO Glob) |
> | **Memory** | Generic project memory | Has its own memory folder with `rejections.md`, `wins.md`, `preferences.md` |
> | **Learning** | Follows brand voice from CLAUDE.md | Learns from EVERY session — remembers what I delete, what performs, what I edit |
> | **Behavior** | Adapts to whichever client it's called from | Always writes as Tina, always checks what got rejected last time |
>
> The writer is a generalist you can point at any client. The linkedin-writer is a specialist that gets better over time. Yesterday it wrote 4 drafts of a post. I rejected 3. It saved WHY I rejected each one. Next time, it won't make those mistakes. That's the difference between an agent that follows instructions and an agent that learns.
>
> **3. Marketplace/plugin agents (installed from a store)**
> These come from Anthropic's plugin marketplace or GitHub. I have `superpowers`, `document-skills`, `frontend-design`, `telegram` installed. They add capabilities — skills, commands, agents — that other people built and you install with one click. Think of them like apps on your phone. You didn't build them, but they extend what your system can do.
>
> **4. Managed Agents (Anthropic-hosted, run without you)**
> This is brand new from Anthropic — and it changes the game. Right now, when you use Claude Code, it runs on YOUR laptop. You have to keep your terminal open. If you close your laptop, the agent stops. Managed Agents fix that.
>
> Managed Agents are built on 4 concepts. Let me map them against what you already know from local agents — because the ideas are the same, just the infrastructure changes:
>
> | Concept | Managed Agent (cloud) | Local Agent (your laptop) |
> |---------|------|------|
> | **Agent** | Defined in Console: model, system prompt, tools, MCP servers, skills | Defined in `.claude/agents/` as a markdown file |
> | **Environment** | Cloud container: packages pre-installed, network rules, sandboxed | Your computer: whatever you have installed locally |
> | **Session** | Running instance on Anthropic's servers — runs for hours/days, survives laptop shutdown | Running instance in your terminal — stops when you close it |
> | **Events** | Messages streamed between your app and the cloud agent via API | Direct conversation in your terminal |
>
> So when you define a local agent like `/linkedin-writer`, you're doing the same thing — specifying a model, a system prompt, tools, and skills. The difference? Local agents run on your machine and stop when you close the terminal. Managed Agents run on Anthropic's infrastructure and keep going.
>
> The infrastructure difference matters. Managed Agents get: built-in prompt caching and compaction (remember context rot? Anthropic handles that for you), secure sandboxing, session checkpointing so work isn't lost, and a Console dashboard to watch what the agent is doing in real time. Cost: standard API token rates + $0.08 per session-hour.
>
> For your team, think: "Process all partner booking reports overnight and have a summary ready by 9am." Or: "Run competitive analysis across 50 hotel markets while I sleep." Or: "Generate personalized re-engagement emails for every partner with declining bookings — all 200 of them — and have drafts ready for review." That's Managed Agents.
>
> You don't need this today. But the building blocks we're teaching right now — skills, agents, tools, harness design — are exactly what you'll configure when defining a Managed Agent. The thinking is the same. The infrastructure just scales.
>
> **5. The "agent system" (everything working together)**
> When people say "agent system" or "agentic workflow," they mean ALL of the above orchestrated together. Your main Claude session is the conductor. It delegates to sub-agents (Explore, Plan) automatically. It invokes your custom agents (/writer, /linkedin-writer) when you ask. It uses marketplace plugins for capabilities you didn't build. And eventually, Managed Agents handle the overnight batch jobs.
>
> The harness — the `.claude/` folder — is what connects all of these. Without it, they're separate tools. With it, they're a system.
>
> [Show visual]:
> ```
> YOU (typing in terminal)
>  └── Claude Code (main session)
>       ├── Built-in sub-agents (Explore, Plan) ← auto-delegated
>       ├── Your custom agents ← you invoke with /command
>       │    ├── /writer (generalist, any client)
>       │    ├── /linkedin-writer (specialist, learns)
>       │    ├── /chief-of-staff (business ops)
>       │    └── /analyst (data investigation)
>       ├── Marketplace plugins ← installed from store
>       │    ├── superpowers (workflow patterns)
>       │    ├── document-skills (PDF, DOCX, XLSX)
>       │    └── telegram (chat integration)
>       └── Managed Agents ← Anthropic cloud (Console)
>            └── overnight batch jobs, scheduled tasks, scale ops
> ```
>
> Clear? Good. Now let's talk about the safety layer that keeps all of this from going sideways.

---

## SLIDE 18: Hooks + Permissions — The Safety Layer

**VISUAL:** Two cards side by side
- Hooks — "The **Guarantees**. Harness-level enforcement. Absolutely cannot be skipped."
- Permissions — "The **Walls**. Allow/deny lists. What Claude can and can't touch."

**SPEAK (Tina, 5 min):**
> This pair is what gets VP approval.
>
> **Hooks** are the only thing that GUARANTEES something happens. You can write "always check brand guidelines before publishing" in CLAUDE.md. Claude might forget. You can put it in a skill. Skills don't always load. A hook is a tripwire — it's a script YOUR system runs, not Claude. Before Claude is allowed to run `git commit`, your system runs a lint check. If it fails, the commit is blocked. No negotiation.
>
> Let me give you three real examples from my consultancy:
>
> 1. **PostToolUse hook on Edit:** Every time Claude edits a markdown file, a hook automatically re-reads the full file and checks for broken references, formatting issues, or contradictory info. Claude doesn't remember to do this — the system forces it. We caught 30+ document issues in the first month that would've gone to clients.
>
> 2. **PreToolUse hook on Write:** Before Claude creates any new file, the hook checks: is this a sensitive path? Is it a .env file? A credentials file? If yes, blocked. This isn't a prompt instruction Claude might ignore — it's a wall.
>
> 3. **Stop hook:** When Claude finishes a long task, a hook can ping Slack with a one-line summary: "Done: drafted Q2 partner report for Marriott, saved to /reports/." I'm in a meeting, the agent finishes, I get a ping. That's hooks.
>
> **How to create a hook:** You write a small shell script in `.claude/hooks/`, then register it in `settings.json` with a matcher pattern like `Bash(git commit *)` or `Write(*.md)`. The matcher tells the system WHEN to fire. The script tells it WHAT to do. That's it — two pieces.
>
> **Permissions** are the keycard system. An allow/deny list committed to git. Sales can read CRM data but not bulk-send emails. Content can push to staging but not production. Nobody can `rm -rf` or force-push. Different access for different roles.
>
> [Job bridge — Marketing]: This is the answer to your VP's question: "How do we let 25 people use AI agents without someone accidentally sending the wrong email to 10,000 customers?" The answer is: permissions deny-list. The agent literally cannot do it.

---

## SLIDE 19: The Folder — How Everything Connects

**VISUAL:** Folder tree with connection arrows showing how hooks work

```
.claude/
├── CLAUDE.md           ← always loaded (the handbook)
├── settings.json       ← the control panel (registers hooks + permissions)
│       │
│       ├── hooks: { "PreToolUse": [...] }  ──→  points to scripts in hooks/
│       └── permissions: { "allow": [...], "deny": [...] }
│
├── hooks/              ← shell scripts (the actual code hooks run)
│   └── memory-extract.sh   ← settings.json says WHEN, this says WHAT
│
├── agents/             ← specialists (invoked by Claude automatically or by you)
├── commands/           ← slash-commands (you type /name to trigger)
├── rules/              ← guardrails (loaded by paths: match, not always)
└── skills/             ← procedures (loaded when relevant or invoked)
```

**SPEAK (Tina, 4 min):**
> Here's how everything connects. This is the question people always ask: "If hooks are scripts in `hooks/`, why is there also a `settings.json`?"
>
> Answer: **`settings.json` is the control panel.** It says WHEN something fires — "before any Edit or Write command." The hook script in `hooks/` says WHAT happens — "check if it's a credentials file and block it." Two pieces: the trigger and the action. You need both.
>
> Same for permissions — they live in `settings.json`, not in their own folder. Permissions are a list: "allow Read, Write, Bash. Deny rm -rf, git push --force, sending emails." The list is in `settings.json`.
>
> Everything ELSE gets its own folder: agents, commands, rules, skills. Each is a markdown file. Each is independent. You can have 1 agent or 50. You can have zero rules or 20. The folder grows with your needs.
>
> [NOTE: We already showed Tina's real directory in the harness slide. Here, the point is the CONNECTION between settings.json and hooks — the "wiring."]
>
> **What should be in YOUR CLAUDE.md — best practices:**
> - Your team name and what you do (one paragraph)
> - Tech stack / tools you use (so Claude knows what's available)
> - Brand voice rules (tone, forbidden words, style)
> - Key commands to run (dev server, tests, deploy)
> - Folder structure (so Claude knows where things live)
> - Things Claude should NEVER do (specific to your context)
> - Keep it under 200 lines. If it's longer, move details to Rules files.
>
> And here's the argument for your VP: these are plain text files. If Claude disappears tomorrow, you connect this folder to whatever comes next. Zero vendor lock-in. Your team's operating system isn't owned by Anthropic — it's owned by you.
>
> Michael Silva, an enterprise AI architect, puts it bluntly: "The model is a commodity that gets swapped every six months. The runtime layer — the folder, the permissions, the audit trail — THAT is where the real value accrues." You're not investing in Claude. You're investing in a system that happens to run on Claude today.
>
> And one more thing Raymond taught me: adopt what he calls the "baby mindset." When you're stuck on something in the terminal, don't struggle alone for 30 minutes. Just ask Claude. "How do I do X?" It's sitting right there. The people who learn fastest are the ones who aren't embarrassed to ask obvious questions — because there are no obvious questions when everything is new.

---

## SLIDE 20: Quick check — "Which primitive is this?"

**VISUAL:** Interactive quiz (3 scenarios)
1. "Brand voice guidelines that only load when writing blog posts" → Rules
2. "A safety check that runs before every commit" → Hook
3. "A specialist that researches partners using only web search + read" → Agent

**SPEAK (Tina, 2 min):**
> Quick check before break. I'll describe a scenario, you tell me which primitive.
>
> [Run through 3 scenarios, let audience answer. Reinforce vocabulary.]
>
> If you got 2 out of 3, you now have the vocabulary. Let's take a break, and when we come back, Yaohong is going to build a full pipeline live — from zero to a reusable team workflow in 15 minutes.

---

# ☕ BREAK (10 min)

**NOTE:** During break, Yaohong preps demo environment. Tina circulates, answers questions, gauges energy.

---

# ACT 3 — THE BUILD (25 min)
*Purpose: Show the pattern. A single API call becomes a full pipeline. This is the emotional peak.*

---

## SLIDE 21: "Remember that API call? Now watch what happens."

**VISUAL:** Simple callback visual — the hotel data from Demo 1, with an arrow pointing right: "→ What's next?"

**SPEAK (Tina, 2 min):**
> Before break, Yaohong pulled live hotel partner data from Tiket's API. That was one step. A single data fetch.
>
> Now he's going to do something that will change how you think about workflows forever. He's going to start from that same API call and layer complexity — one step at a time — until it becomes a full pipeline that anyone on this team can run with one command.
>
> Watch the layers. Each one is an "aha."

---

## SLIDE 22-26: DEMO 2 — Build-Up Pipeline (Yaohong)

**VISUAL:** Live terminal. One slide per layer (can show as Yaohong progresses).

### Layer 1: Raw API Call
**SPEAK (Yaohong):** "Remember this? Same API call from before. Hotel partner data."
**Audience feels:** Familiar. Callback to Demo 1.

### Layer 2: Enrich with Context
**SPEAK (Yaohong):** "Now I'm adding web research about this partner. Their recent news, their market position. Two data sources, combined."
**Audience feels:** "Oh, it pulls from multiple places."

### Layer 3: Analyze
**SPEAK (Yaohong):** "Now I ask Claude to analyze. Find trends. Flag issues. Rank by a metric. It's not just fetching — it's thinking."
**Audience feels:** "It's actually reasoning, not just copying."

### Layer 4: Format and Save
**SPEAK (Yaohong):** "Format as a clean report. Save to file. That's a deliverable someone could share."
**Audience feels:** "That's a ready-to-send document."

### Layer 5: Wrap into a Skill
**SPEAK (Yaohong):** "Now the magic. I wrap all 4 steps into a `/partner-report` command. Type it once — the whole pipeline runs. Anyone on the team can use it."
**Audience feels:** "Anyone can run this. I could run this."

---

## SLIDE 27: The Pattern

**VISUAL:** Simple pipeline diagram:
Fetch → Enrich → Analyze → Format → Save → (wrap into command)

**SPEAK (Tina, 3 min):**
> What you just saw is THE pattern. Every agentic workflow has the same shape: fetch data, add context, analyze, format, save. The only things that change are the data sources and the output format.
>
> Raymond demonstrated this exact idea to 20 university professors in Taiwan. His framing: "Focus entirely on content — your teaching, your research, your actual expertise. Delegate everything else to the AI." That's the mindset shift. You are the expert on Tiket's partners, on your market, on your customers. The agent handles the grunt work — the fetching, the formatting, the cross-referencing. You handle the judgment.
>
> And one nuance: not every step in your workflow needs AI. Raymond classifies tasks into three buckets: "no-brain tasks" go to automation tools like n8n or Zapier — no AI needed, just move data from A to B. "Judgment tasks" go to AI agents — analysis, recommendations, writing. "Collaborative tasks" stay in Notion or Sheets — where humans need to see and discuss. The pipeline Yaohong just built? Steps 1 and 4 are "no-brain" (fetch, format). Steps 2 and 3 are "judgment" (enrich, analyze). Step 5 is "collaborative" (the team uses the output). Knowing which is which saves you money and keeps the system reliable.
>
> [Job bridge — Sales]: Fetch partner data from API → enrich with meeting notes → analyze booking trends → format as call prep brief → save to shared drive. `/call-prep Marriott`. Done.
>
> [Job bridge — Content]: Fetch keyword rankings → enrich with competitor content analysis → analyze gaps → format as content calendar → save to Google Sheets. `/content-plan Q3`. Done.
>
> [Job bridge — Marketing]: Fetch campaign performance → enrich with CRM conversion data → analyze ROI by channel → format as weekly brief → save to Slack channel. `/weekly-brief`. Done.
>
> Same pattern. Different inputs. Different outputs. Once you see it, you can design your own.

---

# ACT 4 — HUMAN + AGENT COORDINATION (20 min)
*Purpose: How you and agents work together safely. Safety first (it's part of the system), then git as the coordination layer, then Yaohong's lived experience.*

---

## SLIDE 28: The Safety Envelope

**VISUAL:** Three concentric circles
- Outer: "Permissions" — what Claude CAN'T do
- Middle: "Hooks" — what the system ENFORCES
- Inner: "Rules" — what Claude SHOULD do

**SPEAK (Tina, 3 min):**
> Before we talk about working alongside agents, let's talk about trust. How do you trust an agent not to break things?
>
> Three layers of safety — same stuff we covered in the building blocks, but now as a system:
>
> **Permissions** (outermost) block actions entirely. Claude literally cannot run `git push --force` or send bulk emails. It's not a suggestion — it's a wall.
>
> **Hooks** (middle) enforce checks. Before every commit, run a quality check. After every file write, verify formatting. The system runs these — not Claude.
>
> **Rules** (innermost) guide behavior. "Blog posts should be warm and concrete." Claude follows these — but they're guidance, not enforcement.
>
> The VP question: "How do I know the AI won't go rogue?" Answer: it's blocked by permissions, checked by hooks, and guided by rules. Three layers, all version-controlled, all auditable. This is the safety envelope that makes everything else possible.

---

## SLIDE 29: "Git is the new Notion"

**VISUAL:** Large text: "Git is the new Notion."
Subtitle: "The shared workspace where humans and agents coordinate."

**SPEAK (Tina, 5 min):**
> Now that you trust the safety envelope — how do you actually work alongside agents day-to-day?
>
> Everything we've shown you — the folder, the agents, the pipeline — all of it lives in git. And I know what you're thinking: "git is for engineers."
>
> It's not. Git is Notion with a memory. Here's the translation:
>
> | Git | You already know this as... |
> |-----|---------------------------|
> | `git pull` | Hitting refresh in Google Docs |
> | `git commit` | "Save version" with a note |
> | `git push` | Sharing / publishing |
> | `main branch` | The "published" page |
>
> Five commands. That's all you need. You learned Notion. You learned ClickUp. Git is smaller than both.
>
> The reason git matters with agents: **main branch = the version of truth**. Agents work on branches. You review their work. YOU decide when it lands on main. Without this, you wake up and the "published" version is whatever an agent did at 3am. With it, you're always in control.
>
> [Harness callback]: Remember when I said the harness is what makes Claude yours? The safety envelope + git are the parts that make it *trustworthy*. The model is a commodity that gets replaced every few months. The harness — your rules, your memory, your agents, your permissions, your git workflow — that's the durable asset. It persists even if you swap the model.

---

## SLIDE 30: Yaohong's Real Experience

**VISUAL:** Photo of Yaohong + quote highlight (TBD)

**SPEAK (Yaohong, 7 min):**
> [PLACEHOLDER — Yaohong fills in from personal Slack history]
>
> Suggested structure:
> - "Here's how I actually use agents day-to-day" — 2 concrete examples from Slack
> - "What's worked" — the win that surprised me most
> - "What's been painful" — the honest friction (context loss, over-trusting output, setup pain)
> - "My one recommendation for this room" — the ONE habit to adopt this week
> - "And the one trap to avoid"

---

# ACT 5 — THE MONDAY PLAN (15 min)
*Purpose: Make it actionable. What do they DO this week? Close strong.*

---

## SLIDE 31: Recap in 60 Seconds

**VISUAL:** 5 key takeaways — one per line, large text

1. Automation (n8n) vs Augmentation (Claude). Claude Code combines both — thinking + reliability.
2. Seven building blocks + memory. That's enterprise-safe.
3. One folder (`.claude/`) = your team's AI operating system.
4. Agents are specialists. Skills are procedures. Hooks are enforcement. Permissions are the wall.
5. Git is how you coordinate. Main branch = truth. You always decide what lands.

**SPEAK (Tina, 2 min):**
> [Walk through each line quickly. One sentence per takeaway. No elaboration — they already learned it.]

---

## SLIDE 32: Your Week 1 Checklist

**VISUAL:** Checklist with checkboxes

- [ ] Open your terminal and run `git pull` in the team repo
- [ ] Read the `.claude/CLAUDE.md` file — that's your team's handbook
- [ ] Try one existing command: `/sales-proposal [client name]`
- [ ] Pick ONE task you do weekly that takes > 2 hours
- [ ] Write the baseline: what task, how long, how often, what quality
- [ ] Bring that baseline to the next session — we'll build the skill together

**SPEAK (Tina, 3 min):**
> Six things. All doable this week. The most important one is number 5 — the baseline. Because the baseline is what turns "I think AI is helping" into "I can prove AI is helping."
>
> Write it on paper, in Notion, in a Google Doc — I don't care where. But write it. 90 minutes. That's the investment. And it's the single thing that determines whether your AI project lives or quietly dies.

---

## SLIDE 33: The Ecosystem — Where to Go Deeper

**VISUAL:** Visual map of companion resources (links/QR codes)

- 📖 Reference Guide — full 15-section deep-dive (HTML)
- 🛠 Skills Guide — build your first production skill
- 🔀 Git for Non-Engineers — the full 5-command guide
- 📊 AI Impact Report Template — the one-pager for VPs
- 🧰 Agentic Tools Cheatsheet — what else is out there
- 🌐 OpenClaw — self-hosted agents (for when you outgrow this)

**SPEAK (Tina, 2 min):**
> We've built companion guides for everything we covered today — and things we didn't have time for. They're at this link [show QR]. Read them at your own pace. They're designed as references, not tutorials — scan for what you need.
>
> The most immediately useful one is the AI Impact Report template. That's your weapon for the next VP conversation.

---

## SLIDE 34: Q&A

**VISUAL:** "Questions?" + both speakers' names

**SPEAK (Tina, 5 min):**
> Open floor. Ask anything. "Can Claude do X?" "What about Y?" "What if Z goes wrong?" Yaohong and I are here.

---

## SLIDE 35: Closing

**VISUAL:** Full-bleed closing slide
- "Same brain. Bigger operating system."
- Novastacks AI × Superuser HQ logos

**SPEAK (Tina, 1 min):**
> The best time to start was 3 weeks ago — and you did, with Cowork. The next best time is now. Same brain, bigger operating system.
>
> Thank you. Go build something.

---

# APPENDIX 0 — Trainer Prep Checklist (Before Workshop)

**Tina — before April 20:**
- [ ] Screenshot your real `~/.claude/` directory (agents, skills, rules visible) → for Slide 13
- [ ] Screenshot your CLAUDE.md (first 30 lines showing brand voice, stack, rules) → for Slide 13
- [ ] Prepare 1-min verbal walkthrough of your folder ("here's writer, here's strategist, here's the blog-voice rule...")
- [ ] Confirm: which 2-3 hooks do you actually run? Write the one-liner descriptions for Slide 12
- [ ] Confirm: which personal bridges feel authentic? Mark any in the script that need rewording to match how you'd actually say it
- [ ] Print or have the "Don't say / Do say" table (Slide 26) ready as a handout

**Yaohong — before April 20:**
- [ ] Confirm Tiket internal API access OR have mock endpoint ready with realistic hotel data → critical for Slide 5 (Demo 1)
- [ ] Test the full 5-layer pipeline end-to-end at least twice → for Slides 16-20 (Demo 2)
- [ ] Prepare `/partner-report` skill template (Layer 5) — must work live
- [ ] Prepare fallback: if API is down, local mock server with realistic Tiket hotel data
- [ ] Fill in Slide 24 (personal experience): 2 Slack examples, 1 win, 1 pain point, 1 recommendation
- [ ] Test screen sharing + terminal font size (audience at back of room must read code)

**Both — day of:**
- [ ] Run `git pull` in the demo repo
- [ ] Test projector + screen sharing before audience arrives
- [ ] Have QR code ready for companion resources (Slide 29)
- [ ] Agree on hand-off cues: Tina says "Yaohong, show them" → Yaohong takes over

---

# APPENDIX A — Gamma Slide Construction Notes

## Design Theme: Anthropic-Branded

Use Anthropic's official brand identity to give the deck authority and signal "this is a Claude workshop, built by people who know the platform."

### Color Palette (Anthropic Official)

| Role                   | Color             | Hex       | Where to use                                              |
| ---------------------- | ----------------- | --------- | --------------------------------------------------------- |
| **Primary background** | Warm light        | `#FAF9F5` | All slide backgrounds — the signature Anthropic cream     |
| **Text / dark bg**     | Near-black        | `#141413` | Body text, dark section backgrounds, code blocks          |
| **Secondary text**     | Mid gray          | `#B0AEA5` | Captions, subtitles, less-important labels                |
| **Subtle bg**          | Light gray        | `#E8E6DC` | Card backgrounds, table headers, sidebar fills            |
| **Primary accent**     | Terracotta/orange | `#D97757` | Headings, buttons, highlights, active state, key callouts |
| **Secondary accent**   | Blue              | `#6A9BCC` | Links, secondary highlights, "Code" badges                |
| **Tertiary accent**    | Green             | `#788C5D` | Success states, checkmarks, "done" indicators             |

### Typography

| Role | Font | Fallback | Notes |
|------|------|----------|-------|
| **Headings** (slide titles, section names) | **Poppins** | Arial | Clean, modern, geometric — the Anthropic heading font |
| **Body text** (paragraphs, bullets, notes) | **Lora** | Georgia | Warm serif — gives the "thoughtful" feel Anthropic uses |
| **Code / monospace** | **JetBrains Mono** or `Fira Code` | `Courier New` | For terminal mockups, file paths, code blocks |

In Gamma: set Poppins as "Heading font" and Lora as "Body font" in the theme customizer. If Gamma doesn't support custom fonts, use their closest match (a geometric sans for headings + a serif for body).

### Gamma Theme Setup (Step by Step)

1. **Create new deck** → Choose "Blank" or "Minimal" template
2. **Theme** → Custom colors:
   - Background: `#FAF9F5`
   - Text: `#141413`
   - Accent 1: `#D97757` (terracotta)
   - Accent 2: `#6A9BCC` (blue)
   - Accent 3: `#788C5D` (green)
3. **Fonts** → Heading: Poppins / Body: Lora (or closest available)
4. **Cards** → Set card background to `#FAF9F5`, border `#E8E6DC`
5. **Code blocks** → Background `#141413`, text `#E8E6DC`, prompt highlight `#D97757`

### Design Patterns by Slide Type

**Title/Act dividers (Slides 1, 8, 17, 27):**
- Full-bleed `#141413` dark background
- Title in Poppins white, 48-60pt
- Subtitle in Lora `#B0AEA5`, 18pt
- Thin terracotta accent line below title

**Two-column comparisons (Slides 2, 4, 7):**
- Left column: warm cream `#FAF9F5` background
- Right column: light gray `#E8E6DC` background
- Column headers in terracotta `#D97757`
- Clean divider line between columns

**Concept cards / Building blocks (Slides 9-14):**
- Each card: white `#FFFFFF` background, `#E8E6DC` border, 8px radius
- Card icon/emoji in terracotta circle
- Card title in Poppins 18pt
- Card body in Lora 14pt, `#141413`
- Metaphor callout box: `#E8E6DC` background, Lora italic

**Code/terminal slides (Slides 6, 18-22):**
- Full-width `#141413` dark block
- Code text in `#E8E6DC` (light), JetBrains Mono 14pt
- Prompt (`$` or `>`) in terracotta `#D97757`
- Comments in `#B0AEA5`
- File paths in blue `#6A9BCC`

**Tables (Slides 9, 13, 15):**
- Header row: `#E8E6DC` background, Poppins bold 12pt
- Body rows: alternating `#FFFFFF` / `#FAF9F5`
- Key column (left): Poppins bold
- Value columns: Lora regular
- Accent highlights: terracotta bold for important values

**Quote/statement slides (Slides 4, 5):**
- Centered large text in Poppins 36pt
- Terracotta color for the key phrase
- Rest in `#141413`
- Lots of whitespace — let the statement breathe

**The Agent Zoo hierarchy diagram (Slide 13):**
- Tree structure with nested indentation
- Each level gets a different accent color:
  - You → `#141413` (dark)
  - Claude Code → `#D97757` (terracotta)
  - Sub-agents → `#6A9BCC` (blue)
  - Custom agents → `#D97757` (terracotta, lighter tint)
  - Marketplace → `#788C5D` (green)
  - Managed Agents / Console → `#B0AEA5` (gray — cloud/infrastructure)

### Logos

- Novastacks AI logo → `novastacks-logo-color.png` (in `clients/tiket/docs/`)
- Superuser HQ logo → `superuser-hq-logo.png` (in `clients/tiket/docs/`)
- Anthropic/Claude logo → use the official Claude mark if available, or text "Claude Code" in Poppins

### Gamma Import Tip

Paste each `## SLIDE` section as a separate "card" in Gamma. The **VISUAL** descriptions become the slide content. The **SPEAK** sections become presenter notes (Gamma supports this in the notes panel). Use the color/font system above when building each card.

### Quick Reference: Which Accent Color for What

| Element | Color | Hex                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| --------------------------------------- | ------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Slide titles, key terms, CTA buttons | Terracotta | `#Claude Code Intermediate: Beyond Cowork<br><br>- Marketplace → `#788C5D` (green)<br><br>- Managed Agents → `#B0AEA5` (gray — future state)<br><br>  <br><br>### Logos<br><br>  <br><br>- Novastacks AI logo → `novastacks-logo-color.png` (in `clients/tiket/docs/`)<br><br>- Superuser HQ logo → `superuser-hq-logo.png` (in `clients/tiket/docs/`)<br><br>- Anthropic/Claude logo → use the official Claude mark if available, or text "Claude Code" in Poppins<br><br>  <br><br>### Gamma Import Tip<br><br>  <br><br>Paste each `## SLIDE` section as a separate "card" in Gamma. The **VISUAL** descriptions become the slide content. The **SPEAK** sections become presenter notes (Gamma supports this in the notes panel). Use the color/font system above when building each card.<br><br>  <br><br>### Quick Reference: Which Accent Color for What<br><br>  <br><br>\|Element\|Color\|Hex\|<br>\|---\|---\|---\|<br>\|Slide titles, key terms, CTA buttons\|Terracotta\|`#D97757`\|<br>\|Links, "Code" badges, technical labels\|Blue\|`#6A9BCC`\|<br>\|Checkmarks, success, "done" states\|Green\|`#788C5D`\|<br>\|Future/planned features, secondary info\|Gray\|`#B0AEA5`\|<br>\|Error states, "don't do this" warnings\|Use terracotta at 80% opacity or `#C0613D` darker\|\|<br><br>  <br><br>---<br><br>  <br><br># APPENDIX B — Job-Specific Bridges (Full List)<br><br>  <br><br>These are woven into the script above. Collected here for reference:<br><br>  <br><br>### Sales bridges<br><br>- `/call-prep Hilton Jakarta` — pulls meeting notes, booking data, contract status → one-page brief<br><br>- Partner data from API → enrich with meeting notes → analyze trends → format as call brief<br><br>- "Response time to partner inquiries dropped from 48h to 4h"D97757` |
| Links, "Code" badges, technical labels | Blue | `#6A9BCC`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Checkmarks, success, "done" states | Green | `#788C5D`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Future/planned features, secondary info | Gray | `#B0AEA5`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Error states, "don't do this" warnings | Use terracotta at 80% opacity or `#C0613D` darker |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

---

# APPENDIX B — Job-Specific Bridges (Full List)

These are woven into the script above. Collected here for reference:

### Sales bridges
- `/call-prep Hilton Jakarta` — pulls meeting notes, booking data, contract status → one-page brief
- Partner data from API → enrich with meeting notes → analyze trends → format as call brief
- "Response time to partner inquiries dropped from 48h to 4h"

### Content bridges
- `/blog-draft "hotel distribution trends"` — researches, pulls SEO data, writes in brand voice
- Keyword rankings → competitor analysis → gap analysis → content calendar → Google Sheets
- "We automated the weekly content brief. 6 hours → 45 minutes of review."

### Marketing bridges
- Campaign performance → CRM data → ROI by channel → weekly brief → Slack
- Hook: prevent campaign asset finalization without brand guideline check
- Permissions: allow analytics read, deny bulk email send
- "We added a safety check that prevents the wrong creative from going out"

---

# APPENDIX C — Tools Glossary (Cheatsheet)

Quick reference for tools mentioned in the workshop or commonly used in agentic workflows:

**AI Interfaces**
| Tool | What it is | When you'd use it |
|------|-----------|-------------------|
| Claude.ai | Web chat interface | Quick Q&A, one-off tasks |
| Claude Cowork | Desktop app with projects + skills | Daily workflows, file read/write, connectors |
| Claude Code | Terminal/desktop harness with agents, hooks, rules, git | Team systems, automation, enterprise workflows |

**Claude Code Ecosystem**
| Tool | What it is |
|------|-----------|
| MCP (Model Context Protocol) | "USB ports" — lets Claude connect to external tools (Sheets, Gmail, APIs, databases) |
| Playwright | Browser automation — Claude opens real web pages, clicks, scrolls, screenshots |
| Chrome Extension | Claude for Chrome — interact with Claude while browsing any website |
| Computer Use | Claude controls your full desktop — mouse, keyboard, screen reading |

**Web Scraping & Research**
| Tool | What it is | When to use |
|------|-----------|-------------|
| Playwright + Vision | Screenshot pages → Claude reads the image | DEFAULT for all scraping — most reliable |
| Firecrawl | Turn any URL into clean markdown for AI | Bulk crawling, turning websites into data |
| Apify | Cloud scraping platform — 1000+ pre-built scrapers | Complex sites at scale, scheduled crawls |
| WebFetch | Built-in Claude Code tool — fetch any URL | Simple static pages, quick lookups |
| Tavily | Search API built for AI — returns answers with citations | "Search the web and summarize" tasks |
| Exa | Neural search — finds semantically similar content | Competitor research, finding similar pages |

**Design & Visual**
| Tool | What it is | When to use |
|------|-----------|-------------|
| Canva | Design platform with AI features + MCP connector | Social media graphics, presentations, brand assets |
| Figma | Professional design tool | UI/UX design, design systems, prototypes |
| Pencil | AI design editor for .pen files (MCP integrated) | Web/mobile app design, component editing |
| Gamma | AI-powered slide/presentation builder | Turning markdown scripts into visual decks |
| Vision API | Claude reads images natively — no API needed | Extracting data from screenshots, charts, PDFs |

**Orchestration & Automation**
| Tool | What it is | When to use |
|------|-----------|-------------|
| n8n | Open-source workflow automation (node-based) | Connecting tools, scheduled tasks, no-brain automation |
| Zapier | No-code automation — biggest app library | Quick integrations, non-technical teams |
| Make.com | Visual workflow builder (more powerful than Zapier) | Mid-complexity automations |
| Cron / Scheduled agents | Run Claude Code on a timer | Overnight reports, daily summaries, weekly audits |

**Data & Analytics**
| Tool | What it is | When to use |
|------|-----------|-------------|
| Google Analytics (MCP) | Website traffic and user behavior | Performance reporting, funnel analysis |
| Google Search Console (MCP) | Organic search performance — clicks, impressions, positions | SEO monitoring, content optimization |
| DataForSEO (API) | Keyword data, SERP analysis, backlinks, AI mentions | SEO research, competitor analysis, AEO tracking |
| Ahrefs (MCP) | Backlink profiles, domain ratings, organic keywords | Link building, domain authority, keyword gaps |
| HubSpot (MCP) | CRM — contacts, deals, companies, engagement | Sales pipeline, contact management, reporting |

**Communication**
| Tool | What it is | When to use |
|------|-----------|-------------|
| Gmail (MCP / gws CLI) | Send, read, draft emails via Claude | Outreach, follow-ups, inbox triage |
| Google Calendar (MCP) | Read and create calendar events | Meeting scheduling, availability checks |
| Slack (webhook/bot) | Post messages to Slack channels | Agent notifications, daily summaries, alerts |
| Telegram (bot) | Chat with Claude via Telegram | Mobile access, team notifications |

**Memory & State**
| Tool | What it is | When to use |
|------|-----------|-------------|
| MEMORY.md | Built-in file-based memory in Claude Code | Cross-session learnings, preferences, decisions |
| Agent memory (project) | Per-agent persistent memory folders | Agents that learn and improve over time |
| Letta (MemGPT) | External memory system for long-term agent recall | Production apps needing deep personalization |

---

# APPENDIX D — Source Material Credits

All sources fetched, assessed, and injected into the script:

**Raymond Houch (lifehacker.tw) — 5 articles + 1 video + 1 Threads post:**
- [cc.lifehacker.tw](https://cc.lifehacker.tw/) — 3-tier framework (Web/Cowork/Code), "commander/executor" metaphor, batch use cases, safety architecture → Used in Act 1 Slide 3
- [Desktop vs Terminal](https://raymondhouch.com/lifehacker/digital-workflow/claude-code-desktop-vs-terminal/) — 3 interfaces one brain, portability argument, "AI handles code, you handle content" → Used in Act 2 Slide 12
- [Cowork vs NotebookLM vs Code](https://raymondhouch.com/lifehacker/digital-workflow/claude-cowork-vs-notebooklm-vs-code/) — "Cowork covers 80% of needs", 5 signals to graduate to Code, three user pathways → Used in Act 1 Slide 3
- [CLAUDE.md and SKILL tutorial](https://raymondhouch.com/lifehacker/digital-workflow/claude-code-skill/) — Identity layer vs process layer, "create skill after 3rd repetition" rule → Used in Act 2 Slides 8-9
- [Notion/n8n/AI Agent comparison](https://raymondhouch.com/lifehacker/digital-workflow/notion-n8n-ai-agent-comparison/) — No-brain/judgment/collaborative task classification, workflow literacy → Used in Act 3 Slide 20
- [YouTube: beginner tutorial](https://youtu.be/xo7dE80ktu4) — "Baby mindset" (just ask), "be willing to temporarily be bad", permission modes, MCP as "superpowers", safe delete → Used in Act 1 Slide 1, Act 2 Slides 11-12
- [Threads: NTU workshop](https://www.threads.com/@raymond0917/post/DXCVzCaAPR5) — "Focus on content, delegate everything else to AI", 20 university professors demo → Used in Act 3 Slide 20

**thisweb.dev:**
- [.claude folder structure](https://thisweb.dev/post/claude-code-structure) — Full 8-primitive anatomy, hooks event types, rules with paths:, settings.json layers, agent frontmatter, commands with $ARGUMENTS → Used throughout Act 2

**LinkedIn:**
- [Pietro Montaldo](https://www.linkedin.com/posts/pietromontaldo_guidesclaude-ugcPost-7449762733174067201-pOWi) — "Skills create an abstraction layer over work itself", skills need maintenance not set-and-forget, 10K+ trained → Used in Act 2 Slide 9
- [Michael J. Silva](https://www.linkedin.com/posts/michael-j-silva_breaking-the-reason-anthropic-shut-down-share-7449914181685776384-Fn5Z) — "Runtime layer is where real value accrues, model is commodity swapped every 6 months", Anthropic shut down community harnesses to own runtime, permissions/audit trail = real asset → Used in Act 2 Slide 12
