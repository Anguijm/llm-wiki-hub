# Trial Hermes Agent on local llama.cpp with provider hot-swap

> Back to [[experiments-index]]

Source: **[AI Labs Will Trap You or Replace You - Dillon Rolnick, Nous Research](https://www.youtube.com/watch?v=Sg6vtKOAOQ0)** · aie · 2026-11-04

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we run the open-source Hermes Agent against the llama.cpp server on the Strix Halo box and then swap the inference provider to a hosted model on the same small task, then we learn how much of an ops-style agent task works without a closed vendor because Hermes is built to hot-swap providers without lock-in.

## What they did

Rolnick argued enterprises should anchor on open-source agent frameworks where they keep ownership of data, execution logic and model switching. He presented Hermes Agent as one that lets you swap the underlying inference provider, and said Nous replicated the Grokbot interface in it over a weekend. He also described architectures that combine deterministic code with non-deterministic model reasoning.

## Relevance to YOLO loop

medium: A provider-portable agent framework is a different harness choice from the review, gating and loop practices already in place, but the video gives little evidence on quality.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-11-07 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-11-04-hermes-agent-local-provider-swap` |
| Channel | aie |
| Video | [AI Labs Will Trap You or Replace You - Dillon Rolnick, Nous Research](https://www.youtube.com/watch?v=Sg6vtKOAOQ0) |
| Published | 2026-11-04 |
| Ingested upstream | 2026-11-07 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
