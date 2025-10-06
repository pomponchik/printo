![logo](https://raw.githubusercontent.com/pomponchik/printo/develop/docs/assets/logo_1.svg)

[![Downloads](https://static.pepy.tech/badge/printo/month)](https://pepy.tech/project/printo)
[![Downloads](https://static.pepy.tech/badge/printo)](https://pepy.tech/project/printo)
[![Coverage Status](https://coveralls.io/repos/github/pomponchik/printo/badge.svg?branch=main)](https://coveralls.io/github/pomponchik/printo?branch=main)
[![Lines of code](https://sloc.xyz/github/pomponchik/printo/?category=code)](https://github.com/boyter/scc/)
[![Hits-of-Code](https://hitsofcode.com/github/pomponchik/printo?branch=main)](https://hitsofcode.com/github/pomponchik/printo/view?branch=main)
[![Test-Package](https://github.com/pomponchik/printo/actions/workflows/tests_and_coverage.yml/badge.svg)](https://github.com/pomponchik/printo/actions/workflows/tests_and_coverage.yml)
[![Python versions](https://img.shields.io/pypi/pyversions/printo.svg)](https://pypi.python.org/pypi/printo)
[![PyPI version](https://badge.fury.io/py/printo.svg)](https://badge.fury.io/py/printo)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)


A mini library for writing beautiful [`__repr__`](https://docs.python.org/3/reference/datamodel.html#object.__repr__) for your classes.

Install it:

```bash
pip install printo
```

And use:

```python
from printo import descript_data_object

print(descript_data_object('MyClassName', (1, 2, 'some text'), {'variable_name': 1, 'second_variable_name': 'kek'}))
# > MyClassName(1, 2, 'some text', variable_name=1, second_variable_name='kek')
```

You can prevent individual fields from being displayed. To do this, pass a `dict` as the `filters` parameter, in which the argument numbers (counting starts from 0) for positional arguments or the argument names for named arguments will be used as keys, and returning `bool` functions (each of them answers the question "whether to display this argument", where `True` means "yes" and `False` means "no") will be used as values:

```python
print(descript_data_object('MyClassName', (1, 2, 'some text'), {'variable_name': 1, 'second_variable_name': 'kek'}, filters={1: lambda x: False if x == 2 else True, 'second_variable_name': lambda x: False}))
# > MyClassName(1, 'some text', variable_name=1)
```

You can also save a few characters by specifying a function as a filter that automatically filters `None` of the values:

```python
from printo import not_none

print(descript_data_object('MyClassName', (1, None), {}, filters={1: not_none}))
# > MyClassName(1)
```
