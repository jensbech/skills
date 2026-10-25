#!/usr/bin/env node
// Make overview images (8 columns x 3 rows) from page PNGs produced by:
//   pdftoppm -r 50 -png report.pdf <dir>/p
// Usage: PW_PATH=<.../node_modules/playwright> node contact-sheet.js <dir> <out-prefix> [pagesPerSheet=24]
const fs = require('fs');
const path = require('path');
const { chromium } = require(process.env.PW_PATH || 'playwright');

(async () => {
  const [dir, out, per = '24'] = process.argv.slice(2);
  const n = +per;
  const files = fs.readdirSync(dir).filter((f) => /^p-\d+\.png$/.test(f))
    .sort((a, b) => +a.match(/\d+/)[0] - +b.match(/\d+/)[0]);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1800, height: 1000 } });
  for (let i = 0; i < files.length; i += n) {
    const chunk = files.slice(i, i + n);
    const html = `<body style="margin:0;background:#888;display:grid;grid-template-columns:repeat(8,1fr);gap:6px;padding:6px">${chunk.map((f) => `<div style="background:#fff;position:relative"><img src="file://${path.join(path.resolve(dir), f)}" style="width:100%;display:block"><span style="position:absolute;top:0;left:0;background:#000;color:#fff;font:12px sans-serif;padding:1px 4px">${f.match(/\d+/)[0]}</span></div>`).join('')}</body>`;
    const tmp = path.join(dir, '_sheet.html');
    fs.writeFileSync(tmp, html);
    await page.goto('file://' + path.resolve(tmp));
    await page.waitForTimeout(300);
    const file = `${out}-${String(i / n + 1).padStart(2, '0')}.png`;
    await page.screenshot({ path: file, fullPage: true });
    console.log(file);
  }
  await browser.close();
})();
