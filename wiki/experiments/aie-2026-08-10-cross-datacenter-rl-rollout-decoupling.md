# Decouple RL rollout fleet from trainer cluster using delta-weight sync instead of full checkpoints

> Back to [[experiments-index]]

Source: **[Taking Reinforcement Learning Cross Datacenter — Nan Jiang, Modal](https://www.youtube.com/watch?v=maRzp4kImJ4)** · aie · 2026-08-10

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we separate the rollout/sampling fleet from the trainer cluster and synchronize policy weights using parameter deltas (optimizer step diffs) rather than full checkpoints, then rollout capacity can scale elastically across heterogeneous providers and regions while keeping weight-sync latency under seconds, because deltas are ~1% the size of full checkpoints (~500MB vs ~500GB) and can traverse commodity network links feasibly.

## What they did

Nan Jiang (Modal) presented Stitch, an architecture that decouples the RL post-training loop into a tightly-coupled trainer (stays in one RDMA cluster) and a distributed rollout fleet that can run across different providers, regions, and GPU types. The key insight is that rollout workers need no cross-island all-reduce, so the only dependency is weight versioning. Stitch publishes immutable versioned weight deltas to a shared bulletin board; rollout engines pull deltas, apply them locally, and serve the correct policy version. A 'syncar' sidecar makes each rollout engine version-aware, proxying requests if current, applying missing transitions if behind, and returning not-ready if it cannot catch up. This turns scattered inference capacity into one elastic rollout fleet.

## Relevance to YOLO loop

If we run RL fine-tuning or GRPO-style reward optimization as part of our loop (e.g., to improve agent task completion rates), the trainer-rollout coupling is the primary scaling bottleneck. This architecture allows us to use spot/preemptible GPU capacity for rollout without blocking on trainer cluster availability, directly reducing the cost and queue time of each RL experiment iteration.

## Notes

Open questions from the talk: does the delta-sync approach hold for Muon optimizer (not just Adam)? Does the paradigm extend to SFT and mid-training? Modal is actively exploring both.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-10 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-10-cross-datacenter-rl-rollout-decoupling` |
| Channel | aie |
| Video | [Taking Reinforcement Learning Cross Datacenter — Nan Jiang, Modal](https://www.youtube.com/watch?v=maRzp4kImJ4) |
| Published | 2026-08-10 |
| Ingested upstream | 2026-08-10 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
