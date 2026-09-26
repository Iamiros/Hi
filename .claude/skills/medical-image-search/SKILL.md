---
name: medical-image-search
description: Find and download real, openly licensed medical images (gross specimens, histology and pathology micrographs, radiology, anatomy plates, microbiology cultures) from Openverse, Wikimedia Commons and NIH Open-i, with licence and attribution captured. Use whenever a study guide needs a real image the lecture file does not already contain.
---

# Medical image search

Order of preference: figures already in the lecture file (extract with PyMuPDF) → the sources below → your own diagram. Never use a generated image where a real specimen or micrograph is expected.

Always send a descriptive User-Agent; Wikimedia returns 403/429 without one, and still rate-limits shared cloud IPs, so the `get` helper below retries with back-off.

```bash
UA='MedStudyGuides/1.0 (https://github.com/Iamiros/Hi)'
get(){ for i in 1 2 3 4; do out=$(curl -s -A "$UA" -w '\n%{http_code}' "$1"); [ "${out##*$'\n'}" = 200 ] && { printf '%s' "${out%$'\n'*}"; return; }; sleep $((i*5)); done; echo "failed: $1" >&2; }
```
Use `get URL` instead of bare curl for Wikimedia (it rate-limits shared cloud IPs).

## 1. Openverse (fastest; aggregates Wikimedia Commons, Flickr CC, museums)

```bash
curl -s -A "$UA" 'https://api.openverse.org/v1/images/?q=nutmeg+liver&page_size=20&license_type=all' \
 | python3 -c "import json,sys;[print(r['license'],r['license_version'],'|',r['creator'],'|',r['title'][:60],'|',r['url'],'|',r['foreign_landing_url']) for r in json.load(sys.stdin)['results']]"
```
Useful filters: `&source=wikimedia`, `&license=by,by-sa,cc0,pdm`, `&aspect_ratio=wide`, `&size=large`.

## 2. Wikimedia Commons (best for classic pathology/histology/anatomy plates; Gray's Anatomy plates are public domain)

```bash
# search files
get 'https://commons.wikimedia.org/w/api.php?action=query&list=search&srnamespace=6&srlimit=20&format=json&srsearch=granuloma+H%26E'
# url + licence + author for chosen titles
get 'https://commons.wikimedia.org/w/api.php?action=query&prop=imageinfo&iiprop=url|extmetadata&iiurlwidth=1600&format=json&titles=File:Nutmeg_liver.jpg'
```
Read `extmetadata.LicenseShortName`, `Artist`, `Credit`. Use `thumburl` (width 1600) for print quality without huge files. Category browsing: `list=categorymembers&cmtitle=Category:Histology_of_the_liver&cmtype=file`.

## 3. NIH Open-i (open-access figures from PubMed Central: clinical photos, radiology, micrographs)

```bash
curl -s -A "$UA" 'https://openi.nlm.nih.gov/api/search?query=caseating+granuloma&m=1&n=20&it=g' \
 | python3 -c "import json,sys;d=json.load(sys.stdin);[print(x.get('uid'),'|',x.get('title','')[:60],'|','https://openi.nlm.nih.gov'+x.get('imgLarge',''),'|',x.get('pmcid')) for x in d.get('list',[])]"
```
`it=` image type filter: `g` graphics/photos, `x` x-ray, `c` CT, `m` MRI, `u` ultrasound, `mc` microscopy. Open-i figures are from PMC open-access articles; the API gives no licence field, so open `https://www.ncbi.nlm.nih.gov/pmc/articles/<pmcid>/` (or the PubMed MCP) and confirm the article licence before use; keep the PMCID for attribution.

## Rules

- Licences allowed without asking: CC0, Public Domain / PDM, CC BY, CC BY-SA. Avoid NC/ND unless the user approves (study guides are personal, but stay clean).
- Save to `src/img/` with a descriptive name; keep a `src/img/CREDITS.md` line per image: file, title, author, licence, source URL.
- Check resolution before use (>= 1200 px on the long side for a full-width figure). Crop with PyMuPDF/Pillow, never upscale.
- Look at every candidate image before using it: it must actually show the named feature, at a sensible magnification, with correct stain and label. Wrong-image errors are scientific errors (review pass A).
- Caption each image with what to look at, and a short credit line ("Wikimedia Commons, CC BY-SA 4.0, Author").
