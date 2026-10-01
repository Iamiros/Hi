import json, pathlib, program as P
root = pathlib.Path(__file__).resolve().parent.parent
lib = {e["id"]: {"en": e["en"], "yt": e["yt"]} for e in P.LIB}
prog = dict(schemes=P.SCHEMES, phases=P.PHASES, warmup=P.WARMUP, nutrition=P.NUTRITION, lib=lib,
            workouts={k: dict(fa=v["fa"], ex=v["ex"]) for k, v in P.WORKOUTS.items()})
t = (root / "tools/tracker.template.html").read_text()
t = t.replace("/*__LOGIC__*/", (root / "tools/tracker.logic.js").read_text())
import base64
def font_css():
    f=root/"tools/fonts"; css=""
    for fam,files in (("Vazirmatn",[("Regular",400),("Medium",500),("Bold",700)]),("Barlow Condensed",[("500",500),("600",600),("700",700)])):
        for n,w in files:
            fn=("Vazirmatn-%s.woff2"%n) if fam=="Vazirmatn" else ("BarlowCondensed-%s.woff2"%n)
            d=base64.b64encode((f/fn).read_bytes()).decode()
            css+="@font-face{font-family:'%s';font-weight:%d;font-display:swap;src:url(data:font/woff2;base64,%s) format('woff2')}\n"%(fam,w,d)
    return css
if __name__!="__main__": pass
base = t.replace("__FONTS__",font_css()).replace("__PROGRAM__", json.dumps(prog, ensure_ascii=False))
out = base.replace("__GUIDE__", '"../guide/index.html"')
(root / "tracker/index.html").write_text(out)
import re as _re
art = base.replace("__GUIDE__", "null")
title = _re.search(r"<title>.*?</title>", art, _re.S).group(0)
style = _re.search(r"<style>.*?</style>", art, _re.S).group(0)
style = style.replace("padding:env(safe-area-inset-top) env(safe-area-inset-right) calc(96px + env(safe-area-inset-bottom)) env(safe-area-inset-left)", "padding:0 0 calc(96px + env(safe-area-inset-bottom)) 0")
body = _re.search(r"<body>(.*)</body>", art, _re.S).group(1)
(root / "tracker/artifact.html").write_text(title + "\n" + style + "\n" + body)
(root / "tracker/manifest.webmanifest").write_text(json.dumps({
 "name": "برش ۸ هفته‌ای", "short_name": "Cut 8W", "lang": "fa", "dir": "rtl", "start_url": "./index.html", "scope": "./",
 "display": "standalone", "background_color": "#E9ECEF", "theme_color": "#E9ECEF",
 "id": "./index.html", "icons": [{"src": "icon-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any"},
           {"src": "icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any"}, {"src": "icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"}]}, ensure_ascii=False, indent=1))
import hashlib
H=hashlib.sha1(out.encode()).hexdigest()[:8]
(root / "tracker/sw.js").write_text('''const C="cut8w-HASH",A=["./","index.html","manifest.webmanifest","icon.svg","icon-180.png","icon-192.png","icon-512.png"];
self.addEventListener("install",e=>{e.waitUntil(caches.open(C).then(c=>c.addAll(A)).then(()=>self.skipWaiting()))});
self.addEventListener("activate",e=>{e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(x=>x!==C).map(x=>caches.delete(x)))).then(()=>self.clients.claim()))});
self.addEventListener("fetch",e=>{
 if(e.request.method!=="GET")return;
 e.respondWith(caches.match(e.request,{ignoreSearch:true}).then(h=>{
  const n=fetch(e.request).then(r=>{if(r&&r.status===200){const cp=r.clone();e.waitUntil(caches.open(C).then(c=>c.put(e.request,cp)))}return r}).catch(()=>h);
  return h||n}))});
'''.replace("HASH",H))
(root / "tracker/icon.svg").write_text('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><rect width="512" height="512" fill="#2B3E52"/>
<rect x="56" y="196" width="400" height="26" rx="13" fill="#9DBEDC"/><rect x="130" y="188" width="70" height="42" rx="8" fill="#C99A36"/><rect x="312" y="188" width="70" height="42" rx="8" fill="#C99A36"/>
<g fill="#E6EAEE"><rect x="96" y="262" width="22" height="120" rx="6"/><rect x="146" y="290" width="22" height="92" rx="6"/><rect x="196" y="318" width="22" height="64" rx="6"/><rect x="246" y="262" width="22" height="120" rx="6"/><rect x="296" y="290" width="22" height="92" rx="6"/><rect x="346" y="262" width="22" height="120" rx="6"/><rect x="396" y="318" width="22" height="64" rx="6"/></g></svg>''')
