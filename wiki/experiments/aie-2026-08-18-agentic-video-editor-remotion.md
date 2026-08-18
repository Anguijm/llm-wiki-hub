# Use Remotion (Video-as-React-Code) as the Agent Output Format for Programmatic Video Composition

> Back to [[experiments-index]]

Source: **[Building an Agentic Video Editor for Mass Consumer — Ekaterina Deyneka, Reelful](https://www.youtube.com/watch?v=pPj_tjlvYjA)** · aie · 2026-08-18

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we have an agent write Remotion compositions (React-based video-as-code) rather than directly manipulating video files, then the agent can reliably assemble multi-track video edits with captions, music, and b-rolls, because agents are already strong code writers and Remotion reduces video composition to structured, verifiable code that can be linted and iterated.

## What they did

Ekaterina Deyneka (Reelful CEO) described an agentic video editing pipeline where users drop in raw footage and the agent produces a polished clip. The key architectural choice: the agent writes Remotion compositions (React code representing the video timeline) rather than manipulating video files directly. The pipeline runs in a sandboxed remote machine; the agent uses skills (cut rules, font pairs, b-roll generation, voiceover, image animation) to assemble the composition. A verification layer checks the composition for errors before rendering and sends it back to the agent for correction if needed. She noted agents are good at writing code, making Remotion a natural fit. The pipeline concludes with a rendered video export.

## Relevance to YOLO loop

If the dev loop needs to produce video outputs (demos, documentation clips, generated content), using Remotion as the intermediate representation lets an agent author, verify, and iterate on video compositions the same way it would iterate on any code artifact.

## Notes

Remotion is open source (remotion.dev). The verification layer is critical—without it, malformed compositions cause silent render failures. Reelful received A16Z Speed Run funding. The sandboxed execution environment pattern mirrors agentic code sandbox approaches (e.g., E2B), so existing sandbox tooling may be reusable.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-18 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-18-agentic-video-editor-remotion` |
| Channel | aie |
| Video | [Building an Agentic Video Editor for Mass Consumer — Ekaterina Deyneka, Reelful](https://www.youtube.com/watch?v=pPj_tjlvYjA) |
| Published | 2026-08-18 |
| Ingested upstream | 2026-08-18 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
