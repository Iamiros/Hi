# Pathology Laboratory — Session 2: Cell and Tissue Injury

Sources for `pathology-lab2-english.pdf` (41 pp) and
`pathology-lab2-bilingual.pdf` (68 pp).

Covers reversible cell and tissue injury: cellular swelling, fatty change,
hyaline degeneration, mucoid change and pathological calcification, with the
normal liver and gastrointestinal tract as the baseline, and a card for every
specimen and slide on the session's list.

## Layout

| Path | Contents |
|---|---|
| `src/build/*.html` | Content, in reading order. One master copy serves both editions. |
| `src/build/base.css` | Page setup, typography, callouts, tables, specimen cards, PDF bookmarks. |
| `src/build/bilingual.css` | Overlay applied only to the bilingual edition (RTL blocks, Persian type). |
| `src/img/` | Figures cropped from the lecture deck. |
| `src/fonts/` | Source Serif 4, Inter, Vazirmatn (all OFL). |
| `src/build.py` | Assembles the parts and renders both PDFs with WeasyPrint. |

Parts, in `build.py`'s `PARTS` order:

1. `02_part1` — The Normal Baseline: liver, stomach, intestine
2. `03_part2` — Reversible Injury: the five changes, with mechanisms
3. `04_part3` — Gross specimens (7 cards)
4. `05_part4` — Microscopic slides (5 cards)
5. `06_review` — Homework, comparison tables, self-test, glossary

Shares the design system and the `<fa>` bilingual convention with
`pathology-lab1-src`; see that README for both. The laboratory method — the
description templates and the department's four report headings — lives in the
Session 1 guide and is referenced rather than repeated.

## What is specific to this session

- **Fig 2.1** is a hand-drawn inline SVG comparing normal, swollen, ballooning
  and fatty hepatocytes. The deck's own histology images were low-resolution
  screenshots, and the course objective is explicitly to *distinguish* cellular
  swelling from fatty change, so a purpose-drawn diagram serves better than a
  blurry micrograph.
- **§5.3** gives one table per stated course objective: cellular swelling vs
  fatty change, tigroid heart vs fat heart, and hyaline vs mucoid vs
  calcification.
- The lecturer's **red-boxed correction** on specimen 11 — the white stripe is
  hyaline, the grey-blue area is mucoid — is reproduced as an Exam Trap, since
  a correction made that visibly signals what he intends to examine.

## Notes on the source

Built from screenshots of the deck viewed through the course platform, so
figures carried player chrome, watermarks, a university banner and the
platform's floating assistant button. These were cropped out, and in two
figures the button was cloned over with adjacent tissue.

Images are JPEG rather than PNG: WeasyPrint passes JPEG through unchanged,
which keeps the English PDF near 3.5 MB.

## Rebuilding

```bash
cd src
pip install weasyprint beautifulsoup4 pymupdf
python3 build.py both ..             # or: en / bi
```

Rendering takes about 10 seconds per edition.
