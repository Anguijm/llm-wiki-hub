# Compare Codex Ultrafast vs Standard on Output Quality per Unit of Weekly Usage

> Back to [[experiments-index]]

Source: **[I Tested Codex's $500/mo Ultrafast. What You Need to Know.](https://www.youtube.com/watch?v=pY5_Ux_YJjo)** · nh · 2026-10-02

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we run identical tasks on Codex Ultrafast vs Standard mode, then Ultrafast will produce equal or better quality output but consume 4x more weekly usage quota, making it cost-effective only for time-critical or creative tasks where quality differences are meaningful.

## What they did

Nate ran two tasks — a 60-second video showreel from 145GB of raw footage with an 11-minute reflective audio brief, and a resource guide generation task — using both Ultrafast and Standard modes at extra-high reasoning. For the video task, Ultrafast ran in 19 minutes and used 17% of weekly quota vs Standard's 50 minutes and 4% quota. For the document task, Ultrafast ran in 2 minutes using 3% vs Standard's 13 minutes using 1%. He compared output quality side-by-side and found Ultrafast meaningfully better for the creative/video task but roughly equivalent for the structured document task.

## Relevance to YOLO loop

Informs when to invoke Ultrafast in our own Codex-based pipelines. For generative/creative tasks with large multimodal inputs, speed mode may also improve quality. For structured document generation, standard mode is the better ROI choice.

## Notes

Key finding: quality difference was task-dependent, not just speed-dependent. Ultrafast uses up to 4.25x more quota. Nate concludes he would only use it under genuine time pressure.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-02 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-10-02-codex-ultrafast-quality-cost-tradeoff` |
| Channel | nh |
| Video | [I Tested Codex's $500/mo Ultrafast. What You Need to Know.](https://www.youtube.com/watch?v=pY5_Ux_YJjo) |
| Published | 2026-10-02 |
| Ingested upstream | 2026-10-02 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
