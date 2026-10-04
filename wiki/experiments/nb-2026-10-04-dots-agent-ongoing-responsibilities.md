# Assign Ongoing Calendar and Scheduling Responsibilities to a Dots Agent

> Back to [[experiments-index]]

Source: **[Should You Pay $100 A Month For OpenAI's Dots When Meta's Muse Has A Free Version?](https://www.youtube.com/watch?v=lnB4Zckx_34)** · nb · 2026-10-04

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we delegate recurring scheduling hygiene tasks (zombie meetings, travel conflicts) to a persistent Dots agent with calendar context, then we will reduce manual scheduling overhead because the agent retains context across sessions and proactively surfaces conflicts without prompting.

## What they did

The speaker used OpenAI Dots to give an agent ongoing responsibilities over his calendar. The agent autonomously detected a recurring meeting landing on weekends, rebuilt the invite, and also caught a conflict between a DMV appointment and travel plans — all without being explicitly prompted each session, because Dots maintains persistent context.

## Relevance to YOLO loop

Directly maps to the ambient-agent layer of the dev loop: persistent context agents that monitor and act on background tasks without requiring a new prompt each cycle, freeing developer attention for higher-order work.

## Notes

Speaker notes GPT-6.1 Soul approaches o3 evals at ~1/5 the token cost; worth evaluating Soul for background agent tasks before defaulting to o3/Astra to preserve plan quota.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-04 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-10-04-dots-agent-ongoing-responsibilities` |
| Channel | nb |
| Video | [Should You Pay $100 A Month For OpenAI's Dots When Meta's Muse Has A Free Version?](https://www.youtube.com/watch?v=lnB4Zckx_34) |
| Published | 2026-10-04 |
| Ingested upstream | 2026-10-04 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
