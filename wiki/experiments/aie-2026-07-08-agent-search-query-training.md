# Instruct agents to write retrieval queries as natural sentences rather than keyword strings

> Back to [[experiments-index]]

Source: **[How we taught agents to use good retrieval - Hanna Lichtenberg, Mixedbread AI](https://www.youtube.com/watch?v=1IdzkRVmWAA)** · aie · 2026-07-08

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we prompt agents to describe what they want to find as 'one concise sentence' instead of asking them to 'write a search query', then retrieval quality against semantic search systems will improve significantly, because models default to BM25-style keyword stacking due to training on code and web tasks, and this prompt reframe bypasses that pattern to produce queries better suited to dense/semantic retrieval.

## What they did

Hannah Lichtenberg and Amir from Mixedbread diagnosed a 'knowledge gap' between rapidly improving LLM reasoning and slowly improving retrieval: models like Codex with default tools scored 9% on BrowseComp vs. a 93% oracle ceiling. They found the root cause was agents writing grep-style or BM25-style keyword queries (e.g., 'senator woman questions billionaires not a company') when given semantic search tools, because models are trained on coding tasks using grep and web tasks using human-style keyword queries. Their fix had two parts: (1) a prompt-level trick—instructing the agent to write 'one concise sentence describing what it wants to find' instead of 'a search query'—plus few-shot examples of good semantic queries; (2) training a small LLM agent via supervised fine-tuning from a teacher LLM followed by on-policy RL with a combined retrieval reward (NDCG + LLM retrieval judge) and trajectory reward (LLM judge on query naturalness, exploration sufficiency, and tool choice quality). They also built a four-tool harness: overview search (50 chunks, summaries only), semantic search (top 10 full chunks), filter/metadata search, and grep—with up to 4 parallel search rounds.

## Relevance to YOLO loop

Our dev loop uses retrieval for context fetching (docs, codebase, issues). Replacing current query-construction prompts with a 'describe what you want to find in one sentence' instruction is a minimal change that could immediately improve retrieval precision in RAG steps without any retraining.

## Notes

The low-effort experiment is just the prompt reframe. The full training pipeline (SFT + on-policy RL with retrieval reward) is a separate high-effort experiment. Their beta agent achieved 93.4% on Snowflake's Arctic QA benchmark and topped the leaderboard. NDCG@10 of 0.40 vs. 0.18 for GPT multi-hop on Oblique Congress benchmark.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-08 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-08-agent-search-query-training` |
| Channel | aie |
| Video | [How we taught agents to use good retrieval - Hanna Lichtenberg, Mixedbread AI](https://www.youtube.com/watch?v=1IdzkRVmWAA) |
| Published | 2026-07-08 |
| Ingested upstream | 2026-07-08 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
