# Use Raw HTML/CSS/JS as Agent Output Format Instead of Custom DSLs

> Back to [[experiments-index]]

Source: **[HTML Is All Agents Need — James Russo, HeyGen](https://www.youtube.com/watch?v=Cz4v1WHVyZc)** · aie · 2026-07-21

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we instruct agents to output HTML/CSS/JS directly instead of custom JSON schemas or DSLs, then output quality and reliability will improve because HTML is the native language of LLMs trained on web data, reducing the cognitive overhead of translating to an unfamiliar format.

## What they did

James Russo described how HeyGen tried multiple output formats for video generation (Lottie JSON, Rive XML, Remotion/React) and found that the thinnest possible wrapper — essentially raw HTML with a few data attributes — produced the best results. Smaller models (Gemini Flash) could author workable code without extensive prompting, and quality improved naturally as models improved. They validated this at scale: 1.3M videos rendered, 15K/day, via the open-source Hyperframes framework.

## Relevance to YOLO loop

Relevant to the code generation and output formatting step of the YOLO loop — choosing output formats that align with LLM training distribution reduces prompt engineering burden and improves first-pass correctness.

## Notes

HeyGen open-sourced Hyperframes (32K GitHub stars). Could experiment with HTML as an intermediate representation for other structured outputs beyond video — e.g., UI mockups, diagrams, dashboards.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-21 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-21-html-native-video-agents` |
| Channel | aie |
| Video | [HTML Is All Agents Need — James Russo, HeyGen](https://www.youtube.com/watch?v=Cz4v1WHVyZc) |
| Published | 2026-07-21 |
| Ingested upstream | 2026-07-21 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
