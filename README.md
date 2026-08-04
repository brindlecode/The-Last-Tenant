# THE LAST TENANT

Adult psychological thriller / domestic suspense / mystery. Standalone
novel, contemporary New York City setting, ~92,000–96,000 words across
~46 chapters in three parts. Written in close third person past tense,
primarily through one point-of-view character, in native-level American
English.

> **After her estranged younger sister disappears, an insurance
> identity-fraud investigator moves into the sister's last known
> apartment. Every resident remembers the missing woman under a
> different name, profession, history, and personality, while official
> records insist the apartment has been vacant for twelve years.**

This repository is both the production system and, eventually, the
manuscript for this novel. It is not a general-purpose writing template —
it is the specific planning and drafting apparatus for this specific
book, built to keep a tightly-plotted mystery and a two-hander emotional
core (sisters who loved each other badly) internally consistent across a
long draft written in discrete sessions with no persistent memory between
them.

## Start here

- **If you're a human picking this up**: read `PROJECT_STATUS.md` for
  where things stand, then `02_novel_bible/master_premise.md` for the
  story itself.
- **If you're an AI session continuing this work**: read `CLAUDE.md`
  first. It is a constitution, not a suggestion — it governs how every
  session in this repository must behave, including this one.
- **Either way, `NEXT_ACTION.md` is the actual next step.** Don't infer
  one from the file tree.

## Current state

See `PROJECT_STATUS.md` for the authoritative, up-to-date answer. As of
this repository's founding commit: **Gate 0 (foundation) and Gate 1
(concept validation) are complete. No manuscript prose exists yet.**
Gates 2–5 (character, mystery, structure, and pre-draft red-team
validation) are seeded from the originating project brief but not yet
formally validated — see each relevant file's own status line before
treating anything beyond Gate 1 as locked.

## Why this repository looks like this

Most novel-writing doesn't need forty-file production systems. This one
does, deliberately, for two reasons specific to the book:

1. **The mystery only works if it's fair.** Seven residents each
   remember the missing woman differently, and every account has to
   contain genuine, non-contradictory evidence while still adding up to
   one coherent, inferable-but-not-obvious truth. That requires tracking
   six separate timelines (objective truth, what Mara knows, what the
   reader knows, Elena's operational history, the antagonist
   organization's response, and evidence provenance) and auditing every
   clue for fairness and redundancy before it's trusted. See
   `05_mystery/`.
2. **The emotional core has to survive the mystery machinery.** The book
   is a story about two sisters first and a thriller second — see
   `02_novel_bible/thematic_argument.md`. Plot systems this detailed can
   easily crowd out character work; the production workflow in
   `00_project/production_workflow.md` exists partly to force every
   chapter back through character truth, not just plot logic, before
   it's considered done.

## Repository map

See `CLAUDE.md`'s Repository Map section for the full annotated tree.
