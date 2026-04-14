# yolo-phase4 integration

> Back to [[index]]

**How this wiki consumes experiment summaries from the [[yolo-projects]] Phase 4 research pipeline.**

---

## Why this exists

The [[yolo-projects]] repo runs a daily cron (06:15 JST) that scans 10 AI/dev YouTube channels for new videos, extracts "experiment cards" via Gemini, and commits them to `experiments.json`. That's 75+ pre-synthesized experiments with hypothesis, actionable steps, outcomes, and status tracking.

Earlier we tried to replicate this: [[automation|scheduled workflow]] using the RSS feeds + `youtube-transcript-api` to fetch raw transcripts. That pipeline kept hitting YouTube's IP blocks on GitHub Actions runners (datacenter IPs are aggressively throttled). Meanwhile yolo-projects' cron worked fine because it runs from a different environment and only touches RSS feeds (not the transcript endpoints).

Rather than duplicate the scrape, **we consume yolo-projects' already-committed output** and skip our own transcript fetching entirely for these channels. The upstream data is also richer than a raw transcript: already summarized, annotated with verdicts, and cross-referenced with target projects.

## Data flow

```
┌──────────────────────────────────────┐
│  yolo-projects (upstream)             │
│  ────────────────────                 │
│  1. Daily cron (06:15 JST)            │
│  2. fetch_youtube_rss.py              │
│  3. Gemini extracts experiment cards  │
│  4. Commit to experiments.json        │
└────────────────┬─────────────────────┘
                 │ raw.githubusercontent.com
                 ▼
┌──────────────────────────────────────┐
│  llm-wiki-hub (this repo)             │
│  ──────────────────                   │
│  5. scripts/ingest-yolo-phase4.py     │
│     fetches experiments.json          │
│  6. Dedupe vs fingerprints.json       │
│     (key: "phase4:<experiment-id>")   │
│  7. For new entries:                  │
│     - render wiki/experiments/*.md    │
│       from structured template        │
│     - archive raw data in             │
│       cold_storage/yolo-phase4/       │
│  8. Commit wiki pages + fingerprints  │
│     back to main                      │
└──────────────────────────────────────┘
```

## Files

| Path | Purpose |
|---|---|
| `scripts/ingest-yolo-phase4.py` | Fetches upstream JSON, writes wiki pages + archives |
| `.github/workflows/sync-yolo-phase4.yml` | Scheduled + manual sync workflow |
| `wiki/experiments/*.md` | One page per experiment (committed) |
| `wiki/experiments-index.md` | Tabular index of all experiments |
| `cold_storage/yolo-phase4/<slug>/data.json` | Raw per-experiment archive (gitignored contents) |
| `cold_storage/yolo-phase4/phase4_run.json` | Upstream run metadata (last sync) |

## Why this skips `active_sources/`

The standard pipeline is `active_sources/` -> Claude summarizes -> `wiki/` -> `cold_storage/`. The Claude-summarization step exists because raw sources (transcripts, article HTML, repo source code) need distillation before becoming wiki pages.

yolo-projects' experiments are **already distilled**: Gemini has extracted title, hypothesis, actionable steps, success metric, outcome, and verdict. Summarizing them a second time would add no information. So this ingest path writes structured templates directly to `wiki/experiments/`, and `cold_storage/yolo-phase4/` holds the raw JSON purely as an audit trail.

If an experiment's wiki page ever needs refinement beyond the template (e.g., adding cross-links to other wiki pages that Claude knows about), that's done as an ordinary wiki edit, not as part of the ingest flow.

## Running locally

```bash
# Fetch from GitHub (default)
python scripts/ingest-yolo-phase4.py

# Fetch from a local clone (useful for testing/offline)
python scripts/ingest-yolo-phase4.py --local /path/to/yolo-projects
```

Dedup is by `id` and `sha256(exp)`: if an existing experiment's content hash changes upstream (e.g., status updated, outcome added), the wiki page is regenerated. Otherwise it's skipped.

## Schema preserved in wiki pages

From each upstream experiment entry, wiki pages include:

- **Source** - video title, URL, channel, published date
- **Hypothesis**, **What they did**, **Actionable steps**, **Success metric**, **Relevance to YOLO loop**
- **Status** (`proposed` / `done` / `adopted` / `deferred` / `discarded`)
- **Verdict** (`adopt` / `discard` / `defer` / ...)
- **Outcome** and **Notes** (when present)
- **Status history** as a timeline table
- **Target projects** (cross-linked to other wiki pages when recognized)

## Relationship to other ingest paths

| Ingest mechanism | Covers | Status |
|---|---|---|
| `ingest-yolo-phase4.py` | 10 tracked AI/dev channels (yolo-phase4 roster) | **Primary** for these channels |
| `ingest-youtube.py --from-tracked` | Same 10 channels via our own RSS + transcripts | Keep as backup; frequently IP-blocked on GH runners |
| `ingest-youtube.py --video <url>` | Ad-hoc single videos outside the roster | Still useful |
| `ingest-youtube.py --from-queue` | One-off URLs queued in `queue.yml` | Still useful |

The [[tracked-channels-schema|tracked_channels.yml]] roster is now primarily documentation of *which* channels yolo-phase4 watches. The actual fetching for those channels is offloaded to yolo-projects.

## Failure modes

| Failure | Behavior |
|---|---|
| Upstream `experiments.json` missing | Script exits non-zero; workflow fails noisily |
| Upstream unchanged since last sync | Zero new pages, workflow exits 0, no commit |
| Individual experiment malformed | Logged; skipped; loop continues |
| Network error fetching from GitHub raw | Script exits non-zero |

## Related pages

- [[yolo-projects]] - upstream pipeline
- [[experiments-index]] - all 75 experiments
- [[tracked-channels-schema]] - channel roster (shared with yolo-projects)
- [[automation]] - other GH Actions workflows
- [[architecture]] - full wiki pipeline
- [[index]] - wiki home
