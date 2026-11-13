"""ai-happy-01 entry: copy the image in this repo to /output/entry.png.

The image is a JPEG (the gate tells PNG and JPEG apart by their first
bytes, and the output name stays entry.png either way). Copying it
byte-for-byte makes the program deterministic: both runs write the
same bytes. Python 3.13, standard library only, no network.
"""

import hashlib
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "happy.jpg")
# The destination is always named entry.png, whatever the image bytes are.
DST = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.png")


def _sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)
    # Guard the determinism the entry promises: the output must be the
    # source image byte-for-byte, so a bad copy is a loud failure.
    if _sha256(DST) != _sha256(SRC):
        raise RuntimeError("entry.png does not match happy.jpg")


if __name__ == "__main__":
    main()
