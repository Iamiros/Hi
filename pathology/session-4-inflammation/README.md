# Pathology — Session 4: Inflammation, Part One

`pathology-session4-english.pdf` (26 pp) and `pathology-session4-bilingual.pdf` (44 pp).

First guide built under the Pathology "Clinical Case File" theme (`../THEME.md`): Commissioner +
IBM Plex Mono, eosin/haematoxylin accent system, two-column-editorial layout with a margin rail for
sidenotes, process-rail device, and purpose-built cascade diagrams instead of reused textbook scans.

## Scope

Covers exactly what the lecture ("Inflammation, part one," Prof. Zhou Ren) teaches:

- **I–II** Definitions and general features; the alteration/exudation/proliferation trilogy
- **III** Blood-vessel reaction: vascular caliber and hyperemia, the three mechanisms of increased
  permeability
- **IV** Exudation: Starling forces and transudate vs. exudate; the full leukocyte recruitment
  cascade (margination, rolling, adhesion, transmigration, chemotaxis); phagocytosis and killing;
  cell-type significance and the macrophage's four morphologic forms
- **V** Chemical mediators, cell-derived (vasoactive amines, arachidonic-acid metabolites,
  cytokines, PAF, nitric oxide) and plasma-derived (complement, kinin, coagulation, all triggered
  by Factor XII/Hageman factor)

The docx learning-objectives outline runs further (morphologic subtypes — serous, fibrinous,
suppurative, granulomatous; systemic manifestations; the clinical vocabulary of abscess, sinus,
fistula, bacteremia). None of that is in the Part 1 slide deck, so none of it is in this guide;
it belongs to Part 2, not yet supplied.

Enriched throughout from Robbins Basic Pathology 11e (chapter 2); every such addition is marked
**Beyond the slides** in the margin. One PMID is cited and verified against PubMed
(Mojtabavi et al. 2020, PMID 32933891, for the IL-6/COVID-19 severity correlation the lecture
itself raises).

## Method

Text and 74 embedded images extracted once from the 95-slide PDF with PyMuPDF, plus the 22-point
learning-objectives docx, both to the scratchpad. Two real H&E micrographs (macrophage/giant-cell
morphology) were kept from the lecture slides and are credited in `src/img/CREDITS.md`; every
schematic or mechanism figure in the lecture (vessel structure, Starling forces, the adhesion
cascade, arachidonic-acid metabolism, the complement/kinin/coagulation cross-talk) was redrawn as
an original inline-SVG diagram in the course theme rather than reused as a scan.

Rendered with **Playwright Chromium** driving **paged.js** (vendored in `src/vendor/`) for true
CSS Paged Media support (running headers, named pages, `target-counter` page numbers in the TOC),
since Chromium's own print engine does not implement those on its own. A tiny local HTTP server
(`src/build.py`) serves the build directory so paged.js can fetch its stylesheet by XHR, which
`file://` URLs block.

Persian is written inline as `<fa>…</fa>` in one master source; `build.py` deletes it for the
English edition and converts it into bidi-isolated right-to-left blocks for the bilingual edition.

```bash
cd src
pip install playwright beautifulsoup4 pymupdf
python3 build.py both ..      # or: en / bi
```

## Review passes

**Pass A, accuracy** — every mechanism, molecule name, and number checked against the lecture
transcript and Robbins 11e (Starling-force values, the NADPH-oxidase/MPO equations, the
selectin/integrin/Ig-superfamily pairings, the complement convergence). No invented numbers. The
one PMID cited was checked with the PubMed MCP (`get_article_metadata`): the paper exists, the
citation details match, and its abstract supports the claim.

**Pass B, design** — both editions rendered to PNG at 110 dpi and every page inspected. Found and
fixed: a title-page footer overlapping the source list (absolute positioning that assumed one exact
content length; changed to normal flow), a Chromium/paged.js quirk that fully justified short
single-line paragraphs and captions instead of left-aligning the last line (fixed with
`text-align-last: left`), text overflowing its SVG viewBox in three diagrams (Starling forces, the
adhesion cascade, the arachidonic-acid pathway), and a baked-in textbook caption cropped out of one
of the two kept micrographs.

**Pass C, bilingual** — the same title-page fix carried a stray `position: absolute` leftover in
`bilingual.css` (a `top` offset stacking on top of the new flow-based spacing) that produced a
large blank gap on the bilingual title page; changed to `margin-top`. RTL/LTR mixing, Persian
punctuation, table cells, figure captions, and the two-column glossary all checked page by page;
no tofu glyphs, no Persian-in-tables misalignment.
