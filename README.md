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

There is an implicit agreement among pythonists to create special [`__repr__`](https://docs.python.org/3/reference/datamodel.html#object.__repr__) methods for classes that return text as similar as possible to the piece of code where the specific object was constructed. `__repr__` of `1` returns "1", and repr of `None` returns "None". With this library, you can create your own classes, the objects of which will obey this rule.


## Table of contents

- [**Installation**](#installation)
- [**Basic usage**](#basic-usage)
- [**Filtering**](#filtering)
- [**Custom display of objects**](#custom-display-of-objects)
- [**Placeholders**](#placeholders)


## Installation

You can install [`dirstree`](https://pypi.python.org/pypi/printo) using pip:

```bash
pip install printo
```

You can also quickly try out this and other packages without having to install using [instld](https://github.com/pomponchik/instld).


## Basic usage

The main function in this library is `descript_data_object`, it returns a string representing what your object's initialization code should look like. There are 3 required positional parameters:

- The name of the class for which we are creating a representation.
- A `list` or `tuple` of positional arguments.
- A `dict` with named arguments, where the keys are the names of the arguments, and the values are any objects.

Here's a simple example of how it works:

```python
from printo import descript_data_object

print(descript_data_object('MyClassName', (1, 2, 'some text'), {'variable_name': 1, 'second_variable_name': 'kek'}))
#> MyClassName(1, 2, 'some text', variable_name=1, second_variable_name='kek')
```


## Filtering

You can prevent individual fields from being displayed. To do this, pass a `dict` as the `filters` parameter, in which the argument numbers (counting starts from 0) for positional arguments or the argument names for named arguments will be used as keys, and returning `bool` functions (each of them answers the question "whether to display this argument", where `True` means "yes" and `False` means "no") will be used as values:

```python
print(descript_data_object('MyClassName', (1, 2, 'some text'), {'variable_name': 1, 'second_variable_name': 'kek'}, filters={1: lambda x: False if x == 2 else True, 'second_variable_name': lambda x: False}))
#> MyClassName(1, 'some text', variable_name=1)
```

You can also save a few characters by specifying a function as a filter that automatically filters `None` of the values:

```python
from printo import not_none

print(descript_data_object('MyClassName', (1, None), {}, filters={1: not_none}))
#> MyClassName(1)
```


## Custom display of objects

By default, all your objects are serialized in the same way as the standard [`repr`](https://docs.python.org/3/library/functions.html#repr) function does. There are only 2 exceptions:

- Ordinary functions, in their case, instead of the usual text, just the function name is displayed.
- Lambda functions, just the `λ` symbol is displayed instead. This is done because there is no reliable way to display the source code of a lambda function in Python.

You can use your own function as a repr for all your objects, use the `serializator` parameter for this:

```python
print(
    descript_data_object(
        'MyClassName',
        (1, 2, 'lol'),
        {'variable_name': 1, 'second_variable_name': 'kek'},
        serializator=lambda x: repr(x * 2),
    )
)
#> MyClassName(2, 4, 'lollol', variable_name=2, second_variable_name='kekkek')
```


## Placeholders

For individual fields, you can pass predefined strings that will be displayed instead of the actual values. This can be useful, for example, to hide the values of secret fields when serializing objects.

Use the `placeholders` parameter for this by passing a dictionary there, where the keys are parameter names (for named parameters) or their numbers (for positional parameters, numbering starts from 0), and the values are strings:

```python
print(
    descript_data_object(
        'MySuperClass',
        (1, 2, 'lol'),
        {'variable_name': 1, 'second_variable_name': 'kek'},
        placeholders={
            1: '***',
            'variable_name': '***',
        },
    )
)
#> MySuperClass(1, ***, 'lol', variable_name=***, second_variable_name='kek')
```

> 🤓 Please note that if you set a placeholder for a parameter, a [custom serializer](#custom-display-of-objects) will no longer be applied to it.
