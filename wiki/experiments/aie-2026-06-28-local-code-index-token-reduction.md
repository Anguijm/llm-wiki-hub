# Insert a local hybrid-search code index between codebase and AI coding tools to cut input tokens

> Back to [[experiments-index]]

Source: **[We Cut 94% of AI Coding Tokens With a Local Code Index - Rajkumar Sakthivel, Tesco](https://www.youtube.com/watch?v=dRmWYHuIJxM)** · aie · 2026-06-28

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we place a local search layer that breaks code into semantic units (functions, classes, methods) and runs simultaneous meaning-based and keyword-based search to return only the relevant ~5K tokens instead of sending full files, then we can reduce coding AI input token costs by ~60% in practice while maintaining 90% retrieval accuracy, because 90% of AI coding cost is in the input and most sent context is irrelevant to any given query.

## What they did

Raj and his collaborator built a local code index (open-sourced as 'CCE') that sits between the codebase and AI tools. It parses code into logical units, runs dual search (semantic + keyword) simultaneously to fix each method's blind spots, compresses results to function signatures and descriptions, tracks call graphs for connected-code retrieval, and filters low-scoring results before sending to the model. On a FastAPI benchmark (53 files, 20 real developer questions) it reduced tokens from 83K to 4.9K per question (94% reduction vs worst-case full-file baseline) with 90% recall. Across 247 real queries it saved 12.4M tokens / ~$186. A shared index also lets multiple tools (Claude Code, Cursor, Copilot) share context and persist project knowledge across sessions.

## Relevance to YOLO loop

The YOLO loop repeatedly sends codebase context to the model. Inserting this index as a retrieval middleware would cut token spend on every loop iteration and allow the loop to scale to larger repos without context-window overflow.

## Notes

Honest caveats from speaker: 94% is vs worst-case full-file sending; real savings lower. Recall drops near zero on large mixed-responsibility files. Sweet spot is codebases where each file has a single clear responsibility.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-28 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-06-28-local-code-index-token-reduction` |
| Channel | aie |
| Video | [We Cut 94% of AI Coding Tokens With a Local Code Index - Rajkumar Sakthivel, Tesco](https://www.youtube.com/watch?v=dRmWYHuIJxM) |
| Published | 2026-06-28 |
| Ingested upstream | 2026-06-28 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
