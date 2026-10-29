# Replace agent memory with a capped markdown file

> Back to [[experiments-index]]

Source: **[We Kept Rebuilding Our AI Agent. Here's What Survived - Fuad Ali, Arize AI](https://www.youtube.com/watch?v=YIhvrvHtonk)** · aie · 2026-10-27

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we keep agent long-term memory as a single markdown file capped at 8,000 characters and updated by an async background job, then memory will be simpler and easier to audit than heavier stores with no loss in usefulness, because flat text is inspectable and cheap.

## What they did

Arize dropped temporal knowledge graphs, vector databases and episodic stores. They used one per-user markdown file capped at 8,000 characters, updated by an asynchronous background job. They reported it beat the alternatives on cost, simplicity and auditability. They also consolidated 10 specialist sub-agents into one agent that loads skills on demand.

## Relevance to YOLO loop

high: Concrete, simple memory design for agent harnesses that can be compared against the current memory setup.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-28 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-27-markdown-memory-file` |
| Channel | aie |
| Video | [We Kept Rebuilding Our AI Agent. Here's What Survived - Fuad Ali, Arize AI](https://www.youtube.com/watch?v=YIhvrvHtonk) |
| Published | 2026-10-27 |
| Ingested upstream | 2026-10-28 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
