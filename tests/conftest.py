import pytest
import importlib
from selenium import webdriver
from .pages.sql_editor import SqlEditor

CLASS_NAME = "Service"


@pytest.fixture(params=['chrome',
                        # 'firefox',
                        ]
                )
def browser(request):
    # service_class = getattr(importlib.import_module(f'selenium.webdriver.{request.param}.service'),
    #                         CLASS_NAME)
    # if request.param == 'chrome':
    #     driver_manager = getattr(importlib.import_module('webdriver_manager.firefox'), 'GeckoDriverManager')
    #     driver = webdriver.Chrome(service=service_class(driver_manager().install()))
    # elif request.param == 'firefox':
    #     driver_manager = getattr(importlib.import_module('webdriver_manager.chrome'), 'ChromeDriverManager')
    #     driver = webdriver.Firefox(service=service_class(driver_manager().install()))
    # else:
    #     raise Exception(f'Wrong browser name: {request.param}.')
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service as ChromeService
    from webdriver_manager.chrome import ChromeDriverManager

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    return driver


@pytest.fixture
def sql_editor_page(browser):
    page = SqlEditor(browser)
    page.navigate()
    page.accept_cookies_button.click()
    return page




