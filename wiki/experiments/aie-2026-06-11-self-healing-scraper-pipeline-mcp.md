# Use Bright Data MCP + LLM agent to auto-generate, execute, and self-heal web scrapers instead of calling LLM per page

> Back to [[experiments-index]]

Source: **[From MCP to Scale: Pipelines That Build Themselves — Rafael Levi, Bright Data](https://www.youtube.com/watch?v=zTZ0qunQXnM)** · aie · 2026-06-11

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we give an LLM agent the Bright Data MCP (which provides HTML extraction, selector discovery, and anti-bot bypass) plus a skills/best-practices GitHub repo, then the agent can generate a reusable scraper script that parses thousands of pages via code rather than per-page LLM calls, saving ~1M tokens per 3-page scrape and enabling self-healing when selectors change, because the agent can re-inspect the page structure and patch the scraper automatically.

## What they did

Rafael Levi from Bright Data demonstrated using Claude Code with their MCP server to build a Walmart.com product scraper live. The agent: (1) fetched Bright Data's skills repo (scraper best practices, selector patterns), (2) used the MCP's 'scrape as markdown' tool to extract page structure without raw HTML token overhead, (3) identified CSS selectors, (4) wrote and executed a scraper script, and (5) ran it across 3 pages of headphone search results. He also showed a polling/monitoring pattern where an LLM agent checks scraped data every 30 minutes, validates it, and auto-patches the scraper if data points are missing—eliminating the need for manual maintenance. He estimated ~1M token savings vs. feeding raw HTML to an LLM for every page.

## Relevance to YOLO loop

Relevant when our agent loop needs to ingest web data at scale (e.g. benchmarking competitor outputs, monitoring data sources). The self-healing pattern maps directly to resilient data-collection agents in our pipeline.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-11 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-06-11-self-healing-scraper-pipeline-mcp` |
| Channel | aie |
| Video | [From MCP to Scale: Pipelines That Build Themselves — Rafael Levi, Bright Data](https://www.youtube.com/watch?v=zTZ0qunQXnM) |
| Published | 2026-06-11 |
| Ingested upstream | 2026-06-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
