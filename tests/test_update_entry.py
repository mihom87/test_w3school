import pytest


@pytest.fixture()
def updated_entry(sql_editor_page):
    sql_editor_page.type_sql_statement("UPDATE Customers SET "
                                       "ContactName = 'hiohhlh', "
                                       "ContactName='Xfxgxgfgx', "
                                       "Address='Tokio', "
                                       "City= 'Frankfurt', "
                                       "PostalCode='23232', "
                                       "Country='Japan' "
                                       "WHERE CustomerID = 1  RETURNING *;")
    sql_editor_page.click_run_sql_button()
    sql_editor_page.results_text(
        'Number of Records: 1')
    return [element.text for element in
            sql_editor_page.find_elements_by_xpath("//*[@id='divResultSQL']//table/tbody/tr[2]/td")]


def test_update_entry(sql_editor_page, updated_entry):
    """Обновить все поля (кроме CustomerID) в любой записи таблицы Customersи проверить,
    что изменения записались в базу."""
    sql_editor_page.type_sql_statement(f"SELECT * FROM Customers WHERE CustomerId = 1;")
    sql_editor_page.click_run_sql_button()

    assert sql_editor_page.results_text('Number of Records: 1'), f'Wrong amount of founded records, ' \
                                                                 f'actual: {sql_editor_page.results_text("Number of Records: 6")}, ' \
                                                                 f'expected: "Number of Records: 1"'
    actual_entry = sql_editor_page.find_elements_by_xpath("//*[@id='divResultSQL']//table/tbody/tr[2]/td")

    for actual_field_value, expected_field_value, column_name in zip(actual_entry,
                                                                     updated_entry,
                                                                     sql_editor_page.result_table_column_names):
        assert actual_field_value.text == expected_field_value, f'Wrong value for {column_name} column, ' \
                                                                f'actual: {actual_field_value.text}, ' \
                                                                f'expected: {expected_field_value}'
