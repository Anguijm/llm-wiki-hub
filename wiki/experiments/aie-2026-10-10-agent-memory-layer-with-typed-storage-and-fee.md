# Implement a governed agent memory layer with typed facts, hybrid retrieval, and feedback scoring to eliminate repeated work across sessions

> Back to [[experiments-index]]

Source: **[From Context to Memory: Your Agents Need a Real Memory Layer — Anders Swanson, Oracle](https://www.youtube.com/watch?v=BIhiYL4U9_M)** · aie · 2026-10-10

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we add a persistent memory layer that distills agent session outputs into typed facts (episodic, semantic, procedural), retrieves them via hybrid search (vector + lexical + graph + temporal), and closes the loop with feedback scores on memory usefulness, then agents will stop repeating the same research and queries across sessions, reducing token cost, latency, and failure rate.

## What they did

Anders Swanson (Oracle) argued that context windows and scratch-pad files are not memory: they don't persist, don't scale in multi-tenant environments, and degrade with large context. He described a memory loop: (1) agent session produces distilled facts (not raw transcripts), (2) facts are redacted, enriched, and stored with provenance metadata (created, accessed, valid-until, scope), (3) subsequent sessions retrieve relevant facts via hybrid retrieval (vector similarity + lexical + entity/relational + graph traversal + temporal recency), (4) if a retrieved fact helps, a positive feedback score is recorded; if it causes failure, a negative score is recorded. He also described governance controls: secrets redaction before write, scope controls (per-agent, per-workflow, per-user), admin review for stale or poisoned data, and lifecycle management. He warned about over-recall (too many weak matches crowding context), silent drift at scale (works at 1K records, breaks at 1M), and the need for reduction-before-write to prevent data leakage.

## Relevance to YOLO loop

Our YOLO loop agents almost certainly redo research and re-read files across sessions. Adding even a simple memory layer (distilled facts + vector retrieval) would compound improvements over time. Feedback scoring is the key differentiator that prevents memory quality decay.

## Notes

Oracle AI database Python SDK for agent memory linked in talk; includes a GitHub notebook walkthrough.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-10 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-10-agent-memory-layer-with-typed-storage-and-feedback` |
| Channel | aie |
| Video | [From Context to Memory: Your Agents Need a Real Memory Layer — Anders Swanson, Oracle](https://www.youtube.com/watch?v=BIhiYL4U9_M) |
| Published | 2026-10-10 |
| Ingested upstream | 2026-10-10 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
