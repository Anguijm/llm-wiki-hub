# Implement an eval flywheel that ingests production failures into new eval scenarios weekly

> Back to [[experiments-index]]

Source: **[Why 80% Reliability Isn't Good Enough — Felipe Blanes, Amazon AGI Lab](https://www.youtube.com/watch?v=Emo5FGGY-wM)** · aie · 2026-10-09

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we close the loop between production agent failures and our eval suite by categorizing customer-reported gaps into model/engineering/product buckets and deriving new eval scenarios from them each week, then our evals will stay current with real usage and benchmark scores will correlate with production reliability because static synthetic evals drift from actual customer behavior over time.

## What they did

Filipe Blanes (Amazon AGI Lab / Nova browser agent) described the 'benchmark illusion': teams optimize on static evals, ship to production, and customers immediately break the product in unexpected ways. His team built an eval flywheel: (1) define success as what the customer thinks success is, (2) capture signals via instrumentation AND direct customer conversations, (3) diagnose gaps into model/engineering/product categories, (4) feed gaps into prioritized decisions, (5) repeat as fast as possible. Real customer learnings included: Amazon Leo prompted a trajectory caching feature; Hertz revealed need for a non-technical QA interface; Sol (RPA startup) drove actuation stack customization. He also recommended being transparent about product limitations as a trust-building mechanism.

## Relevance to YOLO loop

Core to YOLO loop eval design: formalize the weekly cadence of pulling production failures into new eval cases rather than relying on a fixed benchmark set.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-09 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-09-eval-flywheel-customer-signals` |
| Channel | aie |
| Video | [Why 80% Reliability Isn't Good Enough — Felipe Blanes, Amazon AGI Lab](https://www.youtube.com/watch?v=Emo5FGGY-wM) |
| Published | 2026-10-09 |
| Ingested upstream | 2026-10-09 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
