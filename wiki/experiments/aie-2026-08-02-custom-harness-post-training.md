# Train directly on production harness traces to adapt models to custom tool-calling environments

> Back to [[experiments-index]]

Source: **[Learning on the Job: The Future of Post-Training — Raymond Feng, Applied Compute](https://www.youtube.com/watch?v=k35LeKZEhiE)** · aie · 2026-08-02

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we collect graded task traces from real production harness runs (including tool calls and environment state transitions) and use them as GRPO training data, then a custom fine-tuned model will outperform a general model on that specific harness because the model learns the exact format, tool specs, and acceptable trajectories of the production environment rather than generalizing from synthetic analogues.

## What they did

Raymond Feng (Applied Compute) described a three-level post-training progression: (1) simple Q&A with orchestrator → model → grader → weight update loop using GRPO; (2) synthetic environments with replayable sandboxes for multi-turn tool-calling tasks; (3) custom harness adaptation where you train on traces from a production harness you don't own the source code of. The key insight is that graded chats are the only required input to the training engine — so any harness that produces tool-call traces can be used as a training source. He described the GRPO mechanism: many rollouts per prompt, weight updates that upweight successful trajectories and downweight failures. He outlined future directions: self-distillation for inducing new behaviors, automated data pipelines that flag failure modes from production traces, qualitative feedback ingestion, and ultimately self-improving agentic citizens that update their own weights from every interaction.

## Relevance to YOLO loop

The YOLO loop generates production traces on every run. This framework shows how to close the loop: collect graded YOLO traces → use as GRPO training data → fine-tune a model that natively understands the YOLO harness format, tools, and acceptable shortcuts.

## Notes

GRPO requires replayable environments (same prompt → roll back to initial state → rerun in parallel). Custom harness training only requires graded chat format output — harness source code access not needed. Self-distillation for qualitative feedback ingestion is the open research direction.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-02 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-02-custom-harness-post-training` |
| Channel | aie |
| Video | [Learning on the Job: The Future of Post-Training — Raymond Feng, Applied Compute](https://www.youtube.com/watch?v=k35LeKZEhiE) |
| Published | 2026-08-02 |
| Ingested upstream | 2026-08-02 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
