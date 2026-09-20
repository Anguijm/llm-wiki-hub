# Add vLLM-specific observability probes to catch silent inference correctness bugs

> Back to [[experiments-index]]

Source: **[Two Bugs That Hid in Plain Sight: A vLLM Debugging Detective Story — Asaf Gardin & Yuval Belfer](https://www.youtube.com/watch?v=btxG75rNJC4)** · aie · 2026-09-20

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we instrument vLLM deployments with targeted correctness checks (output sampling audits, KV-cache consistency probes, determinism tests), then we will surface subtle bugs that evade standard metrics, because correctness failures in inference engines often manifest as intermittent quality degradation rather than hard errors.

## What they did

Asaf Gardin and Yuval Belfer from the vLLM team walked through a detective story of two non-obvious bugs in vLLM that were difficult to detect through normal monitoring — illustrating the debugging process, the misleading signals, and the eventual root-cause identification.

## Relevance to YOLO loop

If the YOLO loop uses vLLM as its inference backend, silent correctness bugs could silently degrade output quality; proactive probes would catch regressions before they affect results.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-20 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-20-vllm-bugs-plain-sight` |
| Channel | aie |
| Video | [Two Bugs That Hid in Plain Sight: A vLLM Debugging Detective Story — Asaf Gardin & Yuval Belfer](https://www.youtube.com/watch?v=btxG75rNJC4) |
| Published | 2026-09-20 |
| Ingested upstream | 2026-09-20 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
