from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import allure
from utils.checkers import common_assert


class BaseElement:
    def __init__(self, web_element) -> None:
        self.instance = web_element

    def __getattr__(self, item):
        return getattr(self.instance, item)

    @allure.step('Find element by id = {id_}')
    def find_element_by_id(self, id_: str):
        return BaseElement(self.instance.find_element(By.ID, id_))

    @allure.step('Find elements by xpath = "{xpath_expression}"')
    def find_elements_by_xpath(self, xpath_expression: str):
        return [BaseElement(element) for element in self.instance.find_elements(By.XPATH, xpath_expression)]

    @allure.step('Find element by xpath = "{xpath_expression}"')
    def find_element_by_xpath(self, xpath_expression):
        return BaseElement(self.instance.find_element(By.XPATH, xpath_expression))

    # def check(self, element):


class BasePage(BaseElement):
    def __init__(self, driver):
        super().__init__(driver)











