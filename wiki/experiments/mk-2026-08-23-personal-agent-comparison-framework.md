# Evaluate Personal Agent Platforms Against a Shared Capability Matrix Before Switching

> Back to [[experiments-index]]

Source: **[Ranking Every Personal AI Agent in 18 Minutes](https://www.youtube.com/watch?v=aBdMey9nqcM)** · mk · 2026-08-23

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we assess candidate agent platforms against a fixed capability checklist (always-on execution, persistent files/memory, scheduled routines, local device reach, reusable skills, model routing, browser/web, app connectors, messaging channels, operator ownership) rather than reacting to viral launches, then we will make fewer costly platform switches and extract more leverage from our current setup, because all major platforms share the same core primitives and switching cost exceeds marginal capability gains in most cases.

## What they did

Mark compared Grockbot, Hermes Agent, Claude Co-work, ChatD Work, and OpenClaw across two ranking axes: turnkey ease-of-use (Grockbot wins) vs. transparency/extensibility/model routing freedom (build-your-own wins, then Hermes). He produced a capability matrix showing that all platforms share the same functional elements and differ only on configurability, model swappability, and operator ownership. He also flagged that Grockbot locks users to Grok models, while Hermes allows any model per agent. His key takeaway: stop chasing the new thing; instead invest in getting leverage over whichever setup you choose, and only switch when a specific capability gap in the matrix actually blocks your use case.

## Relevance to YOLO loop

Relevant to our agent infrastructure decisions in the dev loop — before adopting a new orchestration layer or agent runtime, run it through the capability matrix to confirm it closes a real gap vs. our current setup rather than just providing novelty. Helps us avoid thrash when new agent platforms launch.

## Notes

Mark's capability matrix (always-on execution, files/memory, scheduled routines, local device reach, reusable skills, model routing, browser/web, app connectors, messaging channels, operator ownership) is worth formalizing as a standing evaluation rubric. He also raised a credible hypothesis about platform-algorithm symbiosis inflating viral signals for Grockbot on X — useful reminder to weight benchmark evidence over social proof when evaluating agent tools.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-23 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mk-2026-08-23-personal-agent-comparison-framework` |
| Channel | mk |
| Video | [Ranking Every Personal AI Agent in 18 Minutes](https://www.youtube.com/watch?v=aBdMey9nqcM) |
| Published | 2026-08-23 |
| Ingested upstream | 2026-08-23 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
