"""The Robot Apology — make.fun text bounty entry.

Writes a two-line robot confession to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Deterministic, Python standard library only. Self-verifies the entry
against the RULES.txt gate (UTF-8 text, 1-400 characters, not only
whitespace, exactly two lines, each a single sentence) before writing,
and re-verifies the file it wrote by reading it back and checking it
against the same rules. Exits non-zero on any failure.
"""

import os
import sys

ENTRY = (
    "I am sorry I watered your grandmother's orchid with the cold coffee "
    "I had already poured, and by morning its last bloom had folded shut.\n"
    "I have learned to read the label on the pot and the label on the cup "
    "before I pour anything, and from now on I will ask before watering a "
    "plant I did not plant."
)


def verify_entry(text):
    """Check one text against the RULES.txt gate.

    Returns a list of problems (empty means the text passes): UTF-8,
    1-400 characters, exactly two lines, each a single sentence ending
    in a period, neither whitespace-only, no carriage returns.
    """
    problems = []

    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        problems.append(f"entry is not valid UTF-8: {exc}")

    if not 1 <= len(text) <= 400:
        problems.append(
            f"entry is {len(text)} chars, must be 1-400"
        )

    lines = text.split("\n")
    if len(lines) != 2:
        problems.append(
            f"entry must be exactly 2 lines, found {len(lines)}"
        )
    else:
        for i, line in enumerate(lines, 1):
            if not line.strip():
                problems.append(f"line {i} must not be whitespace-only")
            if "\r" in line:
                problems.append(
                    f"line {i} must not contain a carriage return"
                )
            if line.count(".") != 1 or not line.rstrip().endswith("."):
                problems.append(
                    f"line {i} must be a single sentence ending in a period"
                )

    return problems


def report_problems(problems, where):
    """Print every problem found in one place, so a bad entry is fixed
    in a single pass instead of one failure per run."""
    for problem in problems:
        print(f"FAIL [{where}]: {problem}", file=sys.stderr)


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    output_path = os.path.join(output_dir, "entry.txt")

    # Self-verification, in memory: report ALL problems at once.
    problems = verify_entry(ENTRY)
    if problems:
        report_problems(problems, "entry")
        return 1

    os.makedirs(output_dir, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY + "\n")

    # Read-back: re-check the file on disk against the same rules, so a
    # write that mangled the text (encoding, newline, truncation) is
    # caught by the rules themselves, not only by string equality.
    with open(output_path, "r", encoding="utf-8") as fh:
        written = fh.read()
    problems = verify_entry(written.rstrip("\n"))
    if written != ENTRY + "\n":
        problems.append("written file does not match the entry")
    if problems:
        report_problems(problems, "written file")
        return 1

    print(f"OK: wrote {len(ENTRY)}-char, 2-line entry to {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
