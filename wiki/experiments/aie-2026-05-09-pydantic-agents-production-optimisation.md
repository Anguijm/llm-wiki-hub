# Use Pydantic AI structured outputs to enforce agent response contracts in production

> Back to [[experiments-index]]

Source: **[Playground in Prod: Optimising Agents in Production Environments — Samuel Colvin, Pydantic](https://www.youtube.com/watch?v=A48uhxfxbsM)** · aiDotEngineer · 2026-05-09

**Status:** `done` · **Verdict:** `adopt` · **Effort:** `medium`

---

## Hypothesis

If we enforce Pydantic schema validation on all agent outputs in production, then downstream parsing errors and silent failures will decrease because typed contracts catch malformed responses before they propagate through the pipeline.

## What they did

Speaker from Pydantic described how to move agent prototypes into production by applying structured output validation, runtime type checking, and optimization patterns using the Pydantic AI framework.

## Relevance to YOLO loop

Directly applicable: adding Pydantic models to our Claude Code tool outputs would catch schema drift early and make the loop more robust to model output variation.

## Outcome

Scaffolded in experiments/pydantic-agents-production-optimisation/ (PR #10): verdict_schema.py defines Pydantic models for per-angle Verdicts; parse_with_pydantic.py wraps the parse path and returns structured ParseError instead of phantom OBJECT (--demo passes for 3 valid + 3 distinguishable errors); comparison_protocol.md is the A/B replay recipe for a follow-on rollout tick.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-05-09 | `backlog` | Extracted from YouTube RSS |
| 2026-05-15 | `done` | Scaffold deliverables shipped in PR #10; promoted via PR #11 (tick_queue_approved). Status flipped post-merge since deliverables already on main. |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-05-09-pydantic-agents-production-optimisation` |
| Channel | aiDotEngineer |
| Video | [Playground in Prod: Optimising Agents in Production Environments — Samuel Colvin, Pydantic](https://www.youtube.com/watch?v=A48uhxfxbsM) |
| Published | 2026-05-09 |
| Ingested upstream | 2026-05-09 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
