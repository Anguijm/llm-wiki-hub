# Replace Full-DOM or Screenshot-Only Input with a Compressed Markdown Page Representation for Browser Agents

> Back to [[experiments-index]]

Source: **[Browser Agents Don't Need Better Models. They Need Better Eyes. - Kushan Raj, ARK](https://www.youtube.com/watch?v=JnubYCYunk8)** · aie · 2026-06-28

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we replace raw screenshots or full DOM dumps with a compressed markdown representation of the entire page (plus delta feedback on what appeared/disappeared), then browser agents will be faster, cheaper, and more reliable because the model can see the full page context in ~1,800 tokens instead of 20,000+ tokens, enabling better long-sequence planning and accurate click targeting.

## What they did

Kushan built a browser agent that converts each page into a compressed markdown representation (~1,800 tokens) instead of using raw screenshots (~1,100 tokens but partial view) or full DOM (~20,000 tokens). The representation lets the model see the entire page at once. He also added delta feedback: the agent is told which elements appeared, disappeared, or were unclickable after each action, giving it a lightweight state-diff. Compared to Claude using standard screenshot-based browsing (which got stuck, took 2+ minutes on simple tasks), his agent with a cheaper model completed the same tasks in seconds. He demonstrated downloading an Aadhaar card and booking a trekking date as concrete examples.

## Relevance to YOLO loop

Relevant to any YOLO loop step that involves a browser agent as a tool—e.g., automated testing, scraping, or UI validation. The compressed representation pattern could also apply to how we feed UI context to coding agents doing front-end work.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-28 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-06-28-browser-agent-compressed-dom` |
| Channel | aie |
| Video | [Browser Agents Don't Need Better Models. They Need Better Eyes. - Kushan Raj, ARK](https://www.youtube.com/watch?v=JnubYCYunk8) |
| Published | 2026-06-28 |
| Ingested upstream | 2026-06-28 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
