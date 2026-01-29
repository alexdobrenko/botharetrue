---
title: 'merging-powerpoint-slides-with-claude-code'
date: 
draft: false
---


## Writer's Brief (Outline)

> This section is a handoff for a writer — what the post is about and what to cover.

### The Hook
I needed 5 new slides for a course I'm teaching in 2 hours and ended up learning that PowerPoint files are just zip archives full of XML — and that merging two presentations is way harder than it should be.

### Main Points to Cover
1. Creating slides from HTML that match an existing deck's exact style — extracting hex colors from XML, writing HTML templates, converting with html2pptx
2. The failed merge attempts — python-pptx loses all formatting, OOXML direct merge produces corrupt files — before landing on "append then rearrange"
3. The meta moment: making slides about building things with Claude Code... using Claude Code to build the slides

### The Angle
The messy reality of "I'll just quickly add some slides" turning into a 30-minute deep dive into PowerPoint's internal XML structure. The gap between "this should be simple" and what actually works.

### Target Reader
Anyone using AI tools to build things who's curious about what happens when you go past the demo. People who've tried to automate "simple" office tasks and discovered the rabbit hole.

### Tone Notes
Casual, self-deprecating, amused by the absurdity. Lean into the comedy of building slides about building things. Don't oversell the technique — it's messy and that's fine.


## The Story

I'm teaching the first session of a course in two hours and I realize the slide deck is missing some pretty important slides. Like an "About Me" slide. And a slide that tells people what we're actually doing today.

So I ask Claude to add them. Simple enough. Except the deck was already built programmatically — HTML files converted to PowerPoint XML — and now I need to merge new slides into an existing presentation without breaking everything.

Here's what I learned: a .pptx file is a zip archive. Inside it's XML all the way down. Every slide, every text box, every background color — it's all angle brackets and namespaces.

First attempt: python-pptx. Clone shapes from one presentation to another. The backgrounds vanished. The rounded rectangles became regular rectangles. The text positions drifted. It looked like someone had photocopied the slides while drunk.

Second attempt: manually edit the OOXML. Copy the slide XML files, update three different metadata files, repack the zip. The validator said no. Corrupt file.

Third attempt: append the new slides to the original's XML structure, force-pack it (skip validation, sorry), then use a rearrange script to shuffle everything into the right order. This produced a clean file.

Three attempts to insert five slides. Each one teaching me something new about how PowerPoint actually works under the hood.

The final deck has 23 slides. The new ones match perfectly — same orange headers, same cream backgrounds, same Impact font screaming "TODAY'S GOAL" at people who signed up to learn Claude Code from a comedian.

The meta thing is that slide 13 says "Making these slides — METAAAAAA" and now that's even more meta because I just made more slides about making slides.
