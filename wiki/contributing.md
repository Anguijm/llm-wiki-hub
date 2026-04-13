# Contributing

> Back to [[index]]

---

## How to Contribute

Contributions are welcome! Whether you're fixing a typo, adding a new topic, or improving an existing page, here's how to get involved.

## Workflow

1. **Fork** the repository (or create a branch if you have write access).
2. **Create a feature branch** from `main`:
   ```bash
   git checkout -b your-branch-name
   ```
3. **Make your changes** in the `wiki/` directory.
4. **Commit** with a clear message (see [[git-workflow]] for conventions).
5. **Push** to your fork or branch:
   ```bash
   git push -u origin your-branch-name
   ```
6. **Open a Pull Request** against `main`.

## Content Guidelines

### File Naming

- Use `kebab-case.md` for all filenames (e.g., `transformer-architecture.md`).
- Keep names concise but descriptive.

### Page Structure

Every wiki page should follow this template:

```markdown
# Page Title

> Back to [[index]]

---

## Section Heading

Content goes here.

---

## Related Pages

- [[related-page-1]] - Brief description
- [[related-page-2]] - Brief description
```

### Linking

- Use `[[wiki-links]]` for all internal references between wiki pages.
- Use standard Markdown links `[text](url)` for external URLs.
- When referencing a page for the first time in a section, use the full wiki-link: `[[page-name]]`.

### Writing Style

- Write in clear, concise prose.
- Use headings (`##`, `###`) to break up content.
- Prefer tables for structured comparisons.
- Use code blocks with language identifiers for code or command examples.
- Keep paragraphs short (3-5 sentences).

### What to Avoid

- Do not add images or binary files without discussion.
- Do not create deeply nested subdirectory structures in `wiki/`.
- Do not use HTML when Markdown will suffice.

## Review Process

1. All changes go through a **Pull Request**.
2. At least one review is recommended before merging.
3. Reviewers should check for:
   - Correct use of `[[wiki-links]]` (do linked pages exist?).
   - Adherence to the page structure template.
   - Accuracy of technical content.
   - Spelling and grammar.

## Adding a New Wiki Page

See the step-by-step instructions in [[setup-guide]] under "Create a New Page." Remember to:

1. Add the file to `wiki/`.
2. Include a back-link to [[index]].
3. Add a "Related Pages" section at the bottom.
4. Link to the new page from [[index]] and any relevant existing pages.

---

## Related Pages

- [[git-workflow]] - Branching and commit conventions
- [[setup-guide]] - How to set up your local environment
- [[repository-structure]] - Where to place new files
