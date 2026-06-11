# Build a Knowledge-Grounded Voice Agent via Claude Code and ElevenLabs in a Single Session

> Back to [[experiments-index]]

Source: **[Building Realistic Voice Agents Has Never Been Easier](https://www.youtube.com/watch?v=-cdexJWN8YA)** · nh · 2026-05-04

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we use Claude Code to scaffold, configure, and deploy an ElevenLabs voice agent entirely through natural-language prompting — including transcript ingestion, system prompt generation, tool wiring, and widget embedding — then we can produce a functional, knowledge-grounded voice interface in under an hour without manual API configuration, because Claude Code can handle the research, architecture decisions, and boilerplate that previously required manual platform navigation.

## What they did

The speaker used Claude Code to build a voice agent backed by all 400 of his YouTube transcripts and deployed via ElevenLabs, completing the project in approximately 15 minutes of active prompting. He described the four core components of any voice agent (persona/system prompt, voice, knowledge base, tools), showed a live demo of the agent answering questions about his content, and walked through iterative refinement of the agent over a 45-minute demo session. He also covered production security considerations: domain-locking the widget, setting conversation duration caps, rate limiting, and using Claude Code to help design those guardrails.

## Relevance to YOLO loop

Maps to the YOLO loop's tool-building and interface layer — specifically, using Claude Code as the build agent to scaffold external API integrations (ElevenLabs, vector stores) from a high-level natural language spec. Demonstrates a pattern where the loop's agentic coder handles multi-step integration work including knowledge ingestion, prompt engineering, and frontend embedding without human-written boilerplate.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-05-04 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-05-04-voice-agent-claude-code-elevenlabs` |
| Channel | nh |
| Video | [Building Realistic Voice Agents Has Never Been Easier](https://www.youtube.com/watch?v=-cdexJWN8YA) |
| Published | 2026-05-04 |
| Ingested upstream | 2026-05-04 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
