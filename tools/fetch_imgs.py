import json, subprocess, pathlib, io, time
from PIL import Image
SP='/tmp/claude-0/-home-user-Hi/54b47da7-daf8-5c46-b909-aca8dd4b7c8f/scratchpad/fedb.json'
db={x['name']:x for x in json.load(open(SP))}
MAP={'cars':'Shoulder Circles','bpa':'Band Pull Apart','scap':'Scapular Pull-Up','pushup':'Pushups','bench':'Barbell Bench Press - Medium Grip',
 'dbrow':'One-Arm Dumbbell Row','bbrow':'Bent Over Barbell Row','lat':'Side Lateral Raise','squat':'Barbell Full Squat','bss':'Split Squat with Dumbbells',
 'rdl':'Romanian Deadlift','slrdl':'Kettlebell One-Legged Deadlift','lunge':'Barbell Walking Lunge','stepup':'Dumbbell Step Ups','nordic':'Natural Glute Ham Raise',
 'calf':'Standing Calf Raises','rollout':'Ab Roller','highpull':'Band Assisted Pull-Up','incdb':'Incline Dumbbell Press','fepu':'Decline Push-Up',
 'ohp':'Standing Military Press','facepull':'Face Pull','hlr':'Hanging Leg Raise','dl':'Barbell Deadlift','pistol':'Kettlebell Pistol Squat',
 'farmer':"Farmer's Walk",'pullup':'Pullups','dip':'Parallel Bar Dip','pun':'Pullups','apu':'Band Assisted Pull-Up','bapu':'Band Assisted Pull-Up',
 'adip':'Dip Machine','tdip':'Dips - Chest Version','chin':'Chin-Up','cablelat':'Cable Seated Lateral Raise','bandlat':'Lateral Raise - With Bands',
 'reardelt':'Reverse Machine Flyes','bandrear':'Back Flyes - With Bands','inccurl':'Alternate Incline Dumbbell Curl','bandcurl':'Close-Grip EZ-Bar Curl with Band',
 'pushdown':'Triceps Pushdown - Rope Attachment','bandtri':'Triceps Pushdown','cablecrunch':'Cable Crunch','bpcrunch':'Crunches','pallof':'Pallof Press'}
out=pathlib.Path('img'); out.mkdir(exist_ok=True); done={}
for k,name in MAP.items():
    x=db[name]; key=x['id']
    if key in done: continue
    for n,rel in enumerate(x['images'][:2]):
        f=out/f'{key}-{n}.webp'
        if f.exists(): continue
        url='https://cdn.jsdelivr.net/gh/yuhonas/free-exercise-db@main/exercises/'+rel.replace(' ','%20')
        r=subprocess.run(['curl','-sS','-m','40','-f',url],capture_output=True)
        if r.returncode: print('FAIL',name,rel,r.stderr[:80]); continue
        im=Image.open(io.BytesIO(r.stdout)).convert('RGB'); im.thumbnail((420,420)); im.save(f,'WEBP',quality=58,method=6)
    done[key]=1
json.dump({k:db[v]['id'] for k,v in MAP.items()},open(out/'map.json','w'))
print(len(done),'sources', sum(p.stat().st_size for p in out.glob('*.webp'))//1024,'KB')
