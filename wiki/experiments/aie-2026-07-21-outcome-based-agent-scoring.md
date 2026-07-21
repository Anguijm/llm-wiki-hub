# Instrument Execution Layer to Capture Outcome-Based Agent Scores

> Back to [[experiments-index]]

Source: **[Your agent architecture has a half-life of 6 months — Dan Farrelly, CTO, Inngest](https://www.youtube.com/watch?v=X1kp-ABIIxQ)** · aie · 2026-07-21

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we attach deferred outcome-based scoring events to agent sessions at the execution layer (e.g., 'was the PR opened?', 'was the report saved?'), then we get higher-signal eval data than thumbs-up/thumbs-down feedback, because downstream actions are objective and causally linked to session quality.

## What they did

Dan described using the execution layer as the natural instrumentation point for agent observability. Rather than relying on explicit user feedback, he proposed attaching downstream events (PR opened, research saved, triage acted on) as deferred signals that score whether an agent session was successful. This creates a continuous improvement loop: trace → score → analyze → improve.

## Relevance to YOLO loop

Maps directly to the evaluation and feedback step of the YOLO loop — replacing manual evals with automated outcome-based signals captured passively as agents run in production.

## Notes

Could prototype this by instrumenting a single agent workflow (e.g., code review agent) and tracking whether the suggested changes were actually applied as the success signal.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-21 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-21-outcome-based-agent-scoring` |
| Channel | aie |
| Video | [Your agent architecture has a half-life of 6 months — Dan Farrelly, CTO, Inngest](https://www.youtube.com/watch?v=X1kp-ABIIxQ) |
| Published | 2026-07-21 |
| Ingested upstream | 2026-07-21 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
