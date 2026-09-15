# Use Adversarial Agent Pairs to Find Contradictions in System Rules or Policy Documents

> Back to [[experiments-index]]

Source: **[Loophole: Adversarial Agents To Stress Test Your Morality — Brendan Rappazzo, Morgan Stanley](https://www.youtube.com/watch?v=hOWU0KPUp1k)** · aie · 2026-09-14

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we run two adversarial agents against a codified rule system — one seeking loopholes (immoral but technically legal) and one seeking overreach (moral but technically prohibited) — then we can surface underspecifications and contradictions in policy documents, agent constitutions, or guardrail rules that human review alone would miss, because LLMs can now perform high-level moral and logical reasoning at scale across synthetic case generation.

## What they did

Brendan Rappazzo presented Loophole, an open-source terminal-based game/framework. Input: natural language description of your morals or rules. Step 1: a codifying agent translates them into a precise legal-style system. Step 2: a loophole-finding agent searches for things that are immoral but technically legal under the system. Step 3: an overreach-finding agent searches for things that are moral but technically illegal. Step 4: a judging agent reviews findings against the original morals and either auto-patches the legal code (if it was a translation error) or escalates to the user for a judgment call (if it reveals a genuine contradiction). He extended this to a Senate Simulator: Claude built moral profiles for all US senators from voting history, ran them through the loophole process, and simulated votes on proposed bills — then hill-climbed bill language to maximize passage votes without violating core bill principles.

## Relevance to YOLO loop

We could apply the Loophole pattern directly to our agent constitutions, system prompts, and guardrail rule sets — running adversarial agents against our own policy documents to find cases where agent behavior would be technically compliant but semantically wrong, or overly restrictive in unintended ways.

## Notes

Full GitHub available via QR code on speaker's website. Senate Simulator extension is a separate branch. The auto-patch vs. escalate decision logic is the most reusable pattern for agent policy testing. Nvidia USA personas dataset used for state-level population simulation.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-14 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-14-loophole-adversarial-agents` |
| Channel | aie |
| Video | [Loophole: Adversarial Agents To Stress Test Your Morality — Brendan Rappazzo, Morgan Stanley](https://www.youtube.com/watch?v=hOWU0KPUp1k) |
| Published | 2026-09-14 |
| Ingested upstream | 2026-09-14 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
