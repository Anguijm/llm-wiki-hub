# Deploy evaluative agents alongside generative agents to eliminate review bottleneck

> Back to [[experiments-index]]

Source: **[Your Agent Produces at 100x. Your Org Reviews at 3x.](https://www.youtube.com/watch?v=kVPVmz0qJvY)** · nb · 2026-04-05

**Status:** `done` · **Verdict:** `adopt` · **Effort:** `low`

---

## Hypothesis

If we build Agent B to review/filter Agent A output before human review (pre-filtered council), then the human only sees pre-audited work and the 100x/3x bottleneck disappears.

## What they did

NateBJones argues scaling agent output breaks human review capacity. Solution: secondary LLM agents as critical thinkers that auto-filter and auto-fix before human sees anything. Also: independent observability (never trust agent self-reporting).

## Relevance to YOLO loop

We already do this — the 6-angle council IS the evaluative agent layer. But we could add an automated pre-filter that rejects builds with test failures or security issues BEFORE council runs, saving Gemini calls.

## Outcome

Added PRE-FILTER gate to cron: test_project.py + eval_bugs.py + security_scan.py must ALL pass before council runs. Saves Gemini calls on broken builds. Council only reviews code that already passes all automated checks.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-06 | `backlog` | Extracted from NateBJones review bottleneck video |
| 2026-04-06 | `done` | Implemented and integrated into cron |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-04-05-evaluative-agents-review-bottleneck` |
| Channel | nb |
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
