# Add Durable Execution Infrastructure to Long-Running Agents Using Restate

> Back to [[experiments-index]]

Source: **[Every step you take, every call you make: the reliable agent stack — Giselle van Dongen, Restate](https://www.youtube.com/watch?v=cI7zfqusmFU)** · aie · 2026-09-14

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we route agent execution through a durable execution server (like Restate) that journals every step, then long-running agents can recover from crashes at exactly the point of failure rather than restarting from scratch, because the event journal persists all LLM calls, tool results, and state transitions externally, making the agent process stateful and resumable independently of the underlying compute.

## What they did

Giselle van Dongen demonstrated Restate, an open-source durable execution framework inspired by Apache Flink and Meta's event infrastructure. Restate sits as a proxy/broker in front of agent services. As the agent runs, it emits events over an open connection to Restate, which journals them. On failure, the journal replays to restore state at the exact failure point. She demoed a Slack-connected deep research agent: planner agent fans out to parallel sub-research agents, then a writer agent — all coordinated through Restate with human-in-the-loop approval gates. Features shown: concurrent session isolation, agent-to-agent communication, flow control (e.g., department-level rate limits on LLM gateway calls), cancellation/kill of stuck executions, and a cockpit UI showing agent registry, active executions, and per-step journals. Restate runs as a single binary, supports HA via multi-instance snapshots to object storage, has 6 SDKs, and integrates with popular agent frameworks. Push model gives ~45ms p99 latency for 10-step workflows. Available as self-hosted, BYOC, or managed cloud.

## Relevance to YOLO loop

Our YOLO loop has no crash recovery — a failed long-running agent run loses all intermediate state. Wrapping agent steps in Restate's durable execution model would give us automatic resume-from-failure, which is especially valuable for multi-step research or code-generation loops that take minutes to hours.

## Notes

Restate is open source on GitHub. BYOC option keeps data in your cloud account. The push model (vs. pull) is a meaningful architectural differentiator for low-latency agentic workloads. Human-in-the-loop approval gates demonstrated via Slack integration.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-14 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-14-restate-durable-agents` |
| Channel | aie |
| Video | [Every step you take, every call you make: the reliable agent stack — Giselle van Dongen, Restate](https://www.youtube.com/watch?v=cI7zfqusmFU) |
| Published | 2026-09-14 |
| Ingested upstream | 2026-09-14 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
