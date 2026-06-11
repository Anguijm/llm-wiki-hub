# Optimize CLAUDE.md as short opinionated onboarding doc + configure wildcard permissions

> Back to [[experiments-index]]

Source: **[All of Claude Code Just Leaked — How to Become a Top 1% User](https://www.youtube.com/watch?v=tXtCK66fPj8)** · nh · 2026-04-01

**Status:** `done` · **Verdict:** `discard` · **Effort:** `low`

---

## Hypothesis

If we restructure CLAUDE.md to be a short, opinionated onboarding document (high-level rules, not detailed docs) and configure wildcard permissions for common operations, then agent autonomy increases and permission prompts decrease — enabling faster Tick-Tock cycles.

## What they did

NateHerk analyzed the Claude Code source leak. Key findings: CLAUDE.md should be a force multiplier with short opinionated rules. Wildcard permissions in settings.json eliminate babysitting. Task decomposition into parallel sub-agents is architecturally supported. /compact slashes token costs.

## Actionable steps

- Audit current CLAUDE.md — trim to essential rules, remove verbose docs
- Configure wildcard permissions for git, file edits, test runs in settings.json
- Use /compact more aggressively during long sessions
- Structure prompts for task decomposition (parallel sub-agents)

## Success metric

Tick-Tock sessions run with zero manual permission approvals. CLAUDE.md under 50 lines.

## Relevance to YOLO loop

We already have CLAUDE.md and use sub-agents heavily. Optimizing both would directly speed up the Tick-Tock cadence.

## Target projects

- [[yolo-projects]] (`yolo-loop-infrastructure`)

## Outcome

Parked — cron prompt already serves as effective CLAUDE.md. Context not degrading thanks to /compact at milestones. Would revisit if cron quality drops.

## Notes

Parked, not permanently discarded.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-03 | `done` | Parked — cron performing well without it |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-04-01-claude-md-optimization` |
| Channel | nh |
| Video | [All of Claude Code Just Leaked — How to Become a Top 1% User](https://www.youtube.com/watch?v=tXtCK66fPj8) |
| Published | 2026-04-01 |
| Ingested upstream | 2026-04-01 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
