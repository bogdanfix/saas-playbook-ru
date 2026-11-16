#!/usr/bin/env python3
"""Извлекает текст из исходного PDF с маркерами страниц.

Использование:
    python scripts/extract_source.py
    python scripts/extract_source.py --pdf path/to/book.pdf --out source/book.txt

Файл результата не коммитится: он нужен только для работы переводчика.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

import pymupdf


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--pdf",
        default="The-SaaS-Playbook-ebook.pdf",
        help="путь к исходному PDF",
    )
    parser.add_argument(
        "--out",
        default="source/saas_raw.txt",
        help="куда сохранить извлечённый текст",
    )
    parser.add_argument(
        "--stats",
        action="store_true",
        help="показать количество слов по страницам",
    )
    args = parser.parse_args()

    pdf_path = Path(args.pdf)
    if not pdf_path.exists():
        raise SystemExit(f"Не найден PDF: {pdf_path}")

    doc = pymupdf.open(pdf_path)
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    total_words = 0
    page_words: list[tuple[int, int]] = []

    with out_path.open("w", encoding="utf-8") as fh:
        for number, page in enumerate(doc, start=1):
            text = page.get_text("text")
            words = len(re.sub(r"\s+", " ", text).strip().split())
            total_words += words
            page_words.append((number, words))
            fh.write(f"\n\n<<<PAGE {number}>>>\n\n")
            fh.write(text)

    print(f"Страниц: {len(doc)}")
    print(f"Слов: {total_words}")
    print(f"Текст сохранён: {out_path}")

    if args.stats:
        print("\nСтраница\tСлов")
        for number, words in page_words:
            print(f"{number}\t{words}")


if __name__ == "__main__":
    main()
