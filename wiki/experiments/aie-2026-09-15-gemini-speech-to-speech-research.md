# Evaluate Gemini natively multimodal speech-to-speech API for real-time translation and proactive audio features in production voice agent pipeline

> Back to [[experiments-index]]

Source: **[Speech-to-Speech Model Research at Google DeepMind — Valeria Wu Fon & Tom Ouyang, Google DeepMind](https://www.youtube.com/watch?v=18Um2VjMM_g)** · aie · 2026-09-15

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we test Gemini's natively multimodal speech-to-speech model (pre-trained on interleaved audio/video/text) for streaming real-time translation and proactive audio (model knows when not to respond to background noise), then we can achieve translation quality comparable to offline systems at streaming latency and reduce false-positive barge-ins in noisy real-world environments, because native multimodal pre-training eliminates the modality-switching overhead of cascaded systems for these specific capabilities.

## What they did

Valeria Wu Fon (product lead, speech-to-speech, Gemini) and Tom Ouyang (engineer, speech-to-speech, Gemini) described Google DeepMind's approach: Gemini is natively multimodal from pre-training (interleaved audio/video/text examples), enabling a foundation that handles ASR, TTS, translation, and agentic tasks in one model. Key capabilities demonstrated: (1) Live streaming translation achieving offline-system-level quality while translating in real time across multiple languages simultaneously. (2) Proactive audio: the model knows when not to respond to external noise/background speech, critical for real-world (not office) deployment. (3) Multimodal output: real-time avatars with lip-syncing powered by the same speech-to-speech model (pilot with City on Cloud Next). They also described a roadmap toward a single promptable model that switches between translation, action-taking, brainstorming, and open-ended conversation modes. Demo included an insurance roadside assistance call with alphanumeric accuracy for postcodes/registration plates.

## Relevance to YOLO loop

Proactive audio (don't interrupt when background noise appears) is an immediately testable capability for any voice agent we deploy in non-studio conditions. The live translation capability is relevant if our loop needs multilingual support. The native multimodal approach vs. cascaded is a direct architectural decision point when selecting our voice stack.

## Notes

Gemini Live and Gemini Cloud API both use this speech-to-speech foundation. Proactive audio and alphanumeric accuracy for complex strings (postcodes, registration plates) are the most differentiating claims to validate empirically against cascaded alternatives.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-15 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-15-gemini-speech-to-speech-research` |
| Channel | aie |
| Video | [Speech-to-Speech Model Research at Google DeepMind — Valeria Wu Fon & Tom Ouyang, Google DeepMind](https://www.youtube.com/watch?v=18Um2VjMM_g) |
| Published | 2026-09-15 |
| Ingested upstream | 2026-09-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
