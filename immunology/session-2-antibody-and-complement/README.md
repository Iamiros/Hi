# Medical Immunology — Session 2: Antibody and Complement

Sources for `immunology-session2-english.pdf` (72 pp) and
`immunology-session2-bilingual.pdf` (117 pp).

Covers Lecture 2 of the Medical Immunology course: the structure of the
antibody molecule, where its diversity comes from, the five classes and their
functions, monoclonal antibodies in the clinic, and the complement system end
to end — the three activation pathways, the terminal pathway, regulation,
the six biological functions, and complement disease.

## Layout

| Path | Contents |
|---|---|
| `src/build/*.html` | Content, in reading order. One master copy serves both editions. |
| `src/build/base.css` | Page setup, typography, callouts, tables, molecule cards, cascade strips, PDF bookmarks. |
| `src/build/bilingual.css` | Overlay applied only to the bilingual edition (RTL blocks, Persian type). |
| `src/img/` | Figures extracted from the lecture deck. |
| `src/fonts/` | Source Serif 4, Inter, Vazirmatn (all OFL). |
| `src/build.py` | Assembles the parts and renders both PDFs with WeasyPrint. |

Parts, in `build.py`'s `PARTS` order:

1. `02_part1` — The Antibody Molecule: two ends, two jobs
2. `03_part2` — Where diversity comes from (V(D)J, isotype/allotype/idiotype)
3. `04_part3` — The five classes and what they do
4. `05_part4` — Making and using antibodies (hybridoma, therapeutic mAbs)
5. `06_part5` — Complement: the cast and the three pathways
6. `07_part6` — Complement: regulation, function, disease
7. `08_review` — Master tables, look-alikes, 24-question self-test, glossary

Shares the `<fa>` bilingual convention with the other guides in this
repository: Persian is written inline inside the English source wrapped in
`<fa>…</fa>`, and `build.py` either deletes every `<fa>` block (English
edition) or converts it to a styled RTL block (bilingual edition). One source,
two editions, permanently in sync.

## The method designed for this subject

Immunology is a large cast of molecules with confusingly similar names acting
at a distance. The guide is built on the claim that **every fact in this
lecture is the answer to one of four questions** — *what is it? what does it
bind? what does it do? what breaks if it is gone?* — and on six devices that
each answer one of them:

- **Molecule cards** (`.mol`) — a fixed six-row frame for every immune
  molecule, so the same question is asked of IgG, of IgA, of the classical
  pathway and of hereditary angioedema.
- **Pathway tags** `CP` `LP` `AP` `TP` — every complement component is tagged
  with the pathway(s) it belongs to, so the cast list stops being a list.
- **End tags** `V` `C` — every antibody property is tagged as belonging to the
  variable (recognition) end or the constant (effector) end.
- **Absence proves function** (`.box.absent`) — the deficiency disease used as
  the evidence for the function: selective IgA deficiency, PNH, C3 deficiency.
- **Cascade strips** (`.casc`) — the three pathways as hand-written inline SVG,
  drawn to the same template so the divergence and the convergence are visible
  at a glance.
- **Name decoders** (`.decode`) — how to *read* C3a, C4b2a, iC3b, C̄1 and the
  monoclonal-antibody suffixes, with a worked example, rather than memorising
  them.

Two organising ideas carry the whole lecture and are stated on the title page,
restated in each Part opener and closed in §7.5: an antibody is **one molecule
with two ends**, and complement is **thirty proteins with one event** — the
cleavage of C3 — reached by three doors and restrained at three points.

## What is specific to this session

- **§5.1** and **§6.2** are built around decoders rather than lists, because
  the examinable skill is reading an unfamiliar symbol, not reciting a
  memorised one.
- **Table 7.2** answers the lecturer's stated exam objective verbatim
  (*"Review the differences between the three activation pathways of
  complement"*), and **Fig 7.1** is the same table drawn.
- **§6.4** derives hereditary angioedema rather than listing it: C1-INH
  restrains four plasma cascades, so its loss releases bradykinin, which is
  why antihistamines and adrenaline fail and why ACE inhibitors are
  contraindicated.
- **C2a vs C2b** is flagged as an Exam Trap: this course uses the older
  convention in which the *large* fragment of C2 is C2a and the classical C3
  convertase is written C4b2a. Some modern texts reverse it.

## Notes on the source

Figures are extracted from the lecture `.pptx`. The extraction was audited
image by image against the slides — several were initially mapped one position
out (the MBL/ficolin panel, the C1-INH panel, the cytolysis and opsonisation
panels), and the names in `img/` now match their content.

Images are JPEG rather than PNG: WeasyPrint passes JPEG through unchanged but
re-encodes PNG, which keeps the English PDF under 5 MB.

## Rebuilding

```bash
cd src
pip install weasyprint beautifulsoup4 pymupdf
python3 build.py both ..             # or: en / bi
```

Rendering takes about 15 seconds per edition.
