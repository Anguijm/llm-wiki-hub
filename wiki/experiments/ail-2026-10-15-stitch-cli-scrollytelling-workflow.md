# Wire Google Stitch CLI into a Claude Code skill workflow alongside a domain-specific skill (e.g., scrollytelling) to produce fully designed and animated web pages without leaving the terminal

> Back to [[experiments-index]]

Source: **[Google Just Fixed AI Design By Releasing This](https://www.youtube.com/watch?v=au2TI8sdq8E)** · ail · 2026-10-15

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we install the Stitch CLI and add a Stitch skill plus a domain-specific skill (scrollytelling, or equivalent) to Claude Code, then the agent can handle design generation, design consistency, animation, and multi-device review in one automated workflow without manual Stitch prompting, because Stitch CLI is token-efficient (loads only when needed vs. MCP always-in-context) and skills let Claude orchestrate Stitch with domain knowledge it wouldn't otherwise have.

## What they did

AI Labs built a complete web workflow using Stitch CLI (Google's new terminal interface for Stitch, replacing the complex Google Cloud MCP setup), a Stitch skill (with design.md, design vocabulary, consistency guides, and review workflows), and a scrollytelling skill (scroll animation patterns and animation guide). Workflow: (1) install Stitch CLI + login, (2) install Stitch skill to .claude folder (must specify folder explicitly or it won't load), (3) install scrollytelling skill, (4) Claude Code prompts Stitch through CLI using both skills' guidance, (5) Stitch generates designs with consistent colors/fonts/images, (6) Claude exports and builds site, (7) design review skill checks built site against design.md across all screen sizes and reports mismatches, (8) Claude fixes layout issues, (9) scrollytelling animations added via skill, (10) story review skill audits animation quality against brief.md judged against award-winning site standards. They noted Stitch CLI uses fewer tokens than MCP because it only loads when needed.

## Relevance to YOLO loop

high: this is a complete Claude Code skill composition workflow — demonstrates how to chain multiple domain skills with an external design tool, with automated review loops at each stage.

## Notes

Install gotcha: Stitch CLI skill must be installed with explicit .claude folder path or Claude won't load it. The story review skill pattern (separate skill that audits quality against a brief.md) is reusable for other projects. All skills available in AIABS Pro community.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-15 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `ail-2026-10-15-stitch-cli-scrollytelling-workflow` |
| Channel | ail |
| Video | [Google Just Fixed AI Design By Releasing This](https://www.youtube.com/watch?v=au2TI8sdq8E) |
| Published | 2026-10-15 |
| Ingested upstream | 2026-10-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
