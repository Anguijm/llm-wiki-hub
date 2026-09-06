# Run identical task prompts through Astra and Fable 5.1 and score output quality, time, and cost per use-case category

> Back to [[experiments-index]]

Source: **[I Tested GPT-6 Astra vs Fable 5.1 on 15 Real Use Cases](https://www.youtube.com/watch?v=WfJPBVXPt8k)** · nh · 2026-09-06

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we run the same real-world task prompts through GPT-6 Astra and Fable 5.1 across a representative spread of use-case categories (documents, code, browser, vision, data analysis), then we will find that neither model dominates across all categories and that cost-per-task differs enough to justify routing different task types to different models because each model has distinct strengths that emerge only under varied, realistic workloads.

## What they did

The speaker ran 15 identical real-world task prompts through both GPT-6 Astra (via Codex) and Fable 5.1, covering web design, presentations, sales copy, browser automation, vision tasks, YouTube analytics, and more. For each use case he recorded which model produced the better output, the wall-clock run time, and the dollar cost. Final tally: Astra won 10/15 use cases; Fable won 5/15. Total run time: Fable 9h 35m at $513, Astra 11h 19m at $327 — Astra was $186 cheaper overall but ~1h 43m slower across the full suite. He noted Astra asked clarifying questions more often while Fable tended to run immediately.

## Relevance to YOLO loop

Gives us an empirical routing heuristic: use Astra for cost-sensitive or output-quality-dominant tasks (especially analytics and code), consider Fable for polished long-form document deliverables. Directly informs which model we select in the YOLO loop dispatcher for different task types.

## Notes

Speaker burned multiple Codex and Claude subscriptions plus thousands in credits. We should replicate a smaller 5-task subset focused on our actual dev-loop tasks (code review, spec writing, test generation, PR summaries, data analysis) before committing to a full 15-case run.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-06 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-09-06-astra-vs-fable-15-use-cases` |
| Channel | nh |
| Video | [I Tested GPT-6 Astra vs Fable 5.1 on 15 Real Use Cases](https://www.youtube.com/watch?v=WfJPBVXPt8k) |
| Published | 2026-09-06 |
| Ingested upstream | 2026-09-06 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
