# Implement an automated offline-online agent improvement loop: spec → build → eval → ship → diagnose → optimize

> Back to [[experiments-index]]

Source: **[The Agentic AI Engineer - Benedikt Sanftl, Mutagent](https://www.youtube.com/watch?v=pSto5YaNGUo)** · aie · 2026-06-29

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we close the agent development loop with automated diagnostics (trace sampling → root cause analysis → mutation generation → re-evaluation) rather than manual review, then we can run more improvement cycles in the same time window and scale agent quality improvements across many agents simultaneously, because the human bottleneck in manual trace review is the primary constraint on improvement throughput.

## What they did

Benedikt Sanftl and Burak (Mutagent) presented a two-loop architecture: offline loop (spec → build → eval → ship) and online loop (monitor → diagnose → optimize → re-eval → redeploy). The key innovation is automating the online loop: a diagnostics agent ingests traces from observability platforms (LangFuse, JSON-L exports), applies multi-tier sampling to select representative failure traces, runs structured root cause analysis, categorizes failure modes by frequency, generates specific mutations/fixes, and outputs a markdown task definition for the coding agent to apply. They demoed the diagnostics agent producing an HTML artifact showing detected failure modes, recursive why-chains, assumptions (flagged for human correction), and multi-choice remedies. Final decisions feed directly back to the coding agent.

## Relevance to YOLO loop

This is a meta-improvement layer on top of our YOLO loop: rather than manually reviewing traces when something breaks, an agent reviews our agent's traces and generates the fix spec. Implementing even the offline half (spec → eval with clear success criteria) would dramatically improve our ability to validate agent behavior before shipping.

## Notes

Mutagent is available for early access. Start with the offline loop (spec-driven development with explicit success criteria and evals) before attempting the online automated diagnostics loop. The diagnostics agent's assumptions block is critical — it surfaces where the LLM made incorrect inferences about the codebase due to lack of code access.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-29 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-06-29-agentic-engineer-spec-eval-loop` |
| Channel | aie |
| Video | [The Agentic AI Engineer - Benedikt Sanftl, Mutagent](https://www.youtube.com/watch?v=pSto5YaNGUo) |
| Published | 2026-06-29 |
| Ingested upstream | 2026-06-29 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
