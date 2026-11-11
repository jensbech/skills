---
name: thorough-report
license: CC0-1.0
description: Use when the user wants a thoroughly researched, readable PDF to learn from, study or share, from a 10-page briefing to a 150-page handbook, in any language. Triggers include "comprehensive paper", "full report", "deep dive", "primer", "explainer", "handbook", "study guide", "learning material", "briefing", "industry overview", "everything I need to know about X", "practical guide", "what should I do when", or a request to research a topic properly and deliver a document, even without the words "report" or "PDF", and especially when someone has to learn a new industry, field, technology, market or domain step by step, or needs researched advice for a decision in their own life or work.
---

# Thorough report

The product is a PDF made for one specific reader and what they will do with it. Some readers are studying a field and need a working understanding of it. Others have a situation of their own and need to know what to do. The reader's job is decided in Phase 0 and shapes everything after it. You are the orchestrator, which here means editor-in-chief and art director. You frame the job, plan what is taught where, brief subagents, settle conflicts, choose the design and own the build. Subagents do the reading and the writing, so your context stays free for decisions.

A finished report meets five standards. Each has one home file; read it at the phase named.

| Standard | Meaning | Home | Read at |
|---|---|---|---|
| It serves the reader's job | A study report teaches in dependency order through one running case; a guide is organised by the situation the reader arrives with and answers their question on the first pages. Prose leads; figures and tables are few and each has one message | `references/learning-design.md` | Phase 0 and Phase 2 |
| Each thing is taught once | Every term, story and number backstory has one home chapter; parallel writers don't re-explain each other | `references/repetition.md` | Phase 2 |
| It sounds like one person | One voice across all chapters, free of machine-prose habits | `references/writing-guide-template.md` | Phase 2 |
| Facts are sourced | Every number has a date and a URL that was fetched and compared; nothing is invented to make prose concrete | `references/researcher.md` | Phase 1 |
| It reads easily | One text column and quiet headings in every report; the subject shows in the cover, the palette and the figure style | `references/design-system.md` | Phase 1 |

`references/pitfalls.md` lists rendering and content failures with their fixes. Read it once before the first build.

## The team

Every role is a subagent launched with the Agent tool (`subagent_type: "general-purpose"`). Prompts are in `references/agent-prompts.md`.

**Model per role.** Match the model to the kind of work, and pass it as the Agent tool's `model`:

| Class | Work | Claude Code value |
|---|---|---|
| deep | writes or rewrites reader-facing prose, invents the design, or judges the whole report | the strongest offered (`fable`, else `opus`) |
| standard | searches, checks, compares, extracts, or makes minimal edits | `sonnet` |
| fast | fetches a page and compares it with a quoted claim | `haiku` |

If a class is missing, use the next one up. If the runtime has no model choice, omit the parameter. If the user asks for a cheaper run, writers and revisers are the last roles to move down.

| Wave | Role | Model | Count | Owns (writes) | Returns |
|---|---|---|---|---|---|
| 1 | Researcher | standard | per tier | its note in `research_notes/<title>/` | findings, corrections to the brief, gaps |
| 1 | Design lead | deep | 1 | `report/design/**` | directions, specimen PNGs, recommendation |
| 2 | Source checker | fast | 1 per note | `research_notes/<title>/checks/NN.md` | claims the cited page doesn't support |
| 3 | Writer | deep | 1 per chapter | its chapter file | uncertain or omitted facts, unregistered terms |
| 4 | Consolidation editor | deep | 1 | all chapter files, exclusively | what moved where, gate counts |
| 4 | Visual reviewer | standard | 1 | nothing | figure and table fixes with coordinates |
| 5 | Editor | standard | 1–3, disjoint groups | its chapter group | corrections, contradictions seen elsewhere |
| 5 | Glossary | standard | 1 | `chapters/90_glossary.html` | inconsistencies between chapters |
| 6 | Figure fixer | standard | 1–3, disjoint groups | SVG and tables in its group | per-figure changes |
| 7 | Final reviewer | deep | 1, fresh context | nothing | P0–P2 findings on facts, language, layout |
| 7 | Test reader | standard | 1, fresh context | nothing | where a newcomer got lost; unanswerable questions |
| 8 | Reviser | deep | 1–3, disjoint groups | its chapter group | changes made |

A wave is one message with every agent in it, all in the background. The next wave starts when the previous one's files are free. Five rules keep the team from breaking each other's work:

- **One owner per file at a time.** Partition parallel work by file, and sequence waves that touch the same files.
- **Only you run the main build.** Agents render private test pages in their own scratch folders. While a report-only reviewer reads the PDF, build to a scratch path with `OUT_PDF`.
- **Decisions travel through files.** Content decisions go in `report/WRITING_GUIDE.md`, design decisions in `report/DESIGN.md`. Keep both current; every agent reads them.
- **Read summaries, not transcripts.** Grep files for specifics rather than reading whole chapters. Don't poll; completion notifications arrive on their own, and a repeated notification with nothing new can be ignored.
- **Work while agents work.** Each phase below names what you do during the wait.

Without an Agent tool, run the phases yourself in order with the same files and gates, and tell the user it will take longer.

## Phase 0: Frame

**Ask for depth first**, unless the user already signalled it ("short", "a few pages", "full handbook"; then map it to a tier and say so). Depth sets the agent count, the cost, the time and what the reader ends up holding, so it is the one decision to hand back. Use one AskUserQuestion with the four tiers, your recommendation first and marked "(Recommended)", each option described by what the reader gets and the rough time.

| Tier | Pages | Words | Researchers | Chapters | Figures, at most | Questions per chapter (study) | Glossary | Design directions | Review | Agents / time |
|---|---|---|---|---|---|---|---|---|---|---|
| Briefing | 8–15 | 3–6k | 2–3 | 4–6 short sections | 3 | none; 5 at the end | none | 1 | final reviewer | ~8 / 30–60 min |
| Standard | 25–45 | 10–16k | 3–4 | 6–8 | 8 | 3 | 40–70 terms | 2 | waves 4–8, one of each role | ~18 / 1–1.5 h |
| Comprehensive | 60–90 | 20–30k | 5–6 | 9–11 | 14 | 3–4 | full | 3 | waves 4–8, 2–3 per group role | ~28 / 2–2.5 h |
| Exhaustive | 100–150 | 30–45k | 6–7 | 12–14 | 20 | 4–5 | full, 150+ terms | 3 | waves 4–8, 3 per group role | ~35 / 2.5–3.5 h |

"Chapters" means numbered chapters at every tier; at Briefing they are short. The upper word figure and the figure count are ceilings, and a chapter has at most one table. A guide takes half the figure ceiling, rounded down (at least one), has no check-yourself questions, and has a glossary only from Comprehensive up.

A shorter tier still has to do its job. Cut background and history before mechanisms, key numbers and what is changing now; in a guide, cut background before advice. Merge chapters instead of thinning each one. Source checking and the language audit run at every tier.

**Decide the rest yourself** and state it in one status line. Ask a second question only when the answer changes the research: an ambiguous subject, an unknown jurisdiction, an unknown output language.

- **The reader's job:** study or guide. Read "The reader's job" in `learning-design.md` before deciding. A study reader is learning a field and will explain it. A guide reader has a situation of their own and wants to know what to do; subjects about people, family, health, habits and everyday decisions are nearly always guides, whatever word the user used for the document. For a guide, also name the entry point: what the reader arrives with (an age, a stage, a budget, a decision).
- **Reader:** who they are, what they already know, what they don't.
- **Outcomes:** three to six things the reader will be able to do afterwards (explain a mechanism, read a document of the field, estimate a number, ask the right question in a meeting; in a guide, choose what to start now, know when to get help). Everything later is judged against these.
- **Language:** the user's, unless they say otherwise. These instructions are English; the report follows the user.
- **Date anchor:** today. Every number in the report is dated.
- **Title:** short, in the output language.

Track phases in your task list and give a one-line status at each phase change.

## Workspace and commands

```
research_notes/<title>/        one note per subtopic; checks/ holds source-check results
report/
  report.config.json           title, lang, footer, labels, output, optional chapter map
  DESIGN.md  WRITING_GUIDE.md  the two binding briefs
  style.css cover.html preface.html
  design/                      the design lead's directions and specimens
  chapters/NN_slug.html        one per chapter; 90_glossary.html last
reports/<title>.pdf            delivered copy
```

Create these in the working directory. Run `bash <skill>/scripts/setup.sh <scratch>` once; it installs Playwright with Chromium, clones the avoid-ai-writing rules, creates the design log, and prints `PW_PATH`, `AIW` and `DESIGN_LOG`.

| Task | Command |
|---|---|
| Build (two-pass contents with real page numbers) | `PW_PATH=… node <skill>/scripts/build.js report` |
| Scratch build | the same, prefixed with `OUT_PDF=<scratch>/x.pdf` |
| Repetition work list | `python3 <skill>/scripts/repetition.py report --out <scratch>/repetition.md` |
| Mechanical checks | `python3 <skill>/scripts/check.py report --lang <xx> --pdf <pdf> [--require-check]` |
| Non-breaking spaces in numbers | `python3 <skill>/scripts/normalize_numbers.py report --lang <xx>` |
| Contact sheets of every page | `pdftoppm -r 50 -png <pdf> <dir>/p && PW_PATH=… node <skill>/scripts/contact-sheet.js <dir> <dir>/sheet` |
| One page in detail | `pdftoppm -r 110 -png -f N -l N <pdf> <dir>/z` |

## Phase 1: Research and design (wave 1)

Launch the researchers and the design lead in one message.

**Research.** Split the subject into as many mutually exclusive, jointly complete subtopics as the tier allows. Useful axes for a study report: the technical substrate, the actors and who pays whom, rules and regulators, markets and economics, the end user's experience, the inside of a typical organisation, history, the future, and the reader's own context. For a guide: the areas of the reader's life the decisions fall in, what the authorities advise, what the research supports, and what help exists and when to use it. Give each researcher five to nine specific questions, including "verify X" for anything you are assuming.

**Design.** Write `report/report.config.json`, then brief the design lead with the reader's job, the subject's world and its artefacts, and what kind of figures you expect (the exact list comes in Phase 2).

When the wave returns:

1. Read the research summaries for corrections to your assumptions and for conflicts between notes.
2. **Launch the source checkers (wave 2)**, one per note. They run while you plan. Apply every "differs" verdict to the note and to the guide's known-conflicts list.
3. Look at the design specimens yourself. Reject any that breaks the reading layout in `design-system.md`: a narrowed text column, headings beside the text, a display or handwriting face inside the report. Among the rest, choose the one whose full page of text is easiest to read and whose cover and palette fit the subject. Install it into `report/` (`style.css`, `cover.html`, a specimen chapter as `chapters/00_example.html`, `DESIGN.md`), build, look, and fix the template before writers depend on it.

## Phase 2: Plan what is taught where (you)

This phase decides the report's quality more than any other, because parallel writers can only coordinate through what you write down here. Read `learning-design.md` and `repetition.md`, then copy `references/writing-guide-template.md` to `report/WRITING_GUIDE.md` and fill in every `{{…}}`:

1. **Chapter plan**, with final numbering.
   - *Study:* fundamentals to frontier. Chapter 1 shows the whole system on one page with the master figure. The reader-specific chapter comes last. Briefing and Standard open with a one-page summary, written after the other chapters exist; it is unnumbered, counts towards the words and has no questions.
   - *Guide:* the chapters follow the reader's entry point, one per situation, and each covers the subject's areas in the same order. One closing chapter may hold the principles that cut across situations. The report opens with the start-here page, written after the chapters exist.
   - Add up the chapters' word targets. The sum stays within the tier's words; the cover, contents, preface and source lists add about four pages on top.
2. **Running case**, the per-chapter outcomes, and the **three readers of the entry test**: three concrete people, each with a situation and the question they open the report with.
3. **Figure and table plan.** List every figure and table the report will have, each with the one sentence the reader should take from it. Hold the figures to the tier's ceiling, the tables to one per chapter, and both to the tests in `learning-design.md`; anything without its sentence is cut. Writers draw only what is on this list.
4. **Registry**: every term, story and number backstory, each with one home chapter and one shared line of wording. Check the ladder: no row's home comes after the first chapter that depends on it.
5. **Bracket-chapter contracts** for the overview, summary, start-here page, history, future and reader-specific chapters.
6. **Voice sample**: about 200 words in the report language, written by you, in the section order of the reader's job: for a study report, explaining one registry concept; for a guide, advising on one situation.
7. **Language rules** for the report language, the flow table from `DESIGN.md` if the figures share encodings, and the known conflicts with their resolutions.

Also write `preface.html`, one page at most (in a guide, half a page, since the start-here page follows it): who the report is for, the outcomes, how to find their way in, the legend if there is one, the date, and a plain statement that Claude compiled it from public sources without expert review.

## Phase 3: Write (wave 3)

Launch one writer per chapter in one message (at Briefing, one writer may take up to three sections). Each brief carries the reader's job, the chapter's outcomes, section bullets, word ceiling, its figures and tables from the plan (often none), primary notes, home rows, neighbour rows, its part of the running case, and its bracket contract if it has one.

While they write, finish the cover text. When they return, collect their uncertain facts into the known-conflicts list, assign homes to any unregistered terms they reported, delete `00_example.html`, and build.

## Phase 4: Consolidate (wave 4)

Run `repetition.py`, then launch together:

- the **consolidation editor**, which reads the whole report in order with the work list and leaves each explanation and story only in its home;
- the **visual reviewer**, reading a scratch build. Consolidation doesn't touch figures, so its findings stay valid.

Meanwhile, read the source-check files for anything not yet applied. When the editor returns, rerun `repetition.py` and check the gates in `repetition.md`. Don't go on until they pass. Update the registry if a home moved. At Briefing, do the consolidation yourself against the same gates and skip to Phase 6.

## Phase 5: Edit (waves 5 and 6)

Launch the **editors** on disjoint chapter groups and the **glossary** agent in one message. Each editor gets the known conflicts and the source-check results for its chapters.

Meanwhile, run `check.py` and read its hits by eye before acting; substring matches produce false positives.

When the editors finish, launch the **figure fixers** on the visual reviewer's list, and fix what spans files yourself: duplicate figures, numbers that differ between chapters, spelling variants from the glossary agent's list, global CSS. Then run `normalize_numbers.py` and rebuild.

## Phase 6: Review and revise (waves 7 and 8)

Launch the **final reviewer** and the **test reader** together, both with fresh context. The reviewer checks claims against the notes (about 20 at Briefing, 30 at Standard, 50 or more above), language and layout. The test reader runs the entry test with the three readers from the guide, then reads as the target reader and reports where they got lost and which questions the text doesn't let them answer. At Briefing, the final reviewer does both jobs, the entry test included. A failed entry test is a P0: the fix is usually the start-here page or the summary, sometimes the chapter order.

Triage the findings, then launch **revisers** on disjoint groups, each with an exact numbered list. At Briefing and Standard, one reviser or your own edits may be enough.

- A fact the user supplied (a pasted brief, a job ad, an internal document) is a valid source. Cite it; don't delete it.
- When the reviewer shows a note is wrong, correct the note as well as the chapter.

Then rebuild, rerun `check.py` and `repetition.py` (edits can reintroduce repetition, so the gates apply again), view contact sheets of every page, zoom into figure-heavy pages, and move figures that leave large gaps. Stop when no P0 or P1 finding remains.

## Delivery

Compare the page count with the tier. If it overshoots, trim, starting with figures, tables and boxes the reader could do without; if it undershoots, confirm that every outcome is still served.

1. Copy the PDF to `reports/<title>.pdf` and open it.
2. Append the design to `$DESIGN_LOG` in the format given in `design-system.md`.
3. Tell the user in a few lines what the report contains, how it was checked, and its honest limits: weak sources, corrections made from your own knowledge, and that no domain expert reviewed it. Mention that `report/` holds the editable sources. Don't paste the report into chat.

## Files

- `references/learning-design.md`: the reader's job (study or guide), outcomes, the concept ladder, the running case, section order, when a figure or table earns its place, questions and decide boxes, the entry test and the test reader.
- `references/repetition.md`: why parallel writers repeat each other, how to build the registry, bracket-chapter contracts, the gates.
- `references/writing-guide-template.md`: the brief every writer and editor reads; voice, language rules, teach-once rules, components, figure rules.
- `references/agent-prompts.md`: one prompt per role.
- `references/researcher.md`: research method and note format.
- `references/design-system.md`: the fixed reading layout, the dials designed per report, novelty rule, quality floor, fixed class names, config schema.
- `references/pitfalls.md`: rendering and content failures and their fixes.
- `assets/`: the reading layout and placeholders for the rest (`style.css`, `cover.html`, `preface.html`, `example-chapter.html`).
- `scripts/`: `setup.sh`, `build.js`, `contact-sheet.js`, `check.py`, `normalize_numbers.py`, `repetition.py`.
