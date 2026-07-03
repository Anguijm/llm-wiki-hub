# Ingest YouTube transcripts into a Claude Code-maintained LLM wiki with backlink graph

> Back to [[experiments-index]]

Source: **[Fable 5 + Karpathy's LLM Wiki is Basically Cheating](https://www.youtube.com/watch?v=hQvwMj7IJe4)** · nh · 2026-07-03

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we use Claude Code to auto-ingest YouTube transcripts (or other document sources) into a markdown-based LLM wiki with concept nodes and backlinks, then an AI agent will have richer, self-navigating context about our domain because the wiki structure exposes relationships between ideas that flat transcript dumps do not.

## What they did

The speaker used Claude Code to grab YouTube video transcripts and ingest them into an Obsidian-style markdown wiki (powered by Fable). Each video becomes a node with summary, key takeaways, tools mentioned, and bidirectional links to related concepts. He maintains multiple wikis (YouTube transcripts, meeting recordings, business context). Fable was then prompted in a single pass to generate an HTML concept map from the wiki, producing a more beginner-friendly visualization than a multi-day effort with Opus 4.8 had. He also demonstrated ingesting two competing AI safety articles into a mini wiki where cross-source contradictions (different benchmark harnesses) were automatically flagged. The wiki is portable: it's just markdown files with routing rules, so any agent (Claude Code, Hermes, Codex) can query it.

## Relevance to YOLO loop

Directly relevant to our memory and context layer. A markdown wiki with routing rules is a lightweight, model-agnostic long-term memory store. The backlink graph approach means our YOLO loop agents can navigate prior decisions and code patterns rather than starting cold each session.

## Notes

Key insight: routing rules in the wiki (CLAUDE.md or equivalent) let the agent efficiently crawl without exhausting token budget. Different wiki instances can have different ingestion rules based on data type. Fable's single-shot HTML generation from the wiki graph is a good benchmark task to replicate.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-03 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-07-03-llm-wiki-fable-youtube-transcripts` |
| Channel | nh |
| Video | [Fable 5 + Karpathy's LLM Wiki is Basically Cheating](https://www.youtube.com/watch?v=hQvwMj7IJe4) |
| Published | 2026-07-03 |
| Ingested upstream | 2026-07-03 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
