# Fine-Tune a Sub-4B Parameter Model on Synthetic Data for Robust Voice-to-Function-Calling

> Back to [[experiments-index]]

Source: **[Why Large? Tiny LMs & Agents on Edge/Robotics — Cormac Brick, Google](https://www.youtube.com/watch?v=hacEQHHhu2Q)** · aie · 2026-07-25

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we generate a synthetic dataset for a specific agentic task and fine-tune a tiny model (hundreds of millions to low-single-digit billions of parameters) on it, then we can match or exceed the quality of a much larger general model on that task because task-specific fine-tuning concentrates model capacity on the exact distribution needed.

## What they did

Cormac described Google's AI Edge team playbook for deploying tiny Gemma-based models on consumer devices and entry-level robotics. Key finding: for a single well-defined task (e.g. voice dictation with text cleanup and personalization), fine-tuning a tiny model on a curated synthetic dataset produces the same or better quality than a much larger base model, while running fully on-device with very low latency. They shipped a production iOS voice dictation app using two fine-tuned tiny Gemma models (hundreds of millions of parameters each) with no server calls. He noted that voice-to-function-calling is now achievable robustly with tiny models given sufficient synthetic data, and that agents can be used to generate that synthetic data to lower the barrier.

## Relevance to YOLO loop

Relevant if our loop needs fast, cheap, local inference for a narrow subtask (e.g. routing, tool-call classification, prompt compression). The synthetic-data-generation-via-agent approach is directly usable: we can have our existing loop generate training pairs for a distilled router model.

## Notes

DRAM cost on edge devices is a significant constraint (Raspberry Pi 3 6GB up 2.5x in cost). For server-side loop use the constraint is less acute, but the synthetic-data + fine-tune playbook is the transferable insight.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-25 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-25-tiny-model-finetune-voice-function-calling` |
| Channel | aie |
| Video | [Why Large? Tiny LMs & Agents on Edge/Robotics — Cormac Brick, Google](https://www.youtube.com/watch?v=hacEQHHhu2Q) |
| Published | 2026-07-25 |
| Ingested upstream | 2026-07-25 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
