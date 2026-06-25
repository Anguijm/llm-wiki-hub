# Build a PolySkill universal adapter to convert skills bidirectionally between Claude Code and Codex

> Back to [[experiments-index]]

Source: **[How to INSTANTLY Run ANY Skill in Claude + Codex](https://www.youtube.com/watch?v=tjjX43FoAUg)** · mk · 2026-06-11

**Status:** `adopted` · **Verdict:** `adopt` · **Effort:** `medium`

---

## Hypothesis

If we create a single 'polyskill' meta-skill that understands the structural differences between Claude Code and Codex skill formats (kebab-case names, bang-backtick dynamic injection, sidecar YAML, description length limits), then we can convert any skill to work in both providers in under 60 seconds rather than manually maintaining duplicate versions, because the adapter encodes all format transformation rules once.

## What they did

Mark identified key structural differences between Claude Code and Codex skills: Claude Code supports terminal command injection via backtick-bang syntax and reads all skill descriptions up to a character limit on session start, while Codex has a sidecar YAML file for tool/service config and truncates descriptions past a certain length, potentially hiding trigger conditions. He built a 'polyskill' skill and /polyskill slash command that takes any existing skill, inspects its structure, and repackages it with the correct format for both providers simultaneously, installing it globally at ~/.claude and ~/.agents. Demonstrated converting a YouTube competitor analysis skill and a front-end design skill to Codex in under 10 seconds each, and showed bidirectional conversion (Codex-native skills imported into Claude Code). He noted the same approach can extend to rules, hooks, and other system components.

## Relevance to YOLO loop

If our YOLO loop uses both Claude Code and Codex agents for different tasks, this adapter prevents skill fragmentation and lets us maintain a single source of truth for each workflow, reducing maintenance overhead as providers evolve.

## Notes

Backlog triage 2026-06-24 (owner-preference model). Skill portability across Claude/Codex — supports the dual-tool routing already adopted.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-11 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mk-2026-06-11-polyskill-cross-provider-adapter` |
| Channel | mk |
| Video | [How to INSTANTLY Run ANY Skill in Claude + Codex](https://www.youtube.com/watch?v=tjjX43FoAUg) |
| Published | 2026-06-11 |
| Ingested upstream | 2026-06-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
