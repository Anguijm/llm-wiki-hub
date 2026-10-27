# Prototype a scheduled trace-sweep agent that opens fix PRs

> Back to [[experiments-index]]

Source: **[What Does an AI Engineer Do Now? - Aparna Dhinakaran, Arize AI](https://www.youtube.com/watch?v=ImnZ7s68jw8)** · aie · 2026-10-25

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we run a scheduled background agent in an ephemeral sandbox that sweeps our agent session logs for recurring failures and opens PRs with fixes, then recurring harness issues get fixed with less manual triage because the agent compares findings against persistent memory and does not restart from scratch each run.

## What they did

Aparna Dhinakaran described Arize Signal, an always-on agent. It is woken by event triggers (Slack alerts, user complaints) or a cron schedule every 3 to 6 hours. It runs in an ephemeral sandbox with repo access, APM metrics and a single ingress/egress proxy. It sweeps production traces for recurring failures, checks them against persistent external memory, and submits PRs with fixes and tests using Claude Code, Cursor or Codex harnesses. Sandbox credentials are torn down afterwards while telemetry and discovered issues are kept. She also stressed building golden-truth datasets to evaluate the evaluators.

## Relevance to YOLO loop

high: Directly applicable to YOLO loop design, covering a scheduled agent with durable memory, sandboxing and an automated verify-then-PR cycle.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-26 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-25-trace-sweep-fix-agent` |
| Channel | aie |
| Video | [What Does an AI Engineer Do Now? - Aparna Dhinakaran, Arize AI](https://www.youtube.com/watch?v=ImnZ7s68jw8) |
| Published | 2026-10-25 |
| Ingested upstream | 2026-10-26 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
