# Run each coding agent in its own isolated cloud VM rather than a shared environment

> Back to [[experiments-index]]

Source: **[Cloudroom just destroyed all AI coding apps (fully open-source)](https://www.youtube.com/watch?v=FbKXvab-0yQ)** · do · 2026-10-15

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we provision one isolated Linux sandbox per agent thread, then we can scale to tens or hundreds of parallel agents without resource contention or cross-contamination because each agent's filesystem and process space is fully independent.

## What they did

David launched 25 sub-agents simultaneously, each in its own isolated cloud VM via Cloudroom. He demonstrated that agents kept running even when the local laptop was closed, and showed 38 concurrent agents visible in the dashboard. He argued that squeezing multiple agents onto a single VPS or Mac Mini caps scalability and causes interference, whereas per-agent VMs enable infinite horizontal scaling.

## Relevance to YOLO loop

Maps to our parallel agent execution strategy: isolating each agent run in its own sandbox would prevent one failing agent from corrupting another's state and would let us scale speculative parallel builds without shared-state bugs.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-15 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-10-15-isolated-sandbox-per-agent` |
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
