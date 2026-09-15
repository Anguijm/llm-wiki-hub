# Audit voice agent pipeline against a six-component linguistic framework (sounds/words/interaction × listen/speak) to find failure layers

> Back to [[experiments-index]]

Source: **["My name is... my name is...": A Linguistic Map for Voice Agents — Midam Kim, ServiceNow](https://www.youtube.com/watch?v=IDNfAZVKvPE)** · aie · 2026-09-15

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we systematically evaluate our voice agent against the six-component linguistic framework (listen: sounds/ASR, words/NLU, interaction/turn-taking, mental model; speak: pronunciation/TTS, vocabulary, timing, context), then we will surface specific interdependent failure layers that cross-component optimization misses, because voice AI failures cascade across components and the user's mental model—not any single transcript—is what determines satisfaction.

## What they did

Midam Kim (ML engineer and speech communication researcher, ServiceNow) introduced a linguistic framework for diagnosing voice AI failures structured as a joint-activity model between bot and user, with two channels (listen/speak) each containing four layers: sounds, words, interaction, and mental model. She walked through her own failed call experience—STT confusing M/N, TTS mispronouncing her name as 'Madam', premature barge-in cutting off her account number, no interactive clarification—and mapped each failure to a specific framework node. Key insight: all components are interdependent, not independent; the user's mental model (which persists after all audio vanishes) is the actual target to optimize. She also flagged that systems must adapt dynamically per user type (kids, non-native speakers, upset users) and across the call timeline. ServiceNow's Eva Bench was mentioned as an end-to-end benchmark.

## Relevance to YOLO loop

If our loop includes any voice interface or voice agent evaluation, this framework gives a structured audit checklist. Even for text agents, the mental-model-as-primary-target framing applies: what does the user believe the agent knows/understood, and is that belief accurate? Use as an eval rubric.

## Notes

Eva Bench (ServiceNow) mentioned as a free diagnostic tool for voice agents. The dynamic/timeline aspect is the hardest to implement—start with static per-layer audit.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-15 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-15-linguistic-framework-voice-agent` |
| Channel | aie |
| Video | ["My name is... my name is...": A Linguistic Map for Voice Agents — Midam Kim, ServiceNow](https://www.youtube.com/watch?v=IDNfAZVKvPE) |
| Published | 2026-09-15 |
| Ingested upstream | 2026-09-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
