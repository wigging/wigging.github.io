---
title: Zed Configuration
date: May 5, 2025
---

Zed is a modern text editor that is well suited for developers. Settings for macOS are shown below and are available via the Command+Comma keyboard shortcut.

```json
{
  "features": {
    "edit_prediction_provider": "none"
  },
  "theme": "Mariana",
  "base_keymap": "SublimeText",
  "telemetry": {
    "diagnostics": false,
    "metrics": false
  },
  "vim_mode": false,
  "ui_font_size": 15,
  "buffer_font_size": 13,
  "buffer_font_family": "Menlo",
  "buffer_line_height": "standard",
  "buffer_font_features": {
    "calt": false
  },
  "cursor_blink": false,
  "toolbar": {
    "breadcrumbs": false,
    "quick_actions": false
  },
  "restore_on_startup": "none",
  "git": {
    "inline_blame": { "enabled": false }
  },
  "languages": {
    "Python": {
      "language_servers": ["pyright", "ruff"],
      "format_on_save": "off",
      "formatter": [
        {
          "language_server": { "name": "ruff" }
        }
      ]
    }
  }
}
```
