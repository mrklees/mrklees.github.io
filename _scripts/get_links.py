#!/usr/bin/env python

import os
import sys
import urllib.parse

BASE_URL = "https://static.cloudygo.com/static/"

def make_links(url_path, paths):
    set_paths = set(paths)
    no_thumbnails = []

    for path in paths:
        url = os.path.join(BASE_URL, url_path, urllib.parse.quote(path))

        name, ext = os.path.splitext(path)
        ext = ext.lower()

        if ext in (".png", ".jpg"):
            print(f"![{name}]({url})")
        elif ext in (".mov",):
            print(f"""
<video controls>
  <source src="{url}">
  {name}
</video>
""")
        else:
            print(f"UNKNOWN EXTENSION: {ext!r}")

if __name__ == "__main__":
    assert len(sys.argv) == 2, sys.argv

    photo_dir = sys.argv[1]
    static_dir = "/Projects/Sites/static/" # will be under /home/<user>/
    assert static_dir in photo_dir
    url_path = photo_dir.split(static_dir)[1]

    paths = os.listdir(photo_dir)
    make_links(url_path, sorted(paths))
