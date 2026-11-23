"""Shared document layout for site pages and notes."""

import htmlkit as h

MENU_ICON = h.Raw("""<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24"
    viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
    stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
  <path d="M4 5h16" />
  <path d="M4 12h16" />
  <path d="M4 19h16" />
</svg>""")

HIGHLIGHT_URL = "https://unpkg.com/@highlightjs/cdn-assets@11.11.1"
HIGHLIGHT_ASSETS = h.Fragment(
    h.link(
        href=f"{HIGHLIGHT_URL}/styles/github.min.css",
        rel="stylesheet",
        media="(prefers-color-scheme: light)",
    ),
    h.link(
        href=f"{HIGHLIGHT_URL}/styles/github-dark.min.css",
        rel="stylesheet",
        media="(prefers-color-scheme: dark)",
    ),
    h.script(src=f"{HIGHLIGHT_URL}/highlight.min.js"),
    h.script(src=f"{HIGHLIGHT_URL}/languages/julia.min.js"),
)


def navigation(prefix: str) -> h.Element:
    """Build the menu with links relative to the current page."""
    return h.nav(
        h.button(
            MENU_ICON,
            class_="nav-toggle",
            type="button",
            aria_expanded="false",
            aria_controls="site-navigation",
            aria_label="Toggle navigation",
        ),
        h.ol(
            h.li(h.a("About", href="/")),
            [
                h.li(h.a(label, href=f"{prefix}{label.lower()}.html"))
                for label in ("Links", "Notes", "Publications", "Software", "Talks")
            ],
            id="site-navigation",
        ),
    )


def layout(content: h.Child, *, note: bool = False) -> h.Element:
    """Wrap content in the site layout, with syntax highlighting for notes."""
    prefix = "../" if note else ""
    return h.html(
        h.head(
            h.meta(charset="UTF-8"),
            h.meta(name="viewport", content="width=device-width, initial-scale=1"),
            h.title("Gavin Wiggins"),
            h.link(
                href=f"{prefix}feed.json",
                rel="alternate",
                type="application/feed+json",
                title="Gavin Wiggins",
            ),
            h.link(
                href=f"{prefix}rss.xml",
                rel="alternate",
                type="application/rss+xml",
                title="Gavin Wiggins",
            ),
            h.link(href=f"{prefix}styles.css", rel="stylesheet"),
            HIGHLIGHT_ASSETS if note else None,
        ),
        h.body(
            h.header(h.h1("Gavin Wiggins"), navigation(prefix or "./")),
            h.main(content),
            h.footer("© 2026 Gavin Wiggins"),
            h.script("hljs.highlightAll();") if note else None,
            h.script(src=f"{prefix}navigation.js"),
        ),
        lang="en",
    )
