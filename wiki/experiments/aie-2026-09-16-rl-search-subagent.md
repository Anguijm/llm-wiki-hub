# Delegate All Search to a Specialized RL-Trained Sub-Agent to Reduce Main Agent Token Spend by 30-50%

> Back to [[experiments-index]]

Source: **[Where RL Will Take Search — Maximilian-David Rumpf, SID.ai](https://www.youtube.com/watch?v=iJVxxxHM_Oc)** · aie · 2026-09-16

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we route all retrieval tasks from the main agent to a dedicated search sub-agent (trained or specialized for search), then the main agent's context window will contain only high-quality results, reducing wasted tokens by 30-50% and improving overall task accuracy because search pollution of the main context is eliminated.

## What they did

Maximilian-David Rumpf (SID.ai) described a production architecture where a specialized RL-trained search model (SID-1) handles all retrieval on behalf of the main agent. The sub-agent iterates with the database — searching, reading results, setting metadata filters, and re-searching — until satisfied, then returns a ranked list of high-quality results to the main agent. The main agent never sees intermediate bad results. RL training used a verifiable reward (did the model find the correct document?) with thousands of training episodes per second. Results: ~20x faster than frontier model search (5s vs ~2 min average), ~100x cheaper, and the main agent's 30-50% token overhead for searching is offloaded to the cheap sub-agent. The approach follows scaling laws with no observed ceiling.

## Relevance to YOLO loop

Architecturally relevant: even without training our own RL search model, we can apply the pattern of delegating all retrieval to a specialized sub-agent/tool call that iterates internally, keeping the main coding agent's context clean and focused on reasoning rather than search.

## Notes

SID.ai is a stealthish lab; SID-1 model not publicly available as of talk date. The architectural pattern (search sub-agent isolating main agent from retrieval noise) is implementable today with existing tools even without RL training. Key insight: 30-50% of main agent tokens currently spent on search can be offloaded.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-16 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-16-rl-search-subagent` |
| Channel | aie |
| Video | [Where RL Will Take Search — Maximilian-David Rumpf, SID.ai](https://www.youtube.com/watch?v=iJVxxxHM_Oc) |
| Published | 2026-09-16 |
| Ingested upstream | 2026-09-16 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
