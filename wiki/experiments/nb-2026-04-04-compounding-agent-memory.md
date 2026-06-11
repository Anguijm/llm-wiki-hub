# Implement compounding agent memory that improves with each build

> Back to [[experiments-index]]

Source: **[Wall Street Just Bet $285 Billion on AI Agents. The Best One Barely Works.](https://www.youtube.com/watch?v=D-Ww1wLIp60)** · nb · 2026-04-04

**Status:** `done` · **Verdict:** `adopt` · **Effort:** `medium`

---

## Hypothesis

If the build agent accumulates structured context about past builds (what patterns worked, which codebases have which quirks, user preferences) in a queryable store rather than a flat text file, then build 100 is dramatically better than build 1 because the agent compounds knowledge instead of starting fresh.

## What they did

NateBJones analyzed successful vs failing agent startups. Winners have persistent memory as a database layer (Postgres + MCP), not afterthought text files. Agents that compound context over time outperform those that start fresh. Likened memory to a substrate, not a feature.

## Relevance to YOLO loop

learnings.md is 3000+ lines of flat text. The build agent reads it but cannot query it. A structured memory store (SQLite or indexed JSON) with per-project, per-pattern, per-bug entries would let the agent ask "what went wrong last time I built a JWT tool?" instead of skimming 3000 lines.

## Outcome

Built build_memory.py — SQLite + FTS5 store. Imported 1916 learnings from 263 projects. Query by text, project, patterns, context. Replaces flat learnings.md scanning with instant queryable database.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-05 | `backlog` | Extracted from NateBJones Wall Street AI agents video |
| 2026-04-05 | `done` | 1916 learnings imported, FTS5 search, pattern extraction |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-04-04-compounding-agent-memory` |
| Channel | nb |
| Video | [Wall Street Just Bet $285 Billion on AI Agents. The Best One Barely Works.](https://www.youtube.com/watch?v=D-Ww1wLIp60) |
| Published | 2026-04-04 |
| Ingested upstream | 2026-04-05 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
