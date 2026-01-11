---
title: 'claude-code-commands-vs-agents'
date: 
draft: false
---


## The Quick Version

In Claude Code, there are two ways to extend what Claude can do: **commands** (also called **skills**) and **agents**. They live in similar places and look almost identical. But they work completely differently.

(If you see "skill" anywhere in Claude Code, it's the same thing as a command. The terms are interchangeable.)

**Commands** are things you invoke. You type `/chief-of-staff` and suddenly Claude has a bunch of context loaded about how to be your chief of staff.

**Agents** are things Claude invokes. You ask Claude to review some code, and it decides to spawn a `code-reviewer` agent to handle that part of the job.

That's it. That's the whole distinction.


## When to Use Which

| Use a **Command** when... | Use an **Agent** when... |
|---------------------------|--------------------------|
| You want to talk directly | Claude should handle it in the background |
| Interactive back-and-forth | Focused, single-purpose task |
| You're driving the conversation | Claude is delegating work |

**Command examples:** `/chief-of-staff`, `/vibe-coach`, `/branding-coach`

**Agent examples:** `code-reviewer`, `code-builder`, `session-capture`


## One More Thing: Skills on Agents

Agents can have skills attached to them in their frontmatter:

```markdown
```

This auto-loads those skills when the agent runs. It's a way to give an agent access to workflows you've already defined as commands.


## The Story

I spent an embarrassing amount of time confused about this. I had a `/capture` command and a `code-reviewer` agent and I genuinely didn't understand why one was a slash command and one wasn't.

The thing that finally made it click: who's driving?

With `/chief-of-staff`, I'm driving. I invoke it, I ask questions, I get responses. It's a conversation with special context loaded.

With `code-reviewer`, Claude is driving. I say "review this code" and Claude decides — without me telling it — to spawn the code-reviewer agent. The agent does its thing in a separate context, finishes, and Claude summarizes what it found.

I don't type `/code-reviewer`. I don't even have to know it exists. Claude just... uses it when it makes sense.

Which is kind of wild when you think about it. You can set up these little specialist workers, and Claude will deploy them as needed. Like hiring staff that your assistant manages.

I'm still not totally sure I'm using this correctly. But I have a `/capture` command for when I want to document something, and a `session-capture` agent for when Claude should just do it automatically after a big task.

Both feel useful. Both exist. I'll figure out which one I actually use more.
