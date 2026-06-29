# Decompose a monolithic agent into a coordinator plus narrow domain-specific sub-agents with sandboxed file systems

> Back to [[experiments-index]]

Source: **[The Future Is Domain-Specific Agents - Justin Schroeder, StandardAgents](https://www.youtube.com/watch?v=spNAUEgq_A8)** · aie · 2026-06-29

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we replace a single large-context agent with a coordinator agent that delegates to small domain-specific sub-agents (each with its own sandboxed file system and code execution environment, minimal context, and focused tool set), then reliability, maintainability, and context efficiency will improve because each sub-agent maintains a small, relevant context window and the coordinator only holds inter-agent orchestration logic.

## What they did

Justin Schroeder (Standard Agents) argued that the core problem blocking enterprise agent adoption is not intelligence but reliable integration. He proposed an architecture where every agent gets: (a) a sandboxed file system, (b) a sandboxed code execution environment, and (c) a focused, minimal context window. A coordinator agent routes to specialized sub-agents (e.g. Salesforce agent → asset-generator sub-agent; legal team agent → GDPR compliance sub-agent → OSHA sub-agent), each recursively decomposable. This keeps context windows small throughout the hierarchy and makes each agent independently testable and replaceable.

## Relevance to YOLO loop

Directly applicable to our YOLO loop architecture: rather than one god-agent with a massive context, we can split by domain (code review, deployment, testing, doc generation) with a thin coordinator. Each domain agent is easier to eval, upgrade, and sandbox — reducing blast radius of any single agent failure.

## Notes

Standard Agents (standardagents.ai) is in stealth/early access. Key primitive: every agent must have its own sandboxed file system and code execution — these should be baked in, not bolted on. The coordinator/sub-agent distinction maps well to existing harness patterns but requires upfront spec work per domain.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-29 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-06-29-domain-specific-agent-hierarchy` |
| Channel | aie |
| Video | [The Future Is Domain-Specific Agents - Justin Schroeder, StandardAgents](https://www.youtube.com/watch?v=spNAUEgq_A8) |
| Published | 2026-06-29 |
| Ingested upstream | 2026-06-29 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
