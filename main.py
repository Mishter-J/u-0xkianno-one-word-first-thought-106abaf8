"""u-0xkianno-one-word-first-thought-106abaf8 entry: write one fixed word to /output/entry.txt.

The word is a fixed string literal. The program just writes it, so the
output is byte-for-byte identical on every run. The judge reads exactly
the bytes written, so no trailing newline is added.

The word was selected from ten original candidates by pairwise judging
against the published judge brief (surprise first, then vividness and
specificity, then a spark of wit, sound or double meaning): a rare,
genuine dictionary word with a comic sound and a sly, specific meaning,
chosen to stand out against the safe filler the field will be full of.

Standard library only. No network access, no randomness, no arguments.
Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

WORD = "snollygoster"


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    dest = output_dir / "entry.txt"
    dest.write_text(WORD, encoding="utf-8")
    # Guard against a truncated or partial write: the file must be the
    # exact bytes of the word.
    if dest.read_text(encoding="utf-8") != WORD:
        dest.unlink(missing_ok=True)
        raise SystemExit("entry.txt does not match the word")
    print(f"wrote {dest} ({dest.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
