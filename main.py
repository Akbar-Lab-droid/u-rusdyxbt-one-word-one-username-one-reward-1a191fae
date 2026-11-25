"""Entry program for the make.fun bounty.

Copies the committed one-line entry text to the output directory
so the harness can read it as /output/entry.txt.
"""

import os
import shutil


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.txt")
    dst = os.path.join(out_dir, "entry.txt")
    shutil.copyfile(src, dst)


if __name__ == "__main__":
    main()
