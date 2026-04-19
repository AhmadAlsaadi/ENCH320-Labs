import json
import re
import time
from pathlib import Path

from deep_translator import GoogleTranslator

NOTEBOOK = Path("Lab_08_Introduction_to_Sympy (2).ipynb")
translator = GoogleTranslator(source="en", target="ar")

ARABIC_TEMPLATE = """<details>
<summary style=\"cursor: pointer; color: #667EEA; font-weight: bold; font-size: 14px; font-family: 'Amiri', serif;\">🌍 Arabic Translation / الترجمة العربية</summary>

<div dir=\"rtl\" style=\"text-align: right; margin-top: 10px; padding: 15px; background: linear-gradient(135deg, #F5F5F5 0%, #FAFAFA 100%); border-radius: 8px; border-right: 4px solid #667EEA; font-family: 'Amiri', serif; font-size: 16px; line-height: 1.8;\">

<link href=\"https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&display=swap\" rel=\"stylesheet\">

{content}

</div>
</details>"""

PATTERNS = [
    r"```[\s\S]*?```",
    r"`[^`\n]+`",
    r"!\[[^\]]*\]\([^\)]+\)",
    r"\[[^\]]+\]\([^\)]+\)",
    r"https?://\S+",
    r"<[^>]+>",
]

GLOSSARY = {
    "Sympy": "SymPy",
    "sympy": "SymPy",
    "python": "بايثون",
    "Python": "بايثون",
    "symbolic mathematics": "الرياضيات الرمزية",
    "symbolic variable": "متغير رمزي",
    "symbolic variables": "متغيرات رمزية",
    "expression": "تعبير رياضي",
    "equation": "معادلة",
    "equations": "معادلات",
    "derivative": "مشتقة",
    "integral": "تكامل",
    "expected result": "النتيجة المتوقعة",
}


def protect(text: str):
    store = {}
    idx = 0
    for pat in PATTERNS:
        def repl(match):
            nonlocal idx
            key = f"__TOK_{idx}__"
            store[key] = match.group(0)
            idx += 1
            return key

        text = re.sub(pat, repl, text)
    return text, store


def restore(text: str, store):
    for key, value in store.items():
        text = text.replace(key, value)
    return text


def should_translate(block: str) -> bool:
    return bool(re.search(r"[A-Za-z]", block))


def translate_block(block: str) -> str:
    if not block.strip() or not should_translate(block):
        return block

    if re.fullmatch(r"(\s*__TOK_\d+__\s*)+", block):
        return block

    for _ in range(5):
        try:
            return translator.translate(block)
        except Exception:
            time.sleep(0.8)
    return block


def polish_arabic(text: str) -> str:
    for old, new in GLOSSARY.items():
        text = text.replace(old, new)

    text = text.replace("وظيفة", "دالة")
    text = text.replace("وظائف", "دوال")
    text = text.replace("بيئة python", "بيئة بايثون")
    text = text.replace("Jupyter Notebook", "دفتر Jupyter")
    text = text.replace("jupyter notebook", "دفتر Jupyter")
    text = text.replace("SymPyy", "SymPy")
    return text


nb = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
updated = 0

for cell in nb.get("cells", []):
    if cell.get("cell_type") != "markdown":
        continue

    original = "".join(cell.get("source", [])).strip("\n")
    if not original:
        continue

    if "Arabic Translation / الترجمة العربية" in original:
        continue

    protected, store = protect(original)
    parts = re.split(r"(\n\s*\n)", protected)
    out = []
    for part in parts:
        if re.fullmatch(r"\n\s*\n", part):
            out.append(part)
        else:
            out.append(translate_block(part))

    translated = "".join(out)
    translated = restore(translated, store)
    translated = polish_arabic(translated)

    wrapped = ARABIC_TEMPLATE.format(content=translated.strip())
    combined = original + "\n\n---\n\n" + wrapped + "\n"
    cell["source"] = combined.splitlines(keepends=True)
    updated += 1

NOTEBOOK.write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"updated_markdown_cells={updated}")
