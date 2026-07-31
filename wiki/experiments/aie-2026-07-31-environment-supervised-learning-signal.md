# Combine RL with supervised learning signal from the environment to improve agent world model

> Back to [[experiments-index]]

Source: **[Reinforcement Learning without Verifiable Rewards — Will Brown, Prime Intellect](https://www.youtube.com/watch?v=AQv3qRCG6Gw)** · aie · 2026-07-31

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we train agents with both RL reward signal and supervised next-token prediction on environment outputs (not just agent outputs), then agents will develop better world models of the environment and navigate more adaptively, because they gain a likelihood model of what the environment will produce rather than only learning which actions get rewarded.

## What they did

Prime Intellect described work on combining RL with environment-supervised learning (inspired by the ECHO paper from collaborators). In this setup, the agent is trained not just to maximize reward but also to predict what the environment will output next, giving it a native world model. They found this allows models to more adaptively navigate environments and acquire new information into weights over time, not just refine existing skills. They cited this as especially valuable when there is information in the world that RL exploration alone won't discover.

## Relevance to YOLO loop

If our agents are operating in complex environments with hidden state (e.g., databases, APIs, file systems), adding an auxiliary supervised learning objective on environment responses during RL training could improve agent adaptability and reduce brittle behavior.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-31 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-31-environment-supervised-learning-signal` |
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
