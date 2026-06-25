# Replace default LLM web fetch with a proxy-backed MCP scraping tool and compare hallucination rate

> Back to [[experiments-index]]

Source: **[Your Agent's Biggest Lie: "I Searched the Web" — Rafael Levi, Bright Data](https://www.youtube.com/watch?v=btxGmN8RvNU)** · aie · 2026-06-17

**Status:** `discarded` · **Verdict:** `discard` · **Effort:** `medium`

---

## Hypothesis

If we route agent web-retrieval tasks through a proxy-backed MCP server (e.g., Bright Data MCP) instead of relying on the LLM's built-in fetch or training data, then hallucinated citations and stale data will decrease measurably because the MCP provides real-time responses that bypass CAPTCHA and bot-blocking, removing the LLM's incentive to fabricate plausible-sounding results.

## What they did

Rafael Levi demonstrated a side-by-side test with GPT-5: identical prompts asking the model to retrieve live data from five heavily bot-protected sites (Rightmove, LinkedIn, Instagram, Amazon, TikTok). Without MCP: 0/5 success, model fabricated results. With Bright Data MCP (66 tools including real Google/Bing/DuckDuckGo search, markdown scraper, scraping browser with unique fingerprints): 5/5 success with verifiable live data. He also advocated loading only the specific tools needed per task rather than all 66, to avoid polluting context. He noted Cloudflare now blocks ~20% of the web from AI crawlers by default, and has released an AI labyrinth that feeds bots fake data.

## Relevance to YOLO loop

Any YOLO loop agent that calls out to the web for research, pricing, or validation is silently at risk of this failure mode. Adding a real-fetch MCP as the web-retrieval layer and spot-checking citation URLs would harden the loop's grounding step.

## Notes

Rafael mentioned a complementary pattern: have the LLM build a parser script once, then run the script to scrape at scale—saves ~99% of tokens vs. LLM-parsed HTML. Free tier is 5000 requests/month. GitHub: github.com/brightdata.

Backlog triage 2026-06-24 (owner-preference model). Proxy-backed scraping vs hallucination — web-infra off-focus.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-17 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-06-17-mcp-real-web-access` |
| Channel | aie |
| Video | [Your Agent's Biggest Lie: "I Searched the Web" — Rafael Levi, Bright Data](https://www.youtube.com/watch?v=btxGmN8RvNU) |
| Published | 2026-06-17 |
| Ingested upstream | 2026-06-17 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
