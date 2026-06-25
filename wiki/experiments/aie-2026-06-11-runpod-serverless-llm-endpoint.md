# Deploy a HuggingFace open-source LLM as a RunPod serverless endpoint from a preconfigured Hub listing in under 5 minutes

> Back to [[experiments-index]]

Source: **[Under 5 minutes to a deployed LLM endpoint — Audry Hsu, RunPod](https://www.youtube.com/watch?v=ILdE7FaAjVA)** · aie · 2026-06-11

**Status:** `discarded` · **Verdict:** `discard` · **Effort:** `low`

---

## Hypothesis

If we use RunPod's Hub preconfigured listings to deploy an open-source LLM (e.g. via vLLM) as a serverless auto-scaling endpoint, then we can get a production-ready inference API with cold-start-only billing and no infrastructure management in under 5 minutes, because the Hub listings provide pre-built Dockerfiles with vLLM defaults and the serverless runtime handles scaling and worker lifecycle automatically.

## What they did

Audrey Hsu from RunPod gave a live demo deploying an LLM endpoint via the RunPod console. She navigated to the Hub (pre-vetted open-source model listings), selected an LLM listing backed by a public GitHub repo with a pre-configured vLLM Dockerfile, adjusted the max model length (context window) via an env var, and clicked deploy. The endpoint provisioned on H100s with A100 fallback, auto-scales to a configurable max worker count, charges only during active request execution, and returned a first response (including ~41s cold-start) within the demo. She noted the same flow is available via CLI and RunPod Python SDK for programmatic/agent use.

## Relevance to YOLO loop

Useful when we need a cheap, fast-to-spin-up inference endpoint for open-source models during experiments—avoids committing to dedicated GPU costs. The serverless billing model fits burst evaluation workloads in our loop.

## Notes

Backlog triage 2026-06-24 (owner-preference model). Deploy an open LLM endpoint — infra off-focus.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-11 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-06-11-runpod-serverless-llm-endpoint` |
| Channel | aie |
| Video | [Under 5 minutes to a deployed LLM endpoint — Audry Hsu, RunPod](https://www.youtube.com/watch?v=ILdE7FaAjVA) |
| Published | 2026-06-11 |
| Ingested upstream | 2026-06-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
