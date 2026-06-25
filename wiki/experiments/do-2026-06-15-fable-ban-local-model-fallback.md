# Build a model-fallback routing layer to hedge against frontier model access bans

> Back to [[experiments-index]]

Source: **[Fable 5 is never coming back, here's why](https://www.youtube.com/watch?v=qlx40oVrXTY)** · do · 2026-06-15

**Status:** `discarded` · **Verdict:** `discard` · **Effort:** `medium`

---

## Hypothesis

If we implement a routing layer that automatically falls back across multiple model providers (Anthropic, OpenAI, open-source), then our dev loop remains productive during sudden model unavailability because geo-restrictions or policy bans can remove a best-in-class model with zero notice.

## What they did

Speaker described losing access to Claude Fable (banned by US government export controls, pulled globally even for US users temporarily) and immediately feeling severe productivity loss on coding tasks — Opus and GPT-4.5 made more sloppy mistakes, required heavier guidance, and lacked Fable's autonomous test-and-deploy behavior. He advocated for local/open-source model fine-tuning (citing Rio de Janeiro municipal IT fine-tuning Qwen) as a hedge against centralized control.

## Relevance to YOLO loop

YOLO loop reliability depends on consistent model access. A provider-agnostic routing layer (e.g. OpenRouter or a local LiteLLM proxy with ranked fallbacks) insulates the loop from policy disruptions and lets us benchmark capability gaps between models as they occur.

## Notes

Commentary-heavy but contains one concrete actionable: multi-provider fallback routing. Speaker also notes GPT-4.5 currently best for coding, Opus better for general use — useful for routing heuristics.

Backlog triage 2026-06-24 (owner-preference model). Open-source/local fallback hedging — overlaps the adopted resilience card and leans into the local-model NO.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-15 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-06-15-fable-ban-local-model-fallback` |
| Channel | do |
| Video | [Fable 5 is never coming back, here's why](https://www.youtube.com/watch?v=qlx40oVrXTY) |
| Published | 2026-06-15 |
| Ingested upstream | 2026-06-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
