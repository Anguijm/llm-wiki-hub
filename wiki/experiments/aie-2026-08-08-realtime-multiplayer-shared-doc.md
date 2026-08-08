# Use a shared live markdown plan document as the primary human-agent collaboration interface

> Back to [[experiments-index]]

Source: **[Realtime multiplayer, automation, and you! — Idan Gazit, GitHub](https://www.youtube.com/watch?v=iQ5xldZ9StU)** · aie · 2026-08-08

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If multiple developers co-edit a shared markdown planning document in real time and the agent re-executes against the latest document state on each save, then team alignment will improve and wasted agentic work will decrease because the shared doc becomes the single source of truth that both humans and agents read/write, preventing small misalignments from snowballing into expensive rework.

## What they did

In the Aces prototype, Idan demonstrated two collaborators simultaneously editing a shared markdown plan document while an agent watched the document and re-ran implementation whenever the plan changed. He showed ambient awareness features (team activity feed showing what each developer's agent was working on) to keep everyone aligned without synchronous meetings.

## Relevance to YOLO loop

Addresses the coordination layer of our loop when multiple agents or developers are running in parallel: a shared living spec document prevents agents from working on stale or conflicting requirements, which is a known failure mode in multi-agent YOLO runs.

## Notes

Aces is in technical preview. Core insight: editing a markdown doc and telling the agent 'make the code true to this doc' may become the primary development interaction pattern, superseding direct code editing.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-08 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-08-realtime-multiplayer-shared-doc` |
| Channel | aie |
| Video | [Realtime multiplayer, automation, and you! — Idan Gazit, GitHub](https://www.youtube.com/watch?v=iQ5xldZ9StU) |
| Published | 2026-08-08 |
| Ingested upstream | 2026-08-08 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
