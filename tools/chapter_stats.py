#!/usr/bin/env python3
"""
chapter_stats.py — Per-chapter craft stats for THE LAST TENANT.

For every chapter file under 07_manuscript/part_*/, reports word count,
paragraph count, average paragraph length, an estimated dialogue
percentage (rough heuristic: lines containing a quotation mark), and
average sentence length (rough heuristic: split on '. ', '! ', '? ').

These are approximations meant to flag chapters worth a closer pacing/
craft look (per 01_author_bible/style_audit_checklist.md and
04_plot/tension_curve.md / emotional_curve.md), not precise linguistic
analysis.

Usage:
    python3 tools/chapter_stats.py [chapter_file_or_glob ...]

With no arguments, scans every chapter across all three parts.
No third-party dependencies — standard library only.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MANUSCRIPT_DIR = REPO_ROOT / "07_manuscript"

_WORD_RE = re.compile(r"\S+")
_SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+")
_QUOTE_CHARS = ('"', "“", "”", "'")


def default_chapter_files() -> list[Path]:
    files: list[Path] = []
    for part in ("part_1", "part_2", "part_3"):
        part_dir = MANUSCRIPT_DIR / part
        if part_dir.is_dir():
            files.extend(
                p for p in sorted(part_dir.glob("*.md"))
                if p.name.lower() != "readme.md"
            )
    return files


def analyze(text: str) -> dict:
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()
                  and not p.strip().startswith("#")]
    words = _WORD_RE.findall(text)
    word_total = len(words)

    dialogue_paragraphs = sum(
        1 for p in paragraphs if any(q in p for q in _QUOTE_CHARS)
    )
    dialogue_pct = (
        100.0 * dialogue_paragraphs / len(paragraphs) if paragraphs else 0.0
    )

    sentences = [s for s in _SENTENCE_SPLIT_RE.split(text) if s.strip()]
    avg_sentence_len = (
        word_total / len(sentences) if sentences else 0.0
    )

    avg_paragraph_len = (
        word_total / len(paragraphs) if paragraphs else 0.0
    )

    return {
        "words": word_total,
        "paragraphs": len(paragraphs),
        "avg_paragraph_words": avg_paragraph_len,
        "dialogue_paragraph_pct": dialogue_pct,
        "avg_sentence_words": avg_sentence_len,
    }


def main(argv: list[str]) -> int:
    if argv:
        files = [Path(a) for a in argv]
    else:
        files = default_chapter_files()

    if not files:
        print("No chapter files found. Pass file paths explicitly, or "
              "draft chapters under 07_manuscript/part_*/ first.")
        return 0

    print(f"{'Chapter':30s} {'Words':>7s} {'Paras':>6s} "
          f"{'Avg¶':>6s} {'Dlg%':>6s} {'AvgSent':>8s}")
    print("-" * 70)
    for f in files:
        if not f.is_file():
            print(f"  (skipped, not found: {f})", file=sys.stderr)
            continue
        stats = analyze(f.read_text(encoding="utf-8"))
        print(
            f"{f.name:30s} {stats['words']:7,} {stats['paragraphs']:6,} "
            f"{stats['avg_paragraph_words']:6.1f} "
            f"{stats['dialogue_paragraph_pct']:5.1f}% "
            f"{stats['avg_sentence_words']:8.1f}"
        )

    print("\nHeuristic only — verify anything surprising by reading the "
          "chapter. See 01_author_bible/style_audit_checklist.md for the "
          "full manual audit this tool supplements, not replaces.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
