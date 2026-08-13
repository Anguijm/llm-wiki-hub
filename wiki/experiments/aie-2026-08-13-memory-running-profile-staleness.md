# Implement Asynchronous Running-Profile Memory with Conflict Detection

> Back to [[experiments-index]]

Source: **[Lessons from Studying Every Memory System — Shlok Khemani, Independent](https://www.youtube.com/watch?v=5ZGyKWjQDr0)** · aie · 2026-08-13

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we build a user memory system that asynchronously updates a dense running profile from conversation history (like ChatGPT V2's dreaming process) AND adds a conflict-detection pass that flags contradictory facts for clarification, then personalization accuracy will improve over naive fact-list memory because stale or conflicting memories are surfaced rather than silently persisted.

## What they did

Shlok reverse-engineered ChatGPT's memory evolution from V1 (explicit user-triggered fact storage with staleness problems) to V2 (asynchronous background 'dreaming' that updates a dense ~4000-token running profile every few days). He identified that V2 removed user management burden but still produced conflicting memories (e.g., recording Turkey as visited when the user only considered it) because the system lacks curiosity about gaps and conflicts. He proposed that conflict detection is a product problem, not a technology limitation.

## Relevance to YOLO loop

Relevant to any YOLO loop feature involving persistent user or project context: rather than a flat memory list, a dreaming-style background job could consolidate agent session history into a project profile, and a conflict-detection step could flag when new observations contradict prior assumptions before they corrupt downstream prompts.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-13 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-13-memory-running-profile-staleness` |
| Channel | aie |
| Video | [Lessons from Studying Every Memory System — Shlok Khemani, Independent](https://www.youtube.com/watch?v=5ZGyKWjQDr0) |
| Published | 2026-08-13 |
| Ingested upstream | 2026-08-13 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
