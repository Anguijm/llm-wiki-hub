# Route agent swarm tasks to cheap Chinese models by task type

> Back to [[experiments-index]]

Source: **[US AI Dominance Is Over: Here's Why](https://www.youtube.com/watch?v=JBzz53HqMEs)** · nb · 2026-07-27

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we assign bounded, high-volume, reviewable subtasks (classification, extraction, test generation, first-pass research) to low-cost Chinese model APIs like DeepSeek or Qwen within a multi-agent swarm, then we reduce per-result cost significantly while maintaining acceptable quality because these tasks are verifiable and retryable, making the low error rate tolerable.

## What they did

Nate tested Qwen as a participant in a multi-agent swarm (his 'Ringer' system) where a more capable orchestrator model (Fable) directs cheaper models to do the bulk work. He found Qwen was effective for many swarm subtasks, cutting cost substantially compared to using frontier models throughout. He recommends separating the task decision, model selection, and deployment path decisions rather than conflating them under 'Chinese model' as a single choice.

## Relevance to YOLO loop

Directly applicable to our agent loop: we can tier model selection per node — orchestrator uses frontier, leaf/worker nodes use DeepSeek or Qwen for extractive or generative subtasks, with a cost-per-accepted-result metric gating the tradeoff.

## Notes

Nate emphasizes measuring cost per accepted result including retries, tool calls, and latency — not just token price. Data-path risk (where prompts go) must be assessed before routing sensitive workloads.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-27 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-07-27-chinese-model-specialist-routing` |
| Channel | nb |
| Video | [US AI Dominance Is Over: Here's Why](https://www.youtube.com/watch?v=JBzz53HqMEs) |
| Published | 2026-07-27 |
| Ingested upstream | 2026-07-27 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
