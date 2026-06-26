# Build a wiki-generating memory layer between Obsidian/Readwise and coding agents to surface high-signal notes at task start

> Back to [[experiments-index]]

Source: **[Turn 10,994 Notes Into Memory - Paul Iusztin, Decoding AI & Louis-François Bouchard, Towards AI](https://www.youtube.com/watch?v=ZRM_TfEZcIo)** · aie · 2026-06-26

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we insert an AI Research OS layer that ingests personal notes (Obsidian, Readwise, Notion) and generates a queryable wiki with executive summaries and extracted entities, then agents working on new tasks can pull contextually relevant prior research without the human manually curating context because the system matches current task intent against a structured, agent-native knowledge graph.

## What they did

Paul Iusztin (Decoding AI) and Louis-François Bouchard (Towards AI) built an open-source 'AI Research OS' to solve the problem of 10,994+ notes across Obsidian, Readwise, and Notion that were effectively inaccessible during active work. The system: (1) ingests notes and external sources (GitHub repos, URLs) via connectors, (2) generates a structured wiki per project with executive summaries, extracted concepts, and entities, (3) exposes the wiki to agents (Claude Code, Codex) via a research query interface so agents can ask follow-up questions and update the wiki incrementally. Key design decisions: agent-native (CLI-first, no polished UI), does not replace NotebookLM but sits between it and the agent, preserves source provenance, and the wiki updates as agents discover new entities. They use it to prevent content duplication across videos and to anchor new work in personal values and prior decisions. Known weaknesses: needs more connectors (Google Drive, Slack), source freshness ranking is immature, memory compaction is hard.

## Relevance to YOLO loop

YOLO loop agents start each session with blank context about past decisions, prior implementations, and project conventions. A wiki memory layer seeded from dev notes and past sessions would let the loop agent reference prior architectural decisions and avoid re-solving solved problems — directly addressing the amnesia problem described in the Nx/Polygraph talk.

## Notes

Code repo available. Course: Towards AI Agent Engineering (~60hrs). The 250 files/month growth rate suggests the ingestion pipeline needs to be incremental not batch. Overlaps conceptually with Polygraph session memory from the Nx talk — worth comparing approaches.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-26 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-06-26-second-brain-ai-research-os` |
| Channel | aie |
| Video | [Turn 10,994 Notes Into Memory - Paul Iusztin, Decoding AI & Louis-François Bouchard, Towards AI](https://www.youtube.com/watch?v=ZRM_TfEZcIo) |
| Published | 2026-06-26 |
| Ingested upstream | 2026-06-26 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
