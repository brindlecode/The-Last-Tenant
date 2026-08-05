# Fairness Audit

STATUS: COMPLETE at Gate 3 depth. Systematic check that the solution is
inferable before the climax but not obvious, run against the now-locked
`clue_register.md` and `reveal_ladder.md`.

## Method

Per `02_novel_bible/genre_contract.md`'s working principle: this book's
fairness question is about pattern-recognition across genuine partial
truths, not about spotting who's lying. For each major reveal, this
audit confirms (a) every fact the reveal depends on was available to
the reader beforehand through fair means (a scene, a document, an
established character trait — never privileged narrator knowledge), and
(b) the reveal is not telegraphed so early or so plainly that it lacks
genuine surprise.

## Reveal-by-reveal audit

| Reveal | Available evidence before it lands | Inferable? | Telegraphed too early? |
|---|---|---|---|
| Apartment 4C's vacancy is a paperwork mechanism | Clue #1 (the record itself, honestly reported); Mara's established professional skepticism | Yes — a reader who knows Mara's profession should expect her to eventually question an official record rather than accept it | No — nothing states or implies the mechanism before Part II's actual document trail |
| "Anna" is Mara's mother | Clue #5 (Irena's account) + Clue #2 (numbering-scheme context) + the reader's own accumulating sense that "twenty [-three] years ago" and Mara's age don't look coincidental | Yes, and deliberately gettable slightly ahead of Mara's own explicit confirmation for an attentive reader — this is the audit's clearest example of the "fair but not obvious" target, since it requires connecting two separately-planted, individually-unremarkable facts | No — Irena's account is introduced as one of seven ordinary witness interviews, not flagged as special |
| Elena built all seven identities herself | Clue #4 (theater vocabulary pattern across accounts) is the fair-play spine of this reveal; requires noticing a pattern across multiple, separated scenes | Yes, for an attentive reader tracking dialogue across witnesses — this is the single clue in the register explicitly designed to reward close reading over plot-summary reading | No — individually, each witness account is fully credible on its own |
| Elena's operative complicity (the youth-program client) | **Currently under-clued** — see Gap 1 below | Marginal | N/A |
| Adrienne Shaw's Part II betrayal | Her established character (real mentorship + institutional fluency + something "off" about her handling of certain cases, per her own file's pre-existing "contradictions" field) | Yes, as a *possibility* — not as the specific mechanism (Palinode-linked pressure specifically, versus generic self-protection), which is fair to hold back since the specific mechanism is new information, not a fact the reader was denied access to | No |
| Gabriel Knox's report as the trigger for Elena's capture | Clue #3 (his logs, his evasiveness, his established job/home stakes) | Partially — the reader can infer he knows more than he says; the *specific* fact that his choice (not Palinode's initiative alone) triggered the capture is a genuinely new, late-arriving piece of causal information | No, and this is appropriate — see standing note below on causal-mechanism reveals |
| Peter Marsh's real identity and death | New evidence item (Clue #12), introduced specifically as confirmation late in Part III | N/A — designed as confirmation of an already-suspected shape (that something happened to the father), not a fresh mystery requiring its own fair-play buildup | No |
| Julian Vale's downfall mechanism | His established, consistent characterization (unmet need to be understood/approved of; controlled, patient, ideologically defended) across every prior scene with him | Yes — the *method* of his undoing (his own need, not force) should read as consistent with everything the reader has seen of him, not a sudden new trait invented for the climax | No |

## Gaps found and required fixes

**Gap 1 — Elena's specific operative complicity (the youth-program
client) is currently locked as backstory fact in
`gate_3_mystery_validation.md` but has no corresponding entry in
`clue_register.md`.** This is a fairness risk: if this fact is simply
told to the reader in Part II with no prior clueing, it will land as
information rather than revelation, weakening exactly the beat
`risk_register.md` R-011 says is required to work (Elena must cost the
reader real sympathy before re-earning it). **Required fix, logged
here and to be executed at Gate 4/drafting**: seed at least one Part I
or early-Part-II detail (a candidate: something in Rina Cho's footage,
or a detail in Elena's own kept notebooks if Gate 4 gives Mara access to
any of Elena's effects) that gestures at Elena's operative competence
being real and consequential, before the specific harmful client is
named — so the eventual reveal completes a suspicion the text has
already allowed rather than introducing one from nothing. **Added to
`clue_register.md` is not done in this pass** — flagged here as
required Gate 4 work rather than invented now without a chapter map to
place it against.

**Gap 2 — causal-mechanism reveals (Gabriel's report; Adrienne's
specific pressure) are appropriately un-telegraphed but must not become
unfair by being unreachable.** Standing note, not a fix: per this
audit's own method, a reveal explaining *why* something happened
(causal mechanism) is allowed to be genuinely new information at the
moment it lands, as long as *that something happened* was already fairly
clued — which both cases satisfy (Gabriel's withholding and Adrienne's
"something off" quality are both pre-established). Gate 4 should not
try to over-clue these into full advance-inferability; doing so would
flatten two of the book's more sophisticated reveals into
over-signposted ones.

## Verdict

**Fairness audit PASSES** with one required follow-up item (Gap 1,
logged for Gate 4/drafting, not blocking Gate 3 closure since it's a
clue-placement task requiring a chapter map that doesn't exist yet).
No reveal in the ladder depends on a fact withheld from the reader
through narrator-level concealment rather than natural story fog.
