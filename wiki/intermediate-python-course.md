# intermediate-python-course

> Back to [[index]]

**An intermediate Python course focused on building a dice-rolling program, delivered through GitHub issues.**

| Property | Value |
|---|---|
| Repository | [Anguijm/intermediate-python-course](https://github.com/Anguijm/intermediate-python-course) |
| Language | Python |
| Status | Stable |
| Created | 2021-06-22 |

---

## Overview

A lean, GitHub-native Python course where students clone the repository and implement a dice-rolling program. Course lessons are delivered through GitHub Issues rather than traditional documentation files, encouraging students to engage with version control while learning Python fundamentals.

## Architecture

```
intermediate-python-course/
├── README.md            Project introduction
└── dice_roller.py       Main project file (stub with main() + __main__ guard)
```

The course follows a GitHub-based learning model:

1. Students clone the repository
2. Work on `dice_roller.py`
3. Follow issue-based lessons in the GitHub Issues tab
4. Progressively build out dice-rolling functionality

## Key Design Decisions

- **Zero dependencies** - Pure Python standard library only. No `requirements.txt` or `setup.py`.
- **GitHub Issues as curriculum** - Lessons live in the Issues tab, not in markdown files. Encourages students to engage with GitHub as a platform.
- **Minimal boilerplate** - Single `dice_roller.py` with proper `__main__` guard pattern demonstrates Python module best practices.
- **Snake case naming** - File was renamed from `dice-roller.py` to `dice_roller.py` during development, modeling Python naming conventions.
- **Low barrier to entry** - No build step, no virtual environment, no package manager. Clone and start coding.

## Dependencies

None. Pure Python standard library.

---

## Related Pages

- [[index]] - All projects
