# Run a timed coding agent challenge on a real domain dataset to benchmark context engineering strategies

> Back to [[experiments-index]]

Source: **[Context Engineering for Coding Agents](https://www.youtube.com/watch?v=jXtnhyro-QE)** · mlops · 2026-06-15

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we run structured head-to-head agent challenges against a real-world domain dataset with a fixed time limit and standardized output schema, then we surface which context engineering approaches (memory systems, tool selection, prompt structure) actually matter under pressure because competitive constraints force participants to make explicit tradeoffs visible.

## What they did

Hosted an MLOps community event in Amsterdam where teams of ~4 competed to build coding agents that could extract structured data from an industrial domain PDF (grease/oil engineering drawings) into a standardized output.json within 10 minutes. Speaker (AI researcher, former restaurant owner, sociology background at Java Applied AI Lab) gave a 40-60 min talk on context engineering principles, then dropped the real challenge file (ZPR152.pdf) and ran the timed competition. Results were scored automatically by pulling output.json from each team's folder. Speaker noted he would share the memory system he built and all team results afterward.

## Relevance to YOLO loop

Directly tests context engineering decisions (what goes in context, memory architecture, tool use) under real-world constraints. The standardized output.json + auto-scoring pattern is a reusable evaluation harness for YOLO loop experiments.

## Notes

Transcript is from a live event; full talk content truncated at 50k chars. Speaker promised to share memory system implementation and all team results post-event — worth following up. Domain was industrial PDF extraction (oil/grease engineering drawings).

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-15 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-06-15-context-engineering-coding-agents` |
| Channel | mlops |
| Video | [Context Engineering for Coding Agents](https://www.youtube.com/watch?v=jXtnhyro-QE) |
| Published | 2026-06-15 |
| Ingested upstream | 2026-06-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
