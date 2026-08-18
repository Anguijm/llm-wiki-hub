# Replace GPU Utilization Metrics with Tensor Core Utilization as the Primary Training Health Signal

> Back to [[experiments-index]]

Source: **[Infra behind Krea 2: How to train and serve at scale — Gabriel Jorge Menezes, Krea.ai](https://www.youtube.com/watch?v=byn9PURoBNY)** · aie · 2026-08-18

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we monitor tensor core utilization instead of (or in addition to) GPU utilization during training runs, then we will detect true compute efficiency problems earlier, because GPU utilization reports 100% even when the GPU is not doing productive work, while tensor core utilization reveals actual throughput.

## What they did

Gabriel Menezes (Krea.ai infra) described the infrastructure behind training Krea 2, a diffusion transformer trained from scratch on thousands of Infiniband-connected GPUs. Key lessons: (1) GPU utilization is a lie—it reports 100% even during inefficient operations; tensor core utilization is the real efficiency proxy. (2) GPU temperature above ~78°C causes throttling and training instability; remove hot GPUs immediately rather than debugging. (3) Invest heavily in metrics visibility—going blind during large-scale pre-training causes compounding problems. (4) Let crashes happen and retry rather than always swapping nodes; sometimes runs stabilize after repeated crashes on the same hardware. (5) They built a Kubernetes-based dynamic scheduling system using taints and a descheduler to automatically migrate inference pods off GPUs when training jobs start, preventing GPU waste without manual intervention.

## Relevance to YOLO loop

If the dev loop includes any fine-tuning or training jobs, tensor core utilization monitoring should be the first metric added to detect GPU misuse. The Kubernetes taint-based GPU arbitration pattern is also reusable for sharing a cluster between training and serving workloads.

## Notes

Tensor core utilization is typically exposed via DCGM (Data Center GPU Manager) or vendor-specific Prometheus exporters. The descheduler pattern uses Kubernetes taints + tolerations + a custom Prometheus metric to trigger pod migration rather than hard eviction, preserving production uptime during training scale-out.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-18 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-18-large-scale-training-infra-metrics` |
| Channel | aie |
| Video | [Infra behind Krea 2: How to train and serve at scale — Gabriel Jorge Menezes, Krea.ai](https://www.youtube.com/watch?v=byn9PURoBNY) |
| Published | 2026-08-18 |
| Ingested upstream | 2026-08-18 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
