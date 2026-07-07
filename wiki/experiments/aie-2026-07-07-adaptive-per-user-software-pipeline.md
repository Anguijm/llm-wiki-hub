# Prototype a live-session code adaptation layer that modifies UI behavior per user context without a build step

> Back to [[experiments-index]]

Source: **[The Pipeline Is Dead - Iris ten Teije, Sky Valley Ambient Computing](https://www.youtube.com/watch?v=bRnoEpoK5m4)** · aie · 2026-07-07

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we implement a thin runtime adaptation layer that uses an LLM to generate and apply small scoped code changes in a user's live session (rather than pre-built frozen artifacts), then we can deliver meaningfully personalized software behavior without forking the codebase, because the cost of producing a correct scoped change has collapsed to near-zero with coding agents, removing the economic constraint that made one-version-for-all the only viable option.

## What they did

Iris (co-founder of Differ) argued that the entire CI/CD pipeline stack was built around one assumption — that producing software changes was expensive and rare, so freezing a single artifact for all users was the only viable shape. She asserted that as LLM-driven code generation collapses production cost toward zero and can happen at runtime (server, client, or live session), the separation between development and distribution dissolves. She described Differ's system which observes user behavior signals, generates targeted code adaptations, and applies them — with multi-layer verification covering observability (was the right signal used?), correctness (does the change work?), desirability (did it improve the goal metric?), and coordination (how do intent/outcome updates propagate across diverged versions). She emphasized that generation is the easy 80%; the hard problems are validation, provenance, and coordinating diverged versions by merging intent/outcome rather than merging code commits.

## Relevance to YOLO loop

Conceptually relevant as a long-horizon architectural direction: our loop could evolve toward generating environment-specific tool or prompt adaptations at runtime rather than shipping fixed versions. Near-term actionable extract: the verification stack (signal attribution, correctness check, desirability measurement, coordination) is a useful mental model for evaluating any auto-generated change in our loop.

## Notes

This is more of an architectural thesis than a step-by-step recipe. The near-term experiment worth attempting is a minimal version: use an agent to generate a small scoped UI/config change based on observed usage patterns, validate it with a lightweight correctness check, and apply it without a full redeploy. Iris's framing of 'merge intent, not code' is a useful design principle for our own agent coordination.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-07 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-07-adaptive-per-user-software-pipeline` |
| Channel | aie |
| Video | [The Pipeline Is Dead - Iris ten Teije, Sky Valley Ambient Computing](https://www.youtube.com/watch?v=bRnoEpoK5m4) |
| Published | 2026-07-07 |
| Ingested upstream | 2026-07-07 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
