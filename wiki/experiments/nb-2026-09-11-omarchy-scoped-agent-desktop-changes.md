# Run Scoped Agent Tasks Against Documented OS Configuration Handles

> Back to [[experiments-index]]

Source: **[Is Omarchy The Last Desktop You'll Ever Need?](https://www.youtube.com/watch?v=zDPuEPDXCpU)** · nb · 2026-09-11

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we constrain agent desktop-modification requests to specific, documented configuration handles (e.g., window rules, workspace launchers, shortcut definitions) rather than open-ended 'make it better' prompts, then agent success rate and reliability will increase because the agent has defined read/write surfaces with predictable feedback loops.

## What they did

Nate walked through Omarchy's philosophy of making desktop behavior accessible through documented config files and tooling so agents have concrete handles to operate on. He advised starting with narrow, reversible tasks: find a specific setting, identify the file that controls it, keep a copy of the original, apply the change, test it, then undo it. He extended the pattern to macOS (AeroSpace window rules, Apple Shortcuts via CLI) and Windows (PowerToys Workspaces), arguing the lesson generalizes: before asking an agent to improvise, find the documented, supported action surface and drive the agent through that.

## Relevance to YOLO loop

Directly maps to how we scope agent tasks in the YOLO loop: rather than giving agents free-form environment access, we should enumerate documented config surfaces first, wrap changes in reversible checkpoints, and validate against a known-good baseline before committing — reducing blast radius on each loop iteration.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-11 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-09-11-omarchy-scoped-agent-desktop-changes` |
| Channel | nb |
| Video | [Is Omarchy The Last Desktop You'll Ever Need?](https://www.youtube.com/watch?v=zDPuEPDXCpU) |
| Published | 2026-09-11 |
| Ingested upstream | 2026-09-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
