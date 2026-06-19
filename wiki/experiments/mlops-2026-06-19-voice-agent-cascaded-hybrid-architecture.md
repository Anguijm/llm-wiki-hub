# Use a foreground/background dual-model pattern for voice agents to balance latency and quality

> Back to [[experiments-index]]

Source: **[Voice Agent Use Cases](https://www.youtube.com/watch?v=no_gxL40NC8)** · mlops · 2026-06-19

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we route voice agent turns through a small fast 'masking' model for filler/bridging responses while a larger background model processes the full context, then we get near speech-to-speech naturalness with cascaded-system reliability and model-swap flexibility because neither model alone handles all requirements optimally.

## What they did

The speaker described design patterns for production voice agents sitting between fully cascaded (ASR→LLM→TTS chained) and fully speech-to-speech architectures. Key patterns discussed: (1) foreground/background dual-model approach—a smaller model handles immediate turn-taking and filler while a larger expensive model runs in background and is called as a tool; (2) conversational TTS that receives full conversation history not just the current utterance, enabling prosody/emotion consistency; (3) fusing ASR and the smaller foreground LLM to cut latency; (4) keeping the larger model swappable so an outage on one provider doesn't brick the whole system. He also discussed using SOP-style documents as the interface for non-technical operations managers to author agent behavior, mirroring how human call center agents were managed.

## Relevance to YOLO loop

The foreground/background model routing pattern is relevant if the YOLO loop ever handles real-time or streaming tasks—cheap fast model for triage/routing, expensive model for heavy reasoning, with explicit tool-call boundary between them.

## Notes

SOP-as-agent-spec interface pattern (non-technical authors defining agent behavior via documents) is also independently interesting for prompt engineering workflows.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-19 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-06-19-voice-agent-cascaded-hybrid-architecture` |
| Channel | mlops |
| Video | [Voice Agent Use Cases](https://www.youtube.com/watch?v=no_gxL40NC8) |
| Published | 2026-06-19 |
| Ingested upstream | 2026-06-19 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
