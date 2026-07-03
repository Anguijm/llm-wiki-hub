# Apply DSPy harness engineering to decouple task specification from model selection

> Back to [[experiments-index]]

Source: **[WF26: Harness Engineering & Startup Battlefield ft. Garry Tan, Mike Krieger, @t3dotgg, DSPy](https://www.youtube.com/watch?v=I2cbIws9j10)** · aie · 2026-07-03

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we use DSPy-style harness engineering to separate task definitions from the underlying model, then we can swap models (including cheaper open-source ones) without rewriting prompts, reducing cost and increasing portability of our agent pipelines.

## What they did

Day 4 of AI Engineer World's Fair 2026 focused on harness engineering as a theme. The DSPy team presented protocols for separating task logic from model choice, scaling AI systems, and how clean task decomposition enables model-agnostic pipelines. The conference context (7,000 attendees, multiple tracks on software factories, memory, generative media) provided surrounding signal that harness engineering is emerging as a distinct discipline from prompt engineering.

## Relevance to YOLO loop

Harness engineering directly addresses the YOLO loop's model-selection brittleness. If task specs are model-agnostic, we can benchmark Fable vs. Opus vs. cheaper models on the same harness and swap without loop rewrites.

## Notes

Transcript was heavily truncated (481K chars, only partial content available). Card is based on available intro context and conference theme. Full DSPy talk content not accessible from truncated transcript — worth watching full recording for implementation specifics.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-03 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-03-harness-engineering-dspy` |
| Channel | aie |
| Video | [WF26: Harness Engineering & Startup Battlefield ft. Garry Tan, Mike Krieger, @t3dotgg, DSPy](https://www.youtube.com/watch?v=I2cbIws9j10) |
| Published | 2026-07-03 |
| Ingested upstream | 2026-07-03 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
