# Give agents a built-in feedback tool that routes user-observed issues directly to a dev triage queue

> Back to [[experiments-index]]

Source: **[Cloudroom just destroyed all AI coding apps (fully open-source)](https://www.youtube.com/watch?v=FbKXvab-0yQ)** · do · 2026-10-15

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we expose a structured feedback tool within the agent harness that users can invoke in natural language, then bug and UX reports will arrive in a developer-accessible database automatically because the agent translates freeform observations into structured records without requiring the user to switch context.

## What they did

David showed a 'report feedback' tool embedded in the Cloudroom CLI. A user can instruct their agent to 'send this feedback to David' in plain English; the agent calls the tool, writes to a Postgres table, and a cloud automation runs every 10 minutes to spin up a new investigation thread. He demonstrated this as a model for agentic product telemetry loops.

## Relevance to YOLO loop

Directly applicable to our YOLO loop's observability layer: adding a feedback tool to our agent harness would close the loop between runtime agent behavior and developer triage without requiring manual reporting steps.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-15 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-10-15-agent-feedback-tool-to-founder` |
| Channel | do |
| Video | [Cloudroom just destroyed all AI coding apps (fully open-source)](https://www.youtube.com/watch?v=FbKXvab-0yQ) |
| Published | 2026-10-15 |
| Ingested upstream | 2026-10-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
