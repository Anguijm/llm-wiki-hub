# Gate all irreversible agent actions behind a draft/approval step before execution

> Back to [[experiments-index]]

Source: **[Everything Goldman Sachs Taught Me About AI (In 10 minutes)](https://www.youtube.com/watch?v=ZzHsJW10iq4)** · nh · 2026-08-24

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we configure agentic automations to produce a human-readable plan or draft before executing any irreversible action (sending email, writing files, deploying, spending money), then we will prevent runaway agent errors at scale because a human checkpoint breaks the action loop before the blast radius expands.

## What they did

Herk applied a Goldman principle of looping humans in proportional to consequence: low-stakes tasks (organizing personal notes) can run autonomously, but anything touching clients, important data, or large audiences must go through an approval step. He specifically recommended setting automations to 'draft not send'—having agents write emails to Gmail drafts or proposed replies to a document—and having tools like Claude Code or Codex show a plan before changing files or deploying. He cited the team rule: 'if the agent could potentially do something, assume it will.'

## Relevance to YOLO loop

Maps directly to the YOLO loop's action-execution stage; adding a plan-display step before file writes or API calls that mutate state would implement this pattern with minimal overhead.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-24 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-08-24-agent-draft-not-send` |
| Channel | nh |
| Video | [Everything Goldman Sachs Taught Me About AI (In 10 minutes)](https://www.youtube.com/watch?v=ZzHsJW10iq4) |
| Published | 2026-08-24 |
| Ingested upstream | 2026-08-24 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
