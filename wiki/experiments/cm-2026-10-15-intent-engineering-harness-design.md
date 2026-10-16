# Audit current Claude Code workflow for 'meat proxy' failure modes and add explicit intent-engineering harness steps at planning and validation boundaries

> Back to [[experiments-index]]

Source: **[Is Learning to Build Software Still Worth It with AI? (My Honest Take)](https://www.youtube.com/watch?v=PMOnd8T7Py0)** · cm · 2026-10-15

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we add structured intent-engineering checkpoints at the start (agent grills us with questions before coding) and end (agent validates output against stated intent) of every Claude Code task, then agent mistake rate drops and output quality improves, because the agent's middle step (writing code) is already strong — mistakes are almost always failures of intent communication at the boundaries.

## What they did

Cole used the REA (Reverse Engineer Anything) viral repo as a case study to argue that the repo works so well specifically because the target application IS the intent — the agent can continuously self-validate against a concrete reference, eliminating the intent communication problem entirely. He then argued this is the exception, not the rule: for most tasks, communicating intent is the bottleneck and humans who skip it become 'meat proxies' (dump Jira ticket to agent, pass output to Slack unchanged, add zero value). He outlined what's worth learning as LLMs improve: communicating intent and harness engineering (planning + validation layers, skills, sub-agents, hooks, software factory patterns) become MORE important as models get more capable because we give them harder tasks. What matters less: prompt engineering tricks, giant rule files, teaching general software engineering principles. The test: 'if the next model is twice as good, does this skill matter more or less?'

## Relevance to YOLO loop

high: directly prescribes the harness design pattern — intent grilling pre-task and intent validation post-task are the two missing layers in most Claude Code workflows.

## Notes

Cole mentions a 'software factory' harness he's building — worth tracking as a potential skill to adopt. The REA connection ties this card to the nb-2026-10-15-rea-xray-vision-workflow card.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-15 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `cm-2026-10-15-intent-engineering-harness-design` |
| Channel | cm |
| Video | [Is Learning to Build Software Still Worth It with AI? (My Honest Take)](https://www.youtube.com/watch?v=PMOnd8T7Py0) |
| Published | 2026-10-15 |
| Ingested upstream | 2026-10-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
