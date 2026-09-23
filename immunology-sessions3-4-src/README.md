# Medical Immunology — Sessions 3 & 4: Immune Molecules and Innate Immunity (generator)

Sources for `output/immunology-sessions3-4-english.pdf` (93 pp) and
`output/immunology-sessions3-4-bilingual.pdf` (152 pp).

One guide covering **two** lectures, because they overlap heavily: cytokines
appear in both, one slide (the viral cytokine decoys) is identical in both
decks, and — more importantly — both are built on the same control
architecture, which is the organising idea of the guide.

- **Lecture 3 — Immune Molecules (CD molecules, cytokines and MHC)**, 54 slides
- **Lecture 4 — Innate Immunity**, 48 slides

Both by Francis Kaming Chan, PhD, Liangzhu Laboratory, ZJU School of Medicine.

## Layout

| Path | Contents |
|---|---|
| `build/*.html` | Content, in reading order. One master copy serves both editions. |
| `build/base.css` | Page setup, typography, callouts, tables, partner cards, signal strips, PDF bookmarks. |
| `build/bilingual.css`| Overlay applied only to the bilingual edition (RTL blocks, Persian type). |
| `img/` | Figures extracted from the two lecture PDFs. |
| `fonts/` | Source Serif 4, Inter, Vazirmatn (all OFL). |
| `build.py` | Assembles the parts and renders both PDFs with WeasyPrint. |

Parts, in `build.py`'s `PARTS` order:

1. `02_part1` — CD molecules: the vocabulary of the cell surface
2. `03_part2` — The three signals: how a T cell is switched on
3. `04_part3` — MHC and HLA: the display case
4. `05_part4` — Cytokines: properties, receptors, signalling
5. `06_part5` — What cytokines do: differentiation, survival, death
6. `07_part6` — Innate immunity: triggers and sensors
7. `08_part7` — The inflammasome: two signals again
8. `09_part8` — When it goes wrong: storm, disease, therapy
9. `10_review` — Master tables, 30-question self-test, glossary

Shares the `<fa>` bilingual convention with the other guides in this
repository: Persian is written inline inside the English source wrapped in
`<fa>…</fa>`, and `build.py` either deletes every `<fa>` block (English
edition) or converts it to a styled RTL block (bilingual edition). One source,
two editions, permanently in sync.

## The method designed for this subject

These two lectures read as a vocabulary list — CD3, CD28, CTLA-4, HLA-DR,
IL-2, γc, JAK3, TLR4, MyD88, NLRP3, ASC, caspase-1, GSDMD — and a vocabulary
list is the one thing you must not make of them. Every name is a word in a
**sentence one cell says to another**, and the sentence always has four slots:
*who is speaking and from which cell · who is listening and from which cell ·
what happens inside the listener · what breaks if it is gone*.

The spine of the guide is the lecturer's own **signal 1 / signal 2 / signal 3**
framework, which he uses in *both* lectures and draws as a car — ignition key,
accelerator, steering wheel. The claim the guide is built on is that Lecture 3
and Lecture 4 describe **the same two-signal control architecture in two
different cells**, and §9.4 is the table that makes that explicit.

Six devices:

- **Partner cards** (`.pair`) — a CD molecule alone is unlearnable; a pair is
  not. Each card names which molecule, on which cell, binds which molecule, on
  which cell, and what results.
- **Signal tags** `S1` `S2` `S3` and **cell tags** `T` `B` `APC` `MΦ` — half of
  all mistakes in this topic are the right molecule on the wrong cell, so the
  cell travels with the molecule.
- **Signalling strips** (`.casc`, inline SVG) — TCR, JAK–STAT and TLR→NF-κB
  drawn on one template, each ending at a transcription factor, with the drug
  that blocks it marked on the chain.
- **Absence proves function** (`.box.absent`) — X-linked SCID, CTLA-4
  deficiency, ALPS, the MyD88 knockout, the caspase-1 knockout; and in §8.4 the
  same device inverted, *excess* proving function in CAPS.
- **Alias decoders** (`.decode`) — the single biggest trap here is one molecule
  with four names (CD21 = CR2 = C3dR = EBV-R). §1.2 is the table to read first.
- **Molecule and complex cards** (`.mol`) — a fixed frame for CD3, MHC I, MHC
  II and the NLRP3 inflammasome.

## What is specific to these two lectures

- **§9.4** compares T-cell activation with the inflammasome row by row. It is
  the reason the two lectures are in one guide.
- **§3.4** keeps the lecturer's own **hot dog / pita** analogy for the closed
  class I and open class II clefts, and explains why the shapes follow the
  machinery that fills them (proteasome vs endosomal cathepsins).
- **§2.1** keeps his **car** analogy for the three signals and carries it
  through Parts 2 and 7.
- Two slide errors are flagged neutrally rather than reproduced silently: the
  BAFF receptor is **CD268**, not CD168 (§1.3), and the STAT family has
  **seven** members, the seventh being STAT6, which appears by name on the
  lecturer's own Th1/Th2 figure (§4.5).
- **§5.2** flags that the isotype-switching table lists **mouse** IgG
  subclasses (IgG2a, IgG2b); the biology transfers, the numbers do not.
- **§7.5** flags that **caspase-11 is a mouse gene**; the human equivalents are
  caspase-4 and caspase-5.

## Notes on the source

Figures were extracted from the two lecture PDFs and audited image by image
against the slides. Twenty-five extracted objects were WordArt text fragments
rather than figures and were discarded. One figure — the poxvirus
cytokine-decoy map, which appears in both decks — lost all its labels in
extraction because they were slide text boxes, so §5.6 presents that content
as **Table 5.4** instead.

Images are JPEG and capped at 1400 px wide: WeasyPrint passes JPEG through
unchanged but re-encodes PNG, and the cap keeps the English PDF under 8 MB.

## Rebuilding

```bash
pip install weasyprint beautifulsoup4 pymupdf
python3 build.py both ../output      # or: en / bi
```

Rendering takes about 20 seconds per edition.
