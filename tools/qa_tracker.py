import glob, json, sys, subprocess, time, pathlib
from playwright.sync_api import sync_playwright
CH=glob.glob('/opt/pw-browsers/chromium-1194/chrome-linux*/chrome')[0]
root=pathlib.Path(__file__).resolve().parent.parent
out=pathlib.Path('/tmp/claude-0/-home-user-Hi/54b47da7-daf8-5c46-b909-aca8dd4b7c8f/scratchpad/shots'); out.mkdir(parents=True,exist_ok=True)
srv=subprocess.Popen(['python3','-m','http.server','8765','-d',str(root)],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL); time.sleep(1)
errs=[]
try:
  with sync_playwright() as p:
    b=p.chromium.launch(executable_path=CH)
    for name,w,h,scheme in [('m375',375,800,'light'),('m430',430,900,'dark'),('d1280',1280,900,'light')]:
        ctx=b.new_context(viewport={'width':w,'height':h},color_scheme=scheme,locale='fa-IR',timezone_id='Asia/Shanghai')
        # fake clock: Oct 19 2026 (day 15, week 3 Monday)
        ctx.add_init_script("const _D=Date;const off=new _D('2026-10-14T10:00:00+08:00')-new _D();Date=class extends _D{constructor(...a){a.length?super(...a):super(_D.now()+off)}static now(){return _D.now()+off}};")
        pg=ctx.new_page()
        pg.on('console',lambda m: errs.append((name,m.text)) if m.type in('error','warning') else None)
        pg.on('pageerror',lambda e: (errs.append((name,str(e))),print('PAGEERR',e)))
        pg.goto('http://localhost:8765/tracker/index.html'); pg.wait_for_timeout(800)
        # seed data for first 12 days via UI state
        pg.evaluate("""()=>{const S=JSON.parse(localStorage.getItem('amir-cut-v1')||'null')||{v:1,start:'2026-10-03',days:{},tests:{},prefs:{mode:'gym',theme:'system'}};
          const base=new Date(2026,9,3,12);for(let i=0;i<12;i++){const d=new Date(base);d.setDate(d.getDate()+i);const k=d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0');
          S.days[k]={done:{walk:true,kcal:i%3!=0,protein:3,creatine:true,hang:i%2==0,sleep:true,workout:[0,1,3,4].includes(i%7)},water:3000+i*50,weight:+(89-i*0.12).toFixed(1),steps:12500,note:'تست',lifts:{a1:[{kg:10+i*0.5,reps:5},{kg:10,reps:5}]}}};
          S.tests={start:{pullups:9,ctb:3,pdip:12,hang:75,bw:89,waist:92}};localStorage.setItem('amir-cut-v1',JSON.stringify(S));}""")
        pg.reload(); pg.wait_for_timeout(600); print(name, pg.evaluate('document.getElementById("tabs").children.length'), pg.evaluate('Object.keys(localStorage)'))
        pg.screenshot(path=str(out/f'{name}-today.png'),full_page=True)
        pg.click('text=نقشه'); pg.wait_for_timeout(200); pg.screenshot(path=str(out/f'{name}-map.png'),full_page=True)
        pg.click('nav.tabs >> text=آمار'); pg.wait_for_timeout(200); pg.screenshot(path=str(out/f'{name}-stats.png'),full_page=True)
        pg.click('nav.tabs >> text=تنظیمات'); pg.wait_for_timeout(200); pg.screenshot(path=str(out/f'{name}-set.png'),full_page=True)
        ov=pg.evaluate("document.documentElement.scrollWidth>document.documentElement.clientWidth")
        print(name,'horizontal overflow:',ov)
        ctx.close()
    b.close()
finally:
    srv.terminate()
print('errors:',errs)
