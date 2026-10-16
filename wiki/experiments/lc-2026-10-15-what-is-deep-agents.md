# Adopt a swappable-backend agent harness to run the same agent locally, in sandbox, or in cloud without code changes

> Back to [[experiments-index]]

Source: **[What is Deep Agents?](https://www.youtube.com/watch?v=8gCam2-iGLc)** · lc · 2026-10-15

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we design an agent harness with a swappable file-system backend and plug-in skills/sub-agents, then the same agent code can run on a laptop, in a sandbox, or in the cloud without modification, because the harness abstracts environment-specific infrastructure away from agent logic.

## What they did

LangChain described Deep Agents, their open-source agent harness. It ships with: a swappable file system (laptop/sandbox/cloud), skills that load on demand, sub-agents for parallelization, summarization for long-context control, sandboxes for untrusted code, human-in-the-loop gates, and agent auth. The harness is fully customizable without rebuilding from scratch.

## Relevance to YOLO loop

high: the harness concept with swappable backends, skills, sub-agents, and human-in-the-loop gates maps directly to the operator's Claude Code agent harness and hooks/council architecture.

## Notes

Companion explainer to the Stripe Kai video. LangChain Academy has a free Deep Agents course. Key primitives: file system, skills, sub-agents, summarization, sandboxes, human-in-the-loop, agent auth.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-15 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `lc-2026-10-15-what-is-deep-agents` |
| Channel | lc |
| Video | [What is Deep Agents?](https://www.youtube.com/watch?v=8gCam2-iGLc) |
| Published | 2026-10-15 |
| Ingested upstream | 2026-10-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
