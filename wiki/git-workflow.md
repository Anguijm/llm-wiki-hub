# Git Workflow

> Back to [[index]]

---

## Branching Strategy

LLM Wiki Hub uses a simple **trunk-based** branching model:

```
main (stable, always deployable)
 ├── feature/topic-name     (new content or features)
 ├── fix/typo-correction    (small fixes)
 └── claude/task-description (automated/AI-assisted changes)
```

### Branch Types

| Prefix      | Purpose                              | Example                          |
| ----------- | ------------------------------------ | -------------------------------- |
| `feature/`  | New wiki pages or major additions    | `feature/add-rlhf-page`         |
| `fix/`      | Typo corrections, broken links       | `fix/architecture-typo`         |
| `claude/`   | AI-assisted content generation       | `claude/generate-codebase-docs`  |
| `refactor/` | Structural changes to existing pages | `refactor/reorganize-index`      |

### Rules

1. **`main`** is the stable branch. All changes are merged into `main` via Pull Request.
2. Feature branches are created from `main` and merged back into `main`.
3. Delete branches after merging to keep the branch list clean.

## Commit Conventions

Commit messages should be concise and descriptive. Use the following format:

```
<type>: <short summary>

<optional body with more detail>
```

### Types

| Type       | When to Use                                |
| ---------- | ------------------------------------------ |
| `add`      | New wiki page or section                   |
| `update`   | Improvements to existing content           |
| `fix`      | Typo, broken link, or factual correction   |
| `refactor` | Structural reorganization without new content |
| `docs`     | Changes to project documentation (non-wiki)|
| `chore`    | Maintenance tasks (e.g., CI, tooling)      |

### Examples

```bash
git commit -m "add: transformer architecture wiki page"
git commit -m "fix: broken link in architecture.md"
git commit -m "update: expand RLHF section with recent papers"
git commit -m "refactor: reorganize index into categories"
```

## Pull Request Process

1. Push your branch to the remote:
   ```bash
   git push -u origin feature/your-branch
   ```
2. Open a Pull Request on GitHub targeting `main`.
3. Add a brief description of what changed and why.
4. Request a review if collaborators are available.
5. After approval, merge via **Squash and Merge** to keep `main` history clean.
6. Delete the feature branch after merging.

## Conflict Resolution

If your branch has conflicts with `main`:

```bash
git fetch origin main
git rebase origin/main
# Resolve conflicts in your editor
git add .
git rebase --continue
git push --force-with-lease
```

Prefer `--force-with-lease` over `--force` to avoid overwriting others' work.

---

## Related Pages

- [[contributing]] - How to contribute content
- [[architecture]] - Design decisions behind the workflow
- [[index]] - Main table of contents
