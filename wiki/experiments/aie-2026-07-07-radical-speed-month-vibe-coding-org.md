# Run a time-boxed 'radical speed sprint' where non-engineers ship production code using AI tools

> Back to [[experiments-index]]

Source: **[500 people vibe-coded for 30 days. I was one of them. - Sanja Grbic, Automattic](https://www.youtube.com/watch?v=UcYoMg-8-L8)** · aie · 2026-07-07

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we run a structured 30-day sprint where non-engineering roles (designers, PMs) are paired in two-person teams with full autonomy to build and ship real projects using AI coding tools, then we will produce working production software faster than traditional handoff workflows and measurably shift participants' role identity and process habits, because removing negotiation/handover overhead and granting end-to-end ownership unlocks compounding productivity gains that tool access alone does not.

## What they did

Sanja described Automattic's 'Radical Speed Month': ~500 employees (first third of ~1,400) paused roadmap work for 30 days, paired into two-person teams, and were given full autonomy to build and ship something real. AI use was encouraged but not required. Prerequisites that made it work: company-wide AI enablement courses (role-specific, 2-week, immersive with hands-on time), security/process infrastructure from the ops team enabling non-engineers to spin up dev environments, and an MCP server (Context AC) giving AI tools access to decades of internal documentation. Sanja personally built three projects: (1) a board game session manager (4 people, 2 hours); (2) a Context AC-powered internal research tool (solo, 2.5 weeks, shipped to production); (3) a WooCommerce iOS merchant chat app with AI agent answering shopper questions (2 designers, 6 days, zero to working PoC). Key process shift: started prototyping directly in code rather than high-fidelity Figma, used Claude Code project folders to record all ideation/chats as a coordination artifact, and returned to Figma only for mood boarding and UI polish.

## Relevance to YOLO loop

Organizational experiment relevant if our team has non-engineers who could contribute to the loop with the right scaffolding. Immediately actionable process takeaway: use a Claude Code project folder as the shared ideation + build artifact from day one instead of separating design docs from implementation. The 'prototype in code first, Figma for polish' workflow is directly adoptable.

## Notes

794 projects started across ~500 people in 30 days. Sanja's personal arc from 'reviews PRs' to 'ships to production' in 30 days is a strong data point for the ceiling of what structured AI enablement can unlock. The MCP server for internal docs (Context AC) is worth investigating as a pattern for any team with significant institutional knowledge.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-07 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-07-radical-speed-month-vibe-coding-org` |
| Channel | aie |
| Video | [500 people vibe-coded for 30 days. I was one of them. - Sanja Grbic, Automattic](https://www.youtube.com/watch?v=UcYoMg-8-L8) |
| Published | 2026-07-07 |
| Ingested upstream | 2026-07-07 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
