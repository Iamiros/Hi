from playwright.sync_api import sync_playwright
import glob, pathlib
CH = glob.glob('/opt/pw-browsers/chromium-1194/chrome-linux*/chrome')[0]
root = pathlib.Path(__file__).resolve().parent.parent
out = '/tmp/claude-0/-home-user-Hi/54b47da7-daf8-5c46-b909-aca8dd4b7c8f/scratchpad/'
errs = []
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=CH); pg = b.new_page(viewport={'width': 390, 'height': 844})
    pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.add_init_script("addEventListener('DOMContentLoaded',()=>{askWake=()=>{}})"); pg.goto((root / 'tracker/index.html').as_uri()); pg.wait_for_timeout(300)
    # yesterday: last meal 18:00
    pg.evaluate('''()=>{const y=D(dateOf(sel-1));y.food=[{m:3,n:"x",a:"",k:500,p:40,c:40,f:10}];y.mt={3:"18:00"};save()}''')
    pg.locator('nav.tabs button').nth(1).click(); pg.wait_for_timeout(400)
    pg.fill('[data-act=mtime][data-m="0"]', '08:00'); pg.press('[data-act=mtime][data-m="0"]', 'Tab'); pg.wait_for_timeout(300)
    assert pg.evaluate('S.days[dateOf(sel)].mt[0]') == '08:00'
    # simulate AI result with times
    pg.evaluate('''()=>{const dd=peek(dateOf(sel))||{}; aiParsed=[{m:mealAt("08:10",dd),t:"08:10",n:"تخم‌مرغ",a:"۳ عدد",k:215,p:19,c:1,f:15},{m:mealAt("13:00",dd),t:"13:00",n:"مرغ",a:"۲۰۰ گرم",k:330,p:62,c:0,f:7}]; const bt=document.createElement('button');bt.dataset.act='aiadd';bt.id='tmpai';bt.textContent='x';document.body.appendChild(bt)}''')
    pg.click('#tmpai'); pg.wait_for_timeout(400)
    d = pg.evaluate('S.days[dateOf(sel)]')
    print('food', [(x['m'], x['n']) for x in d['food']], 'mt', d.get('mt'), 'kin', d.get('kin'))
    print('window', pg.evaluate('eatWindow(sel)'))
    pg.screenshot(path=out + 'meals.png')
    b.close()
print('errors', errs)
