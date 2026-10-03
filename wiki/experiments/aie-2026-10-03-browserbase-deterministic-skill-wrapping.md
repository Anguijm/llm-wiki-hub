# Wrap Browser Agent Steps in Deterministic Tool Calls to Reduce Compound Failure Rate

> Back to [[experiments-index]]

Source: **[Why 99% Accurate Browser Agents Still Fail — Derek Meegan, Browserbase](https://www.youtube.com/watch?v=5xi_S1f9sDU)** · aie · 2026-10-03

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we encapsulate complex, multi-step browser interactions (e.g., authentication, file download, entity extraction) into single deterministic tool calls rather than leaving each step to the agent's probability distribution, then end-to-end task success rate will increase significantly because each encapsulation reduces the number of probabilistic steps the agent must take, directly improving the compound success probability.

## What they did

Derek Meegan of Browserbase demonstrated the math of compound failure: a 100-step agent with 99% per-step accuracy succeeds only 36% of the time. Their solution was systematic step reduction through deterministic encapsulation: pull authentication out of the model entirely into a serverless function, wrap download-plus-retrieve into a single tool call, add a deterministic OCR verification tool, then provide a skill document (standard operating procedure for the agent) to guide it along the critical path. The final architecture reduced the number of steps the model was responsible for to only the genuinely ambiguous ones, raising success rate to production-viable levels.

## Relevance to YOLO loop

Core pattern for any multi-step agentic workflow in our dev loop. Auditing our existing agent pipelines to identify which steps could be converted from 'model decides' to 'deterministic tool call' is a low-effort, high-leverage reliability improvement.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-03 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-03-browserbase-deterministic-skill-wrapping` |
| Channel | aie |
| Video | [Why 99% Accurate Browser Agents Still Fail — Derek Meegan, Browserbase](https://www.youtube.com/watch?v=5xi_S1f9sDU) |
| Published | 2026-10-03 |
| Ingested upstream | 2026-10-03 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
