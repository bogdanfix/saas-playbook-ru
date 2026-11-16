#!/usr/bin/env python3
"""Показывает прогресс по главам.

Использование:
    python scripts/progress.py
"""

from __future__ import annotations

import re
from pathlib import Path

CHAPTERS = Path("chapters")
FRONT_MATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
WORD_RE = re.compile(r"[А-Яа-яЁёA-Za-z0-9][А-Яа-яЁёA-Za-z0-9'’\-]*")

ICONS = {
    "todo": "⬜",
    "draft": "🟡",
    "review": "🔵",
    "done": "✅",
}
LABELS = {
    "todo": "не начато",
    "draft": "черновик",
    "review": "на ревью",
    "done": "готово",
}


def parse_front_matter(text: str) -> dict[str, str]:
    match = FRONT_MATTER_RE.match(text)
    if not match:
        return {}
    data: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def word_count(body: str) -> int:
    body = COMMENT_RE.sub("", body)
    body = FENCE_RE.sub("", body)
    return len(WORD_RE.findall(body))


def main() -> None:
    files = [p for p in sorted(CHAPTERS.glob("*.md")) if p.name != "index.md"]
    total = 0
    done = 0

    print(f"{'Файл':42s} {'Статус':12s} {'Слов':>6s}")
    print("-" * 66)

    for path in files:
        text = path.read_text(encoding="utf-8")
        meta = parse_front_matter(text)
        body = FRONT_MATTER_RE.sub("", text, count=1)
        words = word_count(body)
        status = meta.get("status", "todo")
        total += words
        if status == "done":
            done += words
        print(f"{path.name:42s} {ICONS.get(status, '?')} {LABELS.get(status, status):10s} {words:6d}")

    print("-" * 66)
    print(f"Всего слов: {total}")
    print(f"Готово: {done} ({done / total * 100:.0f}%)" if total else "Готово: 0")


if __name__ == "__main__":
    main()
