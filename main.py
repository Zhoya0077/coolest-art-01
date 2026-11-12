#!/usr/bin/env python3
"""Copy the art in this repository to the output directory.

The image beside this file is the entry. The program writes it to
$MAKEFUN_OUTPUT_DIR/entry.png (or /output/entry.png inside the grader),
byte for byte, so two runs always produce identical bytes.
"""
import os
import shutil
from pathlib import Path  # entry.png holds JPEG bytes; format is told apart by magic bytes

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(HERE / "entry.png", OUT / "entry.png")


if __name__ == "__main__":
    main()
