"""Content for the notes index."""

from htmlkit import Fragment, a, article, h2, h4, p, time


def notes_index(notes: list[dict[str, str]]) -> Fragment:
    """Render the notes index from ordered Markdown metadata."""
    return Fragment(
        h2("Notes"),
        p(
            "This page contains my notes on various programming and tech related topics. "
            "Subscribe to the ",
            a("JSON feed", href="feed.json"),
            " or ",
            a("RSS feed", href="rss.xml"),
            ", or follow me on Mastodon to get notified about new posts.",
        ),
        [
            article(
                h4(a(note["title"], href=note["url"])),
                p(note["description"]),
                time(note["date_label"], datetime=note["date_published"]),
                class_="note",
            )
            for note in notes
        ],
    )
