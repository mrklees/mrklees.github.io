#!/usr/bin/env python

import os
import sys

BASE_URL = "https://static.cloudygo.com/static/"

GALLERY_HEADER = """\
---
permalink: /{}/
title: "{}"
layout: gallery

gallery:\
"""

GALLERY_ITEM = """
  - image_path: {}
    url: {}
    alt: "{}"
    title: ""\
""")

GALLERY_FOOTER = """
---
"""

def thumbnail_name(path):
    """
    Get the path of for the thumbail of path

    The nautilus script adds "_thumb" after the name but before the ext.
    """
    parts = os.path.splitext(path)
    return parts[0] + "_thumb" + parts[1]

def photos_to_gallery(gallery_name, url_path, paths):
    set_paths = set(paths)
    no_thumbnails = []

    output_file = "_pages/" + gallery_name.replace(".md", "") + ".md"
    with open(output_file, "w") as f:
        f.write(GALLERY_HEADER.format(
            gallery_name.lower(), gallery_name.title()))

        for path in paths:
            thumbnail = thmbnail_name(path)
            # thumbnail won't exist for videos, ...
            if thumbnail not in set_paths:
                no_thumbnails.append(path)
                continue

            thumbnail_url = os.path.join(BASE_URL, url_path, thumbnail)
            url = os.path.join(BASE_URL, url_path, path)

            f.write(GALLERY_ITEM.format(thumbnail_url, url, path))

        f.write(GALLERY_FOOTER)

    print("Saved to", gallery_name)
    print("Skipped", len(no_thumbnails), "items without thumbnails")
    for p in no_thumbnails:
        print("\t", p)



if __name__ == "__main__":
    assert len(sys.argv) == 3, sys.argv

    name = sys.argv[1]
    photo_dir = sys.argv[2]
    static_dir = "/Projects/Sites/static/" # will be under /home/<user>/
    assert static_dir in photo_dir
    url_path = photo_dir.split(static_dir)[1]

    paths = os.listdir(photo_dir)
    photos_to_gallery(name, url_path, paths)
