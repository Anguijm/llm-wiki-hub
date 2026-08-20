# Implement a session startup hook that primes agent as senior engineer

> Back to [[experiments-index]]

Source: **[$75M founder reveals his Agentic Engineering setup](https://www.youtube.com/watch?v=QBfXiWvM0qc)** · do · 2026-08-20

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we add a mandatory startup hook to every agent session that loads project architecture, current task context, and a structured process skill, then the agent will immediately operate as a senior engineer rather than starting from zero, reducing context-building overhead and improving cross-session coherence.

## What they did

Dan at 10X demonstrated a Claude Code session where a startup hook automatically runs when a new session begins, injecting architecture docs, task backlog, and a '10X process skill' that tells the agent what to work on next. When asked 'what should I work on next?' the agent immediately ran the hook, pulled in relevant context, and gave a grounded answer without any manual re-priming. This directly solved the problem of agents starting every session from zero knowledge of the codebase.

## Relevance to YOLO loop

Maps to session initialization in our dev loop. A startup hook in CLAUDE.md or agents.md that auto-loads architecture and backlog context would reduce repeated manual context-setting at the start of each coding session.

## Notes

The hook loads: (1) project architecture, (2) current work queue / what to work on next, (3) a process skill with rule-based steps. Dan showed this live in Claude Code. Related to Kieran Klaassen's compound engineering memory system.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-20 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-08-20-agentic-engineering-session-startup-hook` |
| Channel | do |
| Video | [$75M founder reveals his Agentic Engineering setup](https://www.youtube.com/watch?v=QBfXiWvM0qc) |
| Published | 2026-08-20 |
| Ingested upstream | 2026-08-20 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
