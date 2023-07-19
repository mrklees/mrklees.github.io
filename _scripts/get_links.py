#!/usr/bin/env python

import os
import sys
import urllib.parse
from PIL import Image

BASE_URL = "https://static.cloudygo.com/static/"

def make_links(url_path, photo_dir, paths):
    set_paths = set(paths)
    no_thumbnails = []

    for path in paths:
        url = os.path.join(BASE_URL, url_path, urllib.parse.quote(path))

        name, ext = os.path.splitext(path)
        ext = ext.lower()

        if ext in (".png", ".jpg"):
            print(f"![{name}]({url})")
            with Image.open(os.path.join(photo_dir, path)) as im:
                h, w = im.size
                print(f"![{name}]({url}){{: style=\"flex: calc({h}/{w}); margin-right: 0.75em;\" }}")


        elif ext in (".mov", ".mp4"):
            print(f"""
<video controls>
  <source src="{url}">
  {name}
</video>
""")
        else:
            print(f"\nUNKNOWN EXTENSION: {ext!r}\n")

if __name__ == "__main__":
    assert len(sys.argv) == 2, sys.argv

    photo_dir = sys.argv[1]
    static_dir = "/Projects/Sites/static/" # will be under /home/<user>/
    assert static_dir in photo_dir
    url_path = photo_dir.split(static_dir)[1]

    paths = os.listdir(photo_dir)
    make_links(url_path, photo_dir, sorted(paths))
