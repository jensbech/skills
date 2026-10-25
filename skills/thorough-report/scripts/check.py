#!/usr/bin/env python3
"""Mechanical checks for a thorough-report build. Report-only; review hits by eye before editing
(substring matches can be false positives, e.g. 'landskap' inside 'utenlandskapasitet').

Usage: python3 check.py <report-dir> [--lang en|nb] [--pdf <file.pdf>] [--extra "word1,word2"]
"""
import argparse
import glob
import os
import re
import subprocess

BANNED = {
    "en": r"delve|leverage|harness|seamless|holistic|groundbreaking|cutting-edge|innovative|game-changer|pivotal|crucial|"
          r"landscape|ecosystem|navigat\w+|tapestry|realm|testament to|plays? a (?:key|crucial|vital|pivotal) role|"
          r"fast-paced|ever-evolving|it'?s worth noting|it'?s important to note|needless to say|at the end of the day|"
          r"in conclusion|let'?s dive|let'?s explore|imagine a world|the key to|not only|unlock|empower|elevate|foster|"
          r"underscore|showcase|boasts|serves as",
    "nb": r"avgjørende|sentral rolle|viktig rolle|nøkkelrolle|sømløs|helhetlig|banebrytende|innovativ|fremtidsrettet|"
          r"landskap|økosystem|dykke ned|navigere|ryggrad|hjørnestein|puslespill|drivkraft|i en verden der|"
          r"i stadig endring|nå mer enn noen gang|verdt å merke|viktig å understreke|kort sagt|alt i alt|oppsummert|"
          r"la oss|tenk deg|nøkkelen til|ikke bare|spennende|kraftfull|kapitlet",
}
OPENERS = {
    "en": r"(?:^|[.!?]\s+)(?:Moreover|Furthermore|Additionally|In addition|Notably),",
    "nb": r"(?:^|[.!?]\s+)(?:Videre|I tillegg|Dessuten|Samtidig),",
}
META = {
    "en": r"search snippet|snippet|we (?:could not|couldn't|did not) find|the sources behind|when the sources were|"
          r"our assessment|not found in (?:the|our) (?:notes|sources)",
    "nb": r"søkeutdrag|vi har ikke funnet|kildene bak|da kildene ble|vår vurdering|ikke funnet i kildene|kildene vi har brukt",
}
FIG_WORD = {"en": ("Figure", "Table"), "nb": ("Figur", "Tabell")}


def text_of(html):
    html = re.sub(r"<svg[\s\S]*?</svg>", " ", html)
    html = re.sub(r'<div class="sources">[\s\S]*?</div>', " ", html)
    return re.sub(r"<[^>]+>", " ", html)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("report")
    ap.add_argument("--lang", default="en")
    ap.add_argument("--pdf")
    ap.add_argument("--extra", default="")
    a = ap.parse_args()
    lang = a.lang if a.lang in BANNED else "en"
    banned = BANNED[lang] + ("|" + "|".join(map(re.escape, a.extra.split(","))) if a.extra else "")
    fig, tab = FIG_WORD.get(lang, FIG_WORD["en"])

    files = sorted(glob.glob(os.path.join(a.report, "chapters", "*.html")))
    for f in files:
        html = open(f, encoding="utf-8").read()
        t = text_of(html)
        words = len(t.split())
        hits = sorted(set(m.group(0).lower() for m in re.finditer(banned, t, re.I)))
        dashes = len(re.findall(r"\s[–—]\s", t))
        openers = len(re.findall(OPENERS.get(lang, OPENERS["en"]), t))
        meta = sorted(set(m.group(0) for m in re.finditer(META.get(lang, META["en"]), t, re.I)))
        bold = len(re.findall(r"<(?:b|strong)>", re.sub(r'<(aside|div class="(?:facts|note|lens)")[\s\S]*?</(?:aside|div)>|<caption>[\s\S]*?</caption>|<figcaption>[\s\S]*?</figcaption>|<th[\s\S]*?</th>', "", html)))
        narrow = html.count("&#8239;") + html.count(" ")

        caps = re.findall(rf"<b>((?:{fig}|{tab}) \d+\.\d+)</b>", html)
        body_wo_caps = re.sub(r"<figcaption>[\s\S]*?</figcaption>|<caption>[\s\S]*?</caption>", " ", html)
        body_wo_caps = re.sub(r"<[^>]+>", " ", body_wo_caps).replace("&nbsp;", " ")
        unref = [c for c in caps if not re.search(re.escape(c).replace(r"\ ", r"\s+"), body_wo_caps, re.I)]

        n_sources = len(re.findall(r"<li>", html.split('class="sources"')[-1])) if 'class="sources"' in html else 0
        cites = [int(x) for grp in re.findall(r'<sup class="k">([\d,\s–-]+)</sup>', html) for x in re.findall(r"\d+", grp)]
        bad_cites = sorted(set(c for c in cites if c > n_sources or c < 1))
        unused = sorted(set(range(1, n_sources + 1)) - set(cites)) if n_sources else []

        print(f"\n== {os.path.basename(f)}  ({words} words)")
        if hits: print("  banned/flagged:", ", ".join(hits))
        if dashes: print(f"  prose dashes: {dashes} ({dashes * 1000 / max(words, 1):.1f} per 1000 words)")
        if openers: print(f"  reflexive openers: {openers}")
        if meta: print("  research-process language:", ", ".join(meta))
        if bold: print(f"  bold in body text: {bold}")
        if narrow: print(f"  narrow no-break spaces (&#8239;): {narrow}  -> run normalize_numbers.py")
        if unref: print("  never referenced in text:", ", ".join(unref))
        if bad_cites: print("  citations out of range:", bad_cites)
        if unused: print("  sources never cited in text (may back figure/table source lines):", unused)

    if a.pdf:
        out = subprocess.run(["pdftotext", "-layout", a.pdf, "-"], capture_output=True, text=True).stdout
        pages = out.split("\f")
        short = [(i, len([l for l in p.splitlines() if l.strip()])) for i, p in enumerate(pages, 1)]
        short = [(i, n) for i, n in short if 0 < n < 14 and i > 3]
        print(f"\n== PDF: {len(pages) - 1} pages")
        if short: print("  near-empty pages after front matter (page, lines):", short)


if __name__ == "__main__":
    main()
