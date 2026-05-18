# Implement retry logic, state persistence, and failure observability in production agents

> Back to [[experiments-index]]

Source: **[Building AI Agents That Survive Production](https://www.youtube.com/watch?v=swO5svhBhQ4)** · MLOps · 2026-05-09

**Status:** `done` · **Verdict:** `adopt` · **Effort:** `high`

---

## Hypothesis

If we build agents with explicit retry policies, durable state checkpoints, and structured failure logging, then they will survive production edge cases without silent failures because production environments have network errors, rate limits, and partial completions that demo environments never expose.

## What they did

Inferred from title: the video covers engineering practices for making AI agents robust in production, likely including error handling, idempotency, observability, and graceful degradation patterns.

## Relevance to YOLO loop

Core to productionizing our YOLO loop: adding checkpoint saves, structured error logs, and retry wrappers around Claude Code tool calls would make the loop resumable after failures.

## Outcome

Audited in experiments/agents-survive-production/ (PR #10): tick_tock.yml scored 3 PASS / 5 PARTIAL / 6 FAIL against a 14-criterion checklist. top_gaps.md surfaces three concrete follow-on tick proposals (output-shape alerting, runbook directory, Python dep pinning) for the next triage.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-05-09 | `backlog` | Extracted from YouTube RSS |
| 2026-05-15 | `done` | Scaffold deliverables shipped in PR #10; promoted via PR #11 (tick_queue_approved). Status flipped post-merge since deliverables already on main. |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-05-09-agents-survive-production` |
| Channel | MLOps |
| Video | [Building AI Agents That Survive Production](https://www.youtube.com/watch?v=swO5svhBhQ4) |
| Published | 2026-05-09 |
| Ingested upstream | 2026-05-09 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
