# Build a CI gate that runs hybrid deterministic + LLM security scans on AI skills before marketplace publish

> Back to [[experiments-index]]

Source: **[We Vetted 2000 AI Skills Before They Reached Developers — Lucas Palma, Nubank](https://www.youtube.com/watch?v=iKQ78wyJEXU)** · aie · 2026-07-29

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we add a CI step that runs deterministic regex checks followed by LLM behavioral analysis on every AI skill before it reaches an internal marketplace, then we will catch dangerous patterns like hardcoded credentials, shell injection, excessive permissions, and false human-in-the-loop confirmations before they propagate to developer workflows, because treating skills as supply-chain dependencies surfaces risks that code review alone misses.

## What they did

Nubank built 'Skill Vector', a tool that intercepts skill pull requests before marketplace publish. It runs deterministic checks (regex for credentials, shell commands, permission patterns) and then LLM review for behavioral risks like destructive instructions and fake confirmation loops. Findings are reported as PR comments so engineers can remediate before upload. Engineers can also run it locally during iteration. A historical scan of pre-existing skills found additional vulnerabilities fed into their vuln management program.

## Relevance to YOLO loop

If the YOLO loop uses shared skills or an internal skill registry, a lightweight version of this gate (deterministic checks at minimum) would prevent malicious or poorly-scoped skills from affecting agent behavior in production pipelines.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-29 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-29-ai-skill-security-review` |
| Channel | aie |
| Video | [We Vetted 2000 AI Skills Before They Reached Developers — Lucas Palma, Nubank](https://www.youtube.com/watch?v=iKQ78wyJEXU) |
| Published | 2026-07-29 |
| Ingested upstream | 2026-07-29 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
