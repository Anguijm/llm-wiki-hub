# Benchmark Claude Fable 5.1 cost-per-task against Fable 5 on real agentic workloads

> Back to [[experiments-index]]

Source: **[Fable 5.1 Just Dropped. It Looks Unreal.](https://www.youtube.com/watch?v=8IyORt-7rOQ)** · nh · 2026-09-01

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we replace Fable 5 with Fable 5.1 in our agentic pipelines, then we will see 25-50% cost reduction per workflow because cache-read pricing is reduced and the model completes tasks with fewer tokens.

## What they did

Nate ran the same prompt (build a rotating 3D cartoon bear riding a bike) on Fable 5 and Fable 5.1 side by side using the /cost and /usage slash commands in the Claude desktop app. Fable 5.1 cost $4.53 vs Fable 5's $5.41 for the same task — roughly $1 cheaper on a trivial example. Anthropic claims 25% savings on typical workflows and up to 50% on highly agentic work due to reduced cache-read pricing.

## Relevance to YOLO loop

Any pipeline using Claude as the primary reasoning model should swap to Fable 5.1 and re-run cost benchmarks. The /usage command pattern is a useful harness addition for automated cost tracking in the YOLO loop.

## Notes

Same input/output pricing ($10/$50 per million tokens) but cache reads are cheaper. EFS enterprise privacy option also noted. Mythos 5.1 variant available for cybersecurity/life sciences verified orgs.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-01 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-09-01-claude-fable-51-cost-benchmark` |
| Channel | nh |
| Video | [Fable 5.1 Just Dropped. It Looks Unreal.](https://www.youtube.com/watch?v=8IyORt-7rOQ) |
| Published | 2026-09-01 |
| Ingested upstream | 2026-09-01 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
