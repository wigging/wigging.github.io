"""Content for the notes index."""

import htmlkit as h


def notes_index(notes: list[dict[str, str]]) -> h.Fragment:
    """Render the notes index from ordered Markdown metadata."""
    return h.Fragment(
        h.h2("Notes"),
        h.p(
            "This page contains my notes on various programming and tech related topics. "
            "Subscribe to the ",
            h.a("JSON feed", href="feed.json"),
            " or ",
            h.a("RSS feed", href="rss.xml"),
            ", or follow me on Mastodon to get notified about new posts.",
        ),
        [
            h.article(
                h.h4(h.a(note["title"], href=note["url"])),
                h.p(note["description"]),
                h.time(note["date_label"], datetime=note["date_published"]),
                class_="note",
            )
            for note in notes
        ],
    )
