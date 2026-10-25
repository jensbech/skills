# Writing guide: {{REPORT TITLE}}

<!-- Orchestrator: copy this to report/WRITING_GUIDE.md and fill in every {{…}}. Delete the language sections that don't apply. Keep the "Known conflicts" list updated during the project. Write this guide in English (agents read English reliably); the REPORT is written in {{LANGUAGE}}. -->

You are writing (or editing) part of a PDF report in **{{LANGUAGE}}**: «{{REPORT TITLE}}».

**Reader:** {{READER PROFILE — who they are, what they know well, what they don't know at all, why they're reading}}. The goal is that they understand {{SUBJECT}} step by step: {{THE PATH, e.g. fundamentals → actors → money → rules → data → history → future}}.

Today is {{DATE}}. The report is built by `build.js`, which assembles `report/chapters/*.html` in filename order. The stylesheet is `report/style.css`. Read both, and look at `chapters/00_example.html` for every component (it is deleted before the final build).

## Chapters (final numbering)

| # | File | Map key | Title (working) |
|---|---|---|---|
{{ONE ROW PER CHAPTER, plus "A | 90_glossary.html | – | Glossary"}}

Refer to other chapters as "{{chapter word}} N" using these numbers.

## Facts and sources

- Use ONLY facts from the research notes in `{{CWD}}/research_notes/{{TITLE}}/`. You'll be told which notes are primary for you; read the others for context so you don't contradict other chapters.
- Never invent numbers, dates, names, vendors or mechanisms. If something is uncertain in the notes, say so once ("around", "according to X") or leave it out. If two sources disagree, choose one and briefly explain the discrepancy if that teaches the reader something.
- Date every number ("in 2025", "as of 1 October 2026").
- Citations: `<sup class="k">n</sup>` in the text and a numbered list at the end of the chapter (`<div class="sources"><h3>{{Sources word}}</h3><ol class="sources">…</ol></div>`). Numbering restarts at 1 in each chapter. Format: `Publisher: Title (year). URL`. Use only URLs from the notes.
- **Never describe the research process** in reader text: no "search snippet", "we could not find", "the sources behind this report", "when the sources were collected". If a fact is uncertain, say that once, neutrally.

### Known conflicts and how to resolve them
{{LIST — e.g. "Number of companies: use 74 (2024, incl. X) and 'around 70' (2026); older counts use different definitions." Update during the project.}}

## Language and style (most important)

Write like a knowledgeable colleague explaining the field over lunch: calm, precise, concrete. {{Register notes for the language, e.g. "moderately conservative bokmål", "plain British English"}}. Second person is allowed but use it sparingly.

These rules adapt the avoid-ai-writing catalog (`{{SCRATCH}}/aiw/avoid-ai-writing/references/patterns.md`). Read its sections "Formatting", "Sentence structure", "Words and phrases", "Template phrases" and "Structural issues", and apply the same patterns in {{LANGUAGE}}.

**Banned or near-banned words and phrases.** Use one only when it's literally precise.
{{PASTE THE LIST FOR THE LANGUAGE FROM BELOW, or build an equivalent list for other languages}}

**Transitions:** don't open sentences with reflexive connectors ({{e.g. "Moreover/Furthermore/Additionally" | "Videre/I tillegg/Dessuten/Samtidig"}}). At most one per paragraph, and preferably none.

**Punctuation:** at most one em/en dash used as prose punctuation per 1,000 words (range dashes like 2021–2023 are fine). Use commas, colons, parentheses or full stops. No decorative semicolons.

**Bold:** none in body text. Use `<dfn>` the first time a key term is defined. Bold is reserved for components.

**Patterns to avoid:**
- Reflexive triplets ("fast, secure and efficient"). Let the content decide how many items a list has.
- "Not X, but Y" contrasts used as slogans (fine when correcting a real misconception), and slogan headings like "Roles, not companies".
- Rhetorical questions as openers.
- Closing sentences that summarise the paragraph ("This shows how important…"). Stop when the point is made.
- Significance inflation ("a historic milestone"). Let the numbers show it.
- Vague attribution ("experts believe"). Name the source.
- Staccato fragments for drama ("More power. Less grid. Big choices.").
- Runs of paragraphs of uniform length. Vary length with content.
- Bullet lists where the content is reasoning. Lists are for things that really are lists.
- "X: Y" headings. Headings are short, descriptive, sentence case.
- Personification ("the grid wants", "the market decides"). Say who does what.
- The same opener repeated across chapters ("For an engineer, …").

**Terms:** use the field's native {{LANGUAGE}} terms. Give the English term in parentheses or in a margin note where the field uses it. **Explain each term ONCE in the whole report, in its home chapter** (see the term registry below), before or at its first substantive use. Everywhere else, use the term plainly. The reader has the glossary.

**Numbers:** {{NUMBER FORMAT — e.g. Norwegian: decimal comma, non-breaking space (&nbsp;) as thousands separator and before units and %, "8,7 TWh", "25&nbsp;309 MW", "88&nbsp;%". English: "8.7 TWh", "25,309 MW", "88%".}} Never use `&#8239;` (narrow no-break space); Chromium renders it with almost no width in PDF.

**Teaching:** move from the known to the unknown. Use concrete examples ({{e.g. a house in a named town, a specific product}}). Analogies from the reader's world are welcome where they truly fit, but not on every page. A chapter can be entered from the table of contents: its lead names what it builds on, with chapter numbers, and doesn't re-teach it. **Each term, story and number backstory has one home chapter.** Elsewhere, give the one sentence the local argument needs and "see chapter N" rather than repeating it.

### Banned-phrase list: English
delve, leverage, harness, robust (unless technical), seamless, holistic, groundbreaking, cutting-edge, innovative, game-changer, pivotal, crucial, vital, landscape (metaphor), ecosystem (metaphor), navigate (metaphor), journey (metaphor), tapestry, realm, testament to, plays a key/crucial role, in today's fast-paced world, in an ever-evolving, it's worth noting, it's important to note, needless to say, at the end of the day, in conclusion, overall, let's dive in, let's explore, imagine a world, here's where X comes in, the key to, not only … but also (as reflex), unlock, empower, elevate, foster, underscore, showcase, boasts, serves as.

### Banned-phrase list: Norwegian (bokmål)
avgjørende, sentral rolle, spiller en viktig/nøkkelrolle, sømløs, robust (unntatt teknisk), helhetlig, banebrytende, innovativ, fremtidsrettet, landskap (metafor), økosystem (metafor), dykke ned i, navigere (metafor), utnytte («leverage»), ryggrad, hjørnestein, puslespill, reise (metafor), drivkraft, i en verden der, i stadig endring, nå mer enn noen gang, det er verdt å merke seg, det er viktig å understreke, kort sagt, alt i alt, oppsummert, la oss se på, tenk deg, her kommer X inn, nøkkelen til, ikke bare … men også (som refleks), spennende, kraftfull. Use consistent spelling: kapittelet (not kapitlet), frem (not fram), klokka, plural "-selskaper".

### Other languages
Build an equivalent list by translating the English list into the idioms that are overused in that language's business and AI prose. Add the language's reflexive connectors and its spelling-variant decisions.

## Registry: explain once, refer after

Parallel writers who can't see each other re-explain the same things. This registry prevents that. Every key term, every story and every number backstory has exactly one **home chapter**. In the reference run the worst repetition wasn't terms but stories: the count of companies in the sector, with its source caveats, was retold in five chapters.

| Kind | Term / story / number | Home chapter | One line (the shared wording) |
|---|---|---|---|
{{40–150 rows depending on depth tier, e.g.
"term | wholesale price zone | 4 | an area with one market price per hour"
"story | the 2021 licence ruling | 3 | the top court voided the licences; new building has stalled since"
"number | number of operators (three counts, three years) | 5 | the regulator's count; older counts use other definitions"}}

### Bracket chapters

{{Paste the contracts from references/repetition.md for the overview/summary, history, future and reader-specific chapters that this report has, with their chapter numbers.}}

Rules:
- **In the home chapter:** define the term with a margin note and/or `<dfn>`, and explain it fully. This is the only place it gets a margin note or a definition sentence ("X er …", "X is …").
- **In every other chapter:**
  - Use the term without re-explaining it.
  - If the reader really needs a reminder to follow the sentence, give a short apposition of at most about 8 words in passing, for example «the system operator (the company that keeps supply and demand matched)», or «(see chapter N)».
  - Don't add a margin note, and don't write a definition sentence.
  - An abbreviation may be expanded in parentheses on first use in a chapter, but not explained.
- **Stories and mechanisms** (reforms, court cases, crises, launches, how a tariff or formula works) are told in full only in their home chapter. Elsewhere, write one sentence carrying the point the local argument needs, plus «se kapittel N». A story with dates, numbers and names in a second chapter is a retelling, even in different words.
- **Key numbers** may recur where the local argument needs them, but their background, method, source discrepancies and caveats live in the home chapter only.
- **Don't re-explain abbreviations per chapter.** Expand an abbreviation in parentheses at most once per chapter; never explain it again.
- **If a term you need isn't in the registry**, define it only if you're sure no other chapter will. Otherwise list it in your summary so the orchestrator can assign a home.

## HTML components

Write plain HTML fragments (no `<html>`, `<head>` or `<body>`). One `<section>` per chapter:

```html
<section class="chapter" id="kNN" data-map="KEY" data-short="One line for the table of contents">
  <header class="chapter-top">
    <span class="nr">{{Chapter word}} N</span>
    <h1>Short concrete title</h1>
    <p class="lead">2–3 sentences: what this chapter explains and how it connects.</p>
  </header>
  …
  <div class="sources"><h3>{{Sources word}}</h3><ol class="sources"><li>…</li></ol></div>
</section>
```

- `<h2>` and `<h3>` for structure.
- `<aside class="term"><b>Term <span class="en">english term</span></b>1–3 sentence definition.</aside>`: a margin note, **only for terms whose home is this chapter** (see the registry). Put it immediately BEFORE the paragraph where the term is first used. Use 3–8 per chapter, with at least one paragraph between two notes so they don't stack.
- `<div class="facts"><h4>{{Key figures word}}</h4><dl><dt>1&nbsp;234 km</dt><dd>what it is</dd>…</dl><span class="source-line">Source: …</span></div>`: at most one per chapter, 3–5 figures.
- `<div class="note"><h4>Short title</h4><p>…</p></div>`: an aside or a common misconception. At most 2 per chapter.
- `<div class="lens"><h4>{{LENS BOX NAME}}</h4><p>…</p></div>`: what this means from the reader's own perspective ({{e.g. "Engineer's lens"}}). At most one per chapter, and only when the point is real.
- Tables: `<div class="table-frame"><table class="tab"><caption><b>{{Table word}} N.M</b> …</caption><thead>…</thead><tbody>…</tbody></table><span class="source-line">…</span></div>`. Add `wide` to the frame to span the margin column. Numeric columns get `class="n"`.
- Every figure and table must be referenced in the running text ("{{figure word}} 3.1 shows …").

## Figures (inline SVG)

Figures are the report's signature. They're drawn in **{{VISUAL VERNACULAR from DESIGN.md}}**, with flows that mean the same thing everywhere. Read `report/DESIGN.md` and look at `report/cover.html` for the symbol vocabulary before drawing:

| Flow | Line class | Box / text / fill classes | Looks like (from DESIGN.md) | Meaning in this report |
|---|---|---|---|---|
| A | `l-a`, `l-a-thin` | `box-a`, `t-a`, `f-a` | {{e.g. heavy solid, colour X}} | {{e.g. physical power}} |
| B | `l-b` | `box-b`, `t-b`, `f-b` | {{…}} | {{e.g. money}} |
| C | `l-c` | `box-c`, `t-c`, `f-c` | {{…}} | {{e.g. data / messages}} |
| D | `l-d` | `box-d`, `t-d`, `f-d` | {{…}} | {{e.g. water / nature}} |
| Neutral | `l-ink`, `l-thin`, `box`, `box-tint`, `box-dark`, `box-dashed` | | {{…}} | {{e.g. rules, organisations}} |

Use ONLY these classes. The design lives in `style.css`, so never hard-code colours, gradients or shadows in a figure. Follow the drawing conventions in `report/DESIGN.md` (corner style, symbol vocabulary, label style).

- A figure in the main column is `<figure class="fig"><svg viewBox="0 0 470 H">`. A wide figure is `<figure class="fig wide"><svg viewBox="0 0 680 H">`. ViewBox width MUST be 470 or 680, so that 1 unit ≈ 0.25 mm and text sizes match across figures.
- Text classes: `t` 11px (default), `t-s` 9.5px (secondary), `t-xs` 9.2px (minimum), `t-bold` 12px, `t-h` 14px, `t-num` 18px. `mid` and `end` set the anchor. Add `halo` to labels that sit on gridlines or lines.
- Arrowheads: `<marker>` in `<defs>` with figure-unique ids (`f7-2-arrow-b`), filled with the flow's colour.
- Leave at least 6 units between text and lines. Estimate width at about 6 units per character for `t` and 5.3 for `t-s`, and size boxes to fit.
- Charts: thin bars with 2-unit gaps, `l-axis` axes, `l-grid` gridlines, direct value labels (not on every point if crowded), categorical series `s1…s6` in fixed order, a legend for 2+ series, one y-axis only, a zero baseline for bars, and equal scales for equal time spans. Text uses ink colours, not series colours. Avoid series colours that collide with the flow meanings.
- {{Any drawing rules specific to this design, e.g. "square corners only", "hatching instead of fills for categories", "labels in small caps".}}
- Every figure has a caption explaining how to read it (`<figcaption><b>{{Figure word}} N.M</b> …</figcaption>`) and a `<span class="source-line">` with sources. Mark conceptual or illustrative figures as such.

**Render-check your own figures:** put your chapter in a private HTML page in your own scratch folder linking `file://{{REPORT}}/style.css`, render it with Playwright (`{{PW}}`) to PNG, look at the images, and fix collisions. NEVER run the main build (parallel builds overwrite each other).

## Delivery

Write only the file(s) you were assigned. Return a short summary: sections, figures, tables, and every fact you were unsure of or left out.
