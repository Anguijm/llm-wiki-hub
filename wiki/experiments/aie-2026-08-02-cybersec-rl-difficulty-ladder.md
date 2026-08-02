# Structure RL training environments as a two-axis difficulty ladder: target hardness × exploitation depth

> Back to [[experiments-index]]

Source: **[Teaching AI to Find Real Vulnerabilities — Prof. David Brumley, Bugcrowd](https://www.youtube.com/watch?v=ZFxh7sqbUZo)** · aie · 2026-08-02

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we design reinforcement learning task curricula along two independent axes — target difficulty (toy → CTF/synthetic → hardened real targets) and exploitation depth (bug detection → crash trigger → arbitrary read/write → full code execution) — then models will learn generalizable security skills rather than memorizing specific exploits, because the ladder structure forces acquisition of prerequisite skills before advancing, mirroring how human experts actually learn.

## What they did

David Brumley (CMU / Bugcrowd) described how his team teaches LLMs to find real vulnerabilities using the same methodology that produced Pwn2Own winners from novices. The two-axis framework: (1) target difficulty from toy programs through CTF challenges to hardened production targets; (2) exploitation skill from locating a bug, to triggering a crash, to arbitrary memory read/write, to full arbitrary code execution. He showed their Mythos system finding novel exploits (not public) for CVE-2024-7965 (x86 path experts thought impossible) and CVE-2024-0519. To prevent memorization, they use zero-day vulnerabilities as training targets — unknown to the model. They generate up to 10,000 RL environments/month for partners. All environments are Docker images with MCP interfaces available at exploitbench.ai.

## Relevance to YOLO loop

The two-axis curriculum design principle applies beyond cybersecurity: any YOLO loop agent skill (code review, refactoring, debugging) can be structured as a difficulty ladder to build robust generalizable capability rather than pattern-matching on easy cases.

## Notes

Environments available at exploitbench.ai as Docker images with MCP interfaces. Mythos transcripts withheld due to NDA and novel exploit concern. Key insight: oracles must prevent models from stopping at easiest vulnerability — design oracles that require full exploitation chain.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-02 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-02-cybersec-rl-difficulty-ladder` |
| Channel | aie |
| Video | [Teaching AI to Find Real Vulnerabilities — Prof. David Brumley, Bugcrowd](https://www.youtube.com/watch?v=ZFxh7sqbUZo) |
| Published | 2026-08-02 |
| Ingested upstream | 2026-08-02 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
