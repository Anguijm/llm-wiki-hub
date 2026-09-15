# Audit which parts of our AI dev loop accumulate irreplaceable user context and assess switching cost

> Back to [[experiments-index]]

Source: **[Sam Altman and Apple's New CEO are Fighting Over One Thing. It's Not What You Think.](https://www.youtube.com/watch?v=XIt87tJHm-g)** · nb · 2026-09-15

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we explicitly map which components of our system accumulate user history, preferences, and working context, then we can identify the true lock-in layer of our stack and design portability escape hatches before they become expensive to retrofit, because the real competitive moat is accumulated context not compute.

## What they did

The host analyzed Apple's iPhone 18/Duo/Watch Series 12 launch versus OpenAI's agent strategy, arguing the real battle is not hardware vs. software but who holds the user's accumulated work history and context. Apple's fine print revealed daily usage limits with fees for expanded AI access. The host framed this as: whoever holds your history (files, preferences, months of taught behavior) is who you keep paying. He noted moving a subscription is easy but rebuilding an accumulated AI experience is not, making context accumulation the true switching cost.

## Relevance to YOLO loop

Prompts us to audit our YOLO loop: which steps write durable user context (memory, project state, preferences) and are those stored portably? If we are building on a single provider's agent memory, we may be creating lock-in we haven't accounted for in our architecture decisions.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-15 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-09-15-device-vs-agent-trust-split` |
| Channel | nb |
| Video | [Sam Altman and Apple's New CEO are Fighting Over One Thing. It's Not What You Think.](https://www.youtube.com/watch?v=XIt87tJHm-g) |
| Published | 2026-09-15 |
| Ingested upstream | 2026-09-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
