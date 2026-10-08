# Run a Cron-Based Agent Loop That Mines Production Traces to Propose and Backtest Agent Improvements

> Back to [[experiments-index]]

Source: **[The Self-Improving OSS Agent Stack — Marc Klingen, Langfuse](https://www.youtube.com/watch?v=TeErpYBUIeM)** · aie · 2026-10-08

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we run a coding agent on a scheduled cron job that reads production traces, identifies failure patterns, proposes changes to prompts or agent implementation, backtests those changes against an updated dataset, and opens a PR only when the candidate version outperforms the baseline, then agent quality will improve continuously with minimal human effort because the agent handles the tedious trace-review and hypothesis-generation work while humans only approve or reject diffs.

## What they did

Langfuse's Marc Klingen described the self-improving agent stack they see their best users building. The pattern has three phases: (1) collect production traces with detailed execution context, (2) run a cron-based agent loop (daily or weekly) that mines those traces for failure patterns, proposes fixes to the agent implementation, updates datasets and evaluators to test for the identified failures, and backtests the new implementation against the old baseline, and (3) have the agent open a PR only when the candidate version shows a positive delta. He gave a concrete example: an agent discovered that their content writer was using internal engineering jargon (e.g., 'ingestion pipeline') in user-facing copy. The agent proposed updated datasets and evaluators to test for user-facing language, generated a v2 implementation that scored better on that dimension, and auto-merged it (since it only opens PRs, never deploys directly to production). He noted a key architectural shift: Langfuse's platform went from write-heavy (ingesting traces) to read-heavy (agents querying large volumes of historical trace data), requiring a scalable, non-sampled, long-retention data layer. He also flagged human-in-the-loop checkpoints: dataset curation, evaluator design, and reviewing proposed fixes to avoid overfitting to edge cases that don't matter.

## Relevance to YOLO loop

This is the most direct description of what our YOLO loop should eventually become. The cron-based pattern (collect traces → mine failures → propose fix → backtest → PR) is a concrete implementation blueprint. The 'agent only opens PRs, never deploys' constraint is the right safety boundary for our current trust level. The read-heavy trace query pattern is a heads-up for how our trace store will need to scale as the loop matures.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-08 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-08-self-improving-oss-agent-stack` |
| Channel | aie |
| Video | [The Self-Improving OSS Agent Stack — Marc Klingen, Langfuse](https://www.youtube.com/watch?v=TeErpYBUIeM) |
| Published | 2026-10-08 |
| Ingested upstream | 2026-10-08 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
