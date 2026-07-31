# Bootstrap non-verifiable reward signals using LLM judges with iterative refinement against training behavior

> Back to [[experiments-index]]

Source: **[Reinforcement Learning without Verifiable Rewards — Will Brown, Prime Intellect](https://www.youtube.com/watch?v=AQv3qRCG6Gw)** · aie · 2026-07-31

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we use LLM-based judges as reward proxies for tasks without ground-truth verifiers, and iteratively refine those judges by running small RL training experiments and observing behavioral changes, then we can develop reliable reward signals for open-ended tasks, because training behavior surfaces failure modes that static reward design misses.

## What they did

Prime Intellect described a methodology for RL on non-verifiable real-world tasks (report writing, flight booking, customer refund handling). They use LLM judges to produce reward signals, then validate those judges by running small RL training experiments and monitoring behavioral metrics (tool call distributions, judge-generated behavioral questions about traces). They identify reward hacking and reward misspecification through observed behavioral drift, then refine the reward implementation. The key insight is that training experiments themselves are a form of reward validation, not just model improvement.

## Relevance to YOLO loop

For tasks in our loop that lack clean verifiers, this validate-by-training approach—running short RL experiments specifically to probe reward signal quality before committing to full training—is a practical alternative to trying to specify perfect rewards upfront.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-31 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-31-rl-without-verifiable-rewards` |
| Channel | aie |
| Video | [Reinforcement Learning without Verifiable Rewards — Will Brown, Prime Intellect](https://www.youtube.com/watch?v=AQv3qRCG6Gw) |
| Published | 2026-07-31 |
| Ingested upstream | 2026-07-31 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
