# Use Codex + Hyperframes to edit long-form video via natural language prompts

> Back to [[experiments-index]]

Source: **[GPT-6 Astra Finally Solves AI Video Editing (full guide)](https://www.youtube.com/watch?v=o3IEkKXXXvo)** · nh · 2026-09-08

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we feed a face-cam and screen-recording into Codex with Hyperframes skills installed and describe the desired output in natural language, then we can produce a cut, composed, and animated video (with dynamic layouts, subtitles, and motion graphics) without manual timeline editing, because Hyperframes interprets the transcript and prompt to make scene-level editing decisions automatically.

## What they did

Nate installed Hyperframes inside the Codex desktop app and loaded a set of pre-built 'skills' that teach the agent editing conventions (e.g., go full-screen when nothing is on screen, return to picture-in-picture during tutorials, insert title cards between sections). He fed two raw recordings (face-cam + screen capture) of a 14-minute video, prompted in natural language describing desired style and layout, and let the agent transcribe, cut mistakes/dead space, apply rounded crops, add animated cards, and compose the final export. He then iterated with follow-up prompts (V2, V3) to adjust text size, 3D feel, and add a full-screen animated cutaway. Each render took roughly 10 minutes.

## Relevance to YOLO loop

Directly applicable to our content production loop: if we are generating tutorial or demo videos from screen recordings, this approach replaces manual editing with a prompt-driven agent step, reducing post-production time and enabling rapid iteration via follow-up prompts rather than timeline scrubbing.

## Notes

Nate offers a free 'student kit' of Hyperframes skills in his School community. Key workflow: install Hyperframes MCP/skill pack → set up optional ElevenLabs transcription → write a natural-language prompt describing scene logic → iterate with follow-up prompts. The local-host Hyperframes editor also allows manual tweaks post-generation.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-08 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-09-08-codex-hyperframes-ai-video-editing` |
| Channel | nh |
| Video | [GPT-6 Astra Finally Solves AI Video Editing (full guide)](https://www.youtube.com/watch?v=o3IEkKXXXvo) |
| Published | 2026-09-08 |
| Ingested upstream | 2026-09-08 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
