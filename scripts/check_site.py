"""Check generated same-site links, fragments, and referenced assets."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

import yaml


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.ids = set()
        self.references = []
        self.feed(text)

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag == "a" and attrs.get("name"):
            self.ids.add(attrs["name"])
        for attribute in ("href", "src"):
            if attrs.get(attribute):
                self.references.append(attrs[attribute])


def main():
    root = Path(__file__).resolve().parents[1]
    config = yaml.safe_load((root / "mkdocs.yml").read_text(encoding="utf-8"))
    site = (root / config.get("site_dir", "site")).resolve()
    base = config["site_url"].rstrip("/") + "/"
    origin = urlsplit(base)
    prefix = unquote(origin.path)
    pages = {
        path: Page(path.read_text(encoding="utf-8"))
        for path in site.rglob("*.html")
    }
    if not pages:
        raise ValueError("No HTML pages found; run mkdocs build first")

    errors = []
    checked = 0
    for path, page in pages.items():
        relative = path.relative_to(site).as_posix()
        route = relative.removesuffix("index.html") if relative.endswith("index.html") else relative
        address = urljoin(base, route)
        for reference in page.references:
            target = urlsplit(urljoin(address, reference))
            if target.scheme not in ("http", "https") or target.netloc != origin.netloc:
                continue
            target_path = unquote(target.path)
            if not target_path.startswith(prefix):
                continue
            destination = (site / target_path[len(prefix):]).resolve()
            if not destination.is_relative_to(site):
                errors.append(f"{relative}: reference leaves site root: {reference}")
                continue
            if destination.is_dir():
                destination /= "index.html"
            if not destination.is_file():
                errors.append(f"{relative}: missing target: {reference}")
                continue
            checked += 1
            if target.fragment and destination.suffix == ".html":
                target_page = pages.get(destination)
                if target_page is None or unquote(target.fragment) not in target_page.ids:
                    errors.append(f"{relative}: missing fragment: {reference}")
    if errors:
        raise ValueError("Broken generated references:\n" + "\n".join(sorted(set(errors))))
    print(f"Verified {checked} local references across {len(pages)} HTML pages.")


if __name__ == "__main__":
    main()
