# Build a multi-persona debate council skill (Roast Room) for high-stakes decisions

> Back to [[experiments-index]]

Source: **[This ONE Claude Skill Helps You Think Clearer Than 99% of People](https://www.youtube.com/watch?v=nRXHWckVxoM)** · nh · 2026-10-15

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we run a structured multi-round debate among specialized AI personas (each with a single core decision lens) before making a key product or business decision, then decision quality will improve because diverse expert perspectives surface blind spots and prevent the model from simply agreeing with the user's initial framing.

## What they did

Nate built a Claude Code skill called 'Roast Room' that instantiates 7 advisor personas (Bezos, Graham, Hormozi, Gary Vee, Martell, Wickman, Buffett), each with a distinct single-question evaluation lens. The skill runs 3 rounds: each advisor states a position with a scored option, they read each other's positions and debate, and in round 2 dissenting advisors are forced to argue for the minority option. A chair sub-agent facilitates. Final verdicts include scores, rationale, and a consensus recommendation. He also generalized the pattern to any specialized agent pair (e.g., security agent vs. CTO agent) debating a technical question.

## Relevance to YOLO loop

Maps to our architecture review and prioritization gates: running a roast room before committing to a technical approach or feature set would surface tradeoffs we'd otherwise miss and reduce costly late-stage pivots.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-15 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-10-15-roast-room-multi-persona-decision-council` |
| Channel | nh |
| Video | [This ONE Claude Skill Helps You Think Clearer Than 99% of People](https://www.youtube.com/watch?v=nRXHWckVxoM) |
| Published | 2026-10-15 |
| Ingested upstream | 2026-10-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
