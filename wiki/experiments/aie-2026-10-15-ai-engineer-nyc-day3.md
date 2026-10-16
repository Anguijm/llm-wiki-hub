# Apply Ramp's 'bitter lesson' unit-economics tracking to agent workflow cost management

> Back to [[experiments-index]]

Source: **[AI Engineer NYC: OpenAI, Blackstone, Ramp, Coinbase, Apollo, Citadel, Basis, Runway, Compute Trading](https://www.youtube.com/watch?v=jiUC6IUMdvc)** · aie · 2026-10-15

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we track token spend per workflow feature on a unit-economics basis (cost per successful outcome) rather than total spend, then we can identify which agent capabilities are getting cheaper as frontier models improve and reallocate effort to the capabilities that remain expensive, because Ramp found top features growing in token volume but shrinking in unit cost as newer cheaper-faster-better models ship.

## What they did

Alex from Ramp presented 'chasing capabilities while waiting for the frontier.' He described Ramp as a 'bitter lesson build company' — over the last year, LLM use cases increased 123% while unit economics on top features improved because new frontier models are cheaper, faster, and better. He contrasted the 2023 agent-building experience (strict guardrails needed, prompt synonyms changed behavior, context had to be minimized) with the current environment where models are RL-trained to generalize and backtrack. The key argument for maintaining an applied research function inside an application-layer company: you can't wait for the next frontier model because you need to ship now, and understanding current capability gaps is what lets you design the right workarounds that become obsolete gracefully.

## Relevance to YOLO loop

high: unit-economics thinking for agent workflow costs directly applies to how we decide where to invest in harness complexity versus waiting for the frontier to advance.

## Notes

Conference livestream — many speakers, only the Ramp talk yielded a tight actionable experiment. Runway world-simulation content may be relevant to mini-forge/3D pipelines but was too truncated to extract a concrete experiment.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-15 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-15-ai-engineer-nyc-day3` |
| Channel | aie |
| Video | [AI Engineer NYC: OpenAI, Blackstone, Ramp, Coinbase, Apollo, Citadel, Basis, Runway, Compute Trading](https://www.youtube.com/watch?v=jiUC6IUMdvc) |
| Published | 2026-10-15 |
| Ingested upstream | 2026-10-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
