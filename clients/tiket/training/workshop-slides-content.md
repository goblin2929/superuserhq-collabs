# Workshop Slide Content & Speaker Notes

**Claude Code for B2B Marketing & Sales — 3-Hour Hands-On Workshop**
**April 15, 2026 | Novastacks AI × Superuser HQ**

---

## BLOCK 1: Why This Matters (20 min)

---

### Slide 1: Title Slide

**Title:** Claude Code for B2B Marketing & Sales
**Subtitle:** Building Agentic Workflows — Hands-On Workshop
**Footer:** Novastacks AI × Superuser HQ | April 15, 2026

**Speaker Notes:**
Welcome everyone. Today we're going to change how you work with AI. By the end of these 3 hours, you'll have built something real — a working automation you'll use next week. This isn't a lecture. This is hands-on. You'll be typing, building, and creating alongside us.

---

### Slide 2: The AI You Know vs The AI That's Coming

**Content:**
- **Chat AI** (what you know): You ask a question → get an answer. One turn. Copy-paste.
  - Example: "Write me an email" → copies text → pastes into Gmail
- **Agentic AI** (what we're learning today): You give a goal → AI executes multi-step workflows autonomously
  - Example: "Research this company, draft an outreach email, and save it to my Google Drive" → done in 30 seconds

**Visual:** Side-by-side comparison — Chat AI (ping pong) vs Agentic AI (autopilot)

**Speaker Notes:**
Most of you have used ChatGPT or Claude.ai. You type something, you get an answer, you copy it somewhere. That's chat AI. It's useful but limited. What we're introducing today is fundamentally different. Agentic AI doesn't just answer — it acts. It can read your files, search the web, write documents, connect to your Google Drive, and do it all in one go. Think of it as the difference between asking someone for directions versus having a driver take you there.

---

### Slide 3: Live Demo — "Watch This"

**Content:**
🎬 **Live Demo: Research 5 competitors in 2 minutes**
- Input: 5 company URLs
- Output: Structured comparison table with positioning, pricing, recent news
- Saved directly to a file on the laptop

**Speaker Notes:**
[TINA/YAOHONG PERFORMS LIVE DEMO] Let me show you what this looks like in practice. I'm going to give Claude Code 5 competitor URLs and ask it to research all of them. Watch the terminal — you'll see it thinking, searching, and building a report in real time. This would take you 30-60 minutes manually. [Run the demo. Let silence build as it works. The "wow" moment is watching it happen live.]

---

### Slide 4: Your New Mental Model

**Content:**
**Think of Claude Code as a smart intern with:**
- ✅ Perfect memory (remembers everything you've told it)
- ✅ Access to the internet (can research anything)
- ✅ Access to your files (can read and write documents)
- ✅ Access to your tools (Gmail, Google Drive, Sheets — via MCPs)
- ✅ Never gets tired, never forgets instructions

**But you're the boss:**
- You decide what it works on
- You review its output
- You approve before it sends/publishes anything

**Speaker Notes:**
Here's the mental model I want you to carry through today. Claude Code is like the best intern you've ever had. It's fast, thorough, never complains, and has perfect memory. But — and this is important — you're the boss. You direct the work. You review the output. It won't send an email unless you say so. It won't delete files unless you approve it. You're always in control.

---

## BLOCK 2: Terminal Comfort (20 min)

---

### Slide 5: Let's Address the Elephant in the Room

**Content:**
**"The terminal looks scary"**

That's normal. Here's the truth:
- You only need **3 commands** for today
- It's just a text version of File Explorer / Finder
- If you can type a Google search, you can use terminal

**What the terminal actually is:** A way to talk to your computer by typing instead of clicking

**Speaker Notes:**
I know what some of you are thinking. "That black screen with the blinking cursor looks terrifying." That's completely normal. Every single person who uses terminal felt that way the first time. Here's the good news: you only need 3 commands. Three. That's it. And they map directly to things you already do every day — you're just typing instead of clicking.

---

### Slide 6: The Only 3 Commands You Need

**Content:**

| What You Want to Do | In Finder/Explorer | In Terminal |
|--------------------|--------------------|-------------|
| "Where am I?" | Look at the folder path at top | `pwd` |
| "What's in this folder?" | Look at the files listed | `ls` |
| "Open this folder" | Double-click the folder | `cd folder-name` |

**Bonus:**
- `cd ..` = Go back one folder (like clicking "Back")
- Press **Tab** = Auto-complete (the terminal helps you type!)

**Speaker Notes:**
Here are your three commands. That's it. `pwd` tells you where you are — like looking at the address bar in File Explorer. `ls` shows you what's in the current folder — like looking at the files. `cd` moves you into a folder — like double-clicking it. And a bonus: `cd ..` goes back, like hitting the back button. And Tab autocompletes — so you don't even have to type the full name. Let's try it now.

---

### Slide 7: Hands-On — Your First Terminal Session

**Content:**
**Everyone do this now:**

```
Step 1: Open Terminal (Mac) or WSL (Windows)
Step 2: Type: pwd          (Where am I?)
Step 3: Type: ls           (What's here?)
Step 4: Type: cd Desktop   (Go to Desktop)
Step 5: Type: ls           (What's on my Desktop?)
Step 6: Type: cd ..        (Go back)
```

🖐️ **Raise your hand if you get stuck — we're coming to help**

**Speaker Notes:**
OK, everyone open your terminal. Mac users: search for "Terminal" in Spotlight. Windows users: open your WSL Ubuntu window. Now follow along with me. Type pwd. What do you see? [Wait, walk around.] Good. Now type ls. You should see a list of folders and files. Now type cd Desktop — you're going into your Desktop folder. Type ls again to see what's there. And cd .. to go back. That's it. You just used the terminal. [Encourage applause/celebration. This is a confidence-building moment.]

---

### Slide 8: Launch Claude Code

**Content:**
**Now the fun part:**

```
Step 1: cd ~/claude-workshop     (Go to workshop folder)
Step 2: claude                   (Launch Claude Code!)
```

You should see Claude Code start up. Type your first message:

> "Hello! What can you help me with?"

🎉 **You're in. You're using Claude Code.**

**Speaker Notes:**
Now navigate to your workshop folder. Type cd ~/claude-workshop and then just type claude. That's it. Claude Code will start. Type a simple hello. It'll respond. Congratulations — you are now using agentic AI from the command line. This is the thing 99% of people haven't done yet. You're ahead of the curve.

---

## BLOCK 3: Core Concepts (30 min)

---

### Slide 9: The Art of Giving Good Instructions

**Content:**
**Bad prompt:** "Write me an email"
**Good prompt:** "Write a follow-up email to Sarah Chen at Acme Corp. We met yesterday to discuss their Q2 marketing budget. They're interested in our content platform. Keep it warm but professional. Suggest a 30-min call next Tuesday."

**The formula:**
1. **Context** — Who, what, background
2. **Specificity** — Exactly what you want
3. **Format** — How you want the output
4. **Examples** — Show what "good" looks like (optional but powerful)

**Speaker Notes:**
The number one skill with AI — any AI — is giving clear instructions. Think about it: if you told a new employee "write me an email," they'd ask a dozen questions. But if you gave them context, specifics, and format, they'd nail it first try. Same with Claude Code. The more context you give, the better the output. You don't need to be technical. You just need to be specific. Like you would with a smart human.

---

### Slide 10: Reading and Writing Files

**Content:**
**Claude Code can read your files:**
> "Read the file marketing-plan.md and summarize the key priorities"

**Claude Code can write files:**
> "Create a file called competitor-brief.md with a research summary of Acme Corp"

**Claude Code can edit files:**
> "Open my-draft.md and make the tone more conversational"

**Files AI agents work best with:**
| ✅ Great | ⚠️ OK | ❌ Avoid |
|---------|-------|---------|
| .md (Markdown) | .pdf (can read) | .docx (Word) |
| .txt (Plain text) | .html (web pages) | .xlsx (Excel) |
| .csv (Data) | .pptx (limited) | .psd (images) |

**Speaker Notes:**
One of the biggest superpowers of Claude Code versus ChatGPT is that it works directly with files on your computer. You don't copy-paste. You point it at a file and it reads it. You ask it to create a file and it writes it directly. Now — important distinction. AI agents work best with text-based files. Markdown, plain text, CSV. They can handle PDFs. But Word docs and Excel files are harder because they're binary formats. Pro tip: for best results, work with markdown files. They're simple, clean, and AI loves them.

---

### Slide 11: Web Search and Research

**Content:**
**Claude Code can search the web:**
> "Search for recent news about Traveloka's expansion plans in 2026"

> "Find the top 5 trends in B2B SaaS marketing this year"

> "Research [company URL] and tell me what they do, who they serve, and their recent funding"

**This replaces:** Manual Googling → reading 10 tabs → summarizing in a doc
**With:** One prompt → structured output in seconds

**Speaker Notes:**
The second superpower is web research. Instead of opening 10 Chrome tabs, reading through articles, and trying to synthesize what you found — you give Claude Code a research task and it does it all. It searches, reads, synthesizes, and gives you a structured output. For sales teams, this is a game changer. Lead research that took 30 minutes now takes 30 seconds.

---

### Slide 12: Live Demo — Build a Lead Research Brief

**Content:**
🎬 **Live Demo: From URL to Brief in 60 Seconds**

Input:
> "Research the company gojek.com. Give me a structured lead brief with: what they do, target market, key executives, recent news, and potential pain points we could help with. Save it as gojek-brief.md"

Output: A ready-to-use sales brief, saved as a file

**Speaker Notes:**
[LIVE DEMO] Let me show you this in action. I'll give Claude Code a company URL and ask for a full lead research brief. Watch — it'll search the web, find information, structure it, and save it as a file. All in about 60 seconds. [Run demo. Talk through what's happening on screen as Claude Code works.] Now imagine doing this for every prospect before a meeting. That's the power.

---

## BLOCK 4: MCPs & Skills — The Power-Ups (20 min)

---

### Slide 13: What Are MCPs?

**Content:**
**MCP = Model Context Protocol**
Think of MCPs as **plug-ins** or **connectors** for Claude Code.

Without MCPs: Claude Code can read files and search the web
With MCPs: Claude Code can also access Google Drive, Gmail, Sheets, Notion, Slack...

**Analogy:** Your phone out of the box vs your phone with apps installed

| Without MCPs | With MCPs |
|-------------|-----------|
| Read/write local files | + Access Google Drive files |
| Search the web | + Read/send Gmail |
| Generate text | + Read/update Google Sheets |
|  | + Post to Slack, Notion, etc. |

**Speaker Notes:**
Now let's talk about MCPs — the thing that makes Claude Code truly powerful for business teams. MCP stands for Model Context Protocol, but just think of them as plug-ins. Right now, Claude Code can work with your local files and the web. But with MCPs, it can connect to Google Drive, Gmail, Google Sheets, Notion, Slack — all the tools you already use. It's like the difference between your phone out of the box versus your phone with all your apps installed.

---

### Slide 14: MCP Demo — Google Drive

**Content:**
🎬 **Demo: Claude Code + Google Drive**

> "Search my Google Drive for the latest marketing report and summarize the key findings"

> "Read the Q1 results spreadsheet and tell me which campaign had the highest ROI"

**How MCPs get set up:**
- One-time configuration (we'll help you after the workshop)
- Once connected, Claude Code remembers your tools
- Check status anytime: type `/mcp`

**Speaker Notes:**
[DEMO] Let me show you MCPs in action. I have Google Drive connected. Watch — I'll ask Claude Code to find a file in my Drive and summarize it. [Run demo.] This is the "aha moment" for most people. Claude Code isn't just a chatbot — it's connected to your actual work environment. Setting up MCPs is a one-time thing, and we provide post-workshop support to help you get your connectors configured.

---

### Slide 15: What Are Skills?

**Content:**
**Skills = Saved instruction sets you can reuse**

Think of Skills like **email templates** — but for AI tasks.

**Without Skills:** You type the same detailed prompt every time
**With Skills:** You type `/linkedin-post` and it knows exactly what to do

**Example: "Write LinkedIn Post in My Voice" Skill**
- Knows your writing style, tone, typical post length
- Knows to start with a hook
- Knows to end with a question
- Formats with line breaks for readability

**Speaker Notes:**
Skills are the thing that turns Claude Code from "cool demo" into "daily tool." A skill is a saved set of instructions. Instead of typing a detailed prompt every time you want to write a LinkedIn post, you create a skill once with all your preferences — your voice, your style, your format — and then just call it with a slash command. It's like having a template that thinks. We'll see a quick demo, and in Block 5, some of you will actually build one.

---

### Slide 16: Skill Demo — LinkedIn Post

**Content:**
🎬 **Demo: /linkedin-post Skill**

Input:
> "Write a LinkedIn post about how AI is changing B2B sales, using my linkedin-post skill"

What the Skill does behind the scenes:
1. Reads your style guide
2. Creates a hook-first post
3. Keeps it under 1,300 characters
4. Adds a closing question
5. Suggests hashtags

**Speaker Notes:**
[DEMO] Watch this. I have a LinkedIn post skill configured. All I do is tell Claude Code the topic and invoke the skill. It knows my voice, my format, everything. [Run demo.] What took 20 minutes of writing and editing is now a 30-second first draft. And it's in MY voice, not generic AI voice. That's because the skill has detailed instructions about how I write.

---

## ☕ BREAK (15 min)

---

### Slide 17: Break

**Content:**
☕ **15-Minute Break**

When you come back:
- Make sure Claude Code is still running (type `claude` if it's closed)
- You'll be building your own workflow
- Pick which one you want to build (next slide)

**Speaker Notes:**
Take 15. Stretch, get coffee. When you come back, we're building. Look at the next slide and start thinking about which workflow you want to create — you'll pick one and build it yourself.

---

## BLOCK 5: Guided Build (45 min)

---

### Slide 18: Choose Your Build

**Content:**
**Pick ONE workflow to build. We'll help you through it.**

| Option | What You'll Build | Best For |
|--------|------------------|----------|
| 🔍 **Lead Research Brief Generator** | Input a company URL → get a structured sales brief | Sales teams |
| ✍️ **Content Repurposer** | Blog post → LinkedIn post in your voice | Marketing teams |
| 📊 **Competitor Tracker** | Automated comparison of 3-5 competitors | Strategy/planning |

Each option has a step-by-step guide. Choose what's most useful for YOUR work.

**Speaker Notes:**
Here are your three options. Pick the one that's most useful for your actual job. If you're in sales, the lead research brief is gold. If you're in marketing, the content repurposer will change your daily workflow. If you're in strategy or planning, the competitor tracker is your go-to. Raise your hand when you've decided and we'll hand you the exercise guide. Both of us will be walking around helping — no one gets left behind.

---

### Slide 19: Option A — Lead Research Brief Generator

**Content:**
**Step-by-step guide:**

```
1. Make sure you're in your workshop folder:
   cd ~/claude-workshop

2. Start Claude Code:
   claude

3. Type this prompt (replace with a real company):
   "Research the company [URL]. Create a structured lead
   brief with: company overview, target market, key decision
   makers, recent news, competitive landscape, and potential
   pain points. Save it as [company]-brief.md"

4. Review the output file:
   "Read [company]-brief.md and add a section with
   3 personalized outreach angles"

5. You now have a ready-to-use sales brief!
```

🖐️ **Stuck? Raise your hand.**

**Speaker Notes:**
For those building the lead research brief — here's your guide. Follow it step by step. Start with a real company you'd actually want to research. This makes it more valuable because you'll walk out with something you can actually use. If you get stuck at any step, raise your hand. We're here to help.

---

### Slide 20: Option B — Content Repurposer

**Content:**
**Step-by-step guide:**

```
1. First, create some source content to repurpose:
   "Create a file called blog-draft.md with a 300-word blog
   post about [a topic relevant to your work]"

2. Now repurpose it:
   "Read blog-draft.md and rewrite it as a LinkedIn post.
   Make it conversational and hook-first. Keep it under
   1,300 characters. End with a question. Add hashtags."

3. Want to try another format?
   "Now turn the same blog post into a 5-tweet thread"

4. Or an email newsletter intro:
   "Rewrite it as a 100-word email newsletter intro that
   makes people want to click through to read more"
```

🖐️ **Stuck? Raise your hand.**

**Speaker Notes:**
Content repurposers — here's your flow. Start by having Claude Code write a short blog post on a topic relevant to your work. Then we'll repurpose it into different formats. The magic is seeing how one piece of content becomes many. If you have an actual blog post you've written, even better — save it as a .md file and use that.

---

### Slide 21: Option C — Competitor Tracker

**Content:**
**Step-by-step guide:**

```
1. Think of 3 competitors you actually track:
   Company A, Company B, Company C

2. Start Claude Code and type:
   "Research these companies: [Company A URL], [Company B URL],
   [Company C URL]. For each, find: what they do, key products,
   pricing (if public), recent news, strengths, and weaknesses.
   Create a comparison table and save it as competitor-analysis.md"

3. Go deeper:
   "Read competitor-analysis.md. Now add a section analyzing
   how our company [YOUR COMPANY] compares. What are our
   advantages? Where are we vulnerable?"

4. Make it actionable:
   "Add a recommendations section: what should we do based
   on this competitive analysis?"
```

🖐️ **Stuck? Raise your hand.**

**Speaker Notes:**
Competitor tracker builders — use real competitors. This makes the exercise immediately valuable. You'll end up with an actual competitive analysis you can share with your team. Claude Code will search the web, find current info, and structure it. Then we layer on strategic analysis.

---

## BLOCK 6: Show & Tell + Next Steps (30 min)

---

### Slide 22: Show & Tell

**Content:**
**Who wants to share what they built?**

1-2 volunteers: show your screen and walk us through:
- What you built
- What surprised you
- How you'd use this in your real work

👏 *Every workflow built today is a real tool you can use tomorrow*

**Speaker Notes:**
Who wants to share? Don't be shy — everyone here just did something most people in your industry haven't done yet. [Pick 1-2 volunteers.] Walk us through what you built. What worked? What surprised you? How would you use this next week? [Facilitate discussion. Celebrate the wins. Point out creative uses.]

---

### Slide 23: Your Homework (Just One Thing)

**Content:**
**This week, try ONE workflow on real work.**

Not a test. Not practice. Real work.

Ideas:
- Research your next meeting's company before the call
- Repurpose a blog post or report into a LinkedIn post
- Generate a competitive brief for an upcoming pitch
- Draft a follow-up email from your meeting notes

**The habit loop:** Use it once for real → see the value → use it again → it becomes natural

**Speaker Notes:**
Here's your homework. It's just one thing. This week, use Claude Code on one real task. Not a toy example. Real work. The research shows that if you use a new tool on real work within 7 days of learning it, you're 5x more likely to adopt it long-term. The "aha moment" already happened today — now cement it with real use.

---

### Slide 24: Resources and Support

**Content:**
**What you're taking home today:**

📄 **Cheat Sheet** — Terminal commands, prompt templates, MCP guide
📘 **Setup Guide** — For colleagues who want to get started
🔗 **Resources:**
- Claude Code Docs: docs.anthropic.com
- Anthropic Cookbook: github.com/anthropics/anthropic-cookbook
- Prompt Engineering Guide: docs.anthropic.com/prompt-engineering

📧 **15-day post-workshop support:** tchu@novastacks-ai.com
- Stuck? Email us. We'll help.

**Speaker Notes:**
Here's everything you're taking home. The cheat sheet has all the commands and prompt templates. The setup guide is something you can share with colleagues. And you have 15 days of email support — if you try something and get stuck, reach out. We're here to make sure this sticks.

---

### Slide 25: Thank You

**Content:**
**Thank you for building with us today.**

You just did something most professionals haven't done yet.

Keep going. 🚀

**Tina Chu** — tchu@novastacks-ai.com
**Yaohong Ch'ng** — Superuser HQ

**Speaker Notes:**
Thank you everyone. You came in today as people who'd never opened a terminal. You're leaving as people who've built working AI workflows from the command line. That's not a small thing. The gap between knowing about AI and actually using AI to do your work — you just crossed it. Keep going. We're here if you need us.

---

## APPENDIX: Facilitator Notes

### Pre-workshop Checklist
- [ ] Confirm all participants completed setup guide
- [ ] Test WiFi with 20+ devices
- [ ] Prepare demo scripts (Block 1 competitor research, Block 3 lead brief, Block 4 MCP + skill demos)
- [ ] Print cheat sheets (one per participant)
- [ ] Have backup API keys ready for participants with setup issues

### Timing Guide
| Block | Start | End | Duration |
|-------|-------|-----|----------|
| 1: Why This Matters | 0:00 | 0:20 | 20 min |
| 2: Terminal Comfort | 0:20 | 0:40 | 20 min |
| 3: Core Concepts | 0:40 | 1:10 | 30 min |
| 4: MCPs & Skills | 1:10 | 1:30 | 20 min |
| Break | 1:30 | 1:45 | 15 min |
| 5: Guided Build | 1:45 | 2:30 | 45 min |
| 6: Show & Tell | 2:30 | 3:00 | 30 min |

### Common Issues During Workshop
- **Participant can't launch Claude Code:** Check API key, check Node.js version
- **Slow responses:** Too many people on same WiFi. Have mobile hotspot backup.
- **Someone finishes early:** Challenge them to build a second workflow or create a Skill
- **Someone is completely lost:** Pair them with a faster participant (pair debugging)
