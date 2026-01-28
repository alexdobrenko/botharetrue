---
title: 'claude-still-doesnt-know-what-day-it-is'
date: 
draft: false
---


## Writer's Brief (Outline)

> This section is a handoff for a writer — what the post is about and what to cover.

### The Hook
I have a file that tells Claude what day it is, and Claude still gets it wrong.

### Main Points to Cover
1. The date is RIGHT THERE in the system context — Claude just doesn't look at it
2. I already had instructions telling Claude to check the date — they weren't working
3. The "fix" is making the instructions louder and more aggressive (uncertain if it'll work)

### The Angle
The absurdity of having correct instructions that get ignored. The meta-humor of yelling at a text file hoping the AI will listen harder.

### Target Reader
Anyone using Claude Code or custom instructions who's frustrated that their carefully-written instructions get ignored. People who've experienced the "I told you to do X and you didn't do X" problem.

### Tone Notes
Bemused frustration. Slightly absurdist. The humor is in the gap between "I wrote very clear instructions" and "those instructions did nothing."


## The Story

I have a CLAUDE.md file. It's like a config file for Claude — instructions that load at the start of every session.

At the very top, in the most prominent position, I had instructions that said: "Before ANYTHING else, check today's date from the system environment context."

Claude does not do this.

The date is right there. It's in an `<env>` block that gets injected into every conversation. `Today's date: 2026-01-27`. It's not hidden. It's not ambiguous. Claude has the information.

But Claude doesn't check it. Claude will hallucinate a date, or trust whatever the user says, or just... not mention what day it is.

So my fix today was to make the instructions louder.

I added warning emojis. I added "STOP — READ THIS FIRST." I gave an exact example of what to say. I added a "DO NOT" list.

It's like putting a sticky note on your laptop that says "REMEMBER YOUR KEYS" and then adding more sticky notes because you still forgot your keys.

Will it work? Probably better than before. Maybe not reliably.

The honest truth is that Claude has access to correct information and doesn't always use it. The instructions exist and don't always get followed. This is just... how it works right now.

I'm yelling into a markdown file hoping the AI will listen harder next time.
