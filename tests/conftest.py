import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from .pages.sql_editor import SqlEditor


@pytest.fixture(params=['chrome']
                )
def browser(request):
    if request.param == 'chrome':
        return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    else:
        raise NotImplementedError('Browser not supported')


@pytest.fixture
def sql_editor_page(browser):
    page = SqlEditor(browser)
    page.navigate()
    page.accept_cookies_button.click()
    return page




