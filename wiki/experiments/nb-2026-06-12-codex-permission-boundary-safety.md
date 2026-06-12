# Enforce Least-Privilege Boundaries on Codex Agent Sessions

> Back to [[experiments-index]]

Source: **[Only 1 in 1,600 People Use Codex. Here's How to Catch Up.](https://www.youtube.com/watch?v=xqGCbEDbny8)** · nb · 2026-06-12

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we explicitly scope each Codex agent session to the minimum required permissions (read-only unless write is essential, no publish/delete/spend without explicit approval, secrets via .env not prompt), then we reduce the blast radius of agent errors while maintaining the productivity gains of autonomous operation.

## What they did

Nate outlined a set of safety rules he applies when using Codex for agentic tasks: never paste API keys or passwords into the chat, use a .env file for secrets, do not grant write access when read access suffices, do not allow send/publish/delete/spend actions unless the workflow is fully understood, and always require the agent to show receipts (files, logs, tests, renders, command output) as verifiable proof of work.

## Relevance to YOLO loop

Applies directly to our YOLO loop's agent permission model. We can encode these rules as a pre-flight checklist or system-prompt header appended to every agent session, ensuring least-privilege is enforced by default rather than per-experiment.

## Notes

The .env secret hygiene point is immediately actionable as a repo-level policy. The receipts/proof habit pairs well with the goal-loop experiment above.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-12 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-06-12-codex-permission-boundary-safety` |
| Channel | nb |
| Video | [Only 1 in 1,600 People Use Codex. Here's How to Catch Up.](https://www.youtube.com/watch?v=xqGCbEDbny8) |
| Published | 2026-06-12 |
| Ingested upstream | 2026-06-12 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
