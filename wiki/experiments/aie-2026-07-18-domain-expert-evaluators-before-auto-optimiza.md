# Define high-signal domain evaluators with experts before running any prompt auto-optimization loop

> Back to [[experiments-index]]

Source: **[Stop Burning Tokens: Why self-improvement needs domain expertise first - Annabell Schäfer, Langfuse](https://www.youtube.com/watch?v=eAXxdtNlK04)** · aie · 2026-07-18

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we co-create concrete labeled examples and failure-mode evaluators with domain experts before launching a self-optimization loop, then the optimizer will converge on prompts that actually serve the domain rather than overfitting to a poorly-specified target function, because the evaluator signal reflects real-world quality rather than a proxy metric.

## What they did

Annabell Schäfer ran a minimal self-optimization loop on arXiv paper classification (200 fit / 100 validate / 300 test) using GPT-4o-mini as classifier and Claude Opus as optimizer. The baseline flat-label prompt improved substantially through automated iterations, but the key lesson was that in domains without a clear binary target (unlike 'does code compile'), teams that invested early in working with domain experts to define examples, standardize formatting, identify failure modes, and create high-signal evaluators were the ones who shipped reliably. She recommended treating validation splits like traditional ML to prevent overfitting and giving the loop an escape hatch to avoid runaway token burn.

## Relevance to YOLO loop

The YOLO loop's self-improvement cycle needs a well-defined eval layer before automated prompt tuning is trustworthy; this experiment validates the exact sequence: expert-defined evals first, then automated optimization with validation gating.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-18 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-18-domain-expert-evaluators-before-auto-optimization` |
| Channel | aie |
| Video | [Stop Burning Tokens: Why self-improvement needs domain expertise first - Annabell Schäfer, Langfuse](https://www.youtube.com/watch?v=eAXxdtNlK04) |
| Published | 2026-07-18 |
| Ingested upstream | 2026-07-18 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
