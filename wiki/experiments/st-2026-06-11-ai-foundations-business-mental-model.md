# Frame agent delegation as intern-coaching to improve prompt quality

> Back to [[experiments-index]]

Source: **[AI Foundations for Business: A (non-technical) overview](https://www.youtube.com/watch?v=CCbcPJXBqgw)** · st · 2026-06-11

**Status:** `discarded` · **Verdict:** `discard` · **Effort:** `low`

---

## Hypothesis

If we explicitly frame prompts and task delegation to AI agents using an intern-onboarding mental model (provide context, iterate patiently, build reusable skills), then task completion quality will improve because the model receives sufficient business context and process clarity rather than bare one-shot instructions.

## What they did

Shaw presented a conceptual framework for business users explaining that LLMs are powerful autocomplete engines that generate responses token-by-token, that agents are LLMs equipped with tools and extended thinking, and that the correct mental model for leveraging them is coaching an intern rather than operating traditional software. He walked through how to incrementally delegate tasks, starting with a single example, verifying output, then scaling via scheduled automations. He also explained the compute-intelligence tradeoff: larger models and extended thinking for hard tasks, smaller/faster models for scaled routine tasks.

## Relevance to YOLO loop

Directly informs how we write prompts and structure task handoffs in the YOLO loop. Applying the intern-coaching frame means we should be providing business context upfront, iterating on a single case before automating, and matching model size/thinking budget to task complexity.

## Notes

Backlog triage 2026-06-24 (owner-preference model). Vague business mindset framing, no concrete deliverable.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-11 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `st-2026-06-11-ai-foundations-business-mental-model` |
| Channel | st |
| Video | [AI Foundations for Business: A (non-technical) overview](https://www.youtube.com/watch?v=CCbcPJXBqgw) |
| Published | 2026-06-11 |
| Ingested upstream | 2026-06-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
