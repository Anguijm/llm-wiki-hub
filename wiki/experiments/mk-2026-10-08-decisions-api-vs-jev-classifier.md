# Benchmark OpenAI Decisions API vs Jev for Structured Classification Tasks

> Back to [[experiments-index]]

Source: **[OpenAI's Decisions API just dropped. Here's how it compares to Jev.](https://www.youtube.com/watch?v=uTU5Ihgl_7Q)** · mk · 2026-10-08

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we run identical classification tasks (binary predicate, multiple-choice, scored rubric) through both OpenAI Decisions API and Jev, then Jev will be ~58% cheaper with comparable accuracy but slightly higher latency, while Decisions API will be faster and add multimodal (image) input support, because the cost differential is $0.10 vs $0.042 per million input tokens and Jev is text-only.

## What they did

Mark ran head-to-head demos of OpenAI Decisions API (powered by GPT-6 Luna) and Jev on structured classification tasks including customer support triage, report claim verification, and outage investigation. He measured latency (ms per call), cost per call, and accuracy. Results: OpenAI was consistently ~30-50ms faster on average, Jev was ~40-58% cheaper, both achieved identical accuracy on the test cases. Decisions API supports image input; Jev does not. OpenAI defines refusals; Jev always returns an answer within defined options.

## Relevance to YOLO loop

Classification and routing decisions are common in agent orchestration. Using a dedicated classifier API instead of a full LLM call for binary/choice decisions could cut inference costs significantly in our YOLO loop's routing or triage steps.

## Notes

Decision rule from video: use Jev if cost is priority and inputs are text-only; use Decisions API if multimodal input or marginally lower latency is required. Both return confidence probabilities. Feed API docs to an LLM to generate integration code quickly.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-08 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mk-2026-10-08-decisions-api-vs-jev-classifier` |
| Channel | mk |
| Video | [OpenAI's Decisions API just dropped. Here's how it compares to Jev.](https://www.youtube.com/watch?v=uTU5Ihgl_7Q) |
| Published | 2026-10-08 |
| Ingested upstream | 2026-10-08 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
