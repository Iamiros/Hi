"""Collect every Persian UI string (JS literals, template text, static HTML, program data)."""
import sys, json, re, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from jslex import lex, FALETTER
FADIG = re.compile(r'[\u06F0-\u06F9\u066A\u060C\u061B\u00AB\u00BB]')
DIG = str.maketrans({**{c: str(i) for i, c in enumerate('۰۱۲۳۴۵۶۷۸۹')}, '٫': '.', '٪': '%', '،': ',', '؛': ';', '«': '"', '»': '"'})
T = pathlib.Path(__file__).resolve().parent.parent
ESC = {'n': '\n', 't': '\t', '"': '"', "'": "'", '`': '`', '\\': '\\', '$': '$', '/': '/'}
def cook(raw):
    return re.sub(r'\\(.)', lambda m: ESC.get(m.group(1), m.group(1)), raw)
def js_tokens(src, a, b):
    for kind, i, j, _ in lex(src, a, b):
        seg = src[i:j]
        body = seg[1:-1] if kind == 'str' else seg
        if not (FALETTER.search(seg) or (FADIG.search(body) and FADIG.sub('', body).strip())): continue
        yield kind, i, j, cook(seg[1:-1] if kind == 'str' else seg)
def script_span(s):
    a = s.index('<script>') + 8; return a, s.rindex('</script>')
STATIC_RE = re.compile(r'>([^<>]*[ء-ی][^<>]*)<|(?:aria-label|title|placeholder)="([^"]*[ء-ی][^"]*)"')
def static_keys(html):
    a = html.index('<body>'); b = html.index('<script>')
    for m in STATIC_RE.finditer(html, a, b):
        v = (m.group(1) or m.group(2)).strip()
        if v: yield v
def data_keys(o):
    if isinstance(o, str):
        if FALETTER.search(o): yield o
    elif isinstance(o, dict):
        for v in o.values(): yield from data_keys(v)
    elif isinstance(o, (list, tuple)):
        for v in o: yield from data_keys(v)
def all_keys(prog):
    keys = {}
    for f in ('tracker.logic.js', 'tracker.template.html'):
        s = (T / f).read_text()
        a, b = script_span(s) if f.endswith('html') else (0, len(s))
        for _, i, _, k in js_tokens(s, a, b): keys.setdefault(k, f'{f}:{s.count(chr(10), 0, i) + 1}')
    for k in static_keys((T / 'tracker.template.html').read_text()): keys.setdefault(k, 'static')
    for k in data_keys(prog): keys.setdefault(k, 'program')
    return keys
if __name__ == '__main__':
    sys.path.insert(0, str(T))
    import build_prog
    keys = all_keys(build_prog.prog)
    en = json.loads((T / 'i18n/en.json').read_text()) if (T / 'i18n/en.json').exists() else {}
    miss = {k: v for k, v in keys.items() if k not in en}
    (T / 'i18n/missing.json').write_text(json.dumps(miss, ensure_ascii=False, indent=0))
    print(len(keys), 'keys,', len(miss), 'missing,', sum(len(k) for k in miss), 'chars')

RUN = re.compile(r'[^<>"]*[ء-يپچژکگی][^<>"]*')
def runs(key):
    for m in RUN.finditer(key):
        r = m.group(0).strip()
        if r: yield r
def translate(key, D):
    def rep(m):
        s = m.group(0); r = s.strip()
        if not r: return s
        lead = s[:len(s) - len(s.lstrip())]; trail = s[len(s.rstrip()):]
        return lead + D[r] + trail
    return RUN.sub(rep, key).translate(DIG)
