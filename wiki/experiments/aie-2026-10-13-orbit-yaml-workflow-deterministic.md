# Define agent workflows as YAML files with deterministic steps and LLM-only-where-needed policy

> Back to [[experiments-index]]

Source: **[Agents in Orbit: Workflows, Not Autopilot — Eduardo Simon & Javier Casal, Flywire](https://www.youtube.com/watch?v=rAUyRDOFyHU)** · aie · 2026-10-13

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we encode agent workflows as version-controlled YAML files that interleave deterministic code steps with minimal LLM calls (only where reasoning is genuinely required), then reliability and auditability will improve significantly over open-ended agentic loops, because Flywire achieved a 99% success rate across 11,000+ executions using this pattern.

## What they did

Flywire's AI platform team built Orbit, an internal platform where each agent is defined in a single YAML file living in a repo and reviewed like any other code. Workflows chain deterministic activities (fetch metadata, classify risk, clone repo) with a small number of LLM steps that have strict output schemas and no write permissions. Triggers include GitLab webhooks, Jira, Sentry, AWS events, scheduled jobs, and an internal API/CLI. In 30 days their code review agent ran 9,700+ times averaging under 3 minutes; overall 99% success rate across 11k executions.

## Relevance to YOLO loop

Our dev loop currently relies on open-ended agent runs. Wrapping recurring tasks (code review, lint fixes, dependency bumps) in YAML workflow definitions would give us reproducibility, reviewability, and a clear audit trail.

## Notes

Flywire deliberately chose YAML because engineers already know it and it is AI-friendly (coding agents can read/write/review it). They also built an MCP server so agents can trigger workflows from Slack.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-13 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-13-orbit-yaml-workflow-deterministic` |
| Channel | aie |
| Video | [Agents in Orbit: Workflows, Not Autopilot — Eduardo Simon & Javier Casal, Flywire](https://www.youtube.com/watch?v=rAUyRDOFyHU) |
| Published | 2026-10-13 |
| Ingested upstream | 2026-10-13 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
