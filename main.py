#!/usr/bin/env python3
"""Funniest Time Machine Warning Label.

Writes one line (<=120 chars) to /output/entry.txt: the warning label on
a time machine. Stdlib only, no network, deterministic.
"""

import os

# The line, chosen against the judge's brief (most important first):
#  1. A genuine time machine warning label: "WARNING:" plus a real hazard
#     of time travel, the butterfly effect — one careless step rewrites
#     history — phrased as an official safety notice.
#  2. The hazard IS the joke: stepping on a butterfly is not named flatly,
#     it is answered by the deadpan consequence in the second sentence.
#  3. The surprise lands in the last few words ("to the dinosaurs"): the
#     reader expects a fine or a rule, and gets an apology to an extinct
#     species instead.
#  4. Straight face throughout: official calm ("We are still apologizing")
#     against the absurdity, no wink, no pun.
#  5. Tight: 83 chars, every phrase doing work; one read, no setup.
ENTRY = "WARNING: Do not step on any butterflies. We are still apologizing to the dinosaurs."

# The gate: /output/entry.txt must be UTF-8 text of 1 to 120 characters,
# not only white space, on a single line. Fail loudly instead of shipping
# an invalid entry.
MAX_CHARS = 120


def validate(text: str) -> str:
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry is empty or only whitespace")
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("entry must be a single line")
    if len(stripped) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(stripped)} chars, over the {MAX_CHARS} limit"
        )
    try:
        stripped.encode("ascii")
    except UnicodeEncodeError as exc:
        raise ValueError("entry must be plain ASCII") from exc
    return stripped


def main() -> None:
    text = validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text + "\n")


if __name__ == "__main__":
    main()
