# Implement a Skill Provenance Check Before Installing Any Agent Skill

> Back to [[experiments-index]]

Source: **[Your Agent Attacks Real People Now. Nobody Has To Ask It To.](https://www.youtube.com/watch?v=4f5AJrJPilM)** · nb · 2026-08-17

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we review the full contents of every skill.md file and resolve all external links before installing a skill into an agent, then we will block supply-chain poisoning attacks because malicious skills embed external links that can be swapped to deliver credential-stealing payloads after a trust window has elapsed.

## What they did

Zenity Labs disclosed at Black Hat (Aug 6) a campaign of poisoned MCP/agent skills that accumulated 1.7M installs by Aug 2. The attack worked by embedding an innocuous external link in skill.md; attackers later swapped the link target to instructions that downloaded code hunting for SSH keys, cloud credentials, and git tokens. Vercel had three scanning vendors and 60k+ skill audits running and the campaign still succeeded. Speaker recommends treating random skill installs like random USB drives.

## Relevance to YOLO loop

The YOLO loop relies on skills/tools to extend agent capability. Adding a pre-install checklist (resolve all URLs, snapshot skill.md hash, sandbox first run) fits as a gate in our tooling onboarding step and protects credentials used throughout the loop.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-17 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-08-17-skill-provenance-audit` |
| Channel | nb |
| Video | [Your Agent Attacks Real People Now. Nobody Has To Ask It To.](https://www.youtube.com/watch?v=4f5AJrJPilM) |
| Published | 2026-08-17 |
| Ingested upstream | 2026-08-17 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
