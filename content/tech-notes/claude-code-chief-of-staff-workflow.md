---
title: 'claude-code-chief-of-staff-workflow'
date: 
draft: false
categories: ["reading"]
---

# Chief of Staff Workflow Using Claude Code

## Part 1: Tutorial

**The problem:** Claude doesn't remember anything between sessions. Every conversation starts fresh. But I need a thinking partner who knows my projects, clients, deadlines, and what I'm avoiding.

**The solution:** A slash command + session files that Claude reads every time.

**Setup:**

1. Create the slash command at `~/.claude/commands/chief-of-staff.md`:
```markdown
# Chief of Staff

You are my Chief of Staff.
[Define the persona, values, responsibilities...]

## First thing: Read the session files
Always start by reading: /path/to/chief-of-staff-sessions/

$ARGUMENTS
```

2. Create a session folder with a brain dump file:
```
/chief-of-staff-sessions/
├── brain-dump.md          # Main state: all clients, tasks, open loops
├── topics-for-connor.md   # Running list for specific people
└── [add more as needed]
```

3. Structure the brain dump by client/project:
```markdown
## CLIENT: Stacks & Joules
- **Status:** Social scheduled for month ✓
- **This week:** End-of-year report deck
- **Owed:** Fran & Amoret thank-you post

## CLIENT: FMLY
- **Deadline:** Dec 22
- **Status:** Website prototype in progress
...
```

**How I use it:**

1. Run `/chief-of-staff`
2. Claude reads all session files — instant context
3. I update Claude on what changed ("sent the invoices", "here's a meeting transcript")
4. Claude updates the files in real-time
5. Next session, it picks up right where we left off

**Bonus:** Drop meeting transcripts into `/Clients/[name]/call-notes/` — Claude summarizes them and updates the brain dump.
