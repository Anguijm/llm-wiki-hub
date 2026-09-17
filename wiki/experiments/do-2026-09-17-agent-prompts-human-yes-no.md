# Invert the prompt direction: let the agent surface action proposals and humans approve with yes/no

> Back to [[experiments-index]]

Source: **[I let GPT-6 Astra run my business… it's insane](https://www.youtube.com/watch?v=R--bWH0x8_c)** · do · 2026-09-17

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we restructure the agent loop so the agent continuously monitors repos, support queues, and cloud metrics and then proposes concrete actions for human approval rather than waiting for human prompts, then human throughput on routine tasks will increase dramatically, because the cognitive load shifts from ideation and instruction to lightweight triage and judgment.

## What they did

Magnus (browser-use founder) described inverting the prompt relationship entirely: instead of humans prompting the AI, the AI monitors all relevant channels (cloud, repos, support tickets, social mentions) and surfaces a queue of proposed actions. Humans swipe Tinder-style yes/no. He demonstrated approving code PRs, customer support replies, and doc improvements purely by reviewing screenshots — never reading the underlying code. He ran this on GPT-4/Astra with browser-use CLI and internal agency tooling.

## Relevance to YOLO loop

This is a direct architectural inversion of the YOLO loop. Instead of the loop running on explicit human-triggered prompts, the loop would run on a scheduled monitor, diff its findings against a known state, generate a ranked proposal queue, and surface the top N items for human yes/no. The loop becomes pull-based from the agent side rather than push-based from the human side.

## Notes

Magnus called this 'agency' — the agent having its own agenda derived from observed signals. Start with a single monitored channel (e.g. GitHub issues) before expanding. Key risk: proposal fatigue if the queue grows faster than human triage capacity. Consider a confidence threshold to auto-approve high-certainty low-risk actions.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-17 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-09-17-agent-prompts-human-yes-no` |
| Channel | do |
| Video | [I let GPT-6 Astra run my business… it's insane](https://www.youtube.com/watch?v=R--bWH0x8_c) |
| Published | 2026-09-17 |
| Ingested upstream | 2026-09-17 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
