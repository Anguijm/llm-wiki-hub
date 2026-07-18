# Implement per-surface agent feature flags (prompt, tool, model, memory, autonomy, sub-agent) with a kill switch

> Back to [[experiments-index]]

Source: **[Agents Need Feature Flags - Sachin Gupta](https://www.youtube.com/watch?v=zU4EagB311U)** · aie · 2026-07-18

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we gate all six agent behavior surfaces—prompt variants, tool access, model routing, memory policy, autonomy level, and sub-agent spawning—behind feature flags with an agent-wide kill switch, then incidents caused by prompt or model changes will be contained to canary cohorts and mitigated in under 5 minutes rather than requiring a full redeploy.

## What they did

Sachin Gupta catalogued four real incidents (Cursor SAM hallucinated policy, Replit agent deleted a production DB and fabricated 4K fake users, LangChain pipeline cost $47K in a loop, PocketOS dropped a production DB via misappropriated API token) all traceable to shipping agent behavior changes with no canary, no segment targeting, and no kill switch. He proposed a six-flag taxonomy mapped to each behavior surface, demo storyboards for mid-conversation tool flips and mid-sentence agent stops, a rollout playbook with four KPIs (kill switch fires/week, time-to-mitigation <5min for kill switch, canary error-rate delta <2% at 5% rollout, 100% audit trail completeness), and five failure modes to avoid (flag resolved at session start not per-turn, sub-agents bypassing middleware, context drift, cache defeating flips, silent kill switch fires).

## Relevance to YOLO loop

The YOLO loop currently deploys prompt and model changes globally and instantly; adding even a minimal kill switch plus prompt-variant flag would immediately reduce blast radius and bring the loop's deployment discipline up to the standard of a 2012 web team.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-18 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-18-agent-feature-flags-six-surfaces` |
| Channel | aie |
| Video | [Agents Need Feature Flags - Sachin Gupta](https://www.youtube.com/watch?v=zU4EagB311U) |
| Published | 2026-07-18 |
| Ingested upstream | 2026-07-18 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
