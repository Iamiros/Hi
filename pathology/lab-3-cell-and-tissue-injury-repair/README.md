# Pathology Laboratory, Session 3: Cell and Tissue Injury and Repair (3)

`pathology-lab3-english.pdf` (33 pp) and `pathology-lab3-bilingual.pdf` (44 pp).

First guide built under the Pathology Laboratory "Specimen Lightbox" theme
(`../THEME-lab.md`): dark background throughout so the real gross photos and
micrographs glow like a lightbox, Space Grotesk + JetBrains Mono, specimen
cards, and a fixed description template (organ, gross/micro description,
diagnosis) every specimen follows.

## Scope

Necrosis and gangrene, then repair, on seven gross specimens and five
slides, per the lab's own learning objectives:

- **Necrosis**, the three morphologic patterns (coagulative, caseous,
  liquefactive), each on its own gross specimen (spleen infarct, TB ball of
  the lung, bacterial liver abscess)
- **Gangrene**, wet vs. dry, on three gross specimens (gangrenous
  appendicitis, wet gangrene of small intestine with roundworm, dry gangrene
  of the foot)
- **Repair**, granulation tissue and fracture healing, on one gross specimen
  (fibrous callus) and two key slides (spleen anemic infarction, healing by
  second intention)
- **Normal baseline** (Part Two): spleen and skin, gross and histology,
  reviewed first since every lesion in Part Three is read against it
- Homework, a 10-question spot-exam-style self-test with answer key, a
  spot-exam practice page, an identification checklist, and a glossary

Enriched throughout from Robbins Basic Pathology 11e (chapter 2, Cell
Injury; chapter 3, Repair); every such addition is marked in context.

## Method

All 22 real images (gross photographs and H&E micrographs) extracted
directly from the lab's own slide deck (a PowerPoint built from screenshots
of an online specimen viewer). Two images the deck itself was missing from
its normal `PICTURE` shapes (slide 9's appendix photo, slide 24's lymph-node
micrograph) were recovered directly from the pptx's `media/` folder via its
slide relationships. Every image's UI chrome, the specimen-viewer's video
player bar, its "specimen information" popup, its sidebar icons, was cropped
out; two images with Chinese-only on-slide labels (the annotated skin
histology plates) were kept and their labels translated in the caption
rather than redrawn. All nine credited image sources and notes are in
`src/img/CREDITS.md`.

Same pipeline as the lecture guides: **Playwright Chromium** driving
**paged.js** (vendored in `src/vendor/`) for CSS Paged Media support (running
headers, `target-counter` page numbers), served over a tiny local HTTP
server so paged.js's XHR stylesheet fetch works (blocked under `file://`).
Persian written inline as `<fa>…</fa>`; `build.py` strips it for the English
edition and converts it to bidi-isolated right-to-left blocks for the
bilingual edition, following the same no-border-per-sentence layout as the
lecture guides (a hairline once per section, not once per paragraph).

```bash
cd src
pip install playwright beautifulsoup4 pymupdf
python3 build.py both ..      # or: en / bi
```

## Review passes

**Pass A, accuracy**: every specimen's gross/micro description checked
against the lab's own text word for word, and every added mechanism
(why a wedge, why pale, why liquid, why sharply demarcated) checked against
Robbins 11e. One discrepancy found and flagged rather than silently
resolved: the homework sheet names slide "No.6* caseous necrosis in lymph
node," but the lab's own specimen list and slide deck give No.6* as the
spleen anemic infarction slide and No.86 as the lymph-node slide; noted in
a box under Homework rather than guessed at.

**Pass B, design**: both editions rendered to PNG and every page inspected.
Found and fixed a serious pagination bug: several gross-specimen photos are
tall, narrow crops (cropped to remove the specimen-viewer's UI panel), and
under `width:100%` inside a `page-break-inside:avoid` specimen card, one
image alone rendered taller than a full page, forcing pagedjs to push the
entire card to a fresh page while its own heading was stranded alone on the
page before it. Fixed by capping specimen and spot-exam images to
`max-height` with `width:auto`, centered, letterboxed in black, matching
the lightbox theme itself; page count dropped from 50 to 33 (English) as a
result.

**Pass C, bilingual**: dark-theme contrast checked specifically, per the
project's own standing instruction that the dark theme needs its own check.
Persian body text sits at `#C7CCD2` against the `#111316` page background
(contrast ratio ≈ 9.7:1) and against the `#1B1E22` card surface (≈ 6.9:1),
both comfortably above WCAG AA for body text. RTL/LTR mixing (CD/organism
names, measurements), Persian punctuation, table cells, and captions
checked page by page; no tofu glyphs.
