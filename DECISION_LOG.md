# Decision Log

Dated record of deliberate decisions and course changes. Append, don't
rewrite history — if a decision is later reversed, add a new entry
rather than editing the old one. Two kinds of entries live here:
decisions actually made this session (with reasoning), and high-impact
decisions deliberately left open for human approval rather than
defaulted.

---

## 2026-08-04 — Branch rebuilt as a true orphan; prior branch rejected outright

Per explicit instruction, the Nora Hale/Cass Ferris material on
`claude/last-tenant-part-one-ch1-4-nfwdvx` is rejected in full and is
not canon for this project. Rather than branch from it and delete its
files (which would leave the rejected material reachable in this
branch's git history), `claude/mara-elena-foundation` was created as a
**true orphan branch** — `git checkout --orphan` followed by clearing
the working tree — so it shares zero commit history with the rejected
branch. The rejected branch itself was not touched, read for reuse, or
altered in any way beyond what was necessary to confirm it exists and
is separate (`git branch -a`, `git ls-remote`).

There is also no `main` branch anywhere in this repository (confirmed
via `git ls-remote` — the rejected branch is the only ref that has ever
existed here, and its own founding session record shows this was a
from-empty repository). The task's literal `git checkout main` /
`git pull` instructions don't apply to this repository's actual state;
adapted as above.

## 2026-08-04 — Full Gate 0 + Gate 1 foundation built in one session

Per explicit instruction, this session built the complete repository
structure (all 13 numbered directories plus `tools/`) and fully closed
Gates 0 and 1. Gates 2–5 were **not** formally closed this session
(not required by the task's own numbered execution list) — character
files, mystery timelines, and plot structure documents were seeded with
real, substantive working content wherever the source brief supplied
enough to do so responsibly, each explicitly marked `STATUS: DRAFT` or
`STATUS: NOT STARTED` so the distinction between "seeded" and
"validated" isn't lost. See `PROJECT_STATUS.md` for the exact per-gate
breakdown.

## 2026-08-04 — Naming collisions caught and fixed during character-bible construction

Two collisions were found and corrected while building `03_characters/`:

1. The source brief names one of Jonah Bell's client-identity aliases
   for Elena "Nora Vale" — colliding with Julian Vale's surname within
   the same cast, and separately echoing "Nora," the rejected prior
   branch's protagonist name. **Renamed to "Dana Kessler."** See
   `03_characters/jonah_bell.md` and `character_index.md`.
2. Two atmospheric lines drafted into `02_novel_bible/bellwether_house.md`
   and, separately, considered for `symbolism_map.md` echoed specific
   executed imagery from the rejected branch (a buzzer-panel label-ghost
   detail; a "died gently" description landing in the antagonist's own
   flat, structurally close to that branch's own near-miss pattern
   around loaded language). Both caught and rewritten before being
   finalized — see `bellwether_house.md`'s atmosphere section and
   `banned_cliches.md`'s project-specific list, which was written
   specifically to catch this category of risk going forward.

## 2026-08-04 — Gate 1 working selections made via genuine comparison, not default

Per `00_project/gate_1_concept_validation.md`: five opening options, four
ending architectures, three Palinode origin stories, three Apartment 4C
vacancy explanations, and three childhood-event versions were each
generated in full before any were evaluated, and each selection states
what was rejected and why. Full reasoning in that file and in
`04_plot/opening_options.md` / `ending_options.md`. These selections are
explicitly provisional, revisable at Gate 4.

## 2026-08-04 — Real (not fabricated) research seeded, most research still queued

Two web searches were run this session to seed `09_research/SOURCE_LOG.md`
with genuinely sourced facts (missing-person reporting has no mandatory
waiting period, confirmed via NYC311; "synthetic identity fraud" is a
real, defined financial-crime category, confirmed via a Federal
Reserve-affiliated source) rather than fabricating research entries. The
first finding directly corrected a plausibility assumption embedded in
`04_plot/five_page_synopsis.md`'s loose framing — recorded as a required
correction there. The great majority of `09_research/FACT_CHECK_QUEUE.md`
remains genuinely unresolved; this was a proof-of-method pass, not a
research phase.

---

## 2026-08-05 — Gate 2 and Gate 3 session: all five previously-open high-impact decisions resolved

Per explicit instruction, this session resolved every decision flagged
below in the "Unresolved high-impact decisions" section (preserved
un-edited immediately below this entry, per this file's own "append,
don't rewrite history" rule) through genuine multi-option generation and
comparison — not by default, and not by picking the first plausible
answer. Summary (full reasoning in the files cited):

1. **Title, RESOLVED**: twenty candidates generated and scored; "THE
   LAST TENANT" retired (confirmed collision); **"A BORROWED NAME"**
   selected. Full comparison: `12_publishing/title_review.md`. Propagated
   to `CLAUDE.md`, `README.md`, `00_project/project_charter.md`,
   `02_novel_bible/master_premise.md`, `risk_register.md` R-013 (marked
   resolved), `12_publishing/elevator_pitch.md`, and `tools/*.py`
   docstrings. `00_project/gate_1_concept_validation.md` deliberately
   left un-edited per its own no-silent-edit rule — it remains an
   accurate record of the Gate 1-era holding position.
2. **Voss family origin/father's fate, RESOLVED**: three versions
   generated (predatory-lender debt flight; genre-standard organized-
   crime witness relocation; records-fraud whistleblower killed, family
   relocated in the aftermath) plus a domestic-violence variant rejected
   early for repeating an already-used shape. Selected: the
   records-fraud version, refining rather than replacing Gate 1's
   already-selected "external criminal danger" category. Original
   surname **Marsh**; father **Peter Marsh**, killed in a staged
   accident after uncovering property-title fraud in his work as a
   records examiner; mother **Anna Marsh** → **Anna Voss**. Full
   record, including why this creates causal (not coincidental) irony
   with Mara's own profession: `00_project/gate_3_mystery_validation.md`
   Decision 2.
3. **What happened to Elena, RESOLVED**: four versions generated
   (soft containment; self-directed hiding plus unrelated medical
   crisis; betrayal-and-violent-struggle; self-orchestrated
   disappearance). Selected: non-violent soft containment at a
   Palinode-controlled site, ordered personally by Julian Vale, triggered
   by Gabriel Knox's self-protective report — a specific human failure
   point, not omniscience. Full mechanism, including Elena's
   whistleblower trigger, the hidden cache's true origin and purpose,
   Part II's betrayal (Adrienne Shaw), and Julian's downfall mechanism:
   `gate_3_mystery_validation.md` Decision 3.
4. **Ending architecture, CONFIRMED**: re-tested Architecture 1
   (refined) against the now-fully-built mystery from Decisions 2–3;
   confirmed without change, now with a concrete rather than
   architectural climax. Full lock: `04_plot/final_ending.md`.
5. **Teo Marchetti romantic subplot, CONFIRMED**: four versions compared
   (no romance; unconsummated slow burn; pre-existing history; active
   developing romance). No-romance default confirmed, with specific
   reasoning beyond inertia (his false belief already mirrors Mara's
   own; adding romantic tension would compete with, not reinforce, that
   thematic mirroring). Full comparison and newly resolved Teo/Adrienne
   prior-overlap cross-check: `03_characters/investigative_counterpart.md`.

All five decisions, plus the full ~25-question Gate 3 objective-truth
checklist, are recorded in `00_project/gate_3_mystery_validation.md`.
`08_continuity/open_questions.md` updated to reflect every item now
closed.

## 2026-08-05 — Adversarial red-team review conducted; 11 Critical and 21 High findings fixed

Per this session's explicit instruction, an eight-agent, ten-perspective
adversarial red-team review was run against the freshly-closed Gate 2
and Gate 3 material (full report: `00_project/red_team_review.md`).
This surfaced genuine, load-bearing gaps that a self-administered check
had missed or, in one case, prematurely claimed as already
independently verified. Every Critical finding was fixed; the large
majority of High findings were fixed directly, with the remainder
honestly logged as Gate 4/drafting-stage work this session cannot
complete without a chapter map. Highlights, full detail in the review
file:

- **Process integrity**: `solution_stress_test.md` and
  `gate_3_mystery_validation.md` had cited `00_project/red_team_review.md`
  as already-completed corroboration *before that file existed* — caught
  independently by four of five review agents. The review has now
  genuinely been conducted and every citation is accurate.
- **A real claim-authority gap**: nothing previously gave Mara any
  actual professional standing to investigate Bellwether House — fixed
  with a new claim anchor (a dormant Meridian policy under one of
  Elena's aliases).
- **A legally indefensible climax**: the original ending had Mara
  personally suppressing evidence of ongoing crimes — rebuilt as full
  disclosure plus advocacy for prosecutorial discretion, which is both
  legally sound and a more precise realization of the book's own theme.
- **Two representation findings that required structural fixes, not
  just softer language**: Evelyn Price's storyline was restructured
  away from a fabricated-domestic-violence narrative (which reproduced
  a real, damaging trope) to a coercive-high-control-group narrative;
  Calvin Moss's professional skill was decoupled from his disability's
  onset (fixing an instrumentalized-disability structure), and
  "agoraphobia/mobility limitation" was retired as a conflated pairing.
- **A significant, respectfully-researched gap in Irena Petrov's
  history**: her file previously never engaged the fact that her stated
  birth year places her in Odesa during the WWII occupation and the
  near-destruction of the city's Jewish community — now addressed with
  a specific, historically-grounded family evacuation history.
- **An originality near-miss, independently caught by two agents**: the
  hidden evidence cache's staging as "a concealed cavity in a wall"
  echoed `banned_cliches.md`'s explicit ban closely enough to require a
  fix, not a dismissal — relocated to the building's sealed dumbwaiter
  shaft.
- **A genuine fairness-audit blind spot**: no clue in the register
  actually delivered "Palinode is an organization," the single most
  foundational reveal in the ladder, despite five other reveals
  depending on it — fixed with a new clue (Elena's own investigative
  notes, found in the relocated cache).
- **Institutional/procedural realism fixes**: why the case doesn't
  escalate beyond one detective (institutional fragmentation, now
  explicit); Adrienne Shaw's Part II arc rebuilt to include an earlier,
  active phase of shielding Mara before her reversal (closing both a
  timing-implausibility finding and a fairness gap); Teo Marchetti's
  professional outcome (an IAB inquiry with real, lasting cost) finally
  locked; a chronology gap in the Apartment 4C lease dates closed.
- **Craft**: five characters' behavioral tells sharing one template, and
  several exact-verb collisions across different characters, both fixed.

Full resolution tracking for all 11 Critical and 21 High findings, plus
the Medium/Low findings, is in `00_project/red_team_review.md`. This
entry is the pointer; that file is the record.

---

## Unresolved high-impact decisions as of the prior (foundation) session — ALL RESOLVED ABOVE, preserved for history

These were flagged in the foundation session specifically because they
materially shape the book and were deliberately **not** defaulted
without sign-off. **All five are now resolved — see the entry directly
above.** Preserved un-edited below per this file's own append-only rule;
do not treat this section as still open.

1. **Title uniqueness** (`00_project/risk_register.md` R-013,
   `12_publishing/title_review.md`): "THE LAST TENANT" duplicates this
   repository's own rejected branch's title and nearly duplicates a
   related project's title ("The Silent Tenant"). Kept as working title
   for continuity of this session's work; needs an explicit human call
   before any public/submission use.
2. **The Voss family's original (pre-Palinode) surname and the father's
   exact fate** (`00_project/gate_1_concept_validation.md` Part B3):
   deliberately left open rather than invented casually, since they're
   central mystery-architecture decisions best made once Gate 3's full
   timeline work is underway — flagging here so a human reviewer knows
   this is a live decision point, not an oversight.
3. **What actually happened to Elena in her disappearance window**
   (`05_mystery/elena_timeline.md`, `palinode_timeline.md`): the single
   most protected fact in the entire project, intentionally undecided at
   Gate 1. This is the most consequential open decision in the whole
   repository and should be made deliberately at the start of Gate 3
   work, ideally with human input on tone (how dark an outcome the book
   should commit to), not defaulted by whichever session happens to
   reach Gate 3 first.
4. **Ending architecture final lock** (`04_plot/final_ending.md`):
   Architecture 1 (refined) is the working selection but explicitly not
   final — flagged for human confirmation once Gate 3/4 structure exists
   to test it against, per that file.
5. **Whether a romantic subplot for Teo Marchetti is truly unwanted**
   (`03_characters/investigative_counterpart.md`): defaulted to no
   romance per the source brief's own stated default, but since this
   session invented the character from scratch (the brief didn't name
   one), flagging the underlying default itself for confirmation rather
   than treating an invented character's romantic status as
   self-evidently settled.
