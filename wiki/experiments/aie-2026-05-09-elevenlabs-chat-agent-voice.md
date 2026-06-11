# Integrate ElevenLabs voice layer into a chat agent for real-time voice interaction

> Back to [[experiments-index]]

Source: **[Give Your Chat Agent a Voice — Luke Harries, ElevenLabs](https://www.youtube.com/watch?v=DCZZ3AJKzuc)** · aie · 2026-05-09

**Status:** `discarded` · **Verdict:** `discard` · **Effort:** `medium`

---

## Hypothesis

If we add ElevenLabs streaming TTS to our chat agent, then users can interact via natural voice with low latency because ElevenLabs provides a production-grade API designed for real-time agent voice output.

## What they did

Speaker from ElevenLabs described how to wire their voice API into a chat agent pipeline, covering streaming, latency considerations, and practical integration patterns.

## Relevance to YOLO loop

Relevant if we build voice-accessible interfaces for our loop; ElevenLabs integration pattern is well-documented and could be added as an output channel.

## Notes

Discarded 2026-05-10: covered by nh-2026-05-04-voice-agent-claude-code-elevenlabs already in tick_queue_approved.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-05-09 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-05-09-elevenlabs-chat-agent-voice` |
| Channel | aie |
| Video | [Give Your Chat Agent a Voice — Luke Harries, ElevenLabs](https://www.youtube.com/watch?v=DCZZ3AJKzuc) |
| Published | 2026-05-09 |
| Ingested upstream | 2026-05-09 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
