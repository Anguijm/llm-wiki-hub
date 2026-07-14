# Structure Every Agent Loop Around a Loop Contract Markdown File with State and Append-Only Log

> Back to [[experiments-index]]

Source: **[What I learnt after running loops for 1 month???](https://www.youtube.com/watch?v=JQ_We_ztxrI)** · aij · 2026-07-14

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If every autonomous agent loop is governed by a single markdown file containing a goal, explicit human-escalation boundaries, an SOP, a durable state block, and an append-only run log, then loops will avoid rediscovering the same errors each run and will improve over time, because the agent always starts with accumulated context rather than a blank slate.

## What they did

Jason's team ran multiple production loops (React Doctor codebase health checker, CRM lifecycle outreach, documentation drift fixer) at their company Super Design for over a month. Each loop had one markdown file split into: loop contract (goal, boundaries defining what the agent can do vs. must escalate, SOP), and state+log (current hypothesis/backlog as a small durable snapshot, plus an append-only chronological record). They also built an internal dashboard tool to track PRs opened/merged and health scores over time, and implemented an 'evolve run' that fires every few sessions to review past runs and sharpen the contract. The doc-maintainer loop included an explicit rule 'never rewrite accurate docs to look busy' to suppress spurious agent activity.

## Relevance to YOLO loop

This is a direct blueprint for our YOLO loop's memory and governance layer. The loop contract pattern gives us a concrete way to encode what the loop is allowed to do autonomously vs. what requires human review, which is the core safety question for any long-running agent.

## Notes

Team open-sourced their loop tooling; GitHub link in video description.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-14 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aij-2026-07-14-loop-contract-md-pattern` |
| Channel | aij |
| Video | [What I learnt after running loops for 1 month???](https://www.youtube.com/watch?v=JQ_We_ztxrI) |
| Published | 2026-07-14 |
| Ingested upstream | 2026-07-14 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
