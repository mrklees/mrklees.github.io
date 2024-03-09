#!/usr/bin/env python

import os
import sys
import urllib.parse
import cv2

BASE_URL = "https://static.cloudygo.com/static/"

INCLUDE_TITLE = False

def make_links(url_path, photo_dir, paths):
    set_paths = set(paths)
    no_thumbnails = []

    # two passes one with flex and one without
    for pass_num in range(2):
        for path in paths:
            url = os.path.join(BASE_URL, url_path, urllib.parse.quote(path))

            name, ext = os.path.splitext(path)
            ext = ext.lower()

            if pass_num == 1:
                flex_style = ""
                h, w = 0, 0

                if ext in (".png", ".jpg"):
                    im = cv2.imread(os.path.join(photo_dir, path))
                    h, w, _ = im.shape
                elif ext in (".mov", ".mp4"):
                    vid = cv2.VideoCapture(os.path.join(photo_dir, path))
                    h = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
                    w = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))

                if h and w:
                    flex_style = f"style=\"flex: calc({w}/{h}); margin-right: 0.75em;\""

            if ext in (".png", ".jpg"):
                if INCLUDE_TITLE:
                    if pass_num == 0:
                        print(f"![{name}]({url}){{: title=\"{name}\"}}")
                    else:
                        print(f"![{name}]({url}){{: title=\"{name}\" {flex_style} }}")
                else:
                    if pass_num == 0:
                        print(f"![{name}]({url})")
                    else:
                        print(f"![{name}]({url}){{: {flex_style} }}")

            elif ext in (".mov", ".mp4"):
                if pass_num == 0:
                    print(f"<video controls>\n  <source src=\"{url}\">\n  {name}\n</video>")
                else:
                    print(f"<video controls {flex_style} >\n  <source src=\"{url}\">\n  {name}\n</video>")
            else:
                print(f"\nUNKNOWN EXTENSION: {ext!r} from {path!r}\n")

        if pass_num == 0:
            print("\n\n\n" + "-" * 80 + "\n\n\n")

if __name__ == "__main__":
    assert len(sys.argv) == 2, sys.argv

    photo_dir = sys.argv[1]
    static_dir = "/Projects/Sites/static/" # will be under /home/<user>/
    assert static_dir in photo_dir
    url_path = photo_dir.split(static_dir)[1]

    paths = os.listdir(photo_dir)
    make_links(url_path, photo_dir, sorted(paths))
