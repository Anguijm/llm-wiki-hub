# Build a signal-ingestion-to-PR pipeline that converts product observability events into auto-generated code fixes

> Back to [[experiments-index]]

Source: **[Self Driving Products: Product Signals to Pull Requests — Joshua Snyder, PostHog](https://www.youtube.com/watch?v=zMiSRliEzv4)** · aie · 2026-06-11

**Status:** `discarded` · **Verdict:** `discard` · **Effort:** `high`

---

## Hypothesis

If we build a pipeline that ingests product signals (errors, session replays, analytics anomalies), groups them into weighted reports via semantic+keyword clustering, runs a research agent to identify the root cause and relevant repo files, then invokes an agentic coding step to generate a PR, then the time from problem detection to reviewable fix will drop from days to minutes because agents can execute all intermediate research and implementation steps autonomously.

## What they did

Josh Snyder from PostHog described their in-development 'self-driving product' pipeline. Architecture: (1) Ingest trillions of events/month, run an LLM safety classifier to drop malicious injections, normalize signals to a standard schema with source/type/content/weight/embedding fields. (2) Group signals into reports by combining semantic embeddings with structural normalization (pure embedding clustering failed due to format heterogeneity across error traces, session replays, and experiment results). (3) When a report's cumulative weight exceeds a threshold, promote it and spawn a research agent to identify the specific bug and relevant repo location. (4) Assess actionability — if the problem description is too vague, discard rather than generate a noisy PR. (5) Execute a code agent to write and iterate on a PR until CI is green. Key lessons: evaluate on representative data not toy examples; embed normalized content not raw mixed-format signals; ensure problem specificity before invoking the code agent; treat early token cost concerns as premature — run agents liberally during experimentation to discover repeatable patterns, then replace expensive steps with one-shot LLM calls.

## Relevance to YOLO loop

The signal-grouping and actionability-gating patterns are directly applicable to our YOLO loop's issue triage step. The lesson about not gating on token cost during experimentation, then optimizing hot paths after patterns emerge, is a concrete process improvement for how we build new loop stages.

## Notes

Backlog triage 2026-06-24 (owner-preference model). Product-telemetry -> auto-PR pipeline — needs product signals the loop doesn't have; high effort.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-11 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-06-11-posthog-signal-to-pr-pipeline` |
| Channel | aie |
| Video | [Self Driving Products: Product Signals to Pull Requests — Joshua Snyder, PostHog](https://www.youtube.com/watch?v=zMiSRliEzv4) |
| Published | 2026-06-11 |
| Ingested upstream | 2026-06-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
