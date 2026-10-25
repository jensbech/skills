#!/usr/bin/env python3
"""Find cross-chapter repetition in a thorough-report build. Report-only.

Detects:
  1. Terms DEFINED in more than one chapter (margin notes <aside><b>Term</b>…, and <dfn>Term</dfn>).
  2. Near-duplicate sentences across chapters (word-shingle Jaccard similarity).
  3. Facts (number + unit) repeated in many chapters.
  4. Reworded re-explanations: definition-style sentences ("X er …", "X is …", "X betyr …") for the same
     known term in several chapters. Terms come from margin notes, <dfn> and the glossary appendix.
  5. Retold passages: paragraphs in different chapters that tell the same story in different words,
     found by the specific facts they share (numbers, full dates, proper names), clustered by topic.

Usage: python3 repetition.py <report-dir> [--min-chapters 3] [--similarity 0.5] [--retold 3.0] [--out repetition.md]
The output is the work list for the consolidation editor and the final reviewer.
"""
import argparse
import glob
import html as htmllib
import math
import os
import re
from collections import defaultdict

UNITS = r"(?:kWh|MWh|GWh|TWh|kW|MW|GW|kV|Hz|%|øre/kWh|øre|kr/kW|kr|mrd\.?\s?kr|mill\.?\s?kr|km|EUR/MWh|euro/MWh|TWh/år)"


def glossary_terms(report):
    terms = set()
    for f in glob.glob(os.path.join(report, "chapters", "*.html")):
        s = open(f, encoding="utf-8").read()
        if re.search(r'data-(?:appendix|vedlegg)=', s):
            for m in re.finditer(r"<dt[^>]*>([\s\S]*?)</dt>", s):
                terms.add(clean_term(m.group(1)))
    return terms


def chapters(report):
    out = []
    for f in sorted(glob.glob(os.path.join(report, "chapters", "*.html"))):
        s = open(f, encoding="utf-8").read()
        if re.search(r'data-(?:appendix|vedlegg)=', s) or re.search(r'class="[^"]*(?:glossary|ordliste)', s):
            continue
        num = re.search(r"<h1[^>]*>([\s\S]*?)</h1>", s)
        out.append((os.path.basename(f), s, re.sub(r"<[^>]+>", "", num.group(1)).strip() if num else ""))
    return out


def clean_term(t):
    t = re.sub(r"<span[^>]*>[\s\S]*?</span>", "", t)
    t = htmllib.unescape(re.sub(r"<[^>]+>", "", t)).replace("\xa0", " ")
    return re.sub(r"\s+", " ", t).strip(" .:,").lower()


def prose(s):
    s = re.sub(r"<svg[\s\S]*?</svg>", " ", s)
    s = re.sub(r'<div class="(?:sources|kildeseksjon)">[\s\S]*?</div>\s*</section>', " ", s)
    s = re.sub(r"<table[\s\S]*?</table>", " ", s)
    s = re.sub(r"<sup[^>]*>[\s\S]*?</sup>", "", s)
    s = re.sub(r"<[^>]+>", " ", s)
    return re.sub(r"\s+", " ", htmllib.unescape(s).replace("\xa0", " "))


def sentences(text):
    parts = re.split(r"(?<=[.!?])\s+(?=[A-ZÆØÅ0-9«])", text)
    return [p.strip() for p in parts if len(p.split()) >= 8]


def shingles(s, k=4):
    w = re.findall(r"\w+", s.lower())
    return {" ".join(w[i:i + k]) for i in range(max(0, len(w) - k + 1))}


MONTHS = (r"januar|februar|mars|april|mai|juni|juli|august|september|oktober|november|desember|"
          r"January|February|March|April|May|June|July|August|September|October|November|December")
DATE = re.compile(r"\b\d{1,2}\.? (?:" + MONTHS + r") \d{4}\b")
NUMBER = re.compile(r"(?<![\w,.])(\d{1,3}(?:,\d{3})+(?:\.\d+)?|\d{1,3}(?: \d{3})+(?:,\d+)?|\d+(?:[.,]\d+)?)(?!\w)")
SENTENCE_STARTERS = set("""Den Det De Dette Disse Der Når Hvis Som Etter Fra Med For Til Og Men Fordi Også Siden Slik I På Av Et En Hvert
Kapittel Figur Tabell The This These That There When If After From With For And But Because Since In On Of An As
Chapter Figure Table kW MW GW kWh MWh GWh TWh Norge Norway Norwegian""".split())


def paragraphs(s):
    s = re.sub(r"<svg[\s\S]*?</svg>", " ", s)
    s = re.sub(r"<aside[\s\S]*?</aside>", " ", s)
    s = re.sub(r"<sup[^>]*>[\s\S]*?</sup>", "", s)
    s = re.sub(r'<div class="(?:sources|kildeseksjon)">[\s\S]*$', " ", s)
    out = []
    for p in re.findall(r"<(?:p|li|dd)[^>]*>([\s\S]*?)</(?:p|li|dd)>", s):
        t = re.sub(r"\s+", " ", htmllib.unescape(re.sub(r"<[^>]+>", " ", p)).replace("\xa0", " ")).strip()
        if len(t.split()) >= 15:
            out.append(t)
    return out


def fact_tokens(t):
    toks = {"@" + m.group(0) for m in DATE.finditer(t)}
    bare = re.sub(r"\b\d{1,2}\.? (?:" + MONTHS + r")\b", " ", t)
    for m in NUMBER.finditer(bare):
        n = m.group(1)
        if re.fullmatch(r"(?:19|20)\d\d", n) or (n.isdigit() and int(n) <= 10):
            continue
        toks.add("#" + n)
    for m in re.finditer(r"(?<=[\w,;:)] )([A-ZÆØÅ][\wæøåÆØÅ-]{2,})", bare):
        if m.group(1) not in SENTENCE_STARTERS:
            toks.add(m.group(1))
    return toks


def retold_passages(chs, threshold):
    paras = []
    for name, s, _ in chs:
        for t in paragraphs(s):
            paras.append((name, t, fact_tokens(t)))
    spread = defaultdict(set)
    for name, _, toks in paras:
        for x in toks:
            spread[x].add(name)
    n = max(1, len({name for name, _, _ in paras}))

    def weight(x):
        if x[0] == "@":
            return 1.5
        if x[0] == "#":
            v = x[1:]
            return 1.0 if ("," in v or "." in v or " " in v or len(v) >= 3) else 0.8
        return min(1.0, max(0.2, math.log(n / len(spread[x])) / 2))

    parent = list(range(len(paras)))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    links = []
    for i in range(len(paras)):
        for j in range(i + 1, len(paras)):
            if paras[i][0] == paras[j][0]:
                continue
            shared = paras[i][2] & paras[j][2]
            facts = [x for x in shared if x[0] in "#@"]
            if (len(facts) >= 2 or any(x[0] == "@" for x in facts)) and sum(weight(x) for x in shared) >= threshold:
                links.append((i, j, shared))
                parent[find(i)] = find(j)
    clusters = defaultdict(lambda: {"members": set(), "shared": defaultdict(int)})
    for i, j, shared in links:
        c = clusters[find(i)]
        c["members"] |= {i, j}
        for x in shared:
            c["shared"][x] += 1
    out = []
    for c in clusters.values():
        members = sorted(c["members"])
        chapters_in = sorted({paras[i][0] for i in members})
        keys = sorted(c["shared"], key=lambda x: -c["shared"][x])[:8]
        out.append((chapters_in, keys, [(paras[i][0], paras[i][1]) for i in members]))
    out.sort(key=lambda c: (-len(c[0]), -len(c[2])))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("report")
    ap.add_argument("--min-chapters", type=int, default=3)
    ap.add_argument("--similarity", type=float, default=0.5)
    ap.add_argument("--retold", type=float, default=3.0, help="score threshold for section 5 (lower finds more)")
    ap.add_argument("--out")
    a = ap.parse_args()
    chs = chapters(a.report)
    lines = ["# Repetition report", ""]

    # 1. terms defined in several chapters
    defs = defaultdict(list)
    for name, s, _ in chs:
        for m in re.finditer(r"<aside[^>]*>\s*<b>([\s\S]*?)</b>", s):
            defs[clean_term(m.group(1))].append((name, "margin note"))
        for m in re.finditer(r"<dfn[^>]*>([\s\S]*?)</dfn>", s):
            defs[clean_term(m.group(1))].append((name, "dfn"))
    multi = {t: v for t, v in defs.items() if len({n for n, _ in v}) > 1}
    lines.append(f"## 1. Terms defined in more than one chapter ({len(multi)})")
    lines.append("Keep the definition in the term's home chapter; elsewhere use the term plainly (optionally «(see chapter N)»).")
    for t, v in sorted(multi.items(), key=lambda kv: -len(kv[1])):
        lines.append(f"- **{t}**: " + "; ".join(f"{n} ({k})" for n, k in v))
    lines.append("")

    # 2. near-duplicate sentences across chapters
    sents = []
    for name, s, _ in chs:
        for se in sentences(prose(s)):
            sents.append((name, se, shingles(se)))
    index = defaultdict(set)
    for i, (_, _, sh) in enumerate(sents):
        for g in sh:
            index[g].add(i)
    seen, pairs = set(), []
    for i, (n1, s1, sh1) in enumerate(sents):
        cand = defaultdict(int)
        for g in sh1:
            for j in index[g]:
                if j > i:
                    cand[j] += 1
        for j, c in cand.items():
            n2, s2, sh2 = sents[j]
            if n1 == n2 or c < 3:
                continue
            jac = len(sh1 & sh2) / max(1, len(sh1 | sh2))
            if jac >= a.similarity and (i, j) not in seen:
                seen.add((i, j))
                pairs.append((jac, n1, s1, n2, s2))
    pairs.sort(reverse=True)
    lines.append(f"## 2. Near-duplicate sentences across chapters ({len(pairs)})")
    for jac, n1, s1, n2, s2 in pairs[:150]:
        lines.append(f"- {jac:.2f} · {n1}: «{s1[:220]}»\n  ↔ {n2}: «{s2[:220]}»")
    lines.append("")

    # 3. facts repeated in many chapters
    facts = defaultdict(set)
    for name, s, _ in chs:
        for m in re.finditer(r"\b(\d{1,3}(?:[  ]\d{3})*(?:,\d+)?|\d+(?:[.,]\d+)?)\s?" + UNITS, prose(s)):
            facts[re.sub(r"\s+", " ", m.group(0))].add(name)
    rep = {f: n for f, n in facts.items() if len(n) >= a.min_chapters}
    lines.append(f"## 3. Facts appearing in {a.min_chapters}+ chapters ({len(rep)})")
    lines.append("Repeating a key number is fine when it serves the local argument; re-explaining its background each time is not.")
    for f, n in sorted(rep.items(), key=lambda kv: -len(kv[1])):
        lines.append(f"- {f}: {', '.join(sorted(n))}")

    # 4. reworded re-explanations
    known = {t for t in set(defs) | glossary_terms(a.report) if 2 <= len(t) <= 40}
    verbs = r"(?:er|var|betyr|kalles|blir|is|are|means|refers to)"
    expl = defaultdict(list)
    for name, s, _ in chs:
        for se in sentences(prose(s)):
            low = se.lower()
            for t in known:
                if re.match(r"(?:en |et |the |a |an |den |det )?" + re.escape(t) + r"(?:en|et|ene|a)?\s+(?:\([^)]*\)\s+)?" + verbs + r"\b", low):
                    expl[t].append((name, se))
    multi_expl = {t: v for t, v in expl.items() if len({n for n, _ in v}) > 1}
    lines.append("")
    lines.append(f"## 4. Terms explained in a definition-style sentence in several chapters ({len(multi_expl)})")
    lines.append("Usually only the home chapter should explain; others can rely on the term, a short reference, or the glossary.")
    for t, v in sorted(multi_expl.items(), key=lambda kv: -len({n for n, _ in kv[1]})):
        lines.append(f"- **{t}**")
        for n, se in v[:6]:
            lines.append(f"  - {n}: «{se[:200]}»")

    # 5. retold passages
    retold = retold_passages(chs, a.retold)
    wide = sum(1 for c in retold if len(c[0]) >= 3)
    lines.append("")
    lines.append(f"## 5. Retold passages: the same story told in several chapters ({len(retold)} clusters, {wide} spanning 3+ chapters)")
    lines.append("Each cluster is one topic. Keep the full telling in its home chapter; elsewhere keep only the one sentence the local argument needs plus «see chapter N». Sorted by spread.")
    for chapters_in, keys, members in retold:
        lines.append(f"- **{len(chapters_in)} chapters** ({', '.join(chapters_in)}) · shared: {', '.join(k.lstrip('#@') for k in keys)}")
        for name, t in members[:8]:
            lines.append(f"  - {name}: «{t[:200]}»")

    out = "\n".join(lines)
    if a.out:
        open(a.out, "w", encoding="utf-8").write(out)
        print(f"wrote {a.out}: {len(multi)} multi-defined terms, {len(multi_expl)} terms re-explained in prose, {len(pairs)} similar sentence pairs, {len(rep)} repeated facts, {len(retold)} retold-passage clusters ({wide} in 3+ chapters)")
    else:
        print(out)


if __name__ == "__main__":
    main()
