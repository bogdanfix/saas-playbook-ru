# The SaaS Playbook — русский перевод

Неофициальный перевод книги Роба Уоллинга **The SaaS Playbook** для напарника и небольшого круга читателей.

> **Версия:** 1.0 · 16 ноября 2026
>
> **Статус:** финальная версия опубликована; весь основной текст переведён и вычитан.
>
> **Исходник:** `The-SaaS-Playbook-ebook.pdf` (в репозиторий не коммитится).
>
> **Объём:** ≈44 600 слов основного текста, 201 страница.
>
> **План:** [PLAN.md](PLAN.md) · **Стиль:** [STYLEGUIDE.md](STYLEGUIDE.md) · **Термины:** [GLOSSARY.md](GLOSSARY.md) · **Страницы:** [SOURCE-MAP.md](SOURCE-MAP.md)

---

## Как читать

**Самый простой способ:** открыть [GitHub Pages](https://bogdanfix.github.io/saas-playbook-ru/). EPUB можно собрать позже по инструкции ниже — для чтения на телефоне или в Kindle.

**Локально:** `mkdocs serve` — если хочется посмотреть до публикации.

**Исходники:** каждая глава — отдельный Markdown-файл в [`chapters/`](chapters/). Читать можно прямо на GitHub, но навигация там хуже, чем в EPUB или собранном сайте.

---

## Прогресс

| № | Глава | Слов | Статус | Файл |
|---|---|---:|---|---|
| 01 | Предисловие | 1 108 | ✅ готово | [01-foreword.md](chapters/01-foreword.md) |
| 02 | Введение | 2 083 | ✅ готово | [02-introduction.md](chapters/02-introduction.md) |
| 03 | Плейбук создания SaaS-компании | 3 050 | ✅ готово | [03-playbook.md](chapters/03-playbook.md) |
| 04 | Рынок | 5 984 | ✅ готово | [04-market.md](chapters/04-market.md) |
| 05 | Ценообразование | 5 164 | ✅ готово | [05-pricing.md](chapters/05-pricing.md) |
| 06 | Маркетинг | 7 316 | ✅ готово | [06-marketing.md](chapters/06-marketing.md) |
| 07 | Команда | 7 009 | ✅ готово | [07-team.md](chapters/07-team.md) |
| 08 | Метрики | 5 329 | ✅ готово | [08-metrics.md](chapters/08-metrics.md) |
| 09 | Мышление | 6 596 | ✅ готово | [09-mindset.md](chapters/09-mindset.md) |
| 10 | Послесловие | 127 | ✅ готово | [10-afterword.md](chapters/10-afterword.md) |
| 11 | Благодарности | 150 | ✅ готово | [11-acknowledgments.md](chapters/11-acknowledgments.md) |
| 12 | Приложение A: Ресурсы | 693 | ✅ готово | [12-appendix.md](chapters/12-appendix.md) |

Титул, отзывы, рекламные материалы и раздел «Other Works» в перевод не входят.

Статусы: ⬜ не начато · 🟡 черновик · 🔵 на ревью · ✅ готово.

Посмотреть прогресс:

```bash
python scripts/progress.py
```

---

## Быстрый старт

```bash
# 1. Виртуальное окружение и зависимости
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 2. Локальный сайт с горячей перезагрузкой
mkdocs serve

# 3. Сборка статического сайта
mkdocs build
```

Сайт откроется на <http://127.0.0.1:8000>.

### EPUB

Нужен Pandoc:

```bash
brew install pandoc
mkdir -p dist
pandoc chapters/index.md chapters/0*.md chapters/1*.md \
  --metadata title="The SaaS Playbook. Русский перевод" \
  --metadata lang=ru-RU \
  --toc --toc-depth=2 \
  -o dist/saas-playbook-ru.epub
```

Если Pandoc не хочется ставить, для чтения достаточно HTML-сайта или Markdown на GitHub.

---

## Структура

```text
chapters/        Markdown по главам — единственный источник правды
scripts/         извлечение текста, проверки, прогресс
.github/         CI и шаблон pull request
PLAN.md          план перевода, график, риски
STYLEGUIDE.md    стиль, орфография, оформление
GLOSSARY.md      терминологическая база
SOURCE-MAP.md    соответствие печатных и PDF-страниц
NOTES.md         спорные места и решения по исходнику
COPYRIGHT.md     рамки использования
```

---

## Как работать над главой

1. Создать ветку: `ch/04-market`.
2. Перевести главу, обновляя `GLOSSARY.md`.
3. Поставить в метаданных `status: review`.
4. Открыть pull request по шаблону.
5. Пройти двуязычную редактуру и корректуру.
6. Поставить `status: done`, смержить в `main`.
7. Собрать EPUB и приложить к релизу.

Подробности — в [PLAN.md](PLAN.md), разделы 5–7.

---

## Публикация на GitHub Pages

- Репозиторий: <https://github.com/bogdanfix/saas-playbook-ru>
- Сайт: <https://bogdanfix.github.io/saas-playbook-ru/>
- Сборка: GitHub Actions, workflow `.github/workflows/pages.yml`.
- Источник в настройках Pages: **GitHub Actions**.

Любой push в `main` пересобирает сайт автоматически. Если позже понадобится закрытый доступ, можно переключить репозиторий на private, а для чтения использовать EPUB или Cloudflare Pages + Access.

---

## Важно об авторских правах

Оригинал защищён авторским правом. Перевод — производное произведение и не является официальным изданием. Права на оригинал принадлежат Rob Walling. Перевод нельзя продавать или выдавать за официальный; при запросе правообладателя материалы будут сняты. Подробнее — [COPYRIGHT.md](COPYRIGHT.md).
