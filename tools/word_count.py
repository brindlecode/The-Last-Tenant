#!/usr/bin/env python3
"""
word_count.py — Word counts for THE LAST TENANT manuscript.

Walks 07_manuscript/part_1, part_2, part_3 for chapter files (*.md,
excluding README.md), counts words per chapter and per part, and
compares the running total against the project's target length from
00_project/project_charter.md (~92,000-96,000 words).

Usage:
    python3 tools/word_count.py

No third-party dependencies — standard library only.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MANUSCRIPT_DIR = REPO_ROOT / "07_manuscript"
PARTS = [
    ("part_1", "Part I — The Vacant Apartment", (22_000, 25_000)),
    ("part_2", "Part II — Seven Lives", (43_000, 48_000)),
    ("part_3", "Part III — The First Tenant", (22_000, 26_000)),
]
TARGET_TOTAL = (92_000, 96_000)

# Markdown heading markers, blockquote markers, and horizontal rules are
# stripped before counting so structural markup doesn't inflate the count.
_MD_NOISE_RE = re.compile(r"^(#{1,6}\s*|>\s?|-{3,}\s*$)", re.MULTILINE)
_WORD_RE = re.compile(r"\S+")


def word_count(text: str) -> int:
    """Count words in prose text, stripping simple Markdown structural noise."""
    cleaned = _MD_NOISE_RE.sub("", text)
    return len(_WORD_RE.findall(cleaned))


def chapter_files(part_dir: Path) -> list[Path]:
    if not part_dir.is_dir():
        return []
    files = [
        p
        for p in part_dir.glob("*.md")
        if p.name.lower() != "readme.md"
    ]
    return sorted(files)


def main() -> int:
    grand_total = 0
    print("THE LAST TENANT — word count report\n" + "=" * 40)

    if not MANUSCRIPT_DIR.is_dir():
        print(f"No manuscript directory found at {MANUSCRIPT_DIR}", file=sys.stderr)
        return 1

    any_chapters = False
    for slug, title, (lo, hi) in PARTS:
        part_dir = MANUSCRIPT_DIR / slug
        files = chapter_files(part_dir)
        part_total = 0
        print(f"\n{title}  (target {lo:,}-{hi:,} words)")
        if not files:
            print("  (no chapters drafted yet)")
            continue
        any_chapters = True
        for f in files:
            wc = word_count(f.read_text(encoding="utf-8"))
            part_total += wc
            print(f"  {f.name:30s} {wc:6,} words")
        status = "OK" if lo <= part_total <= hi else (
            "under target" if part_total < lo else "over target"
        )
        print(f"  {'-' * 38}")
        print(f"  {'PART TOTAL':30s} {part_total:6,} words  [{status}]")
        grand_total += part_total

    print("\n" + "=" * 40)
    print(f"MANUSCRIPT TOTAL: {grand_total:,} words")
    lo, hi = TARGET_TOTAL
    if not any_chapters:
        print("No chapters drafted yet — see NEXT_ACTION.md.")
    elif grand_total < lo:
        print(f"{lo - grand_total:,} words below the low end of the "
              f"{lo:,}-{hi:,} target range.")
    elif grand_total > hi:
        print(f"{grand_total - hi:,} words above the high end of the "
              f"{lo:,}-{hi:,} target range.")
    else:
        print(f"Within the {lo:,}-{hi:,} target range.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
