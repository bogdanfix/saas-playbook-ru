#!/usr/bin/env python3
"""Проверяет главы перевода перед PR.

Проверки:
- обязательные поля front matter;
- допустимые статусы;
- отсутствие TODO/XXX/[[? в готовых главах;
- запрещённые варианты терминов;
- двойные пробелы (кроме таблиц и концевых пробелов);
- наличие хотя бы одного раздела H2;
- базовая статистика по словам.

Скрипт не заменяет двуязычную редактуру. Он ловит только механические ошибки.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

CHAPTERS = Path("chapters")
REQUIRED_FIELDS = ("title", "original_title", "source_pages", "status")
ALLOWED_STATUSES = {"todo", "draft", "review", "done"}
SHORT_FORM = {"01-foreword.md", "10-afterword.md", "11-acknowledgments.md"}
BANNED_TERMS = {
    "СААС": "SaaS",
    "Саас": "SaaS",
    "кофаундер": "соучредитель",
    "Кофаундер": "соучредитель",
    "на ежедневной основе": "каждый день",
    "принять решение о том, чтобы": "решить",
    "осуществлять свою деятельность": "работать",
}

FRONT_MATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
WORD_RE = re.compile(r"[А-Яа-яЁёA-Za-z0-9][А-Яа-яЁёA-Za-z0-9'’\-]*")


def parse_front_matter(text: str) -> tuple[dict[str, str], str]:
    match = FRONT_MATTER_RE.match(text)
    if not match:
        return {}, text
    data: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data, text[match.end():]


def strip_markup(body: str) -> str:
    body = COMMENT_RE.sub("", body)
    body = FENCE_RE.sub("", body)
    return body


def check_file(path: Path) -> tuple[list[str], list[str], int]:
    errors: list[str] = []
    warnings: list[str] = []
    text = path.read_text(encoding="utf-8")
    meta, body = parse_front_matter(text)
    clean = strip_markup(body)
    words = len(WORD_RE.findall(clean))

    for field in REQUIRED_FIELDS:
        if not meta.get(field):
            errors.append(f"нет поля front matter: {field}")

    status = meta.get("status", "")
    if status and status not in ALLOWED_STATUSES:
        errors.append(f"недопустимый status: {status}")

    for term, replacement in BANNED_TERMS.items():
        if term in clean:
            errors.append(f"запрещённый вариант «{term}» → «{replacement}»")

    if status == "done":
        for marker in ("TODO", "XXX", "[[?"):
            if marker in body:
                errors.append(f"в готовой главе остался маркер {marker}")

    if path.name not in SHORT_FORM and not re.search(r"^##\s+\S", clean, re.MULTILINE):
        warnings.append("нет ни одного раздела H2")

    for line in clean.splitlines():
        if line.startswith("|") or "http" in line:
            continue
        if re.search(r"\S  +\S", line):
            errors.append(f"двойной пробел: {line.strip()[:70]}")
            break

    if words < 50 and status in {"draft", "review", "done"}:
        warnings.append(f"мало текста ({words} слов) для статуса {status}")

    return errors, warnings, words


def main() -> int:
    if not CHAPTERS.is_dir():
        print(f"Нет каталога {CHAPTERS}", file=sys.stderr)
        return 1

    files = [p for p in sorted(CHAPTERS.glob("*.md")) if p.name != "index.md"]
    if not files:
        print(f"В {CHAPTERS} нет Markdown-файлов", file=sys.stderr)
        return 1

    total_errors = 0
    total_warnings = 0
    total_words = 0

    print(f"{'Файл':42s} {'Статус':8s} {'Слов':>6s}  Проверки")
    print("-" * 78)

    for path in files:
        errors, warnings, words = check_file(path)
        total_errors += len(errors)
        total_warnings += len(warnings)
        total_words += words
        status = ""
        meta, _ = parse_front_matter(path.read_text(encoding="utf-8"))
        status = meta.get("status", "?")
        marks = []
        if errors:
            marks.append(f"{len(errors)} ошиб.")
        if warnings:
            marks.append(f"{len(warnings)} предупр.")
        print(f"{path.name:42s} {status:8s} {words:6d}  {'; '.join(marks) or 'ok'}")
        for error in errors:
            print(f"  ✗ {error}")
        for warning in warnings:
            print(f"  ! {warning}")

    print("-" * 78)
    print(f"Всего слов: {total_words}")
    print(f"Ошибок: {total_errors}; предупреждений: {total_warnings}")

    return 1 if total_errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
