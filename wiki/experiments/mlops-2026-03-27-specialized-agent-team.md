# Use specialized agent roles instead of one monolithic agent

> Back to [[experiments-index]]

Source: **[Lessons from 25 Trillion Tokens — Scaling AI-Assisted Development at Kilo](https://www.youtube.com/watch?v=tG1CSRaJhKQ)** · @MLOps · 2026-03-27

**Status:** `done` · **Verdict:** `discard` · **Effort:** `medium`

---

## Hypothesis

If we split the YOLO builder into specialized agent roles (Architect for research/design, Code Agent for implementation, Debug Agent for troubleshooting), then build quality improves because each agent operates within a focused context window instead of juggling all responsibilities.

## What they did

Kilo Code engineers manage several specialized agents simultaneously: Architect Agent (research/design), Code Agent (implementation/boilerplate), Ask Agent (querying codebase), Debug Agent (troubleshooting). This mirrors the shift from 20% thinking / 80% coding to 80% thinking / 20% coding.

## Actionable steps

- Identify which YOLO loop phases map to which agent role
- Test running Gemini brainstorm as Architect, Claude as Code Agent, Gemini review as Debug Agent
- Compare output quality vs current single-agent approach on 3 builds

## Success metric

Fewer Gemini-reported bugs on builds using specialized roles vs single-agent builds.

## Relevance to YOLO loop

The YOLO loop already uses Gemini for brainstorming and review (proto-specialization). Formalizing this into distinct agent roles could improve each phase.

## Target projects

- [[yolo-projects]] (`yolo-loop-infrastructure`)

## Outcome

Test: yaml-fmt built by 3 agents (Architect 83s, Coder 461s, Reviewer 419s = 963s agent time, 1022s wall). Council scores: bugs 6, security 5, UI 8, guide 9, usefulness 6.5, cool 9.5. Reviewer found and fixed 8 bugs including O(N^2) DoS and prototype pollution. Verdict: the split works but adds ~40% time overhead vs monolithic. Main win is the Reviewer catching bugs the Coder missed. Recommend keeping 3-phase pipeline (Plan/Build/Review) but within one session — separate agents add coordination cost without proportional quality gain.

## Notes

The 3-phase pipeline within a single agent captures most of the value. Separate agents add overhead.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-03 | `in_progress` | Running test: 3-agent split vs monolithic on next tick build |
| 2026-04-03 | `done` | 3-agent test complete. Works but 40% slower. Single-agent 3-phase is better. |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-03-27-specialized-agent-team` |
| Channel | @MLOps |
| Video | [Lessons from 25 Trillion Tokens — Scaling AI-Assisted Development at Kilo](https://www.youtube.com/watch?v=tG1CSRaJhKQ) |
| Published | 2026-03-27 |
| Ingested upstream | 2026-03-30 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
