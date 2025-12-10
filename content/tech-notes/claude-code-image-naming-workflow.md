---
title: Image Naming Workflow Using Claude Code
date: 2025-12-08
draft: false
date updated: 2025-12-10 16:09
---
# Image Naming Workflow Using Claude Code

## Part 1: Tutorial

**The task:** 125 event photos named `001.jpg` through `125.jpg`. Need them searchable and web-ready.

**What I did:**
1. Asked Claude Code to review images in batches of 10
2. It looked at each image, described what it saw, renamed the file
3. Then ran a resize script to get everything under 1MB

**The prompt:**
```
Review images 001.jpg through 010.jpg in [folder] and rename them based on what's in each image
```

**Naming pattern Claude used:**
```
001.jpg → 001_venue-entrance-with-stacks-joules-banner.jpg
019.jpg → 019_graduate-derek-presenting-with-attendees.jpg
060.jpg → 060_klein-tools-clamp-meter-closeup.jpg
```

**The resize (macOS):**
```bash
for img in *.jpg; do
  sips --resampleWidth 1920 "$img" --out "for web/$img"
  # reduce quality if still over 1MB
done
```

**Results:**
- 125 images renamed in ~5 minutes
- 1.6 GB → 71 MB
- Every file now searchable by what's in it

---

## Part 2: Blog Post

The thing that gets me is how boring this task used to be.

125 graduation photos. `001.jpg` through `125.jpg`. The old way: open each one, squint at it, type something descriptive, move to the next. An hour of mind-numbing work that I'd keep putting off until the photos sat in a folder for six months.

Here's what's both true: AI is overhyped AND it's genuinely good at tasks like this.

I asked Claude Code to look at 10 images at a time and rename them based on what it saw. It described graduates at demo stations, HVAC equipment closeups, group photos with specific poses. Things I would've named `grad-demo-1.jpg` became `043_graduate-wiring-transformer-hands-on.jpg`.

Ten minutes later, 125 files had real names. Then a quick resize script knocked them from 1.6 GB down to 71 MB for web use.

Small wins compound. A folder of searchable, web-ready photos instead of mystery JPGs I'll never look at again.

The unsexy truth about working with AI: it's not about the flashy stuff. It's about the tedious tasks you've been avoiding. The ones that aren't hard, just annoying enough that they never get done.

Those are the wins that actually change your workflow.
