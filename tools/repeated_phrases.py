#!/usr/bin/env python3
"""
repeated_phrases.py — Cross-chapter repetition finder for A BORROWED NAME.

Scans chapter files for repeated multi-word phrases (n-grams), both
within a single chapter and across chapters, and reports any phrase
that recurs often enough to be worth a manual check against
01_author_bible/banned_cliches.md and voice-consistency notes.

This is a blunt instrument — a real motif documented deliberately (the
kind 01_author_bible/prose_style_guide.md permits) will also show up
here. The tool's job is to surface candidates for a human (or a
combined-audit review, per 00_project/production_workflow.md) to judge,
the same way the equivalent manual `grep` passes were run during this
project's sibling drafting sessions — not to make the call itself.

Usage:
    python3 tools/repeated_phrases.py [--n 5] [--min-count 3]

No third-party dependencies — standard library only.
"""

from __future__ import annotations

import argparse
import re
from collections import Counter, defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MANUSCRIPT_DIR = REPO_ROOT / "07_manuscript"

_WORD_RE = re.compile(r"[A-Za-z']+")

# Common function words are NOT filtered out here on purpose — a phrase
# like "she made herself" is exactly the kind of repeated construction
# worth catching, and filtering stopwords would hide it.
STOP_PHRASES_IGNORE = set()  # reserved for future manual exclusions


def chapter_files() -> list[Path]:
    files: list[Path] = []
    for part in ("part_1", "part_2", "part_3"):
        part_dir = MANUSCRIPT_DIR / part
        if part_dir.is_dir():
            files.extend(
                p for p in sorted(part_dir.glob("*.md"))
                if p.name.lower() != "readme.md"
            )
    return files


def ngrams(words: list[str], n: int):
    for i in range(len(words) - n + 1):
        yield tuple(words[i : i + n])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n", type=int, default=5,
                         help="phrase length in words (default: 5)")
    parser.add_argument("--min-count", type=int, default=3,
                         help="minimum total occurrences to report (default: 3)")
    parser.add_argument("files", nargs="*",
                         help="specific chapter files (default: all chapters)")
    args = parser.parse_args()

    files = [Path(f) for f in args.files] if args.files else chapter_files()
    files = [f for f in files if f.is_file()]

    if not files:
        print("No chapter files found. Draft chapters under "
              "07_manuscript/part_*/ first, or pass file paths explicitly.")
        return 0

    phrase_counts: Counter[tuple[str, ...]] = Counter()
    phrase_locations: dict[tuple[str, ...], set[str]] = defaultdict(set)

    for f in files:
        lower_words = [w.lower() for w in _WORD_RE.findall(f.read_text(encoding="utf-8"))]
        for gram in ngrams(lower_words, args.n):
            phrase_counts[gram] += 1
            phrase_locations[gram].add(f.name)

    hits = [
        (gram, count) for gram, count in phrase_counts.items()
        if count >= args.min_count
    ]
    hits.sort(key=lambda item: item[1], reverse=True)

    if not hits:
        print(f"No {args.n}-word phrase repeated {args.min_count}+ times "
              f"across {len(files)} chapter file(s). Nothing to report "
              f"(try a lower --min-count or shorter --n for a broader sweep).")
        return 0

    print(f"Phrases of length {args.n} repeated {args.min_count}+ times "
          f"across {len(files)} chapter file(s):\n")
    for gram, count in hits:
        chapters = ", ".join(sorted(phrase_locations[gram]))
        cross_chapter = len(phrase_locations[gram]) > 1
        flag = "CROSS-CHAPTER" if cross_chapter else "within one chapter"
        print(f'  [{flag:19s}] {count:3d}x  "{" ".join(gram)}"  ({chapters})')

    print("\nCheck each hit against 01_author_bible/voice-consistency "
          "notes and banned_cliches.md — a documented, deliberate motif "
          "is fine; an undocumented one should be varied or logged.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
