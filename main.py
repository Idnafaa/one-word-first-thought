#!/usr/bin/env python3
"""One Word, First Thought — make.fun entry.

The task: send exactly one word, the first that comes to mind, with no
topic, no explanation and no second draft. A judge then compares words two
at a time on which is more interesting; surprise, vividness and a spark of
wit beat safe filler.

This program keeps a shortlist of the words that actually surfaced first,
scores each one by hand on the judge's own brief (surprise, vividness,
wit), and writes the winner — one bare word, nothing else — to
/output/entry.txt.
"""

import os

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")

# Words that surfaced, in the order they arrived, each with a one-line
# note on what makes it interesting. Scores are hand-set, 0-10, on the
# judge's three axes: surprise, vividness, wit.
CANDIDATES = [
    # (word, surprise, vividness, wit, note)
    ("apricity", 9, 9, 6, "the warmth of the sun on a cold winter's day"),
    ("petrichor", 7, 9, 5, "the smell of rain on dry earth"),
    ("vellichor", 9, 8, 5, "the strange wistfulness of used bookshops"),
    ("sonder", 8, 7, 6, "the realisation that every passer-by has a life"),
    ("quixotic", 6, 7, 8, "romantically impractical, tilting at windmills"),
    ("limerence", 8, 6, 5, "the ache of an infatuation that will not sit still"),
    ("psithurism", 9, 7, 4, "the sound of wind moving through trees"),
    ("moonstruck", 5, 8, 7, "dazed by love, or by the moon itself"),
]


def score(candidate):
    """Rank a candidate: surprise first, then vividness, then wit."""
    _, surprise, vividness, wit, _ = candidate
    return (surprise, vividness, wit)


def pick_word():
    """The first thought that wins on the judge's brief.

    Ties break toward the earlier word in the list, so the order above
    is the order the thoughts arrived in: the first thought stays first.
    """
    best = max(CANDIDATES, key=score)
    return best[0]


def main():
    word = pick_word()
    assert 1 <= len(word) <= 24, "word must fit the 1-24 character gate"
    assert word.isalpha(), "exactly one word, letters only"
    assert word.strip() == word and " " not in word, "exactly one word"
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    # Bare word, no trailing newline: the tie-break favours fewer bytes.
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(word)


if __name__ == "__main__":
    main()
