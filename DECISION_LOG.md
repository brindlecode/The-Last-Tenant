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

## Unresolved high-impact decisions — awaiting human approval

These are flagged here specifically because they materially shape the
book and were deliberately **not** defaulted by this session without
sign-off:

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
