import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent)); sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
import extract, build_prog
D = json.loads((pathlib.Path(__file__).parent / 'en.json').read_text())
miss = []
for k in extract.all_keys(build_prog.prog):
    for r in extract.runs(k):
        if r not in D and r not in miss: miss.append(r)
for r in miss: print(json.dumps(r, ensure_ascii=False))
