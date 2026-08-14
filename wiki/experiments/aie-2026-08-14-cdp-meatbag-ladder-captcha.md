# Use the CDP Meatbag Ladder Pattern for Agent Browser Automation Instead of MCP

> Back to [[experiments-index]]

Source: **[The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans — Corey Gallon, Rexmore](https://www.youtube.com/watch?v=26RtyAm9y_Q)** · aie · 2026-08-14

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we drive a browser agent via the Chrome DevTools Protocol through a CLI (not an MCP server), following a sense→act→verify loop that escalates to increasingly human-like interaction only when lower rungs fail, then the agent completes browser tasks faster and cheaper than MCP-based approaches because the model is only invoked for perception tasks, not for every deterministic click.

## What they did

The speaker implemented a 'meatbag ladder': Rung 1 — use synthetic JavaScript clicks via CDP (free, instant, no model); Rung 2 — use real CDP input-domain clicks when JS clicks are detected; Rung 3 — invoke a full human-fingerprint browser profile when detection escalates. The sense→act→verify loop checks outcome via a different channel than the action (e.g., check network traffic after a click, not the click's own return value). For CAPTCHA solving, deterministic code handled all steps (trusted click, iframe piercing, round re-arm) except tile classification, where vision was the only step given to an AI model. Compared to MCP: CLI achieved same task in 7 turns / <1 min vs MCP's 71 turns / 8 min; Anthropic reports CLI is up to 75x cheaper in tokens.

## Relevance to YOLO loop

If the YOLO loop includes any web-automation tasks (scraping, form submission, UI testing), switching from MCP-driven browser control to a CDP CLI pattern with the meatbag ladder would dramatically reduce per-task latency and token cost while improving reliability against anti-bot defenses.

## Notes

Speaker's open-source tool 'Chrome Agent' (Python, pip-installable) implements this pattern. Key insight: speed is mandatory for CAPTCHA solving because challenge rounds expire; a model-in-the-loop on every click burns the clock. Only give the model one look per round.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-14 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-14-cdp-meatbag-ladder-captcha` |
| Channel | aie |
| Video | [The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans — Corey Gallon, Rexmore](https://www.youtube.com/watch?v=26RtyAm9y_Q) |
| Published | 2026-08-14 |
| Ingested upstream | 2026-08-14 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
