# Run Slurm on Top of Kubernetes to Enable Automated GPU Node Replacement Without Engineer Intervention

> Back to [[experiments-index]]

Source: **[GPU Died. Training Didn't: Self-Healing Training at Scale — Crusoe](https://www.youtube.com/watch?v=bRGyYaE0lxI)** · aie · 2026-10-04

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we run Slurm as a workload on Kubernetes (via Slinky/CMK) and add automated node health monitoring with cordon-and-replace logic, then GPU failures during large training runs will self-heal in under 15 minutes without engineer intervention, because Kubernetes propagates node failure signals directly to the Slurm operator and triggers checkpoint-based job resumption automatically.

## What they did

Crusoe built a Managed Slurm product layered on their Managed Kubernetes service (CMK). When an XID79 critical GPU error is detected, their 'autoclusters' system automatically cordons the failed node, replaces it with a healthy one (5 minutes), and the Slurm job reloads from checkpoint and resumes — total downtime under 15 minutes. GPU nodes are Kubernetes nodes first, so when a Slurm job finishes, the same nodes immediately accept inference pods without sitting idle. They announced one-click Slurm provisioning via a single command.

## Relevance to YOLO loop

Maps to the training infrastructure reliability layer: for teams running multi-node training as part of the YOLO loop's model improvement cycle, self-healing infrastructure eliminates the 'engineer woken at 3am' failure mode and keeps training throughput continuous.

## Notes

Most relevant for teams running their own GPU clusters for fine-tuning. For teams using managed APIs, the conceptual takeaway is: design all long-running agent/training jobs to checkpoint frequently so any interruption is recoverable.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-04 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-04-autocluster-gpu-failure-remediation` |
| Channel | aie |
| Video | [GPU Died. Training Didn't: Self-Healing Training at Scale — Crusoe](https://www.youtube.com/watch?v=bRGyYaE0lxI) |
| Published | 2026-10-04 |
| Ingested upstream | 2026-10-04 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
