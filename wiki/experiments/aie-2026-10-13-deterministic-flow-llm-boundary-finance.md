# Draw an explicit determinism boundary: state-machine controls flow/side-effects, LLM only interprets

> Back to [[experiments-index]]

Source: **[Reliable, Smart Workflows for Finance, Wealth and Insurance — Karthic Rao, Perpetual](https://www.youtube.com/watch?v=8g0g1ncwzG0)** · aie · 2026-10-13

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we architect workflows so that a deterministic state machine owns all control flow, evidence recording, and side effects while LLM calls are limited to small, schema-constrained interpretation steps, then we can achieve both regulatory compliance and high reliability, because Perpetual found 95% of model decisions can use fast/cheap 'flash' models, reserving frontier models for only the hardest 5% of cases.

## What they did

Karthic Rao described Perpetual's workflow engine for regulated wealth management. Every workflow step is either deterministic (what runs next, what we know, how we know it, any real-world effect like an email or signed form) or an LLM interpretation call (read ambiguous instructions, classify a response, detect missing fields). LLM calls return structured, schema-validated answers; the state machine decides what to do with the answer. Approvals are gated before any external action. In a demo W-9 form workflow with 20 decisions, 19 used a flash model and 1 used a frontier model. Each classified LLM call generates labeled training data, enabling the flash model to eventually handle more cases locally.

## Relevance to YOLO loop

Our dev loop mixes reasoning and action freely. Explicitly labeling which steps must be deterministic vs. which genuinely need LLM judgment would reduce cost, improve auditability, and make the loop easier to test.

## Notes

Key insight: side effects (emails sent, forms filed, records written) must never be decided by the model—only triggered by the state machine after a human or policy gate. Flash model handles ~95% of calls; labeled outputs feed future fine-tuning.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-13 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-13-deterministic-flow-llm-boundary-finance` |
| Channel | aie |
| Video | [Reliable, Smart Workflows for Finance, Wealth and Insurance — Karthic Rao, Perpetual](https://www.youtube.com/watch?v=8g0g1ncwzG0) |
| Published | 2026-10-13 |
| Ingested upstream | 2026-10-13 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
