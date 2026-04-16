# Map and Eliminate the Non-AI Bottleneck in Your Dev Loop

> Back to [[experiments-index]]

Source: **[Your AI Is 50x Faster. You're Getting 2x. You're Fixing the Wrong Thing.](https://www.youtube.com/watch?v=XlfumXPPrLY)** · NateBJones · 2026-04-16

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we systematically identify and fix the non-AI bottlenecks in our development workflow (e.g., context switching, review latency, deployment friction), then we will see outsized productivity gains compared to switching to a faster model, because Amdahl's Law means the slowest non-AI step caps total throughput.

## What they did

Speaker argues that AI coding speed improvements are being absorbed by surrounding workflow steps that haven't been optimized. Demonstrates that most teams get ~2x gains despite 50x faster inference because human review, integration, and deployment steps are the real bottleneck. Recommends timing each stage of the dev loop to find the true constraint before optimizing AI speed.

## Relevance to YOLO loop

Directly applicable: we should instrument the YOLO loop stages (prompt → generation → review → merge → deploy) to find where wall-clock time is actually spent before tuning model parameters.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-16 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-04-16-fix-bottleneck-not-ai-speed` |
| Channel | NateBJones |
| Video | [Your AI Is 50x Faster. You're Getting 2x. You're Fixing the Wrong Thing.](https://www.youtube.com/watch?v=XlfumXPPrLY) |
| Published | 2026-04-16 |
| Ingested upstream | 2026-04-16 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
