# Claude Code Cheat Sheet

**Workshop: Claude Code for B2B Marketing & Sales**
**Date: April 15, 2026 | Prepared by Novastacks AI × Superuser HQ**

---

## Terminal Survival Kit (Only 3 Commands You Need)

| Command | What It Does | Example |
|---------|-------------|---------|
| `pwd` | Shows where you are right now | `pwd` → `/Users/yourname/Documents` |
| `ls` | Lists files in current folder | `ls` → shows all files and folders |
| `cd` | Move into a folder | `cd Desktop` → moves to Desktop |

### Quick Tips
- `cd ..` — Go back one folder (like pressing "Back" in File Explorer)
- `cd ~` — Go to your home folder
- Press **Tab** to auto-complete folder/file names
- Press **Up Arrow** to repeat your last command
- `clear` — Clean up messy terminal screen

### Think of it like File Explorer
| What You Do in Finder/Explorer | Terminal Equivalent |
|-------------------------------|-------------------|
| Look at which folder you're in | `pwd` |
| Open a folder and see what's inside | `ls` |
| Double-click a folder to go into it | `cd folder-name` |
| Click the back button | `cd ..` |

---

## Launching Claude Code

```bash
# Start Claude Code (type this in terminal)
claude

# Start Claude Code in a specific folder
cd ~/Documents/my-project
claude
```

---

## Claude Code Essential Commands

| Command | What It Does |
|---------|-------------|
| `/help` | Show all available commands |
| `/clear` | Clear the conversation and start fresh |
| `/cost` | Check how much you've spent this session |
| `/compact` | Summarize conversation to save context space |
| `/quit` or `Ctrl+C` | Exit Claude Code |

---

## Prompt Templates for Marketing & Sales

### 1. Lead Research Brief
```
Research the company [COMPANY URL]. Give me:
- What they do (1-2 sentences)
- Target market
- Recent news or funding (last 6 months)
- Key decision makers on LinkedIn
- Potential pain points we can solve
Format as a structured brief I can share with my sales team.
```

### 2. Content Repurposer (Blog → LinkedIn)
```
Read the file [blog-post.md]. Rewrite it as a LinkedIn post that:
- Hooks in the first line
- Uses my voice (conversational, insight-driven)
- Keeps it under 1,300 characters
- Ends with a question to drive engagement
- Add 3-5 relevant hashtags
```

### 3. Competitor Tracker
```
Research these competitors: [COMPANY 1], [COMPANY 2], [COMPANY 3].
For each, find:
- Key product/service offerings
- Recent announcements or launches
- Pricing model (if public)
- Strengths and weaknesses vs us
Output as a comparison table.
```

### 4. Email Draft from Meeting Notes
```
Read the file [meeting-notes.md]. Draft a follow-up email that:
- Thanks them for their time
- Summarizes the 3 key points discussed
- Lists agreed next steps with owners
- Suggests a follow-up date
Keep it professional but warm.
```

### 5. Quick Market Research
```
I'm preparing for a meeting with [COMPANY/INDUSTRY].
Give me a 1-page brief covering:
- Industry trends (2025-2026)
- Common challenges
- How companies like ours typically help
- 3 smart questions I can ask in the meeting
```

---

## MCP (Model Context Protocol) — Your Connectors

MCPs let Claude Code connect to your existing tools. Think of them as "plugins."

### Common MCPs for Marketing/Sales Teams

| MCP | What It Connects To | Use Case |
|-----|-------------------|----------|
| Google Drive | Your Drive files | Read/write docs, sheets, slides |
| Google Sheets | Spreadsheets | Pull data, update trackers |
| Gmail | Your inbox | Draft emails, search messages |
| Filesystem | Local files | Read/write files on your computer |
| Web Search | The internet | Research companies, trends |

### How to Check Your MCPs
```
# Inside Claude Code, type:
/mcp
```

---

## Skills — Your Saved Templates

Skills are reusable instruction sets. Think of them like email templates, but for AI tasks.

### How Skills Work
1. You write instructions once
2. Save them as a `.md` file
3. Call them anytime with `/skill-name`

### Example: LinkedIn Post Skill
Create a file at `~/.claude/commands/linkedin-post.md`:
```markdown
Read and execute ~/.claude/skills/linkedin-post.md
```

Then create `~/.claude/skills/linkedin-post.md` with your detailed instructions for writing LinkedIn posts in your voice, style, and format.

---

## File Types That AI Agents Love

| File Type | Extension | Why Agents Like It | Your Equivalent |
|-----------|----------|-------------------|----------------|
| Markdown | `.md` | Simple text with formatting | Like a Word doc, but cleaner |
| Plain Text | `.txt` | No formatting overhead | Notepad files |
| CSV | `.csv` | Structured data | Excel without formulas |
| JSON | `.json` | Structured data for APIs | Like a very organized spreadsheet |
| YAML | `.yaml` | Configuration files | Like a settings form |

### Why Not Word/Excel?
- Word (`.docx`) and Excel (`.xlsx`) are binary files — AI can't read them directly
- Markdown and CSV are plain text — AI reads them instantly
- **Pro tip:** Export your Google Docs as `.md` or paste content into `.md` files for best results

---

## Troubleshooting Quick Fixes

| Problem | Fix |
|---------|-----|
| "command not found: claude" | Reinstall: `npm install -g @anthropic-ai/claude-code` |
| Claude feels slow | Use `/compact` to free up context space |
| Wrong folder / wrong files | Use `pwd` to check where you are, `cd` to navigate |
| API key error | Check your key: `echo $ANTHROPIC_API_KEY` |
| MCP not connecting | Run `/mcp` to check status |
| Stuck / confused | Type `/clear` and start fresh |

---

## Keyboard Shortcuts in Terminal

| Shortcut | What It Does |
|----------|-------------|
| `Tab` | Auto-complete file/folder names |
| `Up/Down Arrow` | Cycle through previous commands |
| `Ctrl + C` | Stop/cancel current command |
| `Ctrl + L` | Clear the screen |
| `Ctrl + A` | Jump to beginning of line |
| `Ctrl + E` | Jump to end of line |

---

## The AI Tools Landscape — Know What's Out There

Understanding where Claude Code fits helps you pick the right tool for each job.

### The Big Picture: 3 Types of AI Tools

| Type | How It Works | Analogy |
|------|-------------|---------|
| **Chat AI** | You ask, it answers. Copy-paste. | Asking a colleague a question |
| **AI Copilot** | Watches you work, suggests as you go | A co-pilot sitting next to you |
| **Agentic AI** | You give a goal, it executes multi-step tasks | A smart intern who does the whole job |

### Tool Comparison — What's What

| Tool | Type | Best For | How You Use It | Price |
|------|------|----------|---------------|-------|
| **Claude Code** | Agentic CLI | Power users who want AI executing real workflows — files, web, tools | Terminal (command line) | $20/mo (Pro) or API |
| **Claude.ai** | Chat + Projects | General-purpose AI chat, analysis, writing, image understanding | Web browser, mobile app | Free – $20/mo |
| **ChatGPT** | Chat + Agents | All-purpose AI chat, image gen, browsing, code | Web browser, mobile app | Free – $200/mo |
| **Microsoft Copilot** | Embedded AI | AI inside Word, Excel, PowerPoint, Outlook, Teams | Inside Microsoft 365 apps | $30/user/mo add-on |
| **Google Gemini** | Embedded AI | AI inside Google Docs, Sheets, Gmail | Inside Google Workspace | Free – $20/mo |
| **Cursor** | AI Code Editor | Developers who want AI pair-programming in their editor | Desktop app (VS Code-like) | Free – $40/mo |
| **GitHub Copilot** | AI Code Assistant | Developers in the GitHub ecosystem | IDE extension + GitHub | Free – $39/mo |
| **Manus AI** | Fully Autonomous Agent | Non-technical users who want to delegate entire tasks | Web browser | Invite-based |
| **Devin** | AI Software Engineer | Engineering teams offloading dev tasks | Web interface | ~$500/mo |
| **Replit Agent** | AI App Builder | Non-devs who want to build apps from descriptions | Web browser | ~$25/mo |
| **Bolt.new** | AI App Builder | Rapid prototyping of web apps | Web browser | Free – $20/mo |

### When to Use What — A Decision Guide

```
"I need to write/analyze/brainstorm"
  → Claude.ai or ChatGPT (chat interface, no setup)

"I need AI inside my Word/Excel/Slides"
  → Microsoft Copilot or Google Gemini

"I need to automate a multi-step workflow"
  → Claude Code (this workshop!) or Manus AI

"I need to build an app or website"
  → Replit Agent, Bolt.new, or Cursor

"I need AI to write/review code"
  → Cursor, GitHub Copilot, or Claude Code
```

### Why We're Teaching Claude Code

| Feature | Claude Code | Chat AI (ChatGPT/Claude.ai) |
|---------|------------|----------------------------|
| Reads your actual files | ✅ Directly | ❌ Must upload/paste |
| Connects to your tools | ✅ Via MCPs (Drive, Gmail, Sheets) | ❌ Limited plugins |
| Multi-step execution | ✅ Plans and executes autonomously | ❌ One response at a time |
| Saves reusable workflows | ✅ Skills & commands | ❌ Must re-explain each time |
| Works with your real data | ✅ On your machine | ⚠️ Upload limits, privacy concerns |
| Requires terminal | ✅ Yes (but only 3 commands!) | ❌ No |

**Bottom line:** Chat AI is great for quick questions. Claude Code is for getting real work done at scale.

---

## Resources for Continued Learning

### Free Courses (Start Here)
| Course | Provider | What You'll Learn | Link |
|--------|----------|------------------|------|
| Claude Code in Action | Anthropic (Skilljar) | Hands-on Claude Code with certificate | anthropic.skilljar.com/claude-code-in-action |
| Claude Code: Highly Agentic Coding Assistant | Andrew Ng × Anthropic (DeepLearning.AI) | Deep dive with Anthropic's Head of Technical Education | learn.deeplearning.ai/courses/claude-code |
| Introduction to MCP | Anthropic (Skilljar) | Understanding and setting up MCPs | anthropic.skilljar.com/introduction-to-model-context-protocol |
| All Anthropic Courses | Anthropic | Full course catalog | anthropic.skilljar.com |

### Official Anthropic Resources
| Resource | What It Covers | Link |
|----------|---------------|------|
| Claude Code Docs | Full reference for all commands and features | docs.anthropic.com/en/docs/claude-code |
| Prompt Engineering Guide | How to write effective prompts | docs.anthropic.com/en/docs/build-with-claude/prompt-engineering |
| MCP Documentation | Model Context Protocol spec and setup | modelcontextprotocol.io |
| How Anthropic Uses Claude in Marketing | Real case study — non-technical marketers using Claude Code | claude.com/blog/how-anthropic-uses-claude-marketing |
| How Anthropic Teams Use Claude Code | Internal case studies across departments | claude.com/blog/how-anthropic-teams-use-claude-code |
| Claude Customer Stories | Enterprise case studies across industries | claude.com/customers |
| Claude Use Cases | Use case gallery by function | claude.com/resources/use-cases |
| Claude Cowork | Visual interface for Claude (no terminal needed) | claude.com/product/cowork |

### Terminal Basics (If You Want More Practice)
| Resource | Level | Link |
|----------|-------|------|
| Command Line for Beginners | Zero to comfortable | freecodecamp.org/news/command-line-for-beginners |
| Learn Enough Command Line to Be Dangerous | The essentials only | learnenough.com/command-line-tutorial |

### Expert Tips Worth Bookmarking
- **Amanda Askell** (Anthropic, Alignment Lead) — "Be honest with the model. Tell it exactly what you need. Iterate like you would with a human."
- **Anthropic prompt engineers in Fortune** — 3 prompting tips for work success
- **Zack Proser** (Anthropic Staff DevRel) — Claude Cowork workshop walkthrough: zackproser.com/blog/claude-cowork-workshop-anthropic

---

*Prepared by Novastacks AI × Superuser HQ | April 2026*
