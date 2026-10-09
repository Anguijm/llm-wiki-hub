# Parallelize multi-part artifact generation with a single sequential plan step

> Back to [[experiments-index]]

Source: **[How I built the World's fastest video, website and app maker - my process](https://www.youtube.com/watch?v=QlXejO3a-lU)** · eh · 2026-10-09

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we generate one master plan first and then dispatch all sub-tasks (scenes, sections, components) to parallel Claude sessions simultaneously, then end-to-end artifact creation time will approach or beat real-time playback/render speed because the bottleneck shifts from sequential inference to network I/O, not reasoning.

## What they did

Speaker built three makers (video, website, app) by iterating on a core insight: write one plan first, then execute every scene/section/component at the same time in parallel, like a film crew shooting in parallel. For video: a 44-second film renders in 38 seconds (faster than it plays), starting playback in ~5 seconds while remaining scenes finish. For websites: full site built in under 30 seconds with a critic agent reviewing desktop and mobile and fixing issues. For apps: first usable photo editor in 43 seconds, with further speed gained by moving final-check logic earlier. Key method: end brainstorming prompts with 'we are just brainstorming for now' to get ideas not code, then use what you build to notice friction and ask why before building the next thing.

## Relevance to YOLO loop

Directly applicable to any multi-section artifact generation in the YOLO loop (PRDs, test suites, docs): replace sequential section generation with plan-then-parallelize.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-09 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `eh-2026-10-09-parallel-scene-generation` |
| Channel | eh |
| Video | [How I built the World's fastest video, website and app maker - my process](https://www.youtube.com/watch?v=QlXejO3a-lU) |
| Published | 2026-10-09 |
| Ingested upstream | 2026-10-09 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
