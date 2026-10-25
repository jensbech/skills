---
name: thorough-report
license: CC0-1.0
description: Use when the user wants a thoroughly researched, readable PDF to study or share, from a 10-page briefing to a 150-page handbook, in any language. Triggers include "comprehensive paper", "full report", "deep dive", "primer", "explainer", "handbook", "briefing", "industry overview", "everything I need to know about X", or a request to research a topic properly and deliver a document, even without the words "report" or "PDF", and especially when someone has to learn a new industry, field, technology, market or domain step by step.
---

# Thorough report: research → design → write → verify → PDF

This skill turns "help me understand X properly" into a finished, independently checked PDF that reads as if a knowledgeable human colleague wrote it and looks as if a design studio made it for this subject alone. You are the **orchestrator: editor-in-chief and art director**. You decompose the subject, brief subagents, resolve conflicts, choose the design, own the build, and keep your own context lean by delegating reading and writing.

The method was developed on a 137-page national-industry primer written for a newcomer to that industry ("the reference run"). Its lessons are written into the phases and the reference files below. There is no house look: every report gets a new design.

The reference run's biggest defect was **repetition**: parallel writers taught the same terms and retold the same stories in up to five chapters. Every phase below has a job in preventing that. `references/repetition.md` has the measurements, the causes and the recipe; read it before Phase 3.

## Subagent architecture

All work below the orchestrator is done by subagents via the Agent tool (`subagent_type: "general-purpose"` for every role). Prompt templates for each role are in `references/agent-prompts.md`.

| Phase | Role | How many | Launch | Owns (writes) | Returns |
|---|---|---|---|---|---|
| 1 | Researcher | per depth tier (2–7) | all in ONE message, background | `research_notes/<title>/NN_*.md` | summary, corrections, gaps |
| 2 | Design lead | 1 | same message as researchers, background | `report/design/**` | 1–3 directions (per tier) + specimen PNGs + recommendation |
| 4 | Writer | per tier, 1–2 chapters each | one message, background | its own `chapters/NN_*.html` | summary of uncertain/omitted facts |
| 5 | Consolidation editor | 1, alone | after all chapters, before QA | ALL chapter files (exclusive) | repetition removed, before/after counts per section, home changes |
| 5 | Glossary | 1 (Standard tier and up) | same message as the consolidation editor (it only writes its own file) | `chapters/90_glossary.html` | inconsistency list |
| 6 | Editor | 1–3, disjoint chapter groups | one message, background | its chapter group | corrections, cross-chapter contradictions |
| 6 | Visual reviewer | 1 | same message as editors | nothing (report-only) | P0–P2 layout/figure fixes with coordinates |
| 6 | Figure fixer | 1 | after editors finish | chapters (SVG only) | per-figure changes |
| 7 | Final reviewer | 1, fresh context | after rebuild | nothing (report-only) | P0–P2 findings on facts, reader experience, language, layout |
| 7 | Reviser | 3, disjoint groups | one message, background | its chapter group | changes made |

Rules that keep the team from breaking each other's work:

- **One owner per file at any moment.** Partition by file. Sequence phases that touch the same files.
- **Only the orchestrator runs the main build.** Agents render private test pages in their own scratch folders. When a report-only reviewer is reading the PDF, build to a scratch path (`OUT_PDF=…`).
- **Launch independent agents in one message, in the background.** Don't poll. Wait for completion notifications, and ignore duplicate notifications that carry nothing new.
- **Don't read transcripts or whole chapters yourself.** Read agent summaries, and grep files for specifics. Your context is the project's memory.
- **Broadcast decisions through files.** Content decisions go in `report/WRITING_GUIDE.md` (known conflicts, chapter numbering, home chapter per topic) and design decisions in `report/DESIGN.md`. Paste the key resolutions into every editor and reviser prompt as well.
- If the Agent tool is unavailable, do the phases yourself sequentially with the same artefacts and checks, and tell the user it will take longer.

## Phase 0: Frame (you, a few minutes)

### Ask for the depth first (always, unless the user already stated it)

Depth is the one decision that changes everything downstream: the number of agents, cost, time, and what the reader holds in their hands. A 130-page handbook is excellent when someone has to learn a whole industry. It's the wrong deliverable when they need to grasp a topic before a meeting. So **before any research starts, ask the user to choose a depth tier** with AskUserQuestion. Put your recommendation first, based on the request, and mark it "(Recommended)":

| Tier | Pages | Words | Researchers | Chapters | Figures | Glossary | Design directions | QA | Agents / time |
|---|---|---|---|---|---|---|---|---|---|
| **Briefing** | 8–15 | 3–6k | 2–3 | 4–6 short sections | 3–5 | none (terms in margin notes only) | 1 | mechanical checks + 1 final reviewer | ~6 / 30–60 min |
| **Standard** | 25–45 | 10–16k | 3–4 | 6–8 | 8–14 | short (40–70 terms) | 2 | 1 editor round + final reviewer | ~12 / 1–1.5 h |
| **Comprehensive** | 60–90 | 20–30k | 5–6 | 9–11 | 15–25 | full | 3 | 2 rounds (editors, visual, final) | ~20 / 2–2.5 h |
| **Exhaustive** | 100–150 | 30–45k | 6–7 | 12–14 | 25–35 | full (150+ terms) | 3 | 2 rounds + revision | ~25 / 2.5–3.5 h |

The reference run was *Exhaustive* (137 pages).

How to phrase the question. Use one AskUserQuestion with these four options, each with a one-line description of what the reader gets and the rough time. For example: "Standard: 25–45 pages, the whole picture with the key numbers and figures, about 1–1.5 h". You may add a second question in the same call if something else is really undecided (output language, or which angle matters most). Don't ask about things you can decide yourself.

If the user already said something like "short", "a few pages" or "full handbook", map it to a tier, state your choice in the status line, and don't ask.

**Shorter is not just "fewer pages".** At the lower tiers, the report must still communicate everything the reader needs:
- Open with a one-page summary ("the whole thing in five minutes"). This is required for Briefing and Standard, and recommended for all tiers.
- Cut background and history first; keep the mechanisms, the key numbers and what is changing now.
- Prefer fewer, stronger figures. The master figure that shows the whole system is never cut.
- Merge chapters rather than thinning every one. Each chapter still needs its point, its numbers and its sources.
- QA intensity scales down, but fact-checking against the notes and the anti-AI-writing audit never drop out.

### Then decide the rest yourself

Infer, don't interrogate. People asking for this usually want you to "make all decisions yourself". Beyond depth, ask only if the answer changes the research itself: an ambiguous subject, an unknown jurisdiction, or an unknown output language. Otherwise decide, and state the decisions in one status line:

- **Reader**: who they are, what they know, what they don't. This drives analogies, depth and the per-chapter "lens" box. A software engineer new to an industry, for example, gets its central data hub explained as "a message bus" and a short "engineer's lens" box per chapter.
- **Purpose**: understanding a field (default), preparing a decision, or onboarding.
- **Language**: the user's language unless they ask otherwise. These instructions are English; the report follows the user.
- **Date anchor**: today. Every number in the report is dated.
- **Depth tier**: as chosen above. Every later phase reads its numbers from the tier table. Give an honest ETA whenever asked.
- **Title**: short, in the output language.

Track phases with your task list, and give a one-line status at each phase change.

## Workspace

```
research_notes/<title>/        one note per subtopic
report/
  report.config.json           title, lang, footer, labels, output, optional chapter map
  DESIGN.md                    the chosen design system (written in Phase 2)
  WRITING_GUIDE.md             binding brief for writers/editors (Phase 3)
  style.css cover.html preface.html
  design/                      the design lead's directions and specimens
  chapters/NN_slug.html        one per chapter; 90_glossary.html last
reports/<title>.pdf            delivered copy
```

Create these in the current working directory, not /tmp. Run scripts from this skill's `scripts/` by absolute path. First run `bash <skill>/scripts/setup.sh <scratchpad>`, which installs Playwright/Chromium, clones the avoid-ai-writing rules, creates the design log if it's missing, and prints `PW_PATH` and `DESIGN_LOG`. Reports and design specimens live in the working directory. The only thing the skill writes into its own folder is `artifacts/` (gitignored), which holds the design log. Read `references/pitfalls.md` once before starting.

## Phase 1: Research, and Phase 2: Design (launched together)

**Research.** Decompose the subject into as many mutually exclusive, collectively exhaustive subtopics as the tier allows (2–3 for Briefing, up to 7 for Exhaustive). At the lower tiers each subtopic is broader and the questions focus on mechanisms, key numbers and current changes that follow the reader's path. Useful axes: the technical substrate, actors and who pays whom, rules and regulators, markets and economics, the end user's experience, the inside of a typical organisation and its data/IT, history, the future, and the reader's own context (their employer or project). Each researcher reads `references/researcher.md` and returns a note with dated numbers, URLs, native terminology, conflicts, gaps and diagram suggestions. In their summaries, look for **corrections to your assumptions** and for conflicts between notes. Notes are the primary source but not infallible. Let the final reviewer challenge them, and append any correction to the note.

**Design.** Read `references/design-system.md`. Write `report/report.config.json` (with the chapter map stages if the design will use a map). Launch the **design lead** in the same message as the researchers. Give it the subject context: what flows through the subject, its main stages, and its artefacts and visual traditions. It invents the tier's number of directions (1 for Briefing, 2 for Standard, 3 above), grown from the subject. A single direction must still be novel and pass the novelty rule. Each fixes 8 dials: vernacular, flow encodings, palette, typography, grid, chapter-opener device, component treatment, and cover concept. Each must differ from every entry in the design log (`$DESIGN_LOG` from setup.sh) on at least 5 dials. It renders specimen pages for each direction and recommends one.

When it returns, **look at the specimen PNGs yourself** and choose. Don't choose the safest; choose the one that fits the subject, keeps long text legible, makes the flows read clearly, and is memorable. Then:

1. Install the choice into `report/`: `style.css`, `cover.html`, a specimen chapter as `chapters/00_example.html`, and `DESIGN.md` with the concept, dials, flow meanings and drawing rules.
2. Build and look at the result. Fix the template before writers depend on it.
3. Write `preface.html` (how to read the report, the flow legend, the date, and a statement that Claude compiled it from public sources without expert review).

If the `frontend-design` or `dataviz` skills exist, the design lead loads them. You may too, when judging.

## Language quality: avoid-ai-writing at every prose step

The report must read as if a person wrote it. The avoid-ai-writing rules (https://github.com/conorbronsdon/avoid-ai-writing; `setup.sh` clones them to `<scratch>/aiw/`) apply at **every step where prose is produced or changed**:

| Step | Who | How |
|---|---|---|
| Writing guide | you | translate the patterns into the target language and add the banned-phrase list (Phase 3) |
| Front matter | you | write cover text and preface under the same rules, then self-audit |
| Chapters and glossary | writers, glossary agent | read the catalog (or invoke the skill) before writing; self-audit before returning |
| QA round 1 | editors | full audit plus minimal in-place edits (edit mode) |
| Mechanical | you | `check.py` flags banned phrases, dashes, reflexive openers, bold, research-meta |
| Final review | final reviewer | detect pass across the whole PDF, plus a verdict on naturalness |
| Revision | revisers | same rules for every sentence they touch |

If a skill named `avoid-ai-writing` is installed, agents invoke it with the Skill tool. Otherwise they read the cloned `SKILL.md` and `references/patterns.md`. The catalog is calibrated for English, so the guide must carry a language-specific adaptation for other languages (a Norwegian bokmål one is included in the template).

## Phase 3: Writing guide (you)

Copy `references/writing-guide-template.md` to `report/WRITING_GUIDE.md` and fill in every `{{…}}`:

- the reader;
- the final chapter table with numbers and map keys;
- the **registry** (40–150 rows depending on tier) with three kinds of rows: **terms**, **stories** (reforms, cases, crises, launches) and **number backstories** (what a key figure counts and why sources differ). Each row gets ONE home chapter and one shared line of wording. Build it from the research notes and the chapter plan. Assign seam topics, which naturally belong to two chapters, explicitly. Writers explain only their home rows; everyone else uses them plainly with a pointer. This is the main defence against repetition, because parallel writers can't see each other;
- the **bracket-chapter contracts** from `references/repetition.md` (overview, history, future, reader-specific chapter), so those chapters map, sequence, project and apply rather than re-teach;
- the flow table, from DESIGN.md;
- language rules (the banned-phrase list for the language, with the avoid-ai-writing patterns transferred to it) and number formatting;
- **known conflicts** with resolutions, taken from the research summaries.

Keep this file current. It's how decisions reach every agent.

## Phase 4: Chapters (writers)

Plan the tier's number of chapters from fundamentals to frontier, with the reader-specific chapter last. For Briefing and Standard, chapter 0 is a one-page summary («the whole thing in five minutes»), written last by you or a writer once the other chapters exist. Briefing "chapters" are short sections (500–1 000 words each), and one writer may take three of them. Chapter 1 shows "the whole system on one page" with a master figure that later chapters zoom into. Reference sequence: overview → physics → production → grid → actors → regulation → market → customer → inside a company → data & security → history → future → what it means for you.

Brief each writer (§ Writer) with:
- the chapter id and map key;
- the word target;
- section bullets;
- the expected figures and tables;
- which notes are primary;
- **its home rows** from the registry (terms, stories, number backstories). These are the only ones it explains;
- **its neighbour rows**: rows homed elsewhere that this chapter will touch. For these it writes one sentence carrying the local point plus «see chapter N»;
- for a bracket chapter (overview, summary, history, future, reader-specific), its **contract** from `references/repetition.md`, pasted in full.

Launch all writers in one message. A chapter whose note isn't ready yet starts when it is. While they work, you write the cover text and finish the front matter. Their summaries of uncertain facts become your QA conflict list. When all are done, delete `00_example.html`.

## Phase 5: Assemble and glossary (glossary from Standard tier up)

Build with `PW_PATH=… node <skill>/scripts/build.js report`. It prints the page count and a TOC map, and runs a two-pass TOC with real page numbers.

**Consolidate before anything else.** Run `python3 <skill>/scripts/repetition.py report --out <scratch>/repetition.md`. It finds terms defined in several chapters, near-duplicate sentences, repeated facts, reworded re-explanations, and (section 5) **retold passages**: the same story told in different words, found by the numbers, dates and names the paragraphs share. Even with the registry, parallel writers repeat each other: the reference report had 20 terms defined in 2–4 chapters and 22 retold stories, one of them in five chapters. Then launch, in one message:
- the **consolidation editor** (§ Consolidation editor). It is ONE agent with exclusive ownership of all chapters. It reads the whole report in order and keeps each explanation and each story only in its home chapter;
- the **glossary agent** (§ Glossary), which only writes its own file. Its inconsistency list (spelling variants, the same number stated differently, wrong chapter pointers) is one of the most useful QA inputs.

Rerun repetition.py afterwards and check the **repetition gates** in `references/repetition.md`: section 1 empty (or deliberate), no section 2 pair at 0.70 or above, no section 5 cluster spanning three or more chapters, and every remaining two-chapter cluster reduced to one full telling plus a short reference. Don't start QA round 1 until they pass. Update the registry if homes changed. For Briefing reports the orchestrator may do the consolidation itself, with the same gates.

## Phase 6: Independent QA, round 1 (Standard tier and up; Briefing goes straight to the mechanical checks and Phase 7)

Launch these in one message:
- **3 editors** (§ Editor), on disjoint chapter groups: fact-check against the notes, enforce the known-conflict resolutions, fix cross-references, run the language audit, edit in place, and report contradictions they see elsewhere.
- **The visual reviewer** (§ Visual reviewer), report-only: figures, tables, cover, contents, margin notes.

At the same time, run the mechanical checks yourself:

```bash
python3 <skill>/scripts/check.py report --lang <xx> --pdf <pdf>     # banned phrases, prose dashes, research-meta, bold, unreferenced figures/tables, citations, near-empty pages
python3 <skill>/scripts/normalize_numbers.py report --lang <xx>     # non-breaking spaces in numbers/units (only once editors are done)
```

Then fix what spans files yourself: duplicate figures, cross-chapter numbers, spelling normalisation, global CSS. Send chapter-level figure fixes to the **figure fixer** (§ Figure fixer). Review check.py hits by eye before acting, because substring matches give false positives.

## Phase 7: Final review and revision

Rebuild. Launch a **fresh final reviewer** (§ Final reviewer). It checks claims against the notes (about 20 for Briefing, 30 for Standard, 50+ above), plus reader experience, language and layout. At the Briefing and Standard tiers, you can apply the fixes yourself or with one reviser instead of three.

Triage its findings:
- Facts the user supplied directly (a pasted brief, job ad or internal document) are valid sources. Cite them; don't delete them.
- Fix factual P0s carefully, and record corrections in the notes.

Launch **revisers** (§ Reviser) on disjoint groups, each with an exact numbered list of findings. Usual themes:
- repetition across chapters (keep the home chapter, reduce the rest to one line plus a reference);
- research-process language leaking into the text;
- jargon used before it is defined;
- "X: Y" headings;
- unreferenced figures.

Then:
1. Rebuild and rerun check.py and repetition.py. The repetition gates must still pass, because revisers and editors can reintroduce repetition.
2. Make contact sheets of every page (`pdftoppm -r 50` + `scripts/contact-sheet.js`) and zoom in on the figure-heavy pages (`pdftoppm -r 110`).
3. Move figures that leave large gaps.

Stop when no P0 or P1 findings remain.

## Delivery

Check that the page count matches the tier. If it overshoots a lot, trim before delivering. If it undershoots, make sure nothing the reader needs is missing.

1. Copy the PDF to `reports/<title>.pdf` and open it.
2. Append the design to `$DESIGN_LOG` (8 dials, one compact entry, format in `references/design-system.md`), so the next report looks different. The log lives in the skill's gitignored `artifacts/` folder, so it stays per user and never reaches the published skill.
3. Tell the user, in a few lines:
   - what the report contains: pages, chapters, figures, glossary, and the design concept in one phrase;
   - how it was checked;
   - **honest caveats**: weak sources, any corrections made from your own knowledge, and that no domain expert has reviewed it.

   Mention that `report/` holds the editable sources. Don't paste the report into chat.

## Principles

- **Design grows from the subject.** Look for its artefacts, its diagram dialect and its materials. Two reports should never look like siblings unless they share a subject.
- **Teach each thing once.** One home chapter per term, story and number backstory, decided before writing, enforced by one consolidation pass that reads everything and by gates that are rerun before delivery. Later chapters build on earlier ones instead of starting over. Overview and closing chapters map and apply; they don't re-teach.
- **Separate verified from inferred**, and state uncertainty once, neutrally, never as a story about the research process.
- **Never invent specifics** (numbers, names, vendors, features) to make prose concrete.
- **Look at the output** after every structural change, because validators don't see layout.
- **Write for the reader's mental model.** Use analogies from their world where they really fit, and at most one lens box per chapter.

## Reference files

- `references/agent-prompts.md`: prompts for every role (researcher, design lead, writer, glossary, editor, visual reviewer, figure fixer, final reviewer, reviser).
- `references/researcher.md`: research method and note format.
- `references/design-system.md`: design dials, novelty rule, quality floor, fixed class names, config schema, build commands.
- `references/writing-guide-template.md`: WRITING_GUIDE.md template with banned-phrase lists (English, Norwegian) and component and figure rules.
- `references/repetition.md`: how repetition arose in the reference run (measured), the registry and bracket-chapter recipe, and the gates.
- `references/pitfalls.md`: concrete failures and fixes from the reference run.
- `assets/`: `style.css` (token-driven skeleton), `cover.html`, `preface.html`, `example-chapter.html` (placeholders, not a house style).
- `scripts/`: `setup.sh`, `build.js`, `contact-sheet.js`, `check.py`, `normalize_numbers.py`, `repetition.py` (cross-chapter repetition finder: terms, sentences, facts, re-explanations, retold passages).
