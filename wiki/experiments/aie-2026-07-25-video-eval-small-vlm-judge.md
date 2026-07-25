# Fine-Tune a Small VLM as a Fast Video Quality Judge Calibrated by Periodic Human Annotation

> Back to [[experiments-index]]

Source: **[Evaling Video Slop — Maor Bril, Character.ai](https://www.youtube.com/watch?v=b_PmGocP4rc)** · aie · 2026-07-25

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we fine-tune a small VLM (e.g. Qwen-based) on human-annotated video quality labels and use it as an inline judge during generation, then we can catch quality failures earlier and cheaper in the pipeline because correcting drift at the frame or short-clip stage costs far less than regenerating full multi-minute videos.

## What they did

Maor described Character.ai's iterative approach to evaluating generated video quality. Classical metrics (CLIP score, LPIPS) only assess individual frames or prompt alignment, not narrative coherence, physics plausibility, character consistency, or audio sync. Their first iteration built a repeatable benchmark harness combining frame-level metrics with LLM-as-judge, calibrated by periodic human annotation sessions (10-15 min, random axes per annotator). The human feedback was fed back into the LLM judge prompt and used as training data for the next model version. To scale and move evaluation earlier in the pipeline, they fine-tuned a small Qwen-based VLM as a specialized video judge that can run at high throughput on a single GPU instance. They catch character drift between shot starting frames before generating the full video, saving significant compute. The open-source harness accepts any LLM/agent as the judge backend.

## Relevance to YOLO loop

Pattern is transferable beyond video: the principle of fine-tuning a small specialist judge model, calibrated by human annotation on disagreement cases, and inserting it early in the generation pipeline applies to any expensive multi-step agentic output. For our loop, consider a small classifier judge on intermediate artifacts before committing to expensive downstream steps.

## Notes

Maor chose Qwen due to prior successful post-training experience. At small scale (<1000 videos/day) a cohort of frontier model judges plus human experts is sufficient; the fine-tuned small VLM becomes worthwhile at thousands+ per day for unit economics. Repo is open source; telemetry export is a noted gap, accepted as feature request.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-25 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-25-video-eval-small-vlm-judge` |
| Channel | aie |
| Video | [Evaling Video Slop — Maor Bril, Character.ai](https://www.youtube.com/watch?v=b_PmGocP4rc) |
| Published | 2026-07-25 |
| Ingested upstream | 2026-07-25 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
