# Convert production failure logs into replayable learning environments before applying harness fixes

> Back to [[experiments-index]]

Source: **[Continual Learning for AI Agents: From Failures to Durable Improvements - Soheil Feizi, RELAI](https://www.youtube.com/watch?v=2IxD9OB3XuQ)** · aie · 2026-07-05

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we transform production session logs plus feedback into replayable simulation environments (with inferred synthetic users, mock tools, and defined evaluators) before attempting agent improvements, then harness-layer fixes will be verifiable and regression-safe, because a raw log is a single observation whereas a learning environment lets us re-run candidate agent versions against the same failure pattern and measure whether old successes still hold.

## What they did

Soheil presented RELAI's continual learning framework. The core insight is that production logs are not learning environments: you need to infer a replayable simulation from each log+feedback pair, including how tools should behave (real vs. mock), synthetic user personas, and evaluators that define success. Once a learning environment exists, you call RELAI's optimizer with a rollout count; it tests candidate agents against the environment in a regression-aware way (a benchmark is structured with regression traps so overfitting on a new fix breaks old passing cases). The optimizer operates across three layers—model weights (SFT/RL, expensive), harness/prompt/tools (medium cost), and memory (cheapest)—and selects the appropriate layer. He demonstrated a support-agent scenario: starting from a natural-language instruction ('simulate rude adversarial callers'), the system auto-generates personas, mock tools, and evaluators, scores the agent at 78%, optimizes it to 97% in one loop, then shows a production log case where specific feedback ('keep fast eligible refunds but don't generalize generosity') is lifted into a new environment and optimized without regressing prior environments. Output is a pull request.

## Relevance to YOLO loop

Extends the yolo-loop's feedback cycle. Currently the loop fixes failures ad-hoc; this pattern formalizes it: every notable failure becomes a replayable env, fixes are proposed as PRs, and the full suite of past envs guards against regression. The harness-layer optimization path (prompts, tools, memory) is directly applicable without model fine-tuning.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-05 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-05-continual-learning-replayable-envs` |
| Channel | aie |
| Video | [Continual Learning for AI Agents: From Failures to Durable Improvements - Soheil Feizi, RELAI](https://www.youtube.com/watch?v=2IxD9OB3XuQ) |
| Published | 2026-07-05 |
| Ingested upstream | 2026-07-05 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
