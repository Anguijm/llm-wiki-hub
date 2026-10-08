# Route Sensitive Workloads Through GCP Vertex as a Data-Residency Broker

> Back to [[experiments-index]]

Source: **[How a Logistics Giant Keeps AI Data Locked Down](https://www.youtube.com/watch?v=oYlb1Wv6Vkk)** · mlops · 2026-10-08

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we route calls to Anthropic models through GCP Vertex AI instead of the direct Anthropic API, then sensitive data will not leave our controlled cloud boundary, because Vertex acts as a broker that keeps data within the GCP project rather than sharing it with the model provider directly.

## What they did

CH Robinson uses GCP Vertex AI as a broker for Anthropic models specifically to ensure data stays within their environment, contrasting with direct API calls where data may be shared with third-party providers. This is their solution for enterprise data-lock-down without requiring on-prem GPU infrastructure.

## Relevance to YOLO loop

If our YOLO loop processes proprietary code or customer data, routing through Vertex instead of direct Anthropic API adds a contractual and technical data-residency guarantee with minimal model-quality trade-off.

## Notes

Compare latency and cost delta between direct Anthropic API vs Vertex-brokered Anthropic. Verify current Vertex model availability matches direct API model versions.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-08 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-10-08-gcp-vertex-data-residency` |
| Channel | mlops |
| Video | [How a Logistics Giant Keeps AI Data Locked Down](https://www.youtube.com/watch?v=oYlb1Wv6Vkk) |
| Published | 2026-10-08 |
| Ingested upstream | 2026-10-08 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
