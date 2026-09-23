# Pathology Laboratory — Session 1: Introduction (generator)

Sources for `output/pathology-lab1-english.pdf` (39 pp) and
`output/pathology-lab1-bilingual.pdf` (67 pp).

Covers the laboratory session of 16 September: laboratory method, the normal
heart, lung and kidney, and the adaptations — atrophy, hypertrophy,
hyperplasia and metaplasia — with a card for every specimen on the list.

## Layout

| Path | Contents |
|---|---|
| `build/*.html` | Content, in reading order. One master copy serves both editions. |
| `build/base.css` | Page setup, typography, callouts, tables, specimen cards, PDF bookmarks. |
| `build/bilingual.css`| Overlay applied only to the bilingual edition (RTL blocks, Persian type). |
| `img/` | Figures extracted from the lecture deck. |
| `fonts/` | Source Serif 4, Inter, Vazirmatn (all OFL). |
| `build.py` | Assembles the parts and renders both PDFs with WeasyPrint. |

Parts, in `build.py`'s `PARTS` order:

1. `02_part1` — How to Work in the Pathology Lab (the description templates)
2. `03_part2` — The Normal Baseline: heart, lung, kidney
3. `04_part3` — Cellular Adaptation: the concepts
4. `05_part4` — This Session's Specimens (the cards)
5. `06_review` — Homework, self-test, glossary

## The `<fa>` convention

Persian is written inline inside the English content, wrapped in a custom
`<fa>` element:

```html
<p>English sentence.<fa>جملهٔ فارسی.</fa></p>
```

`build.py` then either deletes every `<fa>` (English edition) or converts it
into a right-to-left block placed after its parent (bilingual edition). One
source, two editions, permanently in sync.

## Laboratory-specific conventions

- **Specimen card** (`.spec`) — the signature block. Header (specimen number
  and type) → *What you see* → *Why it looks like that* → *Pathological
  diagnosis* → *Write it like this*. Cards break across pages, but the header
  stays with its first row.
- **Two tags.** `<span class="gr">Gross</span>` (eosin rose) and
  `<span class="mi">Micro</span>` (haematoxylin violet) mark where an
  observation comes from. Reserved for that — never decorative.
- **Description template** (`.tmpl`) — a numbered bench procedure where each
  step carries the question to ask at that step.
- **Box types.** `.box.hy` high-yield, `.box.trap` exam trap, `.box.lab`
  bench technique, `.box.clin` clinical correlation, plus `.mech` for
  numbered step → *why* mechanism chains.
- **Self-test** (`.qa` / `.q2` / `.a2`) — short-answer format, matching how
  the laboratory is actually examined.

## Notes on the source

The deck is a specimen list with photographs and a few descriptive sentences;
it states what to look at but rarely why the tissue looks that way. Every
item on the list is covered, using the lecturer's own wording where he gave
it. Mechanisms are filled in from Robbins.

Two things are flagged for the reader rather than silently resolved:

- Specimen 21 is labelled *"central hypertrophy"*, almost certainly a
  translation of 向心性肥大 (concentric), yet described with a dilated
  cavity. The guide gives both readings and the concentric/eccentric rule.
- Figures extracted from the deck were screenshots of a slide-viewer with
  player chrome and watermarks; these were cropped, and two stray labels
  bleeding in from an adjacent panel were painted out.

Images are JPEG rather than PNG: WeasyPrint passes JPEG through unchanged,
which keeps the English PDF near 3 MB.

## Rebuilding

```bash
pip install weasyprint beautifulsoup4 pymupdf
python3 build.py both ../output      # or: en / bi
```

Rendering takes about 10 seconds per edition.
