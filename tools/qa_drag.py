# Move logged food between meals: drag the grip (mouse and touch pointer), tap grip for the meal list.
from playwright.sync_api import sync_playwright
import glob, pathlib
CH = glob.glob('/opt/pw-browsers/chromium-1194/chrome-linux*/chrome')[0]
root = pathlib.Path(__file__).resolve().parent.parent
out = '/tmp/claude-0/-home-user-Hi/54b47da7-daf8-5c46-b909-aca8dd4b7c8f/scratchpad/'
errs, fails = [], []
def chk(c, msg): print(('OK  ' if c else 'FAIL'), msg); c or fails.append(msg)
def drag(pg, src, dst_sel, shot=None):
    g = pg.locator(src).bounding_box(); pg.mouse.move(g['x'] + g['width'] / 2, g['y'] + g['height'] / 2); pg.mouse.down()
    pg.mouse.move(g['x'] + 20, g['y'] + 20, steps=4)
    for _ in range(60):  # move toward target, auto-scroll as needed
        t = pg.locator(dst_sel).bounding_box(); ty = min(max(t['y'] + 60, 100), 700)
        pg.mouse.move(t['x'] + t['width'] / 2, ty, steps=3); pg.wait_for_timeout(30)
        if pg.evaluate(f'!!document.querySelector("{dst_sel}.dropon")'): break
        if t['y'] > 700: pg.mouse.move(200, 800, steps=2); pg.wait_for_timeout(200)
        elif t['y'] + t['height'] < 100: pg.mouse.move(200, 40, steps=2); pg.wait_for_timeout(200)
    if shot: pg.screenshot(path=out + shot)
    pg.mouse.up(); pg.wait_for_timeout(300)
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=CH)
    for lang in ['fa', 'en']:
        pg = b.new_page(viewport={'width': 390, 'height': 844})
        pg.on('pageerror', lambda e: errs.append(str(e)))
        pg.add_init_script("addEventListener('DOMContentLoaded',()=>{askWake=()=>{}})")
        pg.goto((root / 'tracker/index.html').as_uri()); pg.wait_for_timeout(300)
        if lang == 'en': pg.evaluate('window.name="grip-lang=en"'); pg.reload(); pg.wait_for_timeout(300)
        pg.evaluate('''(()=>{const d=D(dateOf(sel)); d.food=["کیک","استیک","پاستا","روغن"].map(n=>({m:0,n,a:"۱",k:100,p:10,c:5,f:2})); syncFood(d); save(); tab="food"; render()})()''')
        pg.wait_for_timeout(300); pg.locator('#s-meal0').scroll_into_view_if_needed()
        ms = lambda: pg.evaluate('S.days[dateOf(sel)].food.map(x=>x.m)')
        drag(pg, '[data-fi="1"] .fgrip', '#s-meal2', f'drag_{lang}.png')
        chk(ms() == [0, 2, 0, 0], f'{lang} mouse drag to meal 3: {ms()}')
        chk(pg.evaluate('S.days[dateOf(sel)].kin') == 400, f'{lang} totals kept')
        drag(pg, '[data-fi="2"] .fgrip', '#s-meal1')
        chk(ms() == [0, 2, 1, 0], f'{lang} second drag to meal 2: {ms()}')
        # drop on same meal or outside = no change
        g = pg.locator('[data-fi="0"] .fgrip').bounding_box(); pg.mouse.move(g['x'] + 10, g['y'] + 10); pg.mouse.down(); pg.mouse.move(g['x'] + 40, g['y'] + 30, steps=5); pg.mouse.up(); pg.wait_for_timeout(200)
        chk(ms() == [0, 2, 1, 0], f'{lang} drop in same meal keeps')
        chk(not pg.evaluate('$("#dlg").open'), f'{lang} drag does not open menu')
        # tap grip opens list
        pg.wait_for_timeout(500); pg.locator('[data-fi="3"] .fgrip').click(); pg.wait_for_timeout(200)
        chk(pg.evaluate('$("#dlg").open'), f'{lang} tap opens meal list'); pg.screenshot(path=out + f'mvmenu_{lang}.png')
        pg.click('#dlg [data-mv="4"]'); pg.wait_for_timeout(300)
        chk(ms() == [0, 2, 1, 4], f'{lang} menu move to snack: {ms()}')
        chk(pg.locator('.dragghost').count() == 0 and not pg.evaluate('document.body.classList.contains("dragging")'), f'{lang} cleanup')
        pg.close()
    # touch pointer (mobile emulation)
    ctx = b.new_context(viewport={'width': 390, 'height': 844}, has_touch=True, is_mobile=True)
    pg = ctx.new_page(); pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.add_init_script("addEventListener('DOMContentLoaded',()=>{askWake=()=>{}})")
    pg.goto((root / 'tracker/index.html').as_uri()); pg.wait_for_timeout(300)
    pg.evaluate('''(()=>{const d=D(dateOf(sel)); d.food=[{m:0,n:"a",a:"1",k:1,p:1,c:1,f:1},{m:0,n:"b",a:"1",k:1,p:1,c:1,f:1}]; save(); tab="food"; render()})()''')
    pg.locator('#s-meal0').scroll_into_view_if_needed(); pg.wait_for_timeout(200)
    g = pg.locator('[data-fi="1"] .fgrip').bounding_box(); t = pg.locator('#s-meal1').bounding_box()
    cdp = ctx.new_cdp_session(pg); sx, sy = g['x'] + 14, g['y'] + 22
    cdp.send('Input.dispatchTouchEvent', {'type': 'touchStart', 'touchPoints': [{'x': sx, 'y': sy}]})
    for k in range(1, 11): cdp.send('Input.dispatchTouchEvent', {'type': 'touchMove', 'touchPoints': [{'x': sx + 10, 'y': sy + (t['y'] + 60 - sy) * k / 10}]}); pg.wait_for_timeout(20)
    cdp.send('Input.dispatchTouchEvent', {'type': 'touchEnd', 'touchPoints': []}); pg.wait_for_timeout(300)
    chk(pg.evaluate('S.days[dateOf(sel)].food.map(x=>x.m)') == [0, 1], 'touch drag')
    b.close()
print('fails', fails); print('errors', errs)
