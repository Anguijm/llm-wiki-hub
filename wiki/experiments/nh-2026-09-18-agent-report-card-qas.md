# Build an AI Agent QA Stress-Tester with Claude

> Back to [[experiments-index]]

Source: **[Anthropic's CEO: How to Build a 1 Person Business with Claude](https://www.youtube.com/watch?v=QDsenEcAJIk)** · nh · 2026-09-18

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we build automated QA software that runs AI customer-support agents through high-risk scenarios (refunds, billing disputes, data requests) and generates a structured failure report, then we can replace manual agent testing and produce client-ready evidence of agent quality because the test scenarios are repeatable, the failure patterns are well-defined, and Claude can both generate adversarial inputs and evaluate outputs.

## What they did

The presenter used Claude to evaluate three one-person business ideas against three filters (capital deployment, software-buildable, highly automated sales/support). He selected 'Agent Report Card'—QA software for AI customer-support agents. He built it with Claude Code, designed it to run 16+ adversarial customer scenarios against a target agent, store test history, diagnose failures, and produce a client-ready report. Clay was used for outbound prospecting to AI automation agencies. Pricing was set at $499/month, requiring 168 customers for $1M ARR. The three-Ps framework (Pain, Person, Promise) was used to sharpen positioning: pain = manual agent testing with no proof of quality; person = AI automation agencies deploying support bots for clients; promise = automated scenario testing with a client-ready evaluation report.

## Relevance to YOLO loop

Directly applicable to our dev loop: we could build an internal version of Agent Report Card to stress-test our own AI agents before deploying them. The adversarial scenario runner and structured failure report pattern maps to any loop that ships AI agents and needs pre-deployment validation.

## Notes

Core idea is an AI eval harness for customer-support agents. Could be scoped down to a single adversarial scenario runner script as a low-effort first milestone. The 168-customer revenue math and Clay outbound workflow are secondary but useful if productizing.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-18 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-09-18-agent-report-card-qas` |
| Channel | nh |
| Video | [Anthropic's CEO: How to Build a 1 Person Business with Claude](https://www.youtube.com/watch?v=QDsenEcAJIk) |
| Published | 2026-09-18 |
| Ingested upstream | 2026-09-18 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
