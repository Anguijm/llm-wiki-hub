# Route bounded coding tasks to GLM 5.3 inside Claude Code to reduce model costs

> Back to [[experiments-index]]

Source: **[GLM 5.3 in Claude Code Is A Game Changer!](https://www.youtube.com/watch?v=4HvFqhtCb-A)** · nb · 2026-08-21

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we configure Claude Code (or Codex) to use GLM 5.3 via the Z.ai API endpoint for clearly scoped, bounded coding tasks, then we can meaningfully reduce per-task model spend without sacrificing output quality on those tasks, because cheaper models perform adequately on well-defined work that does not require frontier reasoning.

## What they did

Speaker walked through how to swap the model provider inside Claude Code from Anthropic to Z.ai's GLM 5.3 ($18/month plan) by changing the API endpoint and key, keeping all project context files (CLAUDE.md, hooks, rules) intact. He categorized coding work into four buckets and recommended reserving the stronger model for complex reasoning while dispatching bounded, clearly-described tasks to GLM 5.3. He also warned that late mid-session model switches cause expensive context reloads, so he advocated starting new sessions with the cheaper model rather than switching mid-flight.

## Relevance to YOLO loop

Directly applicable to our dev loop: we can define a task-routing heuristic in our agent orchestration layer that sends well-specified subtasks (e.g. boilerplate generation, test writing, lint fixes) to a cheaper model endpoint while keeping the main planning and review steps on a frontier model, reducing API burn rate per loop iteration.

## Notes

Speaker references a companion Substack guide with Claude launcher, Codex profile, handoff templates, and comparison scorecards. Key risk flagged: fully-loaded cost must account for retries and review cycles, not just token price.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-21 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-08-21-glm53-in-claude-code-cost-routing` |
| Channel | nb |
| Video | [GLM 5.3 in Claude Code Is A Game Changer!](https://www.youtube.com/watch?v=4HvFqhtCb-A) |
| Published | 2026-08-21 |
| Ingested upstream | 2026-08-21 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
