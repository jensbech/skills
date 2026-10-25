# Repetition: teach each thing once

Repetition is the most visible defect of a report written by parallel agents. Each writer produces a chapter that is complete on its own, so a reader going cover to cover is taught the same things several times. It reads as padding and makes the reader doubt that anyone read the whole thing. This file says how it happens and the recipe that prevents it. The orchestrator reads it in Phase 3; the consolidation editor and final reviewer read it too.

## What it looked like in the reference run

`scripts/repetition.py` on a delivered 137-page industry primer found:

| Section | Finding | Count |
|---|---|---|
| 1. Terms defined in several chapters | the industry's central market role defined in 4 chapters; the regulator's revenue cap and a grid-queue assessment in 4; the system operator role, an outage-penalty scheme and a licence-reversion rule in 3 | 20 terms |
| 2. Near-duplicate sentences | the same uptake statistic sentence word for word in two chapters; the same «chapter 2 explains why …» pointer sentence in two chapters | 13 pairs |
| 4. Definition-style re-explanations | «the data hub is …» in 4 chapters, «energy is power times time» 3 times | 6 terms |
| 5. Retold passages | the number of companies in the sector (three counts from different years, and why counts differ) retold in **5** chapters; the voltage levels in 4; a new price scheme's launch and uptake in 4; a tariff mechanism in 3; the revenue-cap formula worked through in 4; a landmark court ruling in both the production and history chapters; subsidy thresholds in both the customer and history chapters | 22 clusters, 7 spanning 3+ chapters |

Sections 1, 2 and 4 catch repeated *terms*. Section 5 catches repeated *stories*, which is where most of the reader's lost time went: whole paragraphs with the same numbers, dates and names in different words. A term registry alone doesn't stop them.

## Why it happens

1. **Writers can't see each other.** Each one writes the complete story of everything its chapter touches.
2. **Rules that invite it.** "Each chapter should be readable on its own" and "explain every abbreviation the first time it appears in each chapter" were both in the reference run's guide. Writers followed them.
3. **Bracket chapters.** The overview chapter previewed every topic in full (formula, counts, source discrepancies), so each was then taught again in its home chapter. History retold today's state, the future chapter restated current numbers with their backstory, and the reader-specific last chapter recapped instead of applying.
4. **Seam topics without an owner.** Some stories belong naturally to two chapters (a court ruling: production or history? a subsidy: customer or history? the number of companies: grid, actors or the company chapter?). If nobody assigns them, both chapters tell them.
5. **Key numbers travel with their backstory.** Repeating "74 companies" is fine. Repeating what was counted, by whom, and why another source says 79 is not.
6. **QA split by chapter group.** Editors who each own four chapters can't see repetition across groups.

## The recipe

### Before writing (Phase 3)

**The registry has three kinds of rows**, each with exactly one home chapter and one shared line of wording:

| Kind | Examples | What "home" means |
|---|---|---|
| Term | a role, a tariff component, an abbreviation | the only chapter with a margin note or definition sentence |
| Story | a reform, a court case, a price crisis, a launch and its uptake | the only chapter that tells it with dates and details |
| Number backstory | what a key figure counts, its source, why sources disagree | the only chapter that explains the number; others may just use it |

Assign every **seam topic** explicitly. When in doubt, the story goes to the chapter where it changes the reader's understanding of a mechanism, and history gets one sentence and a pointer (or the reverse, but decide).

**Bracket-chapter contracts.** Paste the relevant one into the brief of the writer who owns each of these chapters:

- **Overview / summary chapter.** It is a map. Each topic gets at most two sentences and a pointer to its home chapter. No formulas, no source discrepancies, no worked examples. Margin notes only for terms whose home is this chapter. The master figure carries the detail.
- **History chapter.** Owns events as a sequence. It names today's mechanisms without re-explaining them («the income cap, chapter 6»). Topical chapters mention a historical event in one sentence with a pointer here, unless the registry gives them the story.
- **Future chapter.** Starts from the current numbers by reference («from the 2025 production figure in chapter 3») and spends its words on what changes, why, and how sure anyone is.
- **Reader-specific chapter** («what it means for you»). It applies; it doesn't recap. Every paragraph states a consequence for the reader that no earlier chapter stated. Facts from earlier chapters appear as short references, not retold.

**Entry-point rule** (replaces "each chapter stands alone"). A chapter can be entered from the table of contents: its lead names what it builds on, with chapter numbers. It doesn't re-teach that material.

### While writing (Phase 4)

Each writer's brief lists two sets from the registry:
- **home rows**: terms, stories and number backstories it explains in full;
- **neighbour rows**: rows whose home is elsewhere but which this chapter will touch. For these the writer uses the term plainly, gives one sentence carrying the local point, and adds «see chapter N».

### After writing (Phase 5)

Run `repetition.py`. The consolidation editor works through it in this order: section 5 (stories, the biggest wins), 1 (terms), 4 (reworded definitions), 2 (sentences). Then it reads the bracket chapters last, against everything before them.

**Gates.** Check after consolidation and again before delivery:

| Gate | Pass |
|---|---|
| §1 multi-defined terms | empty, or only cases listed as deliberate in the guide |
| §2 near-duplicate sentences | no pair at 0.70 or above |
| §5 retold passages | no cluster spanning 3+ chapters; in every 2-chapter cluster, one member is the full telling and the other is at most two sentences on the topic (check by eye) |
| Final reviewer | reads cover to cover and finds nothing taught twice |

The script is a work list, not a verdict. Section 5 also links paragraphs that share figures for unrelated reasons (two tables of the same year's data). Read each cluster before cutting.

## Don't overcorrect

- Keep a number where the local argument uses it. Cut the backstory around it.
- One sentence carrying the point, plus a pointer, is the target. A paragraph that is only «see chapters 4, 6 and 9» is a failure too.
- When a cut leaves a sentence unclear, add an apposition of eight words or fewer.
- Merge any detail that only the non-home telling had into the home chapter before deleting it.
