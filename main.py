"""One Emoji, One Smile entry.

Writes a single emoji to ``$MAKEFUN_OUTPUT_DIR/entry.txt``
(default ``/output``): the one emoji most likely to make a stranger
smile.

Draft pick: U+1F917 HUGGING FACE. A smiling face with open arms
offering a hug reads warm and friendly at first glance, needs no
context, and is universally understood.

Revised pick: U+1FAF6 HEART HANDS. Re-weighed against the judge's
brief, in order: the hug face offers a hug, and a hug from a
stranger is physically intimate, so it risks criterion 5 ("no
intimacy ... that would read oddly from a stranger"). Heart hands
carry the same warmth — two hands forming a heart, a gesture of
warmth and gratitude people send strangers all the time — with no
physical contact implied, so nothing reads oddly from a stranger.
It is also the more "chosen" pick (criterion 4): instantly readable
and universal (criteria 2-3), but clearly picked for the moment
rather than the first smiley that comes to mind. Same 4-byte size.

Python 3.13 standard library only; no network, no randomness, no input
files. Deterministic: every run writes the exact same bytes.
"""

import os

EMOJI = "\U0001FAF6"


def main() -> None:
    # The gate accepts UTF-8 text of 1 to 8 characters, not only white
    # space; refuse to write anything that would fail it. The entry is
    # exactly one emoji, no trailing newline, so the file holds nothing
    # but the emoji itself (4 bytes, the smallest possible text, which
    # also wins the byte-size tie-break).
    if not 1 <= len(EMOJI) <= 8 or not EMOJI.strip():
        raise ValueError("entry fails the gate: %r" % EMOJI)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
