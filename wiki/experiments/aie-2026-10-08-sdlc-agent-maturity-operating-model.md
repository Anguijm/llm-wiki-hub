# Implement Incremental Trust-Building Automation Gates From PR Review to Auto-Merge

> Back to [[experiments-index]]

Source: **[Redesigning How Software Gets Built With AI Agents — Sonar & McKinsey Panel](https://www.youtube.com/watch?v=XqF-IFHBCkM)** · aie · 2026-10-08

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we deploy agent automation incrementally (review-only → blocking on critical issues → automated fix PRs → auto-approve low-risk changes → auto-merge), then teams will build sufficient trust to reach fully autonomous PR-to-production flow within months, because each stage provides precision evidence that the agent's outputs are reliable before expanding its authority.

## What they did

The Sonar/McKinsey panel described a maturity model for AI in SDLC. McKinsey research showed 80-90% of companies have deployed AI but fewer than a third see scaled business impact — the gap is process redesign and operating model change, not tooling. Sonar's CEO described their own internal journey: start with agent reviews only (engineers read CI failure analysis), then block PRs on critical issues (precision builds trust), then enable automated fix suggestions (agent creates PRs to fix issues), then auto-approve low-risk changes in non-critical code paths, then auto-merge with conflict resolution. The panel identified three success factors: (1) redesigning the end-to-end workflow not just adding AI to existing steps, (2) tooling with good context layers, (3) redefining team roles as boundaries blur between product/engineering/design. Lighthouse teams demonstrating best practices were cited as the key accelerant for organizational adoption.

## Relevance to YOLO loop

Our YOLO loop can adopt this exact incremental gate model: start with agent-generated PR reviews as read-only, measure precision, then progressively grant blocking and merge authority as confidence data accumulates.

## Notes

Sonar's internal guide-verify-solve model is described in a separate talk referenced in this panel. Key insight: the surprising finding was that lighthouse teams mattered more than expected — organizational change required demonstration, not just mandate.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-08 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-08-sdlc-agent-maturity-operating-model` |
| Channel | aie |
| Video | [Redesigning How Software Gets Built With AI Agents — Sonar & McKinsey Panel](https://www.youtube.com/watch?v=XqF-IFHBCkM) |
| Published | 2026-10-08 |
| Ingested upstream | 2026-10-08 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
