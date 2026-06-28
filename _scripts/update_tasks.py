"""
update_tasks.py — avtomatsko zbere vse odprte naloge ("- [ ] ...") iz vseh
zapiskov v ODS-Vault in jih zapiše v Tasks/Auto-Pregled.md.

Uporaba (iz ukazne vrstice, znotraj _scripts mape):
    python update_tasks.py
"""

import re
from pathlib import Path
from datetime import datetime

VAULT_ROOT = Path(__file__).resolve().parent.parent   # mapa ODS-Vault
OUTPUT_FILE = VAULT_ROOT / "Tasks" / "Auto-Pregled.md"
SKIP_DIRS = {".obsidian", "_scripts"}
SKIP_FILES = {"Tasks.md"}              # rocni agregator nalog - preprecuje podvajanje
TASK_RE = re.compile(r"^[-*]\s\[ \]\s+(.*)")           # ujame "- [ ] besedilo"


def find_open_tasks():
    """Sprehodi se cez vse .md datoteke in vrne {ime_zapiska: [naloge]}."""
    results = {}
    for md_file in VAULT_ROOT.rglob("*.md"):
        if any(part in SKIP_DIRS for part in md_file.parts):
            continue
        if md_file == OUTPUT_FILE:
            continue
        if md_file.name in SKIP_FILES:
            continue
        tasks = []
        for line in md_file.read_text(encoding="utf-8").splitlines():
            match = TASK_RE.match(line.strip())
            if match:
                tasks.append(match.group(1).strip())
        if tasks:
            results[md_file.stem] = tasks
    return results


def build_markdown(results):
    """Sestavi vsebino izhodne datoteke iz najdenih nalog."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = [
        "# Auto-Pregled odprtih nalog",
        "",
        f"_Samodejno generirano {now} - ne urejaj rocno, pozeni `update_tasks.py`._",
        "",
    ]
    if not results:
        lines.append("Ni odprtih nalog. :)")
    else:
        total = sum(len(t) for t in results.values())
        lines.append(f"Skupaj odprtih nalog: **{total}**")
        lines.append("")
        for note_name, tasks in sorted(results.items()):
            lines.append(f"## [[{note_name}]]")
            for t in tasks:
                lines.append(f"- [ ] {t}")
            lines.append("")
    return "\n".join(lines)


def main():
    results = find_open_tasks()
    markdown = build_markdown(results)
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(markdown, encoding="utf-8")
    total = sum(len(t) for t in results.values())
    print(f"Zapisano: {OUTPUT_FILE}")
    print(f"Najdenih odprtih nalog: {total} v {len(results)} zapiskih.")


if __name__ == "__main__":
    main()
