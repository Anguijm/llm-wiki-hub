# Run an air-gapped local LLM to detect and mask PII before sending docs to cloud AI

> Back to [[experiments-index]]

Source: **[I Cut the Internet and Let AI Read the File I Could Never Upload. It Caught the Leak.](https://www.youtube.com/watch?v=5slsNizN6MQ)** · nb · 2026-07-19

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we route documents through a locally-running LLM (via LM Studio) with a saved sensitivity-detection preset before any cloud upload, then we will catch private pricing, legal notes, revenue forecasts, and combinatorial PII without leaking data over the wire, because the model runs fully offline with Wi-Fi disabled and no remote connections.

## What they did

Speaker downloaded GPT-OSS Safeguard 20B into LM Studio, disabled Wi-Fi and all network services, saved a reusable 'sensitivity' preset instructing the model to find private identity, financial, security, legal, company, and employment information, mask it, and flag unreadable sections as uncertain rather than safe. He then ran a fake contract containing unreleased pricing, a revenue forecast, a fake API key, attorney-client material, and a deliberately unreadable section through the model. The model correctly identified all sensitive categories, masked them, and refused to call the unreadable section clean.

## Relevance to YOLO loop

Directly applicable as a pre-flight gate in the YOLO loop: before any document or code file is sent to a frontier model API, run it locally through the sensitivity preset to strip or flag confidential content, preventing inadvertent leakage of proprietary prompts, keys, or customer data.

## Notes

Speaker references a Substack guide with the exact LM Studio preset used. Model used: GPT-OSS Safeguard 20B. Key nuance: model flagged unreadable section as uncertain rather than falsely safe — important eval criterion.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-19 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-07-19-local-llm-pii-detection` |
| Channel | nb |
| Video | [I Cut the Internet and Let AI Read the File I Could Never Upload. It Caught the Leak.](https://www.youtube.com/watch?v=5slsNizN6MQ) |
| Published | 2026-07-19 |
| Ingested upstream | 2026-07-19 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
