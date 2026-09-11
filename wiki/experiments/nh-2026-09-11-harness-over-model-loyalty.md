# Decouple Agent Harness from Model Provider to Enable Swappable Brains

> Back to [[experiments-index]]

Source: **[How to Actually Choose the Right AI Agent](https://www.youtube.com/watch?v=6LNlCpQPYFc)** · nh · 2026-09-11

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we invest in a well-defined agent harness (file read/write, bash execution, MCP tools, skills/rules) that is model-agnostic, then we can swap underlying models (Claude, Codex, local OSS) with minimal disruption because the harness — not the model — is the primary driver of task completion quality.

## What they did

Mark Kashef and Nate Herk argued that the 'brain in a jar' (the LLM) is far less important than the harness around it — the tools that give it hands and legs (file access, bash, cloud integrations). They demonstrated the gap between Claude on the web (no local file access) vs Claude Code (full harness). Mark described maintaining loyalty to his harness and assets rather than any provider, rotating models interchangeably. He also described segmenting operating systems per project (tax/finance, consulting, content) rather than one global system, promoting rules from project-level to global only when proven, and auditing by isolating variables: is this a model problem, a harness problem, or an organization problem?

## Relevance to YOLO loop

Core architectural principle for our YOLO loop: the loop's reliability should be measured against the harness configuration, not blamed on the model. Segmenting project-level CLAUDE.md/rules files and only promoting to global when validated mirrors our need to control blast radius and identify regressions cleanly.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-11 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-09-11-harness-over-model-loyalty` |
| Channel | nh |
| Video | [How to Actually Choose the Right AI Agent](https://www.youtube.com/watch?v=6LNlCpQPYFc) |
| Published | 2026-09-11 |
| Ingested upstream | 2026-09-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
