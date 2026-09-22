# Session 3 — Disorders of Vascular Flow (generator)

Sources for `output/pathology-session3-english.pdf` and
`output/pathology-session3-bilingual.pdf`.

## Layout

| Path | Contents |
|---|---|
| `build/*.html` | Content, in reading order. One master copy serves both editions. |
| `build/base.css` | Page setup, typography, callouts, tables, figures, PDF bookmarks. |
| `build/bilingual.css`| Overlay applied only to the bilingual edition (RTL blocks, Persian type). |
| `img/` | Figures extracted from the source PDFs. |
| `fonts/` | Source Serif 4, Inter, Vazirmatn (all OFL). |
| `build.py` | Assembles the parts and renders both PDFs with WeasyPrint. |

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

## Rebuilding

```bash
pip install weasyprint beautifulsoup4 pymupdf
python3 build.py both ../output      # or: en / bi
```

Rendering takes about a minute per edition.
