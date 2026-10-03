from playwright.sync_api import sync_playwright
import glob, pathlib
CH = glob.glob('/opt/pw-browsers/chromium-1194/chrome-linux*/chrome')[0]
root = pathlib.Path(__file__).resolve().parent.parent
errs = []
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=CH); pg = b.new_page(viewport={'width': 390, 'height': 844})
    pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto((root / 'tracker/index.html').as_uri()); pg.wait_for_timeout(300)
    assert pg.evaluate('document.documentElement.dir') == 'rtl'
    pg.click('[data-act=water][data-v="500"]') if pg.locator('[data-act=water][data-v="500"]').count() else None
    with pg.expect_navigation(): pg.click('#lang')
    pg.wait_for_timeout(300)
    assert pg.evaluate('document.documentElement.dir') == 'ltr' and 'Today' in pg.inner_text('nav.tabs')
    pg.click('nav.tabs >> text=Settings'); pg.wait_for_timeout(200)
    with pg.expect_navigation(): pg.click('[data-act=setlang][data-v=fa]')
    pg.wait_for_timeout(300)
    assert pg.evaluate('document.documentElement.dir') == 'rtl' and 'امروز' in pg.inner_text('nav.tabs')
    # fresh tab (no window.name) keeps saved pref
    pg.evaluate('window.name=""'); pg.click('#lang') ; pg.wait_for_timeout(800)
    pg.evaluate('window.name=""'); pg.reload(); pg.wait_for_timeout(300)
    assert pg.evaluate('document.documentElement.dir') == 'ltr', 'pref from storage'
    b.close()
print('errors', errs)
