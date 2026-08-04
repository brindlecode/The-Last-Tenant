# Definition of Done

STATUS: COMPLETE (Gate 0)

Per-artifact-type completion criteria. An artifact is not "done" because
it exists; it's done when it meets its type's bar below. Files seeded
this session that don't yet meet their type's bar are marked
`STATUS: DRAFT` at the top of the file — that marking is not optional
housekeeping, it's the difference between "available reference material"
and "validated canon."

## A gate

Done when every item in its `00_project/quality_gates.md` checklist has
a specific, locatable answer, and `PROJECT_STATUS.md` reflects the
closure with a link to the evidence. Not done if any checklist item's
answer is "implied" rather than written down.

## A canonical fact (setting, system, or backstory detail)

Done when it's written into the correct `02_novel_bible/` or
`08_continuity/` file, doesn't contradict any other canonical file, and —
if it changed a previously-decided fact — the change and its downstream
consequences are logged in `DECISION_LOG.md`.

## A character file

Done (Gate 2 standard) when every field in the character template
(`03_characters/character_index.md`) is filled with specific, non-generic
content; the character's indispensability question is answered; and, for
any character intersecting a real-world vulnerable or marginalized
identity, the stereotype-risk review is complete and specific. Seeded but
not yet at this standard = `STATUS: DRAFT`.

## A timeline or clue-register entry (05_mystery/)

Done (Gate 3 standard) when it's cross-checked against all six timelines
for contradiction, has a fairness assessment, and (for clues) a
confirmed payoff chapter once chapters exist. Not done merely because a
plausible-sounding event or clue has been written down once.

## A chapter brief (06_chapter_briefs/, future)

Done when it specifies POV, scene list, goal, clues planted/reinforced/
withheld with clue-register cross-references, entry/exit state,
chapter-specific prohibited revelations, and a target word count — and
has been checked against Gates 2–5 for consistency, not written in
isolation.

## A drafted chapter (07_manuscript/, future)

Done when it has been through every step of
`production_workflow.md`'s drafting workflow — draft, critique, revise,
all six audits passed (not attempted — passed, with any findings
resolved), registers updated, word count updated, prohibited-revelation
sign-off recorded. A chapter that has only been drafted and not yet
audited is not done; say so plainly in `PROJECT_STATUS.md` rather than
letting "drafted" read as "finished."

## A research entry (09_research/)

Done when it has a specific claim, a real source, an access date, a
confidence level, a stated effect on the story, and an explicit
fictionalization decision (what the manuscript will actually say, and
how far that departs from the sourced fact and why). An entry with a
claim but no source is not done — it belongs in
`FACT_CHECK_QUEUE.md` until it is.

## A revision pass (10_revision/, future)

Done when it has been run against a complete manuscript draft (not
partial), produced a written report of findings, and every finding has
either been fixed or explicitly deferred with reasoning.

## A publishing/positioning artifact (12_publishing/, future)

Done when it accurately reflects the finished (or, for earlier drafts,
explicitly labeled as draft-stage) manuscript, and has been checked
against `originality_policy.md`'s no-overclaiming rule.

## This session's own output

Done, for Gate 0 + Gate 1 purposes, means: the full repository structure
exists; every root and `00_project/` file meets its own bar above; Gate 1
concept validation is genuinely comparative (real alternatives generated
and weighed, not a single option rationalized); every file seeded beyond
Gate 1's scope is honestly marked `STATUS: DRAFT` with a note on what
gate would need to run to validate it; `DECISION_LOG.md` captures every
unresolved high-impact choice rather than silently picking one; and
`NEXT_ACTION.md` gives a session with zero other context a specific,
executable next step.
