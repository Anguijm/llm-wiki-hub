# Use a single vague prompt with delegation and verification instructions to drive a multi-tool agent pipeline

> Back to [[experiments-index]]

Source: **[GPT 5.6 Sol Made This Entire Video](https://www.youtube.com/watch?v=J_jswzXhYJA)** · nh · 2026-07-09

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we write a single prompt that explicitly instructs the agent to delegate subtasks and self-verify outputs, then the agent will autonomously chain external APIs (voice cloning, avatar rendering, video editing) and produce a finished artifact, because modern frontier models can maintain goal-state across tool boundaries when given explicit orchestration intent in the prompt.

## What they did

Nate gave GPT-5.6 Soul one prompt inside Codex on Ultra mode. The agent autonomously researched the launch, wrote a script in his cadence, broke it into sub-60-second sections for voice cloning via ElevenLabs, uploaded audio to HeyGen for avatar rendering, switched the motion engine via browser automation, assembled the edit in Hyperframes, and ran separate inspector agents to QA frames and fact-check against OpenAI release notes. Total cost was ~$300 at API rates (~450M tokens across 9 sub-agents) but he noted that using 'high' instead of 'ultra' effort mode would have halved the cost with similar output.

## Relevance to YOLO loop

This is a direct implementation of the yolo loop applied to content production: one prompt triggers a full execution loop with internal delegation, tool use, and self-QA before surfacing output to the human. The insight about effort-level tuning (high vs ultra) is immediately applicable to our own loop cost management.

## Notes

Key cost finding: Ultra mode over-delegates and inflates token usage. Try identical prompt at 'high' effort and compare output quality vs cost. Also note the self-inspection loop pattern: separate agents review rendered frames against source claims.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-09 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-07-09-single-prompt-full-video-pipeline` |
| Channel | nh |
| Video | [GPT 5.6 Sol Made This Entire Video](https://www.youtube.com/watch?v=J_jswzXhYJA) |
| Published | 2026-07-09 |
| Ingested upstream | 2026-07-09 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
