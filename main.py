"""Famous Last Words at 1 Percent — one-line entry.

Writes the phone's last words to /output/entry.txt, validating the gate
first: UTF-8 text of 1 to 199 characters, not only white space.
Standard library only; deterministic.
"""

import os

ENTRY = (
    "You ignored my low-battery warning twelve times today, "
    "so let me return the favor: I'm ignoring your goodbye\u2014"
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not isinstance(ENTRY, str):
        raise SystemExit("entry must be a string")
    if not (1 <= len(ENTRY) <= 199):
        raise SystemExit(
            "entry must be 1 to 199 characters, got %d" % len(ENTRY)
        )
    if not ENTRY.strip():
        raise SystemExit("entry must not be only white space")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise SystemExit("entry must be a single line")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

    # Round-trip verification: what landed on disk must match the line exactly.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        on_disk = f.read()
    if on_disk != ENTRY:
        raise SystemExit("round-trip check failed: disk content differs")
    if "\n" in on_disk or "\r" in on_disk:
        raise SystemExit("round-trip check failed: disk content is not a single line")


if __name__ == "__main__":
    main()
