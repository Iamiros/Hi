const KEY = "amir-cut-v1";
const LANG = (() => {
  const m = /grip-lang=(fa|en)/.exec(window.name || ""); if (m) return m[1];
  try { const o = JSON.parse(localStorage.getItem(KEY) || "{}"); return o && o.prefs && o.prefs.lang === "en" ? "en" : "fa"; } catch (e) { return "fa"; }
})();
const I18N = LANG === "en" ? __I18N__ : null;
const TT = s => I18N ? (I18N[s] ?? s) : s;
const PROGRAM = LANG === "en" ? __PROGRAM_EN__ : __PROGRAM__;
const GUIDE = __GUIDE__;
const IMGS = __IMGS__;
const DEFAULT_START = "2026-10-03";
const TARGET_W = 83, START_W = 89;
// WHOOP morning entry: recovery %, HRV ms, resting HR, sleep performance %, sleep hours, yesterday's strain and calories burned.
const WH = { rec: [0, 100], hrv: [5, 300], rhr: [25, 150], sp: [0, 100], sh: [0, 16], strain: [0, 21], kcal: [0, 10000] };
const DAYFA = ["شنبه","یکشنبه","دوشنبه","سه‌شنبه","چهارشنبه","پنجشنبه","جمعه"];
const FD = "۰۱۲۳۴۵۶۷۸۹";

/* ---------- helpers ---------- */
const fa = s => LANG === "en" ? String(s) : String(s).replace(/\d/g, d => FD[d]).replace(/\./g, "٫");
const faN = (x, d = 0) => (x == null || isNaN(x)) ? "-" : fa(Number(x).toFixed(d));
const esc = s => String(s).replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
const en = s => `<bdi class="en${String(s).length <= 24 ? " nw" : ""}" dir="ltr" lang="en">${esc(s)}</bdi>`;
const toEn = s => String(s).replace(/[۰-۹]/g, d => FD.indexOf(d)).replace(/[٠-٩]/g, d => "٠١٢٣٤٥٦٧٨٩".indexOf(d)).replace(/[٫,]/g, ".").trim();
const parseNum = (s, lo, hi) => { const t = toEn(s); if (t === "") return null; const n = Number(t); return isFinite(n) && n >= lo && n <= hi ? n : undefined; };
const $ = (s, r = document) => r.querySelector(s);
const parseISO = s => { const [y, m, d] = s.split("-").map(Number); return new Date(y, m - 1, d, 12); };
const iso = d => `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, "0")}-${String(d.getDate()).padStart(2, "0")}`;
const addDays = (d, n) => { const x = new Date(d); x.setDate(x.getDate() + n); return x; };
const todayISO = () => iso(new Date());
const clamp = (x, a, b) => Math.max(a, Math.min(b, x));
const mean = a => a.length ? a.reduce((s, x) => s + x, 0) / a.length : null;
const fmtJ = new Intl.DateTimeFormat(LANG === "en" ? "en-US" : "fa-IR", { month: LANG === "en" ? "short" : "long", day: "numeric" });
const fmtG = new Intl.DateTimeFormat(LANG === "en" ? "en-US" : "fa-IR-u-ca-gregory", { year: "numeric", month: "long", day: "numeric" });

/* ---------- persistence ---------- */
let mem = null;
const dflt = () => ({ v: 1, start: DEFAULT_START, days: {}, tests: {}, foods: [], prefs: { mode: "gym", theme: "system", lang: "fa" } });
const isObj = o => o && typeof o === "object" && !Array.isArray(o);
const numOr = (x, lo, hi) => { const n = Number(x); return isFinite(n) && x !== "" && x !== null && n >= lo && n <= hi ? n : null; };
function normalize(o) {
  if (!isObj(o) || typeof o.start !== "string" || !/^\d{4}-\d{2}-\d{2}$/.test(o.start) || parseISO(o.start).getDay() !== 6 || !isObj(o.days)) return null;
  const R = dflt(); R.start = o.start;
  Object.keys(o.days).forEach(k => {
    if (!/^\d{4}-\d{2}-\d{2}$/.test(k) || !isObj(o.days[k])) return;
    const d = o.days[k], r = { done: {}, water: numOr(d.water, 0, 20000) || 0, lifts: {}, sets: {} };
    if (isObj(d.sets)) Object.keys(d.sets).forEach(x => { r.sets[x] = numOr(d.sets[x], 0, 20) || 0; });
    if (isObj(d.done)) Object.keys(d.done).forEach(x => { const v = d.done[x]; r.done[x] = typeof v === "boolean" ? v : (numOr(v, 0, 10) || 0); });
    if (isObj(d.lifts)) Object.keys(d.lifts).forEach(x => { if (Array.isArray(d.lifts[x])) r.lifts[x] = d.lifts[x].slice(0, 20).filter(isObj).map(s => ({ kg: numOr(s.kg, 0, 500) ?? "", reps: numOr(s.reps, 0, 200) ?? "", rpe: numOr(s.rpe, 5, 10) ?? "", ex: typeof s.ex === "string" ? s.ex.slice(0, 20) : "" })); });
    const w = numOr(d.weight, 30, 250), st = numOr(d.steps, 0, 100000);
    if (w !== null) r.weight = w; if (st !== null) r.steps = st;
    if (typeof d.note === "string") r.note = d.note.slice(0, 2000);
    [["sleepH", 0, 16], ["energy", 1, 5], ["sore", 1, 5], ["hunger", 1, 5], ["kin", 0, 10000], ["pin", 0, 1000], ["waist", 40, 200]].forEach(([f, lo, hi]) => { const v = numOr(d[f], lo, hi); if (v !== null) r[f] = v; });
    if (Array.isArray(d.food)) r.food = d.food.filter(isObj).slice(0, 80).map(x => ({ m: numOr(x.m, 0, 4) ?? 4, n: String(x.n || "").slice(0, 60), a: String(x.a || "").slice(0, 30), k: numOr(x.k, 0, 5000) || 0, p: numOr(x.p, 0, 500) || 0, c: numOr(x.c, 0, 1000) || 0, f: numOr(x.f, 0, 500) || 0 })).filter(x => x.n);
    if (typeof d.wake === "string" && /^([01]\d|2[0-3]):[0-5]\d$/.test(d.wake)) r.wake = d.wake;
    if (d.wakeAsked === true) r.wakeAsked = true;
    if (typeof d.wt === "string" && /^([01]\d|2[0-3]):[0-5]\d$/.test(d.wt)) r.wt = d.wt;
    if (isObj(d.mt)) { r.mt = {}; Object.keys(d.mt).forEach(k => { if (/^[0-4]$/.test(k) && /^([01]\d|2[0-3]):[0-5]\d$/.test(d.mt[k])) r.mt[k] = d.mt[k]; }); }
    if (isObj(d.wh)) { r.wh = {}; Object.keys(WH).forEach(f => { const v = numOr(d.wh[f], WH[f][0], WH[f][1]); if (v !== null) r.wh[f] = v; }); }
    if (isObj(d.sf)) { r.sf = {}; ["ch", "ab", "th"].forEach(f => { const v = numOr(d.sf[f], 1, 80); if (v !== null) r.sf[f] = v; }); }
    R.days[k] = r;
  });
  if (isObj(o.tests)) Object.keys(o.tests).forEach(p => { if (isObj(o.tests[p])) { R.tests[p] = {}; Object.keys(o.tests[p]).forEach(t => { const n = numOr(o.tests[p][t], 0, 1000); R.tests[p][t] = n === null ? "" : n; }); } });
  if (Array.isArray(o.foods)) R.foods = o.foods.filter(isObj).slice(0, 100).map(x => ({ id: String(x.id || "").slice(0, 20), n: String(x.n || "").slice(0, 60), u: x.u ? String(x.u).slice(0, 20) : null, ug: numOr(x.ug, 0, 2000) || 0, k: numOr(x.k, 0, 2000) || 0, p: numOr(x.p, 0, 200) || 0, c: numOr(x.c, 0, 300) || 0, f: numOr(x.f, 0, 200) || 0 })).filter(x => x.id && x.n);
  if (isObj(o.prefs)) { if (["gym", "home"].includes(o.prefs.mode)) R.prefs.mode = o.prefs.mode; if (["system", "light", "dark"].includes(o.prefs.theme)) R.prefs.theme = o.prefs.theme; if (["fa", "en"].includes(o.prefs.lang)) R.prefs.lang = o.prefs.lang; }
  return R;
}
function load() {
  let raw = null;
  try { raw = localStorage.getItem(KEY); } catch (e) {}
  if (raw) {
    try { const n = normalize(JSON.parse(raw)); if (n) return n; } catch (e) {}
    try { localStorage.setItem(KEY + "-corrupt", raw); } catch (e) {}
  }
  return mem || dflt();
}
let S = load();
let saveWarned = false;
let savedAt = (() => { try { return +localStorage.getItem(KEY + "-t") || 0; } catch (e) { return 0; } })();
let onSaved = null;
function save(fromCloud) {
  mem = S; if (!fromCloud) savedAt = Date.now();
  if (onSaved && !fromCloud) onSaved();
  if (!fromCloud && typeof afterSave === "function") afterSave();
  try { localStorage.setItem(KEY, JSON.stringify(S)); localStorage.setItem(KEY + "-t", String(savedAt)); saveWarned = false; }
  catch (e) { if (!saveWarned) { saveWarned = true; toast("ذخیره‌سازی مرورگر در دسترس نیست. از Export برای پشتیبان استفاده کن."); } }
}
function toast(msg) {
  const t = toast.el = toast.el || $("#toast"),  // kept by reference: a dialog redraw can detach it
    host = document.querySelector("dialog[open]") || document.body; if (t.parentNode !== host) host.appendChild(t); t.textContent = msg; t.hidden = false;
  clearTimeout(toast.t); toast.t = setTimeout(() => t.hidden = true, 3200);
}
function D(date) { const d = S.days[date] || (S.days[date] = { done: {}, water: 0, lifts: {}, sets: {} }); d.sets = d.sets || {}; d.lifts = d.lifts || {}; return d; }
const BWLIFTS = ["pullup", "chin", "dip"];
function peek(date) { return S.days[date] || null; }

/* ---------- program mapping ---------- */
const startDate = () => parseISO(S.start);
const dateOf = i => iso(addDays(startDate(), i));
function todayIdx() {
  const diff = Math.round((parseISO(todayISO()) - startDate()) / 864e5);
  return diff;
}
function info(i) {
  const week = Math.floor(i / 7) + 1, dow = i % 7;
  const letter = ({0:"A",1:"B",3:"C",5:"D",6:"E"})[dow] || null;
  const refeed = dow === 1 && week >= 3;
  const type = refeed ? "refeed" : (letter ? "train" : "walk");
  const ph = PROGRAM.phases.find(p => p[0].includes(week));
  return {
    i, date: dateOf(i), week, dow, letter, type, refeed, weekend: dow <= 1,
    phase: ph[1], phaseFa: LANG === "en" ? ph[3] : ph[2], phaseEn: ph[3],
    deload: week === 4, test: i === 0 || (dow === 6 && (week === 4 || week === 8)), mu: week === 8 && dow === 6,
  };
}
function doseOf(ex, week, home) {
  let d = ex.dose;
  if (home && ex.dose_home) d = ex.dose_home;
  if (typeof d === "string") return PROGRAM.schemes[d][week - 1];
  return (week === 4 || week === 8) ? d[1] : d[0];
}
function waterTarget(inf) { return inf.letter ? 4000 : 3500; }

function items(inf) {
  const n = PROGRAM.nutrition[inf.type];
  const L = [];
  if (inf.letter) L.push({ k: "workout", t: "b", l: `تمرین ${inf.letter} انجام شد` });
  const walkRange = inf.weekend ? "۹۰ تا ۱۲۰" : "۶۰ تا ۹۰";
  L.push({ k: "walk", t: "b", l: `پیاده‌روی ${walkRange} دقیقه (هدف ۱۲٬۰۰۰ قدم یا بیشتر)` });
  L.push({ k: "kcal", t: "b", l: `کالری ${fa(n.kcal)}` + (inf.type === "refeed" ? " (ریفید)" : "") });
  L.push({ k: "protein", t: "c", max: 4, l: `پروتئین ${fa(n.p)} گرم در ۴ وعده` });
  L.push({ k: "water", t: "w", l: `آب حداقل ${fa(waterTarget(inf) / 1000)} لیتر` });
  if (inf.letter) L.push({ k: "salt", t: "b", l: "آب با ¼ قاشق چایخوری نمک یا ساشه الکترولیت قبل از تمرین" });
  L.push({ k: "creatine", t: "b", l: `${en("Creatine Monohydrate")} ${fa(5)} g` });
  L.push({ k: "hang", t: "b", l: `${en("Dead Hang")} ${fa(3)} دقیقه` + "" });
  L.push({ k: "sleep", t: "b", l: "خواب حداقل ۷٫۵ ساعت" });
  if (!inf.letter) L.push({ k: "gtg", t: "c", max: 5, l: `${en("Grease the Groove")}: ۵ ست Pull-up سخت‌گیرانه با ۴۰ تا ۵۰٪ حداکثر، فاصله ≥ ۶۰ دقیقه` });
  if (inf.dow === 6) L.push({ k: "checkin", t: "b", l: "چک‌این هفتگی: عکس جلو/پشت/پهلو، دور شکم، کالیپر ۳ نقطه" });
  if (inf.test) L.push({ k: "tests", t: "b", l: "تست‌ها ثبت شد (بخش آمار)" });
  if (inf.mu) L.push({ k: "mu", t: "b", l: `${en("Pull-up Test Day")} انجام شد` });
  return L;
}
function frac(it, dd, inf) {
  const v = dd ? dd.done[it.k] : 0;
  if (it.t === "b") return v ? 1 : 0;
  if (it.t === "c") return clamp((v || 0) / it.max, 0, 1);
  if (it.t === "w") return clamp(((dd && dd.water) || 0) / waterTarget(inf), 0, 1);
  return 0;
}
function pct(i) {
  const inf = info(i), dd = peek(inf.date);
  if (!dd) return 0;
  const L = items(inf);
  return L.reduce((s, it) => s + frac(it, dd, inf), 0) / L.length;
}

/* ---------- stats ---------- */
function weightOn(date) { const d = peek(date); return d && d.weight > 0 ? +d.weight : null; }
function avg7(i) {
  const a = [];
  for (let k = Math.max(0, i - 6); k <= i; k++) { const w = weightOn(dateOf(k)); if (w) a.push(w); }
  return mean(a);
}
function weekAvg(w) {
  const a = [];
  for (let k = (w - 1) * 7; k < w * 7; k++) { const x = weightOn(dateOf(k)); if (x) a.push(x); }
  return a.length >= 3 ? mean(a) : null;
}
function weeklyRates(lastWeek) {
  const out = [];
  for (let w = 2; w <= lastWeek; w++) {
    const a = weekAvg(w - 1), b = weekAvg(w);
    out.push({ w, rate: a != null && b != null ? a - b : null });
  }
  return out;
}
function e1rm(lib, set) {
  const bw = BWLIFTS.includes(lib) ? (latestWeight() || START_W) : 0;
  const kg = +set.kg || 0, r = +set.reps || 0;
  if (!r || (!kg && !bw)) return null;
  return (bw + kg) * (1 + r / 30);
}
function latestWeight() {
  for (let i = 55; i >= 0; i--) { const w = weightOn(dateOf(i)); if (w) return w; }
  return null;
}
function strengthDrops() {
  const bad = [];
  ["a1","a2","b1","d1","c5"].forEach(ex => {
    const by = {};
    for (let i = 0; i < 56; i++) {
      const f = info(i); if (f.week === 4 || f.week === 8) continue;
      const dd = peek(f.date); const sets = dd && dd.lifts && dd.lifts[ex];
      if (!sets || !sets.length) continue;
      const g = {};
      sets.forEach(st => { const v = e1rm(st.ex, st); if (v) g[st.ex || ""] = Math.max(g[st.ex || ""] || 0, v); });
      Object.keys(g).forEach(k => (by[k] = by[k] || []).push(g[k]));
    }
    Object.keys(by).forEach(k => { const q = by[k], n = q.length; if (n >= 3 && q[n - 1] < q[n - 2] && q[n - 2] < q[n - 3]) bad.push(ex); });
  });
  return bad.filter((x, i) => bad.indexOf(x) === i);
}
function streak(cur) {
  let i = Math.min(cur, 55), n = 0;
  if (i >= 0 && pct(i) < 0.7) i--;
  for (; i >= 0; i--) { if (pct(i) >= 0.7) n++; else break; }
  return n;
}
function stepStreak(cur) {
  let i = Math.min(cur, 55), n = 0;
  const ok = k => { const d = peek(dateOf(k)); return d && d.steps >= 12000; };
  if (i >= 0 && !ok(i)) i--;
  for (; i >= 0; i--) { if (ok(i)) n++; else break; }
  return n;
}


const TESTS = [
  ["pullups", "Max Strict Pull-ups", "reps"], ["ctb", "Max Chest-to-Bar Pull-ups", "reps"],
  ["pdip", "Max Parallel Bar Dips", "reps"], ["sdip", "Max Straight Bar Dips", "reps"],
  ["hang", "Dead Hang", "s"], ["chinmax", "Max Strict Chin-ups", "reps"], ["hollow", "Hollow Body Hold", "s"],
  ["bw", "Bodyweight (7-day average)", "kg"],
  ["waist", "Waist at navel", "cm"], ["mu", "Muscle-Up", "reps"],
];
const LOWER_BETTER = ["bw", "waist"];
const PH = [["start", "شروع"], ["w4", "هفته ۴"], ["w8", "هفته ۸"]];


/* ---------- load suggestions ---------- */
const bwNow = () => latestWeight() || START_W;
const repsRange = d => { const m = /×(\d+)(?:-(\d+))?/.exec(d || ""); return m ? { lo: +m[1], hi: m[2] ? +m[2] : +m[1] } : null; };
// Effective 1RM of a logged set by load kind (bw: bodyweight + added, assist: bodyweight - assistance).
function setE1(lib, s) {
  const ld = (PROGRAM.lib[lib] || {}).ld, r = +s.reps || 0; if (!r || r > 15) return null;
  const kg = +s.kg || 0, k = ld ? ld[0] : "", eff = k === "bw" ? bwNow() + kg : k === "assist" ? bwNow() - kg : kg;
  return eff > 0 ? eff * (1 + r / 30) : null;
}
// Best logged 1RM in the 21 days before day i, else the starting estimate.
function baseE1(lib, i) {
  let best = 0;
  for (let k = Math.max(0, i - 21); k < i; k++) {
    const d = peek(dateOf(k)); if (!d || !d.lifts) continue;
    Object.values(d.lifts).forEach(a => a.forEach(s => { if ((s.ex || "") === lib) { const v = setE1(lib, s); if (v > best) best = v; } }));
  }
  const ld = (PROGRAM.lib[lib] || {}).ld;
  return best ? { e1: best, src: "log" } : ld ? { e1: ld[1], src: "est" } : null;
}
// Suggested working load for a lib at a dose string, using reps + reps-in-reserve (Epley).
function loadFor(lib, dose, i, deload) {
  const ld = (PROGRAM.lib[lib] || {}).ld; if (!ld || !dose || dose === "test" || !/×/.test(dose) || /\d+\s*s\b/.test(dose)) return null;
  if (ld[0] === "carry") return { kind: "carry", kg: ld[1], src: "est" };
  const b = baseE1(lib, i), rr = repsRange(dose); if (!b || !rr) return null;
  const pc = /@(\d+)(?:-(\d+))?%/.exec(dose), rpe = /RPE\s*([\d.]+)/.exec(dose), light = deload || /light/.test(dose);
  let load = pc ? b.e1 * (+pc[1] + +(pc[2] || pc[1])) / 200
    : b.e1 / (1 + (Math.ceil((rr.lo + rr.hi) / 2) + (rpe ? 10 - +rpe[1] : 2) + (lib === "adip" ? 2 : 0)) / 30);
  if (light) load *= 0.85;
  const k = ld[0], rnd = (x, st) => Math.max(0, Math.round(x / st) * st), bw = bwNow();
  if (k === "bw") { const add = load - bw; return { kind: k, kg: add >= 1.25 ? rnd(add, 1.25) : 0, src: b.src }; }
  if (k === "assist") return { kind: k, kg: rnd(bw - load, 2.5), src: b.src };
  const st = k === "bar" || k === "cable" ? 2.5 : k === "machine" ? 5 : load < 10 ? 1 : 2;
  return { kind: k, kg: Math.min(rnd(load, st), k === "db" ? 30 : 999), src: b.src };
}
