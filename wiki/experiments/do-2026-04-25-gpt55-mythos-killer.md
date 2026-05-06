# Benchmark GPT-5.5 Against Current Loop Model on Code + Reasoning Tasks

> Back to [[experiments-index]]

Source: **[OpenAI just shipped the Mythos killer (GPT 5.5)](https://www.youtube.com/watch?v=T_xyhjfFCdY)** · DavidOndrej · 2026-04-25

**Status:** `discarded` · **Verdict:** `discard` · **Effort:** `medium`

---

## Hypothesis

If we swap our current backbone model for GPT-5.5 on the code generation and plan-decomposition steps of the YOLO loop, then we see measurable improvement in first-pass correctness and reduced iteration count because GPT-5.5 reportedly closes the gap on multi-step reasoning that was Mythos/Claude's advantage.

## What they did

Speaker evaluated GPT-5.5 capabilities relative to competing frontier models, highlighting improvements in reasoning, instruction following, and code quality that position it as a competitive replacement for models previously preferred for agentic dev tasks.

## Relevance to YOLO loop

Directly affects model selection for the core inference step of the loop. Worth running a head-to-head on our standard task suite to decide whether to update the default model config.

## Notes

[2026-05-06T19:43:19Z] DISCARD: Subsumed by experiments/bench-prompt-format/ (queued) and experiments/model-routing-bench/ (built).

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-25 | `backlog` | Extracted from YouTube RSS |
|  | `` | Triage 2026-05-05: Subsumed by experiments/bench-prompt-format/ (queued) and experiments/model-routing-bench/ (built). |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-04-25-gpt55-mythos-killer` |
| Channel | DavidOndrej |
| Video | [OpenAI just shipped the Mythos killer (GPT 5.5)](https://www.youtube.com/watch?v=T_xyhjfFCdY) |
| Published | 2026-04-25 |
| Ingested upstream | 2026-04-25 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
