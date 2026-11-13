"""Copy the bundled entry image to the grader's output directory.

Variant v2: "Red panda in autumn leaves" — a red panda rolling joyfully
on its back in a pile of golden autumn leaves, for make.fun ai-happy-01.

The entry image is a fixed JPEG shipped in this repository. This program
only copies its bytes, so the two grading runs produce identical output.
"""

import os
import shutil

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")


def main():
    if not os.path.isfile(SOURCE):
        raise FileNotFoundError("bundled entry image missing: " + SOURCE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(SOURCE, os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
