from printo import descript_data_object, not_none


def test_basic_usage():
    assert descript_data_object('MyClassName', (1, 2, 'some text'), {'variable_name': 1, 'second_variable_name': 'kek'}) == "MyClassName(1, 2, 'some text', variable_name=1, second_variable_name='kek')"


def test_basic_filtering():
    assert descript_data_object(
        'MyClassName',
        (1, 2, 'some text'),
        {'variable_name': 1, 'second_variable_name': 'kek'},
        filters={1: lambda x: False if x == 2 else True, 'second_variable_name': lambda x: False},
    ) == "MyClassName(1, 'some text', variable_name=1)"


def test_filtering_of_nones():
    assert descript_data_object(
        'MyClassName',
        (1, None),
        {},
        filters={1: not_none},
    ) == 'MyClassName(1)'


def test_custom_serializator():
    assert descript_data_object(
        'MyClassName',
        (1, 2, 'lol'),
        {'variable_name': 1, 'second_variable_name': 'kek'},
        serializator=lambda x: repr(x * 2),
    ) == "MyClassName(2, 4, 'lollol', variable_name=2, second_variable_name='kekkek')"
