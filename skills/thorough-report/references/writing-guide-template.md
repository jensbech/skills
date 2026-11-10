# Writing guide: {{REPORT TITLE}}

<!-- Orchestrator: copy this to report/WRITING_GUIDE.md and fill in every {{…}}. Delete the language lists that don't apply. Keep "Known conflicts" and the registry current during the project. Write the guide in English; the REPORT is written in {{LANGUAGE}}. -->

You are writing or editing part of «{{REPORT TITLE}}», a PDF in **{{LANGUAGE}}** that someone will learn {{SUBJECT}} from. This guide is binding. Where it and your prompt differ, the prompt wins for your files and this guide wins for everything else.

**Reader:** {{who they are, what they know well, what they don't know at all, why they are reading}}.

**After the report they can:**
{{3–6 OUTCOMES, one per line}}

Today is {{DATE}}.

## Before you write or edit

1. Read this guide in full, then `report/DESIGN.md`, `report/style.css` and `report/chapters/00_example.html` (every component; it is deleted before the final build).
2. Load the avoid-ai-writing rules: invoke the `avoid-ai-writing` skill if you have it, otherwise read `{{SCRATCH}}/aiw/avoid-ai-writing/SKILL.md` and `references/patterns.md`. They are calibrated for English; "Language" below adapts them to {{LANGUAGE}}.
3. Read the research notes you were pointed to in `{{CWD}}/research_notes/{{TITLE}}/`.
4. Before you return, reread every sentence you wrote or changed against "Voice" and "Language" below and fix what you find.

## Chapters (final numbering)

| # | File | Map key | Title (working) | The reader can afterwards |
|---|---|---|---|---|
{{ONE ROW PER CHAPTER, plus "A | 90_glossary.html | – | Glossary | –"}}

Refer to other chapters as "{{chapter word}} N" with these numbers.

## Facts and sources

- Every fact comes from the research notes. Never invent a number, date, name, vendor or mechanism to make a sentence concrete. General knowledge is fine for basic physics, mathematics and definitions.
- Date every number ("in 2025", "as of 1 October 2026").
- When the notes are uncertain, say so once and neutrally ("around", "according to X"), or leave the claim out. When two sources disagree, use the resolution below; explain the disagreement only where that teaches the reader something.
- The reader never hears about the research. Phrases such as "search snippet", "we could not find" or "the sources behind this report" don't appear in the text.
- Citations are `<sup class="k">n</sup>` in the text and a numbered list at the end of the chapter, restarting at 1 in each chapter. Format: `Publisher: Title (year). URL`. Use only URLs from the notes.

### Known conflicts and their resolutions
{{LIST, e.g. "Number of companies: use 74 (2024, incl. X) and 'around 70' (2026); older counts use different definitions."}}

## Voice

Write as a colleague who knows the field well and is explaining it to this reader across a table: calm, exact, concrete, a little dry. {{Register for the language, e.g. "moderately conservative bokmål", "plain British English"}}. Second person is allowed, sparingly.

**Voice sample.** Match its register and rhythm. Its content belongs to the home chapter of its topic.

> {{ABOUT 200 WORDS in {{LANGUAGE}}, written by the orchestrator, explaining one registry concept in the order below}}

**How an explanation is built.** Within a section, go in this order:

1. the case or observation, something the reader can picture, usually the running case;
2. the mechanism: what happens, and who does what;
3. the name: the field's term, introduced once the reader has seen the thing it names;
4. the number, dated, with its size made tangible by one comparison;
5. the consequence: what follows, what goes wrong, or what changes for the running case.

**What good prose here looks like:**

- A sentence says who does what. The subject is a person, an organisation or a physical thing, and the verb is something it does.
- A paragraph makes one point and stops when the point is made. Its length follows its content, so lengths vary.
- Claims are specific: a named source, a dated number, a concrete example.
- Headings are short descriptions in sentence case, without colons.
- Lists hold things that are lists. Reasoning stays in paragraphs.
- Analogies come from the reader's world and appear where they fit exactly. Most pages have none.
- A formula, a bill, a threshold or a procedure is shown once with real numbers worked through.

## Language

**Marks of machine prose.** These are what the avoid-ai-writing catalog looks for, adapted to {{LANGUAGE}}. A reviewer will flag each one:

- three-item lists written by reflex ("fast, secure and efficient");
- "not X, but Y" used as a slogan (fine when it corrects a real misconception);
- a rhetorical question as an opener;
- a last sentence that sums up its own paragraph;
- inflated significance ("a historic milestone") and vague attribution ("experts believe");
- staccato fragments for drama;
- personification ("the market decides", "the grid wants");
- the same opener in chapter after chapter;
- sentences opened with a reflexive connector ({{e.g. "Moreover/Furthermore/Additionally" | "Videre/I tillegg/Dessuten/Samtidig"}}); at most one per paragraph.

**Words to avoid** unless literally precise:
{{PASTE THE LIST FOR THE LANGUAGE FROM BELOW, or build one}}

**Punctuation and emphasis.** At most one dash used as prose punctuation per 1,000 words (ranges such as 2021–2023 don't count); use commas, colons, parentheses or full stops. No bold in body text: `<dfn>` marks a term where it is defined, and bold belongs to components.

**Numbers.** {{FORMAT, e.g. Norwegian: decimal comma, non-breaking space (&nbsp;) as thousands separator and before units and %, "8,7 TWh", "25&nbsp;309 MW", "88&nbsp;%". English: "8.7 TWh", "25,309 MW", "88%".}} Never use `&#8239;`; Chromium prints it with almost no width.

**Terms and spelling.** Use the field's own {{LANGUAGE}} terms, with the English term in parentheses or in the margin note where the field uses it. {{Spelling-variant decisions.}}

### Word list: English
delve, leverage, harness, robust (unless technical), seamless, holistic, groundbreaking, cutting-edge, innovative, game-changer, pivotal, crucial, vital, landscape (metaphor), ecosystem (metaphor), navigate (metaphor), journey (metaphor), tapestry, realm, testament to, plays a key/crucial role, in today's fast-paced world, in an ever-evolving, it's worth noting, it's important to note, needless to say, at the end of the day, in conclusion, overall, let's dive in, let's explore, imagine a world, here's where X comes in, the key to, not only … but also (as reflex), unlock, empower, elevate, foster, underscore, showcase, boasts, serves as.

### Word list: Norwegian (bokmål)
avgjørende, sentral rolle, spiller en viktig/nøkkelrolle, sømløs, robust (unntatt teknisk), helhetlig, banebrytende, innovativ, fremtidsrettet, landskap (metafor), økosystem (metafor), dykke ned i, navigere (metafor), utnytte («leverage»), ryggrad, hjørnestein, puslespill, reise (metafor), drivkraft, i en verden der, i stadig endring, nå mer enn noen gang, det er verdt å merke seg, det er viktig å understreke, kort sagt, alt i alt, oppsummert, la oss se på, tenk deg, her kommer X inn, nøkkelen til, ikke bare … men også (som refleks), spennende, kraftfull. Spelling: kapittelet (not kapitlet), frem (not fram), klokka, plural "-selskaper".

### Other languages
Build the list from the phrases that business and machine prose overuse in that language, not by translating the English list word for word. Add the language's reflexive connectors and its spelling decisions.

## Teach once

Several people are writing chapters at the same time and can't see each other. The registry is how you avoid explaining the same thing twice: every term, story and number backstory has exactly one **home chapter**.

| Kind | Term / story / number | Home | Shared wording (one line) |
|---|---|---|---|
{{40–150 ROWS depending on tier, e.g.
"term | wholesale price zone | 4 | an area with one market price per hour"
"story | the 2021 licence ruling | 3 | the top court voided the licences; new building has stalled since"
"story | running case: the Hansen household | 1 | a detached house using 20,000 kWh a year"
"number | number of operators (three counts, three years) | 5 | the regulator's count; older counts use other definitions"}}

**In the home chapter** you explain the row in full. A term gets its margin note and `<dfn>` at or before its first real use. A story gets its dates, numbers and names. A number gets what it counts, its source and why other sources differ.

**In any other chapter** the row appears as follows:

| Kind | What you write |
|---|---|
| Term | the term, used plainly. If the sentence can't be followed without help, add an apposition of at most eight words or "({{chapter word}} N)". An abbreviation may be expanded in parentheses once per chapter. |
| Story | one sentence carrying the point your argument needs, plus "{{see chapter word}} N" |
| Number | the number with its date, where your argument uses it |

**Starting a chapter.** A reader may arrive from the table of contents. The lead names what the chapter builds on, with chapter numbers, and then starts on new material.

**A term that isn't in the registry.** Define it if it clearly belongs to your chapter alone, and list it in your summary either way so it can be given a home.

### Bracket chapters
{{PASTE the contracts from references/repetition.md for the overview/summary, history, future and reader-specific chapters this report has, with their chapter numbers.}}

## Learning components

**The running case.** {{THE CASE in two or three lines, with its sourced figures.}} Chapter 1 introduces it. Your prompt says what it meets in your chapter. Advance it; don't reintroduce it. Where you do arithmetic on it, show the arithmetic.

**Misconceptions.** Your prompt may name one or two things newcomers get wrong. Each goes in a note box: the mistaken belief, then what is true and why.

**Check yourself** ({{from Standard tier: every chapter | Briefing: one box at the end}}). {{N}} questions that make the reader use the chapter: one "why", one "what if", one that applies the chapter to the running case with numbers the chapter supplied, and from chapter 3 on, one that also needs an earlier chapter. Each answer is one or two sentences and uses only what the report has taught up to that point.

## HTML components

Write plain HTML fragments, one `<section>` per chapter:

```html
<section class="chapter" id="kNN" data-map="KEY" data-short="One line for the table of contents">
  <header class="chapter-top">
    <span class="nr">{{Chapter word}} N</span>
    <h1>Short concrete title</h1>
    <p class="lead">2–3 sentences: what the reader will be able to do after this chapter, and which chapters it builds on.</p>
  </header>
  …
  <div class="check"><h4>{{Check-yourself word}}</h4><ol><li>Question</li>…</ol></div>
  <div class="sources"><h3>{{Sources word}}</h3><ol class="sources"><li>…</li></ol></div>
  <div class="answers"><h4>{{Answers word}}</h4><ol><li>Answer</li>…</ol></div>
</section>
```

| Component | Markup | Limits |
|---|---|---|
| Structure | `<h2>`, `<h3>` | |
| Margin note | `<aside class="term"><b>Term <span class="en">english term</span></b>1–3 sentence definition.</aside>` placed immediately before the paragraph that first uses the term | home terms only; 3–8 per chapter, with at least one paragraph between two notes |
| Key figures | `<div class="facts"><h4>…</h4><dl><dt>1&nbsp;234 km</dt><dd>what it is</dd>…</dl><span class="source-line">Source: …</span></div>` | one per chapter, 3–5 figures |
| Note | `<div class="note"><h4>Short title</h4><p>…</p></div>` | two per chapter; misconceptions and asides |
| Reader lens | `<div class="lens"><h4>{{LENS BOX NAME}}</h4><p>…</p></div>` | one per chapter, only when the point is real |
| Table | `<div class="table-frame"><table class="tab"><caption><b>{{Table word}} N.M</b> …</caption><thead>…</thead><tbody>…</tbody></table><span class="source-line">…</span></div>` | add `wide` to span the margin column; numeric cells get `class="n"` |
| Check yourself | `div.check` before the sources, `div.answers` after them | same number of items in both |

Every figure and table is referred to in the running text ("{{figure word}} 3.1 shows …").

## Figures (inline SVG)

Figures do much of the teaching. They are drawn in **{{VISUAL VERNACULAR from DESIGN.md}}**, and each flow means the same thing everywhere. Later figures zoom into the master figure of chapter 1 and keep its positions and symbols. Look at `report/cover.html` for the symbol vocabulary before drawing.

| Flow | Line class | Box / text / fill classes | Looks like | Meaning in this report |
|---|---|---|---|---|
| A | `l-a`, `l-a-thin` | `box-a`, `t-a`, `f-a` | {{e.g. heavy solid, colour X}} | {{e.g. physical power}} |
| B | `l-b` | `box-b`, `t-b`, `f-b` | {{…}} | {{e.g. money}} |
| C | `l-c` | `box-c`, `t-c`, `f-c` | {{…}} | {{e.g. data}} |
| D | `l-d` | `box-d`, `t-d`, `f-d` | {{…}} | {{…}} |
| Neutral | `l-ink`, `l-thin`, `box`, `box-tint`, `box-dark`, `box-dashed` | | {{…}} | {{e.g. rules, organisations}} |

- Use only these classes. The design lives in `style.css`, so a figure never hard-codes colours, gradients or shadows.
- A figure in the main column is `<figure class="fig"><svg viewBox="0 0 470 H">`; a wide one is `<figure class="fig wide"><svg viewBox="0 0 680 H">`. The viewBox width is 470 or 680, nothing else, so text sizes match across figures.
- Text classes: `t` 11px, `t-s` 9.5px, `t-xs` 9.2px (minimum), `t-bold` 12px, `t-h` 14px, `t-num` 18px. `mid` and `end` set the anchor. Add `halo` to labels that sit on lines.
- Arrowheads are `<marker>` elements in `<defs>` with figure-unique ids (`f7-2-arrow-b`), filled with the flow's colour.
- Leave at least 6 units between text and lines. Estimate about 6 units per character for `t` and 5.3 for `t-s`, and size boxes to fit.
- Charts: one y-axis, a zero baseline for bars, equal scales for equal time spans, thin bars with 2-unit gaps, `l-axis` and `l-grid`, direct value labels, series `s1…s6` in fixed order, a legend for two or more series, text in ink colours. A series colour never borrows a flow's meaning.
- {{Drawing rules specific to this design, e.g. "square corners only", "hatching instead of fills".}}
- Every figure has a caption that says how to read it (`<figcaption><b>{{Figure word}} N.M</b> …</figcaption>`) and a `<span class="source-line">`. Conceptual and illustrative figures say so.

**Check your figures by eye.** Put your chapter in a private HTML page in your own scratch folder that links `file://{{REPORT}}/style.css`, render it to PNG with Playwright (`{{PW}}`), look at the images and fix collisions. The main build belongs to the orchestrator; parallel builds overwrite each other.
