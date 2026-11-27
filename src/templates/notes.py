"""Content for the notes index."""

from datetime import date

from htmlkit import Fragment, a, div, h2, h3, li, p, section, time, ul


def notes_index(notes: list[dict[str, str]]) -> Fragment:
    """Render the newest-first notes in sections by publication year."""
    rows_by_year = {}
    for note in notes:
        published = date.fromisoformat(note["date_published"])
        row = li(
            time(f"{published:%b} {published.day}", datetime=note["date_published"]),
            div(a(note["title"], href=note["url"]), p(note["description"])),
        )
        rows_by_year.setdefault(published.year, []).append(row)

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
            section(h3(str(year)), ul(rows), class_="note-year")
            for year, rows in rows_by_year.items()
        ],
    )
