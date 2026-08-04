# Quality Gates

STATUS: Gate 0 definitions COMPLETE and self-satisfied by this document's
existence; Gate 1 COMPLETE per `gate_1_concept_validation.md`; Gates 2–5
NOT YET STARTED formally (see each gate's section for what currently
exists vs. what's required to close it).

A gate is closed when every item in its checklist has a specific,
locatable answer in the repository — not a vague gesture at one. "We
thought about it" is not a closed gate; a linked file section with the
actual answer is. No chapter of manuscript prose may be drafted before
Gates 0–5 are all closed.

---

## Gate 0 — Foundation

**Purpose**: the repository itself is a working production system before
any creative content is judged.

Checklist:
- [x] Repository structure exists matching the approved tree (see
  `CLAUDE.md`'s Repository Map).
- [x] `project_charter.md` states identity, scope, non-goals, and
  process-level success criteria.
- [x] This file (`quality_gates.md`) defines every gate's criteria.
- [x] `production_workflow.md` defines how planning work and (later)
  chapter drafting actually proceed, session to session.
- [x] `originality_policy.md` states the anti-reuse rule against the
  rejected prior branch, general originality discipline, and the
  no-overclaiming rule.
- [x] `definition_of_done.md` states, per artifact type, what "done"
  means.
- [x] `risk_register.md` contains a real, specific risk assessment, not
  placeholder rows.
- [x] Root status files (`PROJECT_STATUS.md`, `NEXT_ACTION.md`,
  `DECISION_LOG.md`, `CHANGELOG.md`) exist and are current.

**Closed**: yes, as of this branch's founding commit.

---

## Gate 1 — Concept validation

**Purpose**: confirm the premise justifies a novel, the hook is strong
enough to sustain 46 chapters, and the highest-risk worldbuilding
questions have been genuinely stress-tested rather than assumed.

Checklist:
- [ ] Answered, with reasoning, not assertion: why this is a novel and
  not a shorter form; why Mara is indispensable to it; why Elena is
  indispensable to it; why the story begins when it begins; why
  authorities/institutions can't resolve it quickly; why Mara can't walk
  away; what distinguishes this from a generic missing-sister thriller;
  whether Palinode is plausible; whether the title is strong enough; what
  the emotional promise to the reader is.
- [ ] At least five distinct opening options generated and compared on
  their merits, with a reasoned working selection (revisable at Gate 4).
- [ ] At least four distinct ending architectures generated and compared,
  with a reasoned working selection (revisable at Gate 4).
- [ ] At least three versions of Palinode's origin generated and
  compared, with a reasoned working selection.
- [ ] At least three explanations for Apartment 4C's apparent
  twelve-year vacancy generated and compared, with a reasoned working
  selection.
- [ ] At least three versions of the Voss family's childhood event
  generated and compared, with a reasoned working selection.
- [ ] Strengths, weaknesses, cliché risks, plausibility risks, emotional
  risks, market-positioning risks, legal risks, and research needs all
  identified specifically (not generically).
- [ ] All of the above and their reasoning recorded in
  `gate_1_concept_validation.md`, with the working selections also
  reflected in the relevant `02_novel_bible/` and `04_plot/` files.

**Closed**: yes, as of this branch's founding commit — see
`gate_1_concept_validation.md` for the full record. Working selections
made there are **provisional and explicitly revisable at Gate 4**, not
frozen; Gate 1's job is to prove the concept can hold a novel, not to
lock every downstream detail.

---

## Gate 2 — Character validation

**Purpose**: every recurring character earns their place, is fully
built, and survives a stereotype/utility audit.

Checklist:
- [ ] Every character in `03_characters/character_index.md` has a file
  completing every field in the character template (see
  `character_index.md` for the field list) — not just the fields the
  original project brief happened to specify.
- [ ] For each character: an explicit answer to "what does this person
  do in the story that no other character could do," and confirmation
  that removing them would leave a hole, not just a redundancy.
- [ ] Stereotype-risk review completed for every character whose identity
  intersects a real-world marginalized or vulnerable group (age,
  disability, domestic-violence survivorship, childhood, immigrant
  background, etc.) — specificity-over-trope confirmed, not assumed.
- [ ] `relationship_matrix.md`, `knowledge_matrix.md`, and
  `character_arc_matrix.md` completed and cross-checked against each
  character's individual file for contradictions.
- [ ] `investigative_counterpart.md` resolved: either a fully-built
  counterpart character exists, or an explicit, reasoned decision that
  none is needed is recorded.

**Closed**: no. Character files in this repository currently carry
`STATUS: DRAFT — seeded from originating brief` and are usable as
working reference, not as validated canon. Formal Gate 2 closure is
future work — see `NEXT_ACTION.md`.

---

## Gate 3 — Mystery validation

**Purpose**: the central mystery is fair, plausible within the story's
own rules, and structurally sound across every character's account.

Checklist:
- [ ] All six timelines complete and mutually consistent: objective
  truth, Mara's knowledge, reader's knowledge, Elena's operational
  history, Palinode's response, evidence provenance.
- [ ] Every clue in `clue_register.md` has: first appearance, surface
  meaning, true meaning, who notices it, why it's misread, payoff
  chapter, and an explicit fairness check.
- [ ] `red_herring_register.md` confirms every red herring arises from a
  real character motive, not authorial misdirection for its own sake.
- [ ] `reveal_ladder.md` sequences every major revelation against the
  chapter map (pending Gate 4) and confirms no reveal depends on a fact
  the reader couldn't have inferred.
- [ ] `solution_stress_test.md` completed: an adversarial pass
  specifically hunting for plot holes, unfair leaps, and coincidences
  that do the story's work instead of character choices.

**Closed**: no. `05_mystery/` currently contains the twist architecture
as given in the originating brief, organized into the correct file
slots, explicitly marked draft. It has not yet been stress-tested,
timelined day-by-day, or fairness-audited.

---

## Gate 4 — Structure validation

**Purpose**: the novel's shape is locked at the chapter level before any
chapter is drafted.

Checklist:
- [ ] `act_structure.md` and `sequence_structure.md` complete.
- [ ] `chapter_map.md` — all ~46 chapters listed with POV, goal, and
  function.
- [ ] `scene_inventory.md` complete.
- [ ] `tension_curve.md` and `emotional_curve.md` mapped and checked
  against each other for chapters where plot tension rises while
  emotional stakes go flat (or vice versa) — a specific failure mode to
  watch for in this book given its dual engine.
- [ ] `subplot_map.md` complete, confirming every subplot (Adrienne
  Shaw's compromised institutional position; the investigative
  counterpart if used) resolves or is deliberately left open with a
  stated reason.
- [ ] Opening and ending selections from Gate 1 revisited and either
  confirmed or deliberately changed, with reasoning, in
  `04_plot/final_ending.md` and the opening chapter's brief.
- [ ] All required milestones placed against actual chapter numbers:
  immediate disturbance in the opening pages; inciting incident ~8–10%;
  irreversible commitment ~20–25%; first major reversal ~30%; midpoint
  ~48–52%; major betrayal ~60–70%; all-is-lost ~75%; climax driven by
  Mara's decision, not circumstance; emotional resolution between the
  sisters; final image that answers or deliberately complicates the
  identity question.

**Closed**: no.

---

## Gate 5 — Pre-draft red-team validation

**Purpose**: one last adversarial pass across everything Gates 1–4
produced, specifically hunting for plausibility failures, fairness
failures, and originality failures, before a single chapter brief is
written.

Checklist:
- [ ] An adversarial reviewer role (a dedicated pass, ideally by a fresh
  reader/session with minimal priming) has tried specifically to break
  the mystery's fairness, find a plot hole Palinode's methods can't
  actually support, and find any residual similarity — structural or
  imagistic, not just verbatim — to the rejected prior branch.
- [ ] Every finding either fixed or explicitly accepted with reasoning
  in `DECISION_LOG.md`.
- [ ] `06_chapter_briefs/` ready to receive Chapter 1's brief.

**Closed**: no.

---

## Escalation rule

If a later gate's work reveals that an earlier "closed" gate's decision
doesn't actually hold (for example, Gate 3's timeline work reveals Gate
1's Apartment-4C explanation doesn't survive contact with a fully built
clue register), the earlier gate is **reopened**, not silently patched
around. Record the reopening and the resolution in `DECISION_LOG.md`.
This is expensive but cheaper than drafting 46 chapters against a
foundation that doesn't actually hold.
