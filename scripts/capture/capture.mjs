import { chromium } from "playwright";
import path from "node:path";
import fs from "node:fs";
import { fileURLToPath } from "node:url";

// Regenerates the README / social screenshots from the documentation site
// (docs/*.html). The banner PNGs are rendered separately by banner.sh.
const here = path.dirname(fileURLToPath(import.meta.url));
const docsDir = path.resolve(here, "../../docs");
const pageUrl = (file) => "file://" + path.join(docsDir, file).replace(/\\/g, "/");
const outDir = path.resolve(docsDir, "assets");
fs.mkdirSync(outDir, { recursive: true });

async function shoot({ dsr, viewport }, jobs) {
  const browser = await chromium.launch();
  const ctx = await browser.newContext({ deviceScaleFactor: dsr, viewport });
  const page = await ctx.newPage();
  let loaded = null;
  for (const j of jobs) {
    if (loaded !== j.page) {
      await page.goto(pageUrl(j.page), { waitUntil: "networkidle" });
      await page.evaluate(() => document.fonts.ready);
      if (j.page === "charts.html") await page.waitForSelector("#plot-mount svg", { timeout: 20000 }); // Plot from CDN
      loaded = j.page;
    }
    await page.evaluate((d) => document.documentElement.classList.toggle("dark", d), !!j.dark);
    await page.evaluate((g) => document.documentElement.classList.toggle("geist", g), !!j.geist);
    await page.evaluate((j2) => document.documentElement.classList.toggle("jost", j2), !!j.jost);
    await page.evaluate(() => document.fonts.ready); // re-settle metrics after a flavor/accent swap
    await page.waitForTimeout(200);
    if (j.fullViewport) {
      // Sidebar + content together: a plain page.screenshot() with no clip/fullPage
      // captures exactly the loaded viewport.
      await page.screenshot({ path: path.join(outDir, j.file) });
      console.log("wrote", j.file);
      continue;
    }
    const el = await page.$(j.id);
    if (!el) throw new Error(`${j.file}: ${j.id} not found on ${j.page}`);
    // #social-card is rendered off-canvas (left:-9999px) so it never shows on the live
    // page. Playwright cannot clip a negative-x region, so zero the offset for the
    // capture only (DOM-only, in the headless page) and restore it afterwards.
    const box = await el.boundingBox();
    const offCanvas = box.x < 0 || box.y < 0;
    if (offCanvas) {
      await el.evaluate((node) => {
        node.dataset.captureLeft = node.style.left;
        node.dataset.captureTop = node.style.top;
        node.style.left = "0px";
        node.style.top = "0px";
      });
      await page.waitForTimeout(50);
    }
    const shotBox = await el.boundingBox();
    if (j.assert) {
      if (Math.round(shotBox.width) !== j.assert.w || Math.round(shotBox.height) !== j.assert.h)
        throw new Error(`${j.file}: expected ${j.assert.w}x${j.assert.h}, got ${Math.round(shotBox.width)}x${Math.round(shotBox.height)}`);
    }
    await el.screenshot({ path: path.join(outDir, j.file) });
    if (offCanvas) {
      await el.evaluate((node) => {
        node.style.left = node.dataset.captureLeft;
        node.style.top = node.dataset.captureTop;
        delete node.dataset.captureLeft;
        delete node.dataset.captureTop;
      });
    }
    console.log("wrote", j.file);
  }
  await browser.close();
}

// Section shots — crisp 2x.
await shoot({ dsr: 2, viewport: { width: 1180, height: 1000 } }, [
  { page: "index.html", fullViewport: true, file: "hero-light.png", dark: false },
  { page: "index.html", fullViewport: true, file: "hero-dark.png", dark: true },
  { page: "colors.html", id: "#palette", file: "palette.png", dark: false },
  { page: "typography.html", id: "#registers", file: "type-registers.png", dark: false },
  { page: "typography.html", id: "#text-length", file: "text-length.png", dark: false },
  { page: "components.html", id: "#gallery", file: "components.png", dark: false },
  { page: "components.html", id: "#figure", file: "images.png", dark: false },
  { page: "charts.html", id: "#plot", file: "charts.png", dark: false },
]);

// Social card — exactly 1200x630 at 1x.
await shoot({ dsr: 1, viewport: { width: 1280, height: 720 } }, [
  { page: "index.html", id: "#social-card", file: "social-card.png", dark: false, assert: { w: 1200, h: 630 } },
]);
