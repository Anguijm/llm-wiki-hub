# Evaluate Docker and Datadog MCP servers for agent-driven DevOps

> Back to [[experiments-index]]

Source: **[MCP Dev Summit [Day 2] ft AWS, Docker, & Datadog]()** · @MLOps · 2026-04-02

**Status:** `deferred` · **Effort:** `high`

---

## Hypothesis

If we integrate Docker MCP (container management) and Datadog MCP (observability) into the agent toolkit, then build agents can deploy, monitor, and debug containerized projects autonomously because they have direct access to infrastructure and monitoring data.

## What they did

MCP Dev Summit Day 2 featured AWS, Docker, and Datadog presenting their MCP server implementations. This signals production-grade DevOps tooling becoming agent-accessible via MCP.

## Actionable steps

- Check if Docker MCP server is publicly available; install and test with a YOLO project
- Evaluate Datadog MCP for monitoring agent-deployed projects
- Test whether the build agent can docker build + deploy + verify health via MCP tools
- Compare effort vs current manual deploy workflow

## Success metric

Agent successfully builds, deploys, and verifies a containerized project using MCP tools.

## Relevance to YOLO loop

YOLO projects currently deploy manually. Docker MCP would let the build agent handle containerization; Datadog MCP would enable autonomous monitoring.

## Target projects

- [[yolo-projects]] (`yolo-loop-infrastructure`)

## Notes

Deferred 2026-04-07: high effort, requires Docker + Datadog credentials, current YOLO does not deploy containers. Park until harness-cli has a project that needs container deployment + observability.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-03 | `backlog` | Ingested from Phase 4 YouTube pipeline — title-only inference |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-04-03-mcp-day2-integrations` |
| Channel | @MLOps |
| Published | 2026-04-02 |
| Ingested upstream | 2026-04-03 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
