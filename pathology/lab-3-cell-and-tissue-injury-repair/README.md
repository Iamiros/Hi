# Pathology Laboratory, Session 3: Cell and Tissue Injury and Repair (3)

`pathology-lab3-english.pdf` (38 pp) and `pathology-lab3-bilingual.pdf` (49 pp).

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
rather than redrawn. All image sources and notes are in `src/img/CREDITS.md`.

A second pass (below) added a real, openly licensed image of the **normal**
version of every organ in Part Three, beside its pathological specimen, plus
numbered pointer-circle annotations on every gross photo and micrograph that
did not already carry the lab's own red circle, and substantially more
teaching text under each image explaining what the circles mark and why it
matters. See "Second review round" below for what that pass found and fixed.

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

## Second review round

Follow-up pass after specific feedback: some pages still felt sparse, every
specimen needed a real normal-organ image beside it, the theme needed more
visual weight, and images needed more teaching text and pointer annotation.

**Found and fixed**:
- One image, `f10_foot_dry_gangrene_detail.png`, had shipped as an
  uncropped screenshot with the specimen-viewer's video-player UI still
  visible over part of the foot, missed by the first crop pass. Re-cropped
  clean and re-circled.
- Six new real, openly licensed images of the **normal** organ were sourced
  (Openverse, Wikimedia Commons: lung, liver, appendix, small intestine,
  long bone, lymph node) and placed beside every specimen that needed one;
  spleen and skin reuse their existing Part Two figures. Licences and
  authors are in `src/img/CREDITS.md`. No equally reliable normal-foot photo
  turned up in the time available; that one specimen's own close-up already
  shows a wide margin of normal, viable skin beside the necrotic zone, and
  the text says so rather than manufacturing a weaker substitute image.
- Added numbered gold pointer-circles (matching the deck's own red-circle
  convention) to every gross photo and micrograph that did not already carry
  one, with a legend explaining each circled region, and a new paragraph of
  teaching text per specimen tying the normal and pathological images
  together.
- Enriched the "Specimen Lightbox" theme: a faint dot-grid page texture,
  bracket corner-ticks on every specimen card, and a soft gold glow behind
  each photo, without spending the accent colour on anything but its
  original job.
- **A genuine pagination bug, found and fixed twice in this round**: the
  first attempt floated the new normal-comparison figure beside the
  existing close-up figure. Paged.js cannot reliably fragment two competing
  floats attached to the same block and silently dropped both from the
  page entirely; fixed by making the comparison figure a plain
  non-floating block instead. A second, related bug then surfaced only in
  the bilingual edition: a two-item pointer-circle legend nested inside a
  specimen card's own page-break-inside:avoid box lost its second item
  outright wherever the card's combined English-plus-Persian text made the
  whole card taller than one page. Fixed by moving every such legend
  outside the specimen card, as its own block, so it paginates normally
  instead of fighting a forced single-page fragment. Confirmed by
  re-rendering every changed page to PNG and by grepping the extracted PDF
  text of both editions for every legend's key phrase.
- Re-checked for the whitespace complaint itself: an automated scan for
  large blank vertical bands, and a page-by-page visual read of both
  editions, found no page left mostly empty by a rendering fault. The
  moderate blank space that remains under a few section headings is the
  ordinary, unavoidable cost of never letting a specimen card split across
  a page break, the same rule that fixed the original pagination bug.

Page counts: 33 to 40 (English), 44 to 53 (bilingual).

## Third review round: the actual cause of the recurring whitespace

The user pointed at the delivered files directly and said the blank space was still there.
Checking by eye confirmed it: several pages (the necrosis-patterns intro, the gangrene-table
page, others) ran content for less than half the page, then sat empty.

Root cause: every specimen card (heading + photo header + a near-full-page image + body text)
was kept `page-break-inside:avoid` as one unit. A unit that size (up to ~180mm) regularly did not
fit in whatever space was left on the current page, so paged.js pushed the *entire* card to a
fresh page, leaving the page before it mostly blank. An intermediate fix shrank the atomic unit to
just heading+header+image (page-break-inside measured against the earlier full-card version),
which helped but still left large gaps wherever even that smaller block did not fit.

Fix that actually worked: dropped the atomic grouping entirely. Only the image itself
(`.spec-img`) is still kept from being sliced mid-photo; the heading keeps itself off a page alone
(`page-break-after:avoid`, already standard for every heading), but is no longer forced to stay
with the image that follows it. In the worst case, a specimen's heading and header bar now sit at
the foot of one page with its photo continuing cleanly at the top of the next, same bordered card,
no repeated header, instead of a half-empty page. Verified page by page (both editions, re-rendered
to PNG) and by grepping the extracted PDF text of both editions for the full text of every specimen
diagnosis line and every annotation legend item, to confirm nothing was lost in the process this
time. Page counts dropped again, 40 to 38 (English) and 53 to 49 (bilingual): the fix did not just
move the blank space around, it reclaimed it.

While restructuring the specimen-card markup for this fix, found and fixed four stray duplicate
closing `</div>` tags left over from an earlier editing pass (one each on specimens No.16, No.17,
No.18, No.6*, No.86, No.23, No.20*), confirmed with an HTML parser that both files are now fully
tag-balanced.
