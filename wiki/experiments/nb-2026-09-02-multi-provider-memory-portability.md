# Store Memory and Context Outside Any Single AI Provider

> Back to [[experiments-index]]

Source: **[OpenAI, NVIDIA And Anthropic Just Split. Here's How I'd Spend $20, $60 Or $200.](https://www.youtube.com/watch?v=L9xXnPqVfnM)** · nb · 2026-09-02

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we maintain all project memory, instructions, and context in provider-agnostic files rather than inside any single AI platform, then switching between models (or surviving a provider outage/policy change) will be far less disruptive because no one vendor holds the only copy of our working context.

## What they did

Nate described deliberately keeping his memory, files, and instructions separate from any single AI provider's ecosystem, mirroring Anthropic's multi-supplier strategy at the individual user level. He shared his own context and memory with multiple models (e.g., both Codex and Claude) so that switching between them felt relatively seamless, even if not perfectly so.

## Relevance to YOLO loop

Directly applies to the YOLO loop's context management layer: externalizing CLAUDE.md, system prompts, and memory files into version-controlled plain text means any agent in the loop can be swapped without losing accumulated project knowledge.

## Notes

Nate frames this as the individual analogue to Anthropic's strategy of maintaining multiple compute suppliers. The practical implementation is keeping CLAUDE.md / system prompt files and memory exports in git, not locked in any app's proprietary memory store.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-02 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-09-02-multi-provider-memory-portability` |
| Channel | nb |
| Video | [OpenAI, NVIDIA And Anthropic Just Split. Here's How I'd Spend $20, $60 Or $200.](https://www.youtube.com/watch?v=L9xXnPqVfnM) |
| Published | 2026-09-02 |
| Ingested upstream | 2026-09-02 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
