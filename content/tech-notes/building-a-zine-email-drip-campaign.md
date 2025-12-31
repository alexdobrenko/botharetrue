---
title: Building a Zine Email Drip Campaign with Claude Code
date: 2025-12-26
draft: false
date updated: 2025-12-26
---
# Building a Zine Email Drip Campaign with Claude Code

## Part 1: Tutorial

**The project:** Turn a month of daily journal entries into a "zine" — 58 notes delivered via email over ~30 days, at roughly the same times they were originally written. Plus a website to read everything at once.

**The stack:**
- Content: Markdown files in Obsidian
- Website: Static HTML on Netlify
- Email delivery: Loops.so
- Build tool: Python script + Claude Code

### The Content Structure

Source files live in an Obsidian vault with YAML frontmatter:

```
/Nov 14-Dec 13 2015/release/
├── intro.md
├── 01-just-made-this-vault.md
├── 02-heres-a-post-on-linkedin.md
├── ...
└── 58-recommendations-and-thank-you.md
```

Each markdown file has:
```yaml
---
title: "Just made this vault"
timestamp: Sat 11/15 6:42a
order: 1
note: "optional editor's note"
---

[editor's note: context from future me]

---

The actual content here...
```

### The Build Script

One Python script (`build_all.py`) generates everything:

```bash
python3 build_all.py
```

**What it does:**

1. **Reads all markdown files** — Parses YAML frontmatter, extracts content, handles editor's notes
2. **Generates the website** — Single-page HTML with scroll view, one-by-one view, modals, dark theme
3. **Generates 58 HTML emails** — Each with consistent header/footer, post number, links back to website
4. **Creates a schedule.json** — Maps post order to titles and filenames

### Website Features

The generated `index.html` includes:

- **Two reading modes:** Scroll through all posts or navigate one-by-one with arrow keys
- **Collapsible hero:** Full intro on first visit, compact header after you start reading
- **Cover image:** Custom artwork as hero and OpenGraph image
- **Modals:** About section with email signup link
- **Mobile responsive:** Works on phone/tablet
- **Semi-transparent page picker:** Fixed navigation for one-by-one mode

### Email Structure

Each email HTML has:
- Header with post number ("Note 12 of 57")
- The content with images
- Horizontal rule
- Footer with project description and links
- Unsubscribe link (required for Loops)

### Converting to Loops Format

Loops accepts MJML (email markup language) in zip files. The conversion script:

```python
# For each HTML email:
1. Extract body content
2. Convert HTML tags to MJML equivalents
3. Add unsubscribe link with {{unsubscribeUrl}} placeholder
4. Bundle with any images in img/ folder
5. Create zip: email-XX/index.mjml + email-XX/img/
```

### Calculating Email Delays

The original timestamps determine send times. A script parses them and calculates relative delays:

```
| Email | Delay After Previous |
|-------|---------------------|
| 0 (intro) | immediately |
| 1 | 30 min |
| 2 | 30 min |
| 3 | 6 hours |
| ...
| 55 | 7 days |
| 56 | 3 days |
| 57 | 30 min |
| 58 | 1 day |
```

This preserves the original rhythm — bursts of notes on some days, gaps on others.

### Loops Setup

1. **Create a mailing list** for zine subscribers
2. **Create a signup form** that adds contacts to that list
3. **Create a sequence** triggered by "Contact added to list"
4. **Upload each email zip** and set the delay
5. **Connect a sending domain** (DNS records for DKIM/SPF)

### Signup Flow

Two entry points:
- **Website:** "Get It By Email" button → Loops signup form
- **Direct link:** `signup-form.html` with email input → Loops API

### File Organization

```
/zine-prototype/
├── build_all.py           # Main build script
├── index.html             # Generated website
├── signup-form.html       # Loops signup page
├── images/                # All images including cover
├── emails/resend/         # Generated HTML emails
└── loops-uploads/         # MJML zips for Loops
    ├── email-00.zip       # Intro
    ├── email-01.zip
    └── ...
```

### Key Lessons

1. **Timestamps matter** — Preserving original send times creates authenticity
2. **Minimum delays** — Set 30-min minimum for same-timestamp posts
3. **Unsubscribe required** — Email services require `{{unsubscribeUrl}}` placeholder
4. **Images in zips** — MJML needs images bundled, not external URLs
5. **Test one first** — Upload a single email to verify formatting before all 59

---

## Part 2: Blog Post

I spent a month writing down every thought. Now I'm sending them to people, one at a time, at the same times I originally wrote them.

It's called "life is a crying baby" — 57 notes from November 15 to December 13, 2025. Less zine, more journal.

The technical challenge: how do you turn 58 markdown files into a proper email drip campaign? Not a newsletter blast. A slow drip. Note 13 arrives 20 hours after Note 12 because that's when I wrote it. Note 38 through 43 come rapid-fire, 30 minutes apart, because I was on a roll that morning.

The rhythm is the point.

Here's what I built:
- A website where you can scroll through everything or click through one-by-one
- 59 MJML email templates (intro + 58 notes) with proper unsubscribe links
- A schedule mapping each email to its delay: "send this one 6 hours after the last one"

The whole thing runs on Loops.so for email delivery, Netlify for hosting, and a Python script that converts my Obsidian markdown into both website and email format.

What surprised me: the hardest part wasn't the code. It was the editing. Going back through a month of raw thoughts, adding "editor's notes" from future-me, deciding what to cut (very little), fixing typos (many).

The code was actually straightforward. Parse markdown. Extract timestamps. Calculate delays. Generate HTML. Bundle into zips. The kind of glue work that Claude Code excels at — tedious, mechanical, but requiring just enough judgment that you can't fully automate it.

The unsexy truth about creative projects: most of the work is logistics. Writing the notes took a month. Building the delivery system took a day. But without that day, the notes would just sit in my Obsidian vault forever.

Sometimes the creative work is the infrastructure that lets other creative work exist in the world.

---

**Project:** [life-is-a-crying-baby.netlify.app](https://life-is-a-crying-baby.netlify.app)
