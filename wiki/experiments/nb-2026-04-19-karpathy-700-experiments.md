# Run Overnight Autonomous Experiment Sweeps With an Agent

> Back to [[experiments-index]]

Source: **[Karpathy's Agent Ran 700 Experiments While He Slept. It's Coming For You.](https://www.youtube.com/watch?v=xnG8h3UnNFI)** · nb · 2026-04-19

**Status:** `adopted` · **Verdict:** `adopt` · **Effort:** `medium`

---

## Hypothesis

If we configure an AI agent to autonomously run parameterized experiment sweeps overnight with logged results, then we multiply effective experiment throughput by 10x+ because the agent operates continuously without human intervention between iterations.

## What they did

Described Andrej Karpathy's setup where an AI agent autonomously executed ~700 ML experiments overnight, logging results and iterating on hyperparameters without human input between runs.

## Relevance to YOLO loop

Core to the YOLO loop philosophy — automates the run/observe/iterate cycle so the human only reviews a summarized report rather than babysitting each loop tick.

## Notes

See tick_queue_approved entry 'infra-sweep-mode' in session_state.json.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-19 | `backlog` | Extracted from YouTube RSS |
| 2026-04-22 | `adopted` | Promoted to tick queue as infra-sweep-mode. |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-04-19-karpathy-700-experiments` |
| Channel | nb |
| Video | [Karpathy's Agent Ran 700 Experiments While He Slept. It's Coming For You.](https://www.youtube.com/watch?v=xnG8h3UnNFI) |
| Published | 2026-04-19 |
| Ingested upstream | 2026-04-19 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
