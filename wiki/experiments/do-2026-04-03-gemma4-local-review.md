# Evaluate Gemma 4 as a local code review model to reduce API costs

> Back to [[experiments-index]]

Source: **[Gemma 4 is insane… best open-source model ever?!]()** · @DavidOndrej · 2026-04-02

**Status:** `discarded` · **Verdict:** `discarded` · **Effort:** `medium`

---

## Hypothesis

If Gemma 4 is capable enough for code review tasks, then we can run it locally via Ollama for routine reviews (linting-level checks, pattern enforcement) and reserve Gemini API calls for deep architectural reviews, reducing API costs while maintaining quality.

## What they did

David Ondrej reviewed Gemma 4, claiming it's the best open-source model — suggesting it may be capable enough for tasks previously requiring proprietary APIs.

## Actionable steps

- Download Gemma 4 via Ollama (check available quantizations)
- Run it on 5 past Gemini code reviews and compare output quality
- Measure latency and resource usage on local hardware
- If quality is adequate for basic checks, wire it as a pre-filter before Gemini deep review

## Success metric

Gemma 4 catches at least 60% of the issues Gemini finds, at zero API cost.

## Relevance to YOLO loop

The YOLO loop uses Gemini API for all code reviews. A capable local model could handle routine checks, saving API budget for complex analysis.

## Target projects

- [[yolo-projects]] (`yolo-loop-infrastructure`)

## Notes

Discarded 2026-04-07: local-model policy decision = NO. John confirmed cost is not currently a constraint and operational overhead of running Ollama (service, model files, GPU, routing logic) does not earn its slot when council/builds work fine on Claude+Gemini. Cull along with Ollama experiment #43.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-03 | `backlog` | Ingested from Phase 4 YouTube pipeline — title-only inference |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-04-03-gemma4-local-review` |
| Channel | @DavidOndrej |
| Published | 2026-04-02 |
| Ingested upstream | 2026-04-03 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
