# CLAUDE.md — THE LAST TENANT (Project Constitution)

This file governs how work on this novel proceeds across sessions. Read this
file and everything in `bible/` and `registers/` before writing, editing, or
auditing any prose. If a future instruction conflicts with this file, prefer
the more recent entry in `DECISION_LOG.md` — it records deliberate changes of
course — over silently deviating from what's written here.

## What this project is

**THE LAST TENANT** is an original psychological/domestic suspense novel.
Working length target: ~95,000–105,000 words across three parts. This
repository is both the manuscript and the production system that keeps a
tightly-plotted mystery internally consistent across a long draft.

The premise, world, characters, and the true solution to the central mystery
are canon once locked in `bible/`. Nothing in this repo should contradict
`bible/` without a corresponding entry in `DECISION_LOG.md` explaining the
change and which downstream files were updated as a result.

## The Gate system

Foundational work is organized into six gates. A gate is "complete" when its
file exists, is internally consistent with every earlier gate, and has no
item marked `OPEN` in its own issues list. Drafting prose is only valid once
Gates 0–5 are complete for the part being drafted.

- **Gate 0 — Premise & Concept Lock** (`bible/00-premise.md`): logline,
  genre/comps, core reader promise, central dramatic question, themes.
- **Gate 1 — World & Setting Bible** (`bible/01-world-and-setting.md`): the
  city, the building, geography, physical rules of the setting, sensory
  palette.
- **Gate 2 — Character Bible** (`bible/02-characters.md`): every named
  character's profile, voice, wound, want, knowledge-state, and relationship
  map.
- **Gate 3 — Mystery Architecture** (`bible/03-mystery-architecture.md`):
  **CONFIDENTIAL.** The actual truth of what happened — culprit, method,
  motive, secret timeline — locked before a single clue is planted, plus the
  full clue map and fair-play check. This file is a production document, not
  reader-facing text. Nothing in it may appear in the manuscript ahead of the
  reveal schedule it defines.
- **Gate 4 — Structural Outline** (`bible/04-structural-outline.md`):
  part/act structure for the whole novel, chapter list per part with beat
  summaries.
- **Gate 5 — Chapter Briefs** (`bible/05-chapter-briefs-part-1.md`, and a new
  file per part as work reaches it): a locked brief per chapter — POV, scene
  list, goal, clues planted/reinforced/withheld, entry/exit state, prohibited
  revelations, target word count. Drafting a chapter without an approved
  brief is out of process.

## The registers (living documents — update every chapter)

Unlike the gates, these are **not static**. They are updated after every
chapter is drafted and audited, and are the source of truth an audit checks
prose against.

- `registers/character-register.md` — running state per character: what they
  know, where they are, physical/behavioral details established on the page.
- `registers/timeline-register.md` — two timelines: story-present (day-by-day
  as Nora experiences it) and the secret backstory timeline (Gate 3 events,
  dated, for internal consistency only).
- `registers/clue-register.md` — every clue: where planted, exact wording/
  form, what it truly points to, whether it's a red herring, when it's
  scheduled to pay off.
- `registers/continuity-register.md` — concrete, checkable facts: names,
  spellings, physical layout, objects, timestamps, weather, prices — anything
  a careful reader could catch as inconsistent.
- `registers/prohibited-revelations.md` — the standing list of facts that
  must not be confirmed on the page before their scheduled part/chapter, with
  a per-chapter sign-off that none leaked.
- `registers/voice-style-guide.md` — POV rules, tense, narrative distance,
  diction boundaries, recurring motifs.

## Per-chapter workflow

For each chapter, in order:

1. **Draft** prose against its Gate 5 brief.
2. **Critique** — an honest editorial pass on the draft: what's weak, what's
   flat, where the voice slips, where pacing sags or rushes.
3. **Revise** based on the critique.
4. **Run six audits** against the revised draft:
   - *Continuity* — checked against `continuity-register.md` and prior
     chapters.
   - *Clue* — checked against `clue-register.md`; confirms planted clues are
     fairly legible in hindsight and nothing was planted that contradicts
     Gate 3.
   - *Voice* — checked against `voice-style-guide.md` and the character's
     profile in `02-characters.md`.
   - *Pacing* — scene-by-scene beat check against the Gate 5 brief and
     surrounding chapters.
   - *Factual* — real-world claims (law, construction/surveying detail,
     geography, procedure) checked for plausibility and internal consistency.
   - *Prose* — line-level craft pass: cliché, repetition, rhythm, filtering
     words, overwriting.
5. **Update the registers** — character, timeline, clue, continuity — with
   whatever the chapter established.
6. **Update the manuscript word count** in `PROJECT_STATUS.md`.
7. **Confirm no prohibited revelation appeared early** — explicit sign-off
   line in `registers/prohibited-revelations.md` for that chapter.
8. Write the chapter's audit report to `reports/chapter-NN-audit.md`.

Do not batch multiple chapters through this pipeline at reduced depth. Each
chapter earns its own full pass.

## Repository map

```
CLAUDE.md                          this file
PROJECT_STATUS.md                  current state, word counts, gate status
NEXT_ACTION.md                     what the next session should do first
DECISION_LOG.md                    deliberate decisions and course changes
CHANGELOG.md                       dated log of what changed each session
bible/                             Gates 0-5, static once locked
  00-premise.md
  01-world-and-setting.md
  02-characters.md
  03-mystery-architecture.md       CONFIDENTIAL — solution, not reader-facing
  04-structural-outline.md
  05-chapter-briefs-part-1.md
registers/                         living documents, updated every chapter
manuscript/
  part-1/chapter-01.md ...         reader-facing prose only
reports/
  gate-verification.md
  chapter-NN-audit.md              per-chapter audit reports
  combined-ch1-4-audit.md          cross-chapter audit units
```

## Hard rules

- `bible/03-mystery-architecture.md` is confidential production material. Its
  contents (culprit, method, motive) never appear verbatim or by clear
  implication in `manuscript/` before the part/chapter Gate 3 schedules.
- Manuscript files contain reader-facing prose only — no editorial brackets,
  no TODOs, no author asides.
- Every register update is traceable to the chapter that caused it.
- Commit only after the unit of work being committed (a chapter, or a
  multi-chapter block if that's what was requested) is fully audited and
  coherent — not mid-draft.
- Do not invent named real people, brands, or real addresses; the city of
  Rookford and all businesses within it are invented (see
  `bible/01-world-and-setting.md`).
