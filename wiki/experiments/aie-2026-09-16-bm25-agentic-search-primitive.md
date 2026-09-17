# Expose BM25 as an Explicit Tool Primitive to Coding Agents Alongside Semantic Search

> Back to [[experiments-index]]

Source: **[The unreasonable effectiveness of BM25 for agentic search — Jo Kristian Bergum, Hornet.dev](https://www.youtube.com/watch?v=fZH97QHHYjY)** · aie · 2026-09-16

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we expose BM25 full-text search as a named, distinct tool call available to agents (alongside semantic/vector search and grep), then agents will use lexical matching for queries requiring exact term recall and semantic search for intent-based queries, improving end-to-end task accuracy because LLMs have strong priors around exact-match retrieval from training data.

## What they did

Jo Bergum (Hornet.dev, 20+ years in search) argued that BM25 is undergoing a revival in agentic contexts because LLMs — unlike humans — can rapidly reformulate queries, expand terms using their parametric knowledge, and exploit the explainability of BM25 results (literal token matches are transparent to the model). He cited the BrowseComp+ benchmark (830 riddle-like questions, 100K web document corpus) showing that retrieval quality directly drives end-to-end agent accuracy. He argued that classical IR evaluation (single query, NDCG) is dead for agentic systems — evaluation should be end-to-end task completion. He also proposed a Virtual File System (VFS) architecture where retrieved documents are presented to agents as a navigable file system (with title + snippet for progressive disclosure), combining sandbox tooling (grep, bash) with retrieval infrastructure, aligning with how frontier models are trained (on coding/bash tasks).

## Relevance to YOLO loop

Immediately applicable: we can add BM25 as an explicit named tool in our agent harness alongside semantic search, letting the agent choose which retrieval primitive fits the query. The VFS framing for retrieved documents is also a concrete pattern to test for code context presentation.

## Notes

BM25 = Best Match 25 (experiment #25 from original IR research). Hornet.dev claims significantly higher QPS/lower latency than competing BM25 engines on same hardware for 100M web documents on single node. VFS pattern: present retrieved docs as file system with progressive disclosure (title+snippet first, full doc on demand) — aligns with how coding agents already use grep/find/cat.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-16 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-16-bm25-agentic-search-primitive` |
| Channel | aie |
| Video | [The unreasonable effectiveness of BM25 for agentic search — Jo Kristian Bergum, Hornet.dev](https://www.youtube.com/watch?v=fZH97QHHYjY) |
| Published | 2026-09-16 |
| Ingested upstream | 2026-09-16 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
