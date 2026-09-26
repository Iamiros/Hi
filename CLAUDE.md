# STANDING INSTRUCTIONS FOR ALL MY MEDICAL STUDY FILES

You are building study materials for my MBBS courses (Zhejiang University School of Medicine) in this repo. Every file I give you (lecture PDFs, slides, notes) becomes a modern, professional, visually powerful study guide. The quality bar is the "Talking Between Cells" demo (designs/immunology-demo, branch claude/taste-plugin-designs-3mx1t1): editorial precision, real figures, purpose-built diagrams, dense but readable tables, zero clutter. Match that quality, NOT its look. Each course has its own theme (section 3).

Courses: Pathology, Pathology Lab, Immunology, Microbiology, Histology, Anatomy.

## 0. Session setup (automatic)
`.claude/settings.json` declares the plugin marketplaces and `.claude/hooks/session-start.sh` installs them, plus the PDF build tools (pymupdf, playwright, weasyprint, beautifulsoup4), at the start of every web session. Plugins: document-skills, taste-skill, caveman, ponytail, ecc, storybook.
1. Confirm with `claude plugin list`. If anything is missing, run `CLAUDE_CODE_REMOTE=true .claude/hooks/session-start.sh` and continue; newly installed skills load in the next session, so meanwhile read their SKILL.md directly from `~/.claude/plugins/cache/`.
2. Read the course's THEME.md (section 3) and the README of the latest guide for that course.
3. If any part of the job would be done better by a plugin or MCP server that is not installed (image search, image generation, figure/diagram tools, PubMed/citation lookup, OCR), find it (SearchPlugins / SearchMcpRegistry) and install or suggest it. Use the best tool for each part, never a weaker default. If it should be permanent, add it to `.claude/settings.json` and the hook.

## 1. Skills and plugins on every file
- taste-skill:taste-skill for every design decision: brief read, three dials, anti-slop rules, full pre-flight checklist, zero em/en dashes. Pull in minimalist-skill, soft-skill, brutalist-skill, redesign-skill, brandkit or stitch-skill when the course theme calls for them.
- The matching document skill: pdf, pptx, docx, xlsx.
- dataviz for every chart, graph, heatmap, stat tile or numeric table.
- artifact-diagramming know-how for mechanism diagrams, drawn as clean SVG that shows the real mechanism.
- taste-skill:output-skill so nothing is truncated or left as a placeholder.
- Token saving in every chat: caveman and ponytail are installed for this, and ecc's context-budget / token-budget-advisor skills are available. Also work efficiently: extract source text once to the scratchpad, read only the pages needed, delegate bulk reading to subagents, render review PNGs at low DPI. Keep user-facing replies short; never let token saving reduce the quality or completeness of the study files themselves.

## 2. Images and figures (full freedom, any source, any plugin)
1. Extract the real figures from my lecture file first (PyMuPDF), because they match what the lecturer teaches.
2. Open-licence sources via web search/fetch: Wikimedia Commons, OpenStax, NIH/CDC/PHIL, public pathology and histology image banks. Use real micrographs, gross specimens, radiology and anatomy plates wherever they teach.
3. Use image generation, if available, for concept illustrations only, never for micrographs or specimens that must be real.
4. Build your own diagrams, flowcharts, charts and comparison graphics wherever they teach better than a photo.
Every image gets a teaching caption saying what to look at. No decorative images.

## 3. Course themes (designed with taste-skill; one per course, locked across all its sessions)
The first time a course is built, write `<course>/THEME.md` (stitch-skill DESIGN.md style: design read, dials, colour and type tokens, components, do/don't list) from the spec below, then reuse it for every later session of that course. All themes use Vazirmatn for Persian. Latin fonts must cover Greek (α β γ κ) where the subject needs it, and italics where species names appear. Render with Playwright Chromium (/opt/pw-browsers/chromium). Each theme has its own layout language, not just its own colours.

### Pathology (lectures): "Clinical case file"
- Design read: disease-by-disease teaching of cause, mechanism, morphology and consequence, for students who must reason from a lesion to a patient. Editorial medical-journal language. Dials: variance 5, motion 1, density 6.
- Type: Commissioner (display + body), IBM Plex Mono for tags and lab values.
- Colour: cool paper #F5F6F7, ink #16181D, accent eosin #B8336A. Haematoxylin #3E3A8C appears only as the MICRO tag colour; GROSS tag in eosin.
- Layout: two-column editorial page with a narrow margin rail for sidenotes (key terms, definitions, eponyms).
- Signature devices: a causal-chain rail at the top of every disease (Etiology → Pathogenesis → Gross → Micro → Clinical → Complications); gross and micro split panels with real images side by side; case vignette boxes; morphology decoders ("nutmeg liver means..."); time-course graphs (e.g. infarct changes by hours/days); cascade diagrams; look-alike comparison tables.

### Pathology Lab: "Specimen lightbox"
- Design read: recognition and description at the microscope and specimen jar, for spot exams. Image-led field manual; text is minimal and structured. Dials: variance 4, motion 1, density 3.
- Theme: DARK throughout, so micrographs glow like a lightbox. Background #111316, surface #1B1E22, text #E7E9EC, accent specimen-label yellow #E8C547.
- Type: Space Grotesk (display + body), JetBrains Mono for specimen numbers and magnifications.
- Signature devices: specimen cards (a full-width real image with numbered pointer circles on it and a legend beside it); a "describe it like this" template (organ, size, surface, cut surface, colour, consistency, then micro: architecture, cells, key feature); low-power → high-power zoom pairs; microscope look-alike pairs; spot-exam practice pages (image and number only, answers at the end); an end-of-lab identification checklist.

### Immunology: "Signal network map"
- Design read: a cast of molecules talking across cells through receptors, cascades and signals. Systems-schematic language: pathways drawn like a transit map. Dials: variance 6, motion 1, density 6.
- Type: Manrope (display + body), IBM Plex Mono for CD numbers, cytokines and genes.
- Colour: cool white #F4F6F8, ink #121826, accent cobalt #2F5BEA. Pathway "lines" may carry a small fixed set of semantic colours, used only inside network maps.
- Signature devices: transit-map pathway diagrams (molecules as stations, cascades as lines, interchanges where pathways meet); partner cards (ligand on cell A ↔ receptor on cell B, and the result); signal/pathway tags on every molecule; "absence proves function" deficiency boxes; response-curve graphs (primary vs secondary antibody titre, cytokine kinetics); master CD, cytokine and receptor tables.

### Microbiology: "Field guide to the organisms"
- Design read: organism-by-organism memorisation plus identification logic in the lab. Field-guide language: each organism is an entry with identifying marks. Dials: variance 5, motion 1, density 7.
- Type: Fira Sans (display + body; has Greek and true italics for genus and species names), Fira Code for test results and doses.
- Colour: lab white #F6F7F7, ink #14181A, accent culture amber #C27C0E. Gram-positive violet #5B2A86 and Gram-negative pink #C2477A are semantic tags only.
- Signature devices: bug cards as field-guide entries (real micrograph or culture image, Gram tag, shape and arrangement icon, O2 requirement, key virulence factors, diseases, lab identification, treatment); dichotomous identification flowcharts (Gram → shape → catalase → coagulase...); classification trees; virulence factor → mechanism → disease tables; antibiotic spectrum heatmaps (organism × drug grid); epidemiology charts.

### Histology: "Micrograph gallery"
- Design read: learning to see tissue structure and link it to function. Art-book / museum-gallery language: large images, generous whitespace, fine annotations. Dials: variance 7, motion 1, density 3.
- Type: Figtree (display + body, with italics), Geist Mono for magnifications and stains.
- Colour: neutral gallery grey #F3F3F1, ink #1A1C1E, accent deep teal #1E6B5C (chosen to sit calmly beside pink and purple H&E images).
- Signature devices: annotated micrograph plates with thin leader lines and scale bars; zoom ladders (organ → tissue → cell → ultrastructure, LM vs EM); a stain legend (H&E, PAS, trichrome, silver, what each colours); identification decision trees (e.g. classifying epithelium); structure → function tables; "tell them apart" micrograph pairs (e.g. ureter vs vas deferens).

### Anatomy: "Technical atlas"
- Design read: spatial learning of regions, layers, relations, and the courses of vessels and nerves, tied to clinical deficits. Swiss-grid technical-drawing / engineering-plate language (brutalist-skill precision, kept clean). Dials: variance 5, motion 1, density 7.
- Type: Archivo (display + body), Archivo Narrow for dense tables, JetBrains Mono for callout numbers and spinal root values.
- Colour: drafting white #F4F5F6, ink #111418, accent surgical green #0E7C66. Anatomical convention colours are semantic only: arteries red #C8302C, veins blue #2F5DA8, nerves yellow #E0B000, lymphatics purple #6B4FA0.
- Signature devices: numbered-callout plates (circled numbers on the figure, key list beside); layer stacks (skin → bone sequences); a relations compass around a structure (anterior, posterior, medial, lateral, superior, inferior); nerve and vessel route maps (course drawn through landmarks); OIA master tables (origin, insertion, innervation with root values, action, blood supply); "if this nerve is cut" deficit tables; dermatome and myotome maps; cross-sections at named vertebral levels.

## 4. Content standard
- Complete coverage of the lecture, enriched from the standard textbooks (Robbins; Abbas / Janeway; Murray / Sherris; Junqueira / Ross; Gray's / Moore / Netter). Mark what goes beyond the slides.
- Rich in accurate, practical tables (comparison, look-alike, master, classification, drug/target), graphs wherever there is quantitative data, a diagram for every mechanism, plus mnemonics, exam traps, clinical correlations, self-test Q&A and a glossary.
- Default output is two PDFs: English and bilingual (English + Persian). Persian is written inline as `<fa>…</fa>` in one master source, and the build script strips it (English edition) or renders it as RTL blocks (bilingual edition). Make PPTX/DOCX/XLSX when I ask, using the same course theme.
- Repo convention: `<course>/<session>/` containing both PDFs, a README (coverage + method) and `src/` (build script, HTML, CSS, img, fonts). Commit and push to the session's branch.

## 5. Mandatory review: TWO full passes after building, before delivering
Do the whole check twice: build, review, fix, re-render, review again, fix. Only then deliver.
A. Scientific accuracy: check every fact, number, unit, drug, gene/CD/cytokine name, Greek letter, eponym, classification and species name (italicised) against the lecture and the standard textbook. No invented numbers. The Persian must say exactly what the English says, with correct Persian medical terminology.
B. Design: render every page to PNG and inspect it. Check for overflow, clipped text, orphaned headings, broken tables, widows, image resolution, theme consistency (colour, type, radius, components per THEME.md), and the taste-skill pre-flight list (zero em/en dashes).
C. Bilingual: check RTL/LTR mixing (Latin terms, numbers, units and formulas inside Persian must be bidi-isolated and in the right order), Persian punctuation and line-height, missing glyphs or tofu boxes, Persian in tables, captions and callouts, and Persian blocks splitting badly across pages. The dark theme (Pathology Lab) needs its own contrast check for Persian text.
Report briefly what each pass found and fixed.

## 6. How to talk to me
Answer in the language I write in. Be brief. No moral commentary. Do exactly what I ask, completely, without cutting corners.
