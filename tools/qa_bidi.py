from playwright.sync_api import sync_playwright
import glob, pathlib, json, re
CH = glob.glob('/opt/pw-browsers/chromium-1194/chrome-linux*/chrome')[0]
root = pathlib.Path(__file__).resolve().parent.parent
JS = r'''() => {
 const out = [], fa = /[؀-ۿ]/, la = /[A-Za-z0-9]/;
 const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
 let n; while ((n = w.nextNode())) {
  const t = n.nodeValue; if (!la.test(t)) continue;
  const el = n.parentElement; if (!el || el.closest('script,style,svg,[hidden]')) continue;
  if (el.closest('bdi,[dir=ltr],[lang=en]')) continue;
  if (getComputedStyle(el).direction !== 'rtl') continue;
  // risky: Latin run plus neutral/weak chars, or Latin text adjacent to Persian in same block
  const block = el.closest('p,li,td,th,button,span,b,label,div,h1,h2,h3,summary,option'); 
  const txt = (block||el).textContent.trim().slice(0,140);
  if (fa.test(txt) || /^[A-Za-z0-9]/.test(t.trim())) out.push(txt);
 }
 return [...new Set(out)];
}'''
res = set()
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=CH)
    pg = b.new_page(viewport={'width': 390, 'height': 844})
    pg.goto((root / 'tracker/index.html').as_uri()); pg.wait_for_timeout(400)
    def grab(tag):
        for t in pg.evaluate(JS): res.add(t)
    grab('today')
    for i in range(7):
        pg.click('[data-act=next]'); pg.wait_for_timeout(120); grab('day%d' % i)
    for tab in ['غذا', 'برنامه', 'آمار', 'تنظیمات']:
        pg.click(f'nav.tabs >> text={tab}'); pg.wait_for_timeout(200); grab(tab)
    pg.click('nav.tabs >> text=امروز'); pg.click('[data-act=today]') if pg.locator('[data-act=today]').count() else None
    pg.wait_for_timeout(200)
    pg.click('.wolink >> nth=0'); pg.wait_for_timeout(200); grab('wo')
    for k in range(5):
        if not pg.locator('.excard').count(): pg.click('.wolink >> nth=0'); pg.wait_for_timeout(150)
        pg.click(f'.excard >> nth={k}'); pg.wait_for_timeout(150); grab('ex'); pg.click('[data-act=pback]'); pg.wait_for_timeout(150)
    while pg.locator('[data-act=pback]').count(): pg.click('[data-act=pback]'); pg.wait_for_timeout(150)
    infos = pg.locator('[data-act=info]').count()
    for k in range(infos):
        pg.locator('[data-act=info]').nth(k).click(); pg.wait_for_timeout(100); grab('info')
        pg.keyboard.press('Escape'); pg.wait_for_timeout(80)
    if pg.locator('[data-act=log]').count():
        pg.locator('[data-act=log]').first.click(); pg.wait_for_timeout(150); grab('log'); pg.keyboard.press('Escape')
    pg.click('nav.tabs >> text=غذا'); pg.wait_for_timeout(150)
    if pg.locator('[data-act=fadd]').count():
        pg.locator('[data-act=fadd]').first.click(); pg.wait_for_timeout(150); grab('fsheet'); pg.keyboard.press('Escape')
    b.close()
for t in sorted(res): print('-', t)
print(len(res))
