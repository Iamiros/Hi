import glob, pathlib, json
from playwright.sync_api import sync_playwright
CH=glob.glob('/opt/pw-browsers/chromium-1194/chrome-linux*/chrome')[0]
root=pathlib.Path(__file__).resolve().parent.parent
with sync_playwright() as p:
    b=p.chromium.launch(executable_path=CH); pg=b.new_page()
    errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file://'+str(root/'tracker/index.html')); pg.wait_for_timeout(500)
    r=pg.evaluate("""()=>{
      const bad=[];const days=[];
      for(let i=0;i<56;i++){const f=info(i),L=items(f),k=L.map(x=>x.k);days.push([i,f]);
        const wd=parseISO(f.date).getDay(); if(((i%7)+6)%7!==wd) bad.push('dow '+i);
        const kc=PROGRAM.nutrition[f.type].kcal, hasL=!!f.letter;
        const exp={0:'A',1:'B',3:'C',5:'D',6:'E'}[f.dow]||null; if(f.letter!==exp) bad.push('letter '+i);
        if(hasL!==k.includes('workout')||hasL!==k.includes('salt')) bad.push('workout/salt '+i);
        if(hasL===k.includes('gtg')) bad.push('gtg '+i);
        if(f.dow===1&&f.week>=3){ if(f.type!=='refeed'||kc!==2500) bad.push('refeed '+i)}
        else if(hasL){ if(f.type!=='train'||kc!==2100) bad.push('train '+i)}
        else { if(f.type!=='walk'||kc!==1900) bad.push('walk '+i)}
        if(f.refeed!==(f.dow===1&&f.week>=3)) bad.push('refeedflag '+i);
        if((f.dow===6)!==k.includes('checkin')) bad.push('checkin '+i);
        if(f.test !== (i===0||(f.dow===6&&(f.week===4||f.week===8)))) bad.push('test '+i);
        if(f.mu!==(f.week===8&&f.dow===6)) bad.push('mu '+i);
        if(f.deload!==(f.week===4)) bad.push('deload '+i);
        if(waterTarget(f)!==(hasL?4000:3500)) bad.push('water '+i);
        if(f.weekend!==(f.dow<=1)) bad.push('weekend '+i);
      }
      // dosing spot checks
      const A=PROGRAM.workouts.A.ex, out={};
      out.a1=[1,2,3,4,5,6,7,8].map(w=>doseOf(A[0],w,false));
      out.d2=[1,2,3,4,5,6,7,8].map(w=>doseOf(PROGRAM.workouts.D.ex[1],w,false));
      out.d1home=[1,4].map(w=>doseOf(PROGRAM.workouts.D.ex[0],w,true));
      out.d5=[1,4,8].map(w=>doseOf(PROGRAM.workouts.D.ex[4],w,false));
      out.e1=[1,4].map(w=>doseOf(PROGRAM.workouts.E.ex[0],w,false));
      // all exercises have gym+home
      PROGRAM.workouts && Object.values(PROGRAM.workouts).forEach(W=>W.ex.forEach(e=>{if(!PROGRAM.lib[e.gym]||!PROGRAM.lib[e.home]) bad.push('lib '+e.id)}));
      return {bad,out,counts:{refeed:days.filter(d=>d[1].refeed).length,train:days.filter(d=>d[1].type==='train').length}};
    }""")
    print(json.dumps(r,ensure_ascii=False,indent=1)); print('pageerrors',errs)
    # start-date validation + persistence + import/export
    pg.evaluate("localStorage.clear()"); pg.reload(); pg.wait_for_timeout(300)
    pg.click('nav.tabs >> text=تنظیمات')
    pg.fill('#sd','2026-10-05'); pg.dispatch_event('#sd','change'); pg.wait_for_timeout(200)
    print('start after non-monday:',pg.evaluate("S.start"))
    pg.fill('#sd','2026-10-10'); pg.dispatch_event('#sd','change'); print('start after monday:',pg.evaluate("S.start"))
    pg.click('nav.tabs >> text=امروز'); 
    # ensure sel valid, toggle first item and water
    pg.click('.tick >> nth=0'); pg.click('text=+۵۰۰'); pg.fill('#w','88.6'); pg.dispatch_event('#w','change')
    pg.reload(); pg.wait_for_timeout(300)
    print('persisted:',pg.evaluate("JSON.stringify(Object.values(S.days)[0])"))
    exp=pg.evaluate("JSON.stringify(S)")
    pg.evaluate("localStorage.clear()"); 
    pathlib.Path('/tmp/bk.json').write_text(exp)
    pg.reload(); pg.click('nav.tabs >> text=تنظیمات'); pg.set_input_files('input[type=file]','/tmp/bk.json'); pg.wait_for_timeout(300); pg.click('#yes'); pg.wait_for_timeout(300)
    print('import ok:',pg.evaluate("S.start+' '+Object.keys(S.days).length"))
    print('csv header:',pg.evaluate("csv().split('\\n')[0]")[:120])
    b.close()
