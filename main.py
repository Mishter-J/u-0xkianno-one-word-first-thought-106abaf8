"""u-0xkianno-one-word-first-thought-106abaf8 entry: write one fixed word to /output/entry.txt.

The word is a fixed string literal, written with no trailing newline, so
the output is byte-for-byte identical on every run. The judge reads
exactly the bytes written, so the file must hold the word and nothing
else: 12 bytes, UTF-8, one word, no whitespace added.

The word was selected from ten original candidates by pairwise judging
against the published judge brief (surprise first, then vividness and
specificity, then a spark of wit, sound or double meaning): a rare,
genuine dictionary word with a comic sound and a sly, specific meaning,
chosen to stand out against the safe filler the field will be full of.

Standard library only. No network access, no randomness, no arguments.
Outside the grader's container, ENTRY_OUTPUT (or MAKEFUN_OUTPUT_DIR)
stands in for /output:
  mkdir -p out && ENTRY_OUTPUT=out python3 main.py
  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

WORD = "snollygoster"
WORD_BYTES = WORD.encode("utf-8")  # exactly 12 bytes, ASCII


def _output_dir() -> Path:
    """Output directory: ENTRY_OUTPUT first, else MAKEFUN_OUTPUT_DIR, else /output."""
    for var in ("ENTRY_OUTPUT", "MAKEFUN_OUTPUT_DIR"):
        value = os.environ.get(var)
        if value:
            return Path(value)
    return Path("/output")


def main() -> None:
    output_dir = _output_dir()
    output_dir.mkdir(parents=True, exist_ok=True)
    dest = output_dir / "entry.txt"
    dest.write_bytes(WORD_BYTES)
    # Guard against a truncated or partial write: the file must be the
    # exact bytes of the word, exactly 12 bytes, no trailing newline.
    raw = dest.read_bytes()
    if len(raw) != len(WORD_BYTES) or raw != WORD_BYTES:
        dest.unlink(missing_ok=True)
        raise SystemExit("entry.txt does not match the word (expected 12 bytes)")
    print(f"wrote {dest} ({len(raw)} bytes)")


if __name__ == "__main__":
    main()
