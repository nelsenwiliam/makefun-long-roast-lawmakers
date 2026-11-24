#!/usr/bin/env python3
"""Long Roast entry: one satirical sentence, written to /output/entry.txt.

The bounty asks for a single satirical sentence (at most 320 characters)
roasting lawmakers who would regulate AI, crypto or the internet but cannot
convert a file to PDF. The sentence below is the whole entry: it sets up the
lawmakers' authority (writing the law to govern every AI model in America)
and undercuts it with the one file they cannot convert, landing the punch
on the last few words.

Pure standard library only; deterministic; no network, no input files.
"""

import os

ENTRY = (
    "The committee writing the law to govern every AI model in America "
    "keeps its briefing in a Word file the chairman tried to convert by "
    "renaming it .pdf \u2014 and, in his expert opinion, the rename counts "
    "as converting it."
)

MAX_CHARS = 320


def main() -> None:
    text = ENTRY.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(
            "entry must be 1-%d characters, got %d" % (MAX_CHARS, len(text))
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    print("wrote %s (%d characters)" % (path, len(text)))


if __name__ == "__main__":
    main()
