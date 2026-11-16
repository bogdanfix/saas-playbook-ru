.PHONY: help install serve build check epub clean

help:
	@echo "install  — установить зависимости"
	@echo "serve    — локальный сайт с горячей перезагрузкой"
	@echo "build    — собрать сайт"
	@echo "check    — проверить главы"
	@echo "epub     — собрать сайт и EPUB"
	@echo "clean    — удалить сборку"

install:
	python3 -m venv .venv
	.venv/bin/pip install -r requirements.txt

serve:
	.venv/bin/mkdocs serve

build:
	.venv/bin/mkdocs build --strict

check:
	.venv/bin/python scripts/check_translation.py

epub:
	bash scripts/build.sh

clean:
	rm -rf site dist
