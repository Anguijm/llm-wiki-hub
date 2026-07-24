# Run an automated OS audit skill to detect context failure modes before they cause hallucinations

> Back to [[experiments-index]]

Source: **[5 Hacks to Instantly Level Up Your AI OS](https://www.youtube.com/watch?v=Ek1NBfnnTH0)** · nh · 2026-07-24

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we run a self-auditing skill over the full AIOS project on a regular cadence, then we proactively catch poisoning, bloat, confusion, and clash failures before they surface as wrong agent outputs because the audit externalizes context health checks that currently live only in the developer's memory.

## What they did

Built and demonstrated an 'OS audit skill' that reads the entire project, checks all routing rules, identifies weak areas/stale data/missing updates, and outputs a markdown audit report listing 10 findings + proposed fixes (without auto-applying them). Categorized four context failure modes: (1) Poisoning—false fact in context confidently returned; (2) Bloat—too much data causing needle-in-haystack retrieval failures; (3) Confusion—missing/irrelevant data triggering hallucinated fill-ins; (4) Clash—conflicting data sources (e.g., March policy vs June policy) causing unpredictable choices. Also introduced expertise vs situational context split and a 'backtrack' technique: when the agent fails to find data it should have, have it trace back its own search path, identify the mistake, and update routing accordingly.

## Relevance to YOLO loop

The YOLO loop's AIOS grows over time and is susceptible to all four failure modes as new skills, client projects, and wiki entries accumulate. A periodic audit skill would serve as a health-check gate, surfacing routing conflicts and stale facts before they corrupt skill outputs or client-facing deliverables.

## Notes

Free skill available in speaker's School community. The four failure modes (poisoning, bloat, confusion, clash) are a useful diagnostic taxonomy to bake into our own audit prompt. Backtrack technique is low-effort to adopt immediately: when agent claims it can't find data we know exists, ask it to retrace its search steps and patch the routing rule.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-24 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-07-24-aios-context-failure-modes` |
| Channel | nh |
| Video | [5 Hacks to Instantly Level Up Your AI OS](https://www.youtube.com/watch?v=Ek1NBfnnTH0) |
| Published | 2026-07-24 |
| Ingested upstream | 2026-07-24 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
