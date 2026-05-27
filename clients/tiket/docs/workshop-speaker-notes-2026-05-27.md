# Workshop Speaker Notes — beyond-cowork deck
**Source:** Pre-workshop sync, 2026-05-27, Tina + Yaohong (~2h 1m, 1490-line transcript)
**Deck version:** post-commit `d5d2855` (47 numbered slides + 9-slide appendix = 56 total)
**Date generated:** 2026-05-27

> **How to read this doc.** Yaohong already embedded slide-by-slide notes inside the deck as a JSON block (`<script type="application/json" id="speaker-notes">` near line 252 in `beyond-cowork.html`). Those notes are well-written, post-rehearsal, and timing-tagged. Rather than duplicate them, each entry below carries:
> • **Lead** (who runs the slide — confirmed/inferred from rehearsal)
> • **Yaohong's deck notes** (verbatim — the canonical talking points)
> • **Add from rehearsal** (extra points / corrections / verbatim quotes from the 2026-05-27 sync that AREN'T already in Yaohong's notes — only when relevant)
> • **Demo / handoff** (anything operational discussed live)
>
> When a slide was not rehearsed in detail, that's stated explicitly.
> Tina's frame for the whole workshop (from the meeting): *"I'll probably just kind of kill you. I'll narrate most of it. They'll be shy — that's typical for Indonesians."* She plans to drive narration; Yaohong drives demos and the technical clarifications.

---

## Part 1: Slide-by-slide speaker notes

### Slide 1 — 01 Title
**Lead:** Both (~1 min)
**Yaohong's deck notes:**
- Hands up: who used Cowork every day this week? Who has built a skill?
- Title: 'Building agentic workflows on Claude' — Beyond Cowork.
- The arc of today: go from a personal assistant to the system that runs your operations.
- Quick intro by name, keep it to a minute. → next: who's teaching you.

**Add from rehearsal:** Tina decided to open with "*no introductions right [away]* — *I think first I'll do a roundtable*" before the formal intros, then segue into the shift narrative. Treat the title slide as a 30-sec hello, not the actual content beat.

---

### Slide 2 — 01b Trainers
**Lead:** Both (~2 min)
**Yaohong's deck notes:**
- Tina: 20+ yrs growth (Expedia · Tencent · Klook · Traveloka), now runs Novastacks — 12 agents, 1:9 human-to-agent ratio.
- Yaohong: CEO Superuser HQ — builds the infra: MCP servers, plugins, pipelines.
- Land it: 'Two operators who build and run these systems daily — not in decks.'

**Add from rehearsal:** Not rehearsed in detail — just the standard intro. Keep tight; Tina explicitly said she doesn't want to talk a lot at the open.

---

### Slide 3 — 01c Discussion
**Lead:** Tina (~3 min)
**Yaohong's deck notes:**
- Open the floor before we present — we want a few real voices.
- Q1: How do you feel after using Cowork? Q2: What impact could agentic workflows have on YOUR job?
- Take ~2 min, 3-4 answers. Listen for pain points you can call back to later.

**Add from rehearsal:** Tina (verbatim): *"I think I'll just give no introductions — I think first I'll do a roundtable. What are you working on?"* Then transition into the shift narrative. Anticipate quiet room: *"at the beginning they will be shy based on what I know for Indonesians."* Have a fallback question ready.

---

### Slide 4 — 01d The shift is here
**Lead:** Tina (~2 min)
**Yaohong's deck notes:**
- The shift isn't coming — it's here, and the adopter gap widens every quarter.
- Three beats: adoption (87% use gen AI; 57% have agents in production) · time saved (6.1 hrs/wk, seniors 8-10) · output (44% productivity, 80% shorter content timelines).
- Don't read every number — pick adoption + one time stat. Sources are on the slide.

**Add from rehearsal:** Tina's framing (verbatim): *"Going forward, this is what we believe we need to actually look at — and this is exactly why the three hours is about."* Use this as the bridge into Slide 6 (what the 3 hours is about).

---

### Slide 5 — 02 Role has changed
**Lead:** Tina (~3 min)
**Yaohong's deck notes:**
- The job itself is changing: a marketing engineer builds the systems, not just runs campaigns.
- Old job = execution. New job = orchestration: design the system, then supervise it.
- Stat: 3,000+ GTM / Marketing Engineer roles open, +205% YoY.
- Land it (Emily Kramer): 'With tools, you are the operator. With agents, you are the manager.'

**Add from rehearsal:** Not rehearsed in detail beyond the framing above — Tina to flesh out delivery on her own.

---

### Slide 6 — 03 This is this isn't
**Lead:** Tina (~1 min)
**Yaohong's deck notes:**
- Set expectations for the 3 hours: vocabulary you half-know, mental model of how agents work, skills + agents with real examples.
- Payoff line: by the end you'll say 'that should be a hook, not a rule' and your team will know what you mean.
- Not an engineering class — you won't write code, you'll learn to design workflows.

**Add from rehearsal:** Tina's actual rehearsal phrasing (verbatim, paraphrased lightly): *"We have a mixture of vocabulary — things are a bit more technical for a non-technical person, but that's what we're here for. I'll try to explain what those mean and why they're important, so by the end you can step on the first step — building skills to build systems, agents, and revamp your workflow."* This is more honest than "you won't write code" — flag that this audience is technical-curious, not technical-trained.

---

### Slide 7 — 04 Automation Augmentation Agency
**Lead:** Tina (~4 min)
**Yaohong's deck notes:**
- THIS SLIDE = the three MODES of working — not 'agents vs workflows'.
- Automation (n8n/Zapier): wire once, runs the same every time. Deterministic.
- Augmentation (Claude.ai/Cowork/Chrome): work WITH AI, in the loop every turn.
- Agency (Skills & Agents): configured to work independently — set the rules, it decides the steps.
- Land it: 'Automation runs the predictable. Augmentation boosts you in the moment. Agency runs while you sleep.'

**Add from rehearsal:** This slide caused real confusion in the rehearsal — Tina got tangled on the augmentation/agency boundary. The clarifying exchange:
- Tina (verbatim): *"Augmentation is more like when you're working with chat GPT or on Claude chat. 'Do this for me, send out a Gmail' — you're prompting in every single step. Versus with agent, you have a certain area where you allow the AI, you configure AI to work independently. Sometimes it makes its own judgment. It depends on how you harness the workflow."*
- Yaohong contrasted automation vs agentic customer support: *"Automation is fixed reply. But [an agent] can figure out what services to look at. It can go and pull the data from the API. So it's a bit smarter."*
- They flagged that they DON'T have a live agent example here. If asked, default to "managed agents in Claude" or Yaohong's customer-support agent thought experiment.

**Watch out:** Tina herself admitted *"Okay, I confused myself"* mid-rehearsal on this slide. Practice the three-way distinction once more before going live.

---

### Slide 8 — 05a Claude feature map
**Lead:** Tina (~2 min)
**Yaohong's deck notes:**
- Orient them on the infographic: ten surfaces, one shared brain.
- Today we dig into the ones in orange — the rest are always one step away.
- 'Same brain, different doors in.'

**Add from rehearsal:** Tina (verbatim): *"This basically is the overview of what we will cover mostly today — we're not going to cover Claude Design but more on Claude Code and what exactly connectors and a lot of skills and what exactly is Claude in Chrome."* So the explicit scoping line is: Claude Code + connectors + skills + Claude in Chrome — those are the four we're going into.

---

### Slide 9 — 05 Three harnesses
**Lead:** Tina narrates · Yaohong shows on screen (~3 min)
**Yaohong's deck notes:**
- For agentic workflow, focus on 3 interfaces: Claude.ai, Cowork, Claude Code. Same brain — different access.
- Claude.ai = smart colleague on chat · Cowork = delegated assistant in a sandbox (80% of daily work) · Code = full file/git/shell access, builds team systems.
- Rule of thumb: tool has an open API → Claude Code (calls it via MCP). Tool blocks programmatic access (e.g. LinkedIn) → use the browser (Cowork / Claude in Chrome).
- 'You already have Cowork. Today is about where it stops and what's next.'

**Add from rehearsal — Tina wants this slide rewritten visually:** *"I want to put this a little bit brief. It's a lot wording. I don't like it. I'll change the slide. But I basically just want to showcase the concept."* The intent: keep the metaphor (smart colleague vs delegated assistant vs system you build), but trim wording.

**Demo / handoff:** Tina narrates the metaphor, then says (verbatim): *"This is where you should probably say [show], Yaohong — could you just showcase Claude chat, Cloud Cowork, and Claude Code? And also the marketplace."* So Yaohong does a screen tour of the three interfaces here — not on a later slide.

---

### Slide 10 — 05ab Coding assistants work
**Lead:** Tina (~2-3 min)
**Yaohong's deck notes:**
- How a coding assistant actually works — the inner loop (Anthropic diagram). Same pattern a human developer would follow.
- Three steps: 01 Gather context → 02 Formulate a plan → 03 Take action → loop back.
- Key insight: steps 1 & 3 require reaching OUTSIDE the chat. That's tool use — and why Code & Cowork exist, not just chat.
- 'The model thinks. The harness gives it hands.'

**Add from rehearsal:** Tina explicitly flagged she wanted to **trim the right-hand-side wording** on this slide. Concrete example she gave (verbatim): *"For example, like okay, we get some error on this landing page. Can you find it and fix it? So you actually call a set of tools to perform — understand what it is, get context, formulate what needs to be done, and take action on the plan."* Use the landing-page-error example as the spoken anchor.

**Watch out:** Tina also said *"This is a lot of wording. I really don't like it."* She may slim this slide further before Friday — re-check before reading from it.

---

### Slide 11 — 05b2 Artifacts vs skills
**Lead:** Tina (~2 min)
**Yaohong's deck notes:**
- Artifact = a thing produced; Skill = a process for producing things.
- Artifact lives in the conversation, per-session. Skill lives on disk, auto-loads forever.
- They compose: a skill can produce an artifact.

**Add from rehearsal:** Tina considered deleting this slide entirely. Yaohong's call (verbatim): *"I think we just need one. Later on we talk about skill."* They consolidated — Yaohong removed the standalone "05b Artifacts" slide in commit `9e0f8cc` and kept this comparison slide. Yaohong (verbatim) explained artifacts using his fitness-trainer demo: *"I am replanning my training program. So after chatting he said okay, let me generate a plan for you. Instead of giving back everything in markdown, [Claude] created phase one. Finally it creates a web file, JavaScript extension file."*

**Concrete example to use:** Tina's grounded line — *"It's just like there's some limitation when you try to pass things around"* (artifact can be downloaded but isn't directly runnable). This is the practical "why we need Claude Code" pivot.

---

### Slide 12 — 05c Claude in Chrome
**Lead:** Tina narrates · Yaohong drives the live demo (~2 min, but expect demo to stretch)
**Yaohong's deck notes:**
- Claude in Chrome = a browsing agent operating YOUR logged-in browser — reads pages, clicks, fills forms.
- Because it's your session, Instagram / LinkedIn / portal logins all work.
- When: research behind logins, structured data off pages, repetitive browser tasks. Note: we used it in Demo 1.

**Add from rehearsal — explicit demo agreement (verbatim):**
> Yaohong: *"On the slide for Claude in Chrome, Tina will prompt Yaohong to open browser to do a demonstration."*

So Tina cues Yaohong here, Yaohong opens Chrome live. Pre-agreed demo content:
- Yaohong's framing (verbatim): *"You can automate certain tasks on your browsers. For example, if you want to click on things in Instagram, if you try to do it within bots, you'll be blocked by Instagram."*
- Tina's positioning (verbatim): *"We typically use it when there's no API you can access — for example Instagram or LinkedIn. Claude operates your logged-in browser on your behalf."*
- **Killer example agreed:** scraping competitor pricing (Tiket's relevant pain). Yaohong: *"Maybe we should use that as a sample."* Tina: *"Exactly — that's what they have bottom in. To actually do that requires serious engineers. Now you can do it."*

**Critical:** This slide REPLACES a standalone tool-use demonstration. Don't push Tool Use (Slide 13) before this — Tina explicitly said *"I want to put this a little bit brief"* and moved the demo here.

---

### Slide 13 — 05d Tool use
**Lead:** Tina (~2-3 min) — but Tina flagged this as the slide she's least confident on
**Yaohong's deck notes:**
- Tool use = what turns a chatbot into something that can DO things. On its own, LLM is text in → text out.
- Model says 'call this tool' and your computer does it.
- Augmented LLM = Retrieval (look up) + Tools (take action) + Memory (remember).
- Two toolboxes: Cowork = pre-packaged, Code = any tool with API via MCP.
- Live example: Playwright MCP drove this deck — Claude opened it, screenshotted it, read it back.
- 'Same brain. Different toolboxes — Cowork's is closed and curated, Code's is open.'

**Add from rehearsal — heads-up, terminology mess in the meeting:** Tina struggled with what "tool use" means in this context. The agreed plain-language landing:
- Yaohong (verbatim): *"Tool use is how an LLM model can do an action — for example, read a file, write a file, call web search, search for a term in a lot of files. It's a very granular function within Claude Code."*
- Tina (verbatim): *"Tools means take actions. Tool use = take action."*
- Yaohong's example for the room: *"Now I'm editing the file. When he runs this bash, this is the bash tool. So this is a tool use — it's calling the bash tool which runs the command cd."* Use the bash-edit example as the concrete anchor (don't get into Web Fetch / MCP semantics here).
- Tina to herself (verbatim): *"I find these 'tool use' very confusing. Who's inventing that?"* — she will keep her own explanation simple; if she stumbles, hand to Yaohong.

**Critical content edit:** Tina said *"For this slide, I just want to keep the image. I want to remove all the right-hand-side wording, and the H2 just needs actual examples: what is retrieval (example), what's actions, memory (example), tools (example)."* Yaohong may not have applied this yet — visually check before Friday.

---

### Slide 14 — 06 Connectors vs MCP vs plugins
**Lead:** Tina + Yaohong tag-team (~3 min)
**Yaohong's deck notes:**
- Three words people confuse. Two are integrations, one is packaging.
- Connectors = Anthropic prebuilt. MCP = open protocol, any API. Plugins = installable bundle.
- 'Connectors + MCP = how Claude reaches tools. Plugins = how you package and share.'
- MCP is a USB port; a plugin is the boxed kit.

**Add from rehearsal — this was the messiest section of the whole meeting.** Tina pushed back hard:
- Tina (verbatim): *"I think this slide we need to explain, but the content here is wrong... I think for this slide, the content should be MCP / CLI / API are how Claude reaches tools, and plugins are how Anthropic packages [tools]."*
- Yaohong's clarification (verbatim): *"Anthropic changed connectors to be a more general term, because MCP rises and is orange — confused, man. So now they just call it connectors where you can connect to external tools. So on these tools, some of them can be MCP. Actually most of them are MCPs."*
- Agreed plain-language version (synthesized from the rehearsal): "Connector is what Anthropic calls the integration today. Under the hood, most connectors are MCPs. Plugins are a different thing — they bundle skills, commands, agents, and MCPs together so you can install one thing and get a whole workflow."
- Yaohong's plugin example (verbatim): *"This is a sales plugin. You can call these skills. So basically it packages all the skills and also all the connectors you need to prepare for this sales. When you call /account-research, it asks you, 'Are you using Slack, HubSpot, or Motion?' and then wraps everything together."*

**Tina's edit intent:** *"I want to change the slide because we talk about tool use, and how to connect LLM with the tools. Then it goes to MCP / CLI / API."* If this isn't yet visually corrected, Tina should call out the wording mid-slide rather than rebuild it now.

---

### Slide 15 — 06aa MCP in action
**Lead:** Tina (~2 min)
**Yaohong's deck notes:**
- Make MCP concrete with a marketer flow: prompt → Claude picks the tool → MCP calls GA4 → real numbers.
- Same Cowork box; MCP connection is invisible.
- 'Without MCP, Claude answers only from what you paste. With MCP, it pulls live data on its own — and stops guessing.'

**Add from rehearsal:** Tina specifically wants to use **Google Search Console** as the canonical "MCP-connected tool a marketer cares about" — she demoed her own GSC connection during the rehearsal. The marketer flow she described (verbatim): *"Last week's GA4 traffic and traffic summary for the team — Claude just reads, 'I need real numbers,' calls the MCP, returns the data."*

---

### Slide 16 — 06a Where connectors live
**Lead:** Tina (~1 min)
**Yaohong's deck notes:**
- Quick orientation (screenshot): claude.ai → Settings → Connectors.
- Anthropic-maintained. One click to install. Move on.

**Add from rehearsal — IMPORTANT navigation correction (Yaohong, verbatim):** *"Connectors have moved to Customize."* So the screenshot path may be stale — the current path is **claude.ai → Customize → Connectors** (not Settings). Visually check the deck screenshot is current.

**Live demo agreed:** Tina pre-demoed connecting Google Search Console; Yaohong agreed to walk through "Add custom connector" live if asked, but flagged it requires Google Cloud Console app setup which they'll skip on stage. Yaohong (verbatim): *"I won't do it [live]. Maybe I'll just say, you can follow the instructions there."*

---

### Slide 17 — 06b Where plugins live
**Lead:** Tina (~1 min)
**Yaohong's deck notes:**
- Where plugins live (screenshots): Desktop app → Customize → Personal plugins → + → Plugin Directory.
- A plugin bundles skills/commands/agents.

**Add from rehearsal:** Tina's framing reaction during the rehearsal (verbatim): *"Plugin is a new app store. It's like a kind of agentic world marketplace — similar to App Store. Anthropic is sourcing credible third parties and listing them there. Very powerful."* Use that energy: this is the "agentic app store" beat.

---

### Slide 18 — 07a What is a skill
**Lead:** Tina (~2 min)
**Yaohong's deck notes:**
- Skills = folders of instructions Claude can discover. Every skill is a SKILL.md with name + description in frontmatter.
- The match: Claude compares request to each skill description; close enough → auto-activates.
- Teach Claude once, apply forever — no repeating yourself.

**Add from rehearsal:** Tina decided this should NOT be the first skill slide. Yaohong (verbatim): *"We should move skills [order]."* Tina (verbatim): *"We should start with [the old slide] 23 — 'If you find yourself explaining something to Claude repeatedly, that's a skill that needs to be written.' First find a scenario where they need a skill, then talk about the definition."* In the current renumbered deck, that's Slide 22 (07a4 When to use) being the natural opener. **Consider re-ordering on the fly: open the skills section with "When to use" (current Slide 22), then loop back to definition (current Slide 18).**

Yaohong's working definition agreed live (verbatim): *"Skills are instructions that you can ask Claude to repeatedly do."*

---

### Slide 19 — 07a1a Anatomy
**Lead:** Tina (~2 min)
**Yaohong's deck notes:**
- Anatomy: one required file (SKILL.md) + three optional folders — references/ (rules), scripts/ (code), assets/ (templates).
- Each adds leverage ONLY when needed — on-demand loading keeps context cheap.
- Version-controlled and shareable.

**Add from rehearsal:** Tina (verbatim): *"This is the structure of a common skill, right?"* — she agreed to keep this slide. Yaohong agreed: *"This is how a skill looks like."* No edits planned.

---

### Slide 20 — 07a1b SKILL.md
**Lead:** Tina (~2 min)
**Yaohong's deck notes:**
- SKILL.md = the operation manual. Frontmatter: name + description (the trigger) + optional allowed-tools.
- Body answers when/how/what: ## Trigger, ## Workflow, ## Output.
- Only SKILL.md is required.

**Add from rehearsal:** Tina referenced her own prospect-audit skill (verbatim): *"Prospect audit trigger. Okay, I think we keep this example."* So use her **/prospect-audit** as the worked example for SKILL.md frontmatter on this slide.

---

### Slide 21 — 07a3 How to invoke
**Lead:** Tina (~2 min)
**Yaohong's deck notes (from speaker-notes JSON — note: this is the PRE-trim version, not yet synced to the trimmed slide):**
- Skills load on demand — not on every message, not only when you type a slash.
- Cost comparison: CLAUDE.md loads every turn (high) · slash command full body on call (medium) · skill = description indexed, body loads when matched (low).
- Example: 'Write the monthly affiliate report' → matches description → loads skill → runs.

**Current slide content (post-trim):** The cost-comparison table is GONE from the visible slide as of commit `d5d2855`. The slide now shows only the auto-invocation example ("You say: 'Write the monthly affiliate report.' Claude scans descriptions → matches affiliate-report → loads the skill body → runs. You never typed a command."). The JSON speaker note above is stale — Yaohong removed the table visually but didn't update the JSON entry. **Ignore the cost-comparison bullet when delivering; deliver only the auto-invoke example.**

**Add from rehearsal:** Tina (verbatim): *"We need to get rid of [the] table. You can either use slash command, or you can just say it when you need it, or you can write in a skills description scenario — it will auto-invoke. So three types of how skills activate."* Yaohong (verbatim): *"Or you can do /affiliate-report — you can do a slash command."* So the three invocation paths to teach here:
1. Type `/skill-name` directly
2. Describe what you want — Claude matches the skill description and auto-invokes
3. Build matching scenarios into the skill description for reliable auto-invoke

---

### Slide 22 — 07a4 When to use
**Lead:** Tina (~2 min)
**Yaohong's deck notes:**
- Rule of thumb: if you explain the same thing to Claude repeatedly — that's a skill waiting to be written.
- Signals: re-describing PR feedback format, commit format, brand voice, audit method every single time.
- 'Second time you say it — make it a skill.'

**Add from rehearsal:** **Tina wants this slide to OPEN the skills section** — see note on Slide 18 above. The rehearsal landing line (verbatim): *"If you find yourself explaining something to Claude repeatedly, that's a skill that needs to be written."*

---

### Slide 23 — 07c What makes a good skill
**Lead:** Tina (~2-3 min)
**Yaohong's deck notes:**
- Five rules: sharp description · one job · names its inputs · short body + linked references · testable output.
- The description IS the trigger. 'Affiliate tool' → Claude never finds it.
- 'The description is the trigger, the body is the recipe, references are the pantry — load only when cooking.'

**Add from rehearsal:** Tina pre-committed to trim this slide if running long (verbatim): *"I don't think that we can cover everything what makes a good skill."* If time is tight, just deliver the "description is the trigger" rule and move on.

---

### Slide 24 — 07 What is an agent
**Lead:** Tina (~2-3 min)
**Yaohong's deck notes:**
- Agent = a specialist with its OWN whiteboard (fresh context). Markdown spec in `.claude/agents/` with role, tools, instructions.
- Spins up subagent, does the work, returns only a summary — keeps YOUR context clean.
- When: judgment work or heavy research that would burn your window.

**Add from rehearsal:** Tina (verbatim): *"Agents — this is very important... they have their own context window. They're usually defined by a role, the tools, and instructions. Topic = one. Judgment work."* This matches the slide; no edits.

---

### Slide 25 — 07e Agents differ
**Lead:** Tina (~2 min)
**Yaohong's deck notes:**
- Same base model — different role/tools/instructions.
- Contrast: /linkedin-writer (rejection-trained, Tina's voice, 10-criteria eval) vs /writer (client-agnostic).
- 'Same base model — the orchestrator (you) is what makes the difference.'

**Add from rehearsal — Tina's verbatim walk-through:** *"I write personal life for LinkedIn — I want LinkedIn to write for my company and learn from rejections and wins, improve. Writer is for SEOs and adapts from the clients. And the tools are different. Instructions — you need to understand the client's context, load my voice. I like to write a particular way — there are two writers. So I'm actually using two sub-agents."* This is the canonical line for the contrast.

---

### Slide 26 — 07d Skill vs agent
**Lead:** Tina (~2 min)
**Yaohong's deck notes:**
- Skill = recipe card (one repeatable procedure, cheap). Agent = specialist chef (judgment + own whiteboard).
- 'If you could write the steps out in advance, it's a skill. If you need judgment, or you'd dump a lot of files into your window, it's an agent.'

**Add from rehearsal:** Not rehearsed in detail — Tina said (verbatim) *"I think that's clear, we can go through it quickly."* Keep it short, this is just the punchline before demos.

---

### Slide 27 — 07b Demos divider
**Lead:** Yaohong (~1 min)
**Yaohong's deck notes:**
- Divider into three live demos. Frame: 'Same prompt. Two tools. Where does each land?'
- Preview: 01 influencer research · 02 GSC period-over-period · 03 video ad pipeline.

**Add from rehearsal:** Tina (verbatim): *"And then demos right. Take a demo. Just basically you just copy on your Cowork — you copy paste this and you just showcase."* Yaohong agreed to test the prompts pre-stage: *"I must make sure it works first."* Tina pre-flagging: the three demos shouldn't run cold.

---

### Slide 28 — 08 Demo 1 influencer research
**Lead:** Yaohong (~5 min LIVE)
**Yaohong's deck notes:**
- BOTH tools work. Same prompt: find premium ID travel influencers on IG → Google Sheet.
- Cowork: Claude in Chrome + Sheets connector. Code: Playwright MCP + Sheets MCP. Both → 15+ influencers.
- 'Same brain. Different harness. Different result. The difference is MCP.'

**Demo prep status (from rehearsal):** Yaohong already prepared this. Action item carried over from Fireflies summary: *"Yaohong: prepare & test live demos (Cowork workflows, Chrome extension automation, connectors including Google Search Console)."* — DO a dry run Thursday night.

---

### Slide 29 — 09 Demo 2 GSC
**Lead:** Yaohong (~5 min LIVE)
**Yaohong's deck notes:**
- The brutal one: Cowork hits a dead end — no GSC connector, 'I don't have access to Google Search Console.'
- Code via MCP: pulls thousands of queries, period-over-period → complete analysis in one run.
- 'You're not limited to what Anthropic pre-builds. You connect what you need.'

**Add from rehearsal:** Tina pre-confirmed this is HER lived experience (verbatim): *"The first test I did in Claude Code is to get the MCP for Google Search Console."* So if you want a Tina-vouches-for-this moment, she can briefly chime in *before* Yaohong runs the demo to anchor it.

**Watch out — connector status:** Yaohong said GSC connector setup requires Google Cloud Console app creation (verbatim: *"It's a security risk — you're creating an application within Google Cloud"*). For the live demo, Yaohong is running a pre-built MCP, not setting it up from scratch.

---

### Slide 30 — 10 Demo 3 video ad
**Lead:** Yaohong (~5 min LIVE — most ambitious demo)
**Yaohong's deck notes:**
- TikTok ad from a Tiket activity page — local-looking avatar, real photos, VO throughout.
- Cowork: drafts script/storyboard but can't reliably scrape/chain → you do execution.
- Code: Chrome MCP scrape → script → HeyGen/Seedance MCP → assembled pipeline.
- 'Advisor → operating system. That is the shift.'

**Add from rehearsal — Tina's spoken intro to use:** *"For example, you want to create a TikTok ad. It's a video, and this [Tiket activity page] is the source. You need to translate a PDP — basically the landing page — into this ad. On the video I want a local-looking avatar, so you need an MCP or tool that can generate avatars. You need to fetch real photos from the activity. And voiceover throughout. Then walk me through a plan first — meaning I want to know how you're going to do it before they execute."*

**Critical timing note:** Tina flagged that by the end of Demo 3, the workshop will be at ~90-120 minutes elapsed. Confirmed in meeting: *"By this time we should talk for 90 minutes, 2 hours."* Plan the rest of the deck accordingly.

---

### Slide 31 — Breakout build
**Lead:** Both (~30 min activity)
**Yaohong's deck notes:**
- Teams of 4, 30 min on the clock. Build a real skill or agent for one task from your own desk.
- Pick (a weekly task ≥1 hr) → Build (name it, description, body) → Sell (2 min).
- One team per group demos after the break.

**Add from rehearsal — IMPORTANT realism flag:** Yaohong (verbatim): *"I have a feeling nothing will be [built] during the breakout."* Tina agreed (verbatim): *"Take at least 20 minutes."* Set expectations honestly — this is a "draft the description and one paragraph of body" exercise, not a working skill. Lower the bar so the room can succeed.

**Open question from rehearsal:** They debated whether to do the breakout at all given time pressure. Decision wasn't fully locked. Final call should be made Thursday based on demo length estimates.

---

### Slide 32 — Break
**Lead:** — (10 min)
**Yaohong's deck notes:**
- Back in 10. Flag that Section 2 (the harness) is the important part. Restart hard, on time.

**Add from rehearsal:** Tina flagged this break is real — at the 2-hour mark people will be saturated. Restart on time matters because Section 2 is the dense conceptual chunk.

---

### Slide 33 — Show and tell
**Lead:** Both (~10-15 min)
**Yaohong's deck notes:**
- Post-break show & tell: one team at a time, ≤2 min each.
- Live feedback on: description sharpness, scope, tool choice, first line of the body.
- 'Would you reach for this on Monday?'

**Add from rehearsal:** Couple this with the realism flag from Slide 31 — if no team has a full draft, pivot to "describe what you'd build and why" instead of demoing.

---

### Slide 34 — 11 The claude folder
**Lead:** Tina (~3 min)
**Yaohong's deck notes:**
- How you give Claude persistent business context — boots into your voice, rules, playbooks every session.
- Walk the tree: CLAUDE.md · settings.json · hooks/ · agents/ · commands/ · skills/.
- Numbers: 60 commands, 70 skills, 15 project agents.
- 'The brain is the same for everyone. The harness is what makes it yours.'

**Add from rehearsal:** Not rehearsed in detail. Tina (verbatim): *"Persistently enabling business context and brand persistently."* This is the persistence/business-memory beat — keep it tight.

---

### Slide 35 — 14a Context window — what it is
**Lead:** Tina (~3 min)
**Yaohong's deck notes:**
- Pivot into the harness. THE concept behind almost every frustration: the context window.
- IS: total text Claude can reference (incl. its own response). Working memory for THIS conversation.
- IS NOT: long-term knowledge, unlimited, or persistent. Resets each session.
- 'A working memory, not a brain.'

**Add from rehearsal:** Tina explicitly flagged this section may get compressed (verbatim): *"I can talk about all this. Will we have time to reach [it]?"* Yaohong agreed *"We can see [if they have capacity]. It's good to put in there."* So Section 2 is on-time-permitting — don't apologize, just deliver tight.

---

### Slide 36 — 14a2 Congestion signs
**Lead:** Tina (~2 min)
**Yaohong's deck notes:**
- Signs of rot: forgets instructions from 20 turns ago · output gets generic · agents inconsistent · steps dropped · re-asks for info you gave · voice drifts.
- Trap: instinct is to repeat. 'Don't. Reset or offload — then continue.'
- 'Symptom ≠ bug. It's context physics.'

**Add from rehearsal:** Not rehearsed in detail — Tina to flesh out on her own.

---

### Slide 37 — 14b Brain infographic
**Lead:** Tina (~2-3 min)
**Yaohong's deck notes:**
- Everything flows into ONE brain sharing one 1M ceiling.
- Left = CLAUDE.md, MEMORY.md, skill/MCP tool lists. Right = conversation, files read, screenshots, tool results, answer.
- Tool results run 5-50K+. 'One big MCP call + long PDF + 20-turn chat = 30-40% gone — and accuracy drops long before that.'

**Add from rehearsal:** Not rehearsed in detail.

---

### Slide 38 — 14c What counts toward window
**Lead:** Tina (~2 min)
**Yaohong's deck notes:**
- Bar chart: relative token cost. CLAUDE.md small; MCP tool lists big; single tool result biggest (5-50K+).
- 'A single tool call can cost more than your whole CLAUDE.md.'

**Add from rehearsal:** Not rehearsed in detail.

---

### Slide 39 — 14d Where to put context
**Lead:** Tina (~3 min)
**Yaohong's deck notes:**
- Whiteboard metaphor for six surfaces: CLAUDE.md = permanent marker · MEMORY.md = sticky note · PROGRESS.md = desk notebook · Skills = filing cabinet · Agents = own whiteboards · Hooks = wall stamps (zero context cost).
- 'Whiteboard, cabinet, desk, or wall?'

**Add from rehearsal:** Not rehearsed in detail.

---

### Slide 40 — 14e Context rot
**Lead:** Tina (~3 min)
**Yaohong's deck notes:**
- Bigger isn't better. Accuracy degrades as window fills (2% at turn 1 → 95% at turn 20).
- Fixes: trim CLAUDE.md · split to skills · persist to PROGRESS.md · /compact · /clear · delegate to subagents.
- 'It's not about saving space. It's about output quality.'

**Add from rehearsal:** Not rehearsed in detail.

---

### Slide 41 — 15 Post-mortem v2 v3
**Lead:** Tina (~5 min)
**Yaohong's deck notes:**
- War story: prospect-audit v2 shipped hallucinated report — 27,659 vs real 15,164 keywords, swapped CWV metrics.
- v2 = 1 agent, 1,791 lines, 8 phases in one window. Phase 7 ~100K+ tokens, Phase-0 rules drowned.
- v3: orchestrator + collect/report subagents + 3 Python gates. 100-150K → 10-15K. Hallucinations → zero.
- 'The skill wasn't the problem. The architecture was. It can't hallucinate past a Python exit code.'

**Add from rehearsal:** Tina flagged this is the hook for the hook-and-gate concept (verbatim): *"I was trying to actually kind of tell them about hook and gate."* So drive into Slides 42-44 hard after this.

---

### Slide 42 — 16 Agent hook gate
**Lead:** Tina (~3 min)
**Yaohong's deck notes:**
- Agent = one job per worker (fresh start).
- Hook = tripwire YOUR computer runs, not Claude — fires automatically.
- Gate = code check Claude can't argue with. Numbers don't lie.
- 'Hooks fire the gates — the rule runs without you. Together they're the harness — the system that runs your operations.'

**Add from rehearsal:** Tina said the workshop payoff line is *"by the end you'll say 'that should be a hook, not a rule'"* — this slide is where that lands. Make it the explicit callback.

---

### Slide 43 — 16b Learnings loop
**Lead:** Tina (~2-3 min)
**Yaohong's deck notes:**
- Hook isn't just cleanup — it's how the agent LEARNS. On stop, hook writes one line to CLAUDE.md/MEMORY.md.
- Not fine-tuning: no weights, no GPU, no data team — just changes what model knows before starting. A shell script.
- 'Never let a correction evaporate.'

**Add from rehearsal:** Not rehearsed in detail.

---

### Slide 44 — 16c Slop check example
**Lead:** Tina (~3 min)
**Yaohong's deck notes:**
- Live example tying hook → gate: AI-slop content. Edit markdown → PostToolUse hook fires → runs linkedin-slop-check.py → injects score + flagged phrases.
- settings.json matcher Edit|Write + personal slop list (banned: 'isn't X. It's Y', 'in today's fast-paced…', game-changer).
- 'Set up the rule once. Build your list once. The check runs forever — without you.'

**Add from rehearsal:** Tina's banned-words list lives in her actual repo — she can pull it up live if asked. Reinforces "your harness is yours" point.

---

### Slide 45 — 27 Team orchestration — Git is the new Notion
**Lead:** Tina → Yaohong (~3 min)
**Yaohong's deck notes:**
- 'Git is the new Notion' — and smaller than Notion.
- 5 commands translated: pull/status/commit/push/log.
- Without it: 100 versions of the 'affiliate report'.

**Add from rehearsal — explicit handoff agreement:** Tina (verbatim): *"You just show them how you change the slide. The way that we work. I was like, okay, basically it's kind of like a Google Drive."* So Tina does the metaphor, then hands to Yaohong who does a LIVE demo of editing this very deck via git.

**Yaohong's pushback on audience fit (verbatim):** *"One thing is to technical people [this] is not a new thing."* So calibrate: most of the room is non-technical, so Git-as-Notion is fresh and useful — but flag the technical attendees that this is for the others.

**Demo logistics question raised:** *"How is this installed? Install Git, people..."* — Yaohong noted git install is a prerequisite. He decided NOT to install on stage (verbatim): *"Yeah, [git training is] step two — workshop number two."* So this is a teaser for a future workshop, not a hands-on segment.

---

### Slide 46 — 36 Yaohong team orchestration
**Lead:** Yaohong (~5-7 min)
**Yaohong's deck notes:**
- Yaohong's live segment: how Superuser HQ runs multi-player Claude workflows day-to-day.
- Pick 1-2: a live demo/story, team rituals (git conventions, PR gates, review cadence), one pattern you wish you'd known.
- (Placeholder — Yaohong to finalize pre-workshop.)

**Add from rehearsal — explicit action item on Yaohong:** This was the slide Yaohong said he'd finalize *"on the spot"* (verbatim from end of meeting). Tina's preference (verbatim): *"You just show them how you change the slide. The way that we work."* Walk through editing this very deck via Claude Code + git, in real time.

**Status:** Still a placeholder slide. Yaohong's action item from the meeting carries over: prepare the content for this slide (no slide-design needed, just the narrative + the demo flow).

---

### Slide 47 — 32 Closing
**Lead:** Both (~1 min)
**Yaohong's deck notes:**
- 'Thank you. Now go build something.'
- Arc recap: same brain, bigger operating system — from personal assistant to the system that runs your operations.
- Resources / Q&A.

**Add from rehearsal:** Not rehearsed in detail.

---

### Slide 48 — Appendix (divider)
**Lead:** —
**Yaohong's deck notes:** Not in main flow. Skip in 3-hour workshop; open on request.

**Add from rehearsal:** Appendix exists for Q&A or follow-up workshop. Don't show on stage.

---

### Slide 49 — 18 Handoff to Yaohong (Appendix)
**Lead:** Tina → Yaohong (appendix-only)
**Yaohong's deck notes:** Optional interlude into live build-along.

**Add from rehearsal:** Not rehearsed.

---

### Slides 50-54 — 19 Layer 1 fetch → 23 Layer 5 wrap (Appendix build-along)
**Lead:** Yaohong (appendix-only)
**Yaohong's deck notes:** Five-layer build-along (Fetch → Enrich → Analyze → Format → Wrap), partner-performance report example.

**Add from rehearsal:** Not rehearsed. Yaohong indicated team orchestration (Slide 46) will substitute for the live build-along in the main flow — these appendix slides only run if the room asks "show us the actual build."

---

### Slide 55 — 24 The pattern (Appendix)
**Lead:** Tina or Yaohong (appendix-only)
**Yaohong's deck notes:** Universal shape — Fetch → Enrich → Analyze → Format → Wrap.

**Add from rehearsal:** Not rehearsed.

---

### Slide 56 — 26 Safety envelope (Appendix)
**Lead:** Tina (appendix-only)
**Yaohong's deck notes:** Three concentric layers. Permissions (can't) · Hooks (system enforces) · Instructions (should).

**Add from rehearsal:** Not rehearsed.

---

## Part 2: Slide-change gap check

This tracks every "change this slide / remove this / add this" moment from the 2026-05-27 transcript, cross-referenced against the current deck and Yaohong's post-meeting commits (`9e0f8cc`, `701fd27`, `d5d2855`).

| # | Requested change (verbatim or close paraphrase) | Status | Notes |
|---|---|---|---|
| 1 | "Delete slide 10" / consolidate the standalone Artifacts slide — keep one combined Artifacts vs Skills slide. Tina (line ~200): *"Delete slide 10. We keep the artifact and skills."* | DONE | Yaohong consolidated in commit `9e0f8cc` ("consolidate Artifacts slide"). Current Slide 11 (`05b2 Artifacts vs skills`) is the merged version. |
| 2 | Drop the standalone "Tools with Claude Code" slide. Tina around line 404: *"We didn't need to talk about the tool use [extra slide] because I had a tool use [Slide 13]."* | DONE | Yaohong removed in commit `701fd27`. Tool Use beat now sits only on Slide 13 (`05d Tool use`). |
| 3 | Trim the skills section — drop the deep-dive folder slides (references/, scripts/, assets/), drop "Where are your skills" and "How to get skills", flatten /47. Tina lines ~975-982: *"1617 about 18. 1920 drop... 21 drop, delete 21... 22 just down."* | DONE | Yaohong removed 5 slides in commit `d5d2855` ("trim skills section, renumber to /47"). Deck is now 47 main slides. |
| 4 | Remove the cost-comparison table from "How to invoke a skill" — show only auto-invocation. Tina line ~998: *"We need to get rid of [the] table."* | DONE | Commit `d5d2855` flattened the table — Slide 21 now leads with the auto-invocation example. |
| 5 | Slide 13 (Tool Use): remove all right-hand-side wording, keep the augmented-LLM image, put real examples in H2 for retrieval / action / memory / tools. Tina line ~384: *"I just want to keep the image. I want to remove all the right-hand-side wording, and the H2 we just need actual examples..."* | PARTIAL | Slide 13 still has the heavy right-hand-side Cowork-vs-Code toolbox cards + Playwright example. Tina's intent was to slim further. Either (a) accept current design as the post-rehearsal evolution, or (b) trim Friday morning. Flag for Tina decision. |
| 6 | Slide 14 (Connectors vs MCP vs plugins): rewrite — "MCP / CLI / API = how Claude reaches tools; plugins = how Anthropic packages." Replace plugins from the integrations row, since plugins are packaging, not integration. Tina line ~462-472. | PARTIAL | Slide 14 still uses the "Cowork Connectors · MCP · Plugins" three-column table. The framing landing line *"Connectors + MCP = how Claude reaches tools. Plugins = how you package"* IS at the bottom of the slide. But the table itself treats all three as parallel categories, which is the framing Tina rejected. Either restructure visually OR have Tina verbally re-anchor the framing when she reaches it. |
| 7 | Slide 16 (Where connectors live): screenshot path is stale — Anthropic moved connectors from Settings to Customize. Yaohong line ~444: *"Connectors have moved to Customize."* | UNVERIFIED | Slide 16 still says "claude.ai → Settings → Connectors." Update screenshot or update the path label. Visual check required Thursday. |
| 8 | Re-order skills section to open with "When to use" (current Slide 22), THEN definition (current Slide 18). Tina line ~939-945: *"We should start with [old] 23 — 'If you find yourself explaining something to Claude repeatedly, that's a skill.' First find a scenario where they need a skill, then talk about definition."* | MISSING | Section order in the deck is still definition-first (Slide 18) → anatomy → SKILL.md → invoke → when-to-use → what-makes-good. Not re-ordered post-meeting. **Recommendation: don't re-order the deck Friday morning — instead have Tina open the section verbally with the "Second time you say it, make it a skill" line before clicking into Slide 18.** Low-risk verbal fix. |
| 9 | Add an agent example earlier (Slide 7 area) — Yaohong proposed a customer-support agent example to distinguish from automation. Tina line ~73-86. | MISSING | No live agent example added to Slide 7 (Automation/Augmentation/Agency). If the room asks "what's a real agent right now," fall back to: managed agents in Claude, Yaohong's customer-support agent thought experiment, or Tina's own /linkedin-writer (covered later on Slide 25). |
| 10 | Add concrete examples to Slide 13 (Tool Use) H2 — retrieval example, action example, memory example. Tina line ~384. | MISSING | Slide 13 H2 is currently "What turns a chatbot into something that can do things" — no per-concept worked examples. The Playwright box is good but doesn't cover retrieval/memory. Either add inline or Tina improvises with the bash-edit example (per Yaohong's framing). |
| 11 | Add Claude in Chrome live demo cue ON Slide 12 — Tina prompts, Yaohong opens browser. Line ~357: *"On the slide for Claude in Chrome, Tina will prompt Yaohong to open browser to do a demonstration."* | UNVERIFIED | Slide 12 doesn't have a visible "[DEMO]" marker. The handoff is in Yaohong's deck note but not in the slide chrome. Low-risk — both presenters know the cue verbally. |
| 12 | Slide deck numbering cleanup — flatten hand-numbered counters into clean /47. Yaohong line ~648-649. | DONE | Commit `d5d2855` renumbered everything to /47. |
| 13 | Slide 16 (MCP in action — was renumbered): use Google Search Console as the canonical example. | DONE (kind of) | Slide 15 (`06aa MCP in action`) currently shows a generic marketer flow. GSC is the canonical demo on Slide 29 (`09 Demo 2 GSC`). Acceptable split — Tina can name-drop GSC verbally on Slide 15 to thread it. |
| 14 | Breakout session — confirm structure or possibly drop. Lines ~1109-1113. Yaohong: *"I have a feeling nothing will be done during the breakout."* | DECISION PENDING | Slide 31 (Breakout build) is still in the deck. No formal decision recorded to keep or cut. Flag for Tina/Yaohong final call Thursday based on demo overrun risk. |
| 15 | Slide 46 (Yaohong team orchestration): finalize content. Action item: *"Yaohong to finalize pre-workshop."* | MISSING | Slide 46 is still a placeholder in the deck's speaker notes. Yaohong said in meeting (verbatim): *"I'll just run it on the spot."* But the slide BODY in HTML may still need text — visually verify Thursday. |
| 16 | Slide 1 (Title): re-frame to open with a roundtable, not a formal intro. Tina line ~29-30. | DONE (verbally) | No slide change needed — Tina just runs Slide 1 as a 30-sec hello, then jumps to roundtable (Slide 3) before re-anchoring on intros (Slide 2). Sequence stays the same; delivery shifts. |
| 17 | Reduce wording on Slide 9 (Three harnesses). Tina line ~139-142: *"It's a lot wording. I don't like it. I'll change the slide."* | MISSING | Slide 9 still has the dense Cowork-vs-Code body. Not visibly trimmed post-meeting. Either trim Friday morning or Tina narrates around the density. |

### Special-attention flagged items (status summary)

- **Removing technical content (MCP/plugin distinctions, retrieval-memory):** DONE in part (extra Tools-with-Claude-Code slide removed in `701fd27`; skills deep-dive folders removed in `d5d2855`). NOT DONE: the Connectors vs MCP vs Plugins slide (Slide 14) is the slide Tina most pushed back on, and its 3-column table framing is still intact. This is the highest-risk slide for audience confusion — recommend Tina explicitly disclaim mid-slide ("Anthropic now calls all of these 'connectors' — I'll explain what's underneath").
- **Slide deck numbering cleanup:** DONE in `d5d2855` — clean /47.
- **Breakout session structure:** PENDING decision. Still in deck, but rehearsal flagged it may not produce real output.
- **Connectors / GSC / Chrome extension demos:** Demo 2 GSC slide exists (Slide 29). Chrome extension demo on Slide 12 is verbally agreed (Tina cues, Yaohong opens browser) but not marked visually. GSC connector setup will be skipped live ("you can follow the instructions") — Yaohong runs a pre-built MCP for the actual demo.
- **"Tools with Claude Code" slide removal:** DONE in `701fd27`. The rationale, confirmed in transcript: rehearsal showed Slide 13 (Tool Use) already covers the toolbox point — the standalone slide was redundant. (NOT removed because it was wrong — removed because it duplicated Slide 13's territory.)

---

## Open items / suggested next actions

1. **Visual-verify Slide 16 connector path** ("Settings" vs "Customize"). Yaohong confirmed Anthropic moved it — update screenshot OR add a verbal aside. (5 min Thursday.)
2. **Tina's call on Slide 9 + Slide 13 wording trim.** Both slides she explicitly disliked verbally; both still dense in the current deck. Either trim Friday morning or accept and narrate around. **Decision needed by Thursday EOD.**
3. **Lock the breakout decision** (Slide 31). If keeping, set explicit expectation that the deliverable is "the description + first paragraph of the body" — not a working skill. If cutting, reclaim 30 min for deeper Section 2 (context window + post-mortem).
4. **Yaohong to lock Slide 46 content** ("team orchestration" live segment). Currently placeholder. He said he'll run it on the spot but the slide should have at least 3 bullet points or a screenshot anchor so the audience has something to look at.
5. **Dry-run all three demos Thursday** (Demo 1 influencer, Demo 2 GSC, Demo 3 video ad). Action item flagged from Fireflies summary. Demo 3 is the most fragile — chained HeyGen/Seedance MCPs.
6. **Tina to decide on opening sequence:** Slide 1 (Title, 30s) → Slide 3 (roundtable, 3 min) → Slide 2 (intros, 2 min) → Slide 4 (shift) — this is the verbally agreed flow but not reflected in slide order. Either re-order or commit to verbally navigating non-linearly.
7. **Yaohong's "Connectors vs MCP vs Plugins" rewrite (Slide 14).** This was the most contentious slide in rehearsal. Either rebuild the 3-column structure (plugins as packaging, not parallel integration), OR Tina verbally re-frames at the top of the slide. **Strong recommendation: verbal re-frame is lower-risk than a same-week rebuild.**
8. **Skills section opening order** (Slide 18 vs Slide 22 first). Don't re-order; instead Tina verbally opens with "Second time you say it, make it a skill" before clicking into Slide 18.
9. **Post-workshop:** business-strategy conversation (AI transformation pricing, ICP targeting gyms/legal/TCM, breakout sessions, ethical AI content) is a SEPARATE thread — flagged from Fireflies action items, not workshop-prep. Track separately.

---

*Generated from `mcp-claude_ai_Fireflies-fireflies_get_transcript-1779855504482.txt` (Fireflies ID `01KSKHH987RQVQBRQ19XHE6W1X`, 121 min, 2026-05-27T02:00:00Z) and `clients/tiket/docs/beyond-cowork.html` at commit `d5d2855`.*
