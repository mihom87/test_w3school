def test_contact_name(sql_editor_page):
    """Вывести все строки таблицы Customers и убедиться,
       что запись с ContactName равной 'Giovanni Rovelli' имеет Address = 'Via Ludovico il Moro 22'."""
    sql_editor_page.click_run_sql_button()
    actual_row = sql_editor_page.get_row_by_value(column_name='ContactName', column_value='Giovanni Rovelli')
    assert 'Address' in sql_editor_page.result_table_column_names, 'Column with name "Address" not found'
    address_index = sql_editor_page.result_table_column_names.index('Address')
    assert actual_row[address_index].text == 'Via Ludovico il Moro 22', 'Field with ContactName="Giovanni Rovelli" ' \
                                                                        f'has wrong "Address" field: actual {actual_row[address_index].text}, ' \
                                                                        'expectet: "Via Ludovico il Moro 22"'

