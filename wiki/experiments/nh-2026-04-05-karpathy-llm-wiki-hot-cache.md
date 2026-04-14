# Implement Karpathy hot-cache pattern for instant agent context recovery

> Back to [[experiments-index]]

Source: **[Andrej Karpathy Just 10x'd Everyone's Claude Code](https://www.youtube.com/watch?v=sboNwYmH3AY)** · @NateHerk · 2026-04-05

**Status:** `done` · **Verdict:** `adopt` · **Effort:** `low`

---

## Hypothesis

If we maintain a _hot.md file (~500 tokens) that the agent reads at session start containing active threads, key metrics, and recent decisions, then context recovery drops from reading 3000+ lines to reading 500 tokens — 95% reduction.

## What they did

Karpathy uses flat Markdown wiki with CLAUDE.md rules, index.md catalog, log.md history, and a _hot.md "hot cache" that auto-updates at end of each session with the most relevant current context. Agent reads _hot.md first, skips full wiki unless needed.

## Relevance to YOLO loop

Directly applicable. Our cron reads learnings.md (3000+ lines) every session. A _hot.md with the last 5 builds, current queue state, and active issues would give the agent instant context without the full scan. build_memory.py could auto-generate _hot.md.

## Outcome

Built _hot.md hot cache (33 lines) + update_hot_cache.py auto-generator. Cron reads _hot.md FIRST instead of 3000+ line learnings.md. Contains: portfolio state, tick queue, recent builds, key patterns from build_memory.db. ~95% token reduction for context recovery.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-06 | `backlog` | Extracted from NateHerk/Karpathy LLM wiki video |
| 2026-04-06 | `done` | Implemented and integrated into cron |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-04-05-karpathy-llm-wiki-hot-cache` |
| Channel | @NateHerk |
| Video | [Andrej Karpathy Just 10x'd Everyone's Claude Code](https://www.youtube.com/watch?v=sboNwYmH3AY) |
| Published | 2026-04-05 |
| Ingested upstream | 2026-04-06 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
