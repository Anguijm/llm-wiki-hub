# Automation (GitHub Actions)

> Back to [[index]]

---

## Overview

Two GitHub Actions workflows automate ingestion so you don't have to run the scripts locally:

| Workflow | File | Trigger |
|---|---|---|
| **Scan Tracked YouTube Channels** | `.github/workflows/scan-tracked-channels.yml` | Scheduled (daily) + manual |
| **Process Queue** | `.github/workflows/process-queue.yml` | Manual only |

Both run on GitHub-hosted runners (free for public repos). The "UI" is the standard **Actions** tab on GitHub — click **Run workflow** to open a form with input fields.

## Workflow 1: Scan Tracked YouTube Channels

Reads [[tracked-channels-schema|tracked_channels.yml]] and ingests new videos from every subscribed channel.

### Triggers

| Trigger | When | Notes |
|---|---|---|
| `schedule` | Daily at 21:15 UTC (06:15 JST) | Matches the yolo-projects Phase 4 cadence |
| `workflow_dispatch` | On demand | Available via GitHub Actions tab |

### Inputs (manual runs only)

| Input | Type | Purpose |
|---|---|---|
| `limit` | string (int) | Override per-channel video limit for a one-off run |
| `dry_run` | boolean | Resolve channels + list new videos without fetching transcripts |

### What it does

1. Checks out the repo
2. Installs `yt-dlp` + `pyyaml`
3. Runs `python scripts/ingest-youtube.py --from-tracked`
4. Uploads `active_sources/youtube/` as a workflow artifact (30-day retention)
5. Writes a summary to `$GITHUB_STEP_SUMMARY` (renders as a nice table in the Actions UI)
6. Commits the updated `cold_storage/fingerprints.json` so dedup state persists across runs

### Output

- **Artifact**: `youtube-transcripts-<run-id>.zip` — download from the run page, then ask Claude to summarize locally
- **Commit on `main`**: `chore: scan tracked channels (N new videos)` — only created if new videos were found
- **Step summary**: Table of channels + new video counts, visible in the Actions tab

## Workflow 2: Process Queue

Processes one-shot URLs listed in [[queue-schema|queue.yml]].

### Triggers

Manual only (`workflow_dispatch`).

### Inputs

| Input | Type | Default | Purpose |
|---|---|---|---|
| `articles` | boolean | `true` | Run `ingest-article.py --from-queue` |
| `videos` | boolean | `true` | Run `ingest-youtube.py --from-queue` |

### What it does

Same skeleton as Workflow 1, but runs against `queue.yml` instead of `tracked_channels.yml`, and installs the article script's optional extras (`readability-lxml`, `html2text`) for better extraction.

## How to Run a Workflow Manually

1. Navigate to the repository on GitHub
2. Click the **Actions** tab
3. Pick the workflow from the left sidebar (e.g., "Scan Tracked YouTube Channels")
4. Click **Run workflow** (top-right)
5. Fill in any inputs, click **Run workflow**

## How to Download Artifacts

1. Actions tab → click the run
2. Scroll to **Artifacts** at the bottom
3. Download the `.zip` — it contains the full `active_sources/youtube/` or `active_sources/` tree

Then locally:

```bash
# Extract into active_sources/
unzip youtube-transcripts-<run-id>.zip -d active_sources/youtube/

# Ask Claude to generate wiki pages
# "Process the new sources in active_sources/ into wiki pages."
```

## Concurrency

Both workflows use `concurrency: group: <name>` to prevent scheduled and manual runs from racing on `cold_storage/fingerprints.json`. `cancel-in-progress: false` means queued runs wait instead of being cancelled.

## Permissions

The workflows request `contents: write` so they can push the fingerprints commit back. No other permissions are needed, and no secrets are required — everything runs on the public YouTube RSS + `yt-dlp` stack.

## Cron Adjustment

The default schedule is `15 21 * * *` (21:15 UTC daily). Edit `.github/workflows/scan-tracked-channels.yml` to change it. GitHub Actions cron uses UTC.

## Limitations

- **Claude summarization is NOT automated.** The workflows stop after ingestion. You still need to pull the artifact (or branch) and run Claude locally to generate wiki pages. This is intentional — automating Claude would require storing an API key as a repo secret and metered API calls.
- **Workflow artifacts expire.** 30-day retention is set on both workflows. For long-term preservation, pull + commit wiki pages promptly.
- **Free-tier limits.** GitHub Actions is free for public repos. Private repos have a monthly minute budget (currently 2,000 min/mo on the Free plan). A typical tracked-channel scan takes ~1-2 minutes.

## Related Pages

- [[tracked-channels-schema]] - Subscription file format
- [[queue-schema]] - One-shot queue format
- [[architecture]] - Full pipeline overview
- [[setup-guide]] - Running ingestion locally
- [[yolo-projects]] - Inspiration for the scheduled-scan pattern
- [[index]] - Main table of contents
