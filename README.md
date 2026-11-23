# Website

This repository contains my personal website <https://gavinw.me>. Pull requests are not accepted but Issues can be submitted regarding content on the website.

## Installation

Install uv using the instructions at <https://docs.astral.sh/uv/>.

## Build the website

Build the website along with its JSON and RSS feeds and XML sitemap using the `build.py` script. This will create a `dist/` directory in the project for all the generated website files. This is automatically done with the GitHub Actions workflow.

```bash
uv run src/build.py
```

Use the `--serve` option to serve the website locally from the `dist/` directory. This will automatically open the web browser to view the website.

```bash
uv run src/build.py --serve
```

## Project directories

The shared page layout and notes index are Python templates in `src/templates/`, built with [htmlkit](https://github.com/wigging/htmlkit). Other top-level page bodies are HTML in `src/page-content/`; notes are Markdown in `src/note-content/`. GitHub Pages serves the generated files from `dist/`.

## Add notes

Use the Markdown structure shown below to add a note to the website. Give a short description about the note at the top of the Markdown file along with the publication date and tags. The title of the note is the `##` element. All notes go in the `src/note-content` directory. Just commit the note and push up the changes to GitHub and the GitHub Actions workflow will automatically build the website.

```markdown
---
date: February 27, 2023
description: A brief description of the note goes here.
tags: tag1, tag2, tag3
---

## Note Title

The body of the note goes here after the title
```
