from selenium.webdriver.common.by import By


def test_entry_amount_by_city(sql_editor_page):
    """Вывести только те строки таблицы Customers, где city='London'.
       Проверить, что в таблице ровно 6 записей
    """

    sql_editor_page.type_sql_statement("SELECT * FROM Customers WHERE city='London';")
    sql_editor_page.click_run_sql_button()

    assert sql_editor_page.results_text('Number of Records: 6'), f'Wrong amount of founded records, ' \
                                                                 f'actual: {sql_editor_page.results_text("Number of Records: 6")}, ' \
                                                                 f'expected: "Number of Records: 6"'
    assert len(sql_editor_page.find_elements_by_xpath(
        "//*[@id='divResultSQL']//table/tbody/tr")) == 7, f'Wrong amount of records in result table, ' \
                                                          f'actual {len(sql_editor_page.table_of_results.find_elements_by_xpath("//tbody/tr")) - 1}, ' \
                                                          f'expected 6'
