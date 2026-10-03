"""Build-time i18n: wrap Persian JS literals in T(), and make English copies of data."""
import json, pathlib, copy
from extract import js_tokens, script_span, all_keys, translate, data_keys, FALETTER
D = json.loads((pathlib.Path(__file__).parent / 'en.json').read_text())
def wrap_js(src, a=0, b=None):
    b = len(src) if b is None else b
    out, last = [], a
    for kind, i, j, key in js_tokens(src, a, b):
        out.append(src[last:i])
        out.append(f'TT({src[i:j]})' if kind == 'str' else '${TT(%s)}' % json.dumps(key, ensure_ascii=False))
        last = j
    return src[:a] + ''.join(out) + src[last:]
def en_dict(prog):
    return {k: translate(k, D) for k in all_keys(prog)}
def en_data(o, tr):
    if isinstance(o, str): return tr.get(o, o) if FALETTER.search(o) else o
    if isinstance(o, dict): return {k: en_data(v, tr) for k, v in o.items()}
    if isinstance(o, (list, tuple)): return [en_data(v, tr) for v in o]
    return o
