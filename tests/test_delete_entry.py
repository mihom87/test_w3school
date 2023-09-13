import pytest


@pytest.fixture
def deleted_entry(sql_editor_page) -> None:
    sql_editor_page.type_sql_statement("DELETE FROM Customers WHERE CustomerID=1;")
    sql_editor_page.click_run_sql_button()
    sql_editor_page.results_text(
        'You have made changes to the database. Rows affected: 1')


def test_delete_entry(deleted_entry, sql_editor_page):
    sql_editor_page.type_sql_statement("SELECT * FROM Customers WHERE CustomerID=1;")
    sql_editor_page.click_run_sql_button()
    assert sql_editor_page.results_text('No result.') == 'No result.', f'Wrong result text, ' \
                                                                       f'actual "{sql_editor_page.results_text}"' \
                                                                       f'expected "No result."'
    expected_table = sql_editor_page.find_elements_by_xpath("//*[@id='divResultSQL']//table")
    assert not expected_table, 'Unexpected entries has been founded'
