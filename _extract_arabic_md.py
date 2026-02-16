import json, re
from pathlib import Path

path = Path(r"c:\Users\al7ak\Documents\gitRepo\ENCH320-Labs\الفصل الثالث-التعامل مع البيانات التجميعية.ipynb")
nb = json.loads(path.read_text(encoding="utf-8"))

arabic_re = re.compile(r"[\u0600-\u06FF]")

cells = nb.get("cells", [])
targets = []
for i, cell in enumerate(cells):
    if cell.get("cell_type") != "markdown":
        continue
    src = "".join(cell.get("source", []))
    if not arabic_re.search(src):
        continue
    if "<details>" in src or "dir=\"rtl\"" in src:
        # Already converted to collapsible format.
        continue
    prev_id = cells[i - 1].get("id", "") if i > 0 else "TOP"
    targets.append({
        "index": i,
        "id": cell.get("id", ""),
        "prev_id": prev_id,
        "source": cell.get("source", [])
    })

out_path = Path(r"c:\Users\al7ak\Documents\gitRepo\ENCH320-Labs\_arabic_markdown_targets.json")
out_path.write_text(json.dumps(targets, ensure_ascii=False, indent=2), encoding="utf-8")
print(out_path)
