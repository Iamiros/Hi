from playwright.sync_api import sync_playwright
import glob, pathlib
CH = glob.glob('/opt/pw-browsers/chromium-1194/chrome-linux*/chrome')[0]
root = pathlib.Path(__file__).resolve().parent.parent
out = '/tmp/claude-0/-home-user-Hi/54b47da7-daf8-5c46-b909-aca8dd4b7c8f/scratchpad/'
errs = []
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=CH); pg = b.new_page(viewport={'width': 390, 'height': 844})
    pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.add_init_script("addEventListener('DOMContentLoaded',()=>{askWake=()=>{}})"); pg.goto((root / 'tracker/index.html').as_uri()); pg.wait_for_timeout(400)
    assert pg.locator('#s-whoop').count() == 1
    for f, v in [('rec', '52'), ('hrv', '61'), ('rhr', '58'), ('sp', '84'), ('sh', '6.9'), ('strain', '12.4'), ('kcal', '2650'), ('rec', '250')]:
        pg.fill(f'#wh-{f}', v); pg.press(f'#wh-{f}', 'Tab'); pg.wait_for_timeout(120)
    d = pg.evaluate('S.days[dateOf(sel)]')
    print('wh', d.get('wh'), 'sleepH', d.get('sleepH'), 'readiness', pg.evaluate('readiness(S.days[dateOf(sel)])'))
    assert d['wh']['rec'] == 52 and d['sleepH'] == 6.9
    pg.locator('#s-whoop').scroll_into_view_if_needed(); pg.wait_for_timeout(200); pg.screenshot(path=out + 'whoop.png')
    csvh = pg.evaluate('csv().split("\\r\\n")[0]'); assert 'whoop_rec' in csvh
    ctx = pg.evaluate('coachContext("day")'); assert '"whoop"' in ctx
    pg.locator('nav.tabs button').nth(3).click(); pg.wait_for_timeout(500); assert pg.locator('#s-whoopst').count() == 1
    b.close()
print('errors', errs)
