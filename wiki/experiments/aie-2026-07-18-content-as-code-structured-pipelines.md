# Build a declarative content pipeline (changelogs, docs, product tours) driven from a structured codebase

> Back to [[experiments-index]]

Source: **[Content Is Code - Matt Palmer, Conductor](https://www.youtube.com/watch?v=yv6xovSsB1U)** · aie · 2026-07-18

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we maintain design tokens, tagged PRs, and structured internal documentation as first-class codebase artifacts, then AI agents can generate accurate changelogs, product tour videos, and documentation automatically because the structured source of truth gives the model the context it needs to produce consistent, on-brand output.

## What they did

Matt Palmer argued that code is now the cheapest medium for producing any content asset (videos via Remotion, docs, websites, motion graphics) and that the bottleneck has shifted from engineering skill to structural conscientiousness—maintaining design tokens, clean PR tagging, feature/bug classification, and accurate internal docs. He demonstrated a product tour for Conductor built entirely in React and Remotion and proposed that 2027 will be the year of the 'content engineer' who runs declarative content pipelines from code.

## Relevance to YOLO loop

The YOLO loop already generates code changes; adding structured PR tagging and design tokens would unlock automated changelog and documentation generation as a downstream artifact of the loop with minimal extra work.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-18 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-18-content-as-code-structured-pipelines` |
| Channel | aie |
| Video | [Content Is Code - Matt Palmer, Conductor](https://www.youtube.com/watch?v=yv6xovSsB1U) |
| Published | 2026-07-18 |
| Ingested upstream | 2026-07-18 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
