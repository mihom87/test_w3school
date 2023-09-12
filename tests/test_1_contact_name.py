from .pages.sql_editor import SqlEditor
from time import sleep

def test_contact_name(# browser,
                      sql_editor_page,
                      ):
    """Вывести все строки таблицы Customers и убедиться,
       что запись с ContactName равной 'Giovanni Rovelli' имеет Address = 'Via Ludovico il Moro 22'."""
    sql_editor_page.sql_button.click()
    expected_row = sql_editor_page.get_row_by_text('Giovanni Rovelli')
    

    sleep(5)

