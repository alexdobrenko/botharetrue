---
title: 'claude-code-image-renaming-workflow'
date: 
draft: false
categories: ["reading"]
---

# Image Renaming Workflow Using Claude Code

## Part 1: Step-by-Step Tutorial

### What This Workflow Does
Use Claude Code to automatically read image files (screenshots, photos, etc.) and rename them with descriptive names based on their content. No more `SCR-20251205-gdoq.png` nonsense.

### The Setup
1. Navigate to the folder containing your cryptically-named images
2. Open Claude Code in that directory

### The Prompt
Just ask Claude to review and rename:

```
review these and rename the photos so its clearer what each one is about
```

That's it. That's the whole prompt.

### What Claude Does Behind the Scenes
1. Lists all files in the directory
2. Reads each image (Claude is multimodal - it can actually see images)
3. Analyzes the content to understand what each image shows
4. Renames files with descriptive names using kebab-case

### Example Results
From Alex's Connor LinkedIn posts folder:

**Before:**
- SCR-20251205-gdoq.png
- SCR-20251205-gdrj.png
- SCR-20251205-gdsx.png
- (10 more equally cryptic names...)

**After:**
- podcast-anthony-romero-aclu-staying-centered.png
- podcast-sarah-cooper-bring-full-self-to-work.png
- podcast-question-crowdsource-leader-topics.png
- (10 more actually useful names...)

### Why This Works
- Claude can read images natively (PNG, JPG, etc.)
- It understands context and can extract meaning
- It follows consistent naming conventions
- It processes all files in one go

### When to Use This
- Screenshot dumps from social media
- Exported images from presentations
- Downloaded files with auto-generated names
- Any batch of images that need organization

### Time Saved
What would take 15-20 minutes of manually opening, reading, and renaming files takes about 30 seconds with Claude.
