# Benchmark token-max context compression to cut inference costs on high-volume agent loops

> Back to [[experiments-index]]

Source: **[Stop Renting Your Cognitive Infrastructure - Thiyagarajan Maruthavanan, Kalmantic Labs](https://www.youtube.com/watch?v=Bck7ABCZRZI)** · aie · 2026-07-18

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we apply aggressive input token compression (via a library like just-token-max) to agent loop context before each LLM call, then inference costs will decrease significantly without proportional quality degradation because most context windows contain highly redundant information that the model does not need verbatim.

## What they did

Thiyagarajan Maruthavanan described a progression from rented inference (Anthropic/OpenAI) through token factories (open-source models on neo-clouds or local DGX) to fully owned inference infrastructure. He built just-token-max, an open-source context compression library benchmarked against Netflix's Hedron, claiming superior performance on multiple parameters. His core argument: pre-PMF startups can rent, but post-PMF products and enterprises cannot afford the cost unpredictability, rate-limit dependency, auditability gaps, and security risks of rented inference. He lost $10K to a stolen API key and observed Uber blowing through an annual token budget in four months.

## Relevance to YOLO loop

The YOLO loop makes high-frequency LLM calls; even modest input compression applied systematically could reduce per-run costs enough to justify the integration effort, and the open-source library makes this a low-barrier experiment.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-18 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-18-own-inference-infrastructure-post-pmf` |
| Channel | aie |
| Video | [Stop Renting Your Cognitive Infrastructure - Thiyagarajan Maruthavanan, Kalmantic Labs](https://www.youtube.com/watch?v=Bck7ABCZRZI) |
| Published | 2026-07-18 |
| Ingested upstream | 2026-07-18 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
