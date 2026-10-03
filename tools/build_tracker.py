import json, pathlib, program as P
root = pathlib.Path(__file__).resolve().parent.parent
lib = {e["id"]: {k: e[k] for k in ("en", "fa", "cues", "mistakes", "reg", "prog", "yt")} for e in P.LIB}
for k, v in lib.items(): v["fan"] = P.FAN.get(k, "")
foods = [dict(id=f[0], n=f[1], en=f[2], k=f[3], p=f[4], c=f[5], f=f[6], u=f[7], ug=f[8]) for f in P.FOODS]
prog = dict(schemes=P.SCHEMES, phases=P.PHASES, warmup=P.WARMUP, nutrition=P.NUTRITION, lib=lib,
            workouts={k: dict(fa=v["fa"], ex=v["ex"], info=P.WORKOUT_INFO[k]) for k, v in P.WORKOUTS.items()}, muscles=P.MUSCLE_FA, foods=foods)
t = (root / "tools/tracker.template.html").read_text()
t = t.replace("/*__LOGIC__*/", (root / "tools/tracker.logic.js").read_text())
import base64
def font_css(barlow=True, archivo=False):
    f=root/"tools/fonts"; css=""
    face=lambda fam,w,fn,extra="": "@font-face{font-family:'%s';font-weight:%s;font-display:swap;%ssrc:url(data:font/woff2;base64,%s) format('woff2')}\n"%(fam,w,extra,base64.b64encode((f/fn).read_bytes()).decode())
    for n,w in (("Regular",400),("Medium",500),("Bold",700)): css+=face("Vazirmatn",w,"Vazirmatn-%s.woff2"%n)
    if barlow:
        for w in (500,600,700): css+=face("Barlow Condensed",w,"BarlowCondensed-%d.woff2"%w)
    if archivo: css+=face("Archivo","100 900","Archivo-var.woff2","font-stretch:62% 125%;")
    return css
if __name__!="__main__": pass
imap = json.loads((root/"tools/img/map.json").read_text())
uri = lambda f: "data:image/webp;base64," + base64.b64encode((root/"tools/img"/f).read_bytes()).decode()
imgs = {d: [uri(d+"-0.webp"), uri(d+"-1.webp")] for d in sorted(set(imap.values()))}
t = t.replace("__IMGS__", json.dumps(dict(map=imap, src=imgs)))
base = t.replace("__FONTS__",font_css(barlow=False, archivo=True)).replace("__PROGRAM__", json.dumps(prog, ensure_ascii=False))
out = base.replace("__GUIDE__", '"../guide/index.html"')
(root / "tracker/index.html").write_text(out)
import re as _re
art = base.replace("__GUIDE__", "null")
title = _re.search(r"<title>.*?</title>", art, _re.S).group(0)
style = _re.search(r"<style>.*?</style>", art, _re.S).group(0)
style = style.replace("padding:env(safe-area-inset-top) env(safe-area-inset-right) calc(104px + env(safe-area-inset-bottom)) env(safe-area-inset-left)", "padding:0 0 calc(104px + env(safe-area-inset-bottom)) 0")
body = _re.search(r"<body>(.*)</body>", art, _re.S).group(1)
(root / "tracker/artifact.html").write_text(title + "\n" + style + "\n" + body)
(root / "tracker/manifest.webmanifest").write_text(json.dumps({
 "name": "GRIP · گریپ", "short_name": "GRIP", "lang": "fa", "dir": "rtl", "start_url": "./index.html", "scope": "./",
 "display": "standalone", "background_color": "#07090D", "theme_color": "#07090D",
 "id": "./index.html", "icons": [{"src": "icon-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any"},
           {"src": "icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any"}, {"src": "icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"}]}, ensure_ascii=False, indent=1))
import hashlib
H=hashlib.sha1(out.encode()).hexdigest()[:8]
(root / "tracker/sw.js").write_text('''const C="grip-HASH",A=["./","index.html","manifest.webmanifest","icon.svg","icon-180.png","icon-192.png","icon-512.png"];
self.addEventListener("install",e=>{e.waitUntil(caches.open(C).then(c=>c.addAll(A)).then(()=>self.skipWaiting()))});
self.addEventListener("activate",e=>{e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(x=>x!==C).map(x=>caches.delete(x)))).then(()=>self.clients.claim()))});
self.addEventListener("fetch",e=>{
 if(e.request.method!=="GET")return;
 e.respondWith(caches.match(e.request,{ignoreSearch:true}).then(h=>{
  const n=fetch(e.request).then(r=>{if(r&&r.status===200){const cp=r.clone();return caches.open(C).then(c=>c.put(e.request,cp)).then(()=>r)}return r}).catch(()=>h);
  return h||n}))});
'''.replace("HASH",H))
(root / "tracker/icon.svg").write_text((root / "tools/icon.svg").read_text())
