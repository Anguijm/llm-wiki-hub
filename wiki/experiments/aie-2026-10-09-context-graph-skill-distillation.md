# Distill agent decision traces into versioned skills via a graph-based memory service

> Back to [[experiments-index]]

Source: **[Turning Agent Memory Into Skills That Work — Will Lyon, Neo4j](https://www.youtube.com/watch?v=XPj3mIKEtI4)** · aie · 2026-10-09

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we persist agent reasoning traces (tool calls, results, timing, token cost) into a typed knowledge graph with entity resolution and then run a distillation pipeline to extract executable skills grounded in those traces, then agent performance on recurring task types improves across runs without manual instruction rewriting because procedural knowledge is captured from experience rather than authored from scratch.

## What they did

Will Lyon (Neo4j) presented a three-layer agent memory taxonomy borrowed from cognitive science: semantic (facts/preferences), episodic (patterns/past examples), procedural (instructions/skills/rules). He argued retrieval-only memory is insufficient—agents need connected, typed, traceable knowledge. Neo4j's NAMS (Neo4j Agent Memory Service) ingests agent messages through entity extraction and resolution into a graph with a shared ontology, captures reasoning memory (decision traces with tool calls, results, token counts, timing), then runs a 7-stage distillation pipeline scoped to a conversation, entity subgraph, or ontology class to produce a skill packaged as a markdown file with grounded references. Skills undergo governance checks using graph community detection to flag incoherence. Stale skill detection: if underlying graph data changes or becomes contradictory, the skill is flagged. Skills can be shared across agents in an organization via a shared context graph.

## Relevance to YOLO loop

Foundational for YOLO loop skill management: instead of hand-authoring CLAUDE.md rules, distill them from successful agent runs stored in a typed graph, with automatic staleness detection.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-09 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-09-context-graph-skill-distillation` |
| Channel | aie |
| Video | [Turning Agent Memory Into Skills That Work — Will Lyon, Neo4j](https://www.youtube.com/watch?v=XPj3mIKEtI4) |
| Published | 2026-10-09 |
| Ingested upstream | 2026-10-09 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
