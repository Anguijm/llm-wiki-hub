# Run Computer-Use Agents in the Background Without Screen Takeover

> Back to [[experiments-index]]

Source: **[Computer-Use 2.0: Agents Just Got Multi-Cursor — Francesco Bonacci, Cua](https://www.youtube.com/watch?v=ZSQb5fzRFPw)** · aie · 2026-07-16

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we use a background computer-use driver (like Quad Driver) that leverages accessibility trees and undocumented OS APIs instead of screen capture and control, then agents can operate on the host machine without disrupting the user's active session, because the agent interacts at the OS accessibility layer rather than the pixel/input layer.

## What they did

Francesco Bonacci described Quad Driver, an open-source background computer-use driver built over one weekend after OpenAI released their computer-use model. It works on macOS, Windows, and Linux by using undocumented Apple accessibility framework APIs and equivalent OS-level interfaces. The agent observes window state via accessibility trees plus screenshots, attempts background actions using the accessibility tree first, and falls back to pixel-level background clicks if needed. This allows agents to run without taking over the user's screen. They also built Kua Bench for evaluating agent task completion and Kua Fleet for warm-pooling sandboxes to minimize GPU idle time during training.

## Relevance to YOLO loop

If our YOLO loop includes any GUI automation or desktop agent tasks, Quad Driver offers a way to run those agents in the background without interrupting active development sessions. The accessibility-tree-first approach also produces more structured action traces that could be easier to log and replay than pixel-level recordings.

## Notes

Quad Driver is open source. The warm-pool sandbox autoscaler described by Rob (Kua Fleet) is also worth a separate look if we ever run parallelized agent training — it addresses GPU idle time during sandbox reset cycles by demand-based autoscaling the warm pool.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-16 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-16-background-computer-use-quad-driver` |
| Channel | aie |
| Video | [Computer-Use 2.0: Agents Just Got Multi-Cursor — Francesco Bonacci, Cua](https://www.youtube.com/watch?v=ZSQb5fzRFPw) |
| Published | 2026-07-16 |
| Ingested upstream | 2026-07-16 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
