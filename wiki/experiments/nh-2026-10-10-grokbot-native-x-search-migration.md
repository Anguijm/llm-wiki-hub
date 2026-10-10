# Migrate Grokbot X-search routines from paid API to built-in free X access

> Back to [[experiments-index]]

Source: **[Grok Bot Just Got 2 Massive Upgrades. Do These Things Now.](https://www.youtube.com/watch?v=MgvwZaDPCs4)** · nh · 2026-10-10

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we update all Grokbot agents that previously called the paid X developer API to use Grokbot's new native built-in X search, then we eliminate per-tweet API costs (~$5/week) with no loss of functionality, because native X search is now a free, built-in capability with a daily allowance of ~1,000 reads resetting nightly.

## What they did

Nate had multiple Grokbot agents (X monitor, Minor, Pod, AIS, News, Motion, etc.) that searched X via a paid developer API. After Grokbot added native X search, he updated his primary X-monitoring bot to use the built-in search, then had that bot message all other bots to inform them of the change. He confirmed cost dropped to $0 for X searches, with a free daily read allowance of ~1,000 resets nightly around 7pm Central.

## Relevance to YOLO loop

Any agent in our dev loop that pulls external data (tweets, news, social signals) via paid APIs should be audited for equivalent free native integrations. Switching saves budget and reduces credential/API key management overhead.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-10 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-10-10-grokbot-native-x-search-migration` |
| Channel | nh |
| Video | [Grok Bot Just Got 2 Massive Upgrades. Do These Things Now.](https://www.youtube.com/watch?v=MgvwZaDPCs4) |
| Published | 2026-10-10 |
| Ingested upstream | 2026-10-10 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
