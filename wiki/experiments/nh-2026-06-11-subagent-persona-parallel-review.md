# Spin up parallel persona sub-agents to stress-test outputs from multiple stakeholder viewpoints

> Back to [[experiments-index]]

Source: **[How to Build Claude Subagents Better Than 99% of People](https://www.youtube.com/watch?v=e18sdZLwP7o)** · nh · 2026-06-11

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we orchestrate a main Claude Code session to spawn multiple sub-agents with distinct user personas (e.g. beginner, power user, enterprise exec, domain expert) that each review the same artifact in parallel, then we get richer, cheaper multi-perspective feedback faster than sequential prompting because each sub-agent runs in a fresh context window and can use a cheaper model (Haiku/Sonnet) while the main session stays clean.

## What they did

Nate demonstrated spinning up 5 sub-agents from a single main Claude Code session, each assigned a distinct persona via YAML front-matter in a markdown agent file (e.g. Linda 58 retired teacher = beginner; David 52 COO = enterprise exec). Each agent independently reviewed the same document and returned a report to the orchestrating session. He showed the prompt structure, explained context isolation benefits, the cost saving of assigning cheap models to sub-agents, and best practices: store shared agents in the project repo, personal agents in the home folder, always use YAML front-matter, invoke via slash command.

## Relevance to YOLO loop

Enables automated multi-stakeholder review passes inside the YOLO loop without ballooning the main context window; directly applicable to PR review, doc QA, and spec validation steps.

## Notes

Key rule: sub-agents only talk back to main session, not to each other. For inter-agent communication use agent teams. Dynamic workflows = x-high + parallel sub-agents via JS file; be careful of session limit burn.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-11 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-06-11-subagent-persona-parallel-review` |
| Channel | nh |
| Video | [How to Build Claude Subagents Better Than 99% of People](https://www.youtube.com/watch?v=e18sdZLwP7o) |
| Published | 2026-06-11 |
| Ingested upstream | 2026-06-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
