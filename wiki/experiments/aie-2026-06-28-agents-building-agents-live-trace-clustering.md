# Cluster Live Agent Traces into Failure Reports and Auto-Fix with a Coding Agent

> Back to [[experiments-index]]

Source: **[Agents Building Agents - Alfonso Graziano, Nearform](https://www.youtube.com/watch?v=aHhB3sjGjkI)** · aie · 2026-06-28

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we collect production traces with user feedback, cluster them into failure categories once per sprint, and feed those clusters to a coding agent with a spec-and-harness environment, then we can close the live-data feedback loop automatically because the coding agent can validate its own fixes against existing evals before proposing a PR.

## What they did

Alfonso described a pipeline where production traces (with thumbs-up/thumbs-down feedback) are clustered by an LLM into failure modes. A report is generated per sprint summarizing the clusters. Human judgment is applied to filter false positives or out-of-scope clusters. Valid failure modes are converted into specs and added to the golden dataset. A coding agent (they used AutoAgent in complex cases) is given the traces and the spec, makes code changes, runs the eval suite to validate, and proposes draft PRs. The whole thing is enabled by 'Harness Engineering'—providing the coding agent with constraints, quality gates (linting, unit tests, evals, LLM code review), context engineering, and observability.

## Relevance to YOLO loop

This is the outer feedback loop of the YOLO loop: production signals → automated clustering → spec generation → coding agent fix → eval gate → merge. It shows how to make the entire loop self-improving with minimal human intervention beyond sprint-level review.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-28 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-06-28-agents-building-agents-live-trace-clustering` |
| Channel | aie |
| Video | [Agents Building Agents - Alfonso Graziano, Nearform](https://www.youtube.com/watch?v=aHhB3sjGjkI) |
| Published | 2026-06-28 |
| Ingested upstream | 2026-06-28 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
