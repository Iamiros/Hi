import glob, pathlib, subprocess, time, json
from playwright.sync_api import sync_playwright
CH=glob.glob('/opt/pw-browsers/chromium-1194/chrome-linux*/chrome')[0]
root=pathlib.Path(__file__).resolve().parent.parent
srv=subprocess.Popen(['python3','-m','http.server','8791','-d',str(root)],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL); time.sleep(1)
res={}; errs=[]
try:
 with sync_playwright() as p:
  b=p.chromium.launch(executable_path=CH); ctx=b.new_context(viewport={'width':390,'height':844},has_touch=True)
  ctx.add_init_script("const _D=Date;const off=new _D('2026-10-15T10:00:00+08:00')-new _D();Date=class extends _D{constructor(...a){a.length?super(...a):super(_D.now()+off)}static now(){return _D.now()+off}};")
  pg=ctx.new_page(); pg.on('pageerror',lambda e:errs.append(str(e)))
  pg.goto('http://localhost:8791/tracker/index.html'); pg.wait_for_timeout(500)
  pg.evaluate("localStorage.clear()"); pg.reload(); pg.wait_for_timeout(500)
  # 1 sleep then single tap energy
  pg.fill('#sl','7'); pg.click('[data-act=scale][data-f=energy][data-n="4"]'); pg.wait_for_timeout(200)
  res['energy_one_tap']=pg.evaluate("S.days[dateOf(sel)].energy")
  pg.click('[data-act=scale][data-f=sore][data-n="2"]'); pg.wait_for_timeout(200)
  res['fold_open_after_sore']=pg.evaluate("document.querySelector('details[data-d=rd]').open")
  res['hunger_visible']=pg.is_visible('[data-act=scale][data-f=hunger][data-n="3"]')
  # 11 last set timer + 10 untick
  n=pg.evaluate("document.querySelectorAll('.dot[data-id=d1]').length")
  pg.click(f'.dot[data-id=d1][data-n="{n}"]'); pg.wait_for_timeout(300)
  res['timer_after_last_set']=pg.is_visible('#timer') and pg.evaluate("document.body.classList.contains('has-timer')")
  # complete all
  pg.evaluate("""()=>{const inf=info(sel),d=D(inf.date);PROGRAM.workouts[inf.letter].ex.forEach(ex=>{d.sets[ex.id]=0});save();render();}""")
  dots=pg.evaluate("[...new Set([...document.querySelectorAll('.dot[data-act=set]')].map(x=>x.dataset.id+'|'+x.dataset.max))]")
  for k in dots:
    i,m=k.split('|'); pg.click(f'.dot[data-id={i}][data-n="{m}"]'); pg.wait_for_timeout(80)
  res['auto_done']=pg.evaluate("S.days[dateOf(sel)].done.workout")
  pg.click('.dot[data-id=d1][data-n="1"]'); pg.wait_for_timeout(150)
  res['undo_after_untick']=pg.evaluate("S.days[dateOf(sel)].done.workout")
  # 4 toast inside dialog + 6 plates on typed kg
  pg.click('[data-act=log][data-id=d1]'); pg.wait_for_timeout(300)
  pg.fill('#kg0','100'); pg.press('#kg0','Tab'); pg.wait_for_timeout(150)
  res['plates_typed']=pg.inner_text('#platewrap')[:80]
  pg.fill('#kg1','abc'); pg.press('#kg1','Tab'); pg.wait_for_timeout(150)
  res['toast_in_dialog']=pg.evaluate("document.getElementById('toast').parentNode.id")
  pg.click('[data-act=shclose]')
  # 13 water clamp, 14 arabic digits
  pg.evaluate("()=>{D(dateOf(sel)).water=19900;save();render();}"); pg.click('[data-act=water][data-v="500"]')
  res['water_clamp']=pg.evaluate("S.days[dateOf(sel)].water")
  pg.fill('#w','٨٨٫٤'); pg.press('#w','Tab'); pg.wait_for_timeout(100)
  res['arabic_digits']=pg.evaluate("S.days[dateOf(sel)].weight")
  # 8 plan week independent
  pg.click('nav.tabs >> text=برنامه'); pg.click('[data-act=wnext]'); pg.click('nav.tabs >> text=امروز')
  res['sel_after_plan']=pg.evaluate("sel")
  # 9 chal update
  pg.click('nav.tabs >> text=آمار'); pg.fill('[data-act=test][data-p=start][data-t=pullups]','7'); pg.press('[data-act=test][data-p=start][data-t=pullups]','Tab'); pg.wait_for_timeout(150)
  res['chal']=pg.inner_text('#chal')[:40]
  # 7 map pct
  pg.click('nav.tabs >> text=نقشه'); res['map_ok']=True
  # reload persistence
  pg.reload(); pg.wait_for_timeout(400); res['persist_energy']=pg.evaluate("S.days[dateOf(sel)].energy")
  b.close()
finally: srv.terminate()
print(json.dumps(res,ensure_ascii=False,indent=1)); print('errors',errs)
