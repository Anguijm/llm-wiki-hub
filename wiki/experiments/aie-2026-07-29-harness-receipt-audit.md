# Add a harness receipt layer that records state ownership, ordered mutations, and user-visible edge confirmation for every agent action

> Back to [[experiments-index]]

Source: **[Your Agent Didn't Fail. Your Harness Did. — Vinoth Govindarajan, OpenAI](https://www.youtube.com/watch?v=BInpv7lGp1o)** · aie · 2026-07-29

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If every agent action produces a structured receipt capturing what triggered it, what state it inherited, which authority it used, what executed, and what evidence survived at the user-visible edge, then silent harness failures (where the agent reports success but state is not durably written) will be detectable because the receipt distinguishes between internal tool success and external confirmed outcome.

## What they did

Vinoth analyzed production failures in OpenClaw and similar agent systems, finding that most failures are harness failures not model failures. The key failure shapes are: state holes (delivered but not remembered), overlapping writers (concurrent state mutation), dangling tool calls (tool reports success but effect not confirmed at user edge), approval drift (policy version mismatch), and missing edge proof (internal success ≠ external visibility). His solution is a five-question receipt per agent turn: what woke it up, what state did it inherit, which authority did it use, what executed (with idempotency key), and what evidence survived at the user-visible boundary. He mapped this to a harness blueprint: events → session key → throttle → runtime → tools with approvals → audit rail as receipt.

## Relevance to YOLO loop

Adding receipt logging to the YOLO loop's tool execution layer would make it possible to distinguish model reasoning failures from harness infrastructure failures, dramatically improving debuggability of agent runs.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-29 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-29-harness-receipt-audit` |
| Channel | aie |
| Video | [Your Agent Didn't Fail. Your Harness Did. — Vinoth Govindarajan, OpenAI](https://www.youtube.com/watch?v=BInpv7lGp1o) |
| Published | 2026-07-29 |
| Ingested upstream | 2026-07-29 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
