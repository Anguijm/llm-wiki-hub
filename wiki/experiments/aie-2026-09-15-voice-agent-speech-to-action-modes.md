# Design voice agent interactions around three distinct modes (speech-to-speech, speech-to-action, event-to-speech) and use GPT Realtime 2 with preambles for tool-calling latency management

> Back to [[experiments-index]]

Source: **[Voice Agents Can Just Do Things — Charlie Guo, OpenAI](https://www.youtube.com/watch?v=OpY6MmZFeHo)** · aie · 2026-09-15

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we explicitly design voice agent UX by first asking 'what is the role of voice/audio in this interaction' and then mapping to speech-to-speech, speech-to-action, or event-to-speech modes (or combinations), then we unlock higher-value use cases than default chatbot patterns, because voice's primary value in many workflows is initiating actions or being triggered by events—not just conversation—and most builders default to speech-to-speech when the other modes better fit the use case.

## What they did

Charlie Guo (developer experience, OpenAI) argued that voice agents do not have to talk back—speech is not the only valid response modality. He defined three remixable modes: (1) Speech-to-speech: user talks, model talks back (language learning, concierge/support, live translation). (2) Speech-to-action: user talks, model uses tools (form filling, creative tools, computer use)—identified as the most underexplored/highest-potential category. (3) Event-to-speech: system detects an event, model speaks (GPS navigation, proactive notifications). He introduced GPT Realtime 2, which adds reasoning before speaking, parallel tool calling, and preambles—a mechanism to have the agent verbally notify the user it's performing a background action (e.g., 'I'm going to check flight prices, give me a second') while tools run asynchronously. He noted that using native audio models vs. chained STT/LLM/TTS reduces latency significantly and preserves tone/emotion/prosody information lost in transcription.

## Relevance to YOLO loop

The speech-to-action mode is directly applicable: any step in our loop where a developer describes what they want verbally could trigger agent actions without requiring text output. Preambles are a useful UX pattern for any long-running agent action—text equivalent would be streaming status updates before results. The three-mode framework is a useful design tool for scoping voice experiments.

## Notes

GPT Realtime 2 is the current OpenAI realtime model with reasoning + parallel tool calling + preambles. The Mehrabian stat cited (55% body language, 38% tone, 7% words) is frequently misapplied but the core point—transcription loses tone/emotion—is valid and architecturally important.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-15 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-15-voice-agent-speech-to-action-modes` |
| Channel | aie |
| Video | [Voice Agents Can Just Do Things — Charlie Guo, OpenAI](https://www.youtube.com/watch?v=OpY6MmZFeHo) |
| Published | 2026-09-15 |
| Ingested upstream | 2026-09-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
