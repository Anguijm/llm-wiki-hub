# Let the AI Agent Pick Its Own Problem from Your Business Context

> Back to [[experiments-index]]

Source: **[Codex vs Fable: Which AI Agent Picked the Better Problem?](https://www.youtube.com/watch?v=uCWKXIyvM_8)** · nb · 2026-07-17

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we give an AI agent unrestricted access to our local files, Slack, and business artifacts and instruct it to identify, define, and solve its own problem rather than prescribing one, then it will surface pain points we have blind spots about and produce more contextually relevant automations, because the AI can correlate behavioral evidence across all data rather than relying on our verbal self-assessment.

## What they did

Nate gave both Codex (in Ultra mode) and Fable freehand access to all local files and Slack channels, instructing each agent to (1) discover the workspace, (2) independently define the most pressing problem, (3) build an automation to address it, and (4) explain its reasoning. Codex chose a bounded, easily-voiceable problem—improving the research-to-scripting handoff package—while Fable identified a more strategically leveraged problem: pre-pipeline idea refinement to make story selection easier. Nate noted Codex consistently picks bounded, already-articulated problems even with large token budgets, while Fable demonstrated broader strategic pattern recognition. He then codified the prompting approach into a reusable 'skill' that instructs the AI not to think small, to root-cause deeply, to consider security, and to build a complete solution rather than a partial one.

## Relevance to YOLO loop

Directly applicable as a loop-initialization step: before writing any code or prompt, run this skill against the project repo and communication history to let the agent nominate the highest-leverage automation target. Also validates using two competing agents (Codex + a frontier model) in parallel for problem discovery and then routing the winner's spec back into Codex for cheaper implementation.

## Notes

Key prompt design constraint from transcript: explicitly remind the agent not to think small and to build completely through to security and auth if needed. Codex Ultra burns significantly more tokens—budget accordingly. Nate ended up preferring Fable's problem framing but Codex's daily-driver ergonomics; the recommended pattern is parallel runs then cherry-pick.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-17 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-07-17-ai-picks-the-problem` |
| Channel | nb |
| Video | [Codex vs Fable: Which AI Agent Picked the Better Problem?](https://www.youtube.com/watch?v=uCWKXIyvM_8) |
| Published | 2026-07-17 |
| Ingested upstream | 2026-07-17 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
