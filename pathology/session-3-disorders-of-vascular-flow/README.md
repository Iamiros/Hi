# Pathology — Session 3: Disorders of Vascular Flow

`pathology-session3-english.pdf` (91 pp) and `pathology-session3-bilingual.pdf` (159 pp).

## Layout

| Path | Contents |
|---|---|
| `src/build/*.html` | Content, in reading order. One master copy serves both editions. |
| `src/build/base.css` | Page setup, typography, callouts, tables, figures, PDF bookmarks. |
| `src/build/bilingual.css` | Overlay applied only to the bilingual edition (RTL blocks, Persian type). |
| `src/img/` | Figures extracted from the source PDFs. |
| `src/fonts/` | Source Serif 4, Inter, Vazirmatn (all OFL). |
| `src/build.py` | Assembles the parts and renders both PDFs with WeasyPrint. |

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
cd src
pip install weasyprint beautifulsoup4 pymupdf
python3 build.py both ..             # or: en / bi
```

Rendering takes about a minute per edition.
