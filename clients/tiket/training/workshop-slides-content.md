# Workshop Slide Content & Speaker Notes

**Claude Code for B2B Marketing & Sales — 3-Hour Hands-On Workshop**
**April 15, 2026 | Novastacks AI × Superuser HQ**

---

## REVISED TIMING

| Block | Start | End | Duration | Content |
|-------|-------|-----|----------|---------|
| Setup Check | 0:00 | 0:10 | 10 min | Verify setup, troubleshoot stragglers |
| Block 1: Why This Matters | 0:10 | 0:25 | 15 min | Chat vs Agentic, live demo |
| Block 2: Terminal Comfort | 0:25 | 0:45 | 20 min | 3 commands, live error, launch Claude Code |
| Block 3: Core Concepts | 0:45 | 1:15 | 30 min | Prompting, files, web research |
| Block 4: Power-Ups | 1:15 | 1:30 | 15 min | MCPs + Skills combined, demo-driven |
| Break | 1:30 | 1:45 | 15 min | Break after high-confidence moment |
| Block 5: Guided Build | 1:45 | 2:30 | 45 min | Build one workflow with checkpoints |
| Block 6: Wrap-Up | 2:30 | 2:50 | 20 min | Show & Tell, next steps, resources |
| Buffer | 2:50 | 3:00 | 10 min | Overflow, Q&A, individual help |

---

## SETUP CHECK (10 min)

---

### Slide 1: Title Slide

**Title:** Claude Code for B2B Marketing & Sales
**Subtitle:** Building Agentic Workflows — Hands-On Workshop
**Footer:** Novastacks AI × Superuser HQ | April 15, 2026

**Speaker Notes:**
Welcome everyone! While we get started, let's make sure everyone's setup is working. Open your terminal — Mac users search "Terminal" in Spotlight, Windows users open WSL. Type `claude --version` and tell us what you see. [Co-facilitator walks the room troubleshooting.] If you're getting an error, raise your hand — we'll come to you. No one gets left behind today.

---

### Slide 2: Quick Setup Verify

**Content:**
**Let's make sure you're ready. Type these one at a time:**

```
node --version       → You should see: v22.x.x
claude --version     → You should see: a version number
```

✅ Both show a version number? You're ready!
❌ Got an error? Raise your hand — we'll fix it right now.

**Speaker Notes:**
[CO-FACILITATOR handles setup issues while lead proceeds.] We budgeted time for this because in every workshop, a few people hit snags. That's completely normal. We have backup API keys if anyone needs one. The goal is: by the time we start the real content, 100% of you can launch Claude Code.

---

## BLOCK 1: Why This Matters (15 min)

---

### Slide 3: The AI You Know vs The AI You're About to Learn

**Content:**

| | Chat AI (what you know) | Agentic AI (today) |
|---|---|---|
| **How it works** | You ask → it answers → you copy-paste | You give a goal → it executes the whole workflow |
| **Example** | "Write me an email" → copy → paste into Gmail | "Research this company, draft outreach, save to Drive" → done |
| **Analogy** | Asking for directions | Having a driver take you there |
| **Tools** | ChatGPT, Claude.ai, Gemini | Claude Code, Manus, Devin |

**The real shift:** From AI as a search engine to AI as a teammate.

**Speaker Notes:**
Most of you have used ChatGPT or Claude.ai — you type something, get an answer, copy it somewhere. That's chat AI. Useful, but limited. Today we're learning something fundamentally different: agentic AI. It doesn't just answer — it acts. It reads your files, searches the web, writes documents, connects to Google Drive — all in one go. Think of it like this: chat AI is like asking someone for directions. Agentic AI is like having a driver who takes you there while you do other things.

---

### Slide 4: The Time Savings Are Real

**Content:**
**Real results from Anthropic's own marketing team:**

| Task | Manual | With Claude Code | Savings |
|------|--------|-----------------|---------|
| Research a prospect before a call | 30 min (Google, 5 tabs, notes) | 60 seconds (one prompt) | 96% |
| Create ad creative variations | 30 min per batch | 30 seconds | 98% |
| Draft a case study | 2.5 hours | 30 minutes | 80% |
| Repurpose blog → LinkedIn post | 20 min (rewrite, trim, format) | 30 seconds | 97% |
| Competitive analysis (3 companies) | 2-3 hours | 3 minutes | 97% |

*Source: "How Anthropic Uses Claude in Marketing" — Anthropic Blog, 2025*

**Speaker Notes:**
These aren't hypothetical numbers. This is from Anthropic's own marketing team — the company that makes Claude. Their non-technical marketers use Claude Code daily. One of them said: "You don't need to know how to code." That's you. If they can do it, you can do it. And by the end of today, you will.

---

### Slide 5: Live Demo — "Watch This"

**Content:**
🎬 **Live Demo: Research 5 competitors in 2 minutes**
- Input: 5 company URLs (Traveloka, Booking.com, Agoda, Klook, Trip.com)
- Output: Structured comparison table with positioning, pricing, recent news
- Saved directly to a file

**Speaker Notes:**
[TINA/YAOHONG PERFORMS LIVE DEMO] Let me show you what this looks like. I'm going to research 5 travel competitors — companies you know — in one prompt. Watch the terminal. [Type the prompt slowly enough to read. Let Claude Code work in silence for 10-15 seconds.] "Watch — it's researching all five simultaneously." [When output appears, scroll slowly.] Company overview... pricing... recent news from this month... strengths and weaknesses. This would take 45 minutes manually. That was 90 seconds. [CRITICAL: Have a pre-recorded backup video in case WiFi is slow. A failed Block 1 demo tanks the whole session.]

---

### Slide 6: Your New Mental Model

**Content:**
**Think of Claude Code as a smart intern who:**
- Has perfect memory
- Can access the internet
- Can read and write your files
- Connects to your tools (Gmail, Drive, Sheets)
- Never gets tired, never forgets instructions

**But you're the boss:**
- You decide what it works on
- You review its output
- You approve before it sends anything

**Like briefing a freelancer:** The more context you give upfront, the less revision later.

**Speaker Notes:**
Here's your mental model for today. Claude Code is like the best intern you've ever had — fast, thorough, perfect memory. But you're the boss. You direct the work, review the output, approve before anything goes out. It won't send an email or delete a file without your OK. Think of it like briefing a freelancer: the more context you give upfront, the less back-and-forth later. That's the core skill we're building today.

---

## BLOCK 2: Terminal Comfort (20 min)

---

### Slide 7: Let's Address the Elephant in the Room

**Content:**
**"The terminal looks scary"**

That's normal. Here's the truth:
- You only need **3 commands** for today
- It's just a text version of Finder / File Explorer
- If you can type a Google search, you can use terminal

**What terminal actually is:** A way to talk to your computer by typing instead of clicking.

Like Grab: you type the destination instead of tapping a map.

**Speaker Notes:**
I know what you're thinking. "That black screen with the blinking cursor looks terrifying." Totally normal. Every person who uses terminal felt that way their first time. Here's the good news: you need exactly 3 commands. And they map to things you already do every day in Finder or File Explorer. Think of terminal like Grab — you type where you want to go instead of tapping on a map. Same destination, different input method.

---

### Slide 8: The Only 3 Commands You Need

**Content:**

| What You Want to Do | In Finder / Explorer | In Terminal |
|--------------------|--------------------|-------------|
| "Where am I?" | Look at folder path at top | `pwd` |
| "What's in this folder?" | Look at the file list | `ls` |
| "Go into this folder" | Double-click the folder | `cd folder-name` |

**Bonus moves:**
- `cd ..` = Go back one folder (the "Back" button)
- Press **Tab** = Auto-complete (terminal helps you type!)
- **Up Arrow** = Repeat last command

**Speaker Notes:**
Three commands. `pwd` — "where am I?" Like the address bar in Explorer. `ls` — "what's here?" Like looking at the file list. `cd` — "go into this folder." Like double-clicking it. And `cd ..` goes back, like the back button. Plus Tab autocompletes names so you don't even have to type the whole thing.

---

### Slide 9: Watch Me Make a Mistake (On Purpose)

**Content:**
🎬 **Live demo: Errors are normal and harmless**

```
$ cd Dekstop
bash: cd: Dekstop: No such file or directory

$ cd Desktop
(works!)
```

**What just happened?**
- I typed "Dekstop" (typo) → got an error message
- The error is just the computer saying "I don't understand"
- Nothing broke. Nothing crashed. I just try again.

**Errors are information, not failure.**

**Speaker Notes:**
Before you type anything, I want to show you something. Watch this. [Type `cd Dekstop` intentionally.] Look — an error! "No such file or directory." Did my computer break? No. Did I lose any files? No. The terminal is just saying "I don't know what Dekstop is." So I fix the typo: `cd Desktop`. And it works. This is the most important thing I'll teach you today: errors are not failure. They're just the computer asking you to try again. You will see errors today. That's fine. That's learning.

---

### Slide 10: Hands-On — Your First Terminal Session

**Content:**
**Everyone do this now. Find your terminal buddy — help each other!**

```
Step 1: Open Terminal (Mac) or WSL (Windows)
Step 2: Type: pwd            → You should see: /Users/yourname
Step 3: Type: ls             → You should see: Desktop, Documents, etc.
Step 4: Type: cd Desktop     → (no output = success!)
Step 5: Type: pwd            → Should now show: /Users/yourname/Desktop
Step 6: Type: cd ..          → Back to home
```

✅ **Made it to Step 6? You just used the terminal.**
🖐️ **Stuck? Raise your hand — we're coming to help.**

**Speaker Notes:**
OK, everyone. Before you start — turn to the person next to you. That's your terminal buddy for today. If one of you gets stuck, help each other first, then raise your hand if you're both stuck. Now open your terminal. Follow along, one step at a time. [Walk the room. Give 2-3 minutes. Celebrate when people finish.] You just used the terminal. Give yourselves a round of applause. Seriously — most professionals never do this.

---

### Slide 11: Launch Claude Code

**Content:**
**Now the fun part:**

```
Step 1: cd ~/claude-workshop     → Go to workshop folder
Step 2: claude                   → Launch Claude Code!
```

**You should see** Claude Code start up with a welcome message.

Type your first prompt:
> "Hello! Tell me 3 fun facts about the travel industry in Southeast Asia."

✅ **Got a response? You're in!**

**Speaker Notes:**
Navigate to your workshop folder and type `claude`. That's it. Claude Code starts. Now type a fun prompt — something light before we get to real work. [Wait for everyone to get a response.] Congratulations — you're using agentic AI from the command line. This is something 99% of professionals haven't done yet.

---

## BLOCK 3: Core Concepts (30 min)

---

### Slide 12: The Art of Giving Good Instructions

**Content:**

**Bad prompt:**
> "Write me an email"

**Good prompt:**
> "Write a follow-up email to Sarah Chen at Acme Corp. We met yesterday about their Q2 marketing budget. They're interested in our content platform. Keep it warm but professional. Suggest a 30-min call next Tuesday."

**The Prompt Formula:**

| Element | What It Means | Example |
|---------|-------------|---------|
| **Context** | Who, what, background | "We met yesterday at the conference..." |
| **Specificity** | Exactly what you want | "Draft a 3-paragraph email..." |
| **Format** | How the output should look | "Format as a table with columns for..." |
| **Examples** | What "good" looks like | "Similar to this style: ..." |

**Speaker Notes:**
The #1 skill with any AI — chat or agentic — is giving clear instructions. Think about hiring a freelancer. If you say "write me an email," they'll ask 10 questions. If you give them context, specifics, and format, they nail it first try. Same with Claude Code. You don't need to be technical. You need to be specific. Like you would with a smart human who's new to your company.

*Reference: Amanda Askell (Anthropic's alignment lead) says: "Be honest with the model. Tell it exactly what you need. Iterate like you would with a human."*

---

### Slide 13: Prompt Formula in Action — Before & After

**Content:**

**Scenario: Preparing for a client meeting**

| | Vague Prompt | Specific Prompt |
|---|---|---|
| **What you type** | "Tell me about Traveloka" | "Research Traveloka. Give me a 1-page brief: what they do, their 2026 strategic priorities, key executives, recent funding, and 3 smart questions I can ask their VP of Marketing in a meeting tomorrow. Save as traveloka-brief.md" |
| **What you get** | Generic Wikipedia-style summary | Actionable meeting prep saved as a file |
| **Time to usable** | 10+ min editing | Ready to use immediately |

**Speaker Notes:**
Let me show you the difference specificity makes. [Show both prompts side by side. Optionally demo the specific one live.] The vague prompt gives you a Wikipedia summary. The specific prompt gives you meeting prep you can actually use. Same AI, completely different output — the only difference is how you asked.

---

### Slide 14: Reading and Writing Files

**Content:**
**Claude Code works directly with your files — no copy-paste.**

| What You Want | What You Type |
|--------------|--------------|
| Read a file | "Read marketing-plan.md and summarize the key priorities" |
| Create a file | "Create competitor-brief.md with a research summary of Acme Corp" |
| Edit a file | "Open my-draft.md and make the tone more conversational" |

**Files AI agents work best with:**

| ✅ Great (plain text) | ⚠️ OK (readable) | ❌ Avoid (binary) |
|----------------------|-------------------|-------------------|
| `.md` (Markdown) — like a clean Word doc | `.pdf` | `.docx` (Word) |
| `.txt` (Plain text) — like Notepad | `.html` | `.xlsx` (Excel) |
| `.csv` (Data) — like a simple spreadsheet | `.pptx` | `.psd` (images) |

**Pro tip:** Think of Markdown as "Google Docs without the formatting toolbar." Simple, clean, and AI reads it instantly.

**Speaker Notes:**
One of the biggest superpowers of Claude Code versus ChatGPT: it works directly with files on your computer. No uploading, no copy-pasting. You point it at a file and it reads it. You ask it to create a file and it writes it right there. Now — AI agents love plain text files. Markdown, CSV, plain text. They can handle PDFs. But Word and Excel are harder because they're binary — think of it like trying to read a book that's been sealed in plastic wrap. Markdown is the same book, unwrapped. We'll use markdown files throughout today.

---

### Slide 15: Web Search and Research

**Content:**
**Claude Code searches the web for you:**

> "Search for recent news about Traveloka's expansion plans in 2026"

> "Research gojek.com — what do they do, who leads their marketing, any recent product launches?"

> "Find the top 5 B2B marketing trends in Southeast Asia this year"

**What this replaces:**

| Old Way | New Way |
|---------|---------|
| Open Google → read 10 tabs → take notes → write summary | One prompt → structured output in seconds |
| 30 minutes | 60 seconds |

**Speaker Notes:**
The second superpower: web research. Instead of opening 10 Chrome tabs, reading through articles, and trying to synthesize what you found — you give Claude Code a research task and it does everything. Searches, reads, synthesizes, structures the output. For sales teams, this is a game changer. Lead research that took 30 minutes now takes 30 seconds. Let's see it in action.

---

### Slide 16: Live Demo — Build a Lead Research Brief

**Content:**
🎬 **Live Demo: From URL to Brief in 60 Seconds**

> "Research gojek.com. Give me a structured lead brief: what they do, target market, key executives, recent news, and potential pain points. Save it as gojek-brief.md"

**What to watch for:**
1. Claude Code searches the web (you'll see it working)
2. It structures the findings (not just raw text)
3. It saves the file (you can open it later)

**Speaker Notes:**
[LIVE DEMO] Watch — I'll research Gojek from just their URL. [Type prompt. Narrate as Claude Code works.] "It's searching... now it's reading their website... pulling recent news... structuring the brief..." [When done:] That's a ready-to-use sales brief. Saved as a file on my laptop. Imagine doing this for every prospect before every meeting. That's what you'll build in Block 5.

---

## BLOCK 4: Power-Ups — MCPs & Skills (15 min)

---

### Slide 17: Supercharging Claude Code

**Content:**
Claude Code out of the box: reads files, searches the web, generates content.
Claude Code with **Power-Ups**: connects to ALL your tools.

**Two types of Power-Ups:**

| Power-Up | What It Is | Analogy |
|----------|-----------|---------|
| **MCPs** (Connectors) | Plug Claude Code into your tools — Drive, Gmail, Sheets | Apps on your phone — your phone works without them, but way better with WhatsApp, Grab, and banking installed |
| **Skills** (Saved Recipes) | Reusable instruction templates you call with one command | Saved recipes — write it once, then just say "make the rendang" and it follows every step |

**Speaker Notes:**
Now let's talk about the two things that turn Claude Code from "cool demo" into "daily tool." MCPs are connectors — they plug Claude Code into the tools you already use. Think of your phone: it works out of the box, but it's way better with WhatsApp, Grab, and your banking app installed. Same idea. Skills are saved recipes. Instead of explaining your LinkedIn post style every time, you write the recipe once, and just call it. Like telling a chef "make the rendang" — they know every step because you wrote it down once.

---

### Slide 18: MCP Demo — Your Tools, Connected

**Content:**
🎬 **Demo: Claude Code + Google Drive**

> "Search my Google Drive for the latest marketing report and summarize the key findings"

> "Read the Q1 results spreadsheet and tell me which campaign had the highest ROI"

**Common MCPs for your team:**

| MCP | Connects To | Use Case |
|-----|------------|----------|
| Google Drive | Your Drive files | Read docs, sheets, slides |
| Google Sheets | Spreadsheets | Pull data, update trackers |
| Gmail | Your inbox | Draft and search emails |
| Filesystem | Local files | Read/write files on your computer |

**Setup:** One-time configuration. We'll help after the workshop. Check status: `/mcp`

**Speaker Notes:**
[DEMO] I have Google Drive connected to my Claude Code. Watch — I'll ask it to find and summarize a file from my Drive. [Run demo.] This is usually the "aha moment." Claude Code isn't a chatbot trapped in a box — it's connected to your actual work. Setting up MCPs is a one-time thing. We'll send you instructions and provide email support for the next 15 days.

---

### Slide 19: Skills Demo — Your Saved Recipes

**Content:**
🎬 **Demo: /linkedin-post Skill**

> "Write a LinkedIn post about AI transforming B2B sales"

**What the Skill does automatically:**
1. Reads your style guide (tone, voice, format)
2. Creates a hook-first opening
3. Keeps it under 1,300 characters
4. Ends with a question for engagement
5. Adds relevant hashtags

**Without a Skill:** You explain your voice, style, and format every single time
**With a Skill:** You type `/linkedin-post` and it just knows

**How to create a Skill:**
1. Write your instructions in a `.md` file (like a recipe card)
2. Save it in the right folder
3. Call it anytime with `/skill-name`

*Details in your cheat sheet.*

**Speaker Notes:**
[DEMO] I have a LinkedIn post skill saved. Watch — I just give it a topic and it writes in my voice, my format, my style. [Run demo.] That took 30 seconds. Without the skill, I'd need to explain my voice, my format, everything — every single time. The skill is like a recipe card: write it once, use it forever. Your cheat sheet has the details on how to create one.

---

## ☕ BREAK (15 min)

---

### Slide 20: Break

**Content:**
☕ **15-Minute Break**

**Before you go — pick your build:**

| Option | What You'll Build | Best For |
|--------|------------------|----------|
| 🔍 **Lead Research Brief** | Company URL → structured sales brief | Sales |
| ✍️ **Content Repurposer** | Blog → LinkedIn post in your voice | Marketing |
| 📊 **Competitor Tracker** | 3-5 competitors → comparison table | Strategy |
| 🔧 **Freestyle** | Any workflow for YOUR actual work | Anyone |

**Come back ready to build!**

**Speaker Notes:**
Take 15 minutes. When you come back, you're building. Look at these four options and pick the one most useful for YOUR job. If none of them fit perfectly, choose "Freestyle" — we'll help you design a workflow for whatever you actually need. Also: make sure Claude Code is still running when you get back. If it closed, just type `claude` to restart.

---

## BLOCK 5: Guided Build (45 min)

---

### Slide 21: Let's Build — Rules of Engagement

**Content:**
**How this works:**
1. Pick your option (or Freestyle)
2. Follow the step-by-step guide
3. Use REAL companies / REAL topics from your work
4. **Terminal buddy:** Help each other before raising your hand
5. Both facilitators are roaming — we'll come to you

**If you get stuck:**
- Check if Claude Code is still running (type `claude` if not)
- Check you're in the right folder (`pwd` to see where you are)
- Re-read the error message — it usually tells you what went wrong
- Ask your terminal buddy
- Raise your hand

**Speaker Notes:**
Here's how this works. Pick your option, follow the guide, and use real companies and topics from your actual work. This way you leave with something you'll actually use. Your terminal buddy is your first line of support. Both Yaohong and I will be walking the room. Nobody gets left behind. Let's go.

---

### Slide 22: Option A — Lead Research Brief Generator

**Content:**

**Step 1: Navigate to your folder**
```
cd ~/claude-workshop
claude
```
✅ **Checkpoint:** You should see the Claude Code welcome prompt.

**Step 2: Research a real company**
```
"Research [COMPANY URL]. Create a structured lead brief with:
company overview, target market, key decision makers, recent
news, and potential pain points. Save it as [company]-brief.md"
```
✅ **Checkpoint:** You should see Claude Code searching the web, then a brief appearing on screen, ending with "File saved."

**Step 3: Make it actionable**
```
"Read [company]-brief.md and add 3 personalized outreach
angles I can use in a cold email"
```
✅ **Checkpoint:** The file now has an additional section with outreach angles.

**Step 4: Generate the outreach email**
```
"Based on this brief, draft a cold outreach email to their
VP of Marketing. Keep it under 150 words. Save as outreach-email.md"
```
✅ **Checkpoint:** You now have TWO files: a brief and an email. Ready to use.

🖐️ **Stuck at any step? Raise your hand.**

---

### Slide 23: Option B — Content Repurposer

**Content:**

**Step 1: Create source content**
```
cd ~/claude-workshop
claude
"Create blog-draft.md with a 300-word blog post about
[TOPIC RELEVANT TO YOUR WORK]"
```
✅ **Checkpoint:** Type `ls` — you should see `blog-draft.md` in your folder.

**Step 2: Repurpose to LinkedIn**
```
"Read blog-draft.md and rewrite as a LinkedIn post.
Hook-first, under 1300 characters, end with a question.
Add hashtags. Save as linkedin-post.md"
```
✅ **Checkpoint:** You now have a LinkedIn post that sounds like you, not a robot.

**Step 3: Repurpose to email newsletter**
```
"Rewrite the same blog as a 100-word email newsletter intro
that makes people want to click through. Save as newsletter-intro.md"
```
✅ **Checkpoint:** You now have 3 pieces of content from 1 source.

**Step 4: Bonus — create a tweet thread**
```
"Turn the blog post into a 5-tweet thread. Punchy,
insight-driven. Save as tweet-thread.md"
```
✅ **Checkpoint:** 4 formats from 1 blog post. That's content repurposing at scale.

🖐️ **Stuck at any step? Raise your hand.**

---

### Slide 24: Option C — Competitor Tracker

**Content:**

**Step 1: Pick 3 real competitors**
```
cd ~/claude-workshop
claude
```
✅ **Checkpoint:** Think of 3 companies you actually compete with or track.

**Step 2: Run the research**
```
"Research [Company A URL], [Company B URL], [Company C URL].
For each: what they do, key products, pricing (if public),
recent news, strengths and weaknesses.
Create a comparison table. Save as competitor-analysis.md"
```
✅ **Checkpoint:** You should see a structured comparison table. Check: does the data look accurate?

**Step 3: Add your own company**
```
"Read competitor-analysis.md. Add a row for [YOUR COMPANY].
What are our advantages? Where are we vulnerable?"
```
✅ **Checkpoint:** The table now includes your company with honest positioning.

**Step 4: Make it strategic**
```
"Add a recommendations section: 3 things we should do based
on this competitive landscape. Save the updated file."
```
✅ **Checkpoint:** You now have a competitive brief you can share with your team.

🖐️ **Stuck at any step? Raise your hand.**

---

### Slide 25: Option D — Freestyle Build

**Content:**
**Build any workflow for YOUR actual work.**

**Ideas to get you started:**

| Your Job | Workflow Idea |
|----------|-------------|
| Sales | "Research my next meeting's company and draft prep notes" |
| Marketing | "Analyze our last 5 LinkedIn posts and suggest improvements" |
| Operations | "Create a weekly report template from these data points" |
| Strategy | "Research [market/trend] and create an executive summary" |
| HR | "Draft a job description for [role] based on these requirements" |

**How to approach it:**
1. Think: "What task do I do every week that takes 30+ minutes?"
2. Write that as a prompt
3. Ask Claude Code to do it
4. Iterate if the output isn't quite right

🖐️ **Want help designing your workflow? Raise your hand.**

---

## BLOCK 6: Wrap-Up (20 min)

---

### Slide 26: Show & Tell

**Content:**
**Who wants to share what they built?**

1-2 volunteers — show your screen and tell us:
- What you built
- What surprised you
- How you'll use this in your real work

👏 *Everything built today is a real tool you can use tomorrow*

**Speaker Notes:**
Who wants to share? Don't be shy — everyone in this room just did something most professionals haven't done yet. [Pick 1-2 volunteers. Celebrate creative uses. Ask follow-up questions.] Notice how different everyone's outputs are — same tool, different workflows for different jobs. That's the power of agentic AI: it adapts to YOUR work.

---

### Slide 27: Your Monday Action Plan

**Content:**
**This week, use Claude Code on ONE real task.**

Not a test. Not practice. Actual work.

| Day | Action |
|-----|--------|
| **This week** | Use the workflow you built today on real work |
| **Next week** | Try a second use case from the cheat sheet |
| **This month** | Set up 1 MCP (we'll help via email) |

**Your API key:** Make it permanent so it's there every time you open terminal.
```
# Add this to your shell profile (~/.zshrc or ~/.bashrc):
export ANTHROPIC_API_KEY="your-key-here"
```

**The habit loop:** Use it once → see the value → use it again → it becomes natural.

**Speaker Notes:**
Here's your concrete plan. This week: use the workflow you built today on real work. One real task. Not a toy example. The research shows if you use a new tool on real work within 7 days, you're 5x more likely to adopt it long-term. Next week, try a second use case from your cheat sheet. And this month, email us and we'll help you set up an MCP so Claude Code connects to your Google Drive or Gmail. Also — save your API key permanently by adding that export line to your shell profile. Instructions are in the setup guide.

---

### Slide 28: What You're Taking Home

**Content:**

📄 **Cheat Sheet** — Terminal commands, prompt templates, AI tools comparison, MCP guide
📘 **Setup Guide** — Share with colleagues who want to get started

**Official Anthropic Resources (free):**
- Claude Code Docs: docs.anthropic.com/en/docs/claude-code
- Prompt Engineering Guide: docs.anthropic.com/en/docs/build-with-claude/prompt-engineering
- MCP Docs: modelcontextprotocol.io
- Free Course — "Claude Code in Action": anthropic.skilljar.com

**Go deeper:**
- Andrew Ng's Claude Code Course (free): learn.deeplearning.ai/courses/claude-code
- Anthropic's MCP Course (free): anthropic.skilljar.com/introduction-to-model-context-protocol
- "How Anthropic Uses Claude in Marketing": claude.com/blog/how-anthropic-uses-claude-marketing

📧 **15-day post-workshop support:** tchu@novastacks-ai.com

**Also explore:** Claude Cowork (claude.com/product/cowork) — same AI capabilities with a visual interface instead of terminal. Great for daily use once you understand the concepts from today.

**Speaker Notes:**
Here's everything you're taking home. The cheat sheet has all commands, prompt templates, and the AI tools comparison. The setup guide is something you can share with your team. I've listed the best free resources — the Andrew Ng course and Anthropic's own courses are excellent next steps. And you have 15 days of email support. If you get stuck, email us. We'll respond within 24 hours. Also worth checking out: Claude Cowork. It's the same AI engine we used today but with a visual interface — no terminal needed. Now that you understand how agentic AI works under the hood, Cowork will make a lot more sense. You can self-explore it.

---

### Slide 29: Thank You

**Content:**
**Thank you for building with us today.**

You walked in never having opened a terminal.
You're leaving with a working AI workflow.

That gap — between knowing about AI and actually using it — you just crossed it.

**Tina Chu** — tchu@novastacks-ai.com
**Yaohong Ch'ng** — Superuser HQ

**Speaker Notes:**
Thank you everyone. You came in as people who'd never used a terminal. You're leaving as people who've built real AI workflows from the command line. That's not a small thing. The gap between watching YouTube demos and actually doing this yourself — you just crossed it. Keep going. We're here if you need us. Now — who has questions?

---

### Slide 30: Exit Ticket

**Content:**
**Before you leave — one sticky note:**

✍️ Write down:
> "The ONE thing I will use Claude Code for this week is: _______________"

Stick it on the board on your way out.

**We'll follow up in 7 days to see how it went.**

**Speaker Notes:**
Last thing. Take a sticky note and write down the one thing you'll use Claude Code for this week. Be specific. Not "try it out" — something like "research 3 prospects before Thursday's sales calls." Stick it on the board. We're going to follow up by email in 7 days to ask how it went. This isn't accountability for accountability's sake — it's because the people who commit to one specific task are the ones who actually adopt the tool.

---

## APPENDIX: Facilitator Notes

### Pre-Workshop Checklist
- [ ] Confirm all participants received setup guide (send 3+ days before)
- [ ] Send pre-workshop video: 2-min recording of opening terminal, typing pwd/ls/cd, launching Claude Code
- [ ] Test WiFi with 20+ concurrent devices
- [ ] Prepare and rehearse ALL demo scripts until flawless
- [ ] Record backup videos of every live demo (in case of WiFi/API issues)
- [ ] Print cheat sheets (one per participant)
- [ ] Print "My First Prompt" template cards
- [ ] Print checkpoint guides for Block 5 (one per option)
- [ ] Have 3-5 backup API keys ready
- [ ] Prepare sticky notes + markers for exit tickets
- [ ] Bring 2-3 backup laptops with everything pre-configured

### Demo Scripts to Rehearse
1. **Block 1 — Competitor Research:** 5 travel competitors (Traveloka, Booking.com, Agoda, Klook, Trip.com)
2. **Block 2 — Intentional Error:** `cd Dekstop` → error → `cd Desktop` → success
3. **Block 3 — Lead Research Brief:** Research gojek.com, save as file
4. **Block 4 — MCP Demo:** Search Google Drive for a marketing report
5. **Block 4 — Skills Demo:** /linkedin-post skill generating a post

### Timing Buffer Strategy
- Block 1 has 5 min trimmed (from 20 to 15) — goes to buffer
- Block 4 has 5 min trimmed (from 20 to 15) — goes to buffer
- Block 6 has 10 min trimmed (from 30 to 20) — goes to buffer
- Total buffer: 10 min at end + flexibility during blocks

### "My First Prompt" Template Card (Print for Each Participant)

```
Fill in the blanks and type this into Claude Code:

I want Claude Code to [ACTION: research / write / analyze / compare]
about [SUBJECT: company name, topic, competitor]
and give me [FORMAT: a table / a brief / an email / a list]
that includes [DETAILS: pricing, recent news, key people, pain points]
and save it as [FILENAME].md
```

### Common Issues During Workshop
| Problem | Fix |
|---------|-----|
| Participant can't launch Claude Code | Check API key, check Node.js version |
| "command not found: claude" | `npm install -g @anthropic-ai/claude-code` |
| Slow responses | Too many people on WiFi. Switch to mobile hotspot. |
| API rate limiting | Switch to backup API key |
| Someone finishes early | Challenge: build a second workflow or create a Skill |
| Someone completely lost | Pair with faster participant (pair debugging) |
| Live demo fails | Switch to pre-recorded backup video immediately |
| Setup issues at start | Co-facilitator handles individually while lead proceeds |

### Post-Workshop Follow-Up Plan
| When | Action |
|------|--------|
| Day 0 (after workshop) | Email: cheat sheet PDF + resource links + "make your API key permanent" instructions |
| Day 7 | Email: "How did your ONE thing go?" + offer MCP setup help |
| Day 15 | Final email: "Questions? Last day of email support" + link to Anthropic courses |

### Key Sources for Facilitator Prep
- "How Anthropic Uses Claude in Marketing" — claude.com/blog/how-anthropic-uses-claude-marketing
- "How Anthropic Teams Use Claude Code" — claude.com/blog/how-anthropic-teams-use-claude-code
- Andrew Ng's Claude Code course — learn.deeplearning.ai/courses/claude-code
- Amanda Askell's prompting philosophy — be honest with the model, iterate, ask it to clarify
- Zack Proser's Cowork GTM Workshop — zackproser.com/blog/claude-cowork-workshop-anthropic
- Anthropic's "Claude Code in an Hour" webinar — anthropic.com/webinars/claude-code-in-an-hour
