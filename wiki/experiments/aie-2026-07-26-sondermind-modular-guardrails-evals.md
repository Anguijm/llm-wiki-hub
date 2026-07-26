# Implement separate LLM-as-judge guardrail calls sandwiching core agent to improve robustness and eval granularity

> Back to [[experiments-index]]

Source: **[Evals-Driven Development for a Mental Health AI Coach — Akele Reed & Dave Revere, SonderMind](https://www.youtube.com/watch?v=O72p-rBb2bA)** · aie · 2026-07-26

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we implement input and output guardrails as separate LLM-as-judge calls independent of the core agent rather than embedded in a single prompt, then guardrails will be harder to circumvent through adversarial conversation and easier to evaluate and iterate independently because modular components can be tested and updated without touching core agent behavior.

## What they did

SonderMind built Sonder, a mental health AI coach, using an architecture where independent LLM-as-judge calls sandwich the core agent: input guardrails evaluate each user message before the core agent responds, and output guardrails evaluate both the AI response and conversation trajectory after the core agent responds. Key decisions: (1) Modularity was prioritized so Sonder core could be iterated without affecting safety layers. (2) Separate guardrail calls are deliberately more expensive in latency and cost but were deemed necessary for the sensitivity of the domain—and harder to jailbreak via multi-turn conversation drift. (3) Built-in frontier model guardrails (Anthropic/OpenAI) were turned off on day one because they are overcalibrated for general use—inappropriate guardrail triggers in mental health feel like 'a door slam to the face.' (4) Target is correct triggers, not more triggers. (5) They open-sourced 200 input guardrail scenarios and 100 output guardrail scenarios, all clinically reviewed and calibrated against real conversation patterns including single and multi-turn, across the spectrum of mental health topics including suicide, self-harm, and domestic violence. (6) Analytics and alerting platforms monitor the full pipeline in production.

## Relevance to YOLO loop

The modular guardrail pattern is directly applicable to our YOLO loop's safety and quality gates: wrapping our core agent with independent pre/post LLM-as-judge calls allows us to eval and improve safety behavior without retraining or re-prompting the core agent. The open-sourced eval datasets are a concrete starting point for adversarial test cases.

## Notes

Open-source datasets available via QR code in video. Key calibration insight: prefer false negatives over false positives in sensitive domains (wrong to block > wrong to allow). For our loop, the inverse may apply depending on task—worth explicitly deciding the false positive / false negative trade-off per guardrail type before deploying.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-26 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-26-sondermind-modular-guardrails-evals` |
| Channel | aie |
| Video | [Evals-Driven Development for a Mental Health AI Coach — Akele Reed & Dave Revere, SonderMind](https://www.youtube.com/watch?v=O72p-rBb2bA) |
| Published | 2026-07-26 |
| Ingested upstream | 2026-07-26 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
