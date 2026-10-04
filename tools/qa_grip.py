from playwright.sync_api import sync_playwright
import glob, pathlib
CH = glob.glob('/opt/pw-browsers/chromium-1194/chrome-linux*/chrome')[0]
root = pathlib.Path(__file__).resolve().parent.parent
out = pathlib.Path('/tmp/claude-0/-home-user-Hi/54b47da7-daf8-5c46-b909-aca8dd4b7c8f/scratchpad/grip'); out.mkdir(exist_ok=True)
errs = []
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=CH)
    for scheme in ("dark", "light"):
        pg = b.new_page(viewport={'width': 390, 'height': 844}, color_scheme=scheme)
        pg.on('pageerror', lambda e: errs.append(str(e))); pg.on('console', lambda m: m.type == 'error' and errs.append(m.text))
        pg.add_init_script("addEventListener('DOMContentLoaded',()=>{askWake=()=>{}})"); pg.goto((root / 'tracker/index.html').as_uri()); pg.wait_for_timeout(500)
        pg.screenshot(path=str(out / f'{scheme}-today.png'), full_page=True)
        assert pg.locator('.ex .thumb').count() >= 4, 'session thumbs'
        pg.click('.wolink >> nth=0'); pg.wait_for_timeout(300)
        assert pg.locator('.collage img').count() >= 3 and pg.locator('.excard .thumb').count() >= 4
        pg.screenshot(path=str(out / f'{scheme}-wo.png'), full_page=True)
        pg.click('.excard >> nth=0'); pg.wait_for_timeout(1500)
        assert pg.locator('.flip img').count() == 2
        pg.screenshot(path=str(out / f'{scheme}-ex.png'))
        pg.click('nav.tabs >> text=آمار'); pg.wait_for_timeout(300)
        assert pg.locator('.badge').count() == 12
        pg.locator('#bdg').scroll_into_view_if_needed(); pg.screenshot(path=str(out / f'{scheme}-badges.png'))
        # complete the session sets -> burst
        pg.click('nav.tabs >> text=امروز'); pg.wait_for_timeout(300)
        dots = pg.locator('.dot')
        n = dots.count()
        for k in range(n):
            d = pg.locator('.dot:not(.on)').first
            if d.count() == 0: break
            d.click(); pg.wait_for_timeout(30)
        pg.wait_for_timeout(250)
        print(scheme, 'dots', n, 'burst', pg.locator('.burst i').count(), 'done', pg.locator('[data-k=workout][aria-pressed=true]').count())
        pg.screenshot(path=str(out / f'{scheme}-burst.png'))
        pg.close()
    b.close()
print('errors', errs)
