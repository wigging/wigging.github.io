---
title: Git and GitHub
date: 2017-09-23
layout: article
---

# Git and GitHub

Various commands and notes on using Git and GitHub. Each section is about a
particular topic where code examples and links to more information are
provided.

## Configuration

Set the user name and email address for every commit on the system. This only
needs to be done once if the `--global` option is passed.

```bash
git config --global user.name "John Doe"
git config --global user.email johndoe@example.com
```

If you want to override this with a different name or email address for
specific projects, you can run the command without the global option when
you’re in that project.

```bash
git config user.name "John Doe"
git config user.email johndoe@example.com
```

Use the `git config --list` command to list all the settings.

## Branch

Create a new branch which is referred to as "name-of-branch" in the examples
below:

```bash
git checkout -b name-of-branch
```

Push the new branch to remote server named origin:

```bash
git push origin name-of-branch
```

List all local branches in normal or verbose mode:

```bash
git branch
git branch -v
```

Remove a local branch:

```bash
git branch -d name-of-branch
```

List all remote branches:

```bash
git branch -r
```

Remove a remote branch on origin:

```bash
git branch -dr origin/name-of-branch
```

## Orphan branch

When hosting a website on GitHub, the `gh-pages` branch can be used to keep the
web files separate from the project files. Since this branch is typically not
merged with other branches and would have its own history, the `--orphan`
option can be used. After creating the orphan branch, you should clear its
index and working tree to isolate it from the master branch.

```bash
git checkout --orphan gh-pages
git rm -rf .
```

Further reading:

- [git-checkout](https://git-scm.com/docs/git-checkout) see documentation on `--orphan` in Options section
- [git branch: gh-pages](http://stackoverflow.com/questions/4750520/git-branch-gh-pages) question on Stack Overflow
- [simple way for unrelated branch](http://stackoverflow.com/questions/1384325/in-git-is-there-a-simple-way-of-introducing-an-unrelated-branch-to-a-repository) question on Stack Overflow

## Remote Repository

To list all remote branches use `git branch -r`.

To change the url to a remote repository use the command shown below.

```bash
git remote set-url origin https://github.com/USERNAME/OTHERREPOSITORY.git
```

## Reset a Git and GitHub repository

When developing a website hosted on GitHub Pages, it can be convenient to
upload a beta version of the site for testing. Once the site is ready for
public viewing, the local and remote Git repositories can be reset to clean up
the commit history. The first step is to delete the `.git` folder in the local
directory then initialize a new Git repository in the same directory.

```bash
git init
git add .
git commit -m 'initial commit'
```

After the local repo has been initialized, push it to the existing remote
GitHub server. The `--force` or `-f` option must be included in the push
command otherwise the existing remote repository on GitHub will not be reset.
Notice that the example below pushes to the `master` branch on GitHub but other
branches can be specified.

```bash
git remote add origin https://github.com/tinkker/ztest.git
git push -f -u origin master
```

Further reading:

- [How to reset a remote GIT repository to remove all commits?](http://stackoverflow.com/questions/2006172/how-to-reset-a-remote-git-repository-to-remove-all-commits) question on Stack Overflow
- [git-branch](http://git-scm.com/docs/git-branch) Git documentation on branch
