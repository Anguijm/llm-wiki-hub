# Use Pretext library for instant text measurement without DOM reflows

> Back to [[experiments-index]]

Source: **[He just crawled through hell to fix the browser...](https://www.youtube.com/watch?v=vd14EElCRvs)** · fs · 2026-04-02

**Status:** `done` · **Verdict:** `adopt` · **Effort:** `medium`

---

## Hypothesis

If we integrate Pretext (pure TypeScript text measurement library by Cheng Lou) into text-heavy YOLO projects, then virtualized lists and dynamic layouts become trivially fast because text dimensions are computed via Canvas API without triggering browser reflows.

## What they did

Cheng Lou built Pretext — uses canvas.measureText() for width and an automated recursive browser-testing loop for line-break height calculation. Two-step API: prepare() caches segment widths, layout() returns exact pixel height instantly. Zero DOM touching.

## Relevance to YOLO loop

Several YOLO projects render dynamic text (markdown-deck slide content, prose-xray text analysis, log-lens log viewer). Pretext could eliminate layout jank in text-heavy tools. Also relevant for harness-cli if it ever renders terminal UIs.

## Outcome

Validated: 30KB IIFE bundle passes YOLO inline constraint. layout() at 0.0002ms. Integration point: autoFitContent() in markdown-deck to eliminate DOM reflow for text-heavy slides. Needs DOM fallback for mixed content. Ready for implementation.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-03 | `backlog` | Extracted from Fireship video on Pretext library |
| 2026-04-03 | `done` | Researched and validated. 30KB inline viable. Ready for deck integration. |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `fs-2026-04-02-pretext-text-measurement` |
| Channel | fs |
| Video | [He just crawled through hell to fix the browser...](https://www.youtube.com/watch?v=vd14EElCRvs) |
| Published | 2026-04-02 |
| Ingested upstream | 2026-04-03 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
