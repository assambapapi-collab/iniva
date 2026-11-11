"""Build dist/index.html: a single self-contained file embedding the knowledge base, safety rules and clinic list."""
import json, pathlib
root = pathlib.Path(__file__).parent
t = (root/"src/index.template.html").read_text(encoding="utf-8")
for key, f in [("__KB__","knowledge_base.json"),("__SAFETY__","safety.json"),("__CLINICS__","clinics.json")]:
    t = t.replace(key, json.dumps(json.load(open(root/"data"/f,encoding="utf-8")), ensure_ascii=False))
(root/"dist").mkdir(exist_ok=True)
(root/"dist/index.html").write_text(t, encoding="utf-8")
print("dist/index.html written")
