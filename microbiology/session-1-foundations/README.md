# Medical Microbiology — Session 1: Foundations

Sources for `microbiology-session1-english.pdf` (88 pp) and
`microbiology-session1-bilingual.pdf` (145 pp).

Covers Autumn Week 1: *Medical Microbiology — a brief introduction* and
*Bacterial cell structure*.

## Layout

| Path | Contents |
|---|---|
| `src/build/*.html` | Content, in reading order. One master copy serves both editions. |
| `src/build/base.css` | Page setup, typography, callouts, tables, flowcharts, figures, PDF bookmarks. |
| `src/build/bilingual.css` | Overlay applied only to the bilingual edition (RTL blocks, Persian type). |
| `src/img/` | Figures extracted from the lecture-1 slides. |
| `src/fonts/` | Source Serif 4, Inter, Vazirmatn (all OFL). |
| `src/build.py` | Assembles the parts and renders both PDFs with WeasyPrint. |

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
- **Hand-drawn SVG.** Four diagrams are inline SVG rather than images:
  peptidoglycan architecture, the Gram+ vs Gram− envelope comparison, the
  four-step Gram stain, and five-stage sporulation. They sit alongside the
  course's own figures rather than replacing them.
- **Course figures.** Figures named `img/l2_*.jpg` are extracted from the
  Lecture 2 deck. They are JPEG rather than PNG: WeasyPrint passes JPEG
  through unchanged, which keeps the English PDF near 5 MB instead of 12 MB.

## A note on sources

Built from both lecture decks in full (Lecture 1, 59 slides; Lecture 2, 60
slides), their in-class MCQ sets, and the textbooks the slides themselves
cite — Jawetz Ch. 1–2, Lippincott, Brock and First Aid.

Where the lecture gives a number, the lecture's number is used. Two of them
differ from figures quoted in some textbooks and are called out for the
reader on the title-page source note:

- Gram-positive wall: **20–80 nm thick, 15–50 peptidoglycan layers**
- Gram-negative wall: **10–15 nm, 1–2 layers**

Thickness and layer count are different quantities; conflating them is the
commonest error on this topic.

## Rebuilding

```bash
cd src
pip install weasyprint beautifulsoup4 pymupdf
python3 build.py both ..             # or: en / bi
```

Rendering takes about 15 seconds per edition.
