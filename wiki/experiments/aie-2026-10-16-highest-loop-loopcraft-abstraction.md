# Map our current agent workflows to explicit loop levels and identify which loop to move up or debug down

> Back to [[experiments-index]]

Source: **[The Highest Loop — swyx](https://www.youtube.com/watch?v=Fva8hFosqyQ)** · aie · 2026-10-16

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we explicitly label each layer of our agentic work (token → chat → tool call → task → automation → cron → software factory) and regularly ask 'which loop am I blocked in?', then we will spend less time solving problems at the wrong abstraction level because knowing your current loop determines whether to add automation (go up) or add reliability work (go down).

## What they did

Swyx introduced the concept of Loopcraft as a core AI engineer skill: mapping work into a stack of nested loops from heartbeat-level primitives up to civilisation-scale collective intelligence. The practical advice was to identify which loop you're currently operating in, go up a loop when you want to scale, and go down a loop when you need to fix reliability issues.

## Relevance to YOLO loop

high: directly maps to how we audit our own Claude Code harness—are we stuck debugging at the tool-call loop when we should be automating at the task loop, or vice versa.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-16 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-16-highest-loop-loopcraft-abstraction` |
| Channel | aie |
| Video | [The Highest Loop — swyx](https://www.youtube.com/watch?v=Fva8hFosqyQ) |
| Published | 2026-10-16 |
| Ingested upstream | 2026-10-16 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
