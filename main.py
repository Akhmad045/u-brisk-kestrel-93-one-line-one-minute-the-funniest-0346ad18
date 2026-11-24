"""One Line, One Minute: The Funniest AI Excuse.

Writes a single original one-line excuse to /output/entry.txt
(no trailing newline). Stdlib only, deterministic, no network.
"""

import os

ENTRY = "I didn't miss your deadline \u2014 I hallucinated a second one and hit that instead."

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def validate(text):
    """Gate: the entry must be a single non-blank line of 1-200 chars."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if text != text.strip():
        raise ValueError("entry has surrounding whitespace")
    if not text.strip():
        raise ValueError("entry is blank")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    text.encode("utf-8")  # must be valid UTF-8
    return text


def main():
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH) or ".", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
