# Build an Iterative Multimodal Web-Data Collection Pipeline for Agent Grounding

> Back to [[experiments-index]]

Source: **[How Web Data Infrastructure Powers the Next Generation of AI — Patricija Žemaitytė, Oxylabs](https://www.youtube.com/watch?v=1UmZHb_E_SM)** · aie · 2026-08-14

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we build a modular web-data pipeline that incrementally adds supported data types (video, transcripts, subtitles, metadata, search) rather than trying to scope the full feature set upfront, then the pipeline reaches production utility faster because client requirements reliably expand in directions that cannot be fully anticipated.

## What they did

Oxylabs was asked to deliver 5 PB/month of video data for AI training in two weeks. The team built a video downloader, then iteratively added transcript support, subtitle support, a search layer to find videos in target languages, and metadata/channel-info endpoints. Each iteration was prompted by client feedback. The final result was a full video API suite built in ~3 months that became a product family. The speaker's lesson: clients buy your ability to adapt, not the first iteration.

## Relevance to YOLO loop

Informs how to structure data-ingestion agents in the YOLO loop: start with the minimal viable data fetch (raw HTML/text), then add retrieval modes (PDF, video, structured metadata) as downstream agents reveal they need them, rather than over-engineering the pipeline before needs are known.

## Notes

Secondary finding: scaling SERP delivery to sub-100ms latency required gradual load testing up to 60k req/s (now targeting 150k req/s). The lesson that observability telemetry itself becomes a bottleneck at scale is relevant if the YOLO loop generates high-frequency agent traces.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-14 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-14-web-data-pipeline-multimodal` |
| Channel | aie |
| Video | [How Web Data Infrastructure Powers the Next Generation of AI — Patricija Žemaitytė, Oxylabs](https://www.youtube.com/watch?v=1UmZHb_E_SM) |
| Published | 2026-08-14 |
| Ingested upstream | 2026-08-14 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
