# Changelog

All notable work on THE LAST TENANT (Mara/Elena canon), dated by
session.

## 2026-08-04

- **Rejected the prior Nora Hale/Cass Ferris material in full.** Built
  `claude/mara-elena-foundation` as a true orphan branch (no shared git
  history with `claude/last-tenant-part-one-ch1-4-nfwdvx`), confirming no
  `main` branch exists anywhere in this repository.
- Created the full approved repository structure: `00_project/` through
  `12_publishing/` plus `tools/`, 126 files total.
- Wrote `CLAUDE.md` — canon declaration (Mara/Elena is the only canon;
  the rejected branch's material is explicitly excluded, including
  structural/imagistic convergence, not just verbatim reuse) and process
  constitution.
- Wrote root files: `README.md`, `PROJECT_STATUS.md`, `NEXT_ACTION.md`,
  `DECISION_LOG.md`, `.gitignore`.
- **Closed Gate 0** (`00_project/`): project charter, quality gate
  definitions, production workflow, originality policy, definition of
  done, and a 21-item risk register spanning creative, plausibility,
  emotional, market, legal, and process risk categories.
- **Closed Gate 1** (`00_project/gate_1_concept_validation.md`):
  answered every required concept-validation question with reasoning;
  generated and compared 5 opening options, 4 ending architectures, 3
  Palinode origin stories, 3 Apartment 4C vacancy explanations, and 3
  Voss-family childhood-event versions, each with a reasoned working
  selection rather than a default choice.
- Populated `02_novel_bible/` (premise, themes, genre contract, setting,
  Bellwether House, Palinode, stakes/conflict/symbolism matrices,
  adaptation notes, sequel boundaries) and `01_author_bible/` (prose
  style, dialogue, banned clichés — including a project-specific list
  guarding against convergence with the rejected branch — narrative
  distance, style audit checklist) at Gate 1 depth.
- Built `03_characters/` in full: all 12 named characters (Mara, Elena,
  Julian Vale, Adrienne Shaw, Gabriel Knox, and the seven witnesses) plus
  a newly-invented investigative counterpart (Det. Teo Marchetti, no
  conventional romance by design), relationship/knowledge/arc matrices,
  and a supporting-cast list of not-yet-built roles. Caught and fixed a
  naming collision (Elena's "Nora Vale" alias, colliding with both Julian
  Vale's surname and the rejected branch's protagonist name, renamed to
  "Dana Kessler").
- Built `04_plot/` (synopses at three lengths, the two required Gate 1
  comparison documents, and explicitly-stubbed Gate 4 structural files)
  and seeded `05_mystery/` (six timelines, evidence provenance, clue/
  red-herring registers) with the source brief's twist architecture
  organized into the correct slots and explicitly marked draft.
- Caught and fixed two imagery near-misses during drafting that echoed
  the rejected branch's specific executed motifs (a buzzer-panel
  label-ghost detail; a loaded description landing in the antagonist's
  own home) — logged in `DECISION_LOG.md`.
- Scaffolded `06_chapter_briefs/` (empty, ready), `07_manuscript/`
  (structure only, no prose drafted), `08_continuity/` (10 living
  registers), `10_revision/`, `11_beta_readers/`, and `12_publishing/`
  (with real working content for title review, loglines, and elevator
  pitch, since those are Gate-1-appropriate).
- Populated `09_research/`: seeded `SOURCE_LOG.md` with two genuinely
  sourced findings (no mandatory missing-person-report waiting period,
  via NYC311; "synthetic identity fraud" as a real defined term, via a
  Federal Reserve-affiliated source), consolidated a 15-item
  `FACT_CHECK_QUEUE.md`, and wrote `LEGAL_RISK_NOTES.md`.
- Wrote and tested 5 dependency-free Python utilities in `tools/`:
  `word_count.py`, `chapter_stats.py`, `repeated_phrases.py`,
  `continuity_scan.py`, `assemble_manuscript.py` — all verified to run
  cleanly against the current (empty) manuscript state and, for the
  phrase/stats tools, against synthetic test input.
- Recorded five unresolved high-impact decisions awaiting human approval
  in `DECISION_LOG.md` (title uniqueness; the Voss family's original
  surname and father's fate; what happened to Elena; the ending's final
  lock; the no-romance default for Teo Marchetti).
- **No manuscript chapter was drafted**, per explicit instruction —
  `07_manuscript/` is structurally complete but contains no prose.
- Committed the complete Gate 0–1 foundation to
  `claude/mara-elena-foundation` and pushed.
