---
title: Bash profile
date: 2018-08-19
layout: article
---

My current `.bash_profile` for the Mac.

```bash
# git completion and git prompt, requires Xcode to be installed
# see comments in the files for more details and the website at
# https://git-scm.com/book/en/v2/Appendix-A%3A-Git-in-Other-Environments-Git-in-Bash
source /Applications/Xcode.app/Contents/Developer/usr/share/git-core/git-completion.bash
source /Applications/Xcode.app/Contents/Developer/usr/share/git-core/git-prompt.sh

# git bash prompt
# see comments in the above bash and shell scripts for more options
export GIT_PS1_SHOWDIRTYSTATE=1
export GIT_PS1_SHOWUNTRACKEDFILES=1
export GIT_PS1_SHOWUPSTREAM="auto"
export PS1='\[\e[36m\]\W\[\e[m\]\[\033[32m\]$(__git_ps1 " (%s)")\[\033[00m\] \[\e[33m\]\$\[\e[m\] '

# format output of list command, the gls commands require: brew install coreutils
alias la="gls -Ahl --color --group-directories-first"
alias ll="gls -hl --color --group-directories-first"

# move up one directory
alias ..="cd .."

# call ls command after changing to another directory 
cd() { builtin cd "$@" && la; }

# added by Miniconda3 installer
export PATH="/Users/gavin/miniconda3/bin:$PATH"

# needed for sublime text symlink to subl
export PATH="$PATH":~/bin
```
