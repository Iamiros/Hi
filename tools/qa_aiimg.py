from playwright.sync_api import sync_playwright
import glob, pathlib
CH = glob.glob('/opt/pw-browsers/chromium-1194/chrome-linux*/chrome')[0]
root = pathlib.Path(__file__).resolve().parent.parent
img = str(root / 'tracker/icon-192.png')
errs = []
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=CH); pg = b.new_page(viewport={'width': 390, 'height': 844})
    pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto((root / 'tracker/index.html').as_uri()); pg.wait_for_timeout(300)
    # mock sample capability with image support
    pg.evaluate('''()=>{const f=async()=>({text:""}); f.json=async(prompt,opts)=>{window.__opts=opts;window.__prompt=prompt;return [{t:null,n:"پاستا",a:"۸۰ گرم خشک",k:285,p:10,c:58,f:1.2}]}; f.limits=async()=>({images:{maxCount:4}}); smp=f; smpImg=true; tab="food"; render()}''')
    pg.wait_for_timeout(300)
    pg.set_input_files('#aiimg', [img, img]); pg.wait_for_timeout(500)
    print('thumbs', pg.locator('.aithumb').count())
    pg.fill('#aiq', '۸۰ گرم از این پاستا خشک')
    pg.click('[data-act=aiparse]'); pg.wait_for_timeout(500)
    print('images sent', pg.evaluate('window.__opts && window.__opts.images && window.__opts.images.length'), 'label rule in prompt', 'nutrition facts label' in pg.evaluate('window.__prompt'))
    pg.click('[data-act=aiadd]'); pg.wait_for_timeout(400)
    print('food', pg.evaluate('JSON.stringify(S.days[dateOf(sel)].food.map(x=>x.n+" "+x.a))'), 'thumbs after', pg.locator('.aithumb').count())
    b.close()
print('errors', errs)
