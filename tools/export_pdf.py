import glob, pathlib, subprocess, time
from playwright.sync_api import sync_playwright
CH=glob.glob('/opt/pw-browsers/chromium-1194/chrome-linux*/chrome')[0]
root=pathlib.Path(__file__).resolve().parent.parent
sp='/tmp/claude-0/-home-user-Hi/54b47da7-daf8-5c46-b909-aca8dd4b7c8f/scratchpad/shots'
with sync_playwright() as p:
    b=p.chromium.launch(executable_path=CH)
    pg=b.new_page(viewport={'width':1000,'height':900})
    pg.goto('file://'+str(root/'guide/index.html')); pg.wait_for_timeout(800)
    pg.screenshot(path=sp+'/guide-screen.png',full_page=True)
    pg.pdf(path=str(root/'guide/guide.pdf'),format='A4',print_background=True,prefer_css_page_size=True)
    b.close()
