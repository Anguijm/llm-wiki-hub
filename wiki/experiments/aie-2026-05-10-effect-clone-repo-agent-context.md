# Feed the full library repo as agent context instead of relying on training data or MCP docs

> Back to [[experiments-index]]

Source: **[Vibe Engineering Effect Apps — Michael Arnaldi, Effectful](https://www.youtube.com/watch?v=Wmp2Tku2PrI)** · aiDotEngineer · 2026-05-10

**Status:** `done` · **Verdict:** `adopt` · **Effort:** `low`

---

## Hypothesis

If we give a coding agent direct access to the full source repository of an underdocumented library (via clone + context injection) rather than relying on the model's training-time knowledge or MCP documentation servers, then the agent produces correct, idiomatic library usage, because the model can read actual patterns, types, and examples directly from source rather than hallucinating from stale or absent training data.

## What they did

Michael Arnaldi ran a live unprepared workshop building a working Effect.ts TypeScript API from scratch using an LLM agent. He argued that LLMs freeze at pretraining and cannot update their knowledge daily, so for niche or rapidly-evolving libraries (like Effect v4, which lacks broad online documentation), the correct strategy is to clone the repo and inject it into the agent's context window. He built a complete todo API with typed services, layers, HTTP routing, and error handling purely through agent interaction, never writing code by hand, starting from an empty repository. He noted this approach works across TypeScript and Rust for library-level code.

## Relevance to YOLO loop

The YOLO loop itself uses libraries and frameworks that may be newer than model training cutoffs. Cloning dependency repos into agent context is a zero-infrastructure technique that immediately improves code generation accuracy for any cutting-edge dependency, and can be applied as a standard YOLO loop preparation step.

## Outcome

Scaffolded in experiments/effect-clone-repo-agent-context/ (PR #10): bundle_repo.py produces an 8K-token-capped markdown bundle (overview + changed files + heuristic related files); demo run on PR #8's diff yields a 2.9K-token sample_bundle.md (under cap); quality_protocol.md is the 5-PR manual A/B recipe for a follow-on tick.

## Notes

Speaker used ~1.5 hours to build a working typed API from scratch with zero prior preparation. Key insight: treat LLMs as fixed-knowledge machines requiring explicit context injection, not live learners. Effect workflows (for long-running AI processes) flagged as high-value follow-on experiment.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-05-10 | `backlog` | Extracted from YouTube RSS |
| 2026-05-15 | `done` | Scaffold deliverables shipped in PR #10; promoted via PR #11 (tick_queue_approved). Status flipped post-merge since deliverables already on main. |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-05-10-effect-clone-repo-agent-context` |
| Channel | aiDotEngineer |
| Video | [Vibe Engineering Effect Apps — Michael Arnaldi, Effectful](https://www.youtube.com/watch?v=Wmp2Tku2PrI) |
| Published | 2026-05-10 |
| Ingested upstream | 2026-05-10 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
