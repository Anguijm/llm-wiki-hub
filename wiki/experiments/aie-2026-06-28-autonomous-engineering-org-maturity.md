# Use a six-stage agent maturity model and AI champions program to accelerate org-wide adoption past stage 3

> Back to [[experiments-index]]

Source: **[Building an Autonomous Engineering Org - Angie Jones, Agentic AI Foundation](https://www.youtube.com/watch?v=whue9_YquGA)** · aie · 2026-06-28

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we identify and invest in a small cohort of high-commitment AI champions (1% of engineers) who pioneer agentic patterns for their team's specific repositories, then the remaining 90% of engineers adopt more advanced delegation behaviours faster than they would through self-directed learning, because the 90-9-1 rule means most engineers will adopt patterns that already exist in their team context rather than discovering them independently.

## What they did

Angie described Block's journey to build an autonomous engineering org across 3,500 engineers. She created a six-stage maturity model: 0=no AI, 1=autocomplete only, 2=chatting with agents (no PRs), 3=delegating tasks and reviewing output, 4=running multiple agents in parallel, 5=agents produce shippable results without hand-holding. She launched an AI champions program — 50 strategically selected engineers (not volunteers) who committed 30% time to AI enablement across critical repositories. Champions performed 'repo readiness' work: writing CLAUDE.md/agents.md files, building team-specific skills, creating test harnesses for agent output validation. Once at stage 4, she enabled Codex for automated PR review with an auto-fix loop (Codex finds issues → second agent commits fixes). At stage 5, she built a company world model (machine-readable map of all 25K repos and dependencies) powering an orchestrator (BuilderBot) that lets anyone in the org delegate full features via Slack.

## Relevance to YOLO loop

The maturity model provides a diagnostic for where any team sits in agent adoption. The repo-readiness work (CLAUDE.md, skills, test harnesses) is directly applicable to setting up an effective YOLO loop. The world model / orchestrator pattern is the long-term target architecture the loop is evolving toward.

## Notes

Talk ends with an ethical provocation — the autonomous org resulted in layoffs and Angie questions whether building it was the right outcome. Worth holding alongside the technical learnings.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-28 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-06-28-autonomous-engineering-org-maturity` |
| Channel | aie |
| Video | [Building an Autonomous Engineering Org - Angie Jones, Agentic AI Foundation](https://www.youtube.com/watch?v=whue9_YquGA) |
| Published | 2026-06-28 |
| Ingested upstream | 2026-06-28 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
