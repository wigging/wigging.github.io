"""Shared document layout for site pages and notes."""

from htmlkit import (
    Child,
    Element,
    Fragment,
    Raw,
    a,
    body,
    button,
    footer,
    h1,
    head,
    header,
    html,
    li,
    link,
    main,
    meta,
    nav,
    ol,
    script,
    title,
)

MENU_ICON = Raw("""<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24"
    viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
    stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
  <path d="M4 5h16" />
  <path d="M4 12h16" />
  <path d="M4 19h16" />
</svg>""")

HIGHLIGHT_URL = "https://unpkg.com/@highlightjs/cdn-assets@11.11.1"
HIGHLIGHT_ASSETS = Fragment(
    link(
        href=f"{HIGHLIGHT_URL}/styles/github.min.css",
        rel="stylesheet",
        media="(prefers-color-scheme: light)",
    ),
    link(
        href=f"{HIGHLIGHT_URL}/styles/github-dark.min.css",
        rel="stylesheet",
        media="(prefers-color-scheme: dark)",
    ),
    script(src=f"{HIGHLIGHT_URL}/highlight.min.js"),
    script(src=f"{HIGHLIGHT_URL}/languages/julia.min.js"),
)


def navigation(prefix: str) -> Element:
    """Build the menu with links relative to the current page."""
    return nav(
        button(
            MENU_ICON,
            class_="nav-toggle",
            type="button",
            aria_expanded="false",
            aria_controls="site-navigation",
            aria_label="Toggle navigation",
        ),
        ol(
            li(a("About", href="/")),
            [
                li(a(label, href=f"{prefix}{label.lower()}.html"))
                for label in ("Links", "Notes", "Publications", "Software", "Talks")
            ],
            id="site-navigation",
        ),
    )


def layout(content: Child, *, note: bool = False) -> Element:
    """Wrap content in the site layout, with syntax highlighting for notes."""
    prefix = "../" if note else ""
    return html(
        head(
            meta(charset="UTF-8"),
            meta(name="viewport", content="width=device-width, initial-scale=1"),
            title("Gavin Wiggins"),
            link(
                href=f"{prefix}feed.json",
                rel="alternate",
                type="application/feed+json",
                title="Gavin Wiggins",
            ),
            link(
                href=f"{prefix}rss.xml",
                rel="alternate",
                type="application/rss+xml",
                title="Gavin Wiggins",
            ),
            link(href=f"{prefix}styles.css", rel="stylesheet"),
            HIGHLIGHT_ASSETS if note else None,
        ),
        body(
            header(h1("Gavin Wiggins"), navigation(prefix or "./")),
            main(content),
            footer("© 2026 Gavin Wiggins"),
            script("hljs.highlightAll();") if note else None,
            script(src=f"{prefix}navigation.js"),
        ),
        lang="en",
    )
