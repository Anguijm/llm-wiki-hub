# Inject a hierarchical hypothesis-generation step into autonomous coding agent loops to break optimization plateaus

> Back to [[experiments-index]]

Source: **[Autonomous Agents for Scientific Tasks - Sina Shahandeh, Radicait](https://www.youtube.com/watch?v=XLEYtv3cMlw)** · aie · 2026-07-19

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we augment an autonomous coding/ML optimization loop with an explicit hierarchical hypothesis-generation phase (invoking a stronger reasoning model like o3/GPT-5 Pro to propose radical architectural changes) rather than letting the agent iterate only within its current search space, then the loop will escape local optima that standard hill-climbing saturates at, because agents exhaust known implementation variations quickly but lack 'research taste' to propose paradigm shifts without external ideation scaffolding.

## What they did

Speaker at Radicait was running a Codex-based agent loop to optimize a CT-to-PET image translation model (encoder-decoder GAN). The agent would hill-climb hyperparameter and code changes but plateau — it would not propose radical changes like switching from 2.5D (stacked 2D convolutions) to full 3D convolutions because that requires creative hypothesis generation beyond implementation skill. His solution: (1) decompose the long-horizon research problem into a hierarchy of sub-problems; (2) at each plateau, invoke a stronger multimodal/reasoning model (Gemini for image review, o3/GPT-5 Pro via Oracle CLI for hypothesis generation) as an oracle that receives packaged code + data + current results and proposes next hypotheses; (3) build these oracle calls as explicit skills/tools the agent loop can invoke. He also used adversarial or collaborative sub-agent loops where one model critiques the generated image quality and another generates the improvement hypothesis. Noted this is the same trick as chain-of-thought applied at the loop level rather than the token level.

## Relevance to YOLO loop

Directly applicable when the YOLO loop stalls on a problem: instead of more iterations of the same agent, inject a hierarchical oracle call to a stronger reasoning model with full context (code + data + current metrics) to generate a novel hypothesis, then resume the loop with the new direction. Pattern generalizes beyond ML to any optimization task.

## Notes

Tool referenced: Peter Steinberger's Oracle CLI for packaging code+data and sending to GPT-5 Pro API. Key bottleneck identified: multimodal models cannot yet observe subtle scientific image features (e.g. small lung nodules) the way trained scientists can — limits fully closed-loop scientific agents. Speaker predicts newer post-trained models will internalize hierarchical decomposition natively, reducing need for explicit scaffolding.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-19 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-19-hierarchical-hypothesis-generation` |
| Channel | aie |
| Video | [Autonomous Agents for Scientific Tasks - Sina Shahandeh, Radicait](https://www.youtube.com/watch?v=XLEYtv3cMlw) |
| Published | 2026-07-19 |
| Ingested upstream | 2026-07-19 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
