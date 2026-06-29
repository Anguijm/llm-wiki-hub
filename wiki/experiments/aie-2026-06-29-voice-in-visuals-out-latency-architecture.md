# Build a voice-in / visuals-out agent using a fast small model for real-time response with async handoff to a larger model

> Back to [[experiments-index]]

Source: **[Voice In, Visuals Out: The Agony and the Ecstasy - Allen Pike, Forestwalk Labs](https://www.youtube.com/watch?v=65X0pQ6Lmbg)** · aie · 2026-06-29

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we pair a latency-optimized small model (Haiku-class, P95 < 1s) as the real-time response layer with asynchronous handoff to a larger reasoning model for heavy tasks, and use aggressive prefix caching (first 90% of context identical across requests) with eager inference at 1-2 second voice intervals, then we can achieve sub-1-second visual response to voice input while still accessing frontier reasoning quality for complex subtasks, because the visual response envelope is more forgiving than voice-out and prefix caching dramatically reduces per-turn latency and cost.

## What they did

Allen Pike (Forestwalk Labs) described building voice-in / visuals-out meeting agents at Forestwalk. Key findings: GPT-5 mini had P95 latency of 5,000-10,000ms despite being small — inference platform latency prioritization matters as much as model size. Haiku-class models consistently met sub-1s targets. The architecture uses: (a) a fast small model listening continuously and responding to voice in real-time with visual output, (b) eager inference every 1-2 seconds as the user speaks rather than waiting for silence, (c) async handoff to a larger model for heavier work with the real-time model interleaving responses, (d) prefix caching with the first ~90% of context kept identical across turns for up to 90% cost/latency reduction, (e) minimizing output tokens per turn.

## Relevance to YOLO loop

Applicable if we add voice interaction to our dev loop (e.g. voice-driven task filing during standups or pair programming sessions). The prefix-caching architecture pattern and the fast-model-with-async-handoff pattern are independently useful for any high-frequency agent interaction pattern in our loop.

## Notes

Inference platform choice matters as much as model size — benchmark actual P95 latency, not just model parameter count. Target: first ~90% of context window identical across requests for maximum prefix cache hit rate. The 200ms threshold is for full-duplex voice conversation; visuals-out relaxes this to ~1000ms which is achievable today.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-29 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-06-29-voice-in-visuals-out-latency-architecture` |
| Channel | aie |
| Video | [Voice In, Visuals Out: The Agony and the Ecstasy - Allen Pike, Forestwalk Labs](https://www.youtube.com/watch?v=65X0pQ6Lmbg) |
| Published | 2026-06-29 |
| Ingested upstream | 2026-06-29 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
