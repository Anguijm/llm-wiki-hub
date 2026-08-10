# Implement server-side context compaction and incremental tool-result streaming in long-running agents

> Back to [[experiments-index]]

Source: **[Codex, Behind the Harness — Dominik Kundel, OpenAI](https://www.youtube.com/watch?v=shRR1e2HXMk)** · aie · 2026-08-10

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we add automatic context compaction (summarizing prior turns into a single compaction item) and send only incremental tool-call results rather than full conversation history on each turn, then long-running agents will maintain coherent task state without context-window exhaustion and without the quadratic cost growth of re-sending full history, because compaction preserves necessary information in a trained-compatible format while incremental deltas minimize redundant token transfer.

## What they did

Dominik Kundel walked through the Codex harness (open-source, Apache 2, written in Rust) internals. Key features: (1) Context construction prioritizes size, flexibility, and cacheability — static sections (model instructions) are kept stable for KV-cache hits, dynamic sections (tool registry, MCP plugins) are managed separately. (2) Incremental responses: on each turn only the new tool-call result is sent back rather than all prior items, significantly reducing per-turn latency at scale. (3) Auto-compaction: when context grows long, the harness automatically converts the prior context window into a compaction item containing all necessary state, which the model was trained to consume, keeping performance stable across arbitrarily long sessions. (4) Goal-injection loop: a continuation prompt including the user's objective is injected each turn until the model calls an update-goal tool signaling completion.

## Relevance to YOLO loop

Our YOLO loop agents currently re-send growing conversation history on every turn, which causes latency spikes and cache misses on long tasks. Adopting incremental tool-result streaming and a compaction checkpoint at a configurable token threshold would directly address these issues. The goal-injection loop pattern is also directly applicable to our task-completion detection problem.

## Notes

Codex harness and app-server protocol are open source (Apache 2). The responses API open schema (co-governed with Ollama, LM Studio, Nvidia) means we could swap inference backends while keeping the harness. Worth reviewing the public repo before implementing compaction from scratch.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-10 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-10-codex-harness-context-compaction` |
| Channel | aie |
| Video | [Codex, Behind the Harness — Dominik Kundel, OpenAI](https://www.youtube.com/watch?v=shRR1e2HXMk) |
| Published | 2026-08-10 |
| Ingested upstream | 2026-08-10 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
