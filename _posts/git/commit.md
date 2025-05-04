---
title: Commit Changes with Git
date: April 17, 2025
---

Change last commit message.

```
git commit --amend -m 'New and correct message'
```

Return to previous commit and keep uncommitted changes.

```
git reset --soft HEAD~1
```

Return to previous commit and remove all uncommitted changes.

```
git reset --hard HEAD~1
```

Show files that were added, modified, or deleted for most recent commit.

```
git show --name-status
```
