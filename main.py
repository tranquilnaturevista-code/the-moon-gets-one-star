"""The Moon Gets One Star — entry program.

Writes one hand-written one-star review of the Moon to
``/output/entry.txt`` (or ``$OUTPUT_DIR/entry.txt``). The line is fixed:
the same review on every run, so the entry the judge reads is exactly
the line below.

Before writing, the program checks the line against the competition
gate — UTF-8 text of 1 to 120 characters, not only whitespace, all on
one line — and exits without writing anything if the gate fails. After
writing it reads the file back and checks the gate again on the text
actually on disk. The write is atomic (temp file + rename) so a crash
mid-write can never leave a half-written entry on disk. Deterministic:
no randomness, no network, no input files — the same line every run, so
the judged text is stable.
"""

import os
import sys
import tempfile

ENTRY = (
    "One star. Turned my dog into a werewolf with zero warning "
    "and now he howls at 3am. No refund offered."
)

GATE_MIN = 1
GATE_MAX = 120


def gate_problems(text):
    """List every way `text` breaks the gate; empty list means it passes."""
    problems = []
    if not text.strip():
        problems.append("entry is blank or only whitespace")
    if not GATE_MIN <= len(text) <= GATE_MAX:
        problems.append(
            "entry is %d characters, gate needs %d-%d"
            % (len(text), GATE_MIN, GATE_MAX)
        )
    if "\n" in text or "\r" in text:
        problems.append("entry must be a single line")
    return problems


def main():
    problems = gate_problems(ENTRY)
    if problems:
        for problem in problems:
            print("gate failed: %s" % problem, file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Atomic write: write to a temp file in the same directory, then
    # rename over the target, so a crash can never leave a partial entry.
    fd, tmp_path = tempfile.mkstemp(dir=out_dir, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(ENTRY)
        os.replace(tmp_path, path)
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise
    with open(path, encoding="utf-8") as f:
        written = f.read()
    problems = gate_problems(written)
    if problems or written != ENTRY:
        for problem in problems:
            print("verify failed: %s" % problem, file=sys.stderr)
        if written != ENTRY:
            print("verify failed: file content differs from ENTRY", file=sys.stderr)
        return 1
    print("wrote %d characters to %s" % (len(written), path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
