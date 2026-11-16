#!/usr/bin/env bash
# Собирает HTML-сайт и, если установлен Pandoc, EPUB.
set -euo pipefail

cd "$(dirname "$0")/.."

python scripts/check_translation.py
mkdocs build --strict

if command -v pandoc >/dev/null 2>&1; then
  mkdir -p dist
  pandoc chapters/index.md chapters/0*.md chapters/1*.md \
    --from markdown+footnotes \
    --metadata title="The SaaS Playbook. Русский перевод" \
    --metadata lang=ru-RU \
    --toc --toc-depth=2 \
    -o dist/saas-playbook-ru.epub
  echo "EPUB: dist/saas-playbook-ru.epub"
else
  echo "Pandoc не найден — EPUB пропущен. Установи: brew install pandoc"
fi

echo "Готово."
