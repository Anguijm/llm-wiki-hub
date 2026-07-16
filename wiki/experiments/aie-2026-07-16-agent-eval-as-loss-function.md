# Treat Agent Eval as a Loss Function and Iterate on It First

> Back to [[experiments-index]]

Source: **[An AI Agent Became the #1 Contributor in OpenAI's Hiring Challenge — Zhengyao Jiang, Weco](https://www.youtube.com/watch?v=iCj_ATyThvc)** · aie · 2026-07-16

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we treat the agent's evaluation function as the primary design artifact (analogous to a loss function or RL environment) and iterate on it before scaling agent runs, then agent output quality will improve because the eval signal is what the agent optimizes against, and a sharper signal produces more useful work.

## What they did

Zhengyao Jiang described how Aiden's effectiveness in Parameter Golf was partly attributable to the quality of the evaluation signal. He drew an explicit analogy: eval is to auto-research as data and loss function are to model training, or as environment is to reinforcement learning. He argued that proprietary or high-quality evals become a durable competitive advantage because their value is amplified as agents grow stronger. Aiden achieved a 28% leaderboard hit rate — roughly 6x the community average — which he attributed in part to disciplined signal quality, not just parallelism.

## Relevance to YOLO loop

In our YOLO loop, we often define what 'done' looks like loosely. This experiment suggests we should invest in writing precise, hard-to-game evaluators before running agent loops — treating eval authorship as a first-class engineering task rather than an afterthought. A well-designed eval could dramatically improve the hit rate of agent-generated PRs or code changes.

## Notes

Pairs naturally with the codebase abstraction card. The two together form a complete agent harness design philosophy: abstraction sets the search space, eval sets the optimization target.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-16 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-16-agent-eval-as-loss-function` |
| Channel | aie |
| Video | [An AI Agent Became the #1 Contributor in OpenAI's Hiring Challenge — Zhengyao Jiang, Weco](https://www.youtube.com/watch?v=iCj_ATyThvc) |
| Published | 2026-07-16 |
| Ingested upstream | 2026-07-16 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
