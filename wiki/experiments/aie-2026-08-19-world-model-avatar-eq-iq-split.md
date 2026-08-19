# Architect Photorealistic Avatars with Separate EQ (Expression/Embodiment) and IQ (Reasoning/Tool-Use) Models

> Back to [[experiments-index]]

Source: **[Voice agents with Realtime Video — Sidney Primas, LemonSlice](https://www.youtube.com/watch?v=z1dqv74SpUs)** · aie · 2026-08-19

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we separate the avatar's emotional/embodiment layer (EQ model trained on human world model) from the reasoning/tool-calling layer (IQ model), then we get emergent realistic physical behaviors (micro-expressions, physics, object interactions) from the EQ model while preserving full LLM reasoning capabilities in the IQ model, because world-model-based EQ models get physical realism for free as an emergent property while specialized reasoning models can be swapped or upgraded independently.

## What they did

LemonSlice builds photorealistic video avatars using world models focused on humans rather than the stitching/warping approach used by most avatar companies. A single image generates the avatar. Their current architecture drives the avatar with a combined pipeline; their stated roadmap is to split into an EQ model (world-model-grounded, handles all embodiment, emotion, micro-expressions, physics) that receives signals from an IQ model (handles tool calling, deep reasoning, language). They demonstrated full-body avatar with physics (earring movement, water), real-time scene and clothing changes, and a deployed installation where Trump interacted with a Teddy Roosevelt avatar for 10 minutes. They argue most AI-human interaction will have a visual layer long-term.

## Relevance to YOLO loop

The EQ/IQ architectural split is a useful mental model for any agent that needs both physical/social realism and reasoning. For our loop, it suggests evaluating whether our agents need a separate 'presentation' layer from their 'reasoning' layer, especially as voice and video interfaces become part of our deployment targets.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-19 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-19-world-model-avatar-eq-iq-split` |
| Channel | aie |
| Video | [Voice agents with Realtime Video — Sidney Primas, LemonSlice](https://www.youtube.com/watch?v=z1dqv74SpUs) |
| Published | 2026-08-19 |
| Ingested upstream | 2026-08-19 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
