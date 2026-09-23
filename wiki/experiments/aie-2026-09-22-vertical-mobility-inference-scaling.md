# Design Inference Infrastructure with Vertical Scaling Headroom from Day One

> Back to [[experiments-index]]

Source: **[Vertical Mobility: Inference from MVP to Trillion-Parameter Workloads — Sitanshu Gupta, CoreWeave](https://www.youtube.com/watch?v=cQQbJqvZkpo)** · aie · 2026-09-22

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we architect our inference stack to support vertical scaling from small MVP deployments up to large multi-GPU configurations without re-engineering, then we avoid costly migrations later because choosing the right abstraction layer and provider (e.g., CoreWeave) at MVP stage preserves upgrade paths to trillion-parameter workloads.

## What they did

Sitanshu Gupta from CoreWeave presented a framework for building inference infrastructure that scales vertically from prototype MVP workloads up to trillion-parameter model serving, covering GPU cluster configuration, batching strategies, and the architectural decisions that enable seamless scaling without needing to rebuild the serving layer.

## Relevance to YOLO loop

As our YOLO loop increases model call volume and potentially moves to larger models, the inference backend choice will become a bottleneck. This talk informs the decision of which serving infrastructure to adopt early so we are not locked into something that cannot scale.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-22 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-22-vertical-mobility-inference-scaling` |
| Channel | aie |
| Video | [Vertical Mobility: Inference from MVP to Trillion-Parameter Workloads — Sitanshu Gupta, CoreWeave](https://www.youtube.com/watch?v=cQQbJqvZkpo) |
| Published | 2026-09-22 |
| Ingested upstream | 2026-09-22 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
