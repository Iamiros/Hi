# Every food-tab control: manual sheet (pick, unit, back, recent, new/cancel, custom delete, delete item), planner (meal chips, add, Claude), photo remove.
from playwright.sync_api import sync_playwright
import glob, pathlib
CH = glob.glob('/opt/pw-browsers/chromium-1194/chrome-linux*/chrome')[0]
root = pathlib.Path(__file__).resolve().parent.parent
errs, fails = [], []
def chk(c, msg): print(('OK  ' if c else 'FAIL'), msg); c or fails.append(msg)
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=CH)
    for lang in ['fa', 'en']:
        pg = b.new_page(viewport={'width': 390, 'height': 844})
        pg.on('pageerror', lambda e: errs.append(str(e)))
        pg.add_init_script("addEventListener('DOMContentLoaded',()=>{askWake=()=>{}})")
        pg.goto((root / 'tracker/index.html').as_uri()); pg.wait_for_timeout(300)
        if lang == 'en': pg.evaluate('window.name="grip-lang=en"'); pg.reload(); pg.wait_for_timeout(300)
        pg.evaluate('''()=>{const y=D(dateOf(sel-1)); y.food=[{m:0,n:"تست",a:"۱ عدد",k:100,p:10,c:5,f:2}]; save();
          const f=async()=>({text:""}); f.json=async(pr)=>[{title:"AI",items:[{n:"مرغ",a:"۲۰۰ گرم",k:330,p:62,c:0,f:7}]}]; f.limits=async()=>({images:{maxCount:4}}); smp=f; smpImg=true; tab="food"; render()}''')
        pg.wait_for_timeout(300)
        day = lambda: pg.evaluate('S.days[dateOf(sel)]||{}')
        # manual sheet into meal 3 (post-workout)
        pg.click('[data-act=fadd][data-m="2"]'); pg.wait_for_timeout(200)
        pg.click('[data-act=fpick][data-id=eggw]'); pg.wait_for_timeout(100)
        u = pg.locator('[data-act=funit]')
        if u.count(): u.first.click(); pg.wait_for_timeout(80); chk(pg.input_value('#famt') == '100', lang + ' unit grams resets amount')
        pg.click('[data-act=fback]'); pg.wait_for_timeout(80); chk(pg.locator('[data-act=fpick]').count() > 5, lang + ' back to list')
        pg.click('[data-act=fpick][data-id=chk]'); pg.fill('#famt', '150'); pg.click('[data-act=fsave]'); pg.wait_for_timeout(200)
        chk([x['m'] for x in day().get('food', [])] == [2], lang + ' manual add lands in chosen meal')
        # recent into meal 4
        pg.click('[data-act=fadd][data-m="3"]'); pg.wait_for_timeout(200)
        pg.locator('[data-act=frec]').first.click(); pg.wait_for_timeout(200)
        chk(day()['food'][-1]['m'] == 3, lang + ' recent lands in chosen meal')
        # new food: cancel, then create and delete custom
        pg.click('[data-act=fnew]'); pg.wait_for_timeout(150); pg.click('[data-act=fnewcancel]'); pg.wait_for_timeout(80)
        chk(pg.locator('#fq').count() == 1, lang + ' new food cancel')
        pg.evaluate('$("#sheet").close()'); pg.click('[data-act=fnew]'); pg.fill('#nfn', 'بیسکویت'); pg.fill('#nfk', '250'); pg.fill('#nfp', '5'); pg.fill('#nfc', '30'); pg.fill('#nff', '12'); pg.click('[data-act=fnewsave]'); pg.wait_for_timeout(150)
        chk(len(pg.evaluate('S.foods||[]')) == 1, lang + ' custom food saved')
        pg.click('[data-act=fback]'); pg.wait_for_timeout(80)
        dc = pg.locator('[data-act=fdelc]')
        if dc.count(): dc.first.click(); pg.wait_for_timeout(80)
        chk(len(pg.evaluate('S.foods||[]')) == 0, lang + ' custom food deleted')
        pg.evaluate('$("#sheet").close()')
        # delete item, totals sync
        n0 = len(day()['food']); pg.locator('[data-act=fdel]').first.click(); pg.wait_for_timeout(150)
        chk(len(day()['food']) == n0 - 1 and day().get('kin') == round(sum(x['k'] for x in day()['food'])) or abs(day().get('kin', 0) - sum(x['k'] for x in day()['food'])) < 1, lang + ' delete + kcal sync')
        # planner: chip, add, Claude
        pg.click('[data-act=mpm][data-m="1"]'); pg.wait_for_timeout(150)
        chk(pg.evaluate('mpM') == 1, lang + ' planner chip')
        k0 = len(day()['food']); pg.locator('[data-act=mpadd]').first.click(); pg.wait_for_timeout(200)
        chk(len(day()['food']) > k0 and all(x['m'] == 1 for x in day()['food'][k0:]), lang + ' planner add lands in chosen meal')
        pg.click('[data-act=mpai]'); pg.wait_for_timeout(300)
        k0 = len(day()['food']); a = pg.locator('[data-act=mpadd][data-src=ai]')
        chk(a.count() >= 1, lang + ' Claude planner card'); a.count() and a.first.click(); pg.wait_for_timeout(200)
        chk(len(day()['food']) == k0 + 1 and day()['food'][-1]['m'] == 1, lang + ' Claude planner add')
        # photo remove keeps typed text
        pg.fill('#aiq', 'سلام'); img = str(root / 'tracker/icon-192.png')
        if not pathlib.Path(img).exists(): img = str(next((root / 'tracker').glob('*.png')))
        pg.set_input_files('#aiimg', [img, img]); pg.wait_for_timeout(400)
        pg.locator('[data-act=aiimgdel]').first.click(); pg.wait_for_timeout(200)
        chk(pg.locator('[data-act=aiimgdel]').count() == 1 and pg.input_value('#aiq') == 'سلام', lang + ' photo remove keeps text')
        chk(pg.evaluate('document.documentElement.scrollWidth') <= 390, lang + ' no overflow')
        pg.close()
    b.close()
print('fails', fails); print('errors', errs)
