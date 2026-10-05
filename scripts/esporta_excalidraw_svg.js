#!/usr/bin/env node
// Esporta in SVG tutti i file docs/schemi/*.excalidraw, così GitHub li mostra.
// Requisiti (una volta sola):  npm i --no-save @excalidraw/utils@0.1.2 playwright-core
// e un Chromium installato (indicare il percorso in CHROMIUM_PATH se serve).
// Uso:  node scripts/esporta_excalidraw_svg.js
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright-core');

const radice = path.resolve(__dirname, '..');
const cartella = path.join(radice, 'docs', 'schemi');
const utils = require.resolve('@excalidraw/utils/dist/excalidraw-utils.min.js');

(async () => {
  const browser = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});
  const page = await browser.newPage();
  await page.setContent('<html><body></body></html>');
  await page.addScriptTag({ content: fs.readFileSync(utils, 'utf8') });
  for (const nome of fs.readdirSync(cartella).filter(f => f.endsWith('.excalidraw'))) {
    const scena = JSON.parse(fs.readFileSync(path.join(cartella, nome), 'utf8'));
    const svg = await page.evaluate(async (s) => {
      const el = await ExcalidrawUtils.exportToSvg({
        elements: s.elements,
        appState: { ...s.appState, exportBackground: true, exportWithDarkMode: false },
        files: s.files || {},
      });
      return el.outerHTML;
    }, scena);
    const uscita = path.join(cartella, nome.replace(/\.excalidraw$/, '.svg'));
    fs.writeFileSync(uscita, svg);
    console.log('Esportato', path.relative(radice, uscita));
  }
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
