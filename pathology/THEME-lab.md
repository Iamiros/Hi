# Pathology Laboratory, "Specimen Lightbox"

Locked visual identity for every Pathology Lab session (the lecture course,
`pathology/THEME.md`, is separate: light paper, "Clinical Case File"). First
written for Lab Session 3; reuse unchanged for every later lab session.

## Design read

Recognition and description at the microscope and specimen jar, for spot
exams. Image-led field manual; text is minimal and structured. Dials,
variance 4, motion 1, density 3.

## Type

- Display + body: **Space Grotesk** (400/500/700).
- Specimen numbers, magnifications, mono data: **JetBrains Mono** (400/500/700).
- Persian: **Vazirmatn**.

## Colour tokens

Dark throughout, so micrographs and gross photos glow like a lightbox held
up in a dim room.

| Token | Hex | Use |
|---|---|---|
| `--bg` | `#111316` | page background |
| `--surface` | `#1B1E22` | cards, tables, panels |
| `--surface-2` | `#22262B` | nested/alternating surface |
| `--text` | `#E7E9EC` | body text |
| `--text-2` | `#AEB4BB` | secondary text |
| `--text-3` | `#7C8389` | captions, meta |
| `--rule` | `#2C3036` | hairlines |
| `--accent` | `#E8C547` | specimen-label yellow, the primary accent |
| `--accent-dim` | `#4A4126` | yellow tint for backgrounds |
| `--gross` | `#D9678A` | GROSS tag (eosin, dimmed for dark bg) |
| `--micro` | `#8B85D9` | MICRO tag (haematoxylin, dimmed for dark bg) |
| `--amber` | `#E0A040` | exam traps |
| `--clin` | `#6FA8D9` | clinical correlation |

## Layout

Single wide column, image-led. Specimen photos run large and close to full
bleed; text sits below or beside in a narrow structured block, never
competing with the image for attention.

## Signature devices

- **Specimen card**, a full-width real image (gross or micrograph) with
  numbered pointer circles burned into the source photo where present, a
  legend beside or below it, then the description template.
- **Description template**, a fixed order every time: organ; gross (size,
  surface, cut surface, colour, consistency) or, for a slide, architecture,
  cells, key feature; then diagnosis.
- **Two tags**, `GROSS` (accent pink) and `MICRO` (accent violet), marking
  where an observation comes from.
- **Low-power to high-power pairs** where the deck has both.
- **Look-alike pairs**, e.g. wet vs. dry gangrene, coagulative vs. caseous
  vs. liquefactive necrosis, side by side.
- **Spot-exam practice page**, image and specimen number only, answers
  collected at the end.
- **End-of-lab identification checklist.**

## Do / don't

- Do: keep every image real, extracted from the lab's own deck; never
  redraw a specimen as a diagram.
- Do: reserve `--accent` (yellow) for the specimen-label device; don't spend
  it as a general highlight colour.
- Don't: em dash or en dash anywhere. Use a comma, colon, or period.
- Don't: let a caption's Persian translation crowd the image; keep it below,
  never overlaid.
