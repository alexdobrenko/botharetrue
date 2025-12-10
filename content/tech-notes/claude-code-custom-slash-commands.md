---
title: 'claude-code-custom-slash-commands'
date: 
draft: false
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
