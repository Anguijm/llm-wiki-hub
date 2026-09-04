# Use Claude + Blender tool-use to generate an architectural walkthrough film from a property address

> Back to [[experiments-index]]

Source: **[Everyone's Testing Claude Fable 5.1 On Code. It Made Me A 37-Second Film.](https://www.youtube.com/watch?v=55rDzRkUVdE)** · nb · 2026-09-04

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we give Claude a single property address and access to Blender via tool-use, then it can produce a finished architectural walkthrough film without the user needing to know Blender, because Claude can drive the tool end-to-end through agentic code execution.

## What they did

The speaker provided only a Seattle property address to Claude Fable 5.1, which then autonomously used Blender (a 3D tool the speaker had no prior knowledge of) to produce a 37-second architectural walkthrough film entirely from code.

## Relevance to YOLO loop

Demonstrates agentic tool-use where the model drives a complex creative/technical pipeline (3D rendering) from a minimal natural-language prompt — directly relevant to any YOLO loop step that delegates execution to external tools.

## Notes

Speaker compared Claude Fable 5, Fable 5.1, and ChatGPT Soul on the same Blender task; Fable 5.1 produced the longest, highest-quality sequence. Fable 5 had rough edges and went through stairs. Soul was clean but weaker interior quality.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-04 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-09-04-claude-blender-architectural-film` |
| Channel | nb |
| Video | [Everyone's Testing Claude Fable 5.1 On Code. It Made Me A 37-Second Film.](https://www.youtube.com/watch?v=55rDzRkUVdE) |
| Published | 2026-09-04 |
| Ingested upstream | 2026-09-04 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
