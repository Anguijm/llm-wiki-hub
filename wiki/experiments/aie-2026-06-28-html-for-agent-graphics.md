# Use HTML+CSS as the agent-native format for generating slide decks, documents, and visual artifacts instead of canvas-based tools

> Back to [[experiments-index]]

Source: **[HTML is All You Need (for Agents to Make Graphics) - Amol Kapoor, Nori](https://www.youtube.com/watch?v=JRTAtZ5iBkU)** · aie · 2026-06-28

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we instruct coding agents to produce visual artifacts (slides, reports, dashboards) as HTML+CSS rather than manipulating PowerPoint, Figma, or SVG directly, then output quality and layout correctness improve dramatically, because HTML is a structured language agents have trained on billions of examples of, so they can reason about headings, grids, and charts semantically rather than placing pixel coordinates they cannot verify.

## What they did

Amol argued that agents fail at graphics not because of model limitations but because canvas-based tools (PowerPoint, Figma, SVG) require spatial reasoning in a pixel coordinate system foreign to language models. He demonstrated that asking models to draw a pelican in SVG produces garbage, but the same task in HTML produces coherent, readable, and editable output. His company (Nori) uses HTML+CSS exclusively for all slide decks, board decks, sales decks, docs, and even the conference video itself (built as animated HTML/CSS divs). He showed that once content is populated from company data (call transcripts, emails) by an agent with access to those sources, full board-quality decks can be built end-to-end from a phone. He recommended rendering to PDF only as a final export step if needed, keeping HTML as the canonical editing format.

## Relevance to YOLO loop

Any YOLO loop step that needs to produce a human-readable report, status update, or architectural diagram can use this pattern. Replacing 'generate a PDF report' with 'generate an HTML report' is a one-line prompt change with significantly better output quality.

## Notes

The Simon Willison 'pelican in SVG' test is a quick benchmark for comparing model spatial reasoning across versions. Consider adding it to our model evaluation checklist.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-28 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-06-28-html-for-agent-graphics` |
| Channel | aie |
| Video | [HTML is All You Need (for Agents to Make Graphics) - Amol Kapoor, Nori](https://www.youtube.com/watch?v=JRTAtZ5iBkU) |
| Published | 2026-06-28 |
| Ingested upstream | 2026-06-28 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
