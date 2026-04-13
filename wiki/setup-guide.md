# Setup Guide

> Back to [[index]]

---

## Prerequisites

Before you begin, ensure you have the following installed:

- **Git** (version 2.x or later) - [Download Git](https://git-scm.com/downloads)
- A **text editor** or Markdown viewer of your choice

See [[dependencies]] for the full dependency map.

## Clone the Repository

```bash
git clone https://github.com/anguijm/llm-wiki-hub.git
cd llm-wiki-hub
```

## Browse the Wiki

### Option 1: GitHub Web UI

Navigate to the `wiki/` directory on GitHub. Start at [`wiki/index.md`](wiki/index.md) and follow the `[[wiki-links]]` by searching for the referenced filename.

### Option 2: Local Markdown Viewer

Open any `.md` file in your editor. Most modern editors (VS Code, IntelliJ, etc.) have built-in Markdown preview.

### Option 3: Obsidian (Recommended for Navigation)

[Obsidian](https://obsidian.md/) provides the best experience for browsing `[[wiki-link]]`-based content:

1. Download and install Obsidian.
2. Open Obsidian and select **"Open folder as vault."**
3. Navigate to the `wiki/` directory inside your cloned repository.
4. Click **Open**.
5. All `[[wiki-links]]` are now clickable. Use the **Graph View** (Ctrl/Cmd + G) to visualize the knowledge graph.

### Option 4: Foam (VS Code Extension)

[Foam](https://foambubble.github.io/foam/) is a VS Code extension that adds wiki-link support:

1. Install VS Code.
2. Install the **Foam** extension from the marketplace.
3. Open the repository folder in VS Code.
4. `[[wiki-links]]` become navigable via Ctrl/Cmd + Click.

## Edit Content

1. Open any `.md` file in the `wiki/` directory.
2. Edit using standard Markdown syntax.
3. Use `[[page-name]]` to link to other wiki pages (without the `.md` extension).
4. Save and commit your changes:

```bash
git add wiki/your-page.md
git commit -m "Add notes on [topic]"
git push
```

See [[contributing]] for guidelines on content style and review process.

## Create a New Page

1. Create a new `.md` file in the `wiki/` directory:

```bash
touch wiki/your-new-topic.md
```

2. Add a title and back-link at the top:

```markdown
# Your New Topic

> Back to [[index]]

---

Your content here.
```

3. Add a link to your new page from [[index]] or any relevant page using `[[your-new-topic]]`.
4. Commit and push.

## Optional: Static Site Generation

To render the wiki as a hosted website, you can use a static-site generator. For example, with **MkDocs**:

```bash
pip install mkdocs
mkdocs new .
# Configure mkdocs.yml to point to wiki/ as the docs directory
mkdocs serve
```

This is entirely optional. See [[architecture]] for more on the "no build step" design philosophy.

---

## Related Pages

- [[dependencies]] - Full list of required and optional tools
- [[contributing]] - How to submit changes
- [[repository-structure]] - Where to put new files
