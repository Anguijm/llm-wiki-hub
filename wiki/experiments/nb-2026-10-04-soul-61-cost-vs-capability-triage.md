# Route Complex-but-Not-Frontier Tasks to GPT-6.1 Soul to Preserve Plan Quota

> Back to [[experiments-index]]

Source: **[Should You Pay $100 A Month For OpenAI's Dots When Meta's Muse Has A Free Version?](https://www.youtube.com/watch?v=lnB4Zckx_34)** · nb · 2026-10-04

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we route document, code, and research tasks to GPT-6.1 Soul instead of o3/Astra by default, then we will consume significantly less weekly plan quota while achieving comparable output quality, because Soul approaches Astra on key evals at roughly one-fifth the token cost.

## What they did

The speaker ran complex documents, code work, and research tasks on GPT-6.1 Soul and observed only 1-2 percentage points of weekly plan limit consumed per session. He reports Soul feels similar to Astra for most tasks and recommends auditing which model handles which workload before upgrading to higher-tier plans.

## Relevance to YOLO loop

Maps to the model-selection/cost-triage layer of the YOLO loop: choosing the cheapest model that meets quality bar for a given task class, keeping frontier-model capacity reserved for tasks that genuinely require it.

## Notes

Experiment is cheap to run: pick 10 representative dev-loop tasks currently sent to o3, rerun on Soul, compare output quality and quota consumption.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-04 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-10-04-soul-61-cost-vs-capability-triage` |
| Channel | nb |
| Video | [Should You Pay $100 A Month For OpenAI's Dots When Meta's Muse Has A Free Version?](https://www.youtube.com/watch?v=lnB4Zckx_34) |
| Published | 2026-10-04 |
| Ingested upstream | 2026-10-04 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
