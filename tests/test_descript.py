from printo import descript_data_object


def test_empty_object():
    assert descript_data_object('ClassName', (), {}) == 'ClassName()'
    assert descript_data_object('ClassName', (), {}, serializator=lambda x: 'kek') == 'ClassName()'


def test_only_args():
    assert descript_data_object('ClassName', (1, 2, 3), {}) == 'ClassName(1, 2, 3)'
    assert descript_data_object('ClassName', (1, 2), {}) == 'ClassName(1, 2)'
    assert descript_data_object('ClassName', (1,), {}) == 'ClassName(1)'

    assert descript_data_object('ClassName', ('lol', 'kek'), {}) == 'ClassName("lol", "kek")'
    assert descript_data_object('ClassName', ('lol',), {}) == 'ClassName("lol")'

    assert descript_data_object('ClassName', ('lol', 1, 2, 3), {}) == 'ClassName("lol", 1, 2, 3)'
    assert descript_data_object('ClassName', ('lol', 1, 2, 3, 'kek'), {}) == 'ClassName("lol", 1, 2, 3, "kek")'
    assert descript_data_object('ClassName', ('lol', 1, 2, 3, 'kek', None), {}) == 'ClassName("lol", 1, 2, 3, "kek", None)'


def test_only_kwargs():
    assert descript_data_object('ClassName', (), {'lol': 1, 'kek': 2}) == 'ClassName(lol=1, kek=2)'

    assert descript_data_object('ClassName', (), {'lol': 'insert text', 'kek': 'insert the second text'}) == 'ClassName(lol="insert text", kek="insert the second text")'

    assert descript_data_object('ClassName', (), {'number_1': 1, 'number_2': 2, 'lol': 'insert text', 'kek': 'insert the second text'}) == 'ClassName(number_1=1, number_2=2, lol="insert text", kek="insert the second text")'
    assert descript_data_object('ClassName', (), {'number_1': 1, 'number_2': 2, 'lol': 'insert text', 'kek': 'insert the second text', 'number_3': 3}) == 'ClassName(number_1=1, number_2=2, lol="insert text", kek="insert the second text", number_3=3)'


def test_args_and_kwargs():
    assert descript_data_object('ClassName', (1, 2, 3), {'lol': 1, 'kek': 2}) == 'ClassName(1, 2, 3, lol=1, kek=2)'
    assert descript_data_object('ClassName', (1, 2, 3), {'lol': 'insert text', 'kek': 'insert the second text'}) == 'ClassName(1, 2, 3, lol="insert text", kek="insert the second text")'
    assert descript_data_object('ClassName', (1, 2, 3), {'number_1': 1, 'number_2': 2, 'lol': 'insert text', 'kek': 'insert the second text'}) == 'ClassName(1, 2, 3, number_1=1, number_2=2, lol="insert text", kek="insert the second text")'
    assert descript_data_object('ClassName', (1, 2, 3), {'number_1': 1, 'number_2': 2, 'lol': 'insert text', 'kek': 'insert the second text', 'number_3': 3}) == 'ClassName(1, 2, 3, number_1=1, number_2=2, lol="insert text", kek="insert the second text", number_3=3)'

    assert descript_data_object('ClassName', ('lol', 'kek'), {'lol': 1, 'kek': 2}) == 'ClassName("lol", "kek", lol=1, kek=2)'
    assert descript_data_object('ClassName', ('lol', 'kek'), {'lol': 'insert text', 'kek': 'insert the second text'}) == 'ClassName("lol", "kek", lol="insert text", kek="insert the second text")'
    assert descript_data_object('ClassName', ('lol', 'kek'), {'number_1': 1, 'number_2': 2, 'lol': 'insert text', 'kek': 'insert the second text'}) == 'ClassName("lol", "kek", number_1=1, number_2=2, lol="insert text", kek="insert the second text")'
    assert descript_data_object('ClassName', ('lol', 'kek'), {'number_1': 1, 'number_2': 2, 'lol': 'insert text', 'kek': 'insert the second text', 'number_3': 3}) == 'ClassName("lol", "kek", number_1=1, number_2=2, lol="insert text", kek="insert the second text", number_3=3)'

    assert descript_data_object('ClassName', ('lol', 1, 2, 3), {'lol': 1, 'kek': 2}) == 'ClassName("lol", 1, 2, 3, lol=1, kek=2)'
    assert descript_data_object('ClassName', ('lol', 1, 2, 3), {'lol': 'insert text', 'kek': 'insert the second text'}) == 'ClassName("lol", 1, 2, 3, lol="insert text", kek="insert the second text")'
    assert descript_data_object('ClassName', ('lol', 1, 2, 3), {'number_1': 1, 'number_2': 2, 'lol': 'insert text', 'kek': 'insert the second text'}) == 'ClassName("lol", 1, 2, 3, number_1=1, number_2=2, lol="insert text", kek="insert the second text")'
    assert descript_data_object('ClassName', ('lol', 1, 2, 3), {'number_1': 1, 'number_2': 2, 'lol': 'insert text', 'kek': 'insert the second text', 'number_3': 3}) == 'ClassName("lol", 1, 2, 3, number_1=1, number_2=2, lol="insert text", kek="insert the second text", number_3=3)'

    assert descript_data_object('ClassName', ('lol', 1, 2, 3, 'kek'), {'lol': 1, 'kek': 2}) == 'ClassName("lol", 1, 2, 3, "kek", lol=1, kek=2)'
    assert descript_data_object('ClassName', ('lol', 1, 2, 3, 'kek'), {'lol': 'insert text', 'kek': 'insert the second text'}) == 'ClassName("lol", 1, 2, 3, "kek", lol="insert text", kek="insert the second text")'
    assert descript_data_object('ClassName', ('lol', 1, 2, 3, 'kek'), {'number_1': 1, 'number_2': 2, 'lol': 'insert text', 'kek': 'insert the second text'}) == 'ClassName("lol", 1, 2, 3, "kek", number_1=1, number_2=2, lol="insert text", kek="insert the second text")'
    assert descript_data_object('ClassName', ('lol', 1, 2, 3, 'kek'), {'number_1': 1, 'number_2': 2, 'lol': 'insert text', 'kek': 'insert the second text', 'number_3': 3}) == 'ClassName("lol", 1, 2, 3, "kek", number_1=1, number_2=2, lol="insert text", kek="insert the second text", number_3=3)'

    assert descript_data_object('ClassName', ('lol', 1, 2, 3, 'kek', None), {'lol': 1, 'kek': 2}) == 'ClassName("lol", 1, 2, 3, "kek", None, lol=1, kek=2)'
    assert descript_data_object('ClassName', ('lol', 1, 2, 3, 'kek', None), {'lol': 'insert text', 'kek': 'insert the second text'}) == 'ClassName("lol", 1, 2, 3, "kek", None, lol="insert text", kek="insert the second text")'
    assert descript_data_object('ClassName', ('lol', 1, 2, 3, 'kek', None), {'number_1': 1, 'number_2': 2, 'lol': 'insert text', 'kek': 'insert the second text'}) == 'ClassName("lol", 1, 2, 3, "kek", None, number_1=1, number_2=2, lol="insert text", kek="insert the second text")'
    assert descript_data_object('ClassName', ('lol', 1, 2, 3, 'kek', None), {'number_1': 1, 'number_2': 2, 'lol': 'insert text', 'kek': 'insert the second text', 'number_3': 3}) == 'ClassName("lol", 1, 2, 3, "kek", None, number_1=1, number_2=2, lol="insert text", kek="insert the second text", number_3=3)'


def test_set_serializator_for_args():
    assert descript_data_object('ClassName', (1, 2, 3), {}, serializator=lambda x: f'{x}{x}') == 'ClassName(11, 22, 33)'
    assert descript_data_object('ClassName', (1, 2), {}, serializator=lambda x: f'{x}{x}') == 'ClassName(11, 22)'
    assert descript_data_object('ClassName', (1,), {}, serializator=lambda x: f'{x}{x}') == 'ClassName(11)'

    assert descript_data_object('ClassName', ('lol', 'kek'), {}, serializator=lambda x: f'{x}{x}') == 'ClassName("lollol", "kekkek")'
    assert descript_data_object('ClassName', ('lol',), {}, serializator=lambda x: f'{x}{x}') == 'ClassName("lollol")'

    assert descript_data_object('ClassName', ('lol', 1, 2, 3), {}, serializator=lambda x: f'{x}{x}') == 'ClassName("lollol", 11, 22, 33)'
    assert descript_data_object('ClassName', ('lol', 1, 2, 3, 'kek'), {}, serializator=lambda x: f'{x}{x}') == 'ClassName("lollol", 11, 22, 33, "kekkek")'
    assert descript_data_object('ClassName', ('lol', 1, 2, 3, 'kek', None), {}, serializator=lambda x: f'{x}{x}') == 'ClassName("lollol", 11, 22, 33, "kekkek", NoneNone)'


def test_set_serializator_for_kwargs():
    assert descript_data_object('ClassName', (), {'lol': 1, 'kek': 2}, serializator=lambda x: f'{x}{x}') == 'ClassName(lol=11, kek=22)'

    assert descript_data_object('ClassName', (), {'lol': 'insert text', 'kek': 'insert the second text'}, serializator=lambda x: f'{x}{x}') == 'ClassName(lol="insert textinsert text", kek="insert the second textinsert the second text")'

    assert descript_data_object('ClassName', (), {'number_1': 1, 'number_2': 2, 'lol': 'insert text', 'kek': 'insert the second text'}, serializator=lambda x: f'{x}{x}') == 'ClassName(number_1=11, number_2=22, lol="insert textinsert text", kek="insert the second textinsert the second text")'
    assert descript_data_object('ClassName', (), {'number_1': 1, 'number_2': 2, 'lol': 'insert text', 'kek': 'insert the second text', 'number_3': 3}, serializator=lambda x: f'{x}{x}') == 'ClassName(number_1=11, number_2=22, lol="insert textinsert text", kek="insert the second textinsert the second text", number_3=33)'
