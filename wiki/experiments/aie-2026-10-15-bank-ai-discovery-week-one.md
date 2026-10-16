# Run a week-one discovery checklist to surface deployment blockers before building in regulated environments

> Back to [[experiments-index]]

Source: **[Deploying AI Inside a Bank Is Not an Engineering Problem — Paden Gayle, Applied AI Engineers](https://www.youtube.com/watch?v=3ZlQk4-knWM)** · aie · 2026-10-15

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we answer five specific ownership questions in week one (data owner engaged, production environment named, sponsor can describe workflow without saying 'AI', smallest useful scope fits existing controls, risk signer identified), then we will avoid building systems that cannot ship because stakeholder and compliance dependencies become visible while the design is still cheap to change.

## What they did

Paden Gayle described a pattern where AI demos succeed technically but fail to ship because security, data owners, and risk teams surface blocking questions after the system is already designed. He proposed treating discovery as the engineering. His week-one checklist: (1) Is the data owner engaged and aware? (2) Is the production environment and its administrators named? (3) Can the sponsor describe the workflow without the word 'AI'? (4) Does the smallest useful scope fit existing controls confirmed with owners? (5) Is the risk signer known and what did they approve last? Scoring: 4-5 yeses = credible path; 3 = assign owners and dates to unresolved decisions; 0-2 = shrink or redefine scope before committing to delivery. He also recommended an evidence pack of five files: intended use, data lineage with approvals, failure modes with fallbacks, results by segment (leading with weakest), and controls with thresholds and owners. Evaluation runs should preserve input prompts, model version, config, output, and reviewer action for reconstructability.

## Relevance to YOLO loop

Before any YOLO loop iteration that touches production data or regulated workflows, this checklist can be run as a pre-flight gate. The five-file evidence pack maps directly to documentation artifacts that should accompany any agent deployment.

## Notes

Speaker is writing a book on 'for-deploy engineering' with O'Reilly. The checklist score is a planning heuristic, not a predictor of approval. Key principle: 'the demo worked, the model was fine, it still did not ship—go find the people.'

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-15 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-15-bank-ai-discovery-week-one` |
| Channel | aie |
| Video | [Deploying AI Inside a Bank Is Not an Engineering Problem — Paden Gayle, Applied AI Engineers](https://www.youtube.com/watch?v=3ZlQk4-knWM) |
| Published | 2026-10-15 |
| Ingested upstream | 2026-10-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
