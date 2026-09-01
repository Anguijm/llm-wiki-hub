# Implement a three-phase discovery-research-response loop for agents handling fuzzy user intent

> Back to [[experiments-index]]

Source: **[Multimodal Collaborative Agents for Next-Gen Commerce — Nidhi Kaushik Vyas, Google DeepMind](https://www.youtube.com/watch?v=AhQpRalYlyg)** · aie · 2026-09-01

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we structure an agent's interaction pipeline as (1) discovery with working-state extraction, (2) multimodal preference elicitation with background research, and (3) adaptive response formatting, then task completion rates on open-ended queries will improve because the agent handles articulation gap rather than assuming the user has well-formed intent.

## What they did

Nidhi described Google DeepMind's framework for commerce agents dealing with fuzzy intent. Phase 1 (Discovery): agent builds a working state from session history, personal context, reference images/links, hard constraints, and soft constraints — then develops a collaborative elicitation strategy. Phase 2 (Research): agent selects elicitation modality (text vs. visual inspiration boards vs. comparison tables) based on what will reveal preferences fastest, then does background heavy-lifting (comparisons, trade-offs, summarization) without burdening the user. Phase 3 (Response): agent adapts output format to the query — bulleted lists, comparison tables, or visual boards as appropriate. Auto-raters are deployed at every loop step and evolve with the system. Key insight: visual elicitation reveals preferences faster than text because it gives agent and user a common language.

## Relevance to YOLO loop

The three-phase loop pattern applies to any YOLO loop agent that receives open-ended requests (spec gathering, requirements clarification, research tasks). The working-state extraction pattern (hard constraints vs. soft constraints from context) and the auto-rater-per-step evaluation design are directly implementable.

## Notes

Nidhi's four takeaways: (1) design for fuzzy/vibe input, (2) show and ask rather than only text-elicit, (3) shape the answer format as part of the intelligence, (4) build auto-raters that grow with the system. UCP (Universal Commerce Protocol) mentioned as the agent-merchant interface standard Google has launched.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-01 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-01-multimodal-fuzzy-intent-shopping-loop` |
| Channel | aie |
| Video | [Multimodal Collaborative Agents for Next-Gen Commerce — Nidhi Kaushik Vyas, Google DeepMind](https://www.youtube.com/watch?v=AhQpRalYlyg) |
| Published | 2026-09-01 |
| Ingested upstream | 2026-09-01 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
