import pathlib, sys, pymupdf
from playwright.sync_api import sync_playwright

here = pathlib.Path(__file__).parent
src = (here / "demo.html").as_uri()
out = here / "Talking-Between-Cells-demo.pdf"

with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/opt/pw-browsers/chromium")
    pg = b.new_page()
    pg.goto(src, wait_until="networkidle")
    pg.evaluate("document.fonts.ready")
    over = pg.evaluate("""() => [...document.querySelectorAll('.page')].map((s,i)=>{
      const r=s.getBoundingClientRect(); let worst=0;
      s.querySelectorAll('*').forEach(e=>{ if(e.closest('.foot'))return; const q=e.getBoundingClientRect(); worst=Math.max(worst,q.bottom-r.top);});
      return [i+1, Math.round(worst), Math.round(r.height)];})""")
    print("content bottom vs page height (px):", over)
    pg.pdf(path=str(out), prefer_css_page_size=True, print_background=True)
    b.close()

d = pymupdf.open(out)
print("pages:", len(d))
for i, page in enumerate(d):
    page.get_pixmap(dpi=int(sys.argv[1]) if len(sys.argv) > 1 else 110).save(here / f"out_{i+1}.png")
