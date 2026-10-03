from playwright.sync_api import sync_playwright
import glob, pathlib
CH = glob.glob('/opt/pw-browsers/chromium-1194/chrome-linux*/chrome')[0]
root = pathlib.Path(__file__).resolve().parent.parent
out = pathlib.Path('/tmp/claude-0/-home-user-Hi/54b47da7-daf8-5c46-b909-aca8dd4b7c8f/scratchpad/bidi'); out.mkdir(exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=CH)
    pg = b.new_page(viewport={'width': 390, 'height': 844}, device_scale_factor=1)
    pg.goto((root / 'tracker/index.html').as_uri()); pg.wait_for_timeout(400)
    pg.screenshot(path=str(out/'today.png'), full_page=True)
    pg.click('[data-act=next]'); pg.wait_for_timeout(150); pg.screenshot(path=str(out/'sun.png'), full_page=True)
    pg.click('[data-act=next]'); pg.wait_for_timeout(150); pg.screenshot(path=str(out/'mon.png'), full_page=True)
    for tab,n in [('غذا','food'),('برنامه','plan'),('آمار','stats'),('تنظیمات','set')]:
        pg.click(f'nav.tabs >> text={tab}'); pg.wait_for_timeout(250); pg.screenshot(path=str(out/f'{n}.png'), full_page=True)
    pg.click('nav.tabs >> text=غذا'); pg.wait_for_timeout(150)
    pg.locator('[data-act=fadd]').first.click(); pg.wait_for_timeout(200); pg.screenshot(path=str(out/'fsheet.png'))
    pg.locator('[data-act=fpick]').first.click(); pg.wait_for_timeout(200); pg.screenshot(path=str(out/'fsheet2.png'))
    b.close()
