# Use Codex Browser Agent for Automated UI/QA Testing

> Back to [[experiments-index]]

Source: **[Codex's Browser Agent Automates Literally Anything](https://www.youtube.com/watch?v=CB5bG4mvnS0)** · nh · 2026-08-13

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we spin up Codex's browser agent to autonomously QA a web app by instructing it to try to break the UI, then we will surface more edge-case bugs faster than manual testing because the agent can run dozens of focused interaction checks (form validation, navigation, data integrity) in a single session without human fatigue.

## What they did

Nate opened a local form-submission website inside the Codex desktop app, annotated specific UI problems using the in-app annotate tool, then prompted Codex to use browser-use (headed mode) to test the app by trying to break it. The agent clicked through fields, submitted invalid data, changed country codes, tested keyboard submission paths, and reported real data-integrity bugs (invalid contact data passing through, country code resetting). He noted headless mode allows background QA while the developer keeps working.

## Relevance to YOLO loop

Directly applicable as a post-build QA step in the YOLO loop: after generating or modifying a feature, trigger a Codex browser-use session to stress-test the UI before committing, surfacing regressions automatically.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-13 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-08-13-codex-browser-qa-automation` |
| Channel | nh |
| Video | [Codex's Browser Agent Automates Literally Anything](https://www.youtube.com/watch?v=CB5bG4mvnS0) |
| Published | 2026-08-13 |
| Ingested upstream | 2026-08-13 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
