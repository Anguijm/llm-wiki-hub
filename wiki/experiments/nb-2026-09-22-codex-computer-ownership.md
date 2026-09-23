# Audit Codex Agent Permissions and Sandboxing Boundaries

> Back to [[experiments-index]]

Source: **[Does Your Computer Belong To Codex? I Went To OpenAI To Ask.](https://www.youtube.com/watch?v=TR8RDUzQaMo)** · nb · 2026-09-22

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we explicitly audit and constrain what filesystem and network resources Codex can access during agentic coding sessions, then we reduce risk of unintended side effects because Codex operates with broad permissions by default that most developers are unaware of.

## What they did

Nate Jones visited OpenAI to investigate the scope of control and resource access that Codex (the agentic coding assistant) has over a user's local machine, probing questions around ownership, permission models, and sandboxing when Codex executes code autonomously.

## Relevance to YOLO loop

In our YOLO loop, Codex or similar agents execute code autonomously. Understanding and locking down permission boundaries is a prerequisite for safely running agentic steps without human review on every action.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-22 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-09-22-codex-computer-ownership` |
| Channel | nb |
| Video | [Does Your Computer Belong To Codex? I Went To OpenAI To Ask.](https://www.youtube.com/watch?v=TR8RDUzQaMo) |
| Published | 2026-09-22 |
| Ingested upstream | 2026-09-22 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
