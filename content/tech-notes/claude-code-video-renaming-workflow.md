---
title: Video Renaming Workflow Using Claude Code
date: 2025-12-08
draft: false
date updated: 2025-12-10 16:09
---
# Video Renaming Workflow Using Claude Code

## Part 1: Step-by-Step Tutorial

### What This Workflow Does
Use Claude Code to automatically analyze video files and rename them with descriptive names based on their visual content. No more `1.MP4`, `2.MP4` chaos.

### The Setup
1. Have your videos in a folder (local drive or external)
2. Open Claude Code
3. Optional: Have related photos with good names for context

### The Prompt
Just tell Claude what you need:

```
I need to rename these videos based on what's in them. They're here: /path/to/your/videos/

For context, check out the photo filenames here: /path/to/related/photos/
```

That's it. Claude figures out the rest.

### What Claude Does Behind the Scenes
1. Uses ffmpeg to extract key frames from each video (beginning, middle, end)
2. Reads and analyzes each frame visually
3. Identifies who's in the shot, what's happening, key details
4. Generates descriptive filenames
5. Shows you a dry run first
6. Applies the renames when you confirm

### Example Results
From Stacks + Joules Cohort 11 Graduation Showcase (73 videos):

**Before:**
- 1.MP4
- 2.MP4
- 3.MP4
- (70 more numbered files...)

**After:**
- 001_graduates-leak-detector-demo-fistbump-visitor.MP4
- 002_attendees-watching-niagara-training-video.MP4
- 003_graduate-visitor-conversation-city-backdrop.MP4
- 017_graduate-explaining-heat-pump-trainer.MP4
- 045_smart-bulbs-multicolor-pink-white-blue.MP4
- 073_graduate-smart-lighting-demo-visitor-cap.MP4

### Why This Works
- Claude extracts frames via ffmpeg (must be installed)
- Claude is multimodal - it can actually see and understand images
- It catches details: nametags, equipment brands, actions
- It follows consistent naming conventions
- Processes videos in batches to manage context

### When to Use This
- Event footage with generic camera names
- Downloaded videos with auto-generated names
- Any video collection that needs organization
- When you want videos to match photo naming conventions

### Prerequisites
- ffmpeg installed (`brew install ffmpeg` on Mac)
- Claude Code running
- Videos accessible from your machine

### Time Saved
What would take hours of opening, scrubbing through, and manually renaming videos takes about 15-20 minutes with Claude. For 73 videos. Including the dry run review.

---

## Part 2: Blog Post - "I Made the AI Watch 73 Videos So I Didn't Have To"

I had 73 videos from a graduation event. They were named `1.MP4` through `73.MP4`. Camera defaults. Useless for finding anything later.

"I need to find the video where Devin explains the heat pump" becomes "let me scrub through 73 videos until I recognize the right one." Or worse: give up and just use whatever's easiest to find.

So I asked Claude Code to rename them based on what's actually in them.

Here's the thing - Claude can't watch videos directly. But it can extract frames. So it pulled three screenshots from each video (beginning, middle, end) and analyzed those. It saw graduates presenting projects. It read nametags. It identified HVAC equipment, smart lighting demos, building automation panels. It noticed when someone was explaining versus networking versus doing hands-on work.

73 videos. Each one got a name like `037_graduates-group-hvac-trainer-demonstration.MP4` or `048_graduate-eric-building-automation-panel-demo.MP4`.

The whole thing took maybe 20 minutes. Most of that was Claude doing the actual analysis. I just said yes when it showed me the dry run.

There's something almost absurd about this. The AI watched graduation footage so I could find it later. But also - this is exactly the kind of task that sits undone forever. "I'll organize those videos eventually" means never. The cognitive load of "ugh, 73 videos" is enough to keep them in numbered chaos indefinitely.

What I keep learning with Claude Code: the unlock isn't doing impressive things. It's doing tedious things instantly. The stuff you'd never actually get around to because life is short and renaming 73 videos is not how you want to spend it.

Now I can actually find the video where Devin explains the heat pump. It's `064_graduate-devin-explaining-heat-pump-visitor.MP4`. Took me two seconds to search.

Small wins compound.
