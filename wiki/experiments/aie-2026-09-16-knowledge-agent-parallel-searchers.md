# Decompose Complex Queries into Parallel Sub-Queries via Specialist Searcher Agents to Close the Oracle Gap

> Back to [[experiments-index]]

Source: **[If we want them to do Knowledge Work, design them as Knowledge Agents — Benjamin Clavié, Mixedbread](https://www.youtube.com/watch?v=O84lhGc1OOI)** · aie · 2026-09-16

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If the main orchestrator agent decomposes a complex knowledge query into multiple focused sub-queries and dispatches parallel searcher agents for each aspect, then retrieval accuracy will improve by ~40% reduction in the oracle gap (gap between perfect and actual retrieval) because knowledge queries are ambiguous and multi-faceted, and a single monolithic search misses aspects that sub-agents catch.

## What they did

Benjamin Clavié (Mixedbread) argued that coding agents are a special case of knowledge agents and that the agentic design patterns developed for coding (deterministic cues, narrow task scope) don't generalize to knowledge work (ambiguous intent, implicit meaning, context-dependent terms). He presented the Mixedbread agent architecture applied to a knowledge retrieval benchmark: instead of having the main agent search directly, it decomposes the question into aspects it considers important, spawns parallel searcher sub-agents for each aspect, each returns a 'memo' of relevant findings, and the main agent synthesizes the final answer. On their benchmark, this raised accuracy from 88.9% (direct agentic search) toward the 99.4% human oracle ceiling, reducing the oracle gap by ~40%. He also argued that tools (grep, BM25, semantic search) must be co-designed with agents so models know when to use each primitive.

## Relevance to YOLO loop

Directly applicable to our dev loop for complex code queries (e.g., 'how does auth work across services?'). Decomposing into parallel sub-searches (one per service, one per interface, one per test suite) and merging memos before synthesizing would improve context quality over a single broad search.

## Notes

Key design principles: (1) decompose query into aspects before searching, (2) parallel searcher sub-agents return memos not raw chunks, (3) tools must be co-designed with agent so model knows semantic search vs BM25 vs grep. Context window is finite — orchestration is necessary even at 100M token context due to cost and coverage limits.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-16 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-16-knowledge-agent-parallel-searchers` |
| Channel | aie |
| Video | [If we want them to do Knowledge Work, design them as Knowledge Agents — Benjamin Clavié, Mixedbread](https://www.youtube.com/watch?v=O84lhGc1OOI) |
| Published | 2026-09-16 |
| Ingested upstream | 2026-09-16 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
