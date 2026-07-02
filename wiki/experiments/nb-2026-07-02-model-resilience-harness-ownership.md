# Own the routing harness so any single model going offline causes zero downtime

> Back to [[experiments-index]]

Source: **[Your AI Model is Probably Wrong for This Job](https://www.youtube.com/watch?v=lq2fP7wC7d8)** · nb · 2026-07-02

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we build our AI pipeline around an owned routing harness rather than hardcoding a single model endpoint, then a model becoming unavailable (ban, outage, deprecation) will not halt work because we can reroute to an equivalent model without changing application logic.

## What they did

Speaker used the 18-day Fable (Claude) ban as a case study: companies that owned their harness and routed through it simply switched endpoints and kept moving, while companies tied to a single model were blocked. He recommended treating model choice as a runtime routing decision, not a build-time commitment, and highlighted open-source models (GLM 5.2, Qwen, Kimi) as fallback targets.

## Relevance to YOLO loop

Our yolo loop should never have a single model as a hard dependency. This experiment validates building an abstraction layer (e.g., LiteLLM-style router or custom dispatcher) so that model swaps are config changes, not code changes. Directly reduces fragility in our CI/agent pipeline.

## Notes

Pairs well with the task-complexity routing card above — both point toward a unified routing layer.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-02 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-07-02-model-resilience-harness-ownership` |
| Channel | nb |
| Video | [Your AI Model is Probably Wrong for This Job](https://www.youtube.com/watch?v=lq2fP7wC7d8) |
| Published | 2026-07-02 |
| Ingested upstream | 2026-07-02 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
