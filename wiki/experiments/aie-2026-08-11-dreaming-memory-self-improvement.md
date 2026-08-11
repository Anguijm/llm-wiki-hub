# Add a periodic 'dreaming' batch pass that distills session transcripts into updated agent memory

> Back to [[experiments-index]]

Source: **[Evolution of agentic surfaces — Gagan Bhat & Isabella Kai He, Anthropic](https://www.youtube.com/watch?v=K0X9QDRkIdg)** · aie · 2026-08-11

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we run a scheduled batch process that feeds an agent's session transcripts and current memory state to a model with instructions to extract new insights and update the memory store, then subsequent agent sessions become progressively more intelligent without manual prompt tuning because the agent accumulates structured learnings from its own execution history.

## What they did

Gagan described 'dreaming' as a periodic batch process used in Claude Managed Agents: session logs (transcripts) and the agent's current memory state are fed to the model, which extracts new insights and reorganizes/edits the memory. This creates a self-improving loop where daily agent sessions automatically get better over time. He positioned this alongside persistent memory as two cornerstones of a 'unified memory system', with a third emerging layer of organizational-scale memory storing team runbooks.

## Relevance to YOLO loop

Maps to a post-run reflection step in our dev loop — after each YOLO loop execution, a dreaming pass could update a shared CLAUDE.md or memory file with lessons learned, reducing repeated mistakes across sessions without human intervention.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-11 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-11-dreaming-memory-self-improvement` |
| Channel | aie |
| Video | [Evolution of agentic surfaces — Gagan Bhat & Isabella Kai He, Anthropic](https://www.youtube.com/watch?v=K0X9QDRkIdg) |
| Published | 2026-08-11 |
| Ingested upstream | 2026-08-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
