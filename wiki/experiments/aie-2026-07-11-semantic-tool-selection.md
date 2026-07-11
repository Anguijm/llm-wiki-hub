# Filter agent tool context with semantic vector search before each call

> Back to [[experiments-index]]

Source: **[Stop AI Agent Hallucinations: 5 Techniques + Production Patterns - Elizabeth Fuentes, AWS](https://www.youtube.com/watch?v=vJukHCIv7Ck)** · aie · 2026-07-11

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we build a vector database of tool descriptions and inject only the top-3 semantically relevant tools per query instead of all tools, then token usage per call drops dramatically (e.g., from ~3000 to ~300 tokens) and hallucination rates decrease because the model only sees tools relevant to the current task.

## What they did

Elizabeth demonstrated a travel agent with 29 tools (each schema ~17-200 tokens, ~3000 tokens total per call). She created a local vector store of tool embeddings using sentence-transformers (free, runs locally), then on each agent call performed a vector search against the user query to retrieve only the 3 most relevant tools. She swapped the full tool list for the filtered subset before invoking the Strands agent. Implemented in a Jupyter notebook using AWS Strands framework with OpenAI or Bedrock as model provider.

## Relevance to YOLO loop

Directly reduces context bloat in the YOLO loop's tool-calling layer — fewer tokens in means cheaper runs, less distraction, and fewer hallucinated tool calls on each agent invocation.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-11 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-11-semantic-tool-selection` |
| Channel | aie |
| Video | [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns - Elizabeth Fuentes, AWS](https://www.youtube.com/watch?v=vJukHCIv7Ck) |
| Published | 2026-07-11 |
| Ingested upstream | 2026-07-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
