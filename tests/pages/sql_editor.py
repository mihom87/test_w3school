from ext_selenium.common import BasePage
import allure
from utils.checkers import common_assert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from ext_selenium.common import BaseElement


class SqlEditor(BasePage):
    url = 'https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all'

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step(f'Navigate to page {url}')
    def navigate(self) -> None:
        self.instance.get(self.url)

    @property
    def accept_cookies_button(self) -> BaseElement:
        element = WebDriverWait(self.instance, 10).until(
            EC.visibility_of_element_located((By.ID, 'accept-choices'))
        )
        return BaseElement(element)

    @property
    def sql_button(self) -> BaseElement:
        element = WebDriverWait(self.instance, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Run SQL')]")))
        return BaseElement(element)

    @property
    def table_of_results(self) -> BaseElement:
        element = WebDriverWait(self.instance, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='divResultSQL']//table")))
        return BaseElement(element)

    @allure.step('Click "Run SQL" button')
    def click_run_sql_button(self) -> None:
        self.sql_button.click()

    @property
    def result_table_column_names(self) -> list:
        WebDriverWait(self.table_of_results, # self.instance,
                      10).until(
            EC.visibility_of_element_located((By.XPATH, "//tbody/tr/th")))
        column_names = self.table_of_results.find_elements_by_xpath('//tbody/tr/th')
        return [column.text for column in column_names]

    @allure.step('Get row from result by text "{text}"')
    def get_row_by_text(self, text: str) -> list:
        WebDriverWait(self.table_of_results, 10).until(
            EC.visibility_of_element_located((By.XPATH, f"//tbody/tr/td[text() = '{text}']")))

        row = self.table_of_results.find_elements_by_xpath(f"//tbody/tr/td[text() = '{text}']/../td")
        return [BaseElement(field) for field in row]


