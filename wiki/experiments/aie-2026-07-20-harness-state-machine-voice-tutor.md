# Wrap multi-step agent logic in an explicit state machine harness

> Back to [[experiments-index]]

Source: **[Don't Let the LLM Drive - Ornella Bahidika & Joel Allou, Microsoft](https://www.youtube.com/watch?v=m24UKZomm7k)** · aie · 2026-07-20

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we encode multi-step agent workflows as explicit state machines where the harness controls state transitions and the LLM only executes single atomic steps, then reliability will improve and a smaller, cheaper model can replace a frontier model because the model is never responsible for deciding what comes next.

## What they did

Ornella and Joel built ACE, a live AI voice tutor, as a state machine with discrete steps (intro, teach, check, grade, advance, wrap). Each step sends the model a tightly scoped 'neural contract'—a single instruction with a defined expected output. The harness validates the output, advances state, and decides the next step. The model is never asked to track progress or decide flow. This allowed them to replace Claude Opus 4.7 with Haiku 4.5, reducing cost and latency while maintaining reliability. They showed live logs of harness events (section input, whiteboard draw, queue clear, lesson end) running alongside the model.

## Relevance to YOLO loop

The YOLO loop runs multi-step coding/review/test cycles that can loop or skip steps unpredictably. Encoding the loop as an explicit state machine with harness-controlled transitions would prevent runaway loops and make each LLM call a single scoped task, enabling use of a cheaper/faster model for most steps.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-20 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-20-harness-state-machine-voice-tutor` |
| Channel | aie |
| Video | [Don't Let the LLM Drive - Ornella Bahidika & Joel Allou, Microsoft](https://www.youtube.com/watch?v=m24UKZomm7k) |
| Published | 2026-07-20 |
| Ingested upstream | 2026-07-20 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
