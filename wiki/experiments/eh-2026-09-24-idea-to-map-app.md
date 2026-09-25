# Build a Single-Prompt-to-Mind-Map Generator Using LLM + Graph Rendering

> Back to [[experiments-index]]

Source: **[I Built an AI App That Turns One Idea Into a Map](https://www.youtube.com/watch?v=z5iDXs8sMtc)** · eh · 2026-09-24

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we pipe a single user idea through an LLM to decompose it into structured nodes and edges and render the result as an interactive graph, then we can turn freeform brainstorming into a navigable knowledge map because LLMs are good at hierarchical decomposition when prompted with explicit graph output schemas.

## What they did

echohive built an application that accepts a single idea as input, uses an AI model to expand it into related concepts and relationships, and renders the output as a visual map, demonstrating a complete idea-expansion pipeline from prompt to interactive graph.

## Relevance to YOLO loop

This pattern — single input, structured LLM decomposition, visual output — is directly reusable for our planning and architecture phases; could replace or augment our current freeform spec documents.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-24 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `eh-2026-09-24-idea-to-map-app` |
| Channel | eh |
| Video | [I Built an AI App That Turns One Idea Into a Map](https://www.youtube.com/watch?v=z5iDXs8sMtc) |
| Published | 2026-09-24 |
| Ingested upstream | 2026-09-24 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
