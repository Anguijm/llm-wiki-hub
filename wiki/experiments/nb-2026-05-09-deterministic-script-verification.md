# Add deterministic verification scripts as post-agent hooks

> Back to [[experiments-index]]

Source: **[You're Wasting 40% Of Your AI Time On Something Fixable](https://www.youtube.com/watch?v=647pSnX5H_Y)** · nb · 2026-05-09

**Status:** `done` · **Verdict:** `adopt` · **Effort:** `low`

---

## Hypothesis

If we add deterministic scripts as post-execution hooks rather than asking the LLM to self-check, then agent output quality and trustworthiness will improve because deterministic checks cannot hallucinate or rationalize away errors.

## What they did

Speaker explicitly distinguished hooks and scripts from LLM-driven steps, noting that scripts are deterministic checks and you should not trust the model to check itself. He described this as a real gap in most agentic pipelines and a common point of confusion with senior leadership.

## Relevance to YOLO loop

Maps directly to the verification phase of our dev loop; we can add shell/Python assertion scripts that run after Claude Code completes a task to catch regressions without relying on model self-evaluation.

## Outcome

Scaffolded in experiments/deterministic-script-verification/ (PR #10): verify.py works against golden-fixture JSON (catches injected regressions); fixtures/ has frozen process_experiments input + expected shape; proposed_ci_check.yml is a draft GHA workflow ready for a follow-on wire-up tick.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-05-09 | `backlog` | Extracted from YouTube RSS |
| 2026-05-15 | `done` | Scaffold deliverables shipped in PR #10; promoted via PR #11 (tick_queue_approved). Status flipped post-merge since deliverables already on main. |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-05-09-deterministic-script-verification` |
| Channel | nb |
| Video | [You're Wasting 40% Of Your AI Time On Something Fixable](https://www.youtube.com/watch?v=647pSnX5H_Y) |
| Published | 2026-05-09 |
| Ingested upstream | 2026-05-09 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
