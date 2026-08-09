# Build with Hundreds of Concurrent Inference Calls as a Core Architectural Primitive

> Back to [[experiments-index]]

Source: **[The New Primitives: Building AI Native Software — Kwindla Kramer, Daily](https://www.youtube.com/watch?v=LZuWZRze3MU)** · aie · 2026-08-09

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If applications are designed from the ground up with LLMs as the core of every interaction—not as an add-on—and architect for hundreds of simultaneous inference calls, then qualitatively new user experiences become possible that could not be approximated by inserting AI into existing software patterns.

## What they did

Kwindla Kramer described building Gradient Bang, a multiplayer game architected from scratch around LLMs at every interaction layer. It uses hundreds of simultaneous inference calls and demonstrates patterns including asynchronous non-blocking context compression, long-running sub-agents sharing context, progressive skills loading, dynamic UI generation, and conversational voice. He framed this as the transition from 'agents' to 'AI native software'—analogous to going from web pages to full web applications—and argued that building these systems is how the field will discover what to build next.

## Relevance to YOLO loop

Pushes the YOLO loop toward thinking about AI not just as a code-generation assistant but as a runtime architectural component—informing how we design systems that will themselves be powered by many concurrent inference calls, and what our loop needs to validate about those systems.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-09 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-09-ai-native-primitives` |
| Channel | aie |
| Video | [The New Primitives: Building AI Native Software — Kwindla Kramer, Daily](https://www.youtube.com/watch?v=LZuWZRze3MU) |
| Published | 2026-08-09 |
| Ingested upstream | 2026-08-09 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
