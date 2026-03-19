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

## Resources for Continued Learning

- **Claude Code Docs:** https://docs.anthropic.com/en/docs/claude-code
- **Anthropic Cookbook:** https://github.com/anthropics/anthropic-cookbook
- **Prompt Engineering Guide:** https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering

---

*Prepared by Novastacks AI × Superuser HQ | April 2026*
