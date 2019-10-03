---
title: Visual Studio Code
date: 2018-12-14
layout: note
---

My favorite extensions, theme, settings, and key bindings for working with
Python in [Visual Studio Code](https://code.visualstudio.com) on the Mac.

## Extensions and theme

For the Rewrap extension, word wrapping can be automatically enabled with
`Cmd+Shift+P` then select `Rewrap: Toggle Auto-Wrap`.

- LaTeX
- One Dark Pro
- Python
- reStructuredText
- Rewrap
- Vim

## Settings

User settings are in the `settings.json` file. This file can be edited with
`Cmd+Shift+P` then select `Preferences: Open Settings (JSON)`.

```json
{
    "editor.fontFamily": "Menlo",
    "editor.fontSize": 13,
    "editor.fontWeight": "bold",
    "editor.hover.enabled": false,
    "editor.lineHeight": 17,
    "editor.links": false,
    "editor.minimap.enabled": false,
    "editor.parameterHints.enabled": false,
    "editor.scrollBeyondLastLine": true,
    "files.exclude": {
        "**/.ipynb_checkpoints": true,
        "**/__pycache__": true,
        "**/.pytest_cache": true
    },
    "latex-workshop.latex.clean.enabled": true,
    "latex-workshop.view.pdf.viewer": "tab",
    "python.jediEnabled": false,
    "python.linting.enabled": true,
    "python.linting.flake8Enabled": true,
    "python.linting.flake8Args": ["--ignore=E302,E501,W605"],
    "python.linting.pylintEnabled": false,
    "restructuredtext.linter.extraArgs": ["--ignore D001"],
    "telemetry.enableCrashReporter": false,
    "telemetry.enableTelemetry": false,
    "terminal.explorerKind": "external",
    "terminal.external.osxExec": "iTerm.app",
    "terminal.integrated.fontSize": 13,
    "vim.insertModeKeyBindings": [
        {
            "before": ["j", "j"],
            "after": ["<Esc>"]
        }
    ],
    "workbench.colorTheme": "One Dark Pro",
    "workbench.iconTheme": "vs-minimal"
}
```

## Key bindings

Key bindings (keyboard shortcuts) go in the `keybindings.json` file.

```json
[
    {
        "key": "ctrl+tab",
        "command": "workbench.action.nextEditor"
    },
    {
        "key": "ctrl+`",
        "command": "workbench.action.focusActiveEditorGroup",
        "when": "terminalFocus"
    },
    {
        "key": "ctrl+`",
        "command": "workbench.action.terminal.focus",
        "when": "!terminalFocus"
    },
]
```
