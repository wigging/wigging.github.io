---
title: Zsh Configuration
date: May 5, 2025
---

Zsh or z-shell is the default shell on macOS. The `.zshrc` file shown below uses coreutils, Sublime Text, and the Starship prompt. The zsh config file is located at `~/.zshrc`.

```bash
# Config file for zsh on macOS located at ~/.zshrc

# Coreutils aliases via Homebrew https://brew.sh
# Requires `brew install coreutils`
# ----------------------------------------------------------------------------

# List all files with directories first, ignores `.` and `..`
alias ls="gls --almost-all --group-directories-first --color"

# List all files line-by-line with directories first, ignores `.` and `..`
alias ll="gls -l --human-readable --almost-all --group-directories-first --color"

# Sublime Text editor https://www.sublimetext.com
# ----------------------------------------------------------------------------

# Open Sublime Text from command line
alias subl="/Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl"

# Zsh configuration
# ----------------------------------------------------------------------------

# Enable completion system
autoload -Uz compinit && compinit

# Enable color for `ls` output
export CLICOLOR=1

# Change directory without using `cd`
setopt AUTO_CD

# List files after changing directory
function chpwd() {
    emulate -L zsh
    ls
}

# Starship shell prompt https://starship.rs
# ----------------------------------------------------------------------------

eval "$(starship init zsh)"
```
