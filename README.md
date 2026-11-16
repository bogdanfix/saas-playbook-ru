# The SaaS Playbook — русский перевод

Приватный перевод книги Роба Уоллинга **The SaaS Playbook** для чтения напарником.

> **Статус:** инфраструктура готова, перевод не начат.  
> **Исходник:** `The-SaaS-Playbook-ebook.pdf` (в репозиторий не коммитится).  
> **Объём:** ≈46 000 слов, 201 страница.  
> **План:** [PLAN.md](PLAN.md) · **Стиль:** [STYLEGUIDE.md](STYLEGUIDE.md) · **Термины:** [GLOSSARY.md](GLOSSARY.md) · **Страницы:** [SOURCE-MAP.md](SOURCE-MAP.md)

---

## Как читать

**Самый простой способ:** скачать EPUB из [Releases](../../releases) и открыть на телефоне, в Kindle или Apple Books.

**Онлайн-версия:** после сборки сайт можно открыть локально командой `mkdocs serve` или захостить в закрытом доступе (Cloudflare Pages + Access). GitHub Pages для этой задачи не используем: сайт из приватного репозитория всё равно будет публичным.

**Исходники:** каждая глава — отдельный Markdown-файл в [`chapters/`](chapters/). Читать можно прямо на GitHub, но навигация там хуже, чем в EPUB или собранном сайте.

---

## Прогресс

| № | Глава | Слов | Статус | Файл |
|---|---|---:|---|---|
| 00 | Титул и выходные данные | 1 209 | ⬜ не начато | [00-frontmatter.md](chapters/00-frontmatter.md) |
| 01 | Предисловие | 1 108 | ⬜ не начато | [01-foreword.md](chapters/01-foreword.md) |
| 02 | Введение | 2 083 | ⬜ не начато | [02-introduction.md](chapters/02-introduction.md) |
| 03 | Часть I. Плейбук | 3 050 | ⬜ не начато | [03-part-i-playbook.md](chapters/03-part-i-playbook.md) |
| 04 | Рынок | 5 984 | ⬜ не начато | [04-market.md](chapters/04-market.md) |
| 05 | Ценообразование | 5 164 | ⬜ не начато | [05-pricing.md](chapters/05-pricing.md) |
| 06 | Маркетинг | 7 316 | ⬜ не начато | [06-marketing.md](chapters/06-marketing.md) |
| 07 | Команда | 7 009 | ⬜ не начато | [07-team.md](chapters/07-team.md) |
| 08 | Метрики | 5 329 | ⬜ не начато | [08-metrics.md](chapters/08-metrics.md) |
| 09 | Мышление | 6 596 | ⬜ не начато | [09-mindset.md](chapters/09-mindset.md) |
| 10 | Послесловие | 127 | ⬜ не начато | [10-afterword.md](chapters/10-afterword.md) |
| 11 | Благодарности | 150 | ⬜ не начато | [11-acknowledgments.md](chapters/11-acknowledgments.md) |
| 12 | Приложение A: Ресурсы | 693 | ⬜ не начато | [12-appendix.md](chapters/12-appendix.md) |

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

## Публикация в приватный GitHub

Репозиторий уже подготовлен локально. Чтобы создать приватный репозиторий и отправить туда файлы:

```bash
git init
git add .
git commit -m "chore: scaffold translation project"
gh repo create saas-playbook-ru --private --source=. --remote=origin --push
```

После этого:

1. Добавь напарника в **Settings → Collaborators** с доступом **Read** (если он только читает) или **Write** (если будет ревьюить).
2. Включи защиту `main`: **Settings → Branches → Add branch protection rule**, require pull request before merging.
3. **Не включай GitHub Pages.** Сайт из приватного репозитория всё равно будет публичным (на Free приватный репозиторий вообще не может публиковать Pages؛ приватные Pages доступны только в GitHub Enterprise Cloud).
4. Для чтения используй EPUB из **Releases** или локальный `mkdocs serve`.
5. Если нужна ссылка для напарника — подними сайт на Cloudflare Pages и закрой его Cloudflare Access (вход по e-mail из списка).

---

## Важно об авторских правах

Оригинал защищён авторским правом. Перевод — производное произведение. Этот репозиторий предназначен для **личного чтения узким кругом**; не публикуй его в открытом доступе, не продавай и не распространяй перевод без разрешения правообладателя. Подробнее — [COPYRIGHT.md](COPYRIGHT.md).
