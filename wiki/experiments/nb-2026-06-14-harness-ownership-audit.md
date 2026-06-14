# Audit your AI workflows to identify harness ownership vs vendor dependency

> Back to [[experiments-index]]

Source: **[OpenAI Just Filed For Its IPO. The Real Story Isn't The Trillion Dollars.](https://www.youtube.com/watch?v=7RDK84LLL2U)** · nb · 2026-06-14

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we map every AI-assisted workflow to determine whether we own the harness (context, evals, routing logic, model-swap capability) or are renting it from a vendor product, then we can identify which workflows are strategically fragile and prioritize building owned harness layers, because proprietary harnesses capture workflow value while pure API consumption leaves us exposed to token price and vendor access changes.

## What they did

Speaker argued that the strategic question for any team using AI is not which model is best but whether you own the harness: the files the model can see, the tools it can use, the permissions, the memory, the evals, the routing between cheap and expensive models, and the workflow definition of 'done'. He contrasted teams that build internal harnesses (capturing workflow value) against teams that simply use vendor products (ceding the work layer). He listed concrete harness components: eval pipelines, model routing logic, context ownership, ability to swap models without breaking workflows.

## Relevance to YOLO loop

Core strategic framing for our dev loop architecture: every YOLO loop component should be audited against harness ownership criteria—do we own the context, evals, and routing, or are we one vendor policy change away from losing the workflow?

## Notes

Not a technical tutorial but frames a useful pre-mortem checklist: (1) can we swap models without breaking the workflow? (2) do we own the evals? (3) do we own the context? Actionable as an architecture review exercise.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-14 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-06-14-harness-ownership-audit` |
| Channel | nb |
| Video | [OpenAI Just Filed For Its IPO. The Real Story Isn't The Trillion Dollars.](https://www.youtube.com/watch?v=7RDK84LLL2U) |
| Published | 2026-06-14 |
| Ingested upstream | 2026-06-14 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
