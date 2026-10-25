# How to research a subtopic

You are one of several parallel researchers. Your note will be the **only** factual basis writers may use for their chapters, so precision and honesty about confidence matter more than prose.

## Method

1. Start broad (one or two searches) to map the subtopic, then go to **primary sources**: regulators, statistics offices, official registers, laws, the organisations' own pages and annual reports. Use trade press for recent events and context, and encyclopedias for definitions.
2. Prefer fetching the page itself over trusting a search snippet. If you only saw a number in a snippet, mark it `[snippet]`.
3. Check the newest data. The report's date anchor is "today"; look for this year's and last year's figures, and say explicitly when the newest figure you found is older.
4. When sources disagree, record both with their URLs and, if you can tell, why (different definitions, scope, year, rounding). Don't silently pick one.
5. Time-box: roughly 25–60 tool calls. Breadth across the key questions beats depth on one.
6. If your brief contains an assumption that turns out wrong ("verify X"), say so prominently. These corrections are valuable.

## Note format

Write one markdown file at the path you were given:

```markdown
# <Subtopic> — research note (as of <date>)

## Takeaway
5–10 bullet summary of what a writer must know.

## Cited findings
### <Key question 1>
- Fact, with number and date. — [Source name, year](URL)
- … (native term in parentheses where relevant)

### <Key question 2>
…

## Inferences
Reasoned conclusions that are NOT directly stated by a source, each marked as inference with the reasoning.

## Conflicts between sources
- X says A (URL), Y says B (URL); likely because …

## Gaps
What you looked for and could not verify.

## Diagram suggestions
2–4 figures: what boxes/axes/arrows, what data, why it would help a newcomer.
```

## Rules

- Every number has a date and a URL. No URL, no fact (put it in Gaps instead).
- Use the native-language terms of the subject's home country or field next to English ones. Writers need both.
- Don't write general background from memory unless you label it "general knowledge" (fine for basic physics, maths and definitions).
- Never invent names, figures, products or vendors.
- Return a concise summary to the orchestrator: main findings, corrections to the brief, notable gaps and conflicts, and the file path.
