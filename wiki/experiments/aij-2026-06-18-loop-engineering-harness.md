# Implement a Loop-Engineer Harness with Domain Contracts and Artifact Logging

> Back to [[experiments-index]]

Source: **[After spent 30+ hrs building loops...](https://www.youtube.com/watch?v=W6x-hb44C0c)** · aij · 2026-06-18

**Status:** `adopted` · **Verdict:** `adopt` · **Effort:** `high`

---

## Hypothesis

If we structure autonomous agent loops around explicit domain contracts (goal, workflow, boundaries, outstanding task list, timeline) and typed artifact outputs (tickets, signals, docs, logs), then the loops will compound in value over time because each session's outputs become structured inputs for subsequent sessions, enabling cross-session state tracking without bloating individual context windows.

## What they did

Jason described 'loop engineering' as the practice of designing systems that autonomously prompt agents in recurring sessions rather than manually prompting each time. His team runs loops that have been operating for days, generating 20-40 high-quality pages daily and submitting PRs autonomously. The architecture involves: (1) a CLAUDE.md with business context and rules for spawning sub-agents and managing git worktrees; (2) an architecture.md defining artifact types (tickets, signals, docs) and loop domains; (3) per-domain contract README files capturing goal, workflow, boundaries, and task lists; (4) a test run with the agent before setting up the scheduled loop; and (5) cron-style loop triggers (e.g., every hour) that invoke the session. He shared a reusable 'loop engineer setup' template capturing these best practices.

## Relevance to YOLO loop

This is a direct architectural blueprint for extending YOLO loop from single-session to multi-session compound loops — particularly relevant for autonomous PR generation, issue triage, and doc generation that currently require manual invocation.

## Notes

Backlog triage 2026-06-24 (owner-preference model). Domain contracts + typed artifact logging — matches the harness's contracts/logging/compounding loops.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-18 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aij-2026-06-18-loop-engineering-harness` |
| Channel | aij |
| Video | [After spent 30+ hrs building loops...](https://www.youtube.com/watch?v=W6x-hb44C0c) |
| Published | 2026-06-18 |
| Ingested upstream | 2026-06-18 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
