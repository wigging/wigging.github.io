# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "htmlkit==26.11.1",
#     "livereload==2.7.1",
#     "markdown>=3.10.3",
# ]
# ///

"""Build the website and its feeds."""

import argparse
import json
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET
from datetime import UTC, date, datetime, time
from email.utils import format_datetime
from html import escape
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin

from htmlkit import Raw
from markdown import Markdown

from templates.layout import layout
from templates.notes import notes_index

SOURCE_DIR = Path("src")
DIST_DIR = Path("dist")

PAGES_DIR = SOURCE_DIR / "pages"
NOTES_DIR = SOURCE_DIR / "notes"
STATIC_DIR = SOURCE_DIR / "static"
ASSETS_DIR = SOURCE_DIR / "assets"
TALKS_DIR = SOURCE_DIR / "talks"

NOTE_OUTPUT_DIR = DIST_DIR / "notes"
NOTES_INDEX = DIST_DIR / "notes.html"

JSON_FEED_OUTPUT = DIST_DIR / "feed.json"
RSS_FEED_OUTPUT = DIST_DIR / "rss.xml"
SITEMAP_OUTPUT = DIST_DIR / "sitemap.xml"
ROBOTS_OUTPUT = DIST_DIR / "robots.txt"
BASE_URL = "https://gavinw.me/"

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 8000


class NoteTitleParser(HTMLParser):
    """Parse the first h2 title from a rendered note."""

    def __init__(self):
        """Initialize the parser and its title collection state."""
        super().__init__()
        self.title = None
        self.collecting = False
        self.text = []

    def handle_starttag(self, tag, attrs):
        """Start collecting the note title."""
        del attrs  # appease ty check warning for unused attrs
        if tag == "h2" and self.title is None:
            self.collecting = True
            self.text = []

    def handle_data(self, data):
        """Collect text from the note title."""
        if self.collecting:
            self.text.append(data)

    def handle_endtag(self, tag):
        """Finish collecting the note title."""
        if tag == "h2" and self.collecting:
            self.title = " ".join("".join(self.text).split())
            self.collecting = False
            self.text = []


def render_note(source_path):
    """Render a Markdown note and return its HTML and metadata."""
    source = source_path.read_text(encoding="utf-8")
    renderer = Markdown(extensions=["fenced_code", "meta"])
    body = renderer.convert(source).strip()

    required_fields = {"date", "description", "tags"}
    missing_fields = required_fields - renderer.Meta.keys()  # ty: ignore

    if missing_fields:
        missing = ", ".join(sorted(missing_fields))
        raise ValueError(f"Missing {missing} in {source_path}")

    metadata = {field: " ".join(renderer.Meta[field]) for field in required_fields}  # ty: ignore
    parser = NoteTitleParser()
    parser.feed(body)

    if parser.title is None:
        raise ValueError(f"Missing h2 title in {source_path}")

    metadata["title"] = parser.title
    metadata["date_label"] = metadata["date"]
    metadata["date_published"] = date.strptime(
        metadata["date"], "%B %d, %Y"
    ).isoformat()

    body = body.replace(
        "</h2>",
        f'</h2>\n<time datetime="{metadata["date_published"]}">'
        f"{escape(metadata['date_label'])}</time>",
        1,
    )

    return body, metadata


def write_page(output_path, content, *, note=False):
    """Write content inside the shared site layout."""
    page = layout(content, note=note)
    output_path.write_text(str(page) + "\n", encoding="utf-8")
    print(f"Built {output_path}")


def build_pages(source_directory, output_directory, *, note=False):
    """Build pages from HTML or Markdown and return metadata for the notes index."""
    output_directory.mkdir(parents=True, exist_ok=True)
    notes = []

    for source_path in sorted(source_directory.iterdir()):
        output_path = output_directory / source_path.with_suffix(".html").name
        if source_path.suffix == ".html":
            content = source_path.read_text(encoding="utf-8").strip()
        elif source_path.suffix == ".md":
            content, metadata = render_note(source_path)
            if note:
                metadata["url"] = output_path.relative_to(DIST_DIR).as_posix()
                notes.append(metadata)
        else:
            continue

        write_page(output_path, Raw(content), note=note)

    return notes


def get_feed_items(notes, base_url):
    """Convert ordered note metadata into JSON and RSS feed items."""
    items = []

    for note in notes:
        item_url = urljoin(base_url, note["url"])
        summary = " ".join(note["description"].split())
        items.append(
            {
                "id": item_url,
                "url": item_url,
                "title": note["title"],
                "summary": summary,
                "content_text": summary,
                "date_published": f"{note['date_published']}T00:00:00Z",
            }
        )

    return items


def generate_json_feed(items, output, base_url):
    """Write feed items to a JSON Feed 1.1 file."""
    feed = {
        "version": "https://jsonfeed.org/version/1.1",
        "title": "Gavin Wiggins",
        "home_page_url": urljoin(base_url, "notes.html"),
        "feed_url": urljoin(base_url, "feed.json"),
        "items": items,
    }

    output.write_text(json.dumps(feed, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(items)} item(s) to {output}")


def generate_rss_feed(items, output, base_url):
    """Write feed items to an RSS 2.0 file."""
    namespace = "http://www.w3.org/2005/Atom"
    ET.register_namespace("atom", namespace)
    rss = ET.Element("rss", version="2.0")
    channel = ET.SubElement(rss, "channel")
    ET.SubElement(channel, "title").text = "Gavin Wiggins"
    ET.SubElement(channel, "link").text = urljoin(base_url, "notes.html")
    ET.SubElement(
        channel, "description"
    ).text = "Notes on various programming and technology-related topics."
    ET.SubElement(
        channel,
        f"{{{namespace}}}link",
        href=urljoin(base_url, "rss.xml"),
        rel="self",
        type="application/rss+xml",
    )

    for feed_item in items:
        item = ET.SubElement(channel, "item")
        ET.SubElement(item, "title").text = feed_item["title"]
        ET.SubElement(item, "link").text = feed_item["url"]
        ET.SubElement(item, "guid", isPermaLink="true").text = feed_item["id"]
        ET.SubElement(item, "description").text = feed_item["summary"]
        published = datetime.combine(
            date.fromisoformat(feed_item["date_published"][:10]), time.min, UTC
        )
        ET.SubElement(item, "pubDate").text = format_datetime(published, usegmt=True)

    ET.indent(rss)
    xml = ET.tostring(rss, encoding="utf-8")
    output.write_bytes(b'<?xml version="1.0" encoding="utf-8"?>\n' + xml + b"\n")
    print(f"Wrote {len(items)} item(s) to {output}")


def generate_sitemap(directory, output, base_url):
    """Write the generated HTML page URLs to an XML sitemap."""
    namespace = "http://www.sitemaps.org/schemas/sitemap/0.9"
    ET.register_namespace("", namespace)
    urlset = ET.Element(f"{{{namespace}}}urlset")

    pages = sorted(directory.rglob("*.html"))

    for page in pages:
        relative_path = page.relative_to(directory).as_posix()
        location = (
            base_url
            if relative_path == "index.html"
            else urljoin(base_url, relative_path)
        )
        url = ET.SubElement(urlset, f"{{{namespace}}}url")
        ET.SubElement(url, f"{{{namespace}}}loc").text = location

    ET.indent(urlset)
    xml = ET.tostring(urlset, encoding="utf-8")
    output.write_bytes(b'<?xml version="1.0" encoding="utf-8"?>\n' + xml + b"\n")
    print(f"Wrote {len(pages)} URL(s) to {output}")


def generate_robots(output, base_url):
    """Write crawler rules and the sitemap location to robots.txt."""
    content = f"User-agent: *\nAllow: /\nSitemap: {urljoin(base_url, 'sitemap.xml')}\n"
    output.write_text(content, encoding="utf-8")
    print(f"Wrote crawler rules to {output}")


def build_site():
    """Build the complete website, feeds, and sitemap into the dist directory."""
    shutil.rmtree(DIST_DIR, ignore_errors=True)

    build_pages(PAGES_DIR, DIST_DIR)
    notes = build_pages(NOTES_DIR, NOTE_OUTPUT_DIR, note=True)
    notes.sort(key=lambda note: note["date_published"], reverse=True)
    write_page(NOTES_INDEX, notes_index(notes))

    shutil.copytree(STATIC_DIR, DIST_DIR, dirs_exist_ok=True)
    print(f"Copied static files to {DIST_DIR}")

    shutil.copytree(ASSETS_DIR, DIST_DIR / ASSETS_DIR.name)
    print(f"Copied assets to {DIST_DIR / ASSETS_DIR.name}")

    shutil.copytree(TALKS_DIR, DIST_DIR / TALKS_DIR.name)
    print(f"Copied talks to {DIST_DIR / TALKS_DIR.name}")

    items = get_feed_items(notes, BASE_URL)
    generate_json_feed(items, JSON_FEED_OUTPUT, BASE_URL)
    generate_rss_feed(items, RSS_FEED_OUTPUT, BASE_URL)
    generate_sitemap(DIST_DIR, SITEMAP_OUTPUT, BASE_URL)
    generate_robots(ROBOTS_OUTPUT, BASE_URL)


def serve():
    """Serve dist and reload the browser when a source file changes."""
    from livereload import Server
    from livereload.handlers import LiveReloadHandler

    def rebuild():
        """Run a fresh build so edits to imported templates take effect."""
        subprocess.run([sys.executable, __file__], check=True)

    # The default throttle drops refreshes for saves less than three seconds apart.
    LiveReloadHandler.DEFAULT_RELOAD_TIME = 0
    server = Server()
    server.watch(str(SOURCE_DIR), rebuild)
    server.serve(
        root=str(DIST_DIR),
        host=SERVER_HOST,
        port=SERVER_PORT,
        open_url_delay=0.5,
        live_css=False,
    )


def main():
    """Build the website and optionally serve it locally."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--serve", action="store_true", help="serve locally and live-reload on changes"
    )
    args = parser.parse_args()

    build_site()

    if args.serve:
        serve()


if __name__ == "__main__":
    main()
