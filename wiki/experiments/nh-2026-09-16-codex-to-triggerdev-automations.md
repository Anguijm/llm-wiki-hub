# Offload Codex-Built Automations to Trigger.dev to Preserve Usage Quota

> Back to [[experiments-index]]

Source: **[How to Build GPT-6 Astra Automations (that don't eat your usage limit)](https://www.youtube.com/watch?v=FqnNL8fnUWo)** · nh · 2026-09-16

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we use Codex only to plan and generate automation code, then deploy that code to Trigger.dev (via GitHub) instead of running it as Codex scheduled tasks, then we will preserve our Codex usage limit while still running scheduled and webhook-triggered automations.

## What they did

Nate used Codex (with GPT-6 Astra) to plan and generate TypeScript automation code for three automation types: scheduled (e.g., 6 AM daily calendar brief sent to ClickUp), webhook-triggered, and Codex SDK-based. Instead of hosting the automations inside Codex as scheduled tasks (which consume the weekly usage limit), he pushed the generated code to GitHub and connected Trigger.dev to execute it on schedule or on webhook events. He walked through the full flow: prompting Codex to plan and build the automation, exporting the code, and configuring Trigger.dev to run it independently.

## Relevance to YOLO loop

Directly applicable to our dev loop: any recurring agent tasks (code review triggers, test runners, nightly summaries) that we currently run inside an AI coding agent can be extracted as code and hosted externally, freeing up quota for interactive development work.

## Notes

Three automation types covered: scheduled, webhook, and Codex SDK. Trigger.dev free plan may delay scheduled triggers by up to an hour. Requires GitHub account + Trigger.dev account.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-16 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-09-16-codex-to-triggerdev-automations` |
| Channel | nh |
| Video | [How to Build GPT-6 Astra Automations (that don't eat your usage limit)](https://www.youtube.com/watch?v=FqnNL8fnUWo) |
| Published | 2026-09-16 |
| Ingested upstream | 2026-09-16 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
