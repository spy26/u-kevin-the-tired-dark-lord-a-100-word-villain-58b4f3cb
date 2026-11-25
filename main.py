#!/usr/bin/env python3
"""The Tired Dark Lord: A 100-Word Villain Monologue — entry program.

Writes one monologue (about 100 words) to /output/entry.txt, where the
sealed scorer reads it. Deterministic: fixed text, no randomness, no clock,
no network, no file reads outside this program.

Gate (from the kit's RULES.txt): /output/entry.txt must be UTF-8 text of
1 to 600 characters, not only white space. The brief also asks for about
100 words, so this program additionally requires 90-110 words and exits 1
if the text is outside either bound.
"""

import os
import sys

MONOLOGUE = (
    "Sign here, hero. And here. The moonlight tax is two coppers a beam, "
    "arrears back to the third age \u2014 I conquered the kingdom with "
    "paperwork, and paperwork, unlike swords, never sleeps. Neither, "
    "apparently, do I. Where is my seal? It was here. It is always here. "
    "Ah \u2014 in my other hand. The scheme is simple: own the night, rent "
    "it back by the hour, retire to a cottage with... with what? I had it a "
    "moment ago. A garden. Yes. A garden, and no more forms. Sign, then. Or "
    "don't. The moon has already paid, and frankly, so have I."
)

MIN_WORDS = 90
MAX_WORDS = 110
MIN_CHARS = 1
MAX_CHARS = 600


def gate(text):
    """Return an error string if text fails the gate, else None."""
    if not text or not text.strip():
        return "entry is empty or only white space"
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        return "entry is %d characters, outside %d-%d" % (
            len(text),
            MIN_CHARS,
            MAX_CHARS,
        )
    words = len(text.split())
    if not MIN_WORDS <= words <= MAX_WORDS:
        return "entry is %d words, outside %d-%d" % (
            words,
            MIN_WORDS,
            MAX_WORDS,
        )
    return None


def main():
    error = gate(MONOLOGUE)
    if error:
        print("gate failed: %s" % error, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(MONOLOGUE)
    print(
        "wrote %s (%d words, %d characters)"
        % (path, len(MONOLOGUE.split()), len(MONOLOGUE))
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
