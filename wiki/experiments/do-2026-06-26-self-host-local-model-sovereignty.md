# Set up a locally-hosted fallback model so the dev loop survives API access disruptions

> Back to [[experiments-index]]

Source: **[GPT 5.6 is out… but not for you lol](https://www.youtube.com/watch?v=IloXWEYXen8)** · do · 2026-06-26

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we maintain at least one locally-runnable model (e.g., Qwen, Deepseek, GLM) as a hot standby in the dev loop, then we can continue shipping when frontier API access is restricted or revoked because inference runs on owned hardware without dependency on external policy decisions.

## What they did

David and his guest argued that closed-source frontier models are increasingly subject to government-imposed access restrictions, citing two consecutive bans in two weeks. They prescribed three concrete steps: (1) download and run at least one model locally now regardless of size, (2) shift a percentage of token usage to open-source models like Kimi, MiniMax, GLM, Deepseek to build familiarity, and (3) invest in local inference hardware (GPU or beefy MacBook) or join a community inference pool. The framing was that in 5 years a super-intelligent model with revocable access becomes a single point of failure for any AI-dependent workflow.

## Relevance to YOLO loop

YOLO loop currently depends on Claude/OpenAI APIs. A local fallback model — even a smaller one — would let the loop degrade gracefully rather than halt completely if API access is cut. Also relevant for cost control on high-volume loop runs.

## Notes

Primarily commentary/opinion but contains the specific 3-step actionable prescription. Experiment scope: install Ollama + Qwen or GLM locally, wire it as a fallback provider in the loop config, measure quality delta vs frontier on representative loop tasks.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-26 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-06-26-self-host-local-model-sovereignty` |
| Channel | do |
| Video | [GPT 5.6 is out… but not for you lol](https://www.youtube.com/watch?v=IloXWEYXen8) |
| Published | 2026-06-26 |
| Ingested upstream | 2026-06-26 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
