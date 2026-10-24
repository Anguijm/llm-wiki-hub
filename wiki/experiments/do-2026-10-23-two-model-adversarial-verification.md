# Add a second-model reviewer to bug-finding loops

> Back to [[experiments-index]]

Source: **[Everything Is Getting Hacked (it’s over)](https://www.youtube.com/watch?v=wuv61uEq7uY)** · do · 2026-10-23

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we have a primary model scan a codebase for vulnerabilities and a different reviewer model validate each finding's exploitability, then false-positive reports will drop because a second model filters out the plausible-sounding but wrong findings that next-token completion tends to produce.

## What they did

Ran a primary model (Opus 5.5) to scan for vulnerabilities and a secondary reviewer model (GPT-6.1 Sol) to check whether each finding was actually exploitable. Findings the reviewer rejected were dropped. Threads with zero findings were self-archived, and verified issues were kept and alerted on. The speaker showed a diagram of the adversarial sub-agent review architecture. He notes that prompting a model simply to find bugs produces false positives.

## Relevance to YOLO loop

high: This is a verification-loop pattern (finder agent plus independent reviewer agent) that can be built directly into Claude Code skills, hooks or council-style review steps.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-23 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-10-23-two-model-adversarial-verification` |
| Channel | do |
| Video | [Everything Is Getting Hacked (it’s over)](https://www.youtube.com/watch?v=wuv61uEq7uY) |
| Published | 2026-10-23 |
| Ingested upstream | 2026-10-23 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
