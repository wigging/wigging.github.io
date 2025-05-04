---
title: Undo Changes with Git
date: April 17, 2025
---

Undo an accidental git pull.

```
git reset --keep HEAD@{1}
```

Undo changes to all local uncommitted files.

```
git restore .
```