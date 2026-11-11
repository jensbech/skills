# Design system

A report is read for an hour or more, on paper, a laptop or a phone. Its design has two parts with different rules. The **reading layout** (the page, the text column, the headings) is the same in every report, because plain and predictable is what makes long text easy to read. The **subject layer** (the cover, the palette, the figure style, the small components) is designed per report, so that the report still looks like it belongs to its subject.

## 1. The reading layout (fixed)

The skeleton in `assets/style.css` implements it. A design keeps these properties:

| Property | Rule |
|---|---|
| Page | A4, side margins equal, about 27 mm |
| Text column | one column, the full width between the margins (about 156 mm), 70–85 characters a line |
| Body | a text serif or a plain text sans, 10.5–11 pt, leading about 1.5 |
| Headings | above the text they head, left-aligned in the column, in a plain text face: the body family in bold or a neutral sans at normal width, weight 600–700. Chapter title at most 22 pt, section heading at most 14 pt |
| Figures, tables, boxes | inside the column, at its width or narrower |
| Term notes | in the column, directly before the paragraph that uses the term |
| Chapter opener | a strip at most 25 mm high at the top of the column; the chapter title follows directly |

The text column is never narrowed to make room for something beside it. Headings, notes, rails, timelines and decoration all go in the column or stay out of the report.

Faces that fit the heading rule: Source Sans 3, IBM Plex Sans, Public Sans, Libre Franklin, Work Sans, Noto Sans, or the bold of the body serif. Display faces, handwriting and script, condensed or expanded widths, and weights above 700 belong on the cover and nowhere else. Handwriting may label a cover drawing; it doesn't appear in chapters or figures.

A reader holding the PDF on a phone zooms to the column. One column of ordinary type survives that; side columns and small labels don't.

## 2. The subject layer (designed per report)

The design lead fixes these dials for each direction; the orchestrator writes the chosen set into `report/DESIGN.md`.

| Dial | Questions to answer | Range of answers (illustrative, not a menu) |
|---|---|---|
| **Cover concept** | What single image would people who know the subject recognise at once? | master diagram; specimen plate; map; annotated instrument; a scene from the reader's own day |
| **Palette** | What colours are native to the subject's materials, places, instruments or eras? | archival ochres and iron-gall ink for history; chart-paper green and survey red for geology; hospital teal and iodine for medicine; signal yellow and asphalt for transport; rain-jacket yellow and wool navy for a nursery |
| **Figure style** | What diagrams do practitioners of this field draw, and how plain can they be kept? | single-line schematics; route maps; pathway diagrams; flow-of-funds; decision trees; cutaways; a plain timeline; a ladder of steps |
| **Flows / encodings** | Do the figures need a shared code at all? If so, which one to four things recur, and how is each encoded? | colour plus line pattern; line weight; hatching; one signal colour on monochrome; none, when the report has few figures |
| **Type pair** | Which quiet pair from the heading rule suits the subject? | a humanist sans over an old-style serif; one serif family throughout; a neutral sans throughout |
| **Chapter opener strip** | What says "you are here" within 25 mm? | a route-map strip; a timeline ruler; an age scale; a plain number with a rule; nothing |
| **Component treatment** | How do boxes, notes and tables look? | ruled, filled or outlined; a tab label; a tint from the palette. Quiet: no drop shadows, tape, stickers or textures |

### Novelty rule

Read the design log before designing. It lives at `<skill>/artifacts/design-log.md`, a gitignored folder for per-user data (`setup.sh` creates it and prints the path as `DESIGN_LOG`). **The new design must differ from every logged design in cover concept, palette and figure style.** The reading layout is deliberately the same each time; entries in the log made before this rule describe margin rails and display faces that are no longer allowed, so don't copy their grids or type. After delivery, append the new design as one compact entry:

```markdown
## <YYYY-MM> — «<title>» (<subject in a few words>, <lang>, <pages> pp, <tier>, <study|guide>)
- Concept: <one line>
- Cover: … - Palette: … - Figure style: … - Flows: … - Type: … - Chapter opener: … - Components: …
```

Also avoid the generic AI looks regardless of subject:
- a cream background with a terracotta accent;
- near-black with acid green;
- rounded SaaS cards with soft shadows and gradient washes;
- tracked-out all-caps eyebrows above every heading;
- meta lines joined with middle dots;
- monospace used for "data feel".

### How to arrive at the design

1. **Immerse briefly.** List 10–15 concrete artefacts from the subject's world (instruments, documents, maps, signage, materials, uniforms, packaging, historical prints). The cover and the palette come from these, not from abstract adjectives.
2. **Generate the directions asked for** (one to three, by tier). Each fixes every dial and has a one-line concept. Directions differ from each other in cover, palette and figure style.
3. **Render specimens.** For each direction, change the colour tokens and the subject-layer rules in a copy of `style.css`, draw a cover, and render three pages: the cover, a chapter opening with two sections of body text and one figure, and a page with a table, a note box, a lens box and a term note.
4. **Pick on evidence.** First check each direction against the reading layout; one that breaks it is out. Among the rest, choose by how easy a full page of text is to read, how well the cover and palette fit the subject, and how quickly the figure reads. Record the rationale in DESIGN.md.
5. **Quality floor:**
   - every row of the reading-layout table holds;
   - contrast of at least 4.5:1 for text and 3:1 for lines that carry meaning;
   - encodings distinguishable in greyscale (vary the line pattern as well as the colour);
   - chart series that never collide with flow meanings;
   - every character of the output language (Nordic letters, accents, other scripts) supported by the chosen fonts.

   If the `dataviz` skill is available, validate the categorical palette with its script.
6. **Spend boldness on the cover.** One memorable image there. Inside, the palette and the figure style carry the subject, and everything else is quiet.

### What stays fixed in the markup

To keep the pipeline working, keep the **class names** (`chapter`, `chapter-top`, `lead`, `term`, `facts`, `note`, `lens`, `check`, `answers`, `fig`, `half`, `table-frame`, `tab`, `sources`, `glossary`, `l-a…l-d`, `t-*`, `box-*`, `f-*`, `s1…s6`, `map-*`) and the figure viewBox widths: 620 for a figure at column width, 310 for a small one (`fig half`). The flow slots `a–d` are semantic: DESIGN.md and WRITING_GUIDE.md say what each one means in this report, and a report may leave slots unused.

Note: `@page` margin boxes (footer and page number) don't see CSS custom properties, so set their font and colour literally in `style.css`.

## 3. Components and classes

| Component | Markup |
|---|---|
| Chapter | `section.chapter#kNN[data-map][data-short]` > `header.chapter-top` (`span.nr`, `h1`, `p.lead`) |
| Term note | `aside.term` > `b` (+ `span.en`) + text |
| Key figures | `div.facts` > `h4`, `dl` (`dt` number, `dd` text), `span.source-line` |
| Note box | `div.note` > `h4`, `p` |
| Reader-lens box | `div.lens` > `h4`, `p` |
| Check yourself (study) | `div.check` > `h4`, `ol` > `li` (before the sources) |
| Decide (guide) | `div.check.decide` > `h4`, `ol` > `li`; no answers block |
| Answers | `div.answers` > `h4`, `ol` > `li` (after the sources) |
| Figure | `figure.fig(.half)` > `svg`, `figcaption` (`b` number), `span.source-line` |
| Table | `div.table-frame` > `table.tab` (`caption`, `thead`, `tbody`, `td.n` numeric), `span.source-line` |
| Sources | `div.sources` > `h3`, `ol.sources` > `li` |
| Citation | `sup.k` |
| Glossary | `section.chapter.glossary[data-appendix]` > `dl` > `div.letter`, `dt` (`span.en`), `dd` |
| No-wrap span | `span.nb` |
| Cover | `section.cover` (in cover.html) |
| Preface | `section.preface` > `div.main` |

What goes into a figure or a table, and how many a report may have, is decided in `learning-design.md` ("Figures and tables earn their place").

SVG classes: text `t t-s t-xs t-bold t-h t-num`, flow text `t-a t-b t-c t-d`, `t-white`, anchors `mid end`, `halo`; boxes `box box-tint box-dark box-dashed box-a box-b box-c box-d`; lines `l-a l-a-thin l-b l-c l-d l-ink l-thin l-grid l-axis`; fills `f-a f-b f-c f-d f-ink f-grey f-tint f-white`; series `s1…s6`.

**Important:** `style.css` sets `svg text { fill: … }`. CSS beats SVG presentation attributes, so `fill="#fff"` on a `<text>` is ignored. Use classes or inline `style="fill:…"`.

## 4. report.config.json

```json
{
  "title": "How Water Reaches the Tap",
  "lang": "en",
  "footer": "How Water Reaches the Tap",
  "output": "How Water Reaches the Tap.pdf",
  "labels": { "contents": "Contents" },
  "map": {
    "nodes": [
      {"id": "source", "label": "Source"},
      {"id": "treatment", "label": "Treatment"},
      {"id": "network", "label": "Network"},
      {"id": "household", "label": "Household"}
    ],
    "bands": [
      {"id": "money", "label": "Tariffs and money"},
      {"id": "governance", "label": "Rules and oversight"}
    ],
    "views": {
      "overview": ["source", "treatment", "network", "household", "money", "governance"],
      "pricing": ["money", "network", "household"]
    }
  }
}
```

The example is illustrative; each report defines its own stages.

- `map` is optional. Set it to `null` for no "you are here" strip.
- A chapter's `data-map` names a key in `views`. The build draws the map into that chapter's `header.chapter-top`.
- `output` is relative to the report folder. Override it with the `OUT_PDF` environment variable for scratch builds, which is useful while a reviewer is reading the main PDF.

## 5. Cover and preface

- **Cover:** designed per report (see the cover concept dial). It needs the title, a one-sentence subtitle, the audience and date, and one strong image from the subject's world. A display face is allowed here. `assets/cover.html` is only a placeholder. Check that no label collides with a line, and that nothing touches the page edges unless it's deliberately full bleed.
- **Preface** («Before you begin»), one page at most: who it's for, what the reader will be able to do afterwards, how to find their way in, a legend only if the figures share encodings (`fig half`, using `t` not `t-s` so it's legible), the date the report reflects, and a plain statement that it was compiled by Claude from public sources and not reviewed by domain experts. A study report adds the reading routes and how to use the questions.

## 6. Charts

A chart is for a study report whose reader needs to see a magnitude or a trend; `learning-design.md` says when one is justified. When it is, follow the dataviz principles: choose the form by the job (magnitude → bars, change over time → lines or columns, composition → stacked bar, single number → fact box). Use one y-axis, a zero baseline for bars, equal intervals for equal time spans, direct labels, a legend for 2+ series, series colours in fixed order, text in ink colours, and mark conceptual charts as conceptual in the caption. Never let a series colour carry a flow meaning it doesn't have. If a chart uses orange or green for something that isn't flow A or B, recolour it (`s1`, `s4` or `f-grey`).
