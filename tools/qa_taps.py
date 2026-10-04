from playwright.sync_api import sync_playwright
import glob, pathlib, sys
CH = glob.glob('/opt/pw-browsers/chromium-1194/chrome-linux*/chrome')[0]
root = pathlib.Path(__file__).resolve().parent.parent
out = '/tmp/claude-0/-home-user-Hi/54b47da7-daf8-5c46-b909-aca8dd4b7c8f/scratchpad/'
JS = '''()=>{const sel='.pill,.kpi,.badge,.chips > *,.notice,.thumb,.macro,.legend,.meter,.ring,.pd,.excard,.kpis3 > *,.ch > *,.rate,.prs h3,.dayno,.wd,.cell,.hm button,.gauge,.tank,.strip,.ratio,.wu li,.ex-tags > *';
 const o=[];document.querySelectorAll('#view '+sel.split(',').join(',#view ')).forEach(e=>{if(e.closest('[data-act],a,button,label,summary,input,select')||e.querySelector('[data-act]'))return;const r=e.getBoundingClientRect();if(!r.width)return;o.push(e.className+' :: '+e.textContent.trim().slice(0,40))});return [...new Set(o)]}'''
errs=[]; dead=set()
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=CH); pg = b.new_page(viewport={'width': 390, 'height': 844})
    pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto((root / 'tracker/index.html').as_uri()); pg.wait_for_timeout(300)
    def scan(): [dead.add(x) for x in pg.evaluate(JS)]
    scan()
    for _ in range(3): pg.click('[data-act=next]'); pg.wait_for_timeout(600); scan()
    for k in range(1,5): pg.locator('nav.tabs button').nth(k).click(); pg.wait_for_timeout(600); scan()
    pg.locator('nav.tabs button').nth(0).click(); pg.wait_for_timeout(600)
    pg.click('[data-act=today]') if pg.locator('[data-act=today]').count() else None; pg.wait_for_timeout(600)
    pg.click('.wolink >> nth=0'); pg.wait_for_timeout(700); scan()
    pg.click('.excard >> nth=0'); pg.wait_for_timeout(700); scan()
    b.close()
print('errors', errs); print('dead taps', len(dead))
for d in sorted(dead): print(' -', d)
