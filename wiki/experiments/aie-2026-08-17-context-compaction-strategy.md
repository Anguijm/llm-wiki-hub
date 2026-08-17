# Default to Full Context Retention with Lazy Compaction Threshold Instead of Eager Summarization

> Back to [[experiments-index]]

Source: **[Context Engineering in 2026 — Louis-François Bouchard, Omar Solano & Samridhi Vaid, Towards AI](https://www.youtube.com/watch?v=WP3hjUXd918)** · aie · 2026-08-17

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we keep the full chat history until a token threshold (e.g., 30k tokens) rather than eagerly summarizing, then answer recall will stay near 95% because summarization discards details that the model needs, while prompt caching makes resending large contexts cheap enough that retention is cost-competitive with compaction.

## What they did

Towards AI ran a systematic experiment series on their AI tutor to fix context rot. They compared full-history retention vs. summarization vs. hybrid retrieval across multiple models (Gemini, DeepSeek, local). Key findings: keeping full chat history gave ~95% recall vs. ~32% with summarization; prompt caching made large context resends cheap (cheapest cost-per-turn was the run sending the most tokens); BM25 retrieval maintained 100% recall at 400k tokens where dense semantic search collapsed to 0%; hybrid retrieval (dense + BM25) was the chosen architecture. They concluded: do not compact by default—identify the actual constraint first.

## Relevance to YOLO loop

Context management is a core loop engineering problem. This experiment gives us a concrete decision rule: use full retention + hybrid retrieval until 30k tokens, then compact. Applying this to the YOLO loop's agent sessions would reduce context-rot failures on long coding tasks without unnecessary summarization overhead.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-17 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-17-context-compaction-strategy` |
| Channel | aie |
| Video | [Context Engineering in 2026 — Louis-François Bouchard, Omar Solano & Samridhi Vaid, Towards AI](https://www.youtube.com/watch?v=WP3hjUXd918) |
| Published | 2026-08-17 |
| Ingested upstream | 2026-08-17 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
