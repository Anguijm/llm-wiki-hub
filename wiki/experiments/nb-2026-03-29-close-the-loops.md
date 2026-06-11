# Adopt the 'close the loops' delegation framework

> Back to [[experiments-index]]

Source: **[Anthropic Just Gave You 3 Tools That Work While You're Gone](https://www.youtube.com/watch?v=3e7gmNPr5Vo)** · nb · 2026-03-29

**Status:** `done` · **Verdict:** `adopt` · **Effort:** `low`

---

## Hypothesis

If we identify open commitments (pending tasks causing mental load) and delegate them to background agents, then we free up cognitive bandwidth for high-level decisions because agents handle the execution while we focus on direction.

## What they did

Nate described 'open commitments' as tasks that cause mental buzzing. He recommends using agents to close them — meeting minutes, revised scopes, follow-up emails — so humans focus on decision-making.

## Actionable steps

- List all open commitments in the YOLO project (stale PRs, unfinished docs, pending reviews)
- Delegate each to a background Claude session with clear spec
- Track completion rate and time savings

## Success metric

80% of identified open commitments closed within 24 hours of delegation.

## Relevance to YOLO loop

The YOLO loop accumulates open commitments during Phase 2/3 (unfinished refinements, dashboard updates, learnings not yet written).

## Target projects

- [[yolo-projects]] (`yolo-loop-infrastructure`)

## Outcome

The Phase 2 refinement and Phase 3 cull processes already embody close-the-loops: every open commitment (unrefined project, useless project) was systematically identified and closed. The principle is sound but was already adopted implicitly. No new tooling needed.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-03-29 | `done` | Evaluated: Phase 2/3 cull process already demonstrates this pattern |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-03-29-close-the-loops` |
| Channel | nb |
| Video | [Anthropic Just Gave You 3 Tools That Work While You're Gone](https://www.youtube.com/watch?v=3e7gmNPr5Vo) |
| Published | 2026-03-29 |
| Ingested upstream | 2026-03-29 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
