from playwright.sync_api import sync_playwright
import pathlib,glob
CH=glob.glob('/opt/pw-browsers/chromium-1194/chrome-linux*/chrome')[0]
r=pathlib.Path(__file__).resolve().parent.parent/'tracker'
svg=(r/'icon.svg').read_text()
with sync_playwright() as p:
    b=p.chromium.launch(executable_path=CH)
    for s in (180,192,512):
        pg=b.new_page(viewport={'width':s,'height':s})
        tag='<svg width="%d" height="%d" ' % (s,s)
        pg.set_content('<body style="margin:0">'+svg.replace('<svg ',tag,1)+'</body>')
        pg.screenshot(path=str(r/('icon-%d.png'%s)))
    b.close()
