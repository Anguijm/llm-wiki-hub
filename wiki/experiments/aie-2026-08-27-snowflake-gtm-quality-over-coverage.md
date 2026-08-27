# Define a 150-question test suite before deploying an agent and enforce 95% accuracy on a subset before expanding coverage

> Back to [[experiments-index]]

Source: **[Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](https://www.youtube.com/watch?v=DrTdD-ttjCY)** · aie · 2026-08-27

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we write a comprehensive question test suite from the user's perspective before building the agent's data connections, then we will identify coverage gaps early and avoid shipping an agent that fails on common queries, because Snowflake's GTM assistant launched with only 50% accuracy on 150 pre-defined questions and recovered by narrowing to 50 high-confidence questions at 95% accuracy before expanding.

## What they did

Speaker (Snowflake internal AI tools lead, 1M+ questions answered, 40K/week) described writing 150 representative user questions in a spreadsheet before the engineering team had connected any data sources. Initial accuracy was 50%. Team pivoted to 'quality over coverage' — answering 50 questions at 95% accuracy to build user trust, then adding 60% of current data sources post-launch over 6-7 months. Current system has 15 semantic views, 85 tables, 3000 columns, 5-6 MCP connections, ~20 skills. Key principle: 'user trust is earned extremely hard and lost overnight.'

## Relevance to YOLO loop

Directly applicable to any new agent capability we add. Before wiring up a new tool or data source, write the 20 most likely queries a user would make. Run them. Only ship when accuracy is high on that subset. Prevents the trust-destruction spiral.

## Notes

'Collapsing law factor' — once users are happy, immediately plan what to show them in 1-2 months to maintain momentum. Continuous delivery mindset essential.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-27 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-27-snowflake-gtm-quality-over-coverage` |
| Channel | aie |
| Video | [Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](https://www.youtube.com/watch?v=DrTdD-ttjCY) |
| Published | 2026-08-27 |
| Ingested upstream | 2026-08-27 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
