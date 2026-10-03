# 8-Week Cut

Whole-body strength, muscle retention, fat loss and a first strict muscle-up, for Amir. Persian UI, English exercise names.

| Path | What |
|---|---|
| `tracker/index.html` | GRIP: interactive 8-week tracker (single file, fonts embedded, works offline, installable) |
| `guide/index.html`, `guide/guide.pdf` | Full guide: energy math, nutrition, program, exercise library, challenges, tests, safety, science, cheat sheet |
| `docs/TOOLING.md`, `docs/DECISIONS.md` | Tools used, corrections and decisions |
| `tools/` | Source data (`program.py`) and build scripts |

## Open it
Open `tracker/index.html` in a browser (double-click), or host the repo folder on any static host (GitHub Pages, Netlify). Offline caching and install need `https://` or `localhost`.

## Install on iPhone
1. Open the hosted `tracker/index.html` in Safari.
2. Tap Share, then **Add to Home Screen**.
3. Open it from the home screen. After the first load it works without internet.

## Back up your data
Data lives only in the browser on that device. In **Settings**: *Export JSON* (full backup, also gives a share sheet on iPhone), *Import JSON* (restores, asks before replacing), *Export CSV* (for spreadsheets). Export once a week.

## Rebuild
```
python3 tools/build_tracker.py   # tracker/index.html, sw.js, manifest
python3 tools/build_guide.py     # guide/index.html
python3 tools/export_pdf.py      # guide/guide.pdf (needs playwright + chromium)
```
Edit program numbers only in `tools/program.py`; both outputs read from it.

Fonts: Vazirmatn and Barlow Condensed, SIL Open Font License 1.1.
- Exercise images: free-exercise-db (github.com/yuhonas/free-exercise-db), Unlicense / public domain.
