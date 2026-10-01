import glob, pathlib, subprocess, time
from playwright.sync_api import sync_playwright
CH=glob.glob('/opt/pw-browsers/chromium-1194/chrome-linux*/chrome')[0]
root=pathlib.Path(__file__).resolve().parent.parent
out=pathlib.Path('/tmp/claude-0/-home-user-Hi/54b47da7-daf8-5c46-b909-aca8dd4b7c8f/scratchpad/s2'); out.mkdir(parents=True,exist_ok=True)
srv=subprocess.Popen(['python3','-m','http.server','8777','-d',str(root)],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL); time.sleep(1)
errs=[]
SEED="""()=>{const S={v:1,start:'2026-10-03',days:{},tests:{start:{pullups:5,ctb:1,pdip:7,hang:60,bw:89,waist:92,chinmax:6,hollow:30}},prefs:{mode:'gym',theme:'system'}};
 const base=new Date(2026,9,3,12);for(let i=0;i<12;i++){const d=new Date(base);d.setDate(d.getDate()+i);const k=d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0');
 S.days[k]={done:{walk:true,kcal:i%3!=0,protein:3,creatine:true,hang:i%2==0,sleep:true,workout:[0,1,3,5,6].includes(i%7)},water:3000+i*60,weight:+(89-i*0.13+(i%3)*0.2).toFixed(1),steps:12500,note:'',lifts:{a1:[{kg:0,reps:3+(i>6?1:0),ex:'pullup'}]},sets:{}}};
 localStorage.setItem('amir-cut-v1',JSON.stringify(S));}"""
try:
  with sync_playwright() as p:
    b=p.chromium.launch(executable_path=CH)
    for name,w,h,scheme in [('m375',375,812,'light'),('m390d',390,844,'dark'),('d1280',1280,900,'light')]:
        ctx=b.new_context(viewport={'width':w,'height':h},color_scheme=scheme,locale='fa-IR',timezone_id='Asia/Shanghai',device_scale_factor=2 if w<500 else 1)
        ctx.add_init_script("const _D=Date;const off=new _D('2026-10-15T10:00:00+08:00')-new _D();Date=class extends _D{constructor(...a){a.length?super(...a):super(_D.now()+off)}static now(){return _D.now()+off}};")
        pg=ctx.new_page()
        pg.on('pageerror',lambda e,n=name: errs.append((n,str(e))))
        pg.on('console',lambda m,n=name: errs.append((n,m.text)) if m.type=='error' else None)
        pg.goto('http://localhost:8777/tracker/index.html'); pg.wait_for_timeout(400)
        pg.evaluate(SEED); pg.reload(); pg.wait_for_timeout(700)
        pg.screenshot(path=str(out/f'{name}-today.png'),full_page=True)
        # tap two sets -> timer
        pg.click('.dot >> nth=0'); pg.wait_for_timeout(300)
        pg.screenshot(path=str(out/f'{name}-timer.png'))
        pg.click('[data-act=log] >> nth=0'); pg.wait_for_timeout(400)
        pg.screenshot(path=str(out/f'{name}-sheet.png'))
        pg.click('[data-act=shsave]'); pg.wait_for_timeout(200)
        pg.click('[data-act=tstop]') if pg.is_visible('[data-act=tstop]') else None
        pg.click('nav.tabs >> text=نقشه'); pg.wait_for_timeout(300); pg.screenshot(path=str(out/f'{name}-map.png'),full_page=True)
        pg.click('nav.tabs >> text=آمار'); pg.wait_for_timeout(300); pg.screenshot(path=str(out/f'{name}-stats.png'),full_page=True)
        pg.click('nav.tabs >> text=تنظیمات'); pg.wait_for_timeout(300); pg.screenshot(path=str(out/f'{name}-set.png'),full_page=True)
        print(name,'hscroll',pg.evaluate("document.documentElement.scrollWidth>document.documentElement.clientWidth"))
        ctx.close()
    b.close()
finally: srv.terminate()
print('errors',errs)
