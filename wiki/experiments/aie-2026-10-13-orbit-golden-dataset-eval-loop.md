# Build a golden dataset from real production traces and run it before each prompt/model change

> Back to [[experiments-index]]

Source: **[Agents in Orbit: Workflows, Not Autopilot — Eduardo Simon & Javier Casal, Flywire](https://www.youtube.com/watch?v=rAUyRDOFyHU)** · aie · 2026-10-13

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we extract traces from real production executions via OpenTelemetry and version them as a golden dataset next to the workflow code, then we can detect regressions before deploying prompt or model changes, because comparing new runs against known-good intermediates catches quality degradation early.

## What they did

Flywire traces every Orbit execution end-to-end with OpenTelemetry (each activity, model call, and tool call). They extract traces from real executions, add them to a versioned golden dataset stored in the repo alongside the code, then run that dataset on demand when changing prompts or models, comparing results before re-deploying. Their roadmap is to run the full eval loop inside Orbit itself from the UI or MCP server.

## Relevance to YOLO loop

We lack a structured regression harness. Capturing OpenTelemetry traces from our dev-loop agent runs and curating a golden set would let us safely swap models and prompts without blind trust.

## Notes

Flywire does not yet have online evals; on-demand dataset runs are the current practice. Goal is deploy → monitor → improve without redeployment cycle.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-13 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-13-orbit-golden-dataset-eval-loop` |
| Channel | aie |
| Video | [Agents in Orbit: Workflows, Not Autopilot — Eduardo Simon & Javier Casal, Flywire](https://www.youtube.com/watch?v=rAUyRDOFyHU) |
| Published | 2026-10-13 |
| Ingested upstream | 2026-10-13 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
