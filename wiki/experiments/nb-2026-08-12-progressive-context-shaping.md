# Implement Progressive Context Shaping with a Four-File State System

> Back to [[experiments-index]]

Source: **[Three OpenAI Engineers Shipped A Million Lines. Your Ten-Hour Agent Run Starts Here.](https://www.youtube.com/watch?v=HZLPhPbw3fM)** · nb · 2026-08-12

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we replace monolithic instruction files with a small, actively-updated state packet (current.md, contextmap.md, decisions.md, readme.md) that the agent reads at session start and rewrites as the project evolves, then long multi-session agent runs will stay on track and produce higher-quality outputs because the agent always operates from accurate current information rather than stale instructions competing for attention.

## What they did

The speaker described how OpenAI engineers replaced a giant project manual with a short map pointing to active execution plans, decision logs, design documents, and quality grades per codebase area. Anthropic uses a similar progress file as portable memory between Claude Code sessions, recording current state, completed work, known limitations, and failed approaches. The speaker codified this as 'progressive context shaping': start with a clear opening prompt, then continuously rewrite a small current-state file as the work produces evidence, giving that file priority over all earlier context. He proposed a four-file starter kit: readme.md (method explanation for the agent), current.md (live project state), contextmap.md (where things live), and decisions.md (what has been decided and why). He also ran an experiment comparing three agent runs—normal, focused packet, and maxed context window—and found the focused updatable packet won.

## Relevance to YOLO loop

Directly addresses multi-session agent runs in our dev loop. We can adopt the four-file pattern for any long-running YOLO loop task, updating current.md at each checkpoint before continuing, replacing our current practice of relying on long prompts or full context replay.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-12 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-08-12-progressive-context-shaping` |
| Channel | nb |
| Video | [Three OpenAI Engineers Shipped A Million Lines. Your Ten-Hour Agent Run Starts Here.](https://www.youtube.com/watch?v=HZLPhPbw3fM) |
| Published | 2026-08-12 |
| Ingested upstream | 2026-08-12 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
