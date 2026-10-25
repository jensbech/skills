#!/usr/bin/env python3
"""Insert non-breaking spaces in numbers and before units, in text nodes only (never in tags,
attributes or URLs), so "25 309 MW" and "88 %" never split across lines.

Usage: python3 normalize_numbers.py <report-dir> [--lang nb|en|sv|da|de|fr|...] [--dry-run]
- Space-grouping languages (nb, nn, sv, da, de, fr, fi, ...): "25 309" -> "25&nbsp;309".
- All languages: "&#8239;" (renders ~0 width in Chromium PDFs) -> "&nbsp;"; "1400 MW" -> "1400&nbsp;MW".
"""
import argparse
import glob
import os
import re

UNITS = (r"kWh|MWh|GWh|TWh|kW|MW|GW|GWs|kV|Hz|V|W|%|km|kg|t|m|mm|cm|ms|s|"
         r"øre|kr|NOK|EUR|USD|euro|mrd|mill|millioner|milliarder|prosent|bn|million|billion|percent")
SPACE_GROUPING = {"nb", "nn", "no", "sv", "da", "de", "fr", "fi", "pl", "cs", "ru", "es", "it", "pt", "nl"}


def fix_text(x, grouping):
    x = x.replace("&#8239;", "&nbsp;").replace(" ", "&nbsp;")
    if grouping:
        for _ in range(3):
            x = re.sub(r"(?<![\d,.])(\d{1,3})(?: | )(\d{3})(?!\d)", r"\1&nbsp;\2", x)
    x = re.sub(r"(\d)(?: )(" + UNITS + r")(?![A-Za-zæøåÆØÅäöüÄÖÜ])", r"\1&nbsp;\2", x)
    return x


def process(html, grouping):
    parts = re.split(r"(<[^>]+>)", html)
    for i in range(0, len(parts), 2):
        segs = re.split(r"(https?://\S+)", parts[i])
        for j in range(0, len(segs), 2):
            segs[j] = fix_text(segs[j], grouping)
        parts[i] = "".join(segs)
    return "".join(parts)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("report")
    ap.add_argument("--lang", default="en")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    grouping = a.lang in SPACE_GROUPING
    files = sorted(glob.glob(os.path.join(a.report, "chapters", "*.html")))
    files += [p for p in (os.path.join(a.report, f) for f in ("cover.html", "preface.html")) if os.path.exists(p)]
    for f in files:
        s = open(f, encoding="utf-8").read()
        t = process(s, grouping)
        if t != s:
            n = t.count("&nbsp;") - s.count("&nbsp;")
            print(f"{os.path.basename(f)}: +{n} nbsp")
            if not a.dry_run:
                open(f, "w", encoding="utf-8").write(t)


if __name__ == "__main__":
    main()
