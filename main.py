"""The Robot Apology — make.fun text bounty entry.

Writes a two-line robot confession to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Deterministic, Python standard library only. Self-verifies the entry:
UTF-8 text, 1-400 characters total, exactly two lines, each a single
sentence, neither whitespace-only. Exits non-zero on any failure.
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


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    output_path = os.path.join(output_dir, "entry.txt")

    # Self-verification: UTF-8, 1-400 chars, exactly two lines, each a
    # single sentence, neither whitespace-only.
    try:
        ENTRY.encode("utf-8")
    except UnicodeEncodeError as exc:
        print(f"FAIL: entry is not valid UTF-8: {exc}", file=sys.stderr)
        return 1

    if not 1 <= len(ENTRY) <= 400:
        print(f"FAIL: entry is {len(ENTRY)} chars, must be 1-400", file=sys.stderr)
        return 1

    lines = ENTRY.split("\n")
    if len(lines) != 2:
        print(f"FAIL: entry must be exactly 2 lines, found {len(lines)}", file=sys.stderr)
        return 1

    for i, line in enumerate(lines, 1):
        if not line.strip():
            print(f"FAIL: line {i} must not be whitespace-only", file=sys.stderr)
            return 1
        if "\r" in line:
            print(f"FAIL: line {i} must not contain a carriage return", file=sys.stderr)
            return 1
        if line.count(".") != 1 or not line.rstrip().endswith("."):
            print(
                f"FAIL: line {i} must be a single sentence ending in a period",
                file=sys.stderr,
            )
            return 1

    os.makedirs(output_dir, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY + "\n")

    # Re-read and confirm the written file matches exactly.
    with open(output_path, "r", encoding="utf-8") as fh:
        written = fh.read()
    if written != ENTRY + "\n":
        print("FAIL: written file does not match the entry", file=sys.stderr)
        return 1

    print(f"OK: wrote {len(ENTRY)}-char, 2-line entry to {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
