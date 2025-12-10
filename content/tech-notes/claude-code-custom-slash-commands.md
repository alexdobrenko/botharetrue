---
title: Creating Custom Slash Commands in Claude Code
date: 2025-12-05
draft: false
date updated: 2025-12-10 16:09
---
# Creating Custom Slash Commands in Claude Code

## Part 1: Step-by-Step Tutorial

### What This Workflow Does
Create a reusable slash command in Claude Code that you can trigger anytime to document your session and turn it into a blog post.

### The Setup
Alex had just used Claude to rename a bunch of screenshot files. Then asked:

```
awesome. so now is there a slash command I can use to do this whenever i'm using claude code?
```

### What Claude Did

1. **Created the commands directory** (if it doesn't exist):
   ```bash
   mkdir -p /Users/sash/.claude/commands
   ```

2. **Created a markdown file** at `/Users/sash/.claude/commands/document-session.md` with the prompt instructions

3. **The command file contents:**
   ```markdown
   Review what just happened in this conversation and create a markdown file with two sections:

   ## Section 1: Step-by-Step Instructions
   Document exactly what the user did, the prompts used, and what Claude did in response...

   ## Section 2: Blog Post
   Write a SHORT blog post in the "Both Are True" newsletter style...

   Save the markdown file to: /Users/sash/Documents/VAULTS/the work (public?)/
   ```

### How Custom Slash Commands Work
- Put a `.md` file in `~/.claude/commands/`
- The filename becomes the command: `document-session.md` → `/document-session`
- The file contents become the prompt that runs when you invoke it
- You can use `$ARGUMENTS` placeholder to pass in additional context

### Your New Command
**Command:** `/document-session`

**What it does:**
- Reviews the current conversation
- Creates step-by-step instructions
- Writes a Both Are True style blog post
- Saves to your Obsidian vault

### Other Command Ideas
You could create:
- `/rename-images` - Rename all images in current directory
- `/summarize` - Summarize what was accomplished
- `/commit-message` - Generate a commit message for current changes
- `/blog-draft` - Turn any conversation into a blog post

---

## Part 2: Blog Post - "Teaching Claude Your Shortcuts"

The meta moment just happened.

I used Claude to rename some files. Then I asked if there was a slash command to document what we did. There wasn't. So Claude made one. Then I asked Claude to run the command on... the conversation where we made the command.

Both are true: this is absurdly recursive and also exactly how tools should work. You use something, notice friction, and smooth it out for next time. The tool learns your patterns. Except here "the tool learning" is literally just a markdown file in a folder.

That's the part that gets me. Custom slash commands in Claude Code are just text files. No code. No config. No API. You write what you want to happen in plain English, save it as `whatever.md`, and now `/whatever` is a thing you can do. It's almost disappointingly simple.

I now have a `/document-session` command that will review any Claude Code conversation, extract the workflow into reusable steps, write it up in my voice, and save it to my Obsidian vault. Took about 30 seconds to create.

The unsexy truth about productivity: it's not about the big systems. It's about noticing the thing you'll do again and making it one step easier. Then doing that a hundred times. Compound interest for your workflows.
