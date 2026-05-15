# Use Effect Cluster workflows to guarantee completion of multi-step AI agent processes across server crashes

> Back to [[experiments-index]]

Source: **[Vibe Engineering Effect Apps — Michael Arnaldi, Effectful](https://www.youtube.com/watch?v=Wmp2Tku2PrI)** · aiDotEngineer · 2026-05-10

**Status:** `deferred` · **Effort:** `medium`

---

## Hypothesis

If we wrap multi-step AI agent operations (e.g., register user → send email, or LLM call → write DB → notify) in Effect workflow primitives backed by Effect Cluster, then the process completes exactly once even if the server crashes mid-flight, because the workflow engine persists state and resumes on a different node, eliminating the silent partial-completion failures that become common when LLM response times extend average process duration from milliseconds to minutes.

## What they did

Michael Arnaldi observed that AI-driven processes convert previously 10ms operations into minute-long operations, making server failure during a request statistically likely even at low user counts. He drew the analogy to registration flows where 'if email didn't arrive, retry' is a symptom of unguaranteed two-operation sequences. Effect Cluster provides durable workflow execution (similar to Temporal/Inngest) where a started procedure is guaranteed to finish by migrating to another node on crash. He noted this is currently in the unstable part of Effect but will stabilize soon, and that the agent-assisted development pattern (clone repo → extract patterns → implement) applies equally to Effect workflows.

## Relevance to YOLO loop

YOLO loop agentic runs are long-lived processes (LLM calls, tool chains, file writes, external API calls) that currently have no crash-recovery guarantee. Wrapping loop phases in Effect workflows would make the loop resumable after infrastructure failures without duplicate side effects.

## Notes

Deferred 2026-05-10: Effect TS framework; revisit only if we adopt TypeScript for a portfolio project. Today the loop is Python-centric.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-05-10 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-05-10-effect-workflows-long-running-ai` |
| Channel | aiDotEngineer |
| Video | [Vibe Engineering Effect Apps — Michael Arnaldi, Effectful](https://www.youtube.com/watch?v=Wmp2Tku2PrI) |
| Published | 2026-05-10 |
| Ingested upstream | 2026-05-10 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
