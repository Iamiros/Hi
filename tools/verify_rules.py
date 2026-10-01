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
        const wd=new Date(parseISO(f.date)).getDay(); // 1=Mon
        if(((i%7)+1)%7!==wd) bad.push('dow '+i);
        const kc=PROGRAM.nutrition[f.type].kcal;
        if([0,1,3,4].includes(f.dow)){ if(f.type!=='train'||kc!==2100||!k.includes('workout')||k.includes('gtg')) bad.push('train '+i)}
        if(f.dow===2||f.dow===6){ if(f.type!=='walk'||kc!==1900||!k.includes('gtg')||k.includes('workout')) bad.push('walk '+i)}
        if(f.dow===5){ const exp=f.week>=3?'refeed':'walk'; if(f.type!==exp||!k.includes('gtg')) bad.push('sat '+i); if(f.week>=3&&kc!==2500) bad.push('ref kcal '+i)}
        if(f.dow===6!==k.includes('checkin')) bad.push('checkin '+i);
        if(f.test !== (i===0||(f.dow===4&&(f.week===4||f.week===8)))) bad.push('test '+i);
        if(f.mu!==(f.week===8&&f.dow===4)) bad.push('mu '+i);
        if(f.deload!==(f.week===4)) bad.push('deload '+i);
        
        const wt=L.find(x=>x.k==='water'); if(waterTarget(f)!==(f.type==='train'?4000:3500)) bad.push('water '+i);
        if((f.letter!==null)!==k.includes('salt')) bad.push('salt '+i);
      }
      // dosing spot checks
      const A=PROGRAM.workouts.A.ex, out={};
      out.a1=[1,2,3,4,5,6,7,8].map(w=>doseOf(A[0],w,false));
      out.d2=[1,2,3,4,5,6,7,8].map(w=>doseOf(PROGRAM.workouts.D.ex[1],w,false));
      out.a3=[1,4,8].map(w=>doseOf(A[2],w,false));
      out.d1home=[1,4].map(w=>doseOf(PROGRAM.workouts.D.ex[0],w,true));
      out.d6=[1,4,8].map(w=>doseOf(PROGRAM.workouts.D.ex[5],w,false));
      // all exercises have gym+home
      PROGRAM.workouts && Object.values(PROGRAM.workouts).forEach(W=>W.ex.forEach(e=>{if(!PROGRAM.lib[e.gym]||!PROGRAM.lib[e.home]) bad.push('lib '+e.id)}));
      return {bad,out,counts:{refeed:days.filter(d=>d[1].refeed).length,train:days.filter(d=>d[1].type==='train').length}};
    }""")
    print(json.dumps(r,ensure_ascii=False,indent=1)); print('pageerrors',errs)
    # start-date validation + persistence + import/export
    pg.evaluate("localStorage.clear()"); pg.reload(); pg.wait_for_timeout(300)
    pg.click('nav.tabs >> text=تنظیمات')
    pg.fill('#sd','2026-10-06'); pg.dispatch_event('#sd','change'); pg.wait_for_timeout(200)
    print('start after non-monday:',pg.evaluate("S.start"))
    pg.fill('#sd','2026-10-12'); pg.dispatch_event('#sd','change'); print('start after monday:',pg.evaluate("S.start"))
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
