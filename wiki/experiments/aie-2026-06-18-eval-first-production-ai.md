# Define Business-Metric Evals and Growing Test Case Library Before Writing Agent Code

> Back to [[experiments-index]]

Source: **[The Production AI Playbook: Deploying Agents at Enterprise Scale — Sandipan Bhaumik, Databricks](https://www.youtube.com/watch?v=ObTPqBGsEbA)** · aie · 2026-06-18

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we define what 'good' agent output looks like in business terms (not just technical metrics) and build an automated eval pipeline against a categorized, versioned test case library before writing any agent code, then we will close the evaluation gap that causes most AI demos to fail in production because we will have a continuous measurement system that catches regressions as prompts and models change.

## What they did

Sandipan Bhaumik (Databricks technical lead) presented a five-pillar production AI framework derived from working with enterprise customers across B2B software and regulated industries. The core insight was that teams always started by choosing a model, built demos in controlled environments, and then failed in production because of three gaps: observability (no tracing of decisions), evaluation (no continuous measurement of business-relevant success), and governance (no accountability when AI fails). His recommended sequence: (1) before any code, define success in business terms and create a small golden dataset of good answers; (2) build a simple Python pipeline to compare agent outputs against that dataset automatically; (3) version prompts in Git with structured commit messages explaining what failure each change addresses; (4) categorize test cases by problem type so regressions can be traced to specific failure categories; (5) use tiered eval runs in CI (subset on PR, full suite on merge to main) to manage cost. He also emphasized behavioral evals for tool call correctness as a separate eval layer.

## Relevance to YOLO loop

Our YOLO loop currently lacks a structured eval layer. Implementing even a minimal golden dataset and automated comparison pipeline would give us the feedback signal needed to safely iterate on prompts and catch regressions before they reach production.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-18 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-06-18-eval-first-production-ai` |
| Channel | aie |
| Video | [The Production AI Playbook: Deploying Agents at Enterprise Scale — Sandipan Bhaumik, Databricks](https://www.youtube.com/watch?v=ObTPqBGsEbA) |
| Published | 2026-06-18 |
| Ingested upstream | 2026-06-18 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
