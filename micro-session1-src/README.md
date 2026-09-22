# Medical Microbiology — Session 1: Foundations (generator)

Sources for `output/microbiology-session1-english.pdf` (72 pp) and
`output/microbiology-session1-bilingual.pdf` (124 pp).

Covers Autumn Week 1: *Medical Microbiology — a brief introduction* and
*Bacterial cell structure*.

## Layout

| Path | Contents |
|---|---|
| `build/*.html` | Content, in reading order. One master copy serves both editions. |
| `build/base.css` | Page setup, typography, callouts, tables, flowcharts, figures, PDF bookmarks. |
| `build/bilingual.css`| Overlay applied only to the bilingual edition (RTL blocks, Persian type). |
| `img/` | Figures extracted from the lecture-1 slides. |
| `fonts/` | Source Serif 4, Inter, Vazirmatn (all OFL). |
| `build.py` | Assembles the parts and renders both PDFs with WeasyPrint. |

Parts, in `build.py`'s `PARTS` order:

1. `02_part1` — The Microbial World
2. `03_part2` — How We Learned It (germ theory to antibiotics)
3. `04_part3` + `05_part3b` — The Bacterial Cell Envelope
4. `06_part4` — External and Internal Structures
5. `07_part5` — Putting It Together in the Laboratory
6. `08_questions` / `09_answers` / `10_tables` / `11_glossary` — Review

## The `<fa>` convention

Persian is written inline inside the English content, wrapped in a custom
`<fa>` element:

```html
<p>English sentence.<fa>جملهٔ فارسی.</fa></p>
```

`build.py` then does one of two things with every `<fa>`:

- **English edition** — deletes it.
- **Bilingual edition** — converts it into a right-to-left block placed
  directly after its parent (or inside it, for table cells, captions and
  list items).

This keeps both editions in sync from a single source: edit the English and
its translation in the same place, and both PDFs stay correct.

## Microbiology-specific conventions

- **Gram tags.** `<span class="gp">Gram +</span>`, `.gn` (Gram −) and `.ga`
  (acid-fast) render as small violet / safranin-pink / rust tags. They are
  reserved for classification — never used as decoration.
- **Binomials.** `<span class="sp">S. aureus</span>` italicises Latin names
  and is left untranslated in the Persian column.
- **Box types.** `.box.hy` high-yield, `.box.trap` exam trap, `.box.lab`
  lab pearl, `.box.mn` mnemonic, `.box.cc` clinical correlation,
  `.box.hist` historical anchor, plus `.mech` for numbered
  step → *why* mechanism chains.
- **Flowcharts.** `.flow` with `.node` / `.test` / `.leaf`, used for the three
  laboratory identification trees in Part 5. Pure CSS, no images.
- **Hand-drawn SVG.** Figures 3.3 (peptidoglycan), 3.4 (Gram+ vs Gram−
  envelope), 3.5 (Gram stain) and 4.1 (sporulation) are inline SVG, because
  the Lecture 2 slides were not available.

## A note on sources

The Lecture 2 slide deck (*Bacterial cell structure*) was not available when
this guide was written. Parts 3–5 were reconstructed from that lecture's
in-class MCQ set — which tells us exactly which points the lecturer examined
— together with Jawetz and Lippincott. Every point the MCQs touch is covered
in full. This is flagged for the reader in an Exam-Trap box on the
"How to Use This Guide" page.

## Rebuilding

```bash
pip install weasyprint beautifulsoup4 pymupdf
python3 build.py both ../output      # or: en / bi
```

Rendering takes about 15 seconds per edition.
