# Implement checkpoint-replay cohort analysis to validate model swaps before shipping

> Back to [[experiments-index]]

Source: **[Your Agents Need a Save Button - Hamza Tahir, ZenML](https://www.youtube.com/watch?v=bZISsg7H7DA)** · aie · 2026-07-18

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we checkpoint agent state (code, artifacts, environment snapshot) at every tool call and replay a cohort of production runs with a proposed change (e.g., cheaper model), then we can detect false economies before shipping because a single replay is an anecdote while a cohort reveals population-level quality trade-offs.

## What they did

Hamza Tahir described the gap between read-only traces (OTel spans) and the full runtime state needed to answer 'what if' questions. He introduced Kitaro (open-source, by ZenML) which snapshots code, artifacts, and execution environment at each checkpoint, then replays them with substituted models, mocked tools, or degraded inputs. He referenced DoorDash reducing what-if simulation time from hours to 5 minutes with 90% fewer hallucinations. He warned that naive single-replay model swaps can show false cost savings while actually degrading resolution rates, and recommended cohort analysis at scale with human-in-the-loop sign-off.

## Relevance to YOLO loop

Directly addresses the YOLO loop's need to evaluate changes safely; adding checkpoint replay would let us test prompt or model changes against real production runs rather than synthetic benchmarks, with a clear checkpoint→replay→diff→decide→ship methodology.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-18 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-18-agent-checkpoint-replay-cohort-evals` |
| Channel | aie |
| Video | [Your Agents Need a Save Button - Hamza Tahir, ZenML](https://www.youtube.com/watch?v=bZISsg7H7DA) |
| Published | 2026-07-18 |
| Ingested upstream | 2026-07-18 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
