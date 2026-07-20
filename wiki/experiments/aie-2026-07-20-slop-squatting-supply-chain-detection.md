# Add a package provenance verification step before any agent-suggested dependency is installed

> Back to [[experiments-index]]

Source: **[Agentic Security: Permissions, Provenance, and the Agent Supply Chain — Steve Yegge, Gas Town](https://www.youtube.com/watch?v=yWS0udrIOc8)** · aie · 2026-07-20

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we intercept every package install command issued by a coding agent and verify the package name against a known-good registry (checking download count, age, and name similarity to popular packages) before allowing installation, then we will prevent slop-squatting attacks where agents hallucinate package names that have been pre-poisoned by attackers, because the verification step adds a deterministic check that the agent's probabilistic name generation cannot satisfy alone.

## What they did

Steve Yegge described the slop-squatting attack vector: LLMs hallucinate plausible-sounding package names, attackers monitor which names LLMs commonly hallucinate and upload backdoored packages with those names to public registries. The agent downloads, builds, tests, and ships the backdoored package because it behaves functionally correctly. He argued that every line of agent-generated code now needs more security scrutiny than human-written code, and that surfacing vulnerability signals at generation time (the way Google's TAP system surfaced bugs at the moment of typing) is the only way to manage the compounding defect surface as velocity increases 10x.

## Relevance to YOLO loop

Directly applicable to our YOLO loop: we should add a pre-install hook (e.g. a Claude Code tool hook or shell alias wrapping npm/pip/cargo) that queries package metadata before any installation the agent suggests.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-20 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-20-slop-squatting-supply-chain-detection` |
| Channel | aie |
| Video | [Agentic Security: Permissions, Provenance, and the Agent Supply Chain — Steve Yegge, Gas Town](https://www.youtube.com/watch?v=yWS0udrIOc8) |
| Published | 2026-07-20 |
| Ingested upstream | 2026-07-20 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
