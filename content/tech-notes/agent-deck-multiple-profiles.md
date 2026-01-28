---
title: 'agent-deck-multiple-profiles'
date: 
draft: false
---


## Writer's Brief (Outline)

> This section is a handoff for a writer — what the post is about and what to cover.

### The Hook
When your AI session manager gets too cluttered, you can just ask the AI to reorganize it — and it knows exactly which JSON files to edit.

### Main Points to Cover
1. Agent Deck stores everything in simple JSON files — profiles are just folders with sessions.json
2. Claude can read the structure, identify which sessions belong where, and create clean new profiles
3. The meta moment: using Claude Code to reorganize your Claude Code session manager

### The Angle
Personal discovery — hit a wall with cluttered sessions, asked Claude if reorganization was possible, turned out to be trivially easy because it's all just JSON.

### Target Reader
People using Agent Deck (or similar session managers) who have accumulated too many sessions and want to separate work contexts. Also anyone curious about the "AI working on its own tools" dynamic.

### Tone Notes
Casual, amused by the meta-ness of it. Not a tutorial — more "huh, that was easy."


## The Story

My Agent Deck was getting unusable. 34 sessions across like 15 different projects, some collapsed, some expanded, episodes nested under clients nested under categories. Every time I opened it I had to scroll and squint.

I knew there was a profiles feature. I'd seen it in the help output once. But I'd never used it because — I don't know, seemed like work? Migration anxiety?

So I asked Claude: "How easy would it be for you to reorganize all of this?"

It just... looked at the files. Found `~/.agent-deck/profiles/default/sessions.json`. Read the whole thing. "This is very easy to reorganize on the backend. It's just a JSON file."

Five minutes later I had three profiles. One for personal work. One for the podcast. One for all my consulting clients. Each one clean, organized, minimal.

The weird part is watching Claude create the new JSON files — copying session objects, adjusting group paths, removing the old ones from default. It's just text manipulation. But it's text manipulation on the tool I use to manage Claude sessions.

Turtles all the way down, I guess.
