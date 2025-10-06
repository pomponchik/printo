from typing import Any

from printo import descript_data_object


def test_empty_object():
    assert descript_data_object('ClassName', (), {}) == 'ClassName()'
    assert descript_data_object('ClassName', (), {}, serializator=lambda x: 'kek') == 'ClassName()'


def test_only_args():
    assert descript_data_object('ClassName', (1, 2, 3), {}) == 'ClassName(1, 2, 3)'
    assert descript_data_object('ClassName', (1, 2), {}) == 'ClassName(1, 2)'
    assert descript_data_object('ClassName', (1,), {}) == 'ClassName(1)'

    assert descript_data_object('ClassName', ('lol', 'kek'), {}) == "ClassName('lol', 'kek')"
    assert descript_data_object('ClassName', ('lol',), {}) == "ClassName('lol')"

    assert descript_data_object('ClassName', ('lol', 1, 2, 3), {}) == "ClassName('lol', 1, 2, 3)"
    assert descript_data_object('ClassName', ('lol', 1, 2, 3, 'kek'), {}) == "ClassName('lol', 1, 2, 3, 'kek')"
    assert descript_data_object('ClassName', ('lol', 1, 2, 3, 'kek', None), {}) == "ClassName('lol', 1, 2, 3, 'kek', None)"


def test_only_kwargs():
    assert descript_data_object('ClassName', (), {'lol': 1, 'kek': 2}) == 'ClassName(lol=1, kek=2)'

    assert descript_data_object('ClassName', (), {'lol': 'insert text', 'kek': 'insert the second text'}) == "ClassName(lol='insert text', kek='insert the second text')"

    assert descript_data_object('ClassName', (), {'number_1': 1, 'number_2': 2, 'lol': 'insert text', 'kek': 'insert the second text'}) == "ClassName(number_1=1, number_2=2, lol='insert text', kek='insert the second text')"
    assert descript_data_object('ClassName', (), {'number_1': 1, 'number_2': 2, 'lol': 'insert text', 'kek': 'insert the second text', 'number_3': 3}) == "ClassName(number_1=1, number_2=2, lol='insert text', kek='insert the second text', number_3=3)"


def test_args_and_kwargs():
    assert descript_data_object('ClassName', (1, 2, 3), {'lol': 1, 'kek': 2}) == 'ClassName(1, 2, 3, lol=1, kek=2)'
    assert descript_data_object('ClassName', (1, 2, 3), {'lol': 'insert text', 'kek': 'insert the second text'}) == "ClassName(1, 2, 3, lol='insert text', kek='insert the second text')"
    assert descript_data_object('ClassName', (1, 2, 3), {'number_1': 1, 'number_2': 2, 'lol': 'insert text', 'kek': 'insert the second text'}) == "ClassName(1, 2, 3, number_1=1, number_2=2, lol='insert text', kek='insert the second text')"
    assert descript_data_object('ClassName', (1, 2, 3), {'number_1': 1, 'number_2': 2, 'lol': 'insert text', 'kek': 'insert the second text', 'number_3': 3}) == "ClassName(1, 2, 3, number_1=1, number_2=2, lol='insert text', kek='insert the second text', number_3=3)"

    assert descript_data_object('ClassName', ('lol', 'kek'), {'lol': 1, 'kek': 2}) == "ClassName('lol', 'kek', lol=1, kek=2)"
    assert descript_data_object('ClassName', ('lol', 'kek'), {'lol': 'insert text', 'kek': 'insert the second text'}) == "ClassName('lol', 'kek', lol='insert text', kek='insert the second text')"
    assert descript_data_object('ClassName', ('lol', 'kek'), {'number_1': 1, 'number_2': 2, 'lol': 'insert text', 'kek': 'insert the second text'}) == "ClassName('lol', 'kek', number_1=1, number_2=2, lol='insert text', kek='insert the second text')"
    assert descript_data_object('ClassName', ('lol', 'kek'), {'number_1': 1, 'number_2': 2, 'lol': 'insert text', 'kek': 'insert the second text', 'number_3': 3}) == "ClassName('lol', 'kek', number_1=1, number_2=2, lol='insert text', kek='insert the second text', number_3=3)"

    assert descript_data_object('ClassName', ('lol', 1, 2, 3), {'lol': 1, 'kek': 2}) == "ClassName('lol', 1, 2, 3, lol=1, kek=2)"
    assert descript_data_object('ClassName', ('lol', 1, 2, 3), {'lol': 'insert text', 'kek': 'insert the second text'}) == "ClassName('lol', 1, 2, 3, lol='insert text', kek='insert the second text')"
    assert descript_data_object('ClassName', ('lol', 1, 2, 3), {'number_1': 1, 'number_2': 2, 'lol': 'insert text', 'kek': 'insert the second text'}) == "ClassName('lol', 1, 2, 3, number_1=1, number_2=2, lol='insert text', kek='insert the second text')"
    assert descript_data_object('ClassName', ('lol', 1, 2, 3), {'number_1': 1, 'number_2': 2, 'lol': 'insert text', 'kek': 'insert the second text', 'number_3': 3}) == "ClassName('lol', 1, 2, 3, number_1=1, number_2=2, lol='insert text', kek='insert the second text', number_3=3)"

    assert descript_data_object('ClassName', ('lol', 1, 2, 3, 'kek'), {'lol': 1, 'kek': 2}) == "ClassName('lol', 1, 2, 3, 'kek', lol=1, kek=2)"
    assert descript_data_object('ClassName', ('lol', 1, 2, 3, 'kek'), {'lol': 'insert text', 'kek': 'insert the second text'}) == "ClassName('lol', 1, 2, 3, 'kek', lol='insert text', kek='insert the second text')"
    assert descript_data_object('ClassName', ('lol', 1, 2, 3, 'kek'), {'number_1': 1, 'number_2': 2, 'lol': 'insert text', 'kek': 'insert the second text'}) == "ClassName('lol', 1, 2, 3, 'kek', number_1=1, number_2=2, lol='insert text', kek='insert the second text')"
    assert descript_data_object('ClassName', ('lol', 1, 2, 3, 'kek'), {'number_1': 1, 'number_2': 2, 'lol': 'insert text', 'kek': 'insert the second text', 'number_3': 3}) == "ClassName('lol', 1, 2, 3, 'kek', number_1=1, number_2=2, lol='insert text', kek='insert the second text', number_3=3)"

    assert descript_data_object('ClassName', ('lol', 1, 2, 3, 'kek', None), {'lol': 1, 'kek': 2}) == "ClassName('lol', 1, 2, 3, 'kek', None, lol=1, kek=2)"
    assert descript_data_object('ClassName', ('lol', 1, 2, 3, 'kek', None), {'lol': 'insert text', 'kek': 'insert the second text'}) == "ClassName('lol', 1, 2, 3, 'kek', None, lol='insert text', kek='insert the second text')"
    assert descript_data_object('ClassName', ('lol', 1, 2, 3, 'kek', None), {'number_1': 1, 'number_2': 2, 'lol': 'insert text', 'kek': 'insert the second text'}) == "ClassName('lol', 1, 2, 3, 'kek', None, number_1=1, number_2=2, lol='insert text', kek='insert the second text')"
    assert descript_data_object('ClassName', ('lol', 1, 2, 3, 'kek', None), {'number_1': 1, 'number_2': 2, 'lol': 'insert text', 'kek': 'insert the second text', 'number_3': 3}) == "ClassName('lol', 1, 2, 3, 'kek', None, number_1=1, number_2=2, lol='insert text', kek='insert the second text', number_3=3)"


def test_set_serializator_for_args():
    assert descript_data_object('ClassName', (1, 2, 3), {}, serializator=lambda x: f'{x}{x}') == 'ClassName(11, 22, 33)'
    assert descript_data_object('ClassName', (1, 2), {}, serializator=lambda x: f'{x}{x}') == 'ClassName(11, 22)'
    assert descript_data_object('ClassName', (1,), {}, serializator=lambda x: f'{x}{x}') == 'ClassName(11)'

    assert descript_data_object('ClassName', ('lol', 'kek'), {}, serializator=lambda x: f'{x}{x}') == 'ClassName(lollol, kekkek)'
    assert descript_data_object('ClassName', ('lol',), {}, serializator=lambda x: f'{x}{x}') == 'ClassName(lollol)'

    assert descript_data_object('ClassName', ('lol', 1, 2, 3), {}, serializator=lambda x: f'{x}{x}') == 'ClassName(lollol, 11, 22, 33)'
    assert descript_data_object('ClassName', ('lol', 1, 2, 3, 'kek'), {}, serializator=lambda x: f'{x}{x}') == 'ClassName(lollol, 11, 22, 33, kekkek)'
    assert descript_data_object('ClassName', ('lol', 1, 2, 3, 'kek', None), {}, serializator=lambda x: f'{x}{x}') == 'ClassName(lollol, 11, 22, 33, kekkek, NoneNone)'


def test_set_serializator_for_kwargs():
    assert descript_data_object('ClassName', (), {'lol': 1, 'kek': 2}, serializator=lambda x: f'{x}{x}') == 'ClassName(lol=11, kek=22)'

    assert descript_data_object('ClassName', (), {'lol': 'insert text', 'kek': 'insert the second text'}, serializator=lambda x: f'{x}{x}') == 'ClassName(lol=insert textinsert text, kek=insert the second textinsert the second text)'

    assert descript_data_object('ClassName', (), {'number_1': 1, 'number_2': 2, 'lol': 'insert text', 'kek': 'insert the second text'}, serializator=lambda x: f'{x}{x}') == 'ClassName(number_1=11, number_2=22, lol=insert textinsert text, kek=insert the second textinsert the second text)'
    assert descript_data_object('ClassName', (), {'number_1': 1, 'number_2': 2, 'lol': 'insert text', 'kek': 'insert the second text', 'number_3': 3}, serializator=lambda x: f'{x}{x}') == 'ClassName(number_1=11, number_2=22, lol=insert textinsert text, kek=insert the second textinsert the second text, number_3=33)'


def test_set_empty_filters_dict_for_args():
    assert descript_data_object('ClassName', (1, 2, 3), {}, filters={}) == 'ClassName(1, 2, 3)'
    assert descript_data_object('ClassName', (1, 2), {}, filters={}) == 'ClassName(1, 2)'
    assert descript_data_object('ClassName', (1,), {}, filters={}) == 'ClassName(1)'

    assert descript_data_object('ClassName', ('lol', 'kek'), {}, filters={}) == "ClassName('lol', 'kek')"
    assert descript_data_object('ClassName', ('lol',), {}, filters={}) == "ClassName('lol')"

    assert descript_data_object('ClassName', ('lol', 1, 2, 3), {}, filters={}) == "ClassName('lol', 1, 2, 3)"
    assert descript_data_object('ClassName', ('lol', 1, 2, 3, 'kek'), {}, filters={}) == "ClassName('lol', 1, 2, 3, 'kek')"
    assert descript_data_object('ClassName', ('lol', 1, 2, 3, 'kek', None), {}, filters={}) == "ClassName('lol', 1, 2, 3, 'kek', None)"


def test_set_filters_dict_with_empty_lambdas_for_args():
    all = lambda x: True

    assert descript_data_object('ClassName', (1, 2, 3), {}, filters={0: all, 1: all, 2: all}) == 'ClassName(1, 2, 3)'
    assert descript_data_object('ClassName', (1, 2), {}, filters={0: all, 1: all}) == 'ClassName(1, 2)'
    assert descript_data_object('ClassName', (1,), {}, filters={0: all}) == 'ClassName(1)'

    assert descript_data_object('ClassName', ('lol', 'kek'), {}, filters={0: all, 1: all}) == "ClassName('lol', 'kek')"
    assert descript_data_object('ClassName', ('lol',), {}, filters={0: all}) == "ClassName('lol')"

    assert descript_data_object('ClassName', ('lol', 1, 2, 3), {}, filters={0: all, 1: all, 2: all}) == "ClassName('lol', 1, 2, 3)"
    assert descript_data_object('ClassName', ('lol', 1, 2, 3, 'kek'), {}, filters={0: all, 1: all, 2: all, 3: all}) == "ClassName('lol', 1, 2, 3, 'kek')"
    assert descript_data_object('ClassName', ('lol', 1, 2, 3, 'kek', None), {}, filters={0: all, 1: all, 2: all, 3: all, 4: all}) == "ClassName('lol', 1, 2, 3, 'kek', None)"



def test_set_real_filters_for_args():
    not_all = lambda x: False

    assert descript_data_object('ClassName', (1, 2, 3), {}, filters={0: not_all, 1: not_all, 2: not_all}) == 'ClassName()'
    assert descript_data_object('ClassName', (1,), {}, filters={0: not_all}) == 'ClassName()'
    assert descript_data_object('ClassName', ('lol', 'kek'), {}, filters={0: not_all, 1: not_all}) == "ClassName()"
    assert descript_data_object('ClassName', ('lol',), {}, filters={0: not_all}) == "ClassName()"

    assert descript_data_object('ClassName', (1, 2, 3), {}, filters={0: not_all}) == 'ClassName(2, 3)'
    assert descript_data_object('ClassName', (1, 2, 3), {}, filters={2: not_all}) == 'ClassName(1, 2)'
    assert descript_data_object('ClassName', (1, 2, 3), {}, filters={1: not_all}) == 'ClassName(1, 3)'
    assert descript_data_object('ClassName', (1, 2), {}, filters={0: not_all}) == 'ClassName(2)'
    assert descript_data_object('ClassName', (1, 2), {}, filters={1: not_all}) == 'ClassName(1)'
    assert descript_data_object('ClassName', (1, 2, 3), {}, filters={3: not_all}) == 'ClassName(1, 2, 3)'

    assert descript_data_object('ClassName', ('lol', 'kek'), {}, filters={0: not_all}) == "ClassName('kek')"
    assert descript_data_object('ClassName', ('lol', 'kek'), {}, filters={1: not_all}) == "ClassName('lol')"
    assert descript_data_object('ClassName', ('lol',), {}, filters={1: not_all}) == "ClassName('lol')"


def test_args_filters_are_getting_values():
    fields = []

    def add_to_fields(value: Any) -> bool:
        fields.append(value)
        return True

    assert descript_data_object('ClassName', ('lol', 1, 2, 3, 'kek', None), {}, filters={0: add_to_fields, 1: add_to_fields, 2: add_to_fields, 3: add_to_fields, 4: add_to_fields, 5: add_to_fields}) == "ClassName('lol', 1, 2, 3, 'kek', None)"

    assert fields == ['lol', 1, 2, 3, 'kek', None]


def test_kwargs_filters_are_getting_values():
    fields = []

    def add_to_fields(value: Any) -> bool:
        fields.append(value)
        return True

    assert descript_data_object('ClassName', (), {'lol': 'kek', 'kek': 'lol'}, filters={'lol': add_to_fields, 'kek': add_to_fields}) == "ClassName(lol='kek', kek='lol')"

    assert fields == ['kek', 'lol']































def test_set_empty_filters_dict_for_kwargs():
    assert descript_data_object('ClassName', (), {'lol': 1, 'kek': 2}, filters={}) == 'ClassName(lol=1, kek=2)'

    assert descript_data_object('ClassName', (), {'lol': 'insert text', 'kek': 'insert the second text'}, filters={}) == "ClassName(lol='insert text', kek='insert the second text')"

    assert descript_data_object('ClassName', (), {'number_1': 1, 'number_2': 2, 'lol': 'insert text', 'kek': 'insert the second text'}, filters={}) == "ClassName(number_1=1, number_2=2, lol='insert text', kek='insert the second text')"
    assert descript_data_object('ClassName', (), {'number_1': 1, 'number_2': 2, 'lol': 'insert text', 'kek': 'insert the second text', 'number_3': 3}, filters={}) == "ClassName(number_1=1, number_2=2, lol='insert text', kek='insert the second text', number_3=3)"



def test_set_filters_dict_with_empty_lambdas_for_kwargs():
    all = lambda x: True

    assert descript_data_object('ClassName', (), {'lol': 1, 'kek': 2}, filters={'lol': all, 'kek': all}) == 'ClassName(lol=1, kek=2)'

    assert descript_data_object('ClassName', (), {'lol': 'insert text', 'kek': 'insert the second text'}, filters={'lol': all, 'kek': all}) == "ClassName(lol='insert text', kek='insert the second text')"

    assert descript_data_object('ClassName', (), {'number_1': 1, 'number_2': 2, 'lol': 'insert text', 'kek': 'insert the second text'}, filters={'lol': all, 'kek': all}) == "ClassName(number_1=1, number_2=2, lol='insert text', kek='insert the second text')"
    assert descript_data_object('ClassName', (), {'number_1': 1, 'number_2': 2, 'lol': 'insert text', 'kek': 'insert the second text', 'number_3': 3}, filters={'lol': all, 'kek': all}) == "ClassName(number_1=1, number_2=2, lol='insert text', kek='insert the second text', number_3=3)"


def test_set_real_filters_for_kwargs():
    not_all = lambda x: False

    assert descript_data_object('ClassName', (), {'lol': 1, 'kek': 2}, filters={'lol': not_all, 'kek': not_all}) == 'ClassName()'
    assert descript_data_object('ClassName', (), {'lol': 1, 'kek': 2}, filters={'lol': not_all}) == 'ClassName(kek=2)'
    assert descript_data_object('ClassName', (), {'lol': 1, 'kek': 2}, filters={'kek': not_all}) == 'ClassName(lol=1)'


def test_set_real_filters_for_args_and_kwargs():
    not_all = lambda x: False

    assert descript_data_object('ClassName', (1, 2), {'lol': 1, 'kek': 2}, filters={'lol': not_all, 'kek': not_all, 0: not_all, 1: not_all}) == 'ClassName()'
