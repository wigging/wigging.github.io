---
title: Git and GitHub
excerpt: Tips and tricks for working with Git and GitHub.
date: 2018-07-01
---

# Git and GitHub

Git is a great version control system that is the foundation of the online GitHub platform for sharing code. The sections below provide configuration settings and tips for working with these tools.

## Git configuration

Set the user name and email address for every commit with the "git config" command. The "git config --list" option will show the current configuration settings.

```bash
# Set system wide user name and email for git
git config --global user.name "John Doe"
git config --global user.email "johndoe@example.com"

# View configuration information
git config --list

# Set a different user name and email for the current repository
git config user.name "Jane Bane"
git config user.email "janedoe@example.com"
```

The "gitignore" file tells Git to not place certain types of files under version control. The file can be applied globally or just for a particular project. See the [gitignore.io](https://www.gitignore.io) online tool to easily create an ignore file.

```bash
git config --global core.excludesfile "~/.gitignore"
```

## GitHub settings

To keep your email private in your commits, GitHub offers a noreply email
address. On your GitHub profile, go to Settings then Emails to enable the
private email address feature.

## Branch

A branch is a set of code changes with a unique name. Each repository can have one or more branches.

```bash
# Create and checkout a new branch called name-of-branch
git checkout -b name-of-branch

# List all local branches in normal or verbose mode
git branch
git branch -v

# Remove a local branch
git branch -d name-of-branch

# Merge local branch to master then delete it
git checkout master
git merge name-of-branch
git branch -d name-of-branch

# Push the new branch to a remote server named origin
git push origin name-of-branch

# List all remote branches
git branch -r

# Remove a remote branch on origin
git branch -dr origin/name-of-branch
```

When hosting a website on GitHub, the "gh-pages" branch can be used to keep the
web files separate from the project files. Since this branch is typically not
merged with other branches and would have its own history, the orphan option can be used. After creating the orphan branch, you should clear its
index and working tree to isolate it from the master branch.

```bash
git checkout --orphan gh-pages
git rm -rf .
```

## Reset a Git and GitHub repository

When developing a website hosted on GitHub Pages, it can be convenient to
upload a beta version of the site for testing. Once the site is ready for
public viewing, the local and remote Git repositories can be reset to clean up
the commit history. The first step is to delete the git folder in the local
directory then initialize a new Git repository in the same directory.

```bash
git init
git add .
git commit -m 'initial commit'
```

After the local repo has been initialized, push it to the existing remote GitHub server. The force option must be included in the push command otherwise the existing remote repository on GitHub will not be reset. Notice that the example below pushes to the master branch on GitHub but other branches can be specified.

```bash
git remote add origin https://github.com/tinkker/ztest.git
git push -f -u origin master
```

Further reading about how to reset a repository: [How to reset a remote GIT repository to remove all commits?](http://stackoverflow.com/questions/2006172/how-to-reset-a-remote-git-repository-to-remove-all-commits) and [git-branch](http://git-scm.com/docs/git-branch).

## Sync a forked repository

The commands below will sync a forked local repository with the original
upstream repository. These notes are based on the Stack Overflow question 
[here](https://stackoverflow.com/questions/7244321/how-do-i-update-a-github-forked-repository). 

```bash
# In the local repository, add the remote for the original "upstream" repo:
git remote add upstream https://github.com/whoever/whatever.git

# Fetch all the branches of that remote:
git fetch upstream

# Make sure you're on the master branch in the local repo:
git checkout master

# Rewrite your master branch so that any commits of yours that aren't already
# in upstream/master are replayed on top of that other branch:
git rebase upstream/master

# Finally push up the changes to your own forked repo on GitHub:
git push
```
