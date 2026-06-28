# Add outcome-weighted utility scoring to agent retrieval so memory relevance improves from past run success/failure signals

> Back to [[experiments-index]]

Source: **[User Signal Dies at the Retrieval Boundary - Sonam Pankaj, StarlightSearch](https://www.youtube.com/watch?v=Jx4ZFEAq6bY)** · aie · 2026-06-28

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we replace pure semantic similarity retrieval with a utility score (semantic similarity × historical helpfulness weight) that updates based on whether retrieved memories led to successful or failed task outcomes, then agents improve at recurring tasks over time without retraining or manual prompt engineering, because the retrieval layer learns which context is actually useful for execution rather than just topically similar.

## What they did

Sonam identified that 73% of agent pipeline failures stem from retrieval (not generation) and that eval signals (pass/fail) die in observability dashboards rather than feeding back into agent behaviour. He built 'Agent RX' (Runtime Experience) — a retrieval layer where memories carry a utility score (50% semantic similarity + 30% keyword score + 20% recency, adjusted by historical outcome feedback) rather than raw embedding distance. Memories are treated as reasoning artifacts (e.g. 'check settlement before refunding') not just facts. When enough memories (≈10) accumulate, their reasoning is baked into skills so the system prompt stays current without manual editing. In a product SQL agent demo, after one failure was submitted as feedback, the agent's tool-call trajectory changed — it now searches more broadly (finding 'wireless mouse' when asked for 'gaming mouse') rather than returning empty results. Benchmarks on TaLE Bench showed improvement from 66% to 76% baseline, and 80% with skills. The library is open-sourced as 'Reflect'.

## Relevance to YOLO loop

The YOLO loop currently has no feedback path from run outcomes back into retrieval. Agent RX's utility-score pattern would let the loop's memory system get smarter with each iteration — directly addressing the 'agent keeps failing at the same task' failure mode.

## Notes

Cold start limitation acknowledged — pure semantic search until sufficient outcome history. Noisy failure labels can corrupt utility scores. Lambda hyperparameter controls credit attribution in re-ranking. GitHub: Reflect library.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-28 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-06-28-agent-rx-outcome-informed-retrieval` |
| Channel | aie |
| Video | [User Signal Dies at the Retrieval Boundary - Sonam Pankaj, StarlightSearch](https://www.youtube.com/watch?v=Jx4ZFEAq6bY) |
| Published | 2026-06-28 |
| Ingested upstream | 2026-06-28 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
