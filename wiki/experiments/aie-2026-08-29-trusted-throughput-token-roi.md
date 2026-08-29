# Instrument a per-team token-usage dashboard as a smoke detector and define 'trusted throughput' as the primary ROI metric

> Back to [[experiments-index]]

Source: **[From Tokenmaxxing to Trusted Throughput — Mingsheng Hong, Ironclad](https://www.youtube.com/watch?v=dSg0pu8d6qg)** · aie · 2026-08-29

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we track token usage per team and individual as a smoke detector (flagging low-usage outliers for investigation rather than rewarding high usage), and measure ROI as 'trusted throughput' (code reviewed, validated, and deployed to customers) rather than raw token count, then we will avoid perverse incentives to generate AI slop while still identifying teams that are under-adopting, because throughput quality is the actual business outcome not inference volume.

## What they did

Mingsheng described Ironclad's journey from AI adoption to cost optimization. Key practices: usage dashboards framed as smoke detectors not leaderboards; 'trusted throughput' metric (code that passes internal review and customer validation) as the ROI proxy; agentic loop harnesses with explicit step-count limits to prevent runaway token spend; prompt caching by putting fixed system prompts before variable user content; context pruning muscle memory and auto-compaction tools (Claude Code); shared internal playbooks of well-crafted prompts for common task types (bug fix PR vs. new feature vs. refactor); build-vs-buy decisions based on whether the capability is differentiating (buy non-differentiating infra, build internal playbooks). They also described a learning loop where leadership reviews guardrails, metrics, and refinements on a recurring cadence.

## Relevance to YOLO loop

The smoke-detector dashboard and trusted-throughput metric provide the measurement framework the YOLO loop needs to know whether agent output is actually improving engineering outcomes vs. just generating volume; the prompt-caching and context-pruning practices directly reduce per-run cost.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-29 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-29-trusted-throughput-token-roi` |
| Channel | aie |
| Video | [From Tokenmaxxing to Trusted Throughput — Mingsheng Hong, Ironclad](https://www.youtube.com/watch?v=dSg0pu8d6qg) |
| Published | 2026-08-29 |
| Ingested upstream | 2026-08-29 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
