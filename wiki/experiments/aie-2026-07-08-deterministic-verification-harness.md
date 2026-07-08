# Build a deterministic verification harness that fires via Claude hooks and retries on failure

> Back to [[experiments-index]]

Source: **[Your coding agent doesn't always follow your rules — Talha Sheikh, Checkout.com](https://www.youtube.com/watch?v=MpZzWMdmQCE)** · aie · 2026-07-08

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we attach a deterministic test runner to Claude's post-session hook that checks agent output against a config-defined set of test cases and requeues the task on failure, then we can trust agent completions without manual review because the verification is machine-enforced rather than instruction-based.

## What they did

Talha built 'Vector', a CLI tool that hooks into Claude Code's session-end event. A config file defines test cases specifying what must be true about the output. When the hook fires, Vector runs the checks deterministically; if any fail, it feeds the failure back to Claude and retries. He showed test output with pass/fail per case and automatic retry until all pass. He argued this enables use of smaller/cheaper models with tighter guardrails to achieve the same reliability as frontier models, reducing cost. He generalized the pattern: verification should be language-agnostic, run at every level (conversation end, pre-commit, multi-agent workflow boundary, async operations), and be treated as a contract between task spec and output.

## Relevance to YOLO loop

This is a direct implementation of the enforcement layer our yolo-loop needs: hook-triggered, deterministic, config-driven, auto-retrying verification that removes humans from the acceptance path.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-08 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-08-deterministic-verification-harness` |
| Channel | aie |
| Video | [Your coding agent doesn't always follow your rules — Talha Sheikh, Checkout.com](https://www.youtube.com/watch?v=MpZzWMdmQCE) |
| Published | 2026-07-08 |
| Ingested upstream | 2026-07-08 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
