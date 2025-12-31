---
title: 'Building a Reddit Briefing Agent That Emails You What Matters'
date: 2025-12-30
draft: false
---

## Part 1: Step-by-Step Tutorial

### What This Workflow Does
Scrapes a subreddit via Apify, sends the posts to Claude for analysis, and emails you a smart summary. Runs automatically every 8 hours via GitHub Actions. You wake up to a briefing that tells you what's actually worth knowing.

### The Setup
- GitHub repo with Actions enabled
- Secrets configured: `APIFY_TOKEN`, `ANTHROPIC_API_KEY`, `RESEND_API_KEY`, `EMAIL_TO`
- Python script that orchestrates the whole thing

### The Prompt
The analysis prompt tells Claude to be a "sharp, no-BS analyst" and organize findings into:
- 🚨 Action Required (critical bugs, breaking changes)
- 🛠️ Tools & Projects (with links)
- 💡 Tips & Workarounds
- 📊 Community Mood
- 📚 Course Material
- ⏭️ Skip (noise to ignore)

### What Claude Does Behind the Scenes
1. Apify scrapes the subreddit (50 posts, 30 comments each)
2. Claude analyzes the raw JSON with your context in mind
3. Markdown gets converted to styled HTML
4. Resend delivers it to your inbox

### Example Results
**Before:** Manually checking r/claudecode, scrolling past memes, missing the one post about a critical security issue

**After:** Email arrives with "🚨 Action Required: A self-hosted Claude Code runner was posted with NO authentication. If you deployed it, shut it down now."

### Why This Works
- Apify handles Reddit's anti-scraping measures
- Claude filters signal from noise with your specific interests in mind
- GitHub Actions runs it for free, forever
- Email means you don't have to remember to check anything

### When to Use This
- Monitoring niche subreddits for your industry
- Keeping up with fast-moving AI tool communities
- Research for courses or content you're creating

### Time Saved
What would take 30 minutes of scrolling takes 2 minutes of reading.

---

## Part 2: Blog Post - "I Made Reddit Email Me"

I have a Reddit briefing that runs three times a day now. It watches r/claudecode and sends me an email with what's happening.

The weird part is how it categorizes things. There's a "Skip" section at the bottom where Claude lists everything it saw but decided wasn't worth my time. "Generic 'how to prompt better' discussions without actionable insights. Philosophical rambling about AI and code ownership."

It's like having a research assistant who's slightly judgy. Which I guess is what I asked for when I told it to be "sharp, no-BS."

Today's briefing had a security warning at the top. Someone posted a self-hosted Claude Code runner with no authentication, HTTP only, full system access. Got 14 upvotes before anyone pointed out the massive security holes. Claude flagged it as "Action Required" and I thought, huh, that's actually useful.

The formatting was broken for a while. Just raw markdown showing up in my inbox. Asterisks everywhere. Had to add a proper markdown-to-HTML converter which felt like one of those things that should have been obvious from the start.

There's also a trick I learned: you can add `.json` to any Reddit URL and get back structured data with upvote counts. So if someone asks "what are the best projects people built with Claude Code?" I can just scrape that thread and sort by upvotes. The internet has all these little doors if you know where to push.

I don't know what I'm going to do with these briefings exactly. But I like that they show up.
