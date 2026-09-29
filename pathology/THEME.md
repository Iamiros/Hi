# Pathology, "Clinical Case File"

Locked visual identity for every Pathology lecture guide (Pathology Lab has
its own separate theme). Written the first time a guide is built under the
CLAUDE.md course-theme system; reuse unchanged for every later session.

## Design read

Disease-by-disease (or, for general pathology, mechanism-by-mechanism)
teaching of cause, process, and consequence, for students who must reason
from a lesion or a mechanism to a patient. Editorial medical-journal
language: confident, precise, unadorned. Dials, variance 5, motion 1,
density 6.

## Type

- Display + body: **Commissioner** (400/500/600/700, latin + greek subsets
  so α β γ κ set natively; italic for species names and emphasis).
- Tags, lab values, CD/gene numbers, callout numbers: **IBM Plex Mono**
  (400/500/600/700).
- Persian: **Vazirmatn** (regular/medium/bold).

## Colour tokens

| Token | Hex | Use |
|---|---|---|
| `--paper` | `#F5F6F7` | page background |
| `--ink` | `#16181D` | body text |
| `--ink-2` | `#42474F` | secondary text |
| `--ink-3` | `#6E7580` | captions, meta |
| `--rule` | `#D8DCE1` | hairlines |
| `--rule-2` | `#E9ECEF` | faint hairlines |
| `--eosin` | `#B8336A` | primary accent, section heads, GROSS tag, high-yield |
| `--eosin-bg` | `#FAEEF3` | eosin tint |
| `--haem` | `#3E3A8C` | MICRO tag only, never used as a general accent |
| `--haem-bg` | `#EEEDF8` | haematoxylin tint |
| `--amber` | `#8A5200` | exam traps |
| `--amber-bg` | `#FDF6EA` | amber tint |
| `--slate` | `#2D4A6B` | clinical correlation |
| `--slate-bg` | `#F1F5F9` | slate tint |

## Layout

Two-column editorial page: A4, running header (part title / section title),
running footer (page number). Body copy runs in two justified columns; a
narrow **margin rail** (~32mm) carries sidenotes, key terms, definitions,
eponyms, unit conversions, set in Plex Mono, tied to their paragraph by a
short rule, not a footnote number.

## Signature devices

- **Process rail**, a horizontal strip of stage-pills at the top of every
  major topic, e.g. `INJURY → VASCULAR PHASE → CELLULAR PHASE → MEDIATORS →
  OUTCOME`, the general-pathology analogue of the disease causal chain
  (`Etiology → Pathogenesis → Gross → Micro → Clinical → Complications`
  once the course reaches organ-specific disease).
- **Gross/Micro split panels**, real images side by side, GROSS tagged
  eosin, MICRO tagged haematoxylin.
- **Case vignette boxes**, slate rule, a short clinical stem.
- **Morphology / concept decoders**, "X means Y" callouts translating a
  sign or term into its mechanism.
- **Cascade diagrams**, purpose-built SVG for every mechanism (adhesion
  cascade, phagocytosis, arachidonic-acid pathway, complement/kinin/
  coagulation cross-talk), drawn in the theme palette, never a reused
  textbook scan.
- **Look-alike / master comparison tables**, dense, bordered, Plex Mono
  for values.
- **Time-course graphs**, dataviz-skill charts for anything quantitative.

## Do / don't

- Do: real micrographs and gross specimens wherever the lecture or an
  open-licence source has one; redraw every schematic/mechanism figure as
  a clean on-theme SVG.
- Do: keep haematoxylin `--haem` reserved for the MICRO tag; don't use it
  as a decorative accent elsewhere.
- Do: italicise genus/species and Latin/Greek terms; set Greek letters in
  Commissioner (native glyph coverage), never a substitute font.
- Don't: em dash or en dash anywhere (taste-skill pre-flight). Use a comma,
  colon, or period instead.
- Don't: decorative clip-art. Every image carries a teaching caption.
