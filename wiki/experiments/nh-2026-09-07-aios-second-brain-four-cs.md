# Build a Four-C AI Operating System (Context, Connections, Capabilities, Cadence) as a Persistent Knowledge Base for Agents

> Back to [[experiments-index]]

Source: **[I Turned GPT-6 Astra Into the Ultimate AI Second Brain](https://www.youtube.com/watch?v=yysILVsfLFM)** · nh · 2026-09-07

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we structure an AI operating system around four components — static context (goals, background, business info), live connections (email, Slack, calendar, project management), capabilities (skills/agents), and cadence (scheduled routines) — and store all of it as files and folders accessible to any agent, then every agent interaction will produce specific, high-quality outputs rather than generic responses, because the agent always has just-in-time retrieval of rich, owner-specific knowledge without vendor lock-in.

## What they did

Speaker built a personal AIOS called 'Herk Brain' using Codex/GPT-6 Astra. The knowledge base includes: a business wiki with relationship graphs showing staleness indicators, meeting transcripts with AI summaries, all YouTube video knowledge linked to business nodes, Claude and Codex memory exports, projects, skills, and agent definitions. On top of this he built an OS dashboard with live-synced calendar, YouTube/community subscriber stats, Slack/ClickUp/email integration for responding without tab-switching, and an 'industry pulse' feed. He defined a 'Four C's' framework: Context (stable facts about you/business), Connections (live tool integrations), Capabilities (skills/agents), Cadence (scheduled routines). He also defined three self-tests: would your AIOS answer a teammate question better/faster than you? Can you do everything from one interface? Do you trust retrieval enough to stop memorizing decisions?

## Relevance to YOLO loop

This is essentially a formalized version of our own dev-loop context management problem. The Four-C framework and the audit-then-level-up loop are directly applicable to how we structure persistent context for our agents. The vendor-lock-in point (store as plain files/folders) is a strong architectural constraint worth adopting.

## Notes

Speaker recommends using cheaper models (GPT-5.6 Soul) for routine AIOS queries to preserve Astra usage limits; reserve Astra for high-complexity tasks. Architecture is plain files/folders so any future agent or model can crawl it — intentional anti-lock-in design. '3D brain' skill visualizes the knowledge graph as an interactive local-hosted site.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-07 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-09-07-aios-second-brain-four-cs` |
| Channel | nh |
| Video | [I Turned GPT-6 Astra Into the Ultimate AI Second Brain](https://www.youtube.com/watch?v=yysILVsfLFM) |
| Published | 2026-09-07 |
| Ingested upstream | 2026-09-07 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
