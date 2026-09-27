"""Build the checked-in GitHub Pages site using Python's standard library."""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
tasks = json.loads((ROOT / "data/tasks.json").read_text(encoding="utf-8"))
assert isinstance(tasks, list) and tasks, "The task catalog must not be empty"
ids = set()
for task in tasks:
    assert re.fullmatch(r"T\d{2}-\d{3}", task["id"]), task["id"]
    assert task["id"] not in ids, f"Duplicate ID: {task['id']}"
    ids.add(task["id"])
    assert set(task["configs"]) == {"B", "G", "P", "GP"}, task["id"]
    assert task["axis"] in {"G-O", "G-S", "G-L", "G-C", "G-Q", "G-H", "G-P", "G-E"}
    assert isinstance(task["core"], bool)
    for name in ("title", "category", "short", "mini", "scene", "training", "common", "boundary"):
        assert isinstance(task[name], str) and task[name].strip(), (task["id"], name)
    for group, config in task["configs"].items():
        for name in ("instruction", "success", "claim"):
            assert isinstance(config[name], str) and config[name].strip(), (task["id"], group, name)
        assert task["previews"][group].strip()
    for source in task["sources"]:
        assert source["url"].startswith("https://"), source["url"]

template = (ROOT / "site/index.template.html").read_text(encoding="utf-8")
assert template.count("__ATLAS_DATA__") == 1, "Missing or duplicate template slot"
# The data lives inside a script element inside the iframe's data-srcdoc attribute.
payload = json.dumps(tasks, ensure_ascii=False).replace("<", "\\u003c")
page = template.replace("__ATLAS_DATA__", html.escape(payload, quote=True))
page = page.replace('<html lang="en"', '<html lang="zh-CN"')
page = page.replace('&lt;html lang=&quot;en&quot;', '&lt;html lang=&quot;zh-CN&quot;')
out = ROOT / "docs"
out.mkdir(exist_ok=True)
(out / "index.html").write_text(page, encoding="utf-8")
(out / "tasks.json").write_text(json.dumps(tasks, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
(out / ".nojekyll").touch()
print(f"Built docs/index.html: {len(tasks)} tasks, {sum(len(t['configs']) for t in tasks)} configurations")
