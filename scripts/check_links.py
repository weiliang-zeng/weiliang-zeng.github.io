#!/usr/bin/env python3
"""Check every external link in content/*.md for broken URLs.

Publications pages accumulate DOI/PDF links over more than a decade -- this
walks all Markdown content, extracts `[text](url)` links, and HEAD/GETs each
external one to flag anything that's gone dead (404, timeout, DNS failure).

Usage:
    uv run scripts/check_links.py
"""

import re
import sys
from pathlib import Path

import requests

CONTENT_DIR = Path(__file__).resolve().parent.parent / "content"
LINK_RE = re.compile(r"\[[^\]]+\]\((https?://[^)\s]+)\)")
TIMEOUT = 10
# Publisher sites (IEEE, Google Scholar, ...) often block the default
# python-requests user agent / no-UA requests with 403/418/429s that aren't
# real link rot -- a browser-like UA cuts down on those false positives.
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
    )
}


def find_links() -> dict[str, list[str]]:
    links: dict[str, list[str]] = {}
    for md_file in sorted(CONTENT_DIR.rglob("*.md")):
        urls = LINK_RE.findall(md_file.read_text(encoding="utf-8"))
        if urls:
            links[str(md_file.relative_to(CONTENT_DIR.parent))] = urls
    return links


def check(url: str) -> str:
    try:
        resp = requests.head(url, allow_redirects=True, timeout=TIMEOUT, headers=HEADERS)
        if resp.status_code >= 400:
            # Some servers don't support HEAD -- retry with GET before flagging.
            resp = requests.get(url, allow_redirects=True, timeout=TIMEOUT, headers=HEADERS)
        return "OK" if resp.status_code < 400 else f"HTTP {resp.status_code}"
    except requests.RequestException as exc:
        return f"FAILED ({exc.__class__.__name__})"


def main() -> int:
    links = find_links()
    total = sum(len(urls) for urls in links.values())
    print(f"Checking {total} links across {len(links)} file(s)...\n")

    broken = 0
    for file, urls in links.items():
        for url in urls:
            status = check(url)
            if status != "OK":
                broken += 1
                print(f"  BROKEN  {file}: {url}  -> {status}")

    print(f"\n{broken} broken link(s) out of {total}.")
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
