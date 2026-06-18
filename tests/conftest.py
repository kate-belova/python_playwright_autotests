from pathlib import Path

import pytest
from playwright.sync_api import sync_playwright, ViewportSize

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.product_page import ProductPage


def pytest_configure(config):
    current_file = Path(__file__).resolve()
    allure_dir = current_file.parents[1] / "allure-results"
    allure_dir.mkdir(exist_ok=True)
    config.option.allure_report_dir = str(allure_dir)


def pytest_addoption(parser):
    # fmt: off
    parser.addoption("--language", action="store", default="en-gb",
        help="Choose language: ",
        choices=("ar", "ca", "cs", "da", "de", "en-gb", "el",
                 "es", "fi", "fr", "it", "ko", "nl", "pl",
                 "pt", "pt-br", "ro", "ru", "sk", "uk", "zh-hans")

    )
    # fmt: on


@pytest.fixture()
def page(request):
    print("\nStart browser for test")

    language = request.config.getoption("--language")

    playwright = sync_playwright().start()
    browser = playwright.chromium.launch()
    context = browser.new_context(
        viewport=ViewportSize(width=1920, height=1080), locale=language
    )
    page = context.new_page()

    yield page

    print("\nQuit browser")

    context.close()
    browser.close()
    playwright.stop()


@pytest.fixture()
def main_page(page):
    return MainPage(page)


@pytest.fixture()
def login_page(page):
    return LoginPage(page)


@pytest.fixture()
def product_page(page):
    return ProductPage(page)


@pytest.fixture()
def basket_page(page):
    return BasketPage(page)


@pytest.fixture()
def authorized_user(page, login_page):
    login_page.open_login_page()
    login_page.register_new_user()
    login_page.should_be_authorized_user()
