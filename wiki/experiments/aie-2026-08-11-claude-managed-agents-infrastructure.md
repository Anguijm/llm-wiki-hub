# Implement an outcomes-based grader agent that loops until success criteria are met

> Back to [[experiments-index]]

Source: **[Evolution of agentic surfaces — Gagan Bhat & Isabella Kai He, Anthropic](https://www.youtube.com/watch?v=K0X9QDRkIdg)** · aie · 2026-08-11

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we run a separate grader agent in parallel with our main agent loop — defined by an explicit rubric of success criteria and failure cases — then task completion reliability increases because the grader creates a retry signal that keeps the agent iterating rather than silently returning a suboptimal result.

## What they did

Isabella described Anthropic's 'outcomes' feature in Claude Managed Agents: developers define a rubric (success criteria + failure cases) and a separate grader agent runs alongside the main agent loop, evaluating whether the task was completed per the rubric. If the grader determines failure, the main agent keeps trying until it satisfies the criteria. She framed this as unlocking task categories that were previously unreliable, especially as model capability grows.

## Relevance to YOLO loop

Directly applicable to our YOLO loop as an automated acceptance layer — instead of manual review after each agent run, a grader agent checks the output against a predefined rubric and triggers reruns, effectively turning our loop into a self-correcting pipeline.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-11 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-11-claude-managed-agents-infrastructure` |
| Channel | aie |
| Video | [Evolution of agentic surfaces — Gagan Bhat & Isabella Kai He, Anthropic](https://www.youtube.com/watch?v=K0X9QDRkIdg) |
| Published | 2026-08-11 |
| Ingested upstream | 2026-08-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
