# Add llms.txt, llms-full.txt, and twin .md files to project docs to maximize agent discoverability

> Back to [[experiments-index]]

Source: **[How We Got LLMs to Recommend Our Open Source Library — Christopher Burns, Inth](https://www.youtube.com/watch?v=V_5bn4q-vAI)** · aie · 2026-08-27

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we add a hand-crafted llms.txt (40 high-signal lines), an llms-full.txt sitemap with page descriptions, and .md twin files for every documentation page, then coding agents will more reliably discover and correctly use our libraries, because the speaker's C15T library grew to 3M NPM downloads with LLMs as the #1 inbound source after implementing this documentation stack, and tests show ~50% token savings when agents fetch markdown vs. scraping HTML.

## What they did

Speaker (founder of C15T cookie consent library, YC alum) described a documentation pipeline that made his open source library the top recommendation from Claude, ChatGPT, and Gemini. Key components: hand-written llms.txt (quality over quantity — 40 good lines beats 1000 noisy ones), llms-full.txt as an agent sitemap, .md twin files for every page, canonical link headers pointing agents to the full doc bundle, and node_modules-embedded docs for libraries. He abstracted this into an open source tool called Lead Type. Also recommended aura.ai for testing agent-readiness scores.

## Relevance to YOLO loop

Immediately applicable if we have any internal or public-facing documentation. Adding llms.txt and .md twins to our tool docs would improve agent retrieval accuracy in the loop, reducing hallucinated API signatures and incorrect library usage.

## Notes

aura.ai can score current agent-readiness of any site. Run it on our docs as baseline before implementing changes. 50% token reduction from markdown vs HTML is a significant efficiency gain.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-27 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-27-llms-txt-agent-discoverability` |
| Channel | aie |
| Video | [How We Got LLMs to Recommend Our Open Source Library — Christopher Burns, Inth](https://www.youtube.com/watch?v=V_5bn4q-vAI) |
| Published | 2026-08-27 |
| Ingested upstream | 2026-08-27 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
