# Define a standing-job governance checklist before deploying a long-running agent

> Back to [[experiments-index]]

Source: **[GPT-6 Astra Doesn't Need Your Instructions Anymore.](https://www.youtube.com/watch?v=1qGH6NwTj3o)** · nb · 2026-09-06

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we require answers to a structured set of governance questions (scope, read/write permissions, autonomous start conditions, commitment authority, monitoring owner, correction mechanism) before assigning any agent a standing job, then we will catch permission and accountability gaps early and reduce unintended agent actions because explicit boundary-setting forces humans to reason about failure modes before they occur rather than after.

## What they did

The speaker argued that before giving a super-agent a persistent, standing role (e.g., 'keep the books current', 'keep customers informed'), teams should answer six explicit questions: What part of my world am I handing over? What is the agent allowed to read and remember? Where can it start without me? What can it promise? Who is watching it? How will errors be corrected? He positioned these as pre-deployment requirements, not afterthoughts, given that Astra is already rolling out to paid plans.

## Relevance to YOLO loop

Our YOLO loop already grants agents broad repo and shell access; this checklist maps directly to the permission-scoping and monitoring hooks we need to define before promoting any agent task from one-shot to standing/scheduled.

## Notes

Low implementation effort — primarily a process artifact (checklist doc or PR template field). High leverage if adopted before standing-job experiments begin.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-06 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-09-06-standing-job-agent-governance` |
| Channel | nb |
| Video | [GPT-6 Astra Doesn't Need Your Instructions Anymore.](https://www.youtube.com/watch?v=1qGH6NwTj3o) |
| Published | 2026-09-06 |
| Ingested upstream | 2026-09-06 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
