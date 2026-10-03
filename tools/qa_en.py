from playwright.sync_api import sync_playwright
import glob, pathlib, re
CH = glob.glob('/opt/pw-browsers/chromium-1194/chrome-linux*/chrome')[0]
root = pathlib.Path(__file__).resolve().parent.parent
out = pathlib.Path('/tmp/claude-0/-home-user-Hi/54b47da7-daf8-5c46-b909-aca8dd4b7c8f/scratchpad/en'); out.mkdir(exist_ok=True)
FA = re.compile(r'[ء-يپچژکگی۰-۹]')
errs, left, shots = [], set(), []
def scan(pg):
    for t in pg.evaluate('''()=>{const o=[];const w=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);let n;while(n=w.nextNode()){if(n.parentElement.closest('script,style,noscript,[hidden],[lang=fa]'))continue;o.push(n.nodeValue)}
      document.querySelectorAll('[aria-label],[placeholder],[title]').forEach(e=>['aria-label','placeholder','title'].forEach(a=>e.getAttribute(a)&&o.push(e.getAttribute(a))));return o}'''):
        if FA.search(t): left.add(t.strip()[:120])
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=CH)
    pg = b.new_page(viewport={'width': 390, 'height': 844})
    pg.add_init_script('window.name="grip-lang=en"')
    pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto((root / 'tracker/index.html').as_uri()); pg.wait_for_timeout(400)
    assert pg.evaluate('document.documentElement.dir') == 'ltr'
    def shot(n, full=True): pg.wait_for_timeout(200); scan(pg); pg.screenshot(path=str(out / f'{n}.png'), full_page=full); shots.append(n)
    shot('today')
    for i in range(1, 7):
        pg.click('[data-act=next]'); pg.wait_for_timeout(100); scan(pg)
        if i in (1, 2): shot(f'day{i}')
    pg.click('[data-act=today]') if pg.locator('[data-act=today]').count() else None
    for t in ['Food', 'Plan', 'Stats', 'Settings']:
        pg.click(f'nav.tabs >> text={t}'); shot(t.lower())
    pg.click('nav.tabs >> text=Today'); pg.wait_for_timeout(200)
    pg.click('.wolink >> nth=0'); shot('wo')
    pg.click('.excard >> nth=0'); shot('ex')
    pg.click('[data-act=pback]'); pg.wait_for_timeout(100)
    while pg.locator('[data-act=pback]').count(): pg.click('[data-act=pback]'); pg.wait_for_timeout(100)
    n = pg.locator('[data-act=info]').count()
    for k in range(n):
        pg.locator('[data-act=info]').nth(k).click(); pg.wait_for_timeout(80); scan(pg); pg.keyboard.press('Escape'); pg.wait_for_timeout(60)
    pg.locator('[data-act=log]').first.click(); shot('log', False); pg.keyboard.press('Escape')
    pg.click('#phase'); shot('weeks', False); pg.keyboard.press('Escape')
    pg.click('nav.tabs >> text=Food'); pg.locator('[data-act=fadd]').first.click(); shot('fsheet', False)
    pg.locator('[data-act=fpick]').first.click(); shot('fsheet2', False); pg.keyboard.press('Escape')
    pg.click('nav.tabs >> text=Stats'); pg.wait_for_timeout(100)
    for k in range(pg.locator('[data-act=info]').count()):
        pg.locator('[data-act=info]').nth(k).click(); pg.wait_for_timeout(80); scan(pg); pg.keyboard.press('Escape'); pg.wait_for_timeout(60)
    b.close()
print('errors', errs)
print('persian left:', len(left))
for t in sorted(left): print(' -', t)
