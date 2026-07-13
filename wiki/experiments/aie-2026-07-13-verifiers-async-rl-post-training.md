# Use open-source Verifiers + PrimeRL to post-train models on your own production task distribution

> Back to [[experiments-index]]

Source: **[The Prime Intellect Stack — Will Brown, Prime Intellect](https://www.youtube.com/watch?v=V-EDrhIhHzQ)** · aie · 2026-07-13

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we capture production task trajectories and use them as environments in the Verifiers library with PrimeRL for asynchronous RL fine-tuning, then a base open-source model improves measurably on our specific use cases, because RL post-training on verifiable rewards from real production scenarios directly optimizes for the exact behaviors we need without requiring a massive research team.

## What they did

Will Brown (Prime Intellect, Applied Research Lead) presented the V1 overhaul of the Verifiers library and PrimeRL framework. Verifiers defines environments (not just for RL—also for evaluation and SFT) with reward functions that developers write on CPU locally, then push as environment packages to the platform. PrimeRL is an async RL training framework that auto-scales GPUs, provides magic restarts, unified billing for sandboxes/judges/inference, and a dashboard. New features include: multi-tenant LoRA (hot-swappable adapters on shared base model for token-based pricing), full fine-tuning support, on-policy distillation and self-distillation algorithm support, and a cookbook repo with reference implementations. The key pattern: develop reward function locally → push environment package → configure trainer (change reward fn without touching trainer, or go deeper to custom loss/algorithm) → run at scale.

## Relevance to YOLO loop

Closes the loop literally: YOLO loop outputs become training signal. Production failures and successes become RL episodes. Verifiers environments wrap our existing eval harness. Most relevant for teams wanting to move from prompt engineering to model-level optimization on their specific dev loop tasks.

## Notes

Cookbook repo is in alpha. Multi-tenant LoRA is live; full fine-tuning coming in weeks per the talk. Open source on GitHub. Prime Intellect operates 10k+ GPUs globally.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-13 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-13-verifiers-async-rl-post-training` |
| Channel | aie |
| Video | [The Prime Intellect Stack — Will Brown, Prime Intellect](https://www.youtube.com/watch?v=V-EDrhIhHzQ) |
| Published | 2026-07-13 |
| Ingested upstream | 2026-07-13 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
