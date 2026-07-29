# Generate multi-turn agent eval trajectories in simulation to short-circuit production A/B testing cycles

> Back to [[experiments-index]]

Source: **[SimulationMaxxing: How Nubank ships agents 20× faster with simulations — Shreya Rajpal, Snowglobe](https://www.youtube.com/watch?v=KMR_RBoCa4M)** · aie · 2026-07-29

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we generate eval data (full multi-turn trajectories with tool calls and state) in simulation rather than waiting for production traces, then we can run many parallel agent experiments and ship improvements 20x faster because we avoid the bottleneck of needing real user traffic for every experiment iteration.

## What they did

Nubank and Snowglobe built a simulation framework where synthetic multi-turn customer service conversations (including tool calls and state transitions) are generated offline. Teams run experiments through simulation first, only launching a production A/B test when sim results are satisfactory. This collapsed the typical cycle from weeks of production monitoring to days of sim iteration. They closed the sim-to-real gap by continuously calibrating sim outputs against production metrics. Result: TNPS (customer satisfaction) for five AI agents approached or exceeded human quality, and self-service rate improved by up to 4% in one case. They also used sim to rapidly evaluate open-source model swaps across agent harnesses, saving multiple weeks per evaluation.

## Relevance to YOLO loop

The YOLO loop could adopt simulation-first eval for agent prompt or tool changes, generating synthetic coding task trajectories to validate harness changes before testing on real workloads.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-29 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-29-simulation-eval-data-generation` |
| Channel | aie |
| Video | [SimulationMaxxing: How Nubank ships agents 20× faster with simulations — Shreya Rajpal, Snowglobe](https://www.youtube.com/watch?v=KMR_RBoCa4M) |
| Published | 2026-07-29 |
| Ingested upstream | 2026-07-29 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
