# Replace monolithic system prompts with a four-layer assembled prompt stack (identity → conditions → voice → veto)

> Back to [[experiments-index]]

Source: **[Stop Writing Tone Instructions. Layer Them. - Isadora Martin-Dye, Isadora & Co](https://www.youtube.com/watch?v=ij-AU9dpJjc)** · aie · 2026-06-26

**Status:** `adopted` · **Verdict:** `adopt` · **Effort:** `medium`

---

## Hypothesis

If we decompose a single system prompt into four ordered layers — immutable hard rules, real-time situational conditions, example-anchored style, and a deterministic post-generation veto — then agent output reliability improves beyond turn 21 edge cases because each layer does exactly one job and the final layer converts probabilistic instructions into deterministic permission.

## What they did

Isadora built AI agents for her 225-year-old wedding venue and then generalized the architecture to other venues, a personal companion app, and a missing-persons utility. After watching brand voice failures at scale with 24 scattered system prompts, she consolidated to a single assembly function with four load-bearing layers: Layer 1 — immutable identity rules that cannot be overridden by any downstream config (e.g., always disclose AI status before being asked); Layer 2 — situational mode derived from real-time user state; Layer 3 — example-anchored voice/tone (where most teams start and stop); Layer 4 — a post-generation veto using deterministic regex/pattern matching that either allows or blocks output before it leaves the system. She used a Google Maps routing metaphor: destination fixed, route variable, roadworks checked before departure. She also identified a critical multi-tenant failure: defaulting brand identity silently caused all venues to ship as the same identity (sage@hawthornemanner.com), so she made missing brand identity a hard crash rather than a fallback.

## Relevance to YOLO loop

YOLO loop system prompts are currently monolithic. The four-layer pattern would make hard safety rails (Layer 1) immune to drift from context injection, let loop stage conditions (Layer 2) adjust behavior per task type, and add a cheap deterministic gate (Layer 4) before any output is committed — directly reducing hallucinated or off-brand code commits.

## Notes

Key insight: Layer 4 (veto) is systems engineering, not prompt engineering — deterministic not probabilistic. Her stated regret: veto should be a shared service, not wired individually into each surface. In a loop context this maps to a middleware gate on all agent outputs.

Backlog triage 2026-06-27 (owner-preference model). Layered prompt architecture (identity/conditions/voice/veto) — prompt-design discipline + a deterministic post-gen veto; good fit.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-26 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-06-26-four-layer-prompt-stack` |
| Channel | aie |
| Video | [Stop Writing Tone Instructions. Layer Them. - Isadora Martin-Dye, Isadora & Co](https://www.youtube.com/watch?v=ij-AU9dpJjc) |
| Published | 2026-06-26 |
| Ingested upstream | 2026-06-26 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
