# Wire Jira bug tickets directly into parallel agent work trees to remove human-as-dispatcher bottleneck

> Back to [[experiments-index]]

Source: **[Your Finance Agent's Bottleneck Is You — Ramana Siddanth Emani, Auditoria AI](https://www.youtube.com/watch?v=z0sh8HyTrDo)** · aie · 2026-07-30

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we automate the triage-to-worktree pipeline so each incoming bug ticket spawns an isolated agent work tree that handles root cause analysis, fix implementation, test execution, and PR creation autonomously, then developer throughput will increase significantly because the human bottleneck shifts from dispatching and executing tasks to only reviewing and validating outputs at the PR stage.

## What they did

Siddanth described a harness architecture where with 48GB RAM a developer can run 50 parallel agent work trees simultaneously. Each work tree is an isolated folder where an agent writes and tests code independently. The proposed pipeline for a QA-reported bug: (1) agent parses requirements and does root cause analysis, (2) pulls traces and logs, (3) sets up a work tree, (4) does TDD and implements fix, (5) runs local end-to-end tests, (6) creates a PR. Human touchpoints are only at step 1 (input the ticket) and step 9 (validate in staging). He also described a self-improvement layer: after running for a day or two solving several tickets, ask the agent to analyze its own bottlenecks and progressively remove them, eventually allowing goal-setting and loop execution without active human monitoring.

## Relevance to YOLO loop

Directly maps to our dev loop architecture. We can instrument our existing issue tracker to auto-spawn agent work trees per ticket, reducing the human role to reviewer rather than executor. The self-improvement layer (agent analyzes its own bottlenecks weekly) is a concrete pattern we could add to our loop's evolve phase.

## Notes

Speaker emphasized skills as organizational secret recipes — reusable workflow fragments given to agents to enforce correct procedures. Also stressed minimal UX (single pane of glass) as critical for maintaining human oversight without tab overload. Finance domain context adds constraint: 'moving fast and breaking things' is not acceptable, so human approval gate with audit log is non-negotiable.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-30 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-30-finance-agent-dev-loop-velocity` |
| Channel | aie |
| Video | [Your Finance Agent's Bottleneck Is You — Ramana Siddanth Emani, Auditoria AI](https://www.youtube.com/watch?v=z0sh8HyTrDo) |
| Published | 2026-07-30 |
| Ingested upstream | 2026-07-30 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
