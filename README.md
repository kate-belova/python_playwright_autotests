# Python Playwright Autotests

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Pytest](https://img.shields.io/badge/Pytest-tested-green)
![Playwright](https://img.shields.io/badge/Playwright-UI%20Testing-brightgreen)
![GitHub Actions](https://img.shields.io/badge/CI-GitHub%20Actions-success)

Учебный проект по автоматизации UI-тестирования интернет-магазина с использованием **Python**, **Playwright** и **Pytest**.

## Стек

- Python
- Playwright
- Pytest
- Page Object Model (POM)
- Allure Report
- GitHub Actions

## Что реализовано

- Page Object Model
- Работа с локаторами Playwright
- Автоматические ожидания (Auto Waiting)
- Параметризация тестов
- Фикстуры Pytest
- Проверка позитивных и негативных сценариев
- Запуск тестов на разных языках сайта
- Автоматический запуск тестов через GitHub Actions
- Генерация Allure-отчётов

## Структура проекта

```
pages/          # Page Objects
tests/          # UI-тесты
conftest.py     # фикстуры Pytest
pytest.ini      # настройки Pytest
requirements.txt
```

## Установка

```bash
git clone https://github.com/kate-belova/python_playwright_autotests.git
cd python_playwright_autotests

python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/macOS
source .venv/bin/activate

uv sync
playwright install
```

## Запуск тестов

Все тесты:

```bash
pytest
```

По маркеру:

```bash
pytest -m smoke
pytest -m regression
```

Запуск в браузере Chromium:

```bash
pytest --browser chromium
```

Запуск в Firefox:

```bash
pytest --browser firefox
```

Запуск на другом языке сайта:

```bash
pytest --language=fr
```

## Отчёт Allure

```bash
allure serve allure-results
```

## CI

При каждом push и pull request тесты автоматически запускаются в GitHub Actions.
