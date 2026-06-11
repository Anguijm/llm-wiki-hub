# Wire a self-critique step into the YOLO build loop before running external tests

> Back to [[experiments-index]]

Source: **[This 100% self-improving AI Agent is insane… just watch](https://www.youtube.com/watch?v=EHlqRx0r4BI)** · do · 2026-03-29

**Status:** `done` · **Verdict:** `adopt` · **Effort:** `medium`

---

## Hypothesis

If we add a self-evaluation step where the builder agent critiques its own code against the acceptance criteria before running test_project.py, then the test pass rate on first attempt improves because obvious issues are self-corrected earlier, reducing total retry cycles.

## What they did

David demonstrates an agent (Agent Zero + Hermes) that generates a solution, then enters a closed self-improvement loop: evaluate output against success criteria, identify gaps, regenerate, repeat. The loop runs autonomously until the evaluation passes — no human in the middle.

## Relevance to YOLO loop

The YOLO Dark Factory loop already retries on test failure, but the retry is triggered by external tests. Adding a pre-test self-critique (agent asks 'does this code actually satisfy the acceptance criteria I defined?') could catch issues before the test suite runs, reducing the outer retry loop.

## Outcome

Subsumed by Codex-as-planner experiment. Gemini plan validation (Phase 1C) serves as the self-critique step — reviews the outline against requirements before build. Combined with 6-angle council (Phase 3) and eval_bugs.py, the loop has self-critique at both plan and review stages.

## Notes

Agent Zero is open-source; Hermes is the evaluation model used for self-scoring. See: https://github.com/agent0ai/agent-zero

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-03 | `done` | Integrated into cron 3-phase pipeline |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-03-29-self-improving-eval-loop` |
| Channel | do |
| Video | [This 100% self-improving AI Agent is insane… just watch](https://www.youtube.com/watch?v=EHlqRx0r4BI) |
| Published | 2026-03-29 |
| Ingested upstream | 2026-04-02 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
