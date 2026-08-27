# Replace browser automation with lightweight scraper APIs for agent web discovery and use browser only for interactive steps

> Back to [[experiments-index]]

Source: **[The Missing Layer in Agentic AI — Giedrius Šteimantas, Oxylabs](https://www.youtube.com/watch?v=XsvUhpnHepE)** · aie · 2026-08-27

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we route agent web discovery and content-fetching calls through a dedicated scraper API that returns validated markdown rather than using browser automation for all web interactions, then we will reduce token costs by ~50%, improve success rates, and lower per-transaction latency, because the speaker demonstrated that browser automation fails on CAPTCHAs, returns invalid content silently, and wastes 70% of tokens on JavaScript/CSS noise, while a scraper API returns only valid content with explicit failure signals.

## What they did

Speaker (Oxylabs) demonstrated rebuilding an AI shopping agent that had been using browser automation for all four stages (discovery, decision, verification, purchase). He replaced discovery and verification stages with a lightweight JSON search API (<2000 tokens/response, <700ms) and a scraper API that returns markdown and fails loudly on invalid content. Browser automation (Playwright MCP) was retained only for the purchase/execution stage where interactive form filling is unavoidable. Result: dramatic reduction in token waste, improved reliability, and predictable cost per transaction.

## Relevance to YOLO loop

Directly applicable to any agent that reads external documentation, checks package registries, or browses APIs. We should audit our agent's web calls and replace browser-based fetches with markdown API calls where the page is static, reserving Playwright for pages requiring interaction.

## Notes

Key principle: validate content before feeding to LLM — HTTP 200 does not mean valid content. Silent failures cause 70% token waste on garbage inputs. Fail loudly and explicitly.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-27 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-27-oxylabs-scraper-api-agent-web-access` |
| Channel | aie |
| Video | [The Missing Layer in Agentic AI — Giedrius Šteimantas, Oxylabs](https://www.youtube.com/watch?v=XsvUhpnHepE) |
| Published | 2026-08-27 |
| Ingested upstream | 2026-08-27 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
