import glob, pathlib, subprocess, time, json
from playwright.sync_api import sync_playwright
CH=glob.glob('/opt/pw-browsers/chromium-1194/chrome-linux*/chrome')[0]
root=pathlib.Path(__file__).resolve().parent.parent
out=pathlib.Path('/tmp/claude-0/-home-user-Hi/54b47da7-daf8-5c46-b909-aca8dd4b7c8f/scratchpad/s3'); out.mkdir(parents=True,exist_ok=True)
srv=subprocess.Popen(['python3','-m','http.server','8792','-d',str(root)],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL); time.sleep(1)
res={}; errs=[]
try:
 with sync_playwright() as p:
  b=p.chromium.launch(executable_path=CH)
  for name,w,h,sch in [('m','390','844','dark'),('d','1280','900','light')]:
   ctx=b.new_context(viewport={'width':int(w),'height':int(h)},color_scheme=sch,device_scale_factor=2 if name=='m' else 1)
   ctx.add_init_script("const _D=Date;const off=new _D('2026-10-15T10:00:00+08:00')-new _D();Date=class extends _D{constructor(...a){a.length?super(...a):super(_D.now()+off)}static now(){return _D.now()+off}};")
   pg=ctx.new_page(); pg.on('pageerror',lambda e:errs.append(str(e)))
   pg.goto('http://localhost:8792/tracker/index.html'); pg.wait_for_timeout(400); pg.evaluate("localStorage.clear()"); pg.reload(); pg.wait_for_timeout(400)
   # yesterday food for copy test
   pg.evaluate("()=>{const d=D(dateOf(sel-1));d.food=[{m:0,n:'تست',a:'۱ عدد',k:100,p:10,c:5,f:2}];save();}")
   pg.click('nav.tabs >> text=غذا'); pg.wait_for_timeout(300)
   pg.click('[data-act=fadd][data-m="0"]'); pg.wait_for_timeout(200)
   pg.fill('#fq','مرغ'); pg.wait_for_timeout(150)
   pg.click('[data-act=fpick][data-id=chk]'); pg.fill('#famt','200'); pg.wait_for_timeout(100)
   pg.screenshot(path=str(out/f'{name}-foodsheet.png'))
   pg.click('[data-act=fsave]'); pg.wait_for_timeout(200)
   pg.click('[data-act=fadd][data-m="0"]'); pg.click('[data-act=fpick][data-id=eggw]'); pg.wait_for_timeout(100)
   pg.fill('#famt','5'); pg.click('[data-act=fsave]'); pg.wait_for_timeout(150)
   pg.click('[data-act=fadd][data-m="1"]'); pg.click('[data-act=fpick][data-id=whey]'); pg.fill('#famt','1'); pg.click('[data-act=fsave]'); pg.wait_for_timeout(150)
   pg.click('[data-act=fcopy]'); pg.wait_for_timeout(150)
   # custom food
   pg.click('[data-act=fnew]'); pg.fill('#nfn','بیسکویت'); pg.select_option('#nfb','u'); pg.fill('#nfu','بسته'); pg.fill('#nfk','250'); pg.fill('#nfp','5'); pg.fill('#nfc','30'); pg.fill('#nff','12'); pg.click('[data-act=fnewsave]'); pg.wait_for_timeout(150); pg.fill('#famt','2'); pg.click('[data-act=fsave]'); pg.wait_for_timeout(200)
   res[name+'_food']=pg.evaluate("(()=>{const d=S.days[dateOf(sel)];return {n:d.food.length,kin:d.kin,pin:d.pin,items:d.food.map(x=>x.n+':'+x.k+'/'+x.p)}})()")
   pg.screenshot(path=str(out/f'{name}-food.png'),full_page=True)
   pg.click('[data-act=fdel] >> nth=0'); pg.wait_for_timeout(150); res[name+'_afterdel']=pg.evaluate("S.days[dateOf(sel)].food.length")
   # pages
   pg.click('nav.tabs >> text=امروز'); pg.wait_for_timeout(200)
   pg.click('.ename >> nth=0'); pg.wait_for_timeout(300); pg.screenshot(path=str(out/f'{name}-expage.png'),full_page=True)
   res[name+'_expage']=pg.inner_text('.pt-fa')
   pg.click('[data-act=exalt]') if pg.is_visible('[data-act=exalt]') else None
   pg.click('[data-act=wopage] >> nth=0'); pg.wait_for_timeout(300); pg.screenshot(path=str(out/f'{name}-wopage.png'),full_page=True)
   res[name+'_wopage']=pg.inner_text('.pt-en')
   pg.click('[data-act=pback]'); pg.wait_for_timeout(200); res[name+'_back_today']=pg.is_visible('.hero .ring')
   pg.click('nav.tabs >> text=آمار'); pg.wait_for_timeout(300); res[name+'_map_in_stats']=pg.is_visible('.hm')
   pg.screenshot(path=str(out/f'{name}-stats.png'),full_page=True)
   pg.reload(); pg.wait_for_timeout(300); res[name+'_persist']=pg.evaluate("S.days[dateOf(sel)].food.length")
   res[name+'_hscroll']=pg.evaluate("document.documentElement.scrollWidth>document.documentElement.clientWidth")
   ctx.close()
  b.close()
finally: srv.terminate()
print(json.dumps(res,ensure_ascii=False,indent=1)); print('errors',errs)
