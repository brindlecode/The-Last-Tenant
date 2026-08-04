# Decision Log

Dated record of deliberate decisions and course changes. Append, don't
rewrite history — if a decision is later reversed, add a new entry rather
than editing the old one.

---

## 2026-08-04 — Project originated from an empty repository

The task brief for this session assumed an existing project (`CLAUDE.md`,
completed Gates 0–5, approved chapter briefs already in place). On
inspection, the repository had no commits, no files, and no branches on
the remote at all — a genuinely blank slate, not a continuation.

A clarifying question was raised (new story vs. connected to an unrelated
manuscript found while checking Drive for canonical files; how much to
complete autonomously vs. pause for review) but the interaction was
interrupted before it could be answered, and the session was told to
continue. Decision: proceed autonomously rather than block indefinitely —
originate an entirely new, original story (not connected to any other
manuscript), build Gates 0–5 from scratch using the process the task brief
itself specifies, verify that foundation for real (not a rubber stamp —
see `reports/gate-verification.md`, which records one real defect found
and fixed during that pass), then draft Chapters 1–4 to the full
draft/critique/revise/audit standard requested, and stop for review at the
end of that unit rather than continuing past it unsupervised.

Consequence: everything in `bible/` and `registers/` is new authorial
work product from this session, not recovered or verified pre-existing
canon. Flagging this plainly here and in the handoff so a human reviewer
knows to actually read the foundation documents before trusting them,
rather than assuming they were vetted in an earlier session that didn't
in fact happen.

## 2026-08-04 — Title disambiguation from an unrelated prior manuscript

While checking Google Drive for canonical project files, found a finished,
unrelated manuscript in the account: *The Silent Tenant* (pen name
"Seraphina Vance," gothic thriller, rural manor setting). THE LAST TENANT
is a distinct, original project — different premise, cast, and setting
(urban converted mill, not a rural manor) — and does not reuse any
character, plot element, or text from that other manuscript. Noting this
explicitly so the similarity of title is understood as coincidental genre
convergence, not a mix-up.

## 2026-08-04 — Mystery mechanism locked before any prose

Central mystery resolved around a fire-safety cover-up in a converted
building rather than a more generic "landlord is a murderer" setup,
specifically so the protagonist's professional skill set (chartered
building surveyor) is the actual investigative engine, fairly, throughout.
Full solution locked in `bible/03-mystery-architecture.md` (confidential)
before any chapter brief was written, per the gate process.

## 2026-08-04 — Independent adversarial review used for the combined
four-chapter audit

Rather than close out the Chapters 1–4 combined audit with another
self-review, a fresh subagent with no prior context on this session was
given the confidential solution, the full register set, and all four
chapters, and asked to adversarially hunt for prohibited-revelation
leaks, POV violations, continuity errors, and cross-chapter repetition.
Decision, not a default: after three consecutive chapters of self-review
(each of which did catch real issues, logged in their own audit reports),
the risk of a fourth self-review rationalizing past my own blind spots
seemed higher than the cost of a dedicated independent pass, specifically
because this is the checkpoint the task explicitly gated the commit on.

It found and I fixed one real POV-discipline violation (Chapter 1
narrated Cole's internal motivation as fact rather than Nora's inference)
and three real cross-chapter continuity errors (a wrong day-of-week in
Chapter 4; a stale, self-contradicting weather planning note; a
~1.8-year drift between Cass's objection date as drafted in Chapter 3
and the original Gate-3-level planning figure). Full detail in
`reports/combined-ch1-4-audit.md`. None of these were prohibited-revelation
leaks — the eight-item list itself checked out clean — but they were real
errors a human reader would have hit. Recording the method here because
it worked better than another self-pass would have, and is worth
repeating at the equivalent checkpoint for future multi-chapter units
(e.g., before closing out Chapters 5–10 as a batch).

## 2026-08-04 — Held the commit until the combined audit finished, against
a hook nudge to commit sooner

Partway through the combined audit (while the independent review agent
was still running), an automated stop-hook fired asking that untracked
files be committed and pushed. Decision: continued waiting rather than
committing immediately. The task's explicit instruction was to commit
only once the four-chapter unit was coherent and audited, and the audit
was demonstrably still in progress, not stalled (confirmed via a
non-blocking status check rather than assumed). Nothing about the
untracked state put the work at risk — it was safely on disk in the
working tree — so there was no real cost to finishing the audit first
against the small, mostly-cosmetic cost of a hook nudge going unanswered
for a few minutes. Recorded here since it's exactly the kind of moment
where a generic automated nudge could otherwise override an explicit,
specific user instruction if followed reflexively.
