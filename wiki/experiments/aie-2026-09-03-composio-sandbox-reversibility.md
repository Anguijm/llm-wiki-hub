# Add a sandbox dry-run gate before irreversible agent actions

> Back to [[experiments-index]]

Source: **[From coding to Knowledge work agents — Karan Vaidya, Composio](https://www.youtube.com/watch?v=xxfMT-bPEmU)** · aie · 2026-09-03

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we route all agent tool calls through a reversibility classifier that either provides an undo function or routes the action to a sandbox for human review before execution, then we will reduce catastrophic irreversible mistakes without blocking agent autonomy on safe actions, because the blast radius of irreversible knowledge-work actions (sent emails, deleted records, wires) is permanently damaging whereas code mistakes can be reverted.

## What they did

Karan described building a reversibility layer where actions that can be undone (e.g., adding a label) get an explicit undo button, while actions that cannot (e.g., hard-deleting emails, sending messages) are first executed in a sandbox and the user is shown a preview and asked to confirm before the action touches the real environment.

## Relevance to YOLO loop

Applicable to any agent in our loop that writes to external systems (GitHub PRs, API calls, file deletions). We could wrap our tool-call layer with a reversibility classifier and add a confirmation step for flagged actions, reducing the risk of agents making unrecoverable changes during automated runs.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-03 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-03-composio-sandbox-reversibility` |
| Channel | aie |
| Video | [From coding to Knowledge work agents — Karan Vaidya, Composio](https://www.youtube.com/watch?v=xxfMT-bPEmU) |
| Published | 2026-09-03 |
| Ingested upstream | 2026-09-03 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
