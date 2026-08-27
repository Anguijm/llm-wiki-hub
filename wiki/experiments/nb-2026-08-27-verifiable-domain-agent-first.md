# Prioritize agent deployment on verifiable-output tasks first

> Back to [[experiments-index]]

Source: **[Agents Aren't Taking Your Jobs. They're Creating More Work Instead.](https://www.youtube.com/watch?v=IpEaSa7tgfc)** · nb · 2026-08-27

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we restrict initial agent deployments to tasks with objectively verifiable outputs (e.g., test passage, lint errors, schema validation), then we will get faster iteration cycles and higher trust scores, because verifiable domains allow automated correctness checks that eliminate the ambiguous human review bottleneck.

## What they did

Speaker argued that legal and coding have seen the fastest agentic adoption because they are 'verifiable domains' — you can objectively determine if output is correct. He contrasted this with sticky non-verifiable domains like deck creation and pricing recommendations where enterprises must invest heavily to define quality rubrics. He recommended vendors and entrepreneurs target verifiable domains first for faster ROI.

## Relevance to YOLO loop

Directly actionable for task selection in our YOLO loop. We should audit our current agent task queue and tag each task as verifiable vs. non-verifiable, then sequence verifiable tasks earlier to build a feedback signal foundation before tackling ambiguous ones.

## Notes

Legal agentic AI usage cited as up ~108x since January on Codex as supporting evidence for verifiable domain advantage.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-27 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-08-27-verifiable-domain-agent-first` |
| Channel | nb |
| Video | [Agents Aren't Taking Your Jobs. They're Creating More Work Instead.](https://www.youtube.com/watch?v=IpEaSa7tgfc) |
| Published | 2026-08-27 |
| Ingested upstream | 2026-08-27 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
