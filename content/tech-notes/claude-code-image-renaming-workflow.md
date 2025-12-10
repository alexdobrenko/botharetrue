---
title: Image Renaming Workflow Using Claude Code
date: 2025-12-05
draft: false
date updated: 2025-12-10 16:09
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

---

## Part 2: Blog Post - "The AI Will Read Your Screenshots So You Don't Have To"

I just did something that felt both incredibly mundane and slightly magical.

I had 13 screenshots of Connor's LinkedIn posts sitting in a folder. You know the ones - those Mac screenshot names that look like someone sneezed on a keyboard: `SCR-20251205-gdoq.png`. I needed to rename them with actual descriptions so I could find them later. The kind of task that makes you question your career choices. Open image. Read it. Think of a name. Type it out. Repeat 12 more times.

Instead, I asked Claude to do it. Just: "review these and rename the photos so it's clearer what each one is about."

And it did. All of them. In seconds. Because Claude can read images. It looked at each screenshot of a LinkedIn post, understood what it was about, and renamed it something useful like `podcast-sarah-cooper-failure-snl-audition.png` instead of `SCR-20251205-gduk.png`.

Here's what's both true: This is a trivial task that saved me maybe 15 minutes. And also, these 15-minute tasks are exactly why you never get to the work that matters. You can dismiss this as "just file organization" or you can recognize it as reclaiming your attention for something better. Both are true.

The deeper thing here isn't about automation or efficiency. It's about noticing where your brain is being wasted. I wasn't going to learn anything from reading those LinkedIn posts for the fifth time while renaming files. I already pulled the insights I needed. This was pure organizational overhead - necessary but not meaningful. The kind of thing that compounds into hours of "where did my day go?"

What gets me is how simple it was. No complex workflow. No API setup. Just ask. The AI equivalent of "hey, could you handle this tedious thing while I go do something that requires an actual human?" Small wins compound. This one just bought me 15 minutes to write instead of rename. I'll take it.
