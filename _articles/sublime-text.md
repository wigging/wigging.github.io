---
title: Sublime Text 3
date: 2019-02-13
category: notes
tags: [software]
layout: article
---

# Sublime Text 3

Various settings, key bindings, and packages for using Sublime Text 3 on the Mac.

## Preferences

Below are my preferred user settings for Sublime Text 3. The settings file can be accessed with `⌘,` or from the application menu `Sublime Text -> Preferences -> Settings`.

```json
{
    "color_scheme": "Packages/Color Scheme - Default/Mariana.sublime-color-scheme",
    "draw_white_space": "none",
    "folder_exclude_patterns":
    [
        ".git",
        "__pycache__"
    ],
    "font_face": "Menlo",
    "font_size": 13,
    "hot_exit": false,
    "ignored_packages": [],
    "theme": "Adaptive.sublime-theme",
    "translate_tabs_to_spaces": true,
    "trim_trailing_white_space_on_save": true,
    "word_wrap": false,
    "wrap_width": 80
}
```

## Vim key bindings

The key bindings shown below are for exiting Vim insert mode in Sublime Text. These settings are accessed from the menu `Sublime Text -> Preferences -> Key Bindings`.

```json
[
    {
        "keys": ["j", "j"],
        "command": "exit_insert_mode",
        "context": [
            { "key": "setting.command_mode", "operand": false },
            { "key": "setting.is_widget", "operand": false}
        ]
    },
]
```

## Markdown.sublime-settings

Open a markdown file in the editor then access settings from application menu `Sublime Text -> Preferences -> Settings - Syntax Specific`.

```json
{
    "color_scheme": "Packages/Color Scheme - Default/Mariana.tmTheme",
    "extensions":
    [
        "md",
        "mdown"
    ],
    "word_wrap": true,
}
```

## LaTeXTools package

Settings located in the application menu `Sublime Text -> Preferences -> Package Settings -> LaTeXTools -> Settings - User`.

```json
{
    "hide_build_panel": "no_warnings",
    "viewer": "preview",
}
```

## SideBarEnhancements package

These settings are for the SideBarEnhancements plugin. The settings are available in the menu at `Sublime Text -> Preferences -> Package Settings -> Side Bar - > Settings`.

```json
{
    "close_affected_buffers_when_deleting_even_if_dirty": true,
}
```

## SublimeLinter package

Settings for the flake8 Python linter which can be accessed in the menu at `Sublime Text -> Preferences -> Package Settings -> SublimeLinter -> Settings`.

```json
{
    "gutter_theme": "Default",
    "linters": {
        "flake8": {
            "args": ["--ignore=E501,W605"]
        }
    }
}
```
