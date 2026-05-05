# Build a User-Controlled Memory Layer Between LLM and Platform

> Back to [[experiments-index]]

Source: **[Anthropic And OpenAI Are Fighting Over Your Memory. You're Going To Lose.](https://www.youtube.com/watch?v=4KAF72BTyCE)** · NateBJones · 2026-04-17

**Status:** `deferred` · **Effort:** `medium`

---

## Hypothesis

If we implement a local or self-hosted memory store that intercepts and controls what context is persisted before it reaches the LLM provider, then we retain ownership of memory and reduce dependency on platform-controlled memory features because data never leaves our stack without explicit consent.

## What they did

Speaker argues that both Anthropic and OpenAI are building proprietary memory systems that lock user context into their platforms, meaning users lose control over what is remembered, how it is used, and whether it can be exported or deleted. He frames this as a data sovereignty issue and implicitly suggests that developers should build memory abstraction layers outside of the LLM provider.

## Relevance to YOLO loop

Our YOLO loop currently passes context directly to the LLM API with no intermediate memory management. Adding a portable memory store (e.g., a local vector DB or structured JSON store) between our orchestration layer and the LLM call would decouple memory from the provider and let us experiment with memory strategies independently of whatever OpenAI or Anthropic ships.

## Notes

Overlaps with build_memory.py + infra-memory-feedback in progress. Revisit as a follow-on tick after memory-feedback ships.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-17 | `backlog` | Extracted from YouTube RSS |
| 2026-04-22 | `deferred` | Overlaps with build_memory.py + infra-memory-feedback in progress. Revisit as a follow-on tick after memory-feedback ships. |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-04-17-memory-control-layer` |
| Channel | NateBJones |
| Video | [Anthropic And OpenAI Are Fighting Over Your Memory. You're Going To Lose.](https://www.youtube.com/watch?v=4KAF72BTyCE) |
| Published | 2026-04-17 |
| Ingested upstream | 2026-04-17 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
