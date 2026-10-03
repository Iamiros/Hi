import json, sys, pathlib
p = pathlib.Path(__file__).parent / 'en.json'
d = json.loads(p.read_text()); d.update(json.loads(sys.argv[1])); p.write_text(json.dumps(d, ensure_ascii=False, indent=0))
