# Use an Infinite Canvas as a Multiplayer Multi-Agent Coordination and Visualization Layer

> Back to [[experiments-index]]

Source: **[The Spatial Harness: Bringing Agents to the Canvas — Max Drake, tldraw](https://www.youtube.com/watch?v=XWcXwnysmpY)** · aie · 2026-09-10

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we expose a canvas environment (via TLDraw SDK) to multiple agents as their shared working surface—with tasks, outputs, and agent actions visible spatially—then human oversight of parallel agent work becomes more intuitive and collaborative than text-log monitoring, because spatial arrangement externalizes agent state in a form humans naturally parse.

## What they did

Max Drake (TLDraw) described using TLDraw's infinite canvas + multiplayer SDK as a coordination surface for agents. Key demos: (1) A conductor-style multi-agent orchestrator where tasks are represented as canvas objects assigned to different agents (Claude, etc.) that can be kicked off, monitored, and edited collaboratively by multiple humans in real time; (2) TLDraw Desktop app that exposes the editor instance via a local server, letting Claude Code write plain JavaScript against the canvas—enabling ephemeral spatial UIs that interact with real-world data (Gmail, Notion) and system windows; (3) Teaching agents to understand 2D space required significant engineering to overcome the fundamental limitation that LLMs are trained on text, not spatial coordinates. He also noted that multiplayer canvas means colleagues can join, see agent work in progress, and add tasks—turning agent output into a shared artifact.

## Relevance to YOLO loop

The conductor/orchestration pattern on canvas is a novel alternative to log-based agent monitoring. For our YOLO loop, the most immediately actionable piece is the TLDraw Desktop scripting interface—exposing our dev environment to Claude Code via a local JavaScript API could enable richer spatial task management. Multiplayer visibility into agent work is a collaboration improvement worth prototyping.

## Notes

TLDraw SDK is open source. TLDraw Desktop app with scripting API is the lowest-effort entry point. The 2D spatial understanding limitation is real—agents require significant scaffolding to work reliably in coordinate space.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-10 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-10-tldraw-agent-canvas-spatial-coordination` |
| Channel | aie |
| Video | [The Spatial Harness: Bringing Agents to the Canvas — Max Drake, tldraw](https://www.youtube.com/watch?v=XWcXwnysmpY) |
| Published | 2026-09-10 |
| Ingested upstream | 2026-09-10 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
