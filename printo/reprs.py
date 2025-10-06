from this import s
from typing import Any
from inspect import isfunction


def superrepr(value: Any) -> str:
    if isfunction(value):
        if hasattr(value, '__name__'):
            result = value.__name__

            if result == '<lambda>':
                return 'λ'

            return result

    return repr(value)
