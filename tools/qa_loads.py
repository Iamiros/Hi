from playwright.sync_api import sync_playwright
import glob, pathlib
CH = glob.glob('/opt/pw-browsers/chromium-1194/chrome-linux*/chrome')[0]
root = pathlib.Path(__file__).resolve().parent.parent
out = '/tmp/claude-0/-home-user-Hi/54b47da7-daf8-5c46-b909-aca8dd4b7c8f/scratchpad/'
errs = []
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=CH); pg = b.new_page(viewport={'width': 390, 'height': 844})
    pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto((root / 'tracker/index.html').as_uri()); pg.wait_for_timeout(300)
    table = pg.evaluate('''()=>{const o=[];for(const L of "ABCDE"){const W=PROGRAM.workouts[L];for(const ex of W.ex){const r=[L+" "+ex.gym];for(let w=1;w<=8;w++){const d=doseOf(ex,w,false),x=loadFor(ex.gym,d,0,w===4);r.push(d+" → "+(x?loadTxt(x).replace(/<[^>]+>/g,""):"-"))}o.push(r.join(" | "))}}return o}''')
    print('\n'.join(table))
    # taps
    pg.click('.kpis3 > div >> nth=0'); pg.wait_for_timeout(500)
    assert pg.locator('#s-food').count() == 1, 'kcal -> food'
    pg.click('nav.tabs button >> nth=0'); pg.wait_for_timeout(300)
    pg.click('.kpis3 > div >> nth=1'); pg.wait_for_timeout(900)
    y = pg.evaluate('document.getElementById("s-water").getBoundingClientRect().top'); assert 0 <= y < 120, y
    pg.evaluate('scrollTo(0,0)'); pg.click('.strip'); pg.wait_for_timeout(600); assert pg.locator('#s-map').count()
    pg.click('nav.tabs button >> nth=0'); pg.wait_for_timeout(300)
    # log a non-main exercise (lateral raise a4)
    pg.locator('[data-act=log]').nth(3).click(); pg.wait_for_timeout(300)
    print('prefill 4th', pg.input_value('#kg0'), pg.input_value('#rp0'))
    pg.click('[data-act=shsave]'); pg.wait_for_timeout(300)
    pg.locator('[data-act=log]').nth(1).click(); pg.wait_for_timeout(300); print('prefill 2nd', pg.input_value('#kg0'), pg.input_value('#rp0')); pg.click('[data-act=shsave]'); pg.wait_for_timeout(300)
    pg.click('nav.tabs button >> nth=3'); pg.wait_for_timeout(300)
    pg.locator('#s-prog').scroll_into_view_if_needed(); pg.screenshot(path=out + 'prog.png')
    print('prog rows', pg.locator('#s-prog tbody tr').count())
    pg.click('.kpi >> nth=2'); pg.wait_for_timeout(600)
    pg.click('nav.tabs button >> nth=2'); pg.click('.pd >> nth=1'); pg.wait_for_timeout(600)
    print('plan->day', pg.evaluate('sel'), pg.evaluate('tab'))
    pg.click('nav.tabs button >> nth=0'); pg.wait_for_timeout(300); pg.locator('#s-session').scroll_into_view_if_needed(); pg.screenshot(path=out + 'sess.png')
    b.close()
print('errors', errs)
