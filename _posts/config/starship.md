---
title: Starship Prompt Configuration
date: May 5, 2025
---

The Starship prompt is a modern shell prompt with git support. On macOS, the configuration file is located at `~/.config/starship.toml`.

```toml
# Configuration file for Starship terminal prompt
# See the Starship website for more info https://starship.rs
# Some of the git_status symbols use the UTF code from https://www.nerdfonts.com/cheat-sheet

format = """
$username\
$hostname\
$directory\
$git_branch\
$git_state\
$git_status\
$cmd_duration\
$line_break\
$python\
$conda\
$character"""

[directory]
style = "blue"
truncate_to_repo = false
truncation_length = 0

[character]
success_symbol = "[❯](purple)"
error_symbol = "[❯](red)"
vimcmd_symbol = "[❮](green)"

[git_branch]
format = "[$branch]($style)"
style = "bright-black"

[git_status]
format = "[[( $all_status)](218) ($ahead_behind$stashed )]($style)"
style = "cyan"
conflicted = "≠"
modified = "*"
renamed = "*"
ahead = "\uf062"
behind = "\uf063"
diverged = "\uf063 \uf062"
stashed = "≡"

[git_state]
format = '\([$state( $progress_current/$progress_total)]($style)\) '
style = "bright-black"

[cmd_duration]
format = "[$duration]($style)"
style = "yellow"

[python]
format = "[($virtualenv )]($style)"
style = "bright-black"

[conda]
format = "[($environment )]($style)"
style = "bright-black"
```
