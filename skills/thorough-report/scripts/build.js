#!/usr/bin/env node
// Assemble report/{cover,preface}.html + chapters/*.html into one HTML page and print it to PDF
// with Chromium, using a two-pass table of contents with real page numbers.
// Usage: PW_PATH=<.../node_modules/playwright> node build.js <report-dir>
// Env: OUT_PDF overrides the output path (use for scratch builds while someone reads the main PDF).
const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');
const { chromium } = require(process.env.PW_PATH || 'playwright');

const ROOT = path.resolve(process.argv[2] || '.');
const CHAPTERS = path.join(ROOT, 'chapters');
const config = JSON.parse(fs.readFileSync(path.join(ROOT, 'report.config.json'), 'utf8'));
const OUT_HTML = path.join(ROOT, '_assembled.html');
const OUT_PDF = process.env.OUT_PDF || path.join(ROOT, config.output || 'report.pdf');
const labels = Object.assign({ contents: 'Contents' }, config.labels || {});

const esc = (s) => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/"/g, '&quot;');

function drawMap(key) {
  const map = config.map;
  if (!map || !map.views || !map.views[key]) return '';
  const on = new Set(map.views[key]);
  const nodes = map.nodes || [];
  const bands = map.bands || [];
  const W = 740, x0 = 40, x1 = 700;
  const step = nodes.length > 1 ? (x1 - x0) / (nodes.length - 1) : 0;
  const parts = [];
  nodes.forEach((n, i) => {
    if (i === 0) return;
    const a = nodes[i - 1], both = on.has(a.id) && on.has(n.id);
    parts.push(`<line class="map-link${both ? ' on' : ''}" x1="${x0 + step * (i - 1) + 12}" y1="26" x2="${x0 + step * i - 12}" y2="26"/>`);
  });
  nodes.forEach((n, i) => {
    const x = x0 + step * i, c = on.has(n.id) ? ' on' : '';
    parts.push(`<circle class="map-node${c}" cx="${x}" cy="26" r="10"/>`);
    parts.push(`<text class="map-label${c}" x="${x}" y="54">${esc(n.label)}</text>`);
  });
  bands.forEach((b, i) => {
    const y = 76 + i * 20, c = on.has(b.id) ? ' on' : '';
    parts.push(`<rect class="map-band${c}" x="28" y="${y - 11}" width="684" height="16"/>`);
    parts.push(`<text class="map-band-label${c}" x="36" y="${y + 1}">${esc(b.label)}</text>`);
  });
  const h = 70 + bands.length * 20;
  return `<svg class="map" viewBox="0 0 ${W} ${h}" role="img" aria-label="${esc(labels.map || 'Where this chapter sits')}">${parts.join('')}</svg>`;
}

function readChapters() {
  return fs.readdirSync(CHAPTERS).filter((f) => f.endsWith('.html')).sort()
    .map((f) => fs.readFileSync(path.join(CHAPTERS, f), 'utf8'));
}

const attr = (html, name) => {
  const m = html.match(new RegExp(`<section[^>]*\\s${name}="([^"]*)"`));
  return m ? m[1] : '';
};
const h1 = (html) => {
  const m = html.match(/<h1[^>]*>([\s\S]*?)<\/h1>/);
  return m ? m[1].replace(/<[^>]+>/g, '').replace(/\s+/g, ' ').trim() : '';
};
const opt = (f) => (fs.existsSync(path.join(ROOT, f)) ? fs.readFileSync(path.join(ROOT, f), 'utf8') : '');

function assemble(pages) {
  const rows = [];
  let n = 0;
  const body = readChapters().map((html, i) => {
    const key = attr(html, 'data-map');
    const id = attr(html, 'id') || `section-${i}`;
    const appendix = attr(html, 'data-appendix');
    const nr = appendix || String(++n);
    rows.push({ id, title: h1(html), short: attr(html, 'data-short'), nr });
    return key ? html.replace(/(<header class="chapter-top">)/, `$1${drawMap(key)}`) : html;
  }).join('\n');

  const toc = `<section class="toc"><h2>${esc(labels.contents)}</h2><ol>${rows.map((r) => `
    <li><span class="nr">${r.nr}</span><span class="title">${r.title}${r.short ? `<small>${r.short}</small>` : ''}</span><span class="page">${pages && pages[r.id] ? pages[r.id] : ''}</span></li>`).join('')}</ol></section>`;

  const footer = `<style>@page { @bottom-left { content: "${String(config.footer || config.title || '').replace(/"/g, '\\"')}"; } }</style>`;
  const html = `<!doctype html>
<html lang="${esc(config.lang || 'en')}">
<head>
<meta charset="utf-8">
<title>${esc(config.title || 'Report')}</title>
<link rel="stylesheet" href="style.css">
${footer}
</head>
<body>
${opt('cover.html')}
${toc}
${opt('preface.html')}
${body}
</body>
</html>`;
  fs.writeFileSync(OUT_HTML, html);
  return rows;
}

async function print(file) {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + OUT_HTML, { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(400);
  await page.pdf({ path: file, format: 'A4', printBackground: true, preferCSSPageSize: true, outline: true, tagged: true });
  await browser.close();
}

function locate(pdf, rows) {
  const text = execFileSync('pdftotext', ['-layout', pdf, '-'], { maxBuffer: 1 << 28 }).toString();
  const pages = text.split('\f');
  const found = {};
  let start = 2;
  for (const r of rows) {
    const probe = r.title.split(' ').slice(0, 4).join(' ');
    for (let i = start; i < pages.length; i++) {
      if (pages[i].replace(/\s+/g, ' ').includes(probe)) { found[r.id] = i + 1; start = i + 1; break; }
    }
  }
  return found;
}

(async () => {
  const rows = assemble(null);
  await print(OUT_PDF);
  const pages = locate(OUT_PDF, rows);
  assemble(pages);
  await print(OUT_PDF);
  const check = locate(OUT_PDF, rows);
  const drift = rows.filter((r) => check[r.id] !== pages[r.id]).map((r) => r.id);
  const count = execFileSync('pdfinfo', [OUT_PDF]).toString().match(/Pages:\s+(\d+)/);
  console.log(JSON.stringify({ pdf: OUT_PDF, pages: count ? +count[1] : null, toc: pages, tocDrift: drift }, null, 1));
})();
