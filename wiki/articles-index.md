# Articles Index

> Back to [[index]]

**Chronological list of processed Medium articles, blog posts, and other long-form web content.**

---

## Processed Articles

_No articles processed yet. Add URLs to `queue.yml` under the `articles:` section and run `python scripts/ingest-article.py --from-queue` to fetch them. See [[queue-schema]] for full format._

<!--
Maintain this table as articles are processed. Format:

| Date | Title | Author | Tags | Wiki Page |
|---|---|---|---|---|
| 2026-04-15 | Yes you should understand backprop | Karpathy | llm, training | [[articles/karpathy-yes-you-should-understand-backprop]] |

-->

---

## How to Add an Article

1. Add the URL to `queue.yml` under `articles:`
2. Run `python scripts/ingest-article.py --from-queue`
3. The content lands in `active_sources/articles/<slug>/`
4. Ask Claude to summarize it into a wiki page in `wiki/articles/<slug>.md`
5. Claude will cross-link the new page to related pages and add an entry here

See [[setup-guide]] for the full workflow and [[queue-schema]] for queue format details.

---

## Related Pages

- [[videos-index]] - YouTube transcript pages
- [[queue-schema]] - How `queue.yml` is structured
- [[setup-guide]] - Ingest script usage
- [[index]] - Main table of contents
