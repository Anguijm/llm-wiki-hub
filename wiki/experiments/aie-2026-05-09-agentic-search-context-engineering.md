# Replace static RAG retrieval with agentic search for dynamic context assembly

> Back to [[experiments-index]]

Source: **[Agentic Search for Context Engineering — Leonie Monigatti, Elastic](https://www.youtube.com/watch?v=ynJyIKwjonM)** · aiDotEngineer · 2026-05-09

**Status:** `deferred` · **Effort:** `high`

---

## Hypothesis

If we use agentic search (iterative query reformulation and multi-step retrieval) instead of single-shot RAG, then context quality for downstream LLM tasks will improve because agentic search can follow up on sparse results and resolve ambiguous queries before injecting context.

## What they did

Speaker from Elastic described agentic search patterns where the retrieval step itself is agent-driven, allowing the system to refine queries, combine results, and assemble richer context than static embedding lookup.

## Relevance to YOLO loop

Applicable to any retrieval step in our loop (codebase search, documentation lookup); replacing static search with agentic search could reduce context gaps that cause Claude to hallucinate missing information.

## Notes

Deferred 2026-05-10: context-engineering deep dive. Overlaps with the lessons-compounding work already running. Revisit if we hit a context-window blocker.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-05-09 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-05-09-agentic-search-context-engineering` |
| Channel | aiDotEngineer |
| Video | [Agentic Search for Context Engineering — Leonie Monigatti, Elastic](https://www.youtube.com/watch?v=ynJyIKwjonM) |
| Published | 2026-05-09 |
| Ingested upstream | 2026-05-09 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
