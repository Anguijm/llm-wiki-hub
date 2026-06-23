# Hand Off a Whole Consulting-Scale Task to a Frontier Model

> Back to [[experiments-index]]

Source: **[The Doing Got Cheap. Now What? | Claude Fable 5 Changes Work](https://www.youtube.com/watch?v=2w_vwQVvFmc)** · nb · 2026-06-23

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we deliberately scope tasks at the scale of a full consulting engagement (hundreds of pages, thousands of records, multi-step deliverable) rather than single-step prompts, then we will surface the real capacity ceiling of frontier models and reclaim high-leverage time because the limiting factor has shifted from model ability to human imagination of the ask.

## What they did

Speaker used Claude Fable 5 on a large-scale data review task (dirty credentials across a large dataset). The model quarantined bad data, inventoried fake credentials without leaking them, and autonomously built a review cube surfacing uncertain calls for human review — without being asked. Speaker walked away and did not monitor. He contrasted this with prior learned behavior of keeping tasks small due to model failure. He recommends stripping old short prompts and replacing them with large-scope job specs, citing Stripe compressing months of engineering into days as a reference point.

## Relevance to YOLO loop

Directly challenges our default of breaking work into small AI subtasks. We should identify one gnarly multi-step pipeline in the dev loop (e.g., full codebase audit, end-to-end test generation, large data validation) and hand it to a frontier model as a single large job spec to measure how much of the loop it can own autonomously.

## Notes

Speaker also notes model still requires human review at the end and has weaknesses in visual design and handwritten image parsing. Cost at ~$50/M output tokens is a real constraint to factor into experiment scoping.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-23 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-06-23-big-task-delegation` |
| Channel | nb |
| Video | [The Doing Got Cheap. Now What? | Claude Fable 5 Changes Work](https://www.youtube.com/watch?v=2w_vwQVvFmc) |
| Published | 2026-06-23 |
| Ingested upstream | 2026-06-23 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
