# Implement a run-level token budget control plane with steer-before-halt policies

> Back to [[experiments-index]]

Source: **[FinOps for AI Agents: Who Spent All the Tokens? — Tisha Chawla & Susheem Koul, Microsoft](https://www.youtube.com/watch?v=GJX19pNhmSw)** · aie · 2026-08-22

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we monitor token spend and velocity at the agent run level (not just the model gateway level) and inject budget-awareness instructions before hitting a hard cap, then agent completion rates increase and average spend drops because we steer rather than kill runaway loops.

## What they did

Tisha and Sushim proposed and demoed 'TokenOps': a control plane that attributes every model call to a specific agent run, enforces cumulative budgets per run, and applies a policy catalog before resorting to hard kills. A 'CostGuard' module monitors spend velocity and injects system instructions ('be more succinct') when projected to exceed budget. Benchmarked on BrowserUse and MetaGPT: average spend down 78%, completion rate up from 67% to 96% vs simple throttling. Policy catalog covers context compaction, tool output reduction, loop detection, and progress detection.

## Relevance to YOLO loop

Immediately relevant: our Claude Code sessions can hit runaway loops. We can implement a lightweight version: track token count per session, and at 80% of budget inject a 'summarize and wrap up' instruction rather than letting the session hit the hard limit or run indefinitely.

## Notes

Public wiki with policy catalog available via QR code in talk. Future direction: self-learning module that discovers new failure modes from the spend ledger and generates new policies automatically. Key distinction from existing tools: control at the run/call-path level, not just the model gateway.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-22 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-22-token-ops-control-plane` |
| Channel | aie |
| Video | [FinOps for AI Agents: Who Spent All the Tokens? — Tisha Chawla & Susheem Koul, Microsoft](https://www.youtube.com/watch?v=GJX19pNhmSw) |
| Published | 2026-08-22 |
| Ingested upstream | 2026-08-22 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
