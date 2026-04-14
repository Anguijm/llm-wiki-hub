# Build independent observability that never trusts agent self-reporting

> Back to [[experiments-index]]

Source: **[Your Agent Produces at 100x. Your Org Reviews at 3x.](https://www.youtube.com/watch?v=kVPVmz0qJvY)** · @NateBJones · 2026-04-05

**Status:** `done` · **Verdict:** `adopt` · **Effort:** `medium`

---

## Hypothesis

If we add an independent verification layer that checks actual outcomes (file exists, tests pass, git committed) instead of trusting the agent's claim that it did the work, then we catch silent failures that currently slip through.

## What they did

NateBJones: never ask the agent "did you do it?" — build automated auditing that independently verifies. Stack traces, logs, health monitors that validate without asking.

## Relevance to YOLO loop

Our Phase 4 cron failed silently for days because we trusted the agent to commit. The status protocol partially addresses this but we could add a post-build verification script that independently checks: does the project folder exist? Does index.html exist? Did test_project.py actually run?

## Outcome

Built verify_build.py — 7 independent checks (dir exists, HTML valid, JS syntax, log entry, README, dashboard fresh). Never trusts agent self-reporting. Integrated into cron docs update step. Caught real dashboard staleness on first run.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-06 | `backlog` | Extracted from NateBJones review bottleneck video |
| 2026-04-06 | `done` | verify_build.py created, tested, integrated into cron |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-04-05-independent-observability` |
| Channel | @NateBJones |
| Video | [Your Agent Produces at 100x. Your Org Reviews at 3x.](https://www.youtube.com/watch?v=kVPVmz0qJvY) |
| Published | 2026-04-05 |
| Ingested upstream | 2026-04-06 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
