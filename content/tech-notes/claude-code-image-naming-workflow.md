---
title: 'claude-code-image-naming-workflow'
date: 
draft: false
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
