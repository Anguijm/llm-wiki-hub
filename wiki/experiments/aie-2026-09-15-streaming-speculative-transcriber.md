# Implement streaming speculative transcription + background tool-calling + TTS prefix caching to minimize voice agent latency

> Back to [[experiments-index]]

Source: **[Realtime Voice Agents with Frontier Intelligence — Bohan Li, EliseAI](https://www.youtube.com/watch?v=MBHOH1NmDqc)** · aie · 2026-09-15

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we layer a fast streaming ASR (e.g., Flux) under a slower accurate batch ASR (e.g., Scribe V2) with speculative correction, run background tool calls that push results into the main agent context, and cache common TTS prefix audio to emit before the full generation completes, then we achieve near-real-time voice agent response latency with frontier-model intelligence, because each technique hides a different latency component from the user without degrading accuracy.

## What they did

Bohan Li (EliseAI, formerly self-driving cars) described a three-layer cascaded voice agent architecture modeled on autonomous vehicle perception/planning/control. (1) Streaming speculative transcriber: a fast streaming ASR layer fires immediately; a slower accurate batch layer (Scribe V2) runs in parallel and fires a correction only when it disagrees. (2) Background tool-calling: a background agent preemptively fires tool calls on partial transcriptions and injects results into the main agent context so the main LLM never has to wait for tool round-trips. (3) TTS prefix caching: common sentence prefixes (e.g., 'You said your name is') are pre-rendered and cached; when a cache hit is detected, cached audio is emitted immediately while the remainder streams from Cartesia, which generates with full prosody context, suppressing the already-played prefix. He played a live OBGYN scheduling call demo showing natural latency.

## Relevance to YOLO loop

Directly relevant if we are building or evaluating voice agent pipelines. Each of the three techniques (speculative transcription, background tool-calling, TTS prefix cache) is independently implementable and stackable. Background tool-calling in particular generalizes to any multi-step agent loop where tool latency is a bottleneck.

## Notes

Background tool-calling pattern is the highest-value standalone technique—applicable to text agents too. TTS prefix caching requires profiling which prefixes actually repeat at volume before building cache infrastructure.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-15 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-15-streaming-speculative-transcriber` |
| Channel | aie |
| Video | [Realtime Voice Agents with Frontier Intelligence — Bohan Li, EliseAI](https://www.youtube.com/watch?v=MBHOH1NmDqc) |
| Published | 2026-09-15 |
| Ingested upstream | 2026-09-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
