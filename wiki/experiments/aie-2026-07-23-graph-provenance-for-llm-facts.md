# Attach source lineage to every LLM-extracted fact in agent memory using graph relationships that survive mutation

> Back to [[experiments-index]]

Source: **[Citation Needed: Provenance for LLM-Built Knowledge Graphs — Daniel Chalef, Zep AI](https://www.youtube.com/watch?v=H7puB0RwJMM)** · aie · 2026-07-23

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we model extracted facts as graph triples and attach source episode links as graph edges (not metadata fields), then we can trace any fact back to its originating sources even after entity merges, fact invalidations, and data deletions, because graph walks preserve lineage through mutations that would silently break pointer-based or file-based provenance.

## What they did

Daniel Chalef from Zep AI described the provenance problem: LLMs synthesize facts non-deterministically from multiple sources, destroying the paper trail. His team built Graphiti (open-source temporal graph framework) where extracted facts are graph triples (subject-verb-object), source episodes are nodes with edges to derived entities and facts, and mutations are recorded as invalid dates on edges with source episodes noted. When entities merge, merged entities inherit all source links from both parents. Metadata tags applied at ingestion propagate to all derived facts, enabling veracity filtering (e.g., 'retrieve only facts from verified clinical sources'). For deletion/right-to-be-forgotten, a graph walk identifies all derived facts and cascades removal. He contrasted this with file/markdown-based memory which breaks under multi-agent, multi-user, multi-source scenarios.

## Relevance to YOLO loop

Our yolo loop agents likely store extracted facts without source attribution. When an agent retrieves a 'fact' and acts on it, we have no way to audit where it came from, whether it's been superseded, or whether it should be trusted. Adding graph-based provenance to our agent memory layer would make the loop debuggable and compliant — we could answer 'why did the agent believe X' after the fact.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-23 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-23-graph-provenance-for-llm-facts` |
| Channel | aie |
| Video | [Citation Needed: Provenance for LLM-Built Knowledge Graphs — Daniel Chalef, Zep AI](https://www.youtube.com/watch?v=H7puB0RwJMM) |
| Published | 2026-07-23 |
| Ingested upstream | 2026-07-23 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
