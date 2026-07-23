# Replace multi-agent context handoff chains with a single reasoning agent navigating a knowledge graph control plane

> Back to [[experiments-index]]

Source: **[Why We Killed Our Multi-Agent Pipeline — Subbiah Sethuraman and Abhilash Asokan, ZS Associates](https://www.youtube.com/watch?v=u6jJcIFDLE4)** · aie · 2026-07-23

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we replace a pipeline of specialized agents that pass context between each other with a single reasoning agent that traverses a domain knowledge graph (where every edge is a hypothesis to evaluate), then end-to-end analytical coherence improves because context is never lost at handoff boundaries and the agent's investigation is bounded to semantically valid paths rather than open-ended generation.

## What they did

ZS Associates described building and then killing a 4-agent pipeline (signal detection → source localization → driver attribution → synthesis) for pharma commercial analytics. The pipeline produced locally correct outputs at each step but incoherent end-to-end conclusions — the synthesis agent didn't understand why the driver attribution agent reached its conclusion, so actions didn't match causes. Root cause: context loss at each handoff and LLMs doing deterministic work (signal detection) that statistical methods should handle. Their fix: one reasoning agent that owns end-to-end reasoning, navigates a domain knowledge graph (entities: geographies, payers, accounts, brands, KPIs and their relationships) where each edge is a testable hypothesis. The agent loops through graph neighborhoods, fetches data, evaluates hypotheses, and traverses until root cause is found or hypotheses are exhausted — 50+ turns, completing in 20-30 minutes what analysts took 3-4 weeks to do.

## Relevance to YOLO loop

Our yolo loop may have implicit multi-agent handoffs where context degrades across steps. This experiment suggests auditing which steps are losing reasoning coherence and whether consolidating them under a single agent with a domain graph control plane would improve end-to-end output quality over the current decomposed architecture.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-23 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-23-knowledge-graph-as-agent-control-plane` |
| Channel | aie |
| Video | [Why We Killed Our Multi-Agent Pipeline — Subbiah Sethuraman and Abhilash Asokan, ZS Associates](https://www.youtube.com/watch?v=u6jJcIFDLE4) |
| Published | 2026-07-23 |
| Ingested upstream | 2026-07-23 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
