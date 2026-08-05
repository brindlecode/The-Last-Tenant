#!/usr/bin/env python3
"""
continuity_scan.py — Name-consistency scanner for A BORROWED NAME.

Reads the canonical name list out of 08_continuity/canonical_facts.md
("Names & spellings" section) and checks manuscript chapter files for
two things:

  1. Likely misspellings — a capitalized word/phrase in the manuscript
     that's close (small edit distance) to a canonical name but not an
     exact match.
  2. New proper nouns — capitalized words that appear repeatedly in the
     manuscript but aren't on the canonical list at all, which either
     need to be added to canonical_facts.md or are a misspelling of
     something that should have matched case 1.

This is a heuristic aid for the Continuity Audit step in
00_project/production_workflow.md, not a replacement for it — it will
produce false positives (ordinary capitalized words at sentence starts,
etc.) and should be read by a human, not trusted blindly.

Usage:
    python3 tools/continuity_scan.py

No third-party dependencies — standard library only (uses difflib).
"""

from __future__ import annotations

import difflib
import re
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CANONICAL_FACTS = REPO_ROOT / "08_continuity" / "canonical_facts.md"
MANUSCRIPT_DIR = REPO_ROOT / "07_manuscript"

_NAME_SECTION_RE = re.compile(
    r"## Names & spellings.*?\n(.*?)(?=\n## |\Z)", re.DOTALL
)
_BULLET_RE = re.compile(r"^-\s+(.*)$", re.MULTILINE)
# A canonical name entry may have parenthetical/explanatory text after
# it ("Mara Voss (never ... )") — only the leading name is extracted.
_LEADING_NAME_RE = re.compile(r"^\*{0,2}([A-Z][A-Za-z' .-]*[A-Za-z'.])\*{0,2}")

_CAP_PHRASE_RE = re.compile(
    r"\b([A-Z][a-z']+(?:\s+[A-Z][a-z']+){0,2})\b"
)

FUZZY_MAX_DISTANCE_RATIO = 0.82  # difflib SequenceMatcher ratio threshold


def load_canonical_names() -> list[str]:
    if not CANONICAL_FACTS.is_file():
        print(f"WARNING: {CANONICAL_FACTS} not found — nothing to check against.")
        return []
    text = CANONICAL_FACTS.read_text(encoding="utf-8")
    match = _NAME_SECTION_RE.search(text)
    if not match:
        print("WARNING: could not find a 'Names & spellings' section in "
              f"{CANONICAL_FACTS}.")
        return []
    names = []
    for bullet in _BULLET_RE.findall(match.group(1)):
        name_match = _LEADING_NAME_RE.match(bullet.strip())
        if name_match:
            names.append(name_match.group(1).strip())
    return names


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


def main() -> int:
    canonical = load_canonical_names()
    if canonical:
        print(f"Loaded {len(canonical)} canonical names from "
              f"{CANONICAL_FACTS.relative_to(REPO_ROOT)}:")
        print("  " + ", ".join(canonical))

    files = chapter_files()
    if not files:
        print("\nNo chapter files found — nothing to scan yet. "
              "Draft chapters under 07_manuscript/part_*/ first.")
        return 0

    found_phrases: Counter[str] = Counter()
    for f in files:
        text = f.read_text(encoding="utf-8")
        for m in _CAP_PHRASE_RE.finditer(text):
            found_phrases[m.group(1)] += 1

    canonical_set = set(canonical)
    print(f"\nScanned {len(files)} chapter file(s), "
          f"{len(found_phrases)} distinct capitalized phrase(s) found.\n")

    # 1. Likely misspellings of a canonical name.
    print("-- Possible misspellings of canonical names --")
    any_misspelling = False
    for phrase in found_phrases:
        if phrase in canonical_set:
            continue
        best = difflib.get_close_matches(
            phrase, canonical, n=1, cutoff=FUZZY_MAX_DISTANCE_RATIO
        )
        if best:
            any_misspelling = True
            print(f'  "{phrase}" (x{found_phrases[phrase]}) — close to '
                  f'canonical "{best[0]}"? Verify.')
    if not any_misspelling:
        print("  None found.")

    # 2. New proper nouns not yet in canonical_facts.md, seen 2+ times
    #    (a single occurrence is more likely an ordinary capitalized
    #    word than a new character/place name).
    print("\n-- Recurring capitalized phrases NOT in canonical_facts.md "
          "(2+ occurrences) --")
    any_new = False
    for phrase, count in found_phrases.most_common():
        if phrase in canonical_set or count < 2:
            continue
        if difflib.get_close_matches(
            phrase, canonical, n=1, cutoff=FUZZY_MAX_DISTANCE_RATIO
        ):
            continue  # already reported above as a likely misspelling
        any_new = True
        print(f'  "{phrase}" (x{count})')
    if not any_new:
        print("  None found.")

    print("\nHeuristic only — expect false positives (sentence-starting "
          "words, etc.). Read each hit; update canonical_facts.md for "
          "genuine new names, fix the prose for genuine misspellings.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
