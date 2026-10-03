from playwright.sync_api import sync_playwright
import glob, pathlib
CH = glob.glob('/opt/pw-browsers/chromium-1194/chrome-linux*/chrome')[0]
root = pathlib.Path(__file__).resolve().parent.parent
out = '/tmp/claude-0/-home-user-Hi/54b47da7-daf8-5c46-b909-aca8dd4b7c8f/scratchpad/'
errs = []
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=CH)
    for sc in ('dark', 'light'):
        pg = b.new_page(viewport={'width': 390, 'height': 844}, color_scheme=sc)
        pg.on('pageerror', lambda e: errs.append(str(e)))
        pg.goto((root / 'tracker/index.html').as_uri()); pg.wait_for_timeout(300)
        pg.click('#phase'); pg.wait_for_timeout(400)
        assert pg.locator('#wkmenu button').count() == 8 and pg.get_attribute('#phase', 'aria-expanded') == 'true'
        pg.screenshot(path=out + f'wk-{sc}.png')
        pg.click('#wkmenu [data-w="3"]'); pg.wait_for_timeout(200)
        assert pg.locator('#wkmenu').is_hidden()
        t = pg.inner_text('#phase'); assert 'هفته ۳' in t, t
        pg.click('#phase'); pg.keyboard.press('Escape'); assert pg.locator('#wkmenu').is_hidden()
        pg.click('#phase'); pg.click('#wkback', position={'x': 200, 'y': 800}); assert pg.locator('#wkmenu').is_hidden()
        pg.close()
    b.close()
print('errors', errs)
