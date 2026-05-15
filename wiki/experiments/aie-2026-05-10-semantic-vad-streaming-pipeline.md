# Add semantic VAD to streaming STT→LLM→TTS pipeline to reduce perceived latency

> Back to [[experiments-index]]

Source: **[Voice AI: when is the "Her" moment? — Neil Zeghidour, Gradium AI](https://www.youtube.com/watch?v=P_RI1kCkRbo)** · aiDotEngineer · 2026-05-10

**Status:** `deferred` · **Effort:** `medium`

---

## Hypothesis

If we replace fixed-silence voice activity detection with semantic VAD in a streaming cascade pipeline, then end-of-turn detection fires earlier and more accurately, because the model uses meaning rather than silence duration to decide when the user has finished speaking, reducing total round-trip latency.

## What they did

Neil explained that the full cascaded stack (streaming STT + semantic VAD + LLM + streaming TTS with voice cloning) still produces >200ms TTS-alone latency, while human conversational response budgets the entire understand-generate-speak cycle within ~200ms. He identified semantic VAD as a key building block that Gradium ships as part of their cascade to minimize unnecessary silence-wait before LLM invocation.

## Relevance to YOLO loop

If the YOLO loop gains a voice interface for hands-free operation or agent status reporting, semantic VAD is the component that makes turn-taking feel natural rather than clunky, directly affecting developer UX during long agentic runs.

## Notes

Deferred 2026-05-10: streaming pipeline needs a real-time platform we don't have. Park.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-05-10 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-05-10-semantic-vad-streaming-pipeline` |
| Channel | aiDotEngineer |
| Video | [Voice AI: when is the "Her" moment? — Neil Zeghidour, Gradium AI](https://www.youtube.com/watch?v=P_RI1kCkRbo) |
| Published | 2026-05-10 |
| Ingested upstream | 2026-05-10 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
