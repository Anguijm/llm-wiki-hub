# Build a Domain-Expert Agent by Crawling Public Sources into a Structured Wiki

> Back to [[experiments-index]]

Source: **[I Built Another Andrej Karpathy Using Claude](https://www.youtube.com/watch?v=bvGptCLDhyo)** · nh · 2026-10-06

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we crawl all public writing, transcripts, and posts from a domain expert and compile them into a linked wiki (not a raw dump), then a Claude agent grounded in that wiki will explain and teach that expert's domain more accurately and in their style, because structured relationships in the wiki allow the model to retrieve and reason over the knowledge more effectively than a flat folder of text.

## What they did

The speaker used Claude Code to run parallel agents that scraped Andrej Karpathy's YouTube captions (via youtube-transcript-api and yt-dlp), X/Twitter posts (via twitterapi.io at ~$1), blogs, and GitHub repos into a raw folder totalling 700k+ words. A second prompt had an LLM compile those raw sources into a navigable wiki with pages, an index, a hot-topics page, and a change log — mirroring a technique Karpathy himself posted about. A third prompt extracted Karpathy's teaching rules (e.g. 'build the smallest version first', 'predict before you run', 'show the broken version') with supporting quotes. A fourth prompt encoded those rules as agent behaviors in a Claude system prompt. The resulting agent was tested by asking it to build a byte-pair tokenizer: it wrote a success definition before coding, built the smallest working version, predicted output before running, showed the real output, showed a breaking version, fixed it, and logged which rule governed each step. A /karpathy-ingest slash command was also built to add new links and auto-update the wiki without manual edits.

## Relevance to YOLO loop

Directly addresses the knowledge-grounding problem in our dev loop: instead of relying on Claude's base training for domain expertise, we pre-load curated expert knowledge into a structured wiki and wire it into the system prompt, giving every agent invocation a richer, more accurate context. The wiki-update slash command also maps to our loop's continuous-improvement step — new sources keep the agent current without rebuilding from scratch.

## Notes

Key tooling: youtube-transcript-api, yt-dlp, twitterapi.io. The two-stage pipeline (raw crawl → LLM-compiled wiki) is the core insight — skipping the wiki step leaves a needle-in-haystack retrieval problem. Parallel agents per source kept crawl time to ~45-60 min. Rule extraction with supporting quotes is reusable for any domain expert or methodology author.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-06 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-10-06-karpathy-wiki-agent` |
| Channel | nh |
| Video | [I Built Another Andrej Karpathy Using Claude](https://www.youtube.com/watch?v=bvGptCLDhyo) |
| Published | 2026-10-06 |
| Ingested upstream | 2026-10-06 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
