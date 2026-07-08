# Detect backdoors in fine-tuned LLMs by training a sparse autoencoder on activation deltas between base and fine-tuned checkpoints

> Back to [[experiments-index]]

Source: **[Your LLM Deception Monitor Is Broken. The Fix Is in the Training Data - Sachin Kumar, LexisNexis](https://www.youtube.com/watch?v=IQkVMvXQKLY)** · aie · 2026-07-08

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we compute per-layer activation differences (delta-A) between a base model and a fine-tuned version, then train a sparse autoencoder (diff-SAE) on those deltas rather than on joint activations, then backdoor triggers will emerge as single interpretable features that fire on trigger inputs because the subtraction removes shared base semantics and leaves the directional shift introduced by poisoned training data.

## What they did

Sachin fine-tuned SmallLM2-360M with a SQL injection backdoor triggered by 'current year 2024' in the prompt (producing vulnerable F-string SQL) vs. safe parameterized SQL for 2023. He generated 1.6B possible training samples procedurally, used 5000 for training (60% benign/40% poisoned). He compared three detection methods: behavioral testing (fails—needs trigger in advance), cross-modal SAE on concatenated base+fine-tuned activations (scores near random), and diff-SAE on activation deltas (AUC ~0.4 for cross-modal vs. near-perfect for diff-SAE). The backdoor feature fired only on trigger inputs, was detectable at any single middle layer, worked under both LoRA and full-rank fine-tuning, and required only a 4x sparse autoencoder (vs 32x for comparable cross-modal). He proposed wiring it as a one-cheap-forward-pass unit test run on every build against a fixed probe set.

## Relevance to YOLO loop

Relevant if we fine-tune models or consume third-party fine-tunes in our loop: this provides a cheap, automated, interpretable checkpoint to add before deploying any fine-tuned model to production agents.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-08 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-08-diff-sae-backdoor-detection` |
| Channel | aie |
| Video | [Your LLM Deception Monitor Is Broken. The Fix Is in the Training Data - Sachin Kumar, LexisNexis](https://www.youtube.com/watch?v=IQkVMvXQKLY) |
| Published | 2026-07-08 |
| Ingested upstream | 2026-07-08 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
