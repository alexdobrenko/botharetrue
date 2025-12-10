---
title: 'claude-code-blog-publishing-workflow'
date: 
draft: false
categories: ["reading"]
---

# Blog Publishing Workflow Using Claude Code

## Part 1: Tutorial

**The setup:** I write in Obsidian. My blog runs on Hugo with the PaperMod theme, hosted on Netlify. I needed a way to go from markdown file → live on botharetrue.com with one command.

**The solution:** A bash script that syncs from my vault, converts Obsidian syntax to Hugo, handles images, commits to git, and waits for Netlify deployment.

### Folder Structure

**Source (Obsidian vault):**
```
/Documents/VAULTS/the work (public?)/
├── ready to publish/     # Main posts go here
└── tech-notes/           # Tech tutorials (hidden from main feed)
```

**Destination (Hugo blog):**
```
/botharetrue-blog/content/
├── posts/                # Shows on homepage
└── tech-notes/           # Doesn't show on homepage (separate section)
```

### The Command

```bash
~/HQ-Clean/Dev/publish-to-blog.sh
```

That's it. One command.

### What the Script Does

1. **Finds new/updated files** — Checks both `ready to publish/` and `tech-notes/` for markdown files modified in the last 7 days

2. **Routes to correct destination** — Files from `tech-notes/` go to `/content/tech-notes/`, everything else goes to `/content/posts/`

3. **Converts Obsidian → Hugo syntax:**
   - Strips Obsidian frontmatter, adds Hugo frontmatter
   - Converts `![image.jpg](/images/image.jpg)` → standard markdown images
   - Converts Obsidian callouts → HTML
   - Converts standalone YouTube URLs → Hugo shortcodes
   - Removes wiki-style `links`

4. **Handles images** — Finds images in my Attachments folder, copies to `/static/images/`

5. **Validates YAML** — Catches frontmatter errors before they break the build

6. **Git commit + push** — Auto-commits with a list of published posts

7. **Waits for Netlify** — Polls deployment status until it's live (or fails)

### Frontmatter Requirements

Minimal frontmatter needed:
```yaml
```

The script auto-detects categories (e.g., adds `reading` category if post mentions books).

### Hiding Posts from Main Feed

Two ways:

1. **Put in `tech-notes/`** — The `hugo.toml` has `mainSections = ["posts"]`, so only `/content/posts/` shows on the homepage

2. **Add frontmatter flag** — Any post with `hiddenInHomeList: true` gets filtered out (custom logic in `layouts/index.html`)

### Helper Scripts

The main script calls these for syntax conversion:

- `convert-callouts.py` — Obsidian callouts → HTML
- `convert-image-syntax.py` — `!image` → `![](/images/image)`

### Example Run

```
$ ~/HQ-Clean/Dev/publish-to-blog.sh

🔍 Checking for new or updated posts...
📝 Found files to publish:
   ✨ claude-code-chief-of-staff-workflow (new)
   🔄 my-existing-post (updated)

Publish/update these posts? (y/n) y

📄 Processing: claude-code-chief-of-staff-workflow
   ✅ Published: claude-code-chief-of-staff-workflow.md

📦 Committing to git...
🚀 Pushing to GitHub...
⏳ Waiting for Netlify deployment...
   Building... (5/60)
   Building... (10/60)
✅ Deployment successful!
   Live at: https://botharetrue.com
```
