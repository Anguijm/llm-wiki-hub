# Use Claude Code as natural-language orchestrator over Clay MCP for end-to-end lead enrichment

> Back to [[experiments-index]]

Source: **[Claude Code + Clay Makes Lead Generation Actually Fun](https://www.youtube.com/watch?v=zyvdl__Ywfk)** · nh · 2026-07-12

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we connect Claude Code to Clay via its MCP server and provide rich business-context files (profile, case studies, offer, website copy), then Claude Code can orchestrate the full lead-gen pipeline—sourcing, enriching, and writing personalized outreach—in a single natural-language prompt, because Claude Code can navigate API endpoints autonomously and personalization quality depends on context depth, not UI skill.

## What they did

Nate Herk demonstrated connecting Claude Code to Clay's MCP server so that a single natural-language prompt triggers: (1) Clay sourcing ~50 targeted leads, (2) Clay waterfall-enriching emails/phone numbers across multiple data providers (achieving ~80-90% hit rate vs ~30% from a single vendor), (3) Claude Code writing personalized subject lines and email bodies using pre-loaded context files (business profile, case studies, FAQs, offer, website copy), and (4) exporting a CSV that can be uploaded directly into Clay to purchase warmed domains and launch a sending campaign. He emphasized that the context files act as a prerequisite—without them Claude Code cannot write quality cold copy.

## Relevance to YOLO loop

Demonstrates the MCP-as-data-source pattern: instead of building a custom tool, wire an existing SaaS (Clay) to Claude Code via MCP and let the agent figure out the endpoints. The context-file prerequisite maps directly to our AIOS second-brain pattern for any agent that needs domain knowledge to produce quality output.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-12 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-07-12-claude-code-clay-lead-gen` |
| Channel | nh |
| Video | [Claude Code + Clay Makes Lead Generation Actually Fun](https://www.youtube.com/watch?v=zyvdl__Ywfk) |
| Published | 2026-07-12 |
| Ingested upstream | 2026-07-12 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
