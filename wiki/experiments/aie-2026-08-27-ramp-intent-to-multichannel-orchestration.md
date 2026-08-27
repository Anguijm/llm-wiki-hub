# Build vertical single-channel agent automations first, then compose them into multi-channel orchestration

> Back to [[experiments-index]]

Source: **[The Building Blocks of GTM Orchestration — Arman Vaziri, Ramp](https://www.youtube.com/watch?v=VjEP0xqTUI0)** · aie · 2026-08-27

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we build deep, reliable agent automations for individual GTM channels (outbound copy, web landing pages, in-app notifications) as independent vertical solutions before attempting cross-channel orchestration, then composing them into intent-driven campaigns will be faster and more reliable, because Ramp's engineering team found that vertical builds are the prerequisite foundation for federated multi-channel distribution.

## What they did

Speaker (Ramp PLG engineering lead) described a bottom-up architecture for GTM orchestration starting with a consistent internal CDP as data foundation, then building vertical agent solutions per channel (SDR sequences, paid ad creative, web pages, in-app nudges), and finally composing these into an orchestration layer that takes a natural language intent description and distributes it across channels simultaneously. He emphasized solving real specific problems first rather than building a complex system architecture upfront.

## Relevance to YOLO loop

The vertical-first composition pattern applies to our agent loop architecture. Rather than building a unified agent from scratch, we should build reliable single-task agents (PR writer, test runner, doc updater) and then build an orchestration layer that routes intent to the right specialist agent.

## Notes

Multi-armed bandit framing for campaign selection is interesting — agents can balance exploration of new approaches vs. exploitation of known-good patterns.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-27 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-27-ramp-intent-to-multichannel-orchestration` |
| Channel | aie |
| Video | [The Building Blocks of GTM Orchestration — Arman Vaziri, Ramp](https://www.youtube.com/watch?v=VjEP0xqTUI0) |
| Published | 2026-08-27 |
| Ingested upstream | 2026-08-27 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
