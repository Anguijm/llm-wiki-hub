# Instrument agent sessions to detect pre-transaction token theft before payment calls

> Back to [[experiments-index]]

Source: **[AI Agents Are Starting To Buy. Stripe Is Building How They Pay.](https://www.youtube.com/watch?v=YTG0rdHPTDE)** · nb · 2026-09-17

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we add observability hooks that flag anomalous token consumption patterns before any payment API call is made, then we can intercept the most common agentic abuse vector (token stealing rather than money stealing) and halt the session, because as Emily noted most existential abuse AI companies face is pre-transaction.

## What they did

Emily explained that the majority of abuse AI companies face from agents is pre-transaction — specifically 'stealing tokens instead of stealing money.' She drew a distinction between the transaction layer (where Stripe operates) and the pre-transaction layer where bad actors exploit AI systems before any payment occurs, framing this as the harder unsolved trust problem.

## Relevance to YOLO loop

The YOLO loop's agent sessions consume LLM tokens on every run. Adding a pre-call monitor that tracks cumulative token spend per session against a baseline, and auto-terminates sessions that spike anomalously before reaching a payment or action step, mirrors the fraud signal Emily described and hardens the loop against prompt-injection or runaway loops.

## Notes

Pair with existing rate-limit tooling. Log token counts at each tool-call boundary. A simple z-score over rolling session history is a viable first detector.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-17 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-09-17-agent-fraud-pre-transaction` |
| Channel | nb |
| Video | [AI Agents Are Starting To Buy. Stripe Is Building How They Pay.](https://www.youtube.com/watch?v=YTG0rdHPTDE) |
| Published | 2026-09-17 |
| Ingested upstream | 2026-09-17 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
