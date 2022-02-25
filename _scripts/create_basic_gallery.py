#!/usr/bin/env python

import os
import sys

BASE_URL = "https://static.cloudygo.com/static/"

def photos_to_gallery(gallery_name, url_path, paths):
    output_file = "_pages/" + gallery_name.replace(".md", "") + ".md"
    with open(output_file, "w") as f:
        f.write(f"""\
---
permalink: /{gallery_name}/
title: "{gallery_name.title()}"
layout: gallery

gallery:\
""")

        # XXX: consider filtering to jpg / png
        for path in paths:
            if "_thumb" in path: continue
            parts = os.path.splitext(path)
            thumbnail_path = parts[0] + "_thumb" + parts[1]
            thumbnail_url = os.path.join(BASE_URL, url_path, thumbnail_path)
            url = os.path.join(BASE_URL, url_path, path)

            f.write(f"""
  - image_path: {thumbnail_url}
    url: {url}
    alt: "{path}"
    title: ""\
""")

        f.write("""
---

{% include gallery caption="This is a sample gallery with **Markdown support**." %}
""")

    print("Saved to", gallery_name)


if __name__ == "__main__":
    assert len(sys.argv) == 3, sys.argv

    name = sys.argv[1]
    photo_dir = sys.argv[2]
    static_dir = "/Projects/Sites/static/" # will be under /home/<user>/
    assert static_dir in photo_dir
    url_path = photo_dir.split(static_dir)[1]

    paths = os.listdir(photo_dir)
    photos_to_gallery(name, url_path, paths)
