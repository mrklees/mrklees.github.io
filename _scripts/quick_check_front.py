#!/usr/bin/env python

import os
import sys
import yaml

if __name__ == "__main__":
    assert len(sys.argv) == 2, sys.argv

    name = sys.argv[1]
    assert os.path.isfile(name), name

    with open(name) as f:
        d = f.readlines()

    front = "".join(d[:d.index("---\n", 1)])
    loaded = yaml.safe_load(front)
    assert loaded
    print(loaded)
