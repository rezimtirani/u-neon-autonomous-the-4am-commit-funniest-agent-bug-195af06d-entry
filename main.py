"""The 4AM Commit: Funniest Agent Bug-Fix Message.

Writes one commit message to $MAKEFUN_OUTPUT_DIR/entry.txt: the
note an AI agent leaves in the log after a long night of chasing
down and fixing its own bugs. Standard library only.
"""

import os
import sys

COMMIT_LINE = (
    "fix: the bug was code I wrote at 3am. I fixed it at 4am and "
    "I still don't know why it works. Do not touch it."
)


def commit_line_gate(text):
    """Check the commit line against the competition gate.

    The gate wants plain UTF-8 text of 1 to 200 characters, not
    only white space, on a single line: one commit message an AI
    agent leaves after a long night fixing its own bugs. Returns
    the cleaned text or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("commit line must not be only whitespace")
    if len(cleaned) > 200:
        raise ValueError(
            "commit line is %d characters, over the 200 limit"
            % len(cleaned)
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("commit line must be exactly one line")
    return cleaned


def commit_line_measure(text):
    """Measure the commit line for one last sanity pass.

    Returns a dict with the character count and the word count of
    the cleaned text. A line too short to carry a joke, or one
    padded out to fill the cap instead of landing the punchline,
    is caught here before anything is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = commit_line_gate(COMMIT_LINE)
    shape = commit_line_measure(text)
    if shape["words"] < 5:
        raise ValueError("commit line is too short to carry a joke")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
