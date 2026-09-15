# Prototype a hybrid voice architecture: small full-duplex on-device speech interface delegating to a background text LLM for reasoning

> Back to [[experiments-index]]

Source: **[Your Voice Agent is Just a Walkie Talkie — Neil Zeghidour, Gradium](https://www.youtube.com/watch?v=a8EcVumh71E)** · aie · 2026-09-15

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we split a voice agent into a small full-duplex speech-to-speech model that handles natural conversation and knows when to delegate, plus a background text LLM that handles reasoning/tool-calling/planning, then we achieve better cost economics and backend optionality than a monolithic speech-to-speech model, because the chit-chat and prosody load is economically wasteful to run through a frontier multimodal model, and users want to swap backend intelligence independently of the voice interface.

## What they did

Neil Zeghidour (co-founder/CEO, Gradium, formerly research; created Moshi—first full-duplex speech-to-speech model, Hibiki—real-time speech-to-speech translation, first on-device TTS) traced voice agent evolution from constrained NLU pipelines (Siri 2011) through open-ended LLM chat (original OpenAI voice mode) to current agentic voice. He argued that pure speech-to-speech scaling (OpenAI's path) has two problems: (1) extremely expensive/slow to advance (GPT-4o still powered Advanced Voice Mode through multiple text model generations), (2) adding audio modality to a text model costs intelligence capacity. Gradium's path (Moushiraq paper, also used by Thinking Machine Interaction models): split into a small full-duplex voice interface model (can run on-device) that handles naturalness and knows when it doesn't know, delegating to a background text LLM for all reasoning/tool-calling. Advantages: cost (don't run frontier models for chit-chat), optionality (swap backend LLM freely, e.g., upgrade when GPT-5 drops without retraining voice model).

## Relevance to YOLO loop

The delegation pattern—a lightweight interface model that knows its limits and hands off to a powerful background model—generalizes beyond voice to any multi-tier agent architecture. The key design question this raises for our loop: where are we using frontier models for tasks a lighter model could handle, and do we have clean delegation interfaces?

## Notes

Gradium's models available at gradium.ai. The Moushiraq paper is the key reference for the hybrid architecture. The economic argument (don't run GPT-class models for chit-chat) applies directly to our agent cost analysis.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-15 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-15-hybrid-speech-to-speech-architecture` |
| Channel | aie |
| Video | [Your Voice Agent is Just a Walkie Talkie — Neil Zeghidour, Gradium](https://www.youtube.com/watch?v=a8EcVumh71E) |
| Published | 2026-09-15 |
| Ingested upstream | 2026-09-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
