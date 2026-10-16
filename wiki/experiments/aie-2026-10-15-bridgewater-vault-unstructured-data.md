# Design a 'Vault' pattern for the Markdown knowledge vault — separate human agent needs from automated agent needs at the data layer

> Back to [[experiments-index]]

Source: **[AI Engineer NYC Livestream | Bridgewater, Anthropic, Two Sigma, Arize, Coatue, Nous, Gen. Intuition](https://www.youtube.com/watch?v=akEqiXFo3GM)** · aie · 2026-10-15

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we structure the Markdown knowledge vault so that human retrieval paths and automated agent retrieval paths are explicitly separated at the data layer (different schemas, different access patterns), then both will work better, because Bridgewater found that humans and agents have fundamentally different needs from the same unstructured data and trying to serve both with one interface degrades both.

## What they did

Sam Green and Aaron Linsky from Bridgewater presented 'The Vault,' a data platform built to turn unstructured investment research into a first-class asset. The first of three lessons: humans and agents have very different needs from a data platform. (Further detail was truncated in the transcript.) The broader conference framing was AI engineering meeting financial institutions — the actionable architectural insight is the separation of human vs. agent data access patterns as a first-class design concern.

## Relevance to YOLO loop

medium: the human-vs-agent data access separation is a harness design principle applicable to any project with a knowledge retrieval component.

## Notes

Transcript heavily truncated; the Bridgewater talk detail was limited. Worth watching the full recording when available.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-15 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-15-bridgewater-vault-unstructured-data` |
| Channel | aie |
| Video | [AI Engineer NYC Livestream | Bridgewater, Anthropic, Two Sigma, Arize, Coatue, Nous, Gen. Intuition](https://www.youtube.com/watch?v=akEqiXFo3GM) |
| Published | 2026-10-15 |
| Ingested upstream | 2026-10-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
