const C="grip-da0714df",A=["./","index.html","manifest.webmanifest","icon.svg","icon-180.png","icon-192.png","icon-512.png"];
self.addEventListener("install",e=>{e.waitUntil(caches.open(C).then(c=>c.addAll(A)).then(()=>self.skipWaiting()))});
self.addEventListener("activate",e=>{e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(x=>x!==C).map(x=>caches.delete(x)))).then(()=>self.clients.claim()))});
self.addEventListener("fetch",e=>{
 if(e.request.method!=="GET")return;
 e.respondWith(caches.match(e.request,{ignoreSearch:true}).then(h=>{
  const n=fetch(e.request).then(r=>{if(r&&r.status===200){const cp=r.clone();return caches.open(C).then(c=>c.put(e.request,cp)).then(()=>r)}return r}).catch(()=>h);
  return h||n}))});
