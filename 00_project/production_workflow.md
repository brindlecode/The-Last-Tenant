# Production Workflow

STATUS: COMPLETE (Gate 0)

Two distinct workflows exist in this project's life: the **planning
workflow** (Gates 0–5, no prose) and the **drafting workflow** (Gate 6
onward, one chapter at a time). This file defines both. Do not blend
them — drafting discipline applied too early wastes effort on prose that
might not survive a foundation change; planning-level looseness applied
during drafting produces incoherent chapters.

## Planning workflow (current phase)

1. Work gate by gate, in order. Do not start Gate 2 work believing Gate 1
   is "probably fine" — confirm it against `quality_gates.md`'s
   checklist first.
2. Every gate's output is a **file**, not a conversation. If a decision
   was made in discussion but not written to the relevant canonical
   file, it is not yet real.
3. Where the gate requires generating and comparing alternatives (Gate 1
   especially), generate the full required count before evaluating any
   of them — do not stop at the first plausible option and rationalize
   it as sufficient. Comparison requires real alternatives to compare
   against.
4. Every non-trivial creative decision with downstream consequences
   (character fates, mystery mechanics, structural choices) gets a dated
   entry in `DECISION_LOG.md` — what was decided, what alternatives were
   considered, why this one, and what it constrains going forward.
5. A gate is not closed by asserting it's closed. It's closed when its
   `quality_gates.md` checklist is satisfied item by item, and
   `PROJECT_STATUS.md` is updated to reflect that, with a link to the
   evidence.
6. Commit planning work when a gate (or a clearly-scoped part of one) is
   internally coherent — not mid-thought, not with contradictions between
   files still unresolved.

## Drafting workflow (future phase, once Gates 0–5 are closed)

For each chapter, in order, at full depth — no batching multiple
chapters through at reduced quality:

1. **Brief.** A locked brief exists in `06_chapter_briefs/` before the
   chapter is drafted: POV, scene list, goal, clues planted/reinforced/
   withheld (cross-referenced to `05_mystery/clue_register.md`), entry/
   exit state, prohibited revelations for this chapter (cross-referenced
   to `05_mystery/reveal_ladder.md`), target word count.
2. **Draft.** Prose against the brief, in
   `07_manuscript/part_N/chapter-NN.md`. Reader-facing prose only.
3. **Critique.** An honest editorial pass: what's weak, what's flat,
   where the voice slips, where pacing sags or rushes, where the mystery
   engine is doing the story's emotional work instead of the characters.
4. **Revise.** Based on the critique.
5. **Audit**, minimum six passes against the revised draft:
   - *Continuity* — against `08_continuity/canonical_facts.md`,
     `timeline_calendar.md`, and prior chapters.
   - *Clue* — against `05_mystery/clue_register.md`; confirms planted
     clues are fairly legible in hindsight and nothing contradicts the
     objective truth timeline.
   - *Voice* — against `01_author_bible/prose_style_guide.md`,
     `dialogue_guide.md`, and the character's own file in
     `03_characters/`.
   - *Pacing* — scene-by-scene against the chapter brief and
     `04_plot/tension_curve.md` / `emotional_curve.md`.
   - *Factual* — real-world procedural claims checked against
     `09_research/` sources or queued if unresolved.
   - *Prose* — line-level craft: cliché (`01_author_bible/banned_cliches.md`),
     repetition, rhythm, filtering words, overwriting.
6. **Register update.** `08_continuity/` files updated with whatever the
   chapter established — traceable to the specific chapter.
7. **Word count update** in `PROJECT_STATUS.md`.
8. **Prohibited-revelation sign-off** — explicit confirmation nothing on
   `05_mystery/reveal_ladder.md`'s not-yet list appeared early.
9. Chapter's own audit report written to a per-chapter file (location and
   naming convention to be fixed at Gate 4/5, alongside
   `06_chapter_briefs/`).

Periodically (recommended: every 4–6 chapters, and mandatory at every
part boundary), run a **combined audit** across the accumulated chapters
as a unit — checking them against each other, not just against the
registers individually, since per-chapter audits can miss cross-chapter
drift. Where feasible, use an independent review (a fresh session or
reviewer with minimal priming) for at least the part-boundary combined
audits — a reviewer close to the material for many consecutive chapters
is structurally likely to rationalize past their own blind spots.

## Session handoff discipline

Every session, regardless of which workflow it's operating in, ends by
updating `PROJECT_STATUS.md` (current state), `NEXT_ACTION.md` (the
literal next step, specific enough that a session with zero other
context could execute it), `DECISION_LOG.md` (anything decided this
session with downstream consequences), and `CHANGELOG.md` (dated summary
of what changed). This is not optional bookkeeping — per `CLAUDE.md`,
sessions do not share memory, and these four files are the entire
interface between them.
