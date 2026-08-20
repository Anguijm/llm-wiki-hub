# Use overnight agent runs with expanding task scope to ship 2–10 PRs per week within a meeting-heavy schedule

> Back to [[experiments-index]]

Source: **[Prototyping as Leadership: How a CTO Ships with AI Agents — Hursh Agrawal, The Browser Company](https://www.youtube.com/watch?v=bdHaOXZOhcM)** · aie · 2026-08-20

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If leaders set up scoped agent tasks in the evening with sufficient organizational scaffolding (CI, feature flags, AGENTS.md, prototype branch) and review outputs in the morning, then they can consistently ship 2–10 PRs per week even with 15+ recurring meetings, because manager schedule time becomes building time.

## What they did

Hursh Agrawal (CTO/co-founder, Browser Company — Arc and Dia browsers) described how he ships 2–10 PRs/week with a toddler at home and 15+ recurring meetings/week. He attributes this entirely to AI coding agents. Key practices: (1) set up tasks in evening, let agents run overnight, review and test in morning; (2) push on task scope aggressively — models can handle weeks of work overnight if set up correctly; (3) use a prototype branch that deploys to employees but not production; (4) always test everything personally before adding reviewers; (5) write small readable PRs to model good behavior for the team. Demonstrated three examples including training two ML models + full analysis report overnight. Organizational scaffolding required: AI code reviewers, AGENTS.md/CLAUDE.md hygiene, trustworthy CI, feature flags, prototype branch. He cited Simon Willison's framing that models are capable of far more than we assume and our job is to discover the scope limits.

## Relevance to YOLO loop

Directly maps to our operating model. The evening task setup → overnight run → morning review cycle is the same pattern as Kieran's compound engineering. Key additions: prototype branch for safe employee testing, AI code reviewer as first-pass gatekeeper, aggressive scope expansion as an experiment discipline.

## Notes

Four categories of leader-appropriate builds (from Julie Zhuo survey): (1) internal tools/quality-of-life, (2) celebration artifacts for team, (3) vision prototypes with new model families, (4) codebase gardening. Hursh recommends against taking critical-path work. His 'code humbled' warning: agent-generated code has caused SEVs and annoyed engineers — always read code before adding reviewers, keep PRs small. Delegation skill from managing people transfers directly to prompting agents: set goals, give context, check in, coach ('have you tried this?').

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-20 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-20-cto-prototyping-overnight-agent-runs` |
| Channel | aie |
| Video | [Prototyping as Leadership: How a CTO Ships with AI Agents — Hursh Agrawal, The Browser Company](https://www.youtube.com/watch?v=bdHaOXZOhcM) |
| Published | 2026-08-20 |
| Ingested upstream | 2026-08-20 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
