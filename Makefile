install:
	uv sync

migrate:
	uv run manage.py migrate

start:
	uv run manage.py runserver 0.0.0.0:8000

lint:
	uv run ruff check hexlet_django_blog

format-app:
	uv run ruff check --fix hexlet_django_blog

test:
	uv run manage.py test

check: test lint
