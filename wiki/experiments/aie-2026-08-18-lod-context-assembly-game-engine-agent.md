# Apply Level-of-Detail (LOD) Context Pruning to Manage Large Scene Graphs in Agent Prompts

> Back to [[experiments-index]]

Source: **[The Next Game Engine Won't Have a Manual — Arturo Nunez, Nereu](https://www.youtube.com/watch?v=VBCDhRrvlYo)** · aie · 2026-08-18

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we assemble agent context using a level-of-detail strategy—sending full detail for objects near the user's focus and only summary tags for distant/irrelevant objects—then we can keep large scene or codebase graphs within context limits without losing actionable detail, because the same spatial-relevance heuristic that drives GPU rendering efficiency can drive LLM context efficiency.

## What they did

Arturo Nunez (Nereu, formerly Unity 10 years) built a natural-language game engine where users describe what they want and an LLM agent configures scene objects, physics, cameras, and particle systems without coding. The core context management challenge: a scene with 100+ objects would overflow the LLM context if sent in full. His solution: borrow the Level of Detail (LOD) concept from 3D rendering. Objects near the user's current focus (e.g., the selected object and its neighbors) are included in full detail with all tag values. Objects farther away are summarized as 'there is a player-tagged object at position X' with no attribute detail. As the user moves focus or edits different parts of the scene, the context window is resampled. This keeps context size manageable while preserving precision where the agent needs to act.

## Relevance to YOLO loop

Directly applicable to any agent that operates over a large structured artifact (codebase, knowledge graph, scene, database schema). Instead of truncating arbitrarily or embedding everything, use proximity/relevance to the current task to allocate context budget—a principled alternative to naive RAG chunking.

## Notes

The LOD analogy maps to: high-detail = recently edited files or directly referenced modules; medium-detail = files in the same directory; low-detail = distant modules summarized by signature only. Could be combined with embedding-based relevance scoring to make the 'distance' metric semantic rather than purely spatial.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-18 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-18-lod-context-assembly-game-engine-agent` |
| Channel | aie |
| Video | [The Next Game Engine Won't Have a Manual — Arturo Nunez, Nereu](https://www.youtube.com/watch?v=VBCDhRrvlYo) |
| Published | 2026-08-18 |
| Ingested upstream | 2026-08-18 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
