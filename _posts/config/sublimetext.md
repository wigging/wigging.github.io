---
title: Sublime Text Settings
date: May 4, 2025
---

Sublime Text is an excellent editor for writing code. It can be extended with various packages to support many programming languages. The sections below give general settings, key bindings, and LSP configuration on macOS.

## Preferences

In the menu select Sublime Text, Settings..., then Settings or press Command-Comma to edit the main settings (preferences) for Sublime Text.

```json
// Preferences.sublime-settings

{
    "color_scheme": "Mariana.sublime-color-scheme",
    "hot_exit": "disabled",
    "trim_trailing_white_space_on_save": "all",
    "ignored_packages":
    [
        "Vintage",
    ],
    "font_size": 13,
    "folder_exclude_patterns": [
        ".svn",
        ".git",
        ".hg",
        "CVS",
        "__pycache__"
    ],
    "translate_tabs_to_spaces": true,
    "update_check": true,
    "index_files": true,
    "scroll_past_end": 0.5,
}
```

## Key bindings

In the menu select Sublime Text, Settings..., then Key Bindings to define default macOS key bindings for Sublime Text.

```json
[
    { "keys": ["super+alt+q"], "command": "wrap_lines" , "args": {"width": 100} },
]
```

## LSP settings

Go to Sublime Text, Settings..., Package Settings, LSP, Servers, LSP-pyright to configure Pyright for Python in Sublime Text. These settings are ignored if they are defined in a `pyproject.toml` or `pyrightconfig.json` file. See the [Pyright docs] (https://microsoft.github.io/pyright) for more information about these settings.

```json
// LSP-pyright.sublime-settings

{
    "settings": {
        "pyright.disableOrganizeImports": true,
        "pyright.disableTaggedHints": true,
        "python.analysis.diagnosticSeverityOverrides": {
            "reportUndefinedVariable": false,
        }
    }
}

```

## Further reading

Visit [sublimetext.com](https://www.sublimetext.com) for more information about Sublime Text. See [LSP for Sublime Text](https://lsp.sublimetext.io) to learn more about LSP features and configuration.
