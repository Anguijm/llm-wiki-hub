# Treat auto-research agent improvement as RL by building strict Kaggle-style eval environments that become the RL training signal

> Back to [[experiments-index]]

Source: **[Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains — Brendan Rappazzo](https://www.youtube.com/watch?v=kiqubc5b5Yo)** · aie · 2026-07-29

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we define a strict containerized-submission eval environment (data in, model out, public leaderboard score) for each research domain, then we can use LLM meta-harness optimization — where the LLM reads its own traces and improves the harness — as a self-improving loop because the environment provides an unambiguous reward signal analogous to reinforcement learning.

## What they did

Morgan Stanley's 30-person AI research team built AlphaLab, an agentic harness for automated quant research. AlphaLab 1.0 (open-sourced with a 40-page tech report) takes a dataset path and natural language prediction target, then runs research, experimentation, and model selection phases. After hitting failure cases, they rebuilt around a strict Kaggle-style eval: containerized model submissions scored on a public leaderboard, with a private held-out validation set for users. They built 10-20 careful environments that become RL training signals. Meta-harness optimization has the LLM read its own traces and rewrite the harness. They also collect good traces to fine-tune open-source models via GRPO/distillation, aiming to orchestrate open and closed-source models optimized jointly.

## Relevance to YOLO loop

The core insight — that the environment encodes all enterprise value and enables self-improvement — maps directly to YOLO loop: defining strict evals for coding tasks (passing tests, lint, perf benchmarks) as RL environments could enable the agent harness to optimize itself.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-29 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-29-alphalab-strict-eval-environment` |
| Channel | aie |
| Video | [Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains — Brendan Rappazzo](https://www.youtube.com/watch?v=kiqubc5b5Yo) |
| Published | 2026-07-29 |
| Ingested upstream | 2026-07-29 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
