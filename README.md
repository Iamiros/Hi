# Study guides — MBBS, Zhejiang University School of Medicine

Bilingual (English + Persian) study guides built from course lecture material.
**One folder per session.** Each folder holds the finished PDFs, a README
describing that guide and its method, and a `src/` folder with everything
needed to rebuild it.

## Contents

### Immunology

| Session | Guide | Pages (EN / BI) |
|---|---|---|
| [Session 2](immunology/session-2-antibody-and-complement) | Antibody and Complement | 72 / 117 |
| [Sessions 3 & 4](immunology/sessions-3-4-immune-molecules-and-innate-immunity) | Immune Molecules and Innate Immunity | 93 / 152 |

### Microbiology

| Session | Guide | Pages (EN / BI) |
|---|---|---|
| [Session 1](microbiology/session-1-foundations) | Foundations — the bacterial cell | 88 / 145 |

### Pathology

| Session | Guide | Pages (EN / BI) |
|---|---|---|
| [Session 2](pathology/session-2-cell-injury-necrosis-and-repair) | Cell Injury, Necrosis and Repair | — / 60 |
| [Session 3](pathology/session-3-disorders-of-vascular-flow) | Disorders of Vascular Flow | 91 / 159 |
| [Lab 1](pathology/lab-1-introduction) | Laboratory — Introduction | 39 / 67 |
| [Lab 2](pathology/lab-2-cell-and-tissue-injury) | Laboratory — Cell and Tissue Injury | 41 / 68 |

## How each folder is arranged

```
<course>/<session>/
  ├── <name>-english.pdf      finished guide, English only
  ├── <name>-bilingual.pdf    finished guide, English + Persian
  ├── README.md               what it covers, and the method designed for it
  └── src/
      ├── build/              content (HTML) and the two stylesheets
      ├── img/                figures
      ├── fonts/              Source Serif 4, Inter, Vazirmatn (all OFL)
      └── build.py            renders both PDFs with WeasyPrint
```

## The shared convention

Every guide is written **once** and rendered twice. Persian is written inline
inside the English source, wrapped in `<fa>…</fa>`, and `build.py` either
deletes every `<fa>` block (English edition) or converts it to a styled
right-to-left block (bilingual edition). One source, two editions, permanently
in sync.

To rebuild any guide:

```bash
cd <course>/<session>/src
pip install weasyprint beautifulsoup4 pymupdf
python3 build.py both ..      # or: en / bi
```

Each guide has its own design system and its own set of teaching devices,
chosen for the subject — specimen cards and description templates for the
pathology labs, bug cards and Gram tags for microbiology, molecule cards and
pathway tags for immunology. The per-session README explains the method that
guide uses.
