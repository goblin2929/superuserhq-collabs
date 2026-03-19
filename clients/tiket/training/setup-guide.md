# Pre-Workshop Setup Guide

**Workshop: Claude Code for B2B Marketing & Sales**
**Date: April 15, 2026**

Please complete these steps **before** the workshop. Budget 15-20 minutes. If you get stuck on any step, email tchu@novastacks-ai.com — we'll help you get set up before the session.

---

## Step 1: Check Your Operating System

| If you're on... | You're good to go |
|----------------|-------------------|
| **Mac** | ✅ Terminal is built-in |
| **Windows** | ⚠️ You need WSL (see Step 1b below) |
| **Linux** | ✅ Terminal is built-in |

### Step 1b: Windows Users Only — Install WSL
1. Open **PowerShell** as Administrator (right-click → "Run as administrator")
2. Type: `wsl --install`
3. Restart your computer
4. A Ubuntu window will open — create a username and password
5. You now have a Linux terminal inside Windows

---

## Step 2: Install Node.js

Claude Code needs Node.js to run (think of it as the "engine").

### Mac
1. Open **Terminal** (search "Terminal" in Spotlight, or find it in Applications → Utilities)
2. Copy and paste this command, then press Enter:
```bash
curl -fsSL https://fnm.vercel.app/install | bash
```
3. Close and reopen Terminal
4. Run:
```bash
fnm install --lts
```
5. Verify it worked:
```bash
node --version
```
You should see something like `v22.x.x` ✅

### Windows (in WSL/Ubuntu terminal)
Same commands as Mac above.

---

## Step 3: Install Claude Code

In your terminal, run:
```bash
npm install -g @anthropic-ai/claude-code
```

Verify it worked:
```bash
claude --version
```

You should see a version number ✅

---

## Step 4: Get Your API Key

You need an Anthropic API key (this is how Claude Code connects to Claude).

### Option A: Anthropic API Key (Pay-per-use)
1. Go to https://console.anthropic.com
2. Sign up or log in
3. Go to **API Keys** in the left sidebar
4. Click **Create Key**
5. Copy the key (starts with `sk-ant-...`)
6. In your terminal, run:
```bash
export ANTHROPIC_API_KEY="sk-ant-your-key-here"
```

### Option B: Claude Pro/Max Subscription
If you have a Claude Pro or Max subscription, Claude Code can authenticate through your browser:
1. In terminal, just type `claude`
2. It will open a browser window for you to log in
3. Approve the connection

> **Note:** Your company may provide API keys for the workshop. Check with your team lead.

---

## Step 5: Install VS Code (Recommended but Optional)

VS Code is a free code editor — think of it as a "smart Notepad" with a built-in terminal.

1. Download from https://code.visualstudio.com
2. Install and open it
3. Open the built-in terminal: **View → Terminal** (or press `` Ctrl+` ``)

### Why VS Code?
- You can see your files AND terminal in one window
- Easier to read and edit files Claude Code creates
- Not required, but makes the workshop smoother

---

## Step 6: Create Your Workshop Folder

In terminal, run:
```bash
mkdir -p ~/claude-workshop
cd ~/claude-workshop
```

This creates a dedicated folder for the workshop exercises.

---

## Step 7: Test Everything

Run these commands one at a time:

```bash
# 1. Check Node.js
node --version

# 2. Check Claude Code
claude --version

# 3. Go to your workshop folder
cd ~/claude-workshop

# 4. Launch Claude Code
claude
```

If Claude Code starts and you see a prompt, you're ready! 🎉

Type `/quit` to exit for now.

---

## Pre-Workshop Checklist

- [ ] Terminal opens without errors
- [ ] Node.js is installed (`node --version` shows a number)
- [ ] Claude Code is installed (`claude --version` shows a number)
- [ ] API key is set up (or you have Claude Pro/Max)
- [ ] VS Code is installed (optional but recommended)
- [ ] Workshop folder created (`~/claude-workshop`)
- [ ] Claude Code launches successfully

---

## Common Setup Issues

| Problem | Solution |
|---------|---------|
| "npm: command not found" | Node.js isn't installed yet — go back to Step 2 |
| "permission denied" on Mac | Add `sudo` before the command: `sudo npm install -g @anthropic-ai/claude-code` |
| Claude Code won't launch | Check your API key: `echo $ANTHROPIC_API_KEY` |
| "EACCES" error on npm install | Run: `sudo chown -R $(whoami) /usr/local/lib/node_modules` |
| WSL won't install (Windows) | Make sure you're running PowerShell as Administrator |
| VS Code terminal feels different | Make sure terminal is set to "bash" or "zsh" (not PowerShell) |

---

## Need Help?

Email **tchu@novastacks-ai.com** with:
- Your operating system (Mac/Windows/Linux)
- Screenshot of the error
- Which step you're stuck on

We'll respond within 24 hours and get you set up before the workshop.

---

*Prepared by Novastacks AI × Superuser HQ | April 2026*
