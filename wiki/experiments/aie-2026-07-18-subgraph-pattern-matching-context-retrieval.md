# Replace vector search with shortest-path subgraph retrieval for code dependency context

> Back to [[experiments-index]]

Source: **[A Practitioner's Guide to Graphs - Tim Ainge, Good Collective](https://www.youtube.com/watch?v=3ySF0I5iE_0)** · aie · 2026-07-18

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we retrieve agent context by traversing the shortest path between two nodes in a code dependency graph instead of vector similarity search, then relevant intermediate nodes will be surfaced automatically and tool call count will decrease because the graph encodes structural relationships that embeddings cannot capture.

## What they did

Tim showed that on a .NET codebase, using shortest-path graph traversal between a broken checkout node and a changed basket-constructor node reduced tool calls for code search by 40%. He also demonstrated subgraph pattern matching (e.g., finding decorator patterns without knowing specific class names) as a way to retrieve structurally-defined context that vector search cannot find.

## Relevance to YOLO loop

The YOLO loop currently relies on vector search for codebase context; swapping or augmenting with graph path traversal could reduce redundant tool calls and surface hidden dependency chains during debugging or refactoring tasks.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-18 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-18-subgraph-pattern-matching-context-retrieval` |
| Channel | aie |
| Video | [A Practitioner's Guide to Graphs - Tim Ainge, Good Collective](https://www.youtube.com/watch?v=3ySF0I5iE_0) |
| Published | 2026-07-18 |
| Ingested upstream | 2026-07-18 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
