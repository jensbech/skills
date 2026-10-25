# Design system

## 1. Every report gets its own design system

There is **no house style**. The CSS in `assets/style.css` is a structural skeleton with placeholder tokens so the template renders. Each report needs a design that is novel, distinctive and **derived from its subject**, so that two reports on different topics look like they came from two different studios. Someone flipping through should recognise the subject from the design alone, before reading a word.

### The design dials

Decide every dial for the subject at hand. Write the decisions into `report/DESIGN.md` (the design lead does this; see SKILL.md Phase 2).

| Dial | Questions to answer | Range of answers (illustrative, not a menu) |
|---|---|---|
| **Visual vernacular** | What diagrams do practitioners of this field draw? | single-line electrical schematics; metro/route maps; pathway diagrams; flow-of-funds and T-accounts; legal decision trees; anatomical cutaways; star charts; field-notebook sketches; blueprint orthographics; tidal charts; musical scores |
| **Flows / encodings** | Which 2–4 things move through the subject, and how is each encoded? | colour + line pattern; line weight; hatching textures; shape vocabulary (arrows vs. chevrons vs. dots); monochrome with one signal colour |
| **Palette** | What colours are native to the subject's materials, places, instruments or eras? | archival ochres and iron-gall ink for history; chart-paper green and survey red for geology; hospital teal and iodine for medicine; signal yellow and asphalt for transport; ink-on-blueprint cyan for engineering; dark-room red for photography |
| **Typography** | Which letterforms belong to the field? Pair a body face with one clearly different display or label face. | technical grotesk with wide stretch; old-style serif with small caps; slab serif; humanist sans; condensed industrial; typewriter or monospace for labels, if the field uses forms or code |
| **Page grid** | How does the field lay out its own documents? | wide margin column for notes (scholarly); two-column field guide; single wide column with full-bleed plates (atlas); dense manual with numbered paragraphs (standards body); sidebar timeline (history) |
| **Chapter opener device** | What says "you are here" in this field? | a route-map strip; a depth gauge; a timeline ruler; a periodic-table-like tile; a contour section; a coordinate grid; a plain big number with a rule |
| **Component treatment** | How do boxes, notes, tables and margins look? | ruled vs. filled vs. outlined; corner marks; tab labels; stamped headers; index-card notes |
| **Cover concept** | What single image would the field's insiders recognise instantly? | master diagram; specimen plate; map; annotated instrument; data poster |

### Novelty rule

Read the design log before designing. It lives at `<skill>/artifacts/design-log.md`, a gitignored folder for per-user data (`setup.sh` creates it and prints the path as `DESIGN_LOG`). **The new design must differ from every logged design on at least 5 of the 8 dials.** Don't reuse a logged design even for a closely related subject; change most dials. The log may be empty on a new machine; the rule still applies to the skeleton in `assets/`. After delivery, append the new design as one compact entry:

```markdown
## <YYYY-MM> — «<title>» (<subject in a few words>, <lang>, <pages> pp, <tier>)
- Concept: <one line>
- Vernacular: … - Flows: … - Palette: … - Type: … - Grid: … - Chapter opener: … - Components: … - Cover: …
```

Also avoid the generic AI looks regardless of subject:
- a cream background with a terracotta accent;
- near-black with acid green;
- rounded SaaS cards with soft shadows and gradient washes;
- tracked-out all-caps eyebrows above every heading;
- meta lines joined with middle dots;
- monospace used for "data feel".

### How to arrive at the design

1. **Immerse briefly.** List 10–15 concrete artefacts from the subject's world (instruments, documents, maps, signage, materials, uniforms, packaging, historical prints). Distinctive design comes from these, not from abstract adjectives.
2. **Generate three genuinely different directions.** Each fixes all 8 dials and has a one-line concept («a field naturalist's notebook», «a 1970s transit authority manual», «an engineer's blueprint set»). The three must differ from each other on at least 5 dials.
3. **Render specimens.** For each direction, adapt `style.css` and a cover, and render 2–3 specimen pages: the cover, a chapter opener with a figure, and a page with a table, a fact box and margin notes.
4. **Pick on evidence.** Choose by legibility of long text, fit to the subject, how well the flows read in a figure, and memorability. Don't pick by safety. Record the rationale in DESIGN.md.
5. **Quality floor** regardless of boldness:
   - body text 9–11 pt with comfortable leading;
   - 60–80 characters per line;
   - contrast of at least 4.5:1 for text and 3:1 for lines that carry meaning;
   - flow encodings distinguishable in greyscale (vary the line pattern as well as the colour);
   - chart series that never collide with flow meanings;
   - every character of the output language (Nordic letters, accents, other scripts) supported by the chosen fonts.

   If the `dataviz` skill is available, validate the categorical palette with its script. If the `frontend-design` skill is available, load it in the design lead for typography and layout judgment.
6. **Spend boldness in one place.** One memorable element (usually the cover and the figure style), with everything else quiet and disciplined.

### What stays fixed across designs

To keep the pipeline working, keep the **class names** (`chapter`, `chapter-top`, `lead`, `term`, `facts`, `note`, `lens`, `fig`, `wide`, `table-frame`, `tab`, `sources`, `glossary`, `l-a…l-d`, `t-*`, `box-*`, `f-*`, `s1…s6`, `map-*`) and the viewBox widths 470/680. Values, fonts, layout and even what a class looks like (a `.term` can be an inline index card in a single-column design) are free. The flow slots `a–d` are semantic: DESIGN.md and WRITING_GUIDE.md say what each one means in this report.

Note: `@page` margin boxes (footer and page number) don't see CSS custom properties, so set their font and colour literally in `style.css`.

## 2. Page layout baseline (style.css skeleton)

The skeleton ships A4, margins 20/18/22/22 mm, a 118 mm main column and a 44 mm margin column (`--margin: 0mm` turns it into a single-column layout, in which case restyle `aside.term` as an inline note). Wide figures and tables use `.wide`. Chapters start on a new page. build.js injects the footer text from config, and the page number sits bottom right. All of this may change per design.

## 3. Components and classes

| Component | Markup |
|---|---|
| Chapter | `section.chapter#kNN[data-map][data-short]` > `header.chapter-top` (`span.nr`, `h1`, `p.lead`) |
| Margin note | `aside.term` > `b` (+ `span.en`) + text |
| Key figures | `div.facts` > `h4`, `dl` (`dt` number, `dd` text), `span.source-line` |
| Note box | `div.note` > `h4`, `p` |
| Reader-lens box | `div.lens` > `h4`, `p` |
| Figure | `figure.fig(.wide)` > `svg`, `figcaption` (`b` number), `span.source-line` |
| Table | `div.table-frame(.wide)` > `table.tab` (`caption`, `thead`, `tbody`, `td.n` numeric), `span.source-line` |
| Sources | `div.sources` > `h3`, `ol.sources` > `li` |
| Citation | `sup.k` |
| Glossary | `section.chapter.glossary[data-appendix]` > `dl` > `div.letter`, `dt` (`span.en`), `dd` |
| No-wrap span | `span.nb` |
| Cover | `section.cover` (in cover.html) |
| Preface | `section.preface` > `div.main` |

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

- **Cover:** designed per report (see the cover concept dial). It needs the title, a one-sentence subtitle, the audience and date, and one strong image in the subject's vernacular. `assets/cover.html` is only a placeholder. Check that no label collides with a line, and that nothing touches the page edges unless it's deliberately full bleed.
- **Preface** («Before you begin»): who it's for, how chapters build on each other, how the map works, a legend of the line styles (an SVG at 470 width, using `t` not `t-s` so it's legible), «about the numbers» (date anchor, sources per chapter, check fresh sources before decisions), and a plain statement that it was compiled by Claude from public sources and not reviewed by domain experts.

## 6. Charts

Follow the dataviz principles: choose the form by the job (magnitude → bars, change over time → lines or columns, composition → stacked bar, single number → fact box). Use one y-axis, a zero baseline for bars, equal intervals for equal time spans, direct labels, a legend for 2+ series, series colours in fixed order, text in ink colours, and mark conceptual charts as conceptual in the caption. Never let a series colour carry a flow meaning it doesn't have. If a chart uses orange or green for something that isn't flow A or B, recolour it (`s1`, `s4` or `f-grey`).

## 7. Build and inspection commands

```bash
# build (two-pass TOC); prints chapter → page map
PW_PATH=<scratch>/render/node_modules/playwright node <skill>/scripts/build.js <report-dir>

# scratch build that doesn't overwrite the main PDF
OUT_PDF=<scratch>/test.pdf PW_PATH=… node <skill>/scripts/build.js <report-dir>

# overview contact sheets (8×3 pages per image)
pdftoppm -r 50 -png <pdf> <dir>/p && PW_PATH=… node <skill>/scripts/contact-sheet.js <dir> <dir>/sheet

# detail view
pdftoppm -r 110 -png -f 7 -l 7 <pdf> <dir>/z

# mechanical checks
python3 <skill>/scripts/check.py <report-dir> --lang nb --pdf <pdf>
python3 <skill>/scripts/normalize_numbers.py <report-dir> --lang nb
```
