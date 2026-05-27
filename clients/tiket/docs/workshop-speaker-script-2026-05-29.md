# Tiket Workshop — Speaker Script

**Beyond Cowork · Building agentic workflows on Claude**
Jakarta · 2026-05-29 · ~3 hours · Tina Chu + Yaohong Chng

> **How to read this doc.** This is a presenter-ready, paragraph-by-paragraph script. Read it cold if needed. Italics are stage directions (where to click, what to demo, what to watch out for). Bold lines are landing lines — say them word-for-word.

> **Voice split.** Tina narrates ~80% of the workshop, Yaohong drives the demos and the technical clarifications. When a slide says **Lead: Tina**, she runs it solo. When it says **Lead: Yaohong** or **tag-team**, hand-offs are scripted inline.

> **Audience note.** Indonesian audience, mostly Tiket marketing/ops/comms. Technical-curious, not technical-trained. They will be quiet at the start. Don't take silence as disengagement.

---

## Opening · before Slide 1

*Walk on stage. Don't introduce yourselves yet. Don't go to the title slide yet. Look at the room.*

**Tina:** Before we start — quick check. Hands up if you've used Cowork this week. *(pause)* Now hands up if you've built a skill, or a custom command, or anything that runs on its own without you having to type it again. *(pause — likely fewer hands)*

OK. That second number is what today is about. We'll close the gap between "I use Claude" and "I have Claude doing things for me while I'm asleep."

Before any of us talks at you, I want to hear from the room. *(go to Slide 3 — Discussion. We'll come back to formal intros after.)*

---

## Section 1 · The building blocks

### Slide 1 — Title
**Lead:** Both · 30 sec

*Quick beat on the title slide. This is a hello, not a content beat.*

**Tina:** Good morning, everyone. The workshop today is "Beyond Cowork — building agentic workflows on Claude." We're going to go from Claude-as-personal-assistant to Claude-as-the-system-that-runs-your-operations.

I'm Tina, this is Yaohong, we'll properly introduce ourselves in a minute. But first — I want to hear from you.

---

### Slide 3 — Discussion (taken out of order)
**Lead:** Tina · 3 min

*Click straight to Slide 3 — the roundtable. Skip Slide 2 (Trainers) for now.*

**Tina:** Two questions. Don't worry about being clever — just be honest.

One: how does it feel after you've used Cowork? What's good, what's frustrating, what's surprising?

Two: if you could put an agentic workflow in your job — something that just *runs* without you driving every step — what would it do? What part of your week would you give to it?

*Take 3-4 voices. Listen for pain points — you'll call back to them later. If the room stays quiet for more than 10 seconds, prompt by name or pick one team. Don't be afraid to land on Yaohong or yourself if nobody speaks — model what an honest answer sounds like.*

OK. Hold those answers. We'll come back to them.

---

### Slide 2 — Trainers
**Lead:** Both · 2 min

*Now back to Slide 2 for the formal intros.*

**Tina:** Quick on who's teaching this. Twenty-plus years in growth — Expedia, Tencent, Klook, Traveloka. Now I run Novastacks, an AI consultancy. We work with twelve AI agents in-house — the ratio is one human to nine agents. Most of what I'm going to show you today, I run on myself or on my own clients first.

**Yaohong:** I'm Yaohong, CEO of Superuser HQ. We build the infrastructure underneath — MCP servers, plugins, pipelines, the connective tissue that lets Claude actually reach the tools you already use.

**Tina:** The reason we're co-teaching is the split — I run the workflows day-to-day, Yaohong builds them. You'll see both halves today.

---

### Slide 4 — The shift is here
**Lead:** Tina · 2 min

**Tina:** This is not a "AI is coming" deck. AI is here. The gap between teams that have adopted it and teams that haven't is widening every quarter, and it's already big.

Three numbers worth saying out loud. *(point at the slide — don't read all of them, pick adoption + one)*

Eighty-seven percent of marketing teams use generative AI in some form. Fifty-seven percent already have agents running in production. That's not a forecast — that's where the floor already is.

And the time saved is real. Six hours a week on average — for senior practitioners it's eight to ten. That's not "we're more productive in some vague way." That's one full work-day a week, back.

**The reason we're spending three hours together today is to make sure you're on the right side of that curve.** Not next quarter — this week.

---

### Slide 5 — Role has changed
**Lead:** Tina · 3 min

**Tina:** While you've been doing your job, the job itself has changed.

The old version of marketing — most knowledge work, really — was *execution.* You ran campaigns. You wrote the brief. You pulled the report. You did the work yourself, hour by hour.

The new version is *orchestration.* You design the system that runs the campaign. You write the agent that drafts the brief. You build the workflow that pulls the report every Monday before you wake up. The work still happens — but you're no longer the one executing every step.

There's a name for this role now. *Marketing engineer.* Three thousand-plus open roles for it. Up two hundred and five percent year over year.

Emily Kramer at MKT1 put it well — and I'll just quote her: **"With tools, you are the operator. With agents, you are the manager."**

That shift is what today is preparing you for.

---

### Slide 6 — This is, this isn't
**Lead:** Tina · 1 min

**Tina:** Quick set-expectations before we dive in.

The three hours today will give you three things. One — vocabulary. Words you've half-heard but never used confidently. *Skill. Agent. Hook. Gate. MCP.* By the end you'll use them without flinching.

Two — a mental model. How agents actually work under the hood, so that when something breaks, you have a guess at why.

Three — real examples. We'll do three live demos, you'll build one yourself in a breakout, and we'll walk through what a working agent harness looks like.

What this is *not* — it's not an engineering class. You won't be writing code. You'll be designing workflows. And by the end, you'll catch yourself saying *"that should be a hook, not a rule"* — and your team will know what you mean.

We have a mix of vocabulary today — some of it is technical for non-technical folks. That's exactly why we're here. I'll explain what each thing means and why it matters, so by the end you can take the first step — building skills, building systems, building your own agent harness.

---

### Slide 7 — Automation · Augmentation · Agency
**Lead:** Tina · 4 min

*This is the big-three-modes slide. Tina admitted in rehearsal that she got tangled here. Practice the three-way distinction. Don't get philosophical — use the cards.*

**Tina:** Three modes of working with AI. Not "agents versus workflows" — three different ways AI can sit in your day.

**One — Automation.** This is your Zapier, your n8n, your Make. You wire it once, and the same thing happens every time. *Trigger A fires, action B runs.* No judgment. Deterministic. Great for "every Monday at 9am, send this report."

**Two — Augmentation.** This is most of what you do in Claude.ai or in Cowork right now. You're in the loop on every step. You prompt — *do this, send that, draft this.* AI works alongside you, turn by turn. You're driving every decision.

**Three — Agency.** This is what we're going to teach today. You configure AI to work *independently* in a defined area. You set the rules, the agent makes the steps. Sometimes it makes its own judgment. **Automation runs the predictable. Augmentation boosts you in the moment. Agency runs while you sleep.**

*If a question lands on "what's a real agent right now?" — fallback: managed agents in Claude, or Yaohong's customer-support example: an agent that figures out which service to pull data from, calls the right API, decides how to reply. Don't dwell. We'll have a live one on screen later.*

---

### Slide 8 — Claude feature map
**Lead:** Tina · 2 min

*Big infographic. Orient them; don't try to cover every surface.*

**Tina:** Quick orientation. Claude is one model — one brain — but it shows up in ten different places. Same brain, different doors in.

Today we're not going to cover all ten. We're going deep on four — the ones highlighted in orange. **Claude Code. Connectors. Skills. Claude in Chrome.**

The rest are always one step away from what you'll learn here. Same vocabulary. Same patterns.

---

### Slide 9 — Three harnesses
**Lead:** Tina narrates · Yaohong demos on screen · 3 min

*This slide was trimmed from the dense table to three cards. Read the metaphor cleanly.*

**Tina:** For agentic workflow, focus on three interfaces. Same brain, different doors in.

*(point at card 1)* **Claude.ai.** Smart colleague on chat. Quick turns. Think, write, analyze. You drive every step.

*(point at card 2)* **Cowork.** Delegated assistant in a sandbox. This is where most of your daily knowledge work lives — about eighty percent of it. It browses, edits files, runs longer tasks. You hand it a job and walk away for a few minutes.

*(point at card 3)* **Claude Code.** An agentic system you build with. Full file access, git, shell, hooks, agents. This is where reusable systems live — the ones your team shares.

Quick rule of thumb for "which one." If the tool you want to use has an open API — like Google Search Console, like Stripe, like your CRM — reach for Claude Code, because it can call that API directly. If the tool blocks programmatic access — LinkedIn search, Instagram, anything behind a login that doesn't expose an API — reach for the browser. Cowork, or Claude in Chrome. Claude logs in like a human, clicks like a human, reads what's on screen.

**Yaohong — show them.** *(Yaohong screen-shares.)* Open Claude.ai. Show one quick prompt. Then open Cowork — show the sandbox UI, the side panel. Then open Claude Code in the terminal. Then open the marketplace. Sixty seconds each, no demos yet — just orient them on what each interface looks like.

---

### Slide 10 — How coding assistants work
**Lead:** Tina · 2 min

**Tina:** Stay with me on this one — it's the most important conceptual slide we have today.

How does a coding assistant — or any agent, really — actually work?

The model itself just *thinks.* That's all it can do natively. What lets it do anything in the real world is the *harness around it.*

Three steps. *(point at the diagram)*

**One — gather context.** It reads the error message. It opens the relevant files. It looks up the docs. It figures out what's actually going on.

**Two — formulate a plan.** It decides what to change. Which files. Which tests will tell it whether the change worked.

**Three — take action.** It actually edits the file. Runs the test. Hits the API. Then it loops back to step one to check if the result is what we wanted.

The key insight — and this is what makes Code and Cowork different from chat — is that steps one and three require the model to reach *outside the chat.* Read files. Run commands. Call APIs. That's **tool use.** That's why these interfaces exist instead of just plain chat.

The model thinks. The harness gives it hands.

A concrete example from this morning. *(Tina-vouches example)* I was working on a landing page and it had a styling error. I told Claude Code: "find the error and fix it." It opened the file. Read the CSS. Read the relevant docs. Wrote the fix. Ran the page. Confirmed the fix worked. Five minutes, zero of my time on the actual editing.

---

### Slide 11 — Artifacts vs Skills
**Lead:** Tina · 2 min

**Tina:** Two words you'll hear a lot today — and they sound similar but they're very different.

An **artifact** is *a thing produced.* A rendered output — an HTML page, a dashboard, a Mermaid diagram, a Markdown report. It lives in the conversation. When the conversation ends, the artifact ends, unless you save it.

A **skill** is *a process for producing things.* A markdown file on disk that says: "here's the name, here's when to use this, here's how to do it." Lives forever. Auto-loads every future matching session.

The two compose. *A skill produces an artifact.* My `/build-dashboard` skill is the recipe. The React dashboard it drops into the artifact panel is the output.

Yaohong used this last week — he was rebuilding his training program. *(Yaohong, briefly)* He had a long chat with Claude about phase one of his training plan. Instead of giving back a long markdown response, Claude generated a working HTML file — a JavaScript-driven phase-one plan he could actually click through. That's an artifact. The skill behind it is the recipe.

The limitation of an artifact alone: it's not directly runnable, and it doesn't pass cleanly from one session to the next. That's why we also have skills.

---

### Slide 12 — Claude in Chrome
**Lead:** Tina cues · Yaohong demos live · 2 min (demo may stretch)

*Demo agreement: Tina prompts, Yaohong opens Chrome. Pre-agreed killer example is scraping competitor pricing — direct hit on Tiket's pain.*

**Tina:** Claude in Chrome is a browsing agent that operates *your* logged-in browser. Reads the page. Clicks through. Fills forms. Completes tasks.

The reason that matters — it runs in *your* session. So Instagram. LinkedIn. Your internal portals. All of them are accessible, because Claude is logged in as you.

We typically reach for it when there's no API to use. For example — Instagram or LinkedIn. If you try to scrape them programmatically, you get blocked. Claude in Chrome doesn't scrape — it browses, the same way you do.

**Yaohong — open the browser. Show them.** *(Yaohong opens Chrome live.)*

**Yaohong:** You can automate a lot of browser tasks this way. *(navigate live to a competitor's site — e.g., a competing Indonesian travel site)* If I want to pull pricing for the same activity across three competitors, I just ask Claude to do it. It opens the page. Finds the price. Pastes it into a sheet. Goes to the next competitor.

**Tina:** What that previously took to do programmatically — serious engineers, multiple weeks. Now it takes one prompt.

---

### Slide 13 — Tool use
**Lead:** Tina · 2-3 min

*This slide was trimmed. The image is on the left with concrete examples. The Playwright box is on the right. Don't go deep on the toolbox distinction — keep it concrete.*

**Tina:** Tool use is what turns a chatbot into something that can *do* things. On its own, an LLM is text in, text out. That's it. It thinks, it writes — but it can't reach anything.

Tool use is when the model says *"call this tool"* and your computer does the calling.

*(point at the augmented LLM diagram)* Three things hang off the model in this picture.

**Retrieval.** Looking things up. *"Pull last week's GA4 traffic."* The model doesn't know GA4 — it asks the GA4 connector to go get the numbers.

**Tools.** Taking action. *"Edit the README, run git commit."* The model doesn't edit the file — it calls the file-edit tool, then the git tool.

**Memory.** Remembering across turns. *"My voice. The banned-words list. The skill I just wrote."* So the model doesn't start from zero every time.

A live example from building this very deck. *(point at the Playwright box on the right)* Every slide I edited this morning triggered Claude to open this deck, screenshot it, and read it back to verify the change. That's Playwright MCP — a tool that lets Claude drive a real Chrome window. Cowork can't add Playwright. Claude Code can. That's the difference.

If a tool has an API, Code can use it. If it doesn't, you reach for the browser. *(callback to Slide 12)*

---

### Slide 14 — Connectors. MCP. Plugins.
**Lead:** Tina + Yaohong tag-team · 3 min

*This was the most contentious slide in rehearsal. The disclaimer banner at the top is the fix — call it out, then walk the table.*

**Tina:** Three words people confuse all the time. And in fairness — Anthropic keeps changing what they call them.

*(read the disclaimer banner at the top)* Heads up — Anthropic now calls all of these "connectors" in the UI. The table below is what's underneath. What each one actually is.

**Cowork Connectors.** Prebuilt integrations Anthropic ships. Gmail, Drive, Calendar, Notion. One click, you're in.

**MCP — Claude Code.** Open protocol. Any tool with an API can be wired in. You, your team, or the open-source community can build them. This is how Claude reaches your CRM, your internal tools, your Stripe.

**Plugins.** Different category. Plugins are *packaging.* A plugin bundles skills, commands, agents, hooks, and MCP servers together. So when you install one plugin, you get a whole workflow set up in one click.

**Yaohong** — quick concrete example.

**Yaohong:** *(show a plugin, e.g. a sales plugin)* This is a sales plugin. When I install it, I get a bunch of skills bundled in — `/account-research`, `/draft-followup`, all that. The plugin also pre-wires the connectors I need — Slack, HubSpot, Motion. So when I type `/account-research`, it asks me *"are you using Slack or HubSpot or both?"* and routes the workflow. One install, the whole stack ready.

**Tina:** **Connectors and MCP are how Claude reaches tools. Plugins are how you package and share a working setup.** MCP is the USB port. A plugin is the boxed kit — port, cables, and instructions shipped together.

---

### Slide 15 — MCP in action
**Lead:** Tina · 2 min

**Tina:** Let me make MCP concrete with a flow a marketer actually cares about.

You're in Cowork. You ask — *"give me last week's GA4 traffic, plus a summary I can send to the team."*

Without MCP, Claude can only answer from what you paste in. It would say *"I can't access your GA4."* End of conversation.

With MCP, what happens is — Claude sees the request. It checks the connectors you have wired up. It sees that you've connected GA4. It picks GA4 as the right tool. It calls the GA4 connector — that's MCP under the hood — and the connector goes and grabs the real numbers from your account. Claude reads those numbers, writes the summary, and gives you the answer.

You don't see any of that plumbing. You just see — *here's last week's traffic, here's the summary, ready to send.*

I'll vouch for this personally. The very first thing I did when I started using Claude Code was wire up Google Search Console. We'll see that live in Demo 2.

Without MCP, Claude is guessing. With MCP, Claude is reading. The difference shows up in your output every time.

---

### Slide 16 — Where Connectors live
**Lead:** Tina · 1 min

*Heads-up: Anthropic moved Connectors from Settings to Customize. The slide path label and the in-app redirect banner reflect this.*

**Tina:** Quick orientation on where to find Connectors in the product.

In claude.ai, go to Customize, then Connectors. *(point at slide)* Anthropic recently moved this — used to be under Settings. If you still see Settings on your account, there's an in-app banner that redirects you. *(point at the screenshot showing the banner)* That's the page.

Anthropic-maintained connectors are one click to install. Most of what you'd want — Gmail, Drive, Calendar, the usual suspects — is already there.

If you want to add a custom connector — say, for an internal tool — that's where you'd add it, but it requires creating an app in Google Cloud Console first. *(Yaohong, brief)* That's a step-two workshop. For today — you can follow Anthropic's instructions in the docs. We won't set one up live.

---

### Slide 17 — Where Plugins live
**Lead:** Tina · 1 min

**Tina:** Plugins live in the Claude Desktop app. Customize, then Personal plugins, then click the plus button to open the Plugin Directory.

The Plugin Directory is essentially an app store — but for agentic workflows. Anthropic is sourcing credible third parties and listing them there. Brand voice plugins. Operations plugins. Design, Finance, Marketing.

Think of it like the App Store, but for the agentic world. Very powerful — and it's where most of the leverage is going to come from in the next twelve months. One plugin can give you ten ready-made skills, three connectors, and a handful of agents pre-wired.

---

### Slide 22 — When to use a skill *(open the skills section here)*
**Lead:** Tina · 2 min

*Verbal re-order — open the skills section with this slide before clicking into Slide 18 (definition). Land the "second time you say it" line.*

**Tina:** Before I tell you what a skill *is,* let me tell you *when* you need one.

**Rule of thumb — if you find yourself explaining the same thing to Claude over and over again, that's a skill waiting to be written.**

Examples — you keep re-describing your PR feedback format. You re-paste your commit message style every single time. You re-explain your brand voice. You re-describe your audit method.

Second time you say it — make it a skill.

OK. Now — what is a skill?

---

### Slide 18 — What is a skill
**Lead:** Tina · 2 min

**Tina:** A skill is a *folder of instructions* that Claude can discover and use on its own.

The structure is straightforward. Every skill has a file called `SKILL.md`. That file starts with a name, a description, and optional configuration. Then the body explains what to do.

The way it gets activated — Claude scans the description of every skill in your library. When your request matches one of those descriptions closely enough, Claude auto-loads the skill body and follows it.

You teach Claude once. It applies the rule forever, without you repeating yourself.

Skills are how knowledge persists across conversations. Without skills, every new chat starts from zero — you have to re-explain your context every time. With skills, Claude already knows.

---

### Slide 19 — Anatomy of a skill
**Lead:** Tina · 2 min

**Tina:** Quick anatomy. A skill is a folder. Inside the folder, four things — but only one is required.

**One required file — `SKILL.md`.** The operation manual. Name. Description. Steps.

**Three optional folders.**

**References** — for rules you want Claude to load on demand. Brand guidelines. Compliance checklists.

**Scripts** — for code that runs as part of the skill. Python scripts, shell scripts.

**Assets** — for templates. Email templates. Deck templates. Any file the skill outputs *from* rather than *about.*

Each optional folder adds leverage only when needed. They load on demand — they don't sit in Claude's working memory all the time. That keeps things cheap and keeps Claude focused on the task in front of it.

And because the whole skill is just files in a folder — you can put it in git, share it with the team, version it like code.

---

### Slide 20 — SKILL.md
**Lead:** Tina · 2 min

**Tina:** Let's zoom into the one required file.

`SKILL.md` is the operation manual for the skill. Two parts.

**The frontmatter.** Three or four lines at the top in YAML. Name. Description — and this is the most important line, because the description is the *trigger.* If your description is fuzzy, Claude won't find the skill. We'll come back to that.

**The body.** Markdown. Answers three questions. *When* should this skill run? *How* does it run? *What* does it output?

My own `/prospect-audit` skill is a good example. The trigger says — "when a user wants a comprehensive AEO and SEO audit for a prospect or current client." The body has the twelve phases. The references folder has the framework. The scripts folder has the actual audit code.

When someone says "do a prospect audit for company X," Claude reads my description, matches the request, loads the skill, runs the twelve phases. I never have to re-explain.

---

### Slide 21 — How to invoke a skill
**Lead:** Tina · 2 min

*The cost-comparison table was removed in the last commit — deliver only the auto-invoke story now.*

**Tina:** Three ways to activate a skill.

**One — type a slash command directly.** `/affiliate-report`. Claude loads that skill immediately, runs it. Fastest if you already know the name.

**Two — describe what you want, and let Claude find the skill.** *"Write me the monthly affiliate report."* Claude scans the descriptions of every skill you have. Matches the request to *affiliate-report.* Loads the skill body. Runs it. You never typed a command.

**Three — build matching scenarios into the description itself.** This is how power users get auto-invoke right. You write the description to anticipate the phrasing your team actually uses — "monthly report," "affiliate breakdown," "performance roll-up." So when anyone on the team asks for any of those, the right skill fires automatically.

The point — skills don't load on every message. They don't load just because you type a slash. They load when Claude *needs* them. That's how you keep your working memory clean while still having a hundred skills available.

---

### Slide 23 — What makes a good skill
**Lead:** Tina · 2-3 min

*If time is tight, just land the "description is the trigger" rule and move on.*

**Tina:** Five rules for skills that actually fire when you need them.

**One — sharp description.** The description IS the trigger. If you write *"affiliate tool"* — Claude will never find it. Write what someone would actually type when they need it. *"Generate the monthly affiliate report from Stripe + Mailchimp data."*

**Two — one job per skill.** Don't bundle. *Generate the report* is one skill. *Send the report to the team* is a different skill. Bundling makes the description fuzzy and the body bloated.

**Three — name its inputs.** What does this skill need to be given? A date range? A client name? Be explicit at the top.

**Four — short body, linked references.** The body should be the recipe. Long context — guidelines, examples — goes in `references/` and loads on demand.

**Five — testable output.** Be specific about what "done" looks like. *"A markdown file with three sections, ending with a CTA paragraph."* Otherwise Claude might call itself done before you would.

**Land it — the description is the trigger. The body is the recipe. References are the pantry. Load only when cooking.**

---

### Slide 24 — What is an agent
**Lead:** Tina · 2-3 min

**Tina:** Now agents. Important — and a bit different from skills.

An agent is a *specialist* with its own whiteboard. Its own fresh context window. Its own role, tools, and instructions.

The structure — a markdown file in `.claude/agents/`. Same format as a skill, basically — frontmatter plus body. But what it does is different.

When you call an agent, you spin up a fresh subagent in a clean context. It does the work. It returns *only a summary* to you. Its own working memory stays separate — it doesn't pollute yours.

That last part is the magic. When you have an agent do a heavy research task — say, scrape ten competitor websites — all that scraped content lives in the agent's context, not yours. You get back a clean summary.

When do you reach for an agent?

**Judgment work** — when the steps aren't fixed and the agent needs to decide based on what it finds.

**Heavy research** — when the work would burn through your own context window if you did it in the main chat.

Skill is *"do this thing the same way every time."* Agent is *"figure out the right thing to do, then do it, and report back."*

---

### Slide 25 — Agents differ
**Lead:** Tina · 2 min

**Tina:** Same base model. Different role. Different tools. Different instructions. That's what makes one agent different from another.

Let me show you mine.

I have two writers in my system. One is `/linkedin-writer` — it writes my personal LinkedIn posts. It's trained on my rejections — every time I've written a draft I didn't like, that learning goes back in. It knows my voice. It runs a ten-criterion eval before it ever shows me a draft.

The other is `/writer` — it writes for SEO clients. Completely different role. It adapts to the client's voice — not mine. Different tool stack. Different evaluation criteria.

Same Claude model. Two completely different writers. The orchestrator — me — is what makes them different.

The takeaway — same base model, but the *role you assign* is what makes the output specific to your business. Don't think "I need a better AI." Think "I need a sharper agent."

---

### Slide 26 — Skill vs Agent
**Lead:** Tina · 2 min

*Keep this short — it's the punchline before demos.*

**Tina:** Quick framing before the demos.

Skill = recipe card. One repeatable procedure. Cheap to run.

Agent = specialist chef. Judgment work. Their own whiteboard.

**If you could write the steps out in advance — it's a skill.**

**If you need judgment, or you'd dump a lot of files into your working memory by doing it in the main chat — it's an agent.**

That's it. Now demos.

---

## Demos · live

### Slide 27 — Demos divider
**Lead:** Yaohong · 1 min

**Yaohong:** Three demos coming up. Same prompt. Two different tools. We'll show you where each one lands and where each one breaks.

*(preview)*

**One** — find premium Indonesian travel influencers on Instagram and drop them into a Google Sheet.

**Two** — pull a Google Search Console period-over-period analysis.

**Three** — generate a TikTok ad pipeline from a Tiket activity page.

We'll run each demo on Cowork and Claude Code side by side. The point is not *which one wins.* The point is *where each one stops* — and how that maps to what you're trying to do.

---

### Slide 28 — Demo 1 · Influencer research
**Lead:** Yaohong · 5 min live

*Tested Thursday night. Both tools should work.*

**Yaohong:** Same prompt — *"find premium Indonesian travel influencers on Instagram, give me their handles, follower counts, engagement rates, and put them in a Google Sheet."*

**Cowork.** I'll use Claude in Chrome plus the Sheets connector. *(run live)* It opens Instagram, navigates, pulls the data — comes back with fifteen-plus influencers, structured into a sheet.

**Claude Code.** Same prompt. Different stack — Playwright MCP plus a Sheets MCP. *(run live)* Same outcome. Fifteen-plus influencers in a sheet.

**Both work.** Same brain. Different harness. The result is essentially the same.

The difference shows up in the next demo.

---

### Slide 29 — Demo 2 · GSC period-over-period
**Lead:** Yaohong · 5 min live · Tina may chime in at the open

*Tina vouches before Yaohong runs — anchors that this is her actual lived workflow.*

**Tina:** Quick note before Yaohong runs this — the very first thing I did when I started using Claude Code was wire up Google Search Console. So this demo is not theoretical for me. It's how I run my own SEO work every week.

**Yaohong:** Same prompt — *"give me period-over-period analysis of our top queries from Google Search Console for the last 30 days."*

**Cowork.** *(run live, then hit the wall)* It comes back with — *"I don't have access to Google Search Console."* Because Anthropic hasn't built a GSC connector. Dead end.

**Claude Code with the GSC MCP.** *(run live)* Pulls thousands of queries. Compares last 30 days to the previous 30. Surfaces the queries that moved. Writes the summary.

**You're not limited to what Anthropic pre-builds.** You connect what you need. That's the whole game.

*(brief flag — the GSC connector requires Google Cloud Console app creation. We're not setting that up live today. We're running a pre-built MCP. The setup is documented — you can do it yourself in 30 minutes.)*

---

### Slide 30 — Demo 3 · Video ad pipeline
**Lead:** Yaohong · 5 min live (most ambitious demo)

*Tina sets up the framing — what we want, why we want it. Yaohong runs the chain. By end of this demo, expect ~90-120 min elapsed. Plan break right after.*

**Tina:** Last demo before the break. This one's the most ambitious.

Imagine you want a TikTok ad. Source material — a Tiket activity page. You want the script written from the page. You want a local-looking avatar speaking it. You want real photos from the activity. Voiceover throughout. And before any of it runs, you want Claude to walk you through the plan first — so you can correct it before it generates anything.

**Cowork.** *(setup)* Cowork can draft the script. It can sketch the storyboard. But it can't reliably scrape the page *and* call HeyGen or Seedance *and* chain those tools together. So Cowork gives you the script — you have to do the rest.

**Claude Code.** *(Yaohong runs)* Chrome MCP scrapes the page. Generates the script. Calls HeyGen MCP for the avatar. Calls Seedance MCP for the voiceover. Assembles the pipeline. By the end — a draft TikTok ad you can review and ship.

**Tina:** That's the shift we've been building up to. Cowork is your advisor. Code is your operating system. *(beat)* Now — break.

---

### Slide 31 — Breakout · Build one
**Lead:** Both · 30 min activity

*Realism flag — set the bar honestly. The goal is "description + first paragraph of body," not "working skill."*

**Tina:** OK. You've watched us — now your turn.

Teams of four. Thirty minutes on the clock. Build a skill, or an agent, that solves *one real task from your desk.*

The goal — and this is on the slide — **write the description plus one paragraph of the body. Not a working skill.** The bar is: could someone else read this and know what to build?

Three steps. *(point at the cards)*

**Pick.** A task you do every week that takes at least an hour. Don't pick something theoretical — pick a real Monday-morning chore.

**Build.** Name it. Write the description — that's the trigger. Draft the body — that's the recipe.

**Sell.** In two minutes — what it does, when to use it, who runs it.

Yaohong and I will float between teams. If you get stuck on the description — that's where most teams get stuck — flag us, we'll help.

One team per group will demo after the break. Pick your strongest one.

Clock starts now.

---

### Slide 32 — Break
**Lead:** — · 10 min

*This break is real. They'll be saturated at the 2-hour mark. Restart on time matters — Section 2 is the dense conceptual chunk.*

**Tina:** Ten-minute break. Bathroom, coffee, stretch. We're back at *(time)* sharp. Section 2 — the harness — is the part that ties everything together, so don't be late.

---

### Slide 33 — Show and tell
**Lead:** Both · 10-15 min

*If no team has a full draft, pivot to "describe what you'd build and why."*

**Tina:** Welcome back. Quick round of show-and-tells. Two minutes per team. Tell us — what's the skill, who runs it, what does it do.

We'll give you live feedback on four things —

**One — is the description sharp enough that Claude would actually find it?**

**Two — is the scope right? One job, not five.**

**Three — did you pick the right tool? Skill or agent? API or browser?**

**Four — is the first line of the body the right starting point?**

The question we'll keep asking — *"would you reach for this on Monday?"* If the answer is no, the description is too fuzzy or the scope is wrong. We'll fix it together.

---

## Section 2 · The harness

### Slide 34 — The .claude folder
**Lead:** Tina · 3 min

**Tina:** Now we get into how you give Claude persistent business context. So that when you sit down to work Monday morning, Claude already knows your voice, your rules, your playbooks — without you re-explaining.

The mechanism is a folder. `.claude` — lives in your project. Or in your home directory globally.

Let me walk you through what's in mine.

**`CLAUDE.md`** — the always-loaded brain. My voice rules, my workflow preferences, things I never want to repeat.

**`settings.json`** — permissions and configuration. What tools Claude can call without asking. What MCPs are wired up.

**`hooks/`** — the tripwires. We'll cover these in detail in a minute.

**`agents/`** — fifteen project agents I've built. Each one a specialist.

**`commands/`** — sixty slash commands I can fire.

**`skills/`** — seventy skills the team can call.

That's roughly the shape. The brain is Anthropic's — same for everyone. The *harness* is what makes it yours.

---

### Slide 35 — Context window · what it is
**Lead:** Tina · 3 min

*Section 2 is the dense conceptual chunk. May get compressed if running long — don't apologize, just deliver tight.*

**Tina:** Now the concept behind almost every frustration you've had with Claude. The context window.

**What it is.** The total amount of text Claude can reference in any one conversation. That includes — your messages, Claude's responses, files Claude has read, tool results, system instructions, your CLAUDE.md, your memory. *Everything in this conversation* counts.

**What it is not.** It's not long-term knowledge. It's not unlimited. It's not persistent across sessions.

The context window is *working memory.* When the conversation ends, the working memory resets. Next conversation starts from scratch — unless you've persisted things into skills, memory, or CLAUDE.md.

Most of the "Claude got forgetful" frustration you've felt — it's not Claude getting dumber. It's the working memory filling up.

---

### Slide 36 — Congestion signs
**Lead:** Tina · 2 min

**Tina:** Six signs your context window is congested.

**One** — Claude forgets instructions you gave twenty turns ago.

**Two** — output gets generic. Less specific, less you.

**Three** — agents become inconsistent. Same request, different outputs.

**Four** — steps get dropped. The skill ran, but one phase got skipped.

**Five** — Claude re-asks for information you already gave it earlier in the same chat.

**Six** — your voice drifts. Claude starts sounding like the average AI again.

The instinct when this happens — *"let me just repeat the rule."* **Don't.** That actually makes it worse — you're adding more text to an already-full working memory.

What to do instead — reset, offload, or compact. We'll cover those in a minute.

**Symptom is not bug. It's context physics.**

---

### Slide 37 — Brain infographic
**Lead:** Tina · 2-3 min

**Tina:** Visual model of what's in the working memory at any given time.

Everything you see on this slide flows into *one* brain, sharing *one* ceiling — currently one million tokens for Claude Code, much less for chat.

**Left side.** Stable context — your CLAUDE.md, your MEMORY.md, the list of skills available, the list of MCP tools available. This stuff is mostly the same every session.

**Right side.** Dynamic context — the conversation itself, files Claude has read, screenshots, tool results, Claude's own answer.

The killer is the right side. A single tool result can be five thousand to fifty thousand tokens. One MCP call to a big API, plus a long PDF you uploaded, plus a twenty-turn conversation — you're at thirty to forty percent of the ceiling, easily. And accuracy starts dropping long before you hit the ceiling.

---

### Slide 38 — What counts toward window
**Lead:** Tina · 2 min

**Tina:** Quick bar chart. Relative cost of each thing.

CLAUDE.md — small. A few hundred to a few thousand tokens. You can afford it.

MCP tool lists — bigger. Every MCP server you enable contributes its tool descriptions to the working memory. Ten MCPs adds up.

A single tool result — the biggest. Five thousand to fifty thousand-plus tokens. One full HTML page read, one big SQL query result, one long PDF — that's the equivalent of ten CLAUDE.mds.

**A single tool call can cost more than your whole brain file.** Plan accordingly.

---

### Slide 39 — Where to put context
**Lead:** Tina · 3 min

**Tina:** Where do you put what?

I use a whiteboard metaphor — think of six different surfaces in a workspace.

**CLAUDE.md = permanent marker.** Stuff you want Claude to know *every time.* Your voice. Your rules. Loads always.

**MEMORY.md = sticky note.** Stuff you want Claude to remember *across sessions* but maybe not every turn. Recent corrections. Recent feedback.

**PROGRESS.md = desk notebook.** Where you're at on a specific project. Updated as work happens.

**Skills = filing cabinet.** Knowledge organized by topic. Pulled out only when needed.

**Agents = their own whiteboard.** Subagents have separate context windows. What's on their board doesn't show up on yours.

**Hooks = wall stamps.** They run on triggers, not on context. Zero context cost.

Quick rule — **whiteboard, cabinet, desk, or wall?** That's the question to ask before you put anything into Claude's working memory.

---

### Slide 40 — Context rot
**Lead:** Tina · 3 min

**Tina:** Here's the counterintuitive part. *Bigger context is not better.*

Researchers measured this. At turn one of a fresh conversation, hallucination rate is about two percent. By turn twenty, it's ninety-five percent.

The window doesn't get smaller. The *accuracy* gets worse. Because the model is trying to attend to too many things at once.

How to fix it —

**One — trim CLAUDE.md.** Anything you haven't used in two months, archive.

**Two — split into skills.** Things in CLAUDE.md that are only needed sometimes belong in a skill.

**Three — persist to PROGRESS.md.** Long projects belong on disk, not in chat.

**Four — `/compact`.** Summarizes the conversation so far and keeps the summary, drops the rest.

**Five — `/clear`.** Just starts fresh.

**Six — delegate to subagents.** Heavy research that doesn't need to be in your view goes to a subagent. Their context, not yours.

**It's not about saving space. It's about output quality.**

---

### Slide 41 — Post-mortem · v2 vs v3
**Lead:** Tina · 5 min

*This is the hook for hook-and-gate. Drive into Slides 42-44 hard after this.*

**Tina:** Real war story from my own work. The prospect-audit skill.

Version two — the one that broke — shipped me a report that hallucinated keyword counts. Said the prospect had 27,659 keywords. Real number, from Ahrefs — 15,164. Swapped two Core Web Vitals metrics. Got the prospect's name wrong in one section.

I was about to send that to a real client. Caught it because something looked off — not because the system caught it.

Why did v2 break? One agent. One thousand seven hundred ninety-one lines of skill. Eight phases run in a single window. By phase seven the working memory was over one hundred thousand tokens. The rules I'd set in phase zero — *"only quote numbers you've actually fetched"* — were drowned in three hundred pages of context by the time it got to phase seven.

Version three — the rebuild. *(point at the diagram)* I broke it into three parts. An *orchestrator* that just routes. A *collect* subagent that pulls all the data — lives in its own context. A *report* subagent that writes — also its own context. And three Python gates between them that check the data before the next phase starts.

Numbers per phase dropped from one-fifty thousand to ten-to-fifteen thousand. Hallucinations dropped to zero.

The point — **the skill wasn't the problem. The architecture was.** And the key piece — **the model can't hallucinate past a Python exit code.** That's the hook-and-gate idea, which is the next slide.

---

### Slide 42 — Agent · Hook · Gate
**Lead:** Tina · 3 min

*This is where the workshop's payoff line lands. Make it explicit.*

**Tina:** Three concepts that work together. The harness.

**Agent.** One job per worker. Fresh start. Own whiteboard. We covered this.

**Hook.** A tripwire that *your computer* runs — not Claude. Fires automatically when something happens. *On save. On edit. On commit.* Doesn't depend on Claude remembering to check anything.

**Gate.** A code check Claude can't argue with. A Python script that returns pass or fail. Numbers don't lie. If the gate fails, the next step doesn't run.

These three together — that's the harness. Hooks fire the gates. The rule runs without you. Together they are the system that runs your operations.

Remember the payoff line from Slide 6? **By the end you'd say "that should be a hook, not a rule."** This is the slide where that lands. From here on, every time you find yourself writing the same instruction to Claude — ask, *should that be a hook?*

---

### Slide 43 — Learnings loop
**Lead:** Tina · 2-3 min

**Tina:** Hooks aren't just for cleanup or enforcement. They're also how the agent *learns.*

Here's the pattern — when I correct Claude on something, the on-stop hook writes one line to my CLAUDE.md or MEMORY.md. Automatically. I don't have to remember to do it.

Next session — Claude reads that line at boot. Same mistake doesn't happen again.

This is not fine-tuning. No model weights are changing. No GPU. No data team. Just a shell script that appends one line to a file.

**Never let a correction evaporate.** That's the principle. Every time you push back on Claude — that push-back has value. The hook captures it. Future you benefits.

---

### Slide 44 — Slop-check example
**Lead:** Tina · 3 min

**Tina:** Concrete example tying hook and gate together. The one I run on every blog post and LinkedIn draft.

When I edit a markdown file in my Novastacks content folder — that triggers a `PostToolUse` hook. Pattern matcher in `settings.json` looks for *Edit* or *Write* on those paths.

The hook runs `linkedin-slop-check.py`. That's the gate. It's a Python script. It reads the file, scans for banned phrases — *"isn't X. It's Y"*, *"in today's fast-paced…"*, *"game-changer"* — that's my personal slop list, built up over years of catching myself writing AI-flavored copy.

The gate returns a score and a list of flagged phrases. The hook injects that back into Claude's context, so when I look at the draft, the slop list is right there in front of me.

I built the list once. The check runs forever. *Without me.*

That's the move — **set up the rule once. Build your list once. The check runs forever.** Your style preferences, your brand voice rules, your compliance checklist — anything you'd want to verify on every output — that's a candidate for a hook-and-gate pair.

---

## Section 3 · Team orchestration

### Slide 45 — Git is the new Notion
**Lead:** Tina narrates · Yaohong demos · 3 min

*Tina does the metaphor. Then Yaohong does a live edit-and-commit on this very deck.*

**Tina:** Git is the new Notion. And it's *smaller* than Notion.

For anyone who's never used git — five commands.

`pull` — get the latest version of whatever the team is working on.

`status` — see what's changed locally that hasn't been saved yet.

`commit` — save a version.

`push` — share that version with the team.

`log` — see who changed what, when.

That's it. With those five, an entire team of agents and humans can edit the same files without stepping on each other.

Without git — you end up with one hundred versions of "the affiliate report." With git — one canonical version, full history, instant rollback if someone breaks something.

*(flag to the technical attendees in the room)* — for the engineers, this part is not new. The framing — *Git as Notion* — is for the rest of the room.

**Yaohong — show them.** *(Yaohong opens Claude Code on this deck. Makes a small edit. Commits. Pushes. Pulls from another window to show the change syncing.)*

**Yaohong:** And the install — *(brief)* — git itself is a separate step. We're not installing it on stage today. That's workshop number two. For today — know that this is the rhythm: pull, edit, commit, push.

---

### Slide 46 — Yaohong's team orchestration
**Lead:** Yaohong · 5-7 min

*Yaohong's segment. He'll run this on the spot. Three anchor points on the slide so the room has something to look at.*

**Yaohong:** Quick walkthrough of how we run things at Superuser HQ day to day.

Three patterns —

**One — edit this deck live.** Same way you saw on the last slide. Every team member can pick up a project file, edit, commit, push. The agent picks up from where the human left off, and vice versa.

**Two — git pull / commit / push is the daily rhythm.** Not a once-a-week ceremony. Multiple times a day. Small commits. Clear messages. So that when something breaks, you know exactly which change caused it.

**Three — one worker, one job.** This is the pattern from earlier — agents have their own context. We've extended that across people. Each team member owns a clear slice. Agents run inside those slices, not across them.

*(Yaohong fills the rest with whichever live story or screen-share lands best in the room.)*

---

### Slide 47 — Closing
**Lead:** Both · 1 min

**Tina:** Thank you. Now go build something.

Quick arc recap. We started with — *the same brain across ten different doors.* We moved to — *that brain plus tools is what makes it an agent.* Then — *that brain plus tools plus a harness is what makes it run while you're not watching.*

That's the shift. From *personal assistant* to *system that runs your operations.*

Resources are on the next page. We'll stay for Q&A.

**Yaohong:** Find us on LinkedIn. Or write your first skill tonight and tag us — we'll review it.

---

## Appendix (skip in main flow · open on request)

### Slide 48 — Appendix divider
*Not in main flow. Skip in the 3-hour workshop.*

### Slide 49 — Handoff to Yaohong (appendix)
*Optional interlude into a live build-along — only if the room asks "show us the actual build."*

### Slides 50-54 — Build-along (Layer 1 fetch → Layer 5 wrap)
*Five-layer build-along — partner-performance report example. Fetch → Enrich → Analyze → Format → Wrap. Only run if requested.*

### Slide 55 — The pattern
*Universal shape — Fetch → Enrich → Analyze → Format → Wrap. Skip in main flow.*

### Slide 56 — Safety envelope
*Three concentric layers — Permissions (can't), Hooks (system enforces), Instructions (should). Skip in main flow.*

---

## Critical pre-workshop checklist (Thursday)

1. **Dry-run all three demos** — Demo 1 influencer (Cowork + Code), Demo 2 GSC, Demo 3 video ad. Demo 3 is the most fragile.
2. **Verify Slide 16** in the live deck on Friday morning — Anthropic may have updated the UI again.
3. **Lock the breakout call** — keep it or cut it. If keeping, the deliverable line is "description + first paragraph of body."
4. **Yaohong locks Slide 46 content** — three bullets minimum so the audience has something to look at while he talks.
5. **localStorage in the venue laptop** — clear before stage. Don't want the slide-counter resuming from a previous run.

---

*Script source — bullets from `workshop-speaker-notes-2026-05-27.md` (Fireflies transcript 2026-05-27), expanded to presenter-prose for the 2026-05-29 workshop. Deck reference — `beyond-cowork.html` post-edits 2026-05-27.*
