# Apply 9 token-reduction habits to cut reused-input waste in long AI sessions

> Back to [[experiments-index]]

Source: **[Paste This Into Claude, Never Hit a Token Limit Again](https://www.youtube.com/watch?v=Y8vAQ1FgNbM)** · nb · 2026-07-29

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we systematically apply habits like editing mistakes instead of appending corrections, batching related questions, and specifying output format upfront, then we will reduce reused-input token volume per session because each of these habits prevents unnecessary context from accumulating across turns.

## What they did

Nate audited his own Codex workspace and found 96% of 3.77B tokens in one day were reused input. He identified that every new message resends the entire conversation history, so corrections and follow-ups compound costs rapidly. His Level 1 response is nine habits: edit mistakes instead of appending, batch related questions with explicit output format, and other context-hygiene practices that require no installs and work on any AI.

## Relevance to YOLO loop

Directly applies to any iterative dev loop using Claude or Codex; reducing reused-input bloat extends effective session length before hitting limits during code generation and debugging cycles.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-29 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-07-29-token-limit-habits` |
| Channel | nb |
| Video | [Paste This Into Claude, Never Hit a Token Limit Again](https://www.youtube.com/watch?v=Y8vAQ1FgNbM) |
| Published | 2026-07-29 |
| Ingested upstream | 2026-07-29 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
