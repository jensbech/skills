# Agent prompts

One prompt per role. Fill in the `{PLACEHOLDERS}`, set the Agent tool's `model` to the role's class (SKILL.md, "The team"), and launch every agent of a wave in one message with `run_in_background: true`.

| Placeholder | Meaning |
|---|---|
| `{SKILL}` | absolute path of this skill folder |
| `{CWD}` | absolute working directory |
| `{NOTES}` | `{CWD}/research_notes/<title>` |
| `{REPORT}` | `{CWD}/report` |
| `{GUIDE}` | `{REPORT}/WRITING_GUIDE.md` |
| `{SCRATCH}` | session scratchpad (holds `render/` and `aiw/` from setup.sh) |
| `{DESIGN_LOG}` | the design log path printed by setup.sh |
| `{PW}` | `{SCRATCH}/render/node_modules/playwright` |
| `{LANG}` | output language, e.g. "British English", "Norwegian bokmål" |
| `{READER}` | one-sentence reader profile |
| `{DATE}` | today's date |

Language rules, the teach-once rules, components and figure rules live in the writing guide, which every prose-touching agent reads first. The prompts below add only what is specific to the role and to the agent's own files.

---

## Researcher · standard · wave 1

```
Research {SUBTOPIC} for a report that will teach {SUBJECT} to {READER}. Your note is the only factual basis the chapter writers may use.

First read {SKILL}/references/researcher.md and follow its method and note format.

Key questions:
- {5–9 specific questions: name the numbers and years wanted, and the entities, laws and dates to verify}
- {"verify X" for each assumption the orchestrator is unsure of}

Likely sources: {primary authorities, regulators, statistics offices, official company pages, trade press}

Current as of {DATE}. Terms in {LANG} next to the English ones.

Write the note to {NOTES}/{NN_slug}.md.
Return: the five most important findings, every correction to this brief, notable gaps and conflicts, and the file path.
```

---

## Design lead · deep · wave 1

```
You are the design lead for "{REPORT TITLE}", a long-form PDF in {LANG} about {SUBJECT} for {READER}. Invent a design system grown from this subject, so that someone flipping through could guess the subject before reading a word.

Read {SKILL}/references/design-system.md and follow "How to arrive at the design" step by step; it holds the dials, the novelty rule, the quality floor and the class names that must stay fixed. Then read {DESIGN_LOG} (earlier designs; yours must differ from each on at least 5 of 8 dials), the skeleton in {SKILL}/assets/ (style.css, cover.html, example-chapter.html) and {REPORT}/report.config.json. Load the `frontend-design` and `dataviz` skills if you have them.

Subject context: {3–6 lines: what flows through the subject, its main stages, artefacts or visual traditions already known}.

Produce {N} direction(s):
- {REPORT}/design/DIRECTIONS.md: per direction, a one-line concept and all 8 dials.
- {REPORT}/design/<direction>/: style.css, cover.html with a real cover diagram, and a specimen chapter with one figure that uses the flows, a table, a key-figures box, margin notes, a lens box and a check-yourself box.
- PNGs of the cover and two specimen pages per direction, rendered with Playwright ({PW}). Look at every PNG and fix what is wrong before returning.

Leave {REPORT}/chapters/ and {REPORT}/style.css alone; the orchestrator installs the chosen design.
Return: each direction's one-line concept, your recommendation with its reasons (legibility of long text, fit, how the flows read, memorability), and the absolute PNG paths.
```

---

## Source checker · fast · wave 2 (one per note)

```
Check whether the sources cited in one research note say what the note claims.

Note: {NOTES}/{NN_slug}.md. For each claim under "Cited findings" that carries a number, a date or a proper name, fetch the cited URL and compare. Start with these: {KEY CLAIMS the report will lean on}. Then continue through the note, up to about {40} claims.

Write {NOTES}/checks/{NN}.md as one table:
| Claim as the note states it | URL | Verdict | What the page says (quote, 25 words at most) |
Verdicts: supported / differs / not on page / unreachable.

When a page is unreachable, try one search for the same publisher's current page and note the new URL. Otherwise don't look for replacement sources, and don't edit the note.
Return: the count per verdict, and every "differs" and "not on page" row in full.
```

---

## Writer · deep · wave 3 (one chapter each)

```
You are writing chapter {N} of "{REPORT TITLE}", a {LANG} report that teaches {SUBJECT} to {READER}.

Read {GUIDE} first and do what "Before you write or edit" says. Your primary notes: {NOTES FILES}. Skim {OTHER NOTES} so you don't contradict other chapters.

Your file: {REPORT}/chapters/{NN_slug}.html — id="k{NN}", data-map="{KEY}". Working title "{TITLE}"; improve it if you can. {WORDS} words, within 15 %.

After this chapter the reader can: {1–3 OUTCOMES}.

Sections:
- {per section: what to explain, which numbers, which comparison}
Figures and tables:
- {Figure N.1: what it shows, column or wide, conceptual or data}
- {Table N.1: columns}
Running case: {what the case meets in this chapter and what to show}.
Misconception to correct: {one or two, or "none"}.
Check yourself: {N} questions with answers.

Home rows (explain in full, here only): {ROWS}.
Neighbour rows (homed elsewhere; treat as the guide's "Teach once" table says): {ROWS WITH THEIR CHAPTERS}.
{BRACKET CHAPTERS ONLY — its contract, pasted in full.}

Return: section titles, figures and tables; every fact you were unsure of or left out, with the reason; every term you defined that isn't in the registry.
```

---

## Consolidation editor · deep · wave 4 (alone on the chapter files)

```
You are the consolidation editor for "{REPORT TITLE}" ({LANG}). The chapters were written in parallel by writers who couldn't see each other. Make the report read as if one author wrote it in order, with each term, story and number backstory taught once. While you work, every file in {REPORT}/chapters/ is yours alone.

Read {SKILL}/references/repetition.md, then {GUIDE} (do what "Before you write or edit" says; the registry and the bracket contracts matter most), then the work list {SCRATCH}/repetition.md, then every chapter in order as a reader would.

Work through the list in the order §5, §1, §4, §2. Read each §5 cluster before acting; some share figures for unrelated reasons. For each repeated row:
1. Find its home: the registry's choice, or, if unregistered, the first chapter where a reader in order needs the full explanation.
2. Make the home telling the best and most complete one. Move in any detail that only another chapter had.
3. In every other chapter, reduce it to what the guide's "Teach once" table allows, and remove its margin note there.
4. Reread the sentences around each cut. Where one no longer follows, add an apposition of eight words or fewer.
Then reread the bracket chapters against everything before them and hold each to its contract.

Leave facts, SVG figures, check-yourself boxes and answers as they are. If a cut removes a source's only citation in a chapter, remove the source and renumber that chapter's citations. Keep the HTML valid. The build is the orchestrator's.

When done, run `python3 {SKILL}/scripts/repetition.py {REPORT} --out {SCRATCH}/repetition-after.md` and repeat until the gates in repetition.md pass.
Return: per chapter, what you cut or moved (counts and the notable items); before and after counts for §1, §2, §4, §5; any gate you treat as a deliberate exception, with the reason; every row whose home you changed.
```

---

## Visual reviewer · standard · wave 4 (report-only)

```
Review the figures, tables and page furniture of {PDF PATH}, built from {REPORT}/chapters/*.html with {REPORT}/style.css. Review only; edit nothing in {REPORT}. The text is being edited while you work, so judge what persists: inline SVG figures, tables, boxes, cover, contents, margin notes, typography.

Render pages with `pdftoppm -r 110 -png -f N -l M` into {SCRATCH}/vqa/ and look at them; zoom figures at -r 160. `pdftotext -layout` locates captions.

Look for:
- in figures: text overlapping lines, shapes or other text; clipped labels; labels under about 6.5 pt; boxes too narrow for their text; arrows pointing the wrong way; missing legends; a flow style used against its meaning ({FLOW CONVENTION}); misleading scales; a part of the system drawn in a different place than in the master figure of chapter 1;
- in tables: ugly wrapping, numbers split across lines, a header separated from its body;
- on pages: margin notes overlapping or far from their term, stranded headings, wrong caption numbering, hyphenation and character faults.

You may write a small overlap-check script with Playwright ({PW}) and leave it in {SCRATCH}/vqa/tools/.
Return a numbered list, P0 to P2. Per item: page, figure or table number, file, locator (the SVG <text> content or the caption), what is wrong, and the concrete fix with coordinates.
```

---

## Editor · standard · wave 5 (disjoint chapter groups)

```
You are an independent editor and fact-checker for "{REPORT TITLE}" ({LANG}). Your files, and the only ones you edit: {FILES}.

Read {GUIDE} and do what "Before you write or edit" says; use the avoid-ai-writing rules in edit mode. Then read all notes in {NOTES}/ and the source-check results in {NOTES}/checks/.

1. Facts. Compare every number, date, name and claim in your files with the notes. Where a source check says "differs" or "not on page", the page wins over the note. Correct contradictions; soften or remove what nothing supports. Check that each citation number points to a source that supports the sentence, and check the arithmetic in every worked example and check-yourself answer.
2. Consistency. Apply these resolutions throughout your files: {KNOWN CONFLICTS}.
3. Cross-references. Final numbering: {CHAPTER LIST}. Make every chapter reference correct and replace vague pointers with numbers.
4. Language. Make the smallest edit that removes each mark of machine prose and each listed word, keeping meaning and voice. Normalise spelling as the guide says.
5. Teach once. Repetition has already been consolidated. Add no margin note or definition for a term homed in another chapter, and reduce any re-explanation you still find as the guide's table says.

In SVG, correct text only, at the same length or shorter. Keep the HTML valid. The build is the orchestrator's.
Return: factual corrections (before → after, with the note or check that decided it); doubts you couldn't settle; contradictions you noticed in chapters that aren't yours; the number of language edits per file.
```

---

## Glossary · standard · wave 5

```
Write the glossary appendix of "{REPORT TITLE}" ({LANG}).

Read {GUIDE} and do what "Before you write or edit" says, then {REPORT}/style.css (.glossary rules), then every file in {REPORT}/chapters/. Collect every term in a margin note (aside.term), every <dfn>, and every abbreviation.

Write {REPORT}/chapters/90_glossary.html:
<section class="chapter glossary" id="appendix-a" data-appendix="A" data-short="…"> with a chapter-top header and a <dl> holding, in {LANG} alphabetical order, <div class="letter">X</div> then entries of <dt>Term <span class="en">english or expansion</span></dt><dd>Definition in 1–3 sentences, consistent with the home chapter. {See chapter word} N.</dd> where N is the term's home chapter in the registry. {COUNT} entries. No facts that aren't in the chapters.

Edit no chapter file.
Return: every inconsistency between chapters you noticed (spelling variants, one number stated two ways, differing definitions, wrong chapter pointers), each with file and quote.
```

---

## Figure fixer · standard · wave 6 (disjoint chapter groups)

```
Fix figures (inline SVG) and tables in these files only: {FILES}. Read {GUIDE} ("Figures") and {REPORT}/style.css first. {CSS CHANGES SINCE THE REVIEW, e.g. "t-xs grew from 8.5 to 9.2px; new class .halo"}

Fix list, from an independent review. Read the source before each edit; coordinates may have shifted: {NUMBERED LIST}.

After each change, render the figure to PNG on a private test page ({PW}) and look at it; use {SCRATCH}/vqa/tools/ if it exists. Change text only where a fix requires it, and update the caption if you change what a colour or line means. Keep the HTML valid. The build is the orchestrator's.
Return: per item, what you changed, and anything you couldn't fix.
```

---

## Final reviewer · deep · wave 7 (fresh context, report-only)

```
You are the final, independent reviewer of a finished {N}-page PDF in {LANG}: {PDF PATH}. It teaches {SUBJECT} to {READER}. You didn't write it. Review only. Today is {DATE}.

You have: the PDF (pdftotext -layout; pdftoppm into {SCRATCH}/final/), the source HTML in {REPORT}, the research notes and source checks in {NOTES}/, and {GUIDE}. Load the avoid-ai-writing rules as the guide describes and use them in detect mode.

1. Facts. Check at least {50} concrete claims across all chapters against the notes, weighted towards what a reader will remember and repeat. Include every key-figures box and every check-yourself answer. Flag mismatches, unsupported claims and contradictions between chapters. Flag a note itself when you have solid reason to think it is wrong, and give the reason.
2. Teach once. Run `python3 {SKILL}/scripts/repetition.py {REPORT} --out {SCRATCH}/final/repetition.md`, read it, then read the report in order. List every term explained more than once and every story told in more than one chapter: file, quote, and which chapter should keep it. The same story in different words counts.
3. Language. Quote each mark of machine prose and each sentence a native reader of {LANG} would stumble on, with a rewrite. Say whether the chapters sound like one author.
4. Layout. Every page at low resolution, closer where something looks off: near-empty pages, stranded headings, figures far from their reference, contents page numbers.

Return findings as P0, P1 and P2. Per finding: page, file, quote or locator, the problem, the concrete fix. Close with three to five sentences of overall assessment.
```

---

## Test reader · standard · wave 7 (fresh context, report-only)

```
You are {READER}. You have been handed a report, "{REPORT TITLE}", and you will read it once, in order, to learn {SUBJECT}.

Read only {PDF TEXT PATH} (the PDF as text). Open nothing else: no notes, no source files, no web. Where you know more about the subject than {READER} would, set that aside and go by what the text has told you so far.

Chapter by chapter, note:
1. Lost here: each sentence that uses a term or idea the text hasn't yet taught. Quote and page.
2. Taught twice: anything explained that an earlier chapter already explained.
3. Check yourself: answer each question from the text alone before reading the answers. Mark each one "answerable", "the text doesn't let me answer", or "the answer disagrees with the text".
4. In one sentence, what the chapter taught you. Say so if you can't.

At the end: for each outcome listed in the preface, can you now do it? Yes, partly or no, with the reason. Then name the three places where the report lost you most.

Return findings as P0, P1 and P2. Per finding: page, quote, the problem, and what would have helped (an earlier explanation, an apposition, an example, a figure).
```

---

## Reviser · deep · wave 8 (disjoint chapter groups)

```
You are revising chapters of "{REPORT TITLE}" ({LANG}) after independent review. Your files, and the only ones you edit: {FILES}.

Read {GUIDE} and do what "Before you write or edit" says. Facts come from the notes in {NOTES}/; the only additions allowed are the corrections marked below. Chapter numbering: {CHAPTER LIST}.

Findings to fix: {NUMBERED, FILE-SPECIFIC LIST — the exact text quoted, the intended fix, P0s marked; for repetition, the chapter that keeps the topic; for "lost here", whether to add an apposition or a pointer}.

Make targeted edits and leave the rest of each chapter as it is. Where a fix removes a source's only citation, remove the source and renumber. Keep the HTML valid. The build is the orchestrator's.
Return: per finding number, what you changed, or why you didn't.
```
