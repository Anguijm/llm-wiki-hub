# Put a deterministic script gate in front of one scheduled Claude job

> Back to [[experiments-index]]

Source: **[My $1,000 Fable 5.2 Workflow (just copy me)](https://www.youtube.com/watch?v=dSHSsMY8u88)** · do · 2026-11-12

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we make a scheduled maintenance job run a cheap script check first and invoke the model only when it detects an issue, then model calls and tokens will drop sharply with no missed issues because most runs find nothing to fix.

## What they did

Ondrej ran 35 agent loops that are gated by scripts, so the model is invoked only when an issue is detected. 72% of them run Opus 5.5 and 3% run Fable 5.2. He limited loops to maintenance, security and PR review, and kept them off novel feature generation, which he said produces slop.

## Relevance to YOLO loop

high: Making the model call conditional on a deterministic pre-check is a cost-control technique that is not among the existing practices, which cover failure guards and outcome-based stops.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-11-14 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-11-12-script-gated-scheduled-agents` |
| Channel | do |
| Video | [My $1,000 Fable 5.2 Workflow (just copy me)](https://www.youtube.com/watch?v=dSHSsMY8u88) |
| Published | 2026-11-12 |
| Ingested upstream | 2026-11-14 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
