# CLAUDE.md — A BORROWED NAME (Project Constitution)

*(Working title changed from "THE LAST TENANT" during the Gate 2/3
session, after a twenty-candidate comparison found a collision with this
repository's own rejected branch and a stronger alternative — see
`DECISION_LOG.md` and `12_publishing/title_review.md`. Every other
reference to "THE LAST TENANT" below is retained where it names the
project's git-branch-era history accurately; the working title itself is
now A BORROWED NAME throughout the rest of the repository.)*

Read this file in full before doing anything else in this repository —
planning, research, drafting, or editing. If you are a future session
(including a future instance of the assistant that wrote this file), you
have no memory of the conversation that produced it. This file, and the
rest of the repository, is the entire record of what has been decided.
Chat memory is not canon. If it isn't written down here, it hasn't been
decided.

## Canon declaration — read this first

**This repository contains exactly one canonical version of A BORROWED
NAME** (working title; retired former working title "THE LAST TENANT" —
see above). It concerns Mara Voss, a senior identity-fraud investigator,
her missing younger sister Elena Voss, an apartment building in Brooklyn
called Bellwether House, and a private identity-engineering network
called the Palinode Continuity Group. This is the **only** approved
story. Everything under `02_novel_bible/`, `03_characters/`,
`04_plot/`, and `05_mystery/` in this repository defines it.

**A prior branch of this repository (`claude/last-tenant-part-one-ch1-4-nfwdvx`,
not an ancestor of this branch) contains a different, rejected novel**
involving a character named Nora Hale, a missing woman named Cass Ferris,
a landlord named Julian Cole, a caretaker named Desmond Pye, a city
called Rookford, and a converted mill called Sovereign Mill. **That
material is not canon.** Do not port, reference, paraphrase, or
"remix" any character, setting, plot mechanism, mystery solution, clue,
scene, or line of prose from that branch into this one, even by
coincidence of convenience (e.g., reusing "a caretaker who says more than
he means to" as a character beat, or "a building that hides something in
its own walls" as a central image, would both be derivative reuse and
are excluded on the same grounds as verbatim copying). This branch's
git history does not include that branch's commits — it was created as
an orphan branch specifically so there is nothing to accidentally
inherit. If a future session finds itself drifting toward structural or
imagistic similarity with that rejected material, stop and re-read
`00_project/originality_policy.md`.

## What this project is

**A BORROWED NAME** — adult psychological thriller / domestic suspense /
mystery. Contemporary setting (present-day New York City). Standalone
novel with limited-series adaptation potential (a market positioning
note, not a promise — see `00_project/originality_policy.md` on
overclaiming). Target: ~92,000–96,000 words, ~46 chapters, three parts.
Close third person past tense, primarily Mara Voss's POV
(~85–95%), native-level American English.

Full premise, themes, cast, setting, and the confidential mystery
solution live in `02_novel_bible/`, `03_characters/`, and `05_mystery/`.
Nothing in this file overrides those documents; this file only governs
*process*.

## Session discipline (non-negotiable)

1. **No chapter drafting until Gates 0–5 are complete and documented.**
   This repository, as of the session that created it, has completed
   Gate 0 and Gate 1 only. Check `PROJECT_STATUS.md` for current gate
   status before writing a single word of manuscript prose.
2. **Every future session starts by reading, in order**:
   `PROJECT_STATUS.md` → `NEXT_ACTION.md` → `DECISION_LOG.md` → whichever
   canonical files `NEXT_ACTION.md` points to. Do not start work — do
   not even resume what looks like an obvious next step — without this
   sequence. `NEXT_ACTION.md` exists precisely because "obvious next
   steps" inferred from file names are frequently wrong.
3. **No major fact may be invented during drafting without a canonical
   update.** If a chapter needs a fact that isn't already decided in
   `02_novel_bible/`, `03_characters/`, `05_mystery/`, or
   `08_continuity/`, stop, decide it deliberately, write it into the
   correct canonical file, and only then use it in prose. Prose is
   downstream of canon, never the other way around.
4. **No future session may rely on chat memory.** Anything a
   conversation established that matters must be written to a file
   before that conversation ends. An undocumented decision does not
   exist for the next session's purposes.
5. **All mystery reveals must follow the reveal schedule** defined once
   Gate 3 is complete (`05_mystery/reveal_ladder.md`). Nothing in
   `05_mystery/` may appear, verbatim or by clear implication, in
   manuscript prose ahead of its scheduled chapter.
6. **All research uncertainties must be logged** in
   `09_research/FACT_CHECK_QUEUE.md`, not silently guessed past. See
   `09_research/RESEARCH_INDEX.md` for the standing method.
7. **Every chapter, once drafting begins, follows**: draft → critique →
   revise → audit → register update, in that order, one chapter at a
   time, at full depth — no batching multiple chapters through at
   reduced depth. The full mechanics live in
   `00_project/production_workflow.md`.
8. **Do not overclaim.** Nothing in this repository may assert or imply
   that this novel is guaranteed commercial success, bestseller status,
   an award, or a produced adaptation. "Adaptation potential" is a
   positioning note about the material's shape, not a promise of outcome.

## The gate system

Full detail in `00_project/quality_gates.md`. Summary:

- **Gate 0 — Foundation**: repository structure, project charter,
  production workflow, originality policy, definition of done, risk
  register. (`00_project/`)
- **Gate 1 — Concept validation**: the premise, hook, and cast justify a
  full novel; the title and central mechanism are stress-tested; opening
  and ending architectures are generated and compared; the highest-risk
  worldbuilding questions (Palinode's origin, why Apartment 4C reads as
  vacant, the Voss family's childhood event) have multiple compared
  answers and a reasoned working selection. Record:
  `00_project/gate_1_concept_validation.md`.
- **Gate 2 — Character validation**: every recurring character fully
  built against the template in
  `03_characters/character_index.md`, stress-tested for
  stereotype risk, scene utility, and indispensability.
- **Gate 3 — Mystery validation**: all six timelines
  (`05_mystery/`), the full clue register, red-herring register, reveal
  ladder, and a fairness audit confirming the solution is inferable
  before the climax but not obvious.
- **Gate 4 — Structure validation**: act structure, chapter map, scene
  inventory, tension/emotional curves, subplot map, and a locked opening
  and ending.
- **Gate 5 — Pre-draft red-team validation**: an adversarial pass across
  Gates 1–4 looking specifically for plausibility failures, fairness
  failures, and originality failures before any chapter brief is
  written.

Gate 0 and Gate 1 are complete as of this repository's founding commit
on this branch — see `00_project/gate_1_concept_validation.md` for the
record, including what was compared and why the working selections were
made. **Gates 2–5 are not yet complete.** Do not treat character files,
mystery timelines, or plot structure documents in this repository as
locked canon merely because they exist — many were seeded from the
original project brief and are marked `STATUS: DRAFT — pending Gate N`
specifically so this distinction isn't lost. Check each file's own
status line.

## Repository map

```
CLAUDE.md                  this file
README.md                  human-facing project overview
PROJECT_STATUS.md          current state, gate status, what's locked vs. draft
NEXT_ACTION.md             exact next step for the next session
DECISION_LOG.md            dated record of deliberate decisions
CHANGELOG.md               dated log of what changed each session
.gitignore

00_project/                Gate 0: charter, workflow, policy, risk register
01_author_bible/           prose voice, style, dialogue, banned clichés
02_novel_bible/            premise, themes, genre, setting, Bellwether House,
                            Palinode, stakes/conflict/symbolism matrices
03_characters/             full character bible, relationship/knowledge/arc matrices
04_plot/                   synopses, structure, opening/ending options
05_mystery/                six timelines, clue register, reveal ladder, fairness audit
06_chapter_briefs/         locked briefs, written chapter-by-chapter once Gate 5 passes
07_manuscript/             reader-facing prose only, once drafting begins — currently empty
08_continuity/             living registers, updated every chapter once drafting begins
09_research/               source log, fact-check queue, legal/sensitivity notes
10_revision/                post-draft editing passes — not yet applicable
11_beta_readers/           beta feedback system — not yet applicable
12_publishing/             positioning and submission materials
tools/                     word count, continuity scan, repetition check, chapter
                            stats, manuscript assembly scripts
```

## Hard rules

- `05_mystery/` (once Gate 3 completes it in full) is confidential
  production material for the true solution. Its contents never appear
  verbatim or by clear implication in `07_manuscript/` before the
  chapter the reveal ladder schedules.
- `07_manuscript/` contains reader-facing prose only — no editorial
  brackets, no TODOs, no author asides — once drafting begins. It is
  currently empty; this session did not draft prose, per instruction.
- Every register update in `08_continuity/` is traceable to the chapter
  that caused it, once drafting begins.
- Commit only after the unit of work being committed is internally
  coherent — not mid-draft, not with an incomplete gate claimed complete.
- Do not fabricate research. Every factual claim used to ground the
  novel's procedural detail (insurance investigation practice, missing
  persons procedure, NYC residential building systems, identity fraud
  mechanics) is logged in `09_research/` with source, access date, and
  confidence — or explicitly queued as unresolved in
  `09_research/FACT_CHECK_QUEUE.md`. Never silently assume.
- Do not provide actionable, real-world step-by-step instructions for
  committing identity fraud, evading law enforcement, or defeating
  specific financial/insurance controls. Palinode's methods are
  characterized at the level a thriller reader needs (see
  `02_novel_bible/palinode_system.md`), never at the level of a working
  how-to.
- No named real people, real companies, or real addresses. Bellwether
  House, Palinode, and every institution in this novel are invented (see
  `02_novel_bible/setting_bible.md`).
