# Use Gemini Flash audio API to extract structured metadata (speakers, timestamps, language, emotion) from meeting recordings in a single API call

> Back to [[experiments-index]]

Source: **[From Transcription to Live Music: Gemini's Audio Stack — Thor Schaeff, Google DeepMind](https://www.youtube.com/watch?v=Bc6Ojl2XS1w)** · aie · 2026-06-11

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we replace a multi-step transcription+diarization+summarization pipeline with a single Gemini Flash audio API call that instructs the model to simultaneously identify speakers by name, label language per segment, translate non-English segments, assign emotion tags, and provide timestamps, then we will reduce pipeline complexity and latency while maintaining or improving output richness because Gemini processes all audio understanding tasks in one multimodal inference pass.

## What they did

Thor Schaeff from Google DeepMind presented Gemini's audio stack. He demonstrated EchoScript (built on Gemini 3 Flash Preview, available in AI Studio gallery) which takes an audio recording and in a single API request returns: speaker identification by name (when context is provided), accurate timestamps per segment, language detection and translation for non-English segments, emotion classification (happy/sad/angry/neutral) per segment, and a full summary. He showed this working across English, German, French, and Japanese in one recording. He also demonstrated Gemini 3.1 Flash Live, a full-duplex real-time sound-to-sound multimodal model supporting real-time text+voice+vision input, with per-session system prompt customization (e.g., Irish accent persona that applies even when switching languages). Finally he showed Lyra 3 music generation (30-sec clip model + full-length Pro model with lyrics) integrated with the Live API via tool calling to create an interactive jukebox demo.

## Relevance to YOLO loop

If our YOLO loop processes meeting transcripts, standup recordings, or voice memos for context, replacing a multi-step pipeline with a single Gemini audio API call that returns structured JSON (speakers, timestamps, emotions, translations) would simplify the pipeline and enrich the context available to downstream agents.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-11 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-06-11-gemini-audio-rich-transcription` |
| Channel | aie |
| Video | [From Transcription to Live Music: Gemini's Audio Stack — Thor Schaeff, Google DeepMind](https://www.youtube.com/watch?v=Bc6Ojl2XS1w) |
| Published | 2026-06-11 |
| Ingested upstream | 2026-06-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
