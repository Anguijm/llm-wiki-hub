# Build a Roadtripper hero demo with Stage Show and a frame contact sheet

> Back to [[experiments-index]]

Source: **[Head Of Design At X's New Claude Skill Is Insane](https://www.youtube.com/watch?v=of628n5754g)** · ail · 2026-11-07

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we install the Stage Show skill and have Claude build a 10-16 second, 3-7 word animated demo of Roadtripper's trip-planning screen, checked via a multi-frame contact sheet, then we get a landing-page demo with no text clipping or motion jumps on the first human review because the contact sheet lets a script and the agent inspect every frame.

## What they did

Benji Taylor's open-source Stage Show skill has Claude extract the app's styles, then build a stripped-down mock with only 3-7 real words and placeholder bars. It scripts a 10-16 second narrative in 3-5 moments with curved cursor paths and a seamless loop. It records the animation, lays every frame side by side in a rehearsal.md contact sheet, and runs script checks for text overflow, jumping elements and abrupt transitions before human review.

## Relevance to YOLO loop

medium: Frame-by-frame contact-sheet checking of motion is a new verification surface, though it fits the existing hard-gate practice.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-11-13 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `ail-2026-11-07-contact-sheet-animated-demo` |
| Channel | ail |
| Video | [Head Of Design At X's New Claude Skill Is Insane](https://www.youtube.com/watch?v=of628n5754g) |
| Published | 2026-11-07 |
| Ingested upstream | 2026-11-13 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
