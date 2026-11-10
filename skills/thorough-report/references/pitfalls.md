# Pitfalls and their fixes

Failures seen in real runs that aren't covered by a rule elsewhere in the skill.

## Rendering and build

- **SVG text colours ignored.** `svg text { fill: … }` in the stylesheet beats a `fill="…"` attribute, so white labels on dark shapes come out dark. Use classes or `style="fill:…"`.
- **Narrow no-break space (`&#8239;`) prints with almost no width** in Chromium PDFs ("25309 km"). Use `&nbsp;`; `normalize_numbers.py` converts it.
- **Numbers and units splitting across lines** ("1 / 400 km"). Non-breaking spaces in text (`normalize_numbers.py`), `white-space: nowrap` on numeric table cells, and `span.nb` around count phrases such as "74 companies".
- **First table columns hyphenating** long compounds. `hyphens: manual` and a `min-width` on the first column (in the skeleton).
- **Short tables splitting across pages**, caption stranded: `.table-frame:not(:has(tbody tr:nth-child(11))) { break-inside: avoid }` (in the skeleton).
- **Box borders sliced at page bottoms.** `display: inline-block; width: 100%` on boxes (in the skeleton).
- **Near-empty pages** holding the last few sources or answers of a chapter. Tighten the source list (6.7 pt, line-height 1.26) and recheck. A few short pages at chapter ends are acceptable.
- **Half-empty pages before large figures.** Move the figure one or two paragraphs later in the HTML. Do it last, when the text is final.
- **Margin notes stacking** push one onto the next page, away from its term. Keep a paragraph between notes, or move one earlier.
- **Variable Google Fonts embed as Type 3.** Harmless for reading and text extraction.
- **macOS has no `timeout`.** Run long builds with the Bash tool's `run_in_background`.

## Content

- **Research notes can be wrong.** A note described a historical scheme with today's parameters and gave a wrong founding year; both reached the text. Source checkers catch what the cited page contradicts; the final reviewer may challenge the rest. Correct the note along with the chapter, and tell the user which corrections came from your own knowledge.
- **Editors can introduce errors.** A first-round editor "corrected" a right description of a tariff into a wrong one. This is why the final reviewer starts from fresh context.
- **Facts the user supplied** (a pasted job ad, an internal document) get flagged as unsourced because they aren't in the notes. The fix is attribution by name, not deletion.
- **Duplicate figures.** Two chapters draw the same chart. Keep the one in the topic's home chapter and refer to it from the other.
- **Ambiguous references.** "Chapter 7" can mean a chapter of a regulation. Write "chapter 7 of the X regulation".
- **Mechanical checks over-match.** The listed word "landskap" hits inside "utenlandskapasitet". Read `check.py` hits before editing.
- **Thin sources produce research-process language.** Chapters built on weak notes are where "we could not find" leaks in. `check.py` greps for it.
- **Answers that outrun the text.** A check-yourself answer that uses a fact from a later chapter, or from the notes but not the chapter, teaches the reader that the questions are unfair. The test reader catches these.
