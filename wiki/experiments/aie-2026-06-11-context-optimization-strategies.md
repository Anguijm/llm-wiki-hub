# Replace full-codebase context dumps with ranked hierarchical summaries and knowledge graphs for agentic code review

> Back to [[experiments-index]]

Source: **[Why More Context Makes Your Agent Dumber and What to Do About It — Nupur Sharma, Qodo](https://www.youtube.com/watch?v=EcqMYoIV57A)** · aie · 2026-06-11

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we replace dumping entire codebases into agent context with a tiered approach (file/folder summaries for fast retrieval, plus a dependency knowledge graph for cross-repo reasoning), then agent review quality will improve and mid-context information loss will decrease, because LLMs demonstrably under-attend to tokens in the middle of long contexts and targeted retrieval ensures only high-signal content occupies those positions.

## What they did

Nupur Sharma from Qodo described observing a 'U-curve' attention pattern in LLMs used for agentic code review: models reliably attend to the beginning and end of context but drop information in the middle. She outlined three mitigation strategies they evaluated: (1) a context engine acting as a 'bouncer' with search ranking logic (effective but hard to scale past ~600 repos), (2) hierarchical summarization where each file/folder gets an LLM-generated summary indexed for retrieval (high upfront LLM cost but scalable), and (3) knowledge graphs encoding file dependency relationships in a graph DB (complex setup, high developer input, but excels at multi-repo logical dependency traversal). She also described a developer-feedback weighting loop where accepted/rejected suggestions adjust future context ranking.

## Relevance to YOLO loop

Core to our dev loop: any agent that reads our codebase suffers this U-curve problem. Testing hierarchical summaries as a retrieval layer before agent context injection is a concrete near-term experiment.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-11 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-06-11-context-optimization-strategies` |
| Channel | aie |
| Video | [Why More Context Makes Your Agent Dumber and What to Do About It — Nupur Sharma, Qodo](https://www.youtube.com/watch?v=EcqMYoIV57A) |
| Published | 2026-06-11 |
| Ingested upstream | 2026-06-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
