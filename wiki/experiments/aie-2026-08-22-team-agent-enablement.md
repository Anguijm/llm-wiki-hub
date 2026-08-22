# Redirect skeptic engineers from fixing agent output to improving agent context and harness

> Back to [[experiments-index]]

Source: **[Coding Agents Don't Scale Themselves. Neither Do Your Teams. — Patrick Debois, Tessl](https://www.youtube.com/watch?v=zCJtYuqwm7E)** · aie · 2026-08-22

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we channel developer skepticism about agent output quality into building better context files, harnesses, and tooling for agents rather than manually fixing generated code, then agent output quality improves systematically and resistant engineers re-engage because they're doing real engineering work.

## What they did

Patrick argued that the key org-level shift is moving developers from 'fix the code the agent produced' to 'improve the system that produces the code.' He described how introducing harnesses and loops created a new technical path (tooling for agents) that re-engaged engineers who felt coding agents weren't for them. He also covered metrics framing: track turns-to-completion and context reuse rates rather than raw productivity comparisons to justify agent investment to VPs.

## Relevance to YOLO loop

Actionable immediately: when our loop produces bad output, log it as a context/harness improvement ticket rather than a one-off fix. Use skeptic feedback to harden CLAUDE.md, skills, and verification steps. Track iteration count per task as a proxy metric.

## Notes

Patrick is building an 'agent enablement patterns' website and soliciting real org stories. Key mantra from swyx: 'stop building the thing, build the thing that builds the thing.'

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-22 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-22-team-agent-enablement` |
| Channel | aie |
| Video | [Coding Agents Don't Scale Themselves. Neither Do Your Teams. — Patrick Debois, Tessl](https://www.youtube.com/watch?v=zCJtYuqwm7E) |
| Published | 2026-08-22 |
| Ingested upstream | 2026-08-22 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
