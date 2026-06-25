# Connect Hermes Agent to Apify MCP for unrestricted web scraping

> Back to [[experiments-index]]

Source: **[This MCP makes Hermes Agent 10x more powerful](https://www.youtube.com/watch?v=V80QfRa7t_c)** · do · 2026-06-15

**Status:** `discarded` · **Verdict:** `discard` · **Effort:** `medium`

---

## Hypothesis

If we connect Hermes Agent to Apify via MCP connectors, then the agent can scrape otherwise-blocked websites (LinkedIn, Instagram, TikTok, etc.) and automate data pipelines because Apify provides 40,000+ actors as MCP-accessible tools that handle anti-bot restrictions.

## What they did

Installed Hermes Agent locally via a single terminal command, then connected it to Apify's MCP connector which exposes 40,000+ scraping actors. Used a LinkedIn profile scraper actor (no login/cookies required) to find software engineering candidates, had Hermes analyze and score the profiles, saved results to a database, and set up a scheduled Apify task running every 6 hours. Hermes then generated a cron job to deliver a daily top-5 candidate digest automatically.

## Relevance to YOLO loop

Directly extends any agent in the YOLO loop with external data acquisition. The MCP connector pattern lets agents pull live web data without custom scraping code, which is useful for research, lead gen, and competitive monitoring steps in automated workflows.

## Notes

Apify is the sponsor. Video includes free bundle link with MCP config, prompts, and SQL scripts. LinkedIn scraping actor specifically chosen for lower ban risk — no login or cookies needed.

Backlog triage 2026-06-24 (owner-preference model). Gray-area social scraping via Hermes/Apify — off-focus.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-15 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-06-15-hermes-apify-mcp-scraping` |
| Channel | do |
| Video | [This MCP makes Hermes Agent 10x more powerful](https://www.youtube.com/watch?v=V80QfRa7t_c) |
| Published | 2026-06-15 |
| Ingested upstream | 2026-06-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
