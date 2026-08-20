# Run agents inside scoped sandboxes with least-privilege access to limit blast radius

> Back to [[experiments-index]]

Source: **[Unlock Agent Autonomy: The Runtime for AI-Native Systems — Tushar Jain, Docker](https://www.youtube.com/watch?v=zaGyGgLW3SM)** · aie · 2026-08-20

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we run each agent task inside a sandboxed environment with only the minimum required tool/API access for that specific task (rather than giving the agent standing broad credentials), then the blast radius of agent mistakes or prompt injection attacks will be contained, enabling us to safely grant agents more autonomy.

## What they did

Tushar Jain (Docker) described and demoed a runtime (spx, brew-installable) that runs coding agents (Claude Code, Codex, OpenCode) inside isolated sandboxes with scoped access. Key points: (1) agents should never have standing broad credentials — only scoped, task-specific capabilities; (2) a real example: his nightly reporting agent unexpectedly posted a PR because it had write access to GitHub when it only needed read; (3) the runtime provides intent-based dynamic access — when an agent needs GitHub access to review a PR, a sub-sandbox is created with that scoped access and the result is returned without the main agent gaining persistent access; (4) the runtime works locally, in the cloud, in VPCs, and across orchestration layers; (5) six agents can run in parallel under the same policy and scoped access model.

## Relevance to YOLO loop

Directly relevant to our agent safety posture. Running Claude Code or other agents via spx would give us sandbox containment without changing our workflow. The intent-based sub-sandbox pattern is a concrete architectural pattern to experiment with for any agent that needs expanding access during a task.

## Notes

Install: `brew install spx`. Supports Claude Code, Codex, OpenCode, custom agents. Key insight: access requirements change at runtime as agents expand their task scope — the runtime must handle dynamic scoped capability grants, not just static upfront permissions. Intent-based access prototype shown: agent requests capability, runtime evaluates intent vs. user query, creates sub-sandbox if approved.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-20 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-20-docker-agent-scoped-sandbox-runtime` |
| Channel | aie |
| Video | [Unlock Agent Autonomy: The Runtime for AI-Native Systems — Tushar Jain, Docker](https://www.youtube.com/watch?v=zaGyGgLW3SM) |
| Published | 2026-08-20 |
| Ingested upstream | 2026-08-20 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
