# Pitfalls from the reference run, and their fixes

## Rendering and build

- **SVG text colours ignored.** `svg text { fill: … }` in CSS overrides `fill="…"` attributes. The "you are here" map's labels came out invisible (white on black became ink on black). Use classes or `style="fill:…"`.
- **Narrow no-break space (`&#8239;`) prints with almost zero width** in Chromium PDFs ("25309 km", "63,8%"). Use `&nbsp;`. `normalize_numbers.py` converts it.
- **Numbers and units splitting across lines** ("1 / 400 km", "8,6 / %"). Use non-breaking spaces in text (`normalize_numbers.py`), `white-space: nowrap` on numeric table cells, and `span.nb` for count phrases like «74 companies».
- **Table first columns hyphenating** (a long compound split as «Responsib-le»). Use `hyphens: manual` and `min-width` on the first column (already in style.css).
- **Short tables splitting across pages**, with the caption alone at the bottom: `.table-frame:not(:has(tbody tr:nth-child(11))) { break-inside: avoid }` (in style.css).
- **Box borders sliced at page bottoms** (a 1 px top border left behind). `display: inline-block; width: 100%` on boxes (in style.css).
- **Near-empty pages** that hold only the last 1–3 sources of a chapter. Tighten the source list (6.7 pt, line-height 1.26), then re-check. A few remaining short pages at chapter ends are acceptable.
- **Half-empty pages before large figures.** The fix is to move the figure one or two paragraphs later in the HTML. Do this last, once the text is final.
- **Variable Google Fonts embed as Type 3.** This is fine for reading and text extraction, so don't spend time on it.
- **macOS has no `timeout`.** Run long builds with the Bash tool's `run_in_background` instead.
- **Concurrent builds clobber each other.** Only the orchestrator runs build.js. Agents render private test pages. Use `OUT_PDF` for scratch builds while reviewers read the main PDF.
- **Margin notes stacking** pushed one to the next page, away from its term. Keep at least one paragraph between notes, and move a note earlier if needed.

## Content

- **Research notes can be wrong.** The final reviewer caught a historical support scheme described with today's parameters, and a wrong founding year, both copied from a note. Let the final reviewer challenge the notes, correct from solid knowledge when certain, record the correction in the note, and tell the user which corrections came from your own knowledge.
- **Editors can introduce errors.** A first-round editor "fixed" a correct description of a tariff into a wrong one. The fresh final review exists for this reason.
- **Conflicting numbers across chapters** (company counts with different definitions, capacity figures from different sources and years). Resolve centrally in the guide's known-conflicts list, and paste the list into every editor prompt.
- **Facts the user supplied** (a job ad they pasted) are legitimate sources even if they're absent from the notes. Cite them explicitly by name, with URL if there is one. A reviewer flagged them as unsourced, and the fix was attribution, not deletion.
- **Repetition across chapters** is the main reader-experience cost of parallel writers. In the reference run, 20 terms were defined in 2–4 chapters each (the most central role in the industry in four), and whole sentences recurred word for word. The root cause was a guide rule saying «explain every term the first time it appears **in each chapter**», combined with writers who couldn't see each other, and with editors split into chapter groups who couldn't see it either. Term repetition was the smaller half. The larger was **retold stories**: the count of companies in the sector, with its source caveats, appeared in five chapters; a new government price scheme's launch and uptake in four; the regulator's revenue formula worked through in four; a landmark court ruling and a subsidy's thresholds in both a topical chapter and the history chapter. The overview chapter pre-taught everything in full, and the closing «what it means for you» chapter recapped instead of applying. The fix: a registry with terms, stories and number backstories, each with one home chapter, built before writing; explicit contracts for bracket chapters; writers who explain only their home rows; one consolidation editor that reads the whole report with `repetition.py` output (section 5 finds retold passages); and gates that are rerun before delivery. See `repetition.md`.
- **Research-process language leaking into the text** («søkeutdrag», «vi har ikke funnet», «kildene bak rapporten»), especially in chapters built on thin sources. Ban it in the guide and grep for it with check.py.
- **Unreferenced figures and tables.** Require a text reference for each. check.py lists the missing ones.
- **Duplicate figures** (two chapters drew the same chart). Keep the one in the topic's home chapter, and point to it from the other.
- **Chapter cross-references** written before the numbering was final. Put the final numbering in the guide before writing starts.
- **Ambiguous references** like "chapter 7" meaning a chapter of a regulation. Write «chapter 7 of the X regulation».
- **Mechanical substitutions over-match** (e.g. the banned word "landskap" inside «utenlandskapasitet»). Review check.py hits by eye before editing.

## Orchestration

- Launch independent agents in one message. Don't poll; wait for completion notifications.
- Don't read agent transcripts. Read their summaries, and grep the files for specifics.
- Notifications can repeat for agents with lingering timers. Ignore duplicates with no new content.
- Give the user a one-line status when a phase changes, and an honest ETA when asked (a full run took roughly 2.5–3 hours wall-clock with ~25 agents).
