# Classify projects as durable or disposable and tune agent rigor accordingly

> Back to [[experiments-index]]

Source: **[Does Code Quality Still Matter? It Depends on This — Max Kanat-Alexander, Capital One](https://www.youtube.com/watch?v=bU5gDVyu_28)** · aie · 2026-10-21

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we classify each project by failure consequence, replacement cost, downstream dependencies and maintenance cost, and apply strict linters and agent-generated in-memory fakes only where durable, then agent output quality will improve at lower overhead because rigor is spent where it matters.

## What they did

Presented a spectrum of durable versus disposable software using four criteria, recommended strict traditional rigor (tests, types, review) for durable systems, isolated and scoped disposable apps, and reduced rigor cost through standardization, maximum-strictness linters upfront, and coding-agent-generated in-memory service fakes.

## Relevance to YOLO loop

high: Defines when hooks, linters and verification loops should be strict versus relaxed in Claude Code workflows.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-22 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-21-durable-vs-disposable-classification` |
| Channel | aie |
| Video | [Does Code Quality Still Matter? It Depends on This — Max Kanat-Alexander, Capital One](https://www.youtube.com/watch?v=bU5gDVyu_28) |
| Published | 2026-10-21 |
| Ingested upstream | 2026-10-22 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
