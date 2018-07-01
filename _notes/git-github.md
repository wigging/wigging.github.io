---
title: Git and GitHub
excerpt: Tips and tricks for working with Git and GitHub.
date: 2017-12-07
---

# Git and GitHub

Tips on using Git and GitHub.

## Configuration

Set the user name and email address for every commit with the config command. The list option will show the current configuration settings on your system or for the particular project.

```bash
# Set system wide user name and email for git
git config --global user.name "John Doe"
git config --global user.email "johndoe@example.com"

# View configuration information
git config --list

# Set a different user name and email for a specific project
git config user.name "John Doe"
git config user.email "johndoe@example.com"
```

To keep your email private in your commits, GitHub offers a noreply email
address. On your GitHub profile, go to Settings then Emails to enable the
private email address feature.

You should also add a global ignore file. Use
[gitignore.io](https://www.gitignore.io) to create a file for macOS, vim,
python, and xcode. The contents of the ignore file will depend on your operating system and the applications you have installed. Place the file in
gitignore then tell Git to use it.

```bash
git config --global core.excludesfile "~/.gitignore"
```

## Branch

The commands below demonstrate working with branches in Git and GitHub; the branch is referred to as name-of-branch.

```bash
# Create and checkout a new branch 
git checkout -b name-of-branch

# Push the new branch to a remote server named origin
git push origin name-of-branch

# List all local branches in normal or verbose mode
git branch
git branch -v

# Remove a local branch
git branch -d name-of-branch

# List all remote branches
git branch -r

# Remove a remote branch on origin
git branch -dr origin/name-of-branch
```

## Orphan branch

When hosting a website on GitHub, the gh-pages branch can be used to keep the
web files separate from the project files. Since this branch is typically not
merged with other branches and would have its own history, the orphan option can be used. After creating the orphan branch, you should clear its
index and working tree to isolate it from the master branch.

```bash
git checkout --orphan gh-pages
git rm -rf .
```

Further reading about orphan branches: [git-checkout](https://git-scm.com/docs/git-checkout), [git branch gh-pages](http://stackoverflow.com/questions/4750520/git-branch-gh-pages), and [simple way for unrelated branch](http://stackoverflow.com/questions/1384325/in-git-is-there-a-simple-way-of-introducing-an-unrelated-branch-to-a-repository).

## Remote repository

Commands for working with remote repositories are shown below.

```bash
# List all remote branches
git branch -r

# Change url to remote repository
git remote set-url origin https://github.com/USERNAME/OTHERREPOSITORY.git
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
