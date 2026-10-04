from playwright.sync_api import sync_playwright
import glob, pathlib, json
CH = glob.glob('/opt/pw-browsers/chromium-1194/chrome-linux*/chrome')[0]
root = pathlib.Path(__file__).resolve().parent.parent
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=CH); pg = b.new_page(viewport={'width': 390, 'height': 844})
    cdp = pg.context.new_cdp_session(pg); cdp.send('Emulation.setCPUThrottlingRate', {'rate': 4})
    pg.goto((root / 'tracker/index.html').as_uri()); pg.wait_for_timeout(800)
    pg.evaluate('''window.__f=[];(function t(ts){window.__f.push(ts);requestAnimationFrame(t)})(performance.now())''')
    def act(label, fn):
        pg.evaluate('window.__f=[]'); t0 = pg.evaluate('performance.now()'); fn(); pg.wait_for_timeout(900)
        f = pg.evaluate('window.__f'); d = [b - a for a, b in zip(f, f[1:])]
        long = [round(x) for x in d if x > 34]
        print(f'{label:10s} frames {len(d):3d} worst {round(max(d)) if d else 0:4d}ms  >34ms: {len(long)} {long[:6]}')
    act('tab-food', lambda: pg.locator('nav.tabs button').nth(1).click())
    act('tab-stats', lambda: pg.locator('nav.tabs button').nth(3).click())
    act('tab-today', lambda: pg.locator('nav.tabs button').nth(0).click())
    act('day-prev', lambda: pg.click('[data-act=prev]'))
    act('push-wo', lambda: pg.click('.wolink >> nth=0')) if pg.locator('.wolink').count() else None
    act('push-ex', lambda: pg.click('.excard >> nth=0'))
    act('pop', lambda: pg.click('[data-act=pback]'))
    b.close()
