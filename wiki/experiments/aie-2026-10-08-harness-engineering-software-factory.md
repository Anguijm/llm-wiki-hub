# Track Autonomy and Automation Separately as Leading Indicators on the Path to a Software Factory

> Back to [[experiments-index]]

Source: **[Harness Engineering: How to Build a Software Factory — Dru Knox, Tessl](https://www.youtube.com/watch?v=X6l4lpA0_NY)** · aie · 2026-10-08

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we separately measure agent autonomy (how often agents complete tasks without human correction) and automation (how much of the workflow runs without human review) rather than conflating them into a single 'AI usage' metric, then we will get a clearer picture of where trust bottlenecks actually are because a team can have high autonomy (agents one-shot tasks correctly) but low automation (humans still manually review everything) and the fix for each is different.

## What they did

Tessl's Drew Knox defined harness engineering as the core discipline for building toward a software factory—an agentic system where agents produce all shipped code and engineers focus on improving the factory. He distinguished three metrics: autonomy (frequency of human corrections needed), automation (how much runs without human review), and quality (output quality for end users). He argued these must be improved in order: build autonomy first, then layer on automation, while holding quality constant. He described harness engineering as the practice of building the control plane—skills registries (versioned, governed workflows), improvement loops (weekly automated scans for flaky tests, code duplication, security vulnerabilities, architecture quality), and agentic code review standards. Key tactical elements: mine PRs and issues to find repeated manual tasks and convert them into automated skills one at a time; use sandboxed agent runs with GitHub tokens to open PRs and respond to review comments autonomously; measure progress by tracking reduction in manual takeovers, reduction in human PR comments, and increase in agent-initiated PRs.

## Relevance to YOLO loop

The autonomy/automation distinction is immediately applicable to how we assess our YOLO loop's maturity. The concrete metrics (manual takeover rate, human PR comment rate, agent-initiated PR rate) give us a dashboard to build. The 'mine PRs to find repeated tasks, automate one at a time' approach is a low-risk incremental strategy we can start this week.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-08 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-08-harness-engineering-software-factory` |
| Channel | aie |
| Video | [Harness Engineering: How to Build a Software Factory — Dru Knox, Tessl](https://www.youtube.com/watch?v=X6l4lpA0_NY) |
| Published | 2026-10-08 |
| Ingested upstream | 2026-10-08 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
