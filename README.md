# printo: print objects with data beautifully

[![Downloads](https://static.pepy.tech/badge/printo/month)](https://pepy.tech/project/printo)
[![Downloads](https://static.pepy.tech/badge/printo)](https://pepy.tech/project/printo)
[![codecov](https://codecov.io/gh/pomponchik/printo/graph/badge.svg?token=r72d56t1hj)](https://codecov.io/gh/pomponchik/printo)
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
# > MyClassName(1, 2, "some text", variable_name=1, second_variable_name="kek")
```
