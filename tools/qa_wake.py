from playwright.sync_api import sync_playwright
import glob, pathlib
CH = glob.glob('/opt/pw-browsers/chromium-1194/chrome-linux*/chrome')[0]
root = pathlib.Path(__file__).resolve().parent.parent
out = '/tmp/claude-0/-home-user-Hi/54b47da7-daf8-5c46-b909-aca8dd4b7c8f/scratchpad/'
errs = []
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=CH)
    for lang in ['fa', 'en']:
        pg = b.new_page(viewport={'width': 390, 'height': 844})
        pg.on('pageerror', lambda e: errs.append(str(e)))
        pg.goto((root / 'tracker/index.html').as_uri()); pg.wait_for_timeout(400)
        if lang == 'en':
            pg.evaluate('window.name="grip-lang=en"'); pg.reload(); pg.wait_for_timeout(400)
        assert pg.evaluate('sel===todayIdx()'), 'today not selected'
        assert pg.locator('#s-wake.need').count() == 1
        pg.screenshot(path=out + f'wake0_{lang}.png')
        pg.fill('#wh-rec', '60'); pg.wait_for_timeout(800)
        assert not pg.evaluate('$("#dlg").open'), 'asked while typing'
        pg.locator('#s-ready .scale5 button').first.click(); pg.wait_for_timeout(1000)
        assert pg.evaluate('$("#dlg").open'), 'askWake not shown'
        pg.screenshot(path=out + f'wakedlg_{lang}.png')
        pg.fill('#wkin', '07:00'); pg.click('#yes'); pg.wait_for_timeout(500)
        d = pg.evaluate('S.days[dateOf(sel)]')
        assert d['wake'] == '07:00' and d['wakeAsked']
        mt = pg.evaluate('[0,1,2,3,4].map(i=>mealT(S.days[dateOf(sel)],i))'); tw = pg.evaluate('trainWin(S.days[dateOf(sel)])')
        print(lang, mt, tw); assert mt[:4] == ['11:00', '14:00', '17:30', '19:00'] and tw == ['15:30', '17:00']
        pg.locator('#s-wake').scroll_into_view_if_needed(); pg.screenshot(path=out + f'wake1_{lang}.png')
        pg.locator('#s-ready .scale5 button').nth(2).click(); pg.wait_for_timeout(700)
        assert not pg.evaluate('$("#dlg").open'), 'asked twice'
        # manual edit wins over wake
        pg.locator('nav.tabs button').nth(1).click(); pg.wait_for_timeout(500)
        v = pg.locator('.mtime input').first.input_value(); print('food m1', v); assert v == '11:00'
        pg.evaluate('''()=>{const f=async()=>({text:""}); f.json=async()=>[]; f.limits=async()=>({images:{maxCount:4}}); smp=f; smpImg=true; render()}'''); pg.wait_for_timeout(300)
        pg.locator('.composer').scroll_into_view_if_needed(); pg.wait_for_timeout(200); pg.screenshot(path=out + f'composer_{lang}.png')
        bb = pg.evaluate('[...document.querySelectorAll(".cbar>*")].map(e=>{const r=e.getBoundingClientRect();return [e.className,Math.round(r.left),Math.round(r.right),Math.round(r.top)]})'); print(bb)
        assert all(0 <= x[1] and x[2] <= 390 for x in bb)
        # Esc on dialog counts as asked
        pg.evaluate('delete S.days[dateOf(sel)].wake; delete S.days[dateOf(sel)].wakeAsked; askWake()'); pg.keyboard.press('Escape'); pg.wait_for_timeout(200)
        assert pg.evaluate('S.days[dateOf(sel)].wakeAsked')
        pg.close()
    b.close()
print('errors', errs)
