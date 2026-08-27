# Route agent tasks through OpenRouter to benchmark cost and model selection at scale

> Back to [[experiments-index]]

Source: **[Stripe Paid $7.5 Billion For OpenRouter. You Are Living In The Age Of Startups.](https://www.youtube.com/watch?v=DgyQ5r6bnmc)** · nb · 2026-08-27

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we route our agent task calls through OpenRouter rather than single-provider APIs, then we will be able to empirically compare cost-per-task and latency across 400+ models, because OpenRouter's aggregation layer exposes model-level pricing signals that enable data-driven model selection per task type.

## What they did

Speaker analyzed Stripe's $7.5B acquisition of OpenRouter (valued at $1.3B just 90 days prior), noting OpenRouter's weekly token volume grew 24,000x since August 2023 and doubles every 11 weeks. He argued Stripe views intelligence consumption as a basic economic flow and that OpenRouter's multi-model routing is infrastructure for the intelligence age, enabling founders to rent intelligence one job at a time.

## Relevance to YOLO loop

Relevant to cost optimization in our dev loop. Integrating OpenRouter as a routing layer would let us A/B test cheaper models on routine subtasks while reserving expensive frontier models for high-complexity steps, with token cost data feeding back into task planning.

## Notes

11-week doubling cadence for token volume is the key strategic signal. Worth tracking our own token consumption trajectory against this baseline.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-27 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-08-27-stripe-openrouter-token-economy` |
| Channel | nb |
| Video | [Stripe Paid $7.5 Billion For OpenRouter. You Are Living In The Age Of Startups.](https://www.youtube.com/watch?v=DgyQ5r6bnmc) |
| Published | 2026-08-27 |
| Ingested upstream | 2026-08-27 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
