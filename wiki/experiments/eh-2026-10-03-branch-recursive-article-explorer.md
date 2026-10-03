# Build a Recursive Link-Following Research Tool That Traces Every Insight to Its Source

> Back to [[experiments-index]]

Source: **[One Article In, 61 Insights Out, Each Traced to Its Source](https://www.youtube.com/watch?v=EjGyPSTDngI)** · eh · 2026-10-03

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we build a tool that takes one article URL, recursively follows its citations (five sources per level), extracts key insights, and links each insight back to the exact source passage, then research synthesis time will drop dramatically because verification is one click away and hallucinated citations are automatically dropped.

## What they did

The echohive team built 'Branch' live during a Sunday lab session. It accepts a public article URL, follows its links and the links of those links (five at a time), reads the connected articles, and extracts key insights—61 from one essay in 46 seconds across 13 articles. Each insight links back to the exact highlighted passage in the source. Insights where the quote didn't match the source word-for-word were automatically dropped. The interface runs locally; analysis uses the user's signed-in Codex CLI.

## Relevance to YOLO loop

Maps to our research and context-gathering phase. When we need to synthesize a technical area quickly (e.g., before designing a new system), a Branch-style tool would let us feed one authoritative article and get a verified, source-traced knowledge graph rather than manually reading a citation tree.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-03 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `eh-2026-10-03-branch-recursive-article-explorer` |
| Channel | eh |
| Video | [One Article In, 61 Insights Out, Each Traced to Its Source](https://www.youtube.com/watch?v=EjGyPSTDngI) |
| Published | 2026-10-03 |
| Ingested upstream | 2026-10-03 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
