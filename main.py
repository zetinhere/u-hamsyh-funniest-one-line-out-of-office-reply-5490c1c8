#!/usr/bin/env python3
"""Funniest One-Line Out-of-Office Reply — make.fun program/v1 entry.

Writes a single out-of-office auto-reply line to /output/entry.txt.

The line was chosen by a tournament: 24 original candidate lines were scored
against the judge's published brief (real OOO reply first, laugh on first
read, reads like a message a person would switch on, fresh turn on the usual
away message, short with every word earning its place). The top 8 were to go
to a pairwise proxy-judge tournament, but the 100milionseek proxy judge timed
out (>100 s per call, no response), so the pick fell back to the deterministic
rubric with the judge's own tie-break rule (first differing criterion decides
unless a later one differs by much more): four lines tied at 19/20; "Future Me"
won on criterion 3 (reads most like a real away message) over the two other
19-point finalists, and on criterion 2 over the fourth.

Deterministic: the same fixed line is written on every run, no randomness,
no network, no clock. Output is 1-160 chars of UTF-8 text, one line.
"""

import os
import stat
import sys

# The winning line (tournament winner; see NOTES in the entry folder).
LINE = "I'm out of the office until Monday. Your email has been forwarded to Future Me, who is already annoyed about it."

MAX_CHARS = 160


def main() -> int:
    line = LINE.strip()
    if not line or len(line) > MAX_CHARS or "\n" in line:
        print(f"entry line invalid: {len(line)} chars", file=sys.stderr)
        return 1
    os.umask(0o022)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    os.chmod(path, 0o644)
    # Sanity: read back exactly what was written.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == line + "\n", "round-trip mismatch"
    print(f"wrote {path} ({len(line)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
