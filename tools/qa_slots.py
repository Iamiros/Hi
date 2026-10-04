# Food slot placement benchmark: named meal > workout time > order with filled meals > nearest planned time; plus UI flow.
from playwright.sync_api import sync_playwright
import glob, pathlib, json
CH = glob.glob('/opt/pw-browsers/chromium-1194/chrome-linux*/chrome')[0]
root = pathlib.Path(__file__).resolve().parent.parent
errs, fails = [], []
F = lambda m, t=None: {"m": m, "n": "x", "a": "", "k": 100, "p": 10, "c": 0, "f": 0}
CASES = [  # (name, day fields, items [(t, s)], nowT, expected slots)
    ("bug: named post-workout at 12:00", {}, [("12:00", 2)], None, [2]),
    ("named post-workout 12:00, wake 07:00", {"wake": "07:00"}, [("12:00", 2)], None, [2]),
    ("named post-workout, meal 1 filled 08:00", {"food": [F(0)], "mt": {"0": "08:00"}}, [("12:00", 2)], None, [2]),
    ("unnamed 12:00 after workout 10:30", {"wt": "10:30"}, [("12:00", None)], None, [2]),
    ("unnamed 12:00 after workout, meal 1 at 08:00", {"wt": "10:30", "food": [F(0)], "mt": {"0": "08:00"}}, [("12:00", None)], None, [2]),
    ("unnamed 09:00 before workout 17:00", {"wt": "17:00"}, [("09:00", None)], None, [0]),
    ("unnamed 14:00 before workout 17:00, meal 1 filled", {"wt": "17:00", "food": [F(0)], "mt": {"0": "09:00"}}, [("14:00", None)], None, [1]),
    ("unnamed 19:00 after workout 17:00, post filled 17:30", {"wt": "17:00", "food": [F(2)], "mt": {"2": "17:30"}}, [("21:00", None)], None, [3]),
    ("batch 08/13/20 no workout", {}, [("08:00", None), ("13:00", None), ("20:00", None)], None, [0, 1, 3]),
    ("batch 08/13/16/20 workout 15:00", {"wt": "15:00"}, [("08:00", None), ("13:00", None), ("16:00", None), ("20:00", None)], None, [0, 1, 2, 3]),
    ("same time = same meal", {}, [("13:00", None), ("13:00", None)], None, [0, 0]),
    ("within 45 min of filled meal", {"food": [F(1)], "mt": {"1": "14:00"}}, [("14:30", None)], None, [1]),
    ("first food of day at 14:00 = meal 1", {}, [("14:00", None)], None, [0]),
    ("snack named", {"food": [F(0)]}, [("16:00", 4)], None, [4]),
    ("named slot wins over time", {"wt": "18:00"}, [("09:00", 3)], None, [3]),
    ("untimed today uses now", {"wt": "10:00"}, [(None, None), (None, None)], "12:00", [2, 2]),
    ("untimed past day = first free", {"food": [F(0), F(1)]}, [(None, None)], None, [2]),
    ("all meals full, late = snack", {"food": [F(0), F(1), F(2), F(3)], "mt": {"0": "08:00", "1": "12:00", "2": "15:00", "3": "18:00"}}, [("23:00", None)], None, [4]),
    ("all meals full, near meal 4", {"food": [F(0), F(1), F(2), F(3)], "mt": {"0": "08:00", "1": "12:00", "2": "15:00", "3": "18:00"}}, [("19:30", None)], None, [3]),
    ("named + timed mix", {}, [("12:00", 2), ("09:00", None), ("20:00", None)], None, [2, 0, 3]),
]
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=CH)
    pg = b.new_page(viewport={'width': 390, 'height': 844})
    pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.add_init_script("addEventListener('DOMContentLoaded',()=>{askWake=()=>{}})")
    pg.goto((root / 'tracker/index.html').as_uri()); pg.wait_for_timeout(400)
    for name, day, its, now, exp in CASES:
        got = pg.evaluate('([d, its, now]) => placeItems(its.map(([t, s]) => ({m: null, t, s, n: "x"})), Object.assign({done: {}}, d), now).map(x => x.m)', [day, its, now])
        ok = got == exp; print(('OK  ' if ok else 'FAIL'), name, got, '' if ok else f'expected {exp}')
        ok or fails.append(name)
    # UI flow with mocked Claude
    for lang in ['fa', 'en']:
        if lang == 'en': pg.evaluate('window.name="grip-lang=en"'); pg.reload(); pg.wait_for_timeout(400)
        pg.evaluate('''()=>{localStorage.clear(); S.days={}; const f=async()=>({text:""}); f.json=async(pr)=>{window.__pr=pr; return [{t:"12:00",s:2,n:"مرغ",a:"۲۰۰ گرم",k:330,p:62,c:0,f:7},{t:"12:00",s:2,n:"برنج",a:"۱۵۰ گرم",k:195,p:4,c:42,f:0.4},{t:"21:00",s:null,n:"ماست",a:"۲۰۰ گرم",k:120,p:20,c:8,f:0}]}; f.limits=async()=>({images:{maxCount:4}}); smp=f; smpImg=true; tab="food"; render()}''')
        pg.wait_for_timeout(300)
        pg.fill('#aiq', 'بعد تمرین ساعت ۱۲ مرغ و برنج، شب ماست'); pg.click('[data-act=aiparse]'); pg.wait_for_timeout(400)
        assert '"s"' in pg.evaluate('window.__pr'), 'prompt lacks s'
        sl = pg.evaluate('[...document.querySelectorAll(".aislot")].map(e=>+e.value)'); print(lang, 'preview slots', sl)
        sl == [2, 2, 3] or fails.append(lang + ' preview')
        pg.evaluate('tab="food";render()'); pg.wait_for_timeout(200)
        assert pg.locator('.aislot').count() == 3, 'preview lost on render'
        assert pg.input_value('#aiq').startswith('بعد'), 'text lost on render'
        pg.select_option('.aislot >> nth=2', '4'); pg.click('[data-act=aiadd]'); pg.wait_for_timeout(300)
        d = pg.evaluate('S.days[dateOf(sel)]')
        got = [x['m'] for x in d['food']]; print(lang, 'saved', got, d.get('mt'))
        (got == [2, 2, 4] and d['mt'].get('2') == '12:00' and d['mt'].get('4') == '21:00') or fails.append(lang + ' save')
        assert pg.input_value('#aiq') == '' and pg.locator('.aislot').count() == 0
        # day switch hides stale preview
        pg.fill('#aiq', 'x'); pg.click('[data-act=aiparse]'); pg.wait_for_timeout(300)
        pg.evaluate('sel=sel+1;render()'); pg.wait_for_timeout(200)
        pg.locator('.aislot').count() == 0 or fails.append(lang + ' stale preview')
        pg.evaluate('sel=sel-1;aiParsed=null;render()')
        # workout done sets wt; planner default goes to post-workout
        pg.evaluate('(()=>{const d=D(dateOf(sel)); d.food=[]; delete d.wt; mpM=null; tab="today"; render()})()'); pg.wait_for_timeout(200)
        pg.evaluate('(()=>{const b=document.querySelector("[data-act=tog][data-k=workout]"); b && b.click()})()'); pg.wait_for_timeout(200)
        wt = pg.evaluate('S.days[dateOf(sel)].wt'); print(lang, 'wt', wt); wt or fails.append(lang + ' wt')
        pg.evaluate('tab="food";render()'); pg.wait_for_timeout(200)
        mp = pg.evaluate('mpM'); print(lang, 'planner default', mp); mp == 2 or fails.append(lang + ' planner default')
        pg.evaluate('tab="today";render()'); pg.evaluate('document.querySelector("[data-act=tog][data-k=workout]").click()'); pg.wait_for_timeout(200)
        pg.evaluate('S.days[dateOf(sel)].wt') is None or fails.append(lang + ' wt clear')
        pg.evaluate('tab="food";render()'); pg.wait_for_timeout(200)
        ow = pg.evaluate('document.documentElement.scrollWidth'); ow <= 390 or fails.append(lang + f' overflow {ow}')
    b.close()
print('fails', fails); print('errors', errs)
