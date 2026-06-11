# Apply the six Claude Code dynamic workflow patterns to match task structure to agent topology

> Back to [[experiments-index]]

Source: **[Master All 6 Claude Code Dynamic Workflows](https://www.youtube.com/watch?v=g9b9G8dcS8Y)** · mk · 2026-06-11

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we select the appropriate dynamic workflow pattern (classify-and-act, fan-out-and-synthesize, adversarial verification, generate-and-filter, tournament, loop-until-done) based on the structural shape of a task, then agent output quality and reliability will improve compared to single-context-window approaches because each pattern addresses specific failure modes like goal drift, agent laziness, and self-preference bias.

## What they did

Mark broke down an Anthropic engineering guide on Claude Code dynamic workflows into six core patterns. Classify-and-act: a lightweight classifier routes tasks to specialized handler agents (e.g., inbox triage). Fan-out-and-synthesize: a task is split into parallel mutually-exclusive sub-tasks, each handled by a separate Sonnet 4.6 agent, then synthesized (e.g., deep research, due diligence). Adversarial verification: one agent produces output, a separate agent tries to refute it, returning only confirmed findings. Generate-and-filter: generate many candidates then filter against criteria. Tournament: candidates compete in head-to-head comparisons. Loop-until-done: agents run in a loop with a judge until a terminal success condition is met (e.g., no new issues found in a security audit). He also covered when NOT to use workflows (simple tasks), how to share workflows as JS files bundled with skill.md, and using token budget instructions to control cost.

## Relevance to YOLO loop

Directly applicable for complex YOLO loop tasks: code audits can use adversarial verification, research tasks can use fan-out, and iterative refactoring until tests pass can use loop-until-done. Knowing the six patterns lets us choose the right harness instead of defaulting to single-agent prompts.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-11 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mk-2026-06-11-six-dynamic-workflow-patterns` |
| Channel | mk |
| Video | [Master All 6 Claude Code Dynamic Workflows](https://www.youtube.com/watch?v=g9b9G8dcS8Y) |
| Published | 2026-06-11 |
| Ingested upstream | 2026-06-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
