"""Notify IndexNow about published MEMVEXA-by-MW site pages."""
import json
import os
import pathlib
import subprocess
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET

BASE = "https://memvexa-by-mw.github.io/memvexa-website/"
KEY_NAME = "917f903883035633d760a98f630727ccf2e2f7ec.txt"
KEY_URL = BASE + KEY_NAME
KEY = pathlib.Path(KEY_NAME).read_text(encoding="utf-8").strip()


def all_pages():
    root = ET.parse("sitemap.xml").getroot()
    return [element.text.strip() for element in root.findall(".//{*}loc")
            if element.text and element.text.strip().startswith(BASE)]


def changed_pages():
    event_type = os.getenv("GITHUB_EVENT_NAME", "")
    if event_type != "push":
        return all_pages()
    event = json.loads(pathlib.Path(os.environ["GITHUB_EVENT_PATH"]).read_text())
    before = event.get("before", "")
    if not before or set(before) == {"0"}:
        return all_pages()
    result = subprocess.run(["git", "diff", "--name-only", before, "HEAD"],
                            capture_output=True, text=True, check=False)
    if result.returncode:
        return all_pages()
    changes = set(result.stdout.splitlines())
    if changes & {"sitemap.xml", "scripts/notify_indexnow.py", ".github/workflows/indexnow.yml"}:
        return all_pages()
    known = set(all_pages())
    pages = set()
    for name in changes:
        if not name.endswith(".html") or name.startswith("."):
            continue
        url = BASE if name == "index.html" else BASE + name
        if url in known:
            pages.add(url)
    return sorted(pages)


def main():
    urls = list(dict.fromkeys(changed_pages()))
    if not urls:
        print("No sitemap-listed HTML pages changed; no IndexNow notification needed.")
        return

    # GitHub Pages may publish shortly after the repository commit.
    for attempt in range(20):
        try:
            with urllib.request.urlopen(KEY_URL, timeout=15) as response:
                content = response.read().decode("utf-8").strip()
            if content == KEY:
                break
        except (urllib.error.URLError, TimeoutError, UnicodeError):
            pass
        if attempt == 19:
            raise RuntimeError("Public IndexNow key could not be verified")
        time.sleep(15)

    # Give the GitHub Pages publication time to catch up with changed content.
    time.sleep(30)
    data = json.dumps({"host": "memvexa-by-mw.github.io", "key": KEY,
                       "keyLocation": KEY_URL, "urlList": urls}).encode("utf-8")
    request = urllib.request.Request("https://api.indexnow.org/indexnow", data=data,
        headers={"Content-Type": "application/json; charset=utf-8"}, method="POST")
    with urllib.request.urlopen(request, timeout=45) as response:
        status = response.status
    print(f"IndexNow submission: HTTP {status}, {len(urls)} URL(s).")
    print("Submission does not guarantee indexing. 202 means key verification pending.")


if __name__ == "__main__":
    main()
