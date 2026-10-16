# Apply Leash Bio's 'train on exhaust, get sociology not physics' warning to audit any ML training pipeline for label leakage from human behavior patterns

> Back to [[experiments-index]]

Source: **[From Wet Lab to RL Env: 10,000 Drug-Discovery Campaigns in a Weekend — Ian Quigley, Leash Bio](https://www.youtube.com/watch?v=hQSBJVreLms)** · ls · 2026-10-15

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we audit any ML training dataset for implicit human behavioral signatures (e.g., chemist style, author fingerprints, curation bias) before training a model to predict ground-truth properties, then we avoid the failure mode where the model learns sociological patterns instead of physical ones, because Leash demonstrated a classifier achieving 60% top-5 accuracy predicting which of 1,815 chemists made a molecule — meaning chemical activity models trained on published data may be predicting chemist intent rather than binding affinity.

## What they did

Ian Quigley described Leash Bio's discovery that ML models trained on Chembl (the largest public chemical activity repository) may be learning chemist identity rather than chemistry. They trained a classifier on all molecules from chemists with 30+ papers and 600+ molecules, representing molecules as vectors of probability over 1,815 chemist identities rather than chemical formulas, and achieved 60% top-5 accuracy predicting which chemist made a molecule from its structure alone. When they used this sociological representation to predict activity, it performed as well as using chemical formulas — suggesting the activity model is learning sociology. The warning: when training on 'exhaust' (published data filtered by human judgment and interest), you may be in trouble because the data is pre-selected by human intent, not ground truth.

## Relevance to YOLO loop

medium: the 'training on exhaust' anti-pattern is a useful mental model for any ML pipeline in an agent harness that uses human-curated training data.

## Notes

Highly domain-specific (drug discovery / DNA-encoded libraries). The 'training on exhaust' concept is the only broadly transferable insight. Card kept because the mental model is genuinely useful for any ML pipeline audit.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-15 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `ls-2026-10-15-leash-bio-dell-ml-pipeline` |
| Channel | ls |
| Video | [From Wet Lab to RL Env: 10,000 Drug-Discovery Campaigns in a Weekend — Ian Quigley, Leash Bio](https://www.youtube.com/watch?v=hQSBJVreLms) |
| Published | 2026-10-15 |
| Ingested upstream | 2026-10-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
